*** Settings ***
Documentation    Suite description
Library          todoist_selenium_library.RobotUILibrary

Test Setup       Set UP
Test Teardown    Tear Down
*** Test Cases ***
Create Project
    When Create Project   Roman's create project
    Then Assert Project With Name Exists   Roman's create project
Crate Task
    When Create Task   Roman's create project   Roman's create task
    Then Assert Task With Name Exists   Roman's create task
Create task with date and time
    When Create Task With Date And Time   Roman's create project   Roman's create task   12 июль 2020 20:20
    Then Assert Task With Due Date Exist   Roman's create task   12 июль 20:20