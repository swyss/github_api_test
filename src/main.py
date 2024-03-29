from repository_info import RepositoryInfo
from user_repositories_summary import UserRepositoriesSummary

def main():
    # Beispiel-Username und Repository
    username = 'swyss'
    repo_name = 'swyss'

    # Repository-Informationen abrufen
    repo_info = RepositoryInfo(username, repo_name)
    details = repo_info.get_details()
    print("Repository-Details:", details)

    # Benutzer-Repositories zusammenfassen
    user_summary = UserRepositoriesSummary(username)
    summary = user_summary.summarize_repos()
    print("\nBenutzer-Repositories Zusammenfassung:", summary)

if __name__ == '__main__':
    main()
