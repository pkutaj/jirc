from jirc.logger import print_JIRA_project
from jirc.handle_config_file import get_config
import json
from pprint import pprint as pp
from settings import *
import sys
import webbrowser

try:
    from jira import JIRA
    from jira import exceptions
except ImportError as e:
    print(e, file=sys.stderr)
    sys.exit(
        "\tYou ran into the problem of importing the required Jira module.\n"
        "\tRunning >>> pip install -r requirements.txt <<< can fix the problem"
    )

config = get_config()
jira_server = {"server": config["jira_server"]}
jira = JIRA(options=jira_server, basic_auth=(config["jira_user"], config["jira_token"]))
project_ids = sorted([i.key for i in jira.projects()])


def change_jira_project():
    new_project_id = input("Enter Jira Project Name:")
    if new_project_id in project_ids:
        config["jira_project"] = new_project_id
    else:
        print("~~> Wrong Input. Select one of the following:")
        print(project_ids)
        change_jira_project()
    with open(config_file_path, mode="wt", encoding="utf-8") as config_file:
        json.dump(config, config_file)


def get_jira_projects():
    print_JIRA_project(config["jira_project"])
    return jira.project(config["jira_project"])


def create_card(issue_id):
    issue_dict = {
        "project": config["jira_project"],
        "summary": input("Card Title: "),
        "issuetype": {"id": issue_id},
    }
    try:
        new_issue = jira.create_issue(fields=issue_dict)
    except exceptions.JIRAError:
        print("\t~~> This did NOT work for Jira-speficic reasons.")
        print(
            "\t~~> A typical scenario is a missing required fields - Can't fix this for you, sorry!"
        )
        if input("Do you want to open Jira in browser now? (y/N): ") == "y":
            webbrowser.open(f'{config["jira_server"]}/browse/{config["jira_project"]}')
        sys.exit("Bye!")
    jira_card_url = new_issue.permalink()
    del (issue_dict["project"], issue_dict["issuetype"])
    issue_dict["url"] = jira_card_url
    issue_dict["key"] = new_issue.key
    pp(issue_dict)
    webbrowser.open(jira_card_url)
