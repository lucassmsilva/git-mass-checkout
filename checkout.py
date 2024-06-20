import os
import git
from repositories import REPOS

def clone_or_update_repo(repo_name, repo_url, base_dir='./repo', branch='master'):
    clone_dir = os.path.join(base_dir, repo_name)
    try:
        if not os.path.exists(clone_dir):
            os.makedirs(clone_dir)
            repo = git.Repo.clone_from(repo_url, clone_dir, branch=branch)
            print(f"Repository {repo_name} cloned to {clone_dir} and checked out to {branch}")
        else:
            repo = git.Repo(clone_dir)
            repo.git.checkout(branch)
            origin = repo.remotes.origin
            origin.pull()
            print(f"Repository {repo_name} updated in {clone_dir} and checked out to {branch}")
    except Exception as e:
        print(f"Error handling repository {repo_name}: {e}")

def main():
    for repo_name, repo_url in REPOS.items():
        clone_or_update_repo(repo_name, repo_url)

if __name__ == '__main__':
    main()
