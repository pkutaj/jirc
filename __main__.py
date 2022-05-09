from jirc.handle_jira import *


def main():
    print("LET'S CREATE A JIRA CARD".center(80, "—"))
    jira_project = get_jira_projects()
    for i, issue in enumerate(jira_project.issueTypes):
        print(i, issue.name)
    issue_or_project = input("Enter number OR 'c' for project change: ")
    if issue_or_project == ("c" or "C"):
        change_jira_project()
        main()
    else:
        create_card(issue_id=jira_project.issueTypes[int(issue_or_project)].id)


if __name__ == "__main__":
    main()
