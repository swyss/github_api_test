from github import Github

# Github Enterprise with custom hostname
g = Github(base_url="https://{swyss}/api/v3", auth=auth)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)

# To close connections after use
g.close()