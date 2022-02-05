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
        'project': {'key': 'SPT'},
        'summary': input('Card Title: '),
        'issuetype': {'name': issue_type}
    }
    pp(issue_dict)
    new_issue = jira.create_issue(fields=issue_dict)
    jira_card_url = new_issue.permalink()
    if(input("Browser? (y/N):")):
        webbrowser.open(jira_card_url)
    print(f"MrD created {new_issue.key} at {jira_card_url}")
