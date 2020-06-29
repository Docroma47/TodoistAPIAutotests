from todoist import TodoistAPI

class TodoistLibrary:
    api: TodoistAPI

    ### Test Setup ###
    def todoist_api_client_is_connected(self):
        self.api = TodoistAPI('313f6bf203b35e7ac56e39561a80633e459c9c54')
        self.api.sync()

    ### Test Teardown ###
    def test_clean_up(self):
        self.delete_project("Roma's Project")
        self.api.commit()

    ### Общие функции ###
    def commit_and_sync(self):
        self.api.commit()
        self.api.sync()

    def delete_project(self, name):
        def flt(project):
            return project["name"] == name
        for project in self.api.projects.all(filt=flt):
            self.api.projects.delete(project["id"])

    ### Функции создания и добавления проектов и задач ###
    def create_new_project_with_name(self, name: str):
        self.api.projects.add(name)

    def create_new_task_with_name(self, name_project: str, name_task: str):
        project = self.api.projects.add(name_project)
        self.api.items.add(name_task, project_id=project['id'])

    def create_new_task_with_datetime_with_name(self, name_project: str, name_task: str):
        project = self.api.projects.add(name_project)
        self.api.items.add(name_task, project_id=project['id'], due={'date': '2020-07-18T07:00:00Z'})

    def create_new_task_and_subtask_with_name(self, name_project: str, name_task: str, name_subtask: str):
        project = self.api.projects.add(name_project)
        task_id = self.api.items.add(name_task, project_id=project['id'], due={'date': '2020-07-18T07:00:00Z'})
        subtask = self.api.items.add(name_subtask, project_id=project['id'], due={'date': '2020-07-18T05:00:00Z'})
        subtask.move(parent_id=task_id['id'])

    def create_new_project_and_add_comment(self, name_project, name_task):
        project = self.api.projects.add(name_project)
        task_id = self.api.items.add(name_task, project_id=project['id'], due={'date': '2020-07-18T07:00:00Z'})
        self.api.notes.add(task_id['id'], 'Comment3')

    def create_invalid_parent_project_and_child_project(self, name, parent_id: int):
        self.api.projects.add(name, parent_id)

    def create_valid_parent_project_and_child_project(self, parent: str, child: str):
        parent_project = self.api.projects.add(parent)
        self.api.projects.add(child, parent_id=parent_project["id"])

    def create_empty_name_project(self):
        self.api.projects.add("")

    def create_new_task_with_name_and_priority(self, name, priority: int):
        self.api.projects.add(name)
        self.api.items.add(name, priority=priority)

    def commit_and_expect_error(self, error_code, error):
        try:
            self.api.commit()
            assert False
        except Exception as ex:
            if ex.args[1]['error_code'] != error_code:
                assert False
            if ex.args[1]['error'] != error:
                assert False

    ### Assert для проверки результатов ###
    def project_with_name_exists(self, name):
        found = False
        for project in self.api.projects.all():
            if project["name"] == name:
                found = True
                break
        assert found, "Project not found"

    def assert_task_exists(self, name):
        found = False
        for items in self.api.items.all():
            if items["content"] == name:
                found = True
                break
        assert found, "Task not found"

    def assert_task_with_datetime_exists(self, task_name, task_date):
        found = False
        for items in self.api.items.all():
            if items["content"] == task_name:
                found = True
                break
        assert found, "Task not found"

        range_items = len(self.api.items.all())
        items = self.api.items.all()
        found = False
        for i in range(range_items):
            if items[i]['due']['date'] == task_date:
                found = True
                break
        assert found, "Task with date not found"

    def assert_task_with_subtask_exists(self, name, subtask):
        found = False
        for items in self.api.items.all():
            if items["content"] == name:
                found = True
                break
        assert found, "Task not found"

        found = False
        for items in self.api.items.all():
            if items["content"] == subtask:
                found = True
                break
        assert found, "Subtask with date not found"

    def commit_and_sync_expect_error_invalid_parent(self, error_code = None, error = None):
        try:
            self.api.commit()
            self.api.sync()
            assert False, "Project should not be created with invalid parent"
        except Exception as ex:
            assert False, "Project should not be created with invalid parent"

    def child_project_with_parent_project_exists(self, parent, child):
        found = False
        for project in self.api.projects.all():
            if project["name"] == parent:
                found = True
                break
        assert found, "Project parent is not created"

        found = False
        for project in self.api.projects.all():
            if project["name"] == child:
                found = True
                break
        assert found, "Project child is not created"

    def commit_and_sync_expect_error(self, error_code: int, error: str):
        try:
            self.api.commit()
            self.api.sync()
            assert False
        except Exception as ex:
            if ex.args[1]['error_code'] != error_code:
                assert False
            if ex.args[1]['error'] != error:
                assert False

    def assert_commit_create_empty_name_project_expect_error(self):
        try:
            self.api.commit()
            assert False, "Project should not be created with invalid name"
        except Exception as ex:
            assert False, "Project should not be created with invalid name"

    def commit_and_sync_create_long_name_project_expect_error(self):
        try:
            self.api.commit()
            self.api.sync()
            assert False, "Project should not be created with invalid long name"
        except Exception as ex:
            assert False, "Project should not be created with invalid long name"

