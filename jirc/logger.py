def print_JIRA_project(jira_project):
    jira_project = f"PROJECT: {jira_project} "
    print(((4 + len(jira_project)) * "—").center(80))
    print(f"| {jira_project} |".center(80))
    print(((4 + len(jira_project)) * "—").center(80))
