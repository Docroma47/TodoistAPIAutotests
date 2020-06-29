*** Settings ***
Library            todoist_library.TodoistLibrary

Test Setup       Todoist Api Client Is Connected
Test Teardown    Test Clean Up
*** Test Cases ***
Create Project
    When Create New Project With Name  Roma's Project
    And Commit
    Then Assert Project Exists  Roma's Project

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