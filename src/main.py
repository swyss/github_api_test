import requests

username = "swyss"
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url)
print(user_data.json())


base_url = "https://api.github.com"

def get_user_repos(username):
    url = f"{base_url}/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repositories_data = response.json()
        return repositories_data
    else:
        return None


user_repos = get_user_repos(username)
if user_repos:
    print(f"Repositories of {username}:")
    for repo in user_repos:
        print(repo["name"])
else:
    print(f"Failed to retrieve repositories.")