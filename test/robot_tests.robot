*** Settings ***
### Библиотека с функциями использующиеся в robot Framefork ###
Library            todoist_library.TodoistLibrary

Test Setup       Todoist Api Client Is Connected
Test Teardown    Test Clean Up
*** Test Cases ***

### Позитивные тесты ###
### Create task - тест создающий таск ###
Create task - positive
    When Create New Task With Name  Roma's Project    Task-1-No-Data
    And Commit
    Then Assert Task Exists  Task-1-No-Data
### Create task with date and time - тест создающий таск с временем и датой ###
Create task with date and time - positive
    When Create New Task With Datetime With Name  Roma's Project    Task-1-Yes-Datetime
    And Commit
    Then Assert Task With Datetime Exists  Task-1-Yes-Datetime    2020-07-18T07:00:00Z
### Create task - тест создающий подзадачу к таску ###
Create subtask - positive
    When Create New Task And Subtask With Name  Roma's Project    Task-For-Subtask    Subtask
    And Commit
    Then Assert Task With Subtask Exists  Task-For-Subtask    Subtask
### Create project with parent id - тест создающий проект c параметром родительского элемента ###
Create project with parent id - positive
    When Create Project Parent Id Positive
    Then Assert Project With Parent Id Exists

### Негативные тесты ###
### Create project with parent id - тест создающий проект c параметром родительского элемента, тест должен падать ###
Create project with parent id - negative
    When Create Project Parent Id Negative
    Then Assert Commit Parent Id And Expect Error
### Create project and add commet - тест создающий проект и добавляющий комментарий, тест должен падать ###
Create project and add commet - negative
    When Create New Project And Add Comment  Roma's Project    Task-For-Subtask
    Then Assert Commit And Expect Error  32    Premium only feature

### Тесты эквивалентности и граничных значений ###
### Create Project - тест создающий проект ###
Create Project - positive
    When Create New Project With Name  Roma's Project
    And Commit
    Then Assert Project Exists  Roma's Project
### Create project with empty name - тест создающий проект c пустым именем, тест должен падать ###
Create project with empty name - negative
    When Create Empty Name Project
    Then Assert Commit Create Empty Name Project Expect Error
### Create project with empty name - тест создающий проект c длинным именем в 121 символ, тест должен падать ###
Create project with long name - negative
    When Create Project With Long Name
    Then Assert Commit Create Long Name Project Expect Error

### Тесты эквивалентности и граничных значений ###
### Create task with valid priority - тест создающий таск c минимальным приоритетом###
### Позитивные тесты ###
Create task with valid priority - lower bound
    When Create New Task With Name And Priority  Roma's Project   1
    And Commit
    Then Assert Task Exists  Task-1-No-Data
### Create task with valid priority - тест создающий таск c максимальным приоритетом###
Create task with valid priority - upper bound
    When Create New Task With Name And Priority  Roma's Project   4
    And Commit
    Then Assert Task Exists  Task-1-No-Data

### Негативные тесты ###
### Create task with invalid priority - тест создающий таск c минимальным приоритетом, тест должен падать###
Create task with invalid priority - lower bound
    When Create New Task With Name And Priority  Roma's Project   0
    Then Commit And Expect Error  20   Invalid priority
### Create task with invalid priority - тест создающий таск c максимальным приоритетом, тест должен падать###
Create task with invalid priority - upper bound
    When Create New Task With Name And Priority  Roma's Project   5
    Then Commit And Expect Error  20   Invalid priority