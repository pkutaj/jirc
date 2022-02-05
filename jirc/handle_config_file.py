import json
import os
import sys
config_file_path = "./jirc/jirc/config.json"
config_file_template = {
    "jira_server": None,
    "jira_user": None,
    "jira_token": None,
    "jira_project": None
}


def create_config():
    with open(config_file_path, mode="wt", encoding="utf-8") as config_file:
        config_file_template["jira_server"] = input("Jira server:")
        config_file_template["jira_user"] = input("Jira user:")
        config_file_template["jira_token"] = input("Jira token:")
        config_file_template["jira_project"] = input("Jira project:")
        json.dump(config_file_template, config_file)


def get_config():
    if os.path.exists(config_file_path):
        with open(config_file_path) as config:
            return json.load(config)
    else:
        print("\t~~> missing Jira connection settings, please populate")
        if input("Create now? (y/N): ") == ("y" or "Y"):
            create_config()
            return get_config()
        else:
            sys.exit("bye-bye!")
