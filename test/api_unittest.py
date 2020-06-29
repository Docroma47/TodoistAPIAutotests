import unittest

from todoist import TodoistAPI

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
        project = self.api.projects.add("CREATE API PROJECT")
        task_1 = self.api.items.add('Task-1-No-Data', project_id=project['id'])
        task_2 = self.api.items.add('SUB-Task', project_id=project['id'], due={'date': '2020-07-17T23:00:00Z'})
        task_2.move(parent_id=task_1['id'])
        print(task_1)
        print(task_2)

        parent_task = self.api.items.all(filt=lambda item: item["content"] == 'Task-1-No-Data')[0]
        assert parent_task is not None, "Parent task could not be found"
        print(parent_task['id'])
        child_task = self.api.items.all(filt=lambda item: item["content"] == 'SUB-Task')[0]
        assert child_task["parent_id"] == parent_task['id'], "Child task could not be found"

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
            self.api.projects.add(name="Roma's child Project parent invalid", parent_id=345345345345345)
            self.api.commit()
            assert False, "Project should not be created with invalid parent"
        except Exception as ex:
            assert False, "Project should not be created with invalid parent"

    def test_equivalence_create_project(self):
        try:
            self.api.projects.add("")
            self.api.commit()
            assert False, "Project should not be created with invalid name"
        except Exception as ex:
            assert False, "Project should not be created with invalid name"