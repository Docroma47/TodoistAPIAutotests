*** Settings ***
Library            todoist_library.TodoistLibrary

Test Setup       Todoist Api Client Is Connected
Test Teardown    Test Clean Up
*** Test Cases ***

### Project test cases ###
### Positive cases ###
Create Project
    When Create Project With Name  Roma's Project
    And Commit And Sync
    Then Assert Project With Name Exists  Roma's Project
Create parent project and child project
    When Create Parent Project And Child Project    Roma's parent project    Roma's child project
    And Commit And Sync
    Then Assert Project With Name Exists  Roma's parent project
    And Assert Project With Name Exists  Roma's child project
    And Assert Project Is Parent Of Another Project  Roma's parent project  Roma's child project

### Negative cases ###
Create project with invalid parent id
    When Create Project With Name And Parent Id   Roma's project   345345345345345
    Then Commit And Sync Expect Error   Invalid parent projecrt
# Boundary-value analysis: project name should be not empty and be less than 120 characters
Create project with empty name
    When Create Project With Name
    Then Commit And Sync Expect Error  Empty project name
Create project with long name
    When Create Project With Name  sdsadasdasdasdasdasdddddddddddddddddddddddddddddddddddddddddddddddddddasddddddddddddasdasdasdasdsdadsasdassdasdasasddddsd
    Then Commit And Sync Expect Error   Project is too long

### Tasks test cases ###
### Positive cases ###
Create task
    When Create Task With Name  Roma's Project    Task-1-No-Data
    And Commit And Sync
    Then Assert Task Exists  Task-1-No-Data
Create task with date and time
    When Create Task With Name And Due Date  Roma's Project    Task-1-Yes-Datetime   2020-07-18T07:00:00Z
    And Commit And Sync
    Then Assert Task Has Due Date  Task-1-Yes-Datetime    2020-07-18T07:00:00Z
Create subtask
    When Create Task And Subtask With Name  Roma's Project    Task-For-Subtask    Subtask
    And Commit And Sync
    Then Assert Task With Subtask Exists  Task-For-Subtask    Subtask
# Boundary-value analysis and equivalent classes: priority should be between 1 - 4
Create task with valid priority - lower bound
    When Create Task With Name And Priority  Roma's Project   Task-1-Priority   1
    And Commit And Sync
    Then Assert Task Exists  Task-1-Priority
    And Task Has Priority  Task-1-Priority   1
Create task with valid priority - upper bound
    When Create Task With Name And Priority  Roma's Project   Task-1-Priority   4
    And Commit And Sync
    Then Assert Task Exists  Task-1-Priority
    And Task Has Priority  Task-1-Priority   4
### Negative cases ###
# Boundary-value analysis and equivalent classes: priority should be between 1 - 4
Create task with invalid priority - lower bound
    When Create Task With Name And Priority  Roma's Project   Task-1-Priority   0
    Then Commit And Sync Expect Error  Invalid priority
Create task with invalid priority - upper bound
    When Create Task With Name And Priority  Roma's Project   Task-1-Priority   5
    Then Commit And Sync Expect Error  Invalid priority

### Comments test cases ###
### Negative cases ###
Create project and add commet
    When Create Project And Add Comment  Roma's Project    Task-For-Subtask
    Then Assert Commit And Expect Error  32    Premium only feature
