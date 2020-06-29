# Todoist API Test
This project is a demonstration of Robot framework and Todoist API using Todoist website.

The following features have been tested:
* Create project
* Create task
* Create task with date and time
* Create subtask
* Add comment
* Positive and negative scenarios
* Boundary value analysis and equivalence

The following test types have been implemented:
- UI Test using selenium  ```test\unittest_project.py```
- API unittest (used for getting to know Todois API) ```test\api_unittest.py```
- API tests using Robot Framework ```test\robot_test.robot```


### Installation:
```
git clone git@github.com:Docroma47/TodoistAutotests.git
cd TodoistAutotests
pip install -r requirements.txt
``` 

requirements: [selenium; todoist-python; webdriver-manager; webdrivermanager; robotframework-seleniumlibrary]

### Running Test

*IMPORTANT*, please note: 

Some API tests (robot tests) are failing for the following reasons (possibly bugs in the API):

* Create project with invalid parent id - (normal severity) Web Application does not accept project name that 
  is longer than 120 characters (Create project with empty name), so I assumed that the API should also reject lengthy names

* Create task with valid priority - lower bound - (normal severity) The API documentation 
[states](https://developer.todoist.com/sync/v8/#add-an-item) that task priority should be between 1 and 4,
so I assumed that the API should also reject priority values that are outside of the valid range

* Create project with invalid parent id - (critical severity) The API allows to create a subtask with parent ID which does not exist

#### API unittest: 
``` sh run/run_api_unittests.sh ```
#### UI/Selenium tests: 
``` sh run/run_selenium_tests.sh ```
#### API Robot tests: 
``` sh run/run.sh ```
