*** Settings ***
Library            todoist_library.TodoistLibrary

Test Setup       Todoist Api Client Is Connected
Test Teardown    Test Clean Up
*** Test Cases ***

### Project test cases ###
### Positive cases ###
Create Project
    When Create New Project With Name  Roma's Project
    And Commit
    Then Assert Project Exists  Roma's Project
# Boundary-value analysis and equivalent classes
Create project with parent id
    When Create Project Parent Id Positive
    Then Assert Project With Parent Id Exists
### Negative cases ###
Create project with parent id
    When Create Project Parent Id Negative
    Then Assert Commit Parent Id And Expect Error
# Boundary-value analysis and equivalent classes
Create project with empty name
    When Create Empty Name Project
    Then Assert Commit Create Empty Name Project Expect Error
Create project with long name
    When Create Project With Long Name
    Then Assert Commit Create Long Name Project Expect Error

### Tasks test cases ###
### Positive cases ###
Create task
    When Create New Task With Name  Roma's Project    Task-1-No-Data
    And Commit
    Then Assert Task Exists  Task-1-No-Data
Create task with date and time
    When Create New Task With Datetime With Name  Roma's Project    Task-1-Yes-Datetime
    And Commit
    Then Assert Task With Datetime Exists  Task-1-Yes-Datetime    2020-07-18T07:00:00Z
Create subtask
    When Create New Task And Subtask With Name  Roma's Project    Task-For-Subtask    Subtask
    And Commit
    Then Assert Task With Subtask Exists  Task-For-Subtask    Subtask
# Boundary-value analysis and equivalent classes
Create task with valid priority - lower bound
    When Create New Task With Name And Priority  Roma's Project   1
    And Commit
    Then Assert Task Exists  Task-1-No-Data
Create task with valid priority - upper bound
    When Create New Task With Name And Priority  Roma's Project   4
    And Commit
    Then Assert Task Exists  Task-1-No-Data
### Negative cases ###
# Boundary-value analysis and equivalent classes
Create task with invalid priority - lower bound
    When Create New Task With Name And Priority  Roma's Project   0
    Then Commit And Expect Error  20   Invalid priority
Create task with invalid priority - upper bound
    When Create New Task With Name And Priority  Roma's Project   5
    Then Commit And Expect Error  20   Invalid priority

### Comments test cases ###
### Negative cases ###
Create project and add commet - negative
    When Create New Project And Add Comment  Roma's Project    Task-For-Subtask
    Then Assert Commit And Expect Error  32    Premium only feature
