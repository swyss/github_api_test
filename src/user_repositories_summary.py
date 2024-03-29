# user_repositories_summary.py
import requests
from collections import Counter

class UserRepositoriesSummary:
    base_url = "https://api.github.com"

    def __init__(self, username):
        self.username = username

    def get_user_info(self):
        url = f"{self.base_url}/users/{self.username}"
        response = requests.get(url)
        return response.json() if response.ok else None

    def get_user_repos(self):
        url = f"{self.base_url}/users/{self.username}/repos"
        repos = []
        while url:
            response = requests.get(url)
            if response.ok:
                repos.extend(response.json())
                if 'next' in response.links:
                    url = response.links['next']['url']
                else:
                    break
            else:
                return None
        return repos

    def summarize_repos(self):
        repos = self.get_user_repos()
        if not repos:
            return None

        language_counter = Counter()
        repo_summaries = []

        for repo in repos:
            language_counter.update([repo['language']])
            repo_summary = {
                'Name': repo['name'],
                'Sterne': repo['stargazers_count'],
                'Forks': repo['forks_count'],
                'Hauptprogrammiersprache': repo['language']
            }
            repo_summaries.append(repo_summary)

        top_languages = language_counter.most_common(3)

        return {
            'Benutzer': self.username,
            'Gesamt Repositories': len(repos),
            'Top 3 Programmiersprachen': top_languages,
            'Repositories Zusammenfassung': repo_summaries
        }

    def get_user_orgs(self):
        url = f"{self.base_url}/users/{self.username}/orgs"
        response = requests.get(url)
        return response.json() if response.ok else None

if __name__ == '__main__':
    username = 'swyss' 
    user_summary = UserRepositoriesSummary(username)
    summary = user_summary.summarize_repos()
    print(summary)
