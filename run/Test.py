from Tests import CreateProjectTest

def createTask():
    CreateProjectTest.LoginProfile().Login()
    CreateProjectTest.CreateProject().create()
    CreateProjectTest.CreateTask().createTask()


def createProject():
    CreateProjectTest.LoginProfile().Login()
    CreateProjectTest.CreateProject().create()


def createTaskWithDate():
    CreateProjectTest.LoginProfile().Login()
    CreateProjectTest.CreateProject().create()
    CreateProjectTest.CreateTaskWithDate().createTaskWithDate()


def createSubtask():
    CreateProjectTest.LoginProfile().Login()
    CreateProjectTest.CreateProject().create()
    CreateProjectTest.CreateTask().createTask()
    CreateProjectTest.CreateSubtask().createSubtask()


def addComment():
    CreateProjectTest.LoginProfile().Login()
    CreateProjectTest.CreateProject().create()
    CreateProjectTest.AddComment().createSubtask()

if __name__ == '__main__':
    createProject()
    createTask()
    createTaskWithDate()
    createSubtask()
    addComment()