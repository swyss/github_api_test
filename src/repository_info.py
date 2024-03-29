# repository_info.py
import requests

class RepositoryInfo:
    base_url = "https://api.github.com"

    def __init__(self, username, repo_name):
        self.username = username
        self.repo_name = repo_name

    def get_details(self):
        url = f"{self.base_url}/repos/{self.username}/{self.repo_name}"
        response = requests.get(url)
        return response.json() if response.ok else None

    def get_commits(self):
        url = f"{self.base_url}/repos/{self.username}/{self.repo_name}/commits"
        response = requests.get(url)
        return response.json() if response.ok else None

    def get_issues(self):
        url = f"{self.base_url}/repos/{self.username}/{self.repo_name}/issues"
        response = requests.get(url)
        return response.json() if response.ok else None

    def get_pulls(self):
        url = f"{self.base_url}/repos/{self.username}/{self.repo_name}/pulls"
        response = requests.get(url)
        return response.json() if response.ok else None

    def get_branches(self):
        url = f"{self.base_url}/repos/{self.username}/{self.repo_name}/branches"
        response = requests.get(url)
        return response.json() if response.ok else None

    def get_tags(self):
        url = f"{self.base_url}/repos/{self.username}/{self.repo_name}/tags"
        response = requests.get(url)
        return response.json() if response.ok else None

if __name__ == '__main__':
    username = 'swyss'
    repo_name = 'swyss'
    repo_info = RepositoryInfo(username, repo_name)
    details = repo_info.get_details()
    print(details)