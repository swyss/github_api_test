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

# -----------------------------------------------------------
