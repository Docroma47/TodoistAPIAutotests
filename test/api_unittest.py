import unittest

from todoist import TodoistAPI

class Todoist(unittest.TestCase):
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

        self.api.commit()

    def test_create_project(self):
        name = str('CREATE API PROJECT')
        self.api.projects.add(name)

        found = False
        for project in self.api.projects.all():
            if project["name"] == name:
                found = True
                break
        assert found, "Project not found"


    def test_create_task(self):
        task = str('Task-1-No-Data')
        project = self.api.projects.add('CREATE API PROJECT')
        self.api.items.add('Task-1-No-Data', project_id=project['id'])

        found = False
        for items in self.api.items.all():
            if items["content"] == task:
                found = True
                break
        assert found, "Task not found"

    def test_create_task_with_datetime(self):
        date = str('2020-07-18T07:00:00Z')
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
            if items[i]['due']['date'] == date:
                found = True
                break
        assert found, "Task with date not found"


    def test_create_subtask_(self):
        project = self.api.projects.add("CREATE API PROJECT")
        task_1 = self.api.items.add('Task-1-No-Data', project_id=project['id'])
        task_2 = self.api.items.add('SUB-Task', project_id=project['id'], due={'date': '2020-07-17T23:00:00Z'})
        task_2.move(parent_id=task_1['id'])

        found = False
        for items in self.api.items.all():
            if items["content"] == 'Task-1-No-Data':
                found = True
                break
        assert found, "Task not found"

        found = False
        for items in self.api.items.all():
            if items["content"] == 'SUB-Task':
                found = True
                break
        assert found, "Subtask with date not found"
