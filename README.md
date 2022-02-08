 # jirc
![FOR](https://img.shields.io/badge/FOR-TERMINAR_DWELLERS-magenta?style=for-the-badge&logo=JIRA&logoColor=magenta)

![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=flat)
![Visual Studio Code Badge](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?logo=visualstudiocode&logoColor=fff&style=flat)

The aim of this code🎯 is to allow you to create a new JIRA card without leaving terminal. It also asks if you want to open the new card in the default browser. 
Note that you run this project as an executable directory. Set it as an alias for shell and you can start just throwing cards in the project with issue type selected from your shell. 

```
python jirc
```

### 1. demo


### config
* Initially, you need the 4 values from Jira

Value       | Location                                                    | Example
------------|-------------------------------------------------------------|----------------------------
Jira Server | Browser URL                                                 | `https://foo.atlassian.net`
User        | email address / jira account                                | `pkutaj@gmail.com`
Token       | https://id.atlassian.com/manage-profile/security/api-tokens | `abcdefGHiJKLMnOprStu0W5Z`
Project     | first 3 letters of project name                             | `DEV`

* The script checks for the existence of `./jirc/config.json` 
* If the file does not exist it will prompt you to enter the required information
 
