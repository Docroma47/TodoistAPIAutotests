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

#### Api unittest: 
``` sh run/run_api_unittests.sh ```
#### UI/Selenium tests: 
``` sh run/run_selenium_tests.sh ```
#### API Robot tests: 
``` sh run/run.sh ```
