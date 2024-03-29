import requests
from collections import Counter

base_url = "https://api.github.com"

def get_user_data(username):
    url = f"{base_url}/users/{username}"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_user_repos(username):
    url = f"{base_url}/users/{username}/repos"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_user_followers(username):
    url = f"{base_url}/users/{username}/followers"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_user_following(username):
    url = f"{base_url}/users/{username}/following"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_user_gists(username):
    url = f"{base_url}/users/{username}/gists"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_user_starred_repos(username):
    url = f"{base_url}/users/{username}/starred"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_repository_issues(username, repo_name):
    url = f"{base_url}/repos/{username}/{repo_name}/issues"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_repository_pulls(username, repo_name):
    url = f"{base_url}/repos/{username}/{repo_name}/pulls"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_repository_commits(username, repo_name):
    url = f"{base_url}/repos/{username}/{repo_name}/commits"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_repository_contributors(username, repo_name):
    url = f"{base_url}/repos/{username}/{repo_name}/contributors"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_repository_languages(username, repo_name):
    url = f"{base_url}/repos/{username}/{repo_name}/languages"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_repository_tags(username, repo_name):
    url = f"{base_url}/repos/{username}/{repo_name}/tags"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_user_organizations(username):
    url = f"{base_url}/users/{username}/orgs"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_repository_branches(username, repo_name):
    url = f"{base_url}/repos/{username}/{repo_name}/branches"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_repository_releases(username, repo_name):
    url = f"{base_url}/repos/{username}/{repo_name}/releases"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_specific_commit(username, repo_name, commit_sha):
    url = f"{base_url}/repos/{username}/{repo_name}/commits/{commit_sha}"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_user_events(username):
    url = f"{base_url}/users/{username}/events"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_repository_events(username, repo_name):
    url = f"{base_url}/repos/{username}/{repo_name}/events"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_user_received_events(username):
    url = f"{base_url}/users/{username}/received_events"
    response = requests.get(url)
    return response.json() if response.ok else None

def get_user_repos(username):
    url = f"{base_url}/users/{username}/repos"
    response = requests.get(url)
    return response.json() if response.ok else None

def summarize_repo_properties(username):
    repos = get_user_repos(username)
    if not repos:
        print(f"Keine Repositories gefunden für Benutzer: {username}")
        return

    summary = []  # Eine Liste, um Zusammenfassungen für jedes Repository zu speichern

    for repo in repos:
        repo_summary = {
            'Name': repo['name'],
            'Sterne': repo['stargazers_count'],
            'Forks': repo['forks_count'],
            'Hauptprogrammiersprache': repo['language'],
            'Erstellt am': repo['created_at']
        }
        summary.append(repo_summary)

    return summary
def get_user_repos(username):
    url = f"{base_url}/users/{username}/repos"
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

def get_repo_contributors(username, repo_name):
    url = f"{base_url}/repos/{username}/{repo_name}/contributors"
    response = requests.get(url)
    return len(response.json()) if response.ok else 0

def get_repo_branches(username, repo_name):
    url = f"{base_url}/repos/{username}/{repo_name}/branches"
    response = requests.get(url)
    return len(response.json()) if response.ok else 0

def summarize_repo_properties(username):
    repos = get_user_repos(username)
    if not repos:
        print(f"Keine Repositories gefunden für Benutzer: {username}")
        return [], []

    language_counter = Counter()
    summary = []

    for repo in repos:
        repo_name = repo['name']
        contributors_count = get_repo_contributors(username, repo_name)
        branches_count = get_repo_branches(username, repo_name)
        issues_count = repo['open_issues_count']
        language_counter.update([repo['language']])

        repo_summary = {
            'Name': repo_name,
            'Sterne': repo['stargazers_count'],
            'Forks': repo['forks_count'],
            'Hauptprogrammiersprache': repo['language'],
            'Erstellt am': repo['created_at'],
            'Branches': branches_count,
            'Mitwirkende': contributors_count,
            'Offene Issues': issues_count
        }
        summary.append(repo_summary)

    top_languages = language_counter.most_common(3)
    return summary, top_languages

# -----------------------------------------------------------
username = "swyss"
user_data = get_user_data(username)
if user_data:
    print(f"User data for {username}: {user_data}")

user_repos = get_user_repos(username)
if user_repos:
    print(f"Repositories of {username}:")
    for repo in user_repos:
        print(repo["name"])

user_followers = get_user_followers(username)
if user_followers:
    print(f"Followers of {username}:")
    for follower in user_followers:
        print(follower["login"])


repo_name = "swyss"  

repo_issues = get_repository_issues(username, repo_name)
if repo_issues:
    print(f"Issues in {repo_name}:")
    for issue in repo_issues:
        print(issue["title"])

repo_pulls = get_repository_pulls(username, repo_name)
if repo_pulls:
    print(f"Pull Requests in {repo_name}:")
    for pull in repo_pulls:
        print(pull["title"])

commit_sha = "commit-sha" 

repo_branches = get_repository_branches(username, repo_name)
if repo_branches:
    print(f"Branches in {repo_name}:")
    for branch in repo_branches:
        print(branch["name"])

repo_releases = get_repository_releases(username, repo_name)
if repo_releases:
    print(f"Releases in {repo_name}:")
    for release in repo_releases:
        print(release["name"])

specific_commit = get_specific_commit(username, repo_name, commit_sha)
if specific_commit:
    print(f"Details of commit {commit_sha}:")
    print(specific_commit)

# repo_summary = summarize_repo_properties(username)

# if repo_summary:
#     for repo in repo_summary:
#         print(f"Repository: {repo['Name']}")
#         print(f"Sterne: {repo['Sterne']}, Forks: {repo['Forks']}, Hauptprogrammiersprache: {repo['Hauptprogrammiersprache']}, Erstellt am: {repo['Erstellt am']}")
#         print("------")

