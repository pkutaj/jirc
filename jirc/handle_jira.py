from jirc.logger import print_JIRA_project
from jira import JIRA
from jirc.handle_config_file import get_config
from pprint import pprint as pp
import webbrowser

config = get_config()
jira_server = {'server': config["jira_server"]}
jira = JIRA(options=jira_server, basic_auth=(
    config["jira_user"], config["jira_token"]))


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
    if(input("Browser? (y/N):")) == "y" or "Y":
        webbrowser.open(jira_card_url)
