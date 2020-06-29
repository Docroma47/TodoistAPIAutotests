import unittest

from todoist import TodoistAPI
from todoist.api import SyncError


class Todoist_API_Test(unittest.TestCase):
    api: TodoistAPI

    @classmethod
    def setUp(cls):
        cls.api = TodoistAPI('313f6bf203b35e7ac56e39561a80633e459c9c54')
        cls.api.sync()

    @classmethod
    def tearDown(cls):
        def flt(project):
            return project["name"] == "CREATE API PROJECT"
        for project in cls.api.projects.all(filt=flt):
            cls.api.projects.delete(project["id"])
        cls.api.items.all().clear()
        cls.api.commit()

    def test_todoist_api_client_is_connected(self):
        project = self.api.projects.add("CREATE API PROJECT")
        self.api.items.add('Task-1-No-Data', project_id=project['id'])
        task_2 = self.api.items.add('Task-2-Yes-Data-And-Time', project_id=project['id'], due={'date': '2020-07-18T07:00:00Z'})
        task_3 = self.api.items.add('SUB-Task', project_id=project['id'], due={'date': '2020-07-17T23:00:00Z'})
        task_3.move(parent_id=task_2['id'])

    def test_create_project(self):
        self.api.projects.add('CREATE API PROJECT')

        found = False
        for project in self.api.projects.all():
            if project["name"] == 'CREATE API PROJECT':
                found = True
                break
        assert found, "Project not found"

    def test_create_task(self):
        project = self.api.projects.add('CREATE API PROJECT')
        self.api.items.add('Task-1-No-Data', project_id=project['id'])

        found = False
        for items in self.api.items.all():
            if items["content"] == 'Task-1-No-Data':
                found = True
                break
        assert found, "Task not found"

    def test_create_task_with_datetime(self):
        project = self.api.projects.add('CREATE API PROJECT')
        self.api.items.add('Task-2-Yes-Data-And-Time', project_id=project['id'], due={'date': '2020-07-18T07:00:00Z'})

        found = False
        for items in self.api.items.all():
            if items["content"] == 'Task-2-Yes-Data-And-Time':
                found = True
                break
        assert found, "Task not found"

        range_items = len(self.api.items.all())
        items = self.api.items.all()
        found = False
        for i in range(range_items):
            if items[i]['due']['date'] == '2020-07-18T07:00:00Z':
                found = True
                break
        assert found, "Task with date not found"

    def test_create_subtask(self):
        project = self.api.projects.add("New Project-Test")
        task_id = self.api.items.add("Task Name New", project_id=project['id'], due={'date': '2020-07-18T07:00:00Z'})
        subtask = self.api.items.add("SUB Task New", project_id=project['id'], due={'date': '2020-07-18T05:00:00Z'})
        subtask.move(parent_id=task_id['id'])
        self.api.sync()
        self.api.commit()

        parent_tasks = self.api.items.all(filt=lambda task: task["content"] == task_id["content"])
        assert len(parent_tasks) > 0, "Parent task could not be found"
        parent = parent_tasks[0]
        child_tasks = self.api.items.all(filt=lambda project: project["content"] == subtask["content"])
        assert len(child_tasks) > 0, "Child task could not be found"
        child = child_tasks[0]
        assert child["parent_id"] == parent['id'], "Task is not parent of another project"

    def test_create_project_task_comment_non_premium(self):
        project = self.api.projects.add("CREATE API PROJECT")
        task = self.api.items.add('Task-1-No-Data', project_id=project['id'])
        self.api.notes.add(task['id'], 'Comment3')

        try:
            self.api.commit()
            assert False
        except Exception as ex:
            self.assertEqual(ex.args[1]['error_code'], 32)
            self.assertEqual(ex.args[1]['error'], "Premium only feature")

    def test_project_parent_id_positive(self):
        parent_project = self.api.projects.add("Roma's Project parent valid")
        self.api.projects.add("Roma's Project child valid", parent_id=parent_project["id"])

        found = False
        for project in self.api.projects.all():
            if project["name"] == "Roma's Project parent valid":
                found = True
                break
        assert found, "Project parent is not created"

        found = False
        for project in self.api.projects.all():
            if project["name"] == "Roma's Project child valid":
                found = True
                break
        assert found, "Project child is not created"

    def test_project_parent_id_negative(self):
        try:
            self.api.commit()
            self.api.sync()
            assert False, "Server did not throw any error"
        except AssertionError as ae:
            raise ae
        except SyncError as ex:
            assert ex.args[1]['error'] == "Invalid parent project", "Wrong error message"
            if None is not None and ex.args[1]['error_code'] != None:
                assert False, "Wrong error code"
