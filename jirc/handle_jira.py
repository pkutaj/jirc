from jirc.logger import print_JIRA_project
from jirc.handle_config_file import get_config
import json
from pprint import pprint as pp
import sys
import webbrowser
try:
    from jira import JIRA
except ImportError as e:
    print(e, file=sys.stderr)
    sys.exit("\tYou ran into the problem of importing the required Jira module.\n"
             "\tRunning >>> pip install -r requirements.txt <<< can fix the problem")
config = get_config()
config_file_path = "./jirc/jirc/config.json"
jira_server = {'server': config["jira_server"]}
jira = JIRA(options=jira_server, basic_auth=(
    config["jira_user"], config["jira_token"]))


def change_jira_project():
    config["jira_project"] = input("Enter Jira Project Name:")
    with open(config_file_path, mode="wt", encoding="utf-8") as config_file:
        json.dump(config, config_file)


def get_jira_projects():
    print_JIRA_project(config["jira_project"])
    return jira.project(config["jira_project"])


def create_card(issue_type):
    issue_dict = {
        "project": config["jira_project"],
        "summary": input('Card Title: '),
        "issuetype": issue_type
    }
    new_issue = jira.create_issue(fields=issue_dict)
    jira_card_url = new_issue.permalink()
    del(issue_dict["project"], issue_dict["issuetype"])
    issue_dict["url"] = jira_card_url
    issue_dict["key"] = new_issue.key
    pp(issue_dict)
    if (input("Browser? (y/N):")) == ("y" or "Y"):
        webbrowser.open(jira_card_url)
