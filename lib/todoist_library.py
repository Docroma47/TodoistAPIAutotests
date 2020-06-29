from todoist import TodoistAPI
from todoist.api import SyncError


class TodoistLibrary:
    api: TodoistAPI

    ### Test Setup ###
    def todoist_api_client_is_connected(self):
        self.api = TodoistAPI('313f6bf203b35e7ac56e39561a80633e459c9c54')
        self.api.sync()

    ### Test Teardown ###
    def test_clean_up(self):
        self.delete_project()
        self.api.commit()

    def commit_and_sync(self):
        self.api.commit()
        self.api.sync()

    def delete_project(self):
        for project in self.api.projects.all():
            self.api.projects.delete(project["id"])
        self.api.items.all().clear()

    def create_project_with_name(self, name: str = None):
        self.api.projects.add(name)

    def create_project_with_name_and_parent_id(self, name: str, parent_id: int = None):
        self.api.projects.add(name=name, parent_id=parent_id)

    def create_task_with_name(self, name_project: str, name_task: str):
        project = self.api.projects.add(name_project)
        self.api.items.add(name_task, project_id=project['id'])

    def create_task_with_name_and_due_date(self, name_project: str, name_task: str, due_date: str):
        project = self.api.projects.add(name_project)
        self.api.items.add(name_task, project_id=project['id'], due={'date': due_date})

    def create_task_and_subtask_with_name(self, name_project: str, name_task: str, name_subtask: str):
        project = self.api.projects.add(name_project)
        task_id = self.api.items.add(name_task, project_id=project['id'], due={'date': '2020-07-18T07:00:00Z'})
        subtask = self.api.items.add(name_subtask, project_id=project['id'], due={'date': '2020-07-18T05:00:00Z'})
        subtask.move(parent_id=task_id['id'])

    def create_project_and_add_comment(self, name_project, name_task):
        project = self.api.projects.add(name_project)
        task_id = self.api.items.add(name_task, project_id=project['id'], due={'date': '2020-07-18T07:00:00Z'})
        self.api.notes.add(task_id['id'], 'Comment3')

    def create_parent_project_and_child_project(self, parent: str, child: str):
        parent_project = self.api.projects.add(parent)
        self.api.projects.add(child, parent_id=parent_project["id"])

    def create_task_with_name_and_priority(self, name_project, task_name, priority: int):
        self.api.projects.add(name_project)
        self.api.items.add(task_name, priority=priority)

    def assert_project_with_name_exists(self, name_project):
        projects = self.api.projects.all(filt=lambda project: project['name'] == name_project)
        assert len(projects) > 0, "Project could not be found"
        project = projects[0]
        assert project['name'] == name_project, "Project is not created"

    def assert_task_exists(self, name_task):
        name_tasks = self.api.items.all(filt=lambda task: task['content'] == name_task)
        assert len(name_tasks) > 0, "Parent task could not be found"
        task = name_tasks[0]
        assert task['content'] == name_task, "Task is not created"


    def assert_task_has_due_date(self, task_name, due_date):
        tasks = self.api.items.all(filt=lambda task: task["content"] == task_name)
        assert len(tasks) > 0, "Parent task could not be found"
        task = tasks[0]
        assert task['due']['date'] == due_date, "Task due date is wrong"

    def assert_task_with_subtask_exists(self, parent_task, child_task):
        parent_tasks = self.api.items.all(filt=lambda task: task["content"] == parent_task)
        assert len(parent_tasks) > 0, "Parent task could not be found"
        parent = parent_tasks[0]
        child_tasks = self.api.items.all(filt=lambda project: project["content"] == child_task)
        assert len( child_tasks) > 0, "Child task could not be found"
        child = child_tasks[0]
        assert child["parent_id"] == parent['id'], "Task is not parent of another project"

    def assert_project_is_parent_of_another_project(self, parent, child):
        projects = self.api.projects.all(filt=lambda project: project["name"] == parent)
        assert len(projects) > 0, "Parent project could not be found"
        parent_project = projects[0]
        projects = self.api.projects.all(filt=lambda project: project["name"] == child)
        assert len(projects) > 0, "Child project could not be found"
        child_project = projects[0]
        assert child_project["parent_id"] == parent_project['id'], "Project is not parent of another project"

    def commit_and_sync_expect_error(self, error: str, error_code: int = None):
        try:
            self.api.commit()
            self.api.sync()
            assert False, "Server did not throw any error"
        except AssertionError as ae:
            raise ae
        except SyncError as ex:
            assert ex.args[1]['error'] == error, "Wrong error message"
            if error_code is not None and ex.args[1]['error_code'] != error_code:
                assert False, "Wrong error code"

    def task_has_priority(self, task_name, priority: int):
        tasks = self.api.items.all(filt=lambda task: task["content"] == task_name)
        assert len(tasks) > 0, "Task could not be found"
        task = tasks[0]
        assert task['priority'] == priority, "Task priority is wrong"

