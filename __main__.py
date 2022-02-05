from jirc.handle_jira import *


def main():
    print("LET'S CREATE A JIRA CARD".center(80, "—"))
    jira_project = get_jira_projects()
    for i, issue in enumerate(jira_project.issueTypes):
        print(i, issue.name)
    create_card(
        issue_type=jira_project.issueTypes[int(input("Enter Number: "))].name)


if __name__ == "__main__":
    main()
