import unittest

from todoist import TodoistAPI

### Данные юнит-тесты использовались в изучении API Todoist и в дальнейшем я решил оставить их ###
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

    ### Простейший тест без проверки с созданием почти все нужной функциональности для задания ###
    def test_todoist_api_client_is_connected(self):
        project = self.api.projects.add("CREATE API PROJECT")
        self.api.items.add('Task-1-No-Data', project_id=project['id'])
        task_2 = self.api.items.add('Task-2-Yes-Data-And-Time', project_id=project['id'], due={'date': '2020-07-18T07:00:00Z'})
        task_3 = self.api.items.add('SUB-Task', project_id=project['id'], due={'date': '2020-07-17T23:00:00Z'})
        task_3.move(parent_id=task_2['id'])

    ### Юнит-тест создающий проект (с проверкой)###
    def test_create_project(self):
        self.api.projects.add('CREATE API PROJECT')

        found = False
        for project in self.api.projects.all():
            if project["name"] == 'CREATE API PROJECT':
                found = True
                break
        assert found, "Project not found"

    ### Юнит-тест создающий таск (с проверкой)###
    def test_create_task(self):
        project = self.api.projects.add('CREATE API PROJECT')
        self.api.items.add('Task-1-No-Data', project_id=project['id'])

        found = False
        for items in self.api.items.all():
            if items["content"] == 'Task-1-No-Data':
                found = True
                break
        assert found, "Task not found"

    ### Юнит-тест создающий таск с датой и временем (с проверкой)###
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

    ### Юнит-тест создающий подзадачу в таске (с проверкой)###
    def test_create_subtask(self):
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

    ### Юнит-тест создающий коммент в проекте, тест должен падать###
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

    ### Юнит-тест создающий проект и привязывающий его к родительскому ###
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

    ### Юнит-тест создающий проект и привязывающий его к родительскому, тест должен падать ###
    def test_project_parent_id_negative(self):
        try:
            self.api.projects.add(name="Roma's child Project parent invalid", parent_id=345345345345345)
            self.api.commit()
            assert False, "Project should not be created with invalid parent"
        except Exception as ex:
            assert False, "Project should not be created with invalid parent"

    ### Юнит-тест создающий проект с пустым именем, тест должен падать ###
    def test_equivalence_create_project(self):
        try:
            self.api.projects.add("")
            self.api.commit()
            assert False, "Project should not be created with invalid name"
        except Exception as ex:
            assert False, "Project should not be created with invalid name"