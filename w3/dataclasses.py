from dataclasses import dataclass
from github import Github, Auth

@dataclass
class GitHubIssue:
    id: int
    title: str
    state: str
    labels: list

    @classmethod
    def from_api_response(cls, issue_obj):
        label_names = [label.name for label in issue_obj.labels]
        
        return cls(
            id=issue_obj.id,
            title=issue_obj.title,
            state=issue_obj.state,
            labels=label_names
        )

if __name__ == "__main__":
    token = input().strip()
    
    auth = Auth.Token(token=token)
    g = Github(auth=auth)

    repo = g.get_repo("luongnv89/claude-howto")
    
    open_issues = repo.get_issues(state='open')
    
    for raw_issue in open_issues:
        issue_item = GitHubIssue.from_api_response(raw_issue)
        print(issue_item)

        
    g.close()