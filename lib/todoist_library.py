from todoist import TodoistAPI

class TodoistLibrary:
    api: TodoistAPI

    def todoist_api_client_is_connected(self):
        self.api = TodoistAPI('313f6bf203b35e7ac56e39561a80633e459c9c54')
        self.api.sync()

    def create_new_project_with_name(self, name: str):
        self.api.projects.add(name)

    def delete_project(self, name):
        def flt(project):
            return project["name"] == name
        for project in self.api.projects.all(filt=flt):
            self.api.projects.delete(project["id"])

    def test_clean_up(self):
        self.delete_project("Roma's Project")
        self.api.commit()

    def commit(self):
        self.api.commit()

    def assert_project_exists(self, name):
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