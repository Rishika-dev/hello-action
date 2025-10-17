#!/usr/bin/env python3
"""
Hello World GitHub Action
Updates README with a simple Hello World message and timestamp
"""

import os
import re
from datetime import datetime
from git import Repo, Actor
from github import Github

def main():
    print("🚀 Hello World Action starting...")
    
    # Read inputs from environment variables
    gh_token = os.environ.get('INPUT_GH_TOKEN')
    section_name = os.environ.get('INPUT_SECTION_NAME', 'hello')
    
    if not gh_token:
        print("❌ ERROR: GH_TOKEN is required!")
        exit(1)
    
    print(f"📝 Section name: {section_name}")
    
    # Authenticate with GitHub
    print("🔐 Authenticating with GitHub...")
    github = Github(gh_token)
    user = github.get_user()
    print(f"✅ Authenticated as: {user.login}")
    
    # Define repository to update
    repo_name = f"{user.login}/{user.login}"
    print(f"📦 Target repository: {repo_name}")
    
    # Clone the repository
    print("📥 Cloning repository...")
    repo_url = f"https://{gh_token}@github.com/{repo_name}.git"
    local_path = "./repo"
    
    try:
        repo = Repo.clone_from(repo_url, to_path=local_path)
        print("✅ Repository cloned successfully")
    except Exception as e:
        print(f"❌ Failed to clone repository: {e}")
        exit(1)
    
    # Get README path
    try:
        remote = github.get_repo(repo_name)
        readme = remote.get_readme()
        readme_path = os.path.join(local_path, readme.path)
        print(f"📄 README found at: {readme.path}")
    except Exception as e:
        print(f"❌ Failed to get README: {e}")
        exit(1)
    
    # Read current README content
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
        print("✅ README content loaded")
    except Exception as e:
        print(f"❌ Failed to read README: {e}")
        exit(1)
    
    # Generate Hello World message
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    hello_message = f"""## 👋 Hello World!

This section was automatically updated by a GitHub Action.

**Message:** Hello from GitHub Actions! 🎉

**Last Updated:** {timestamp} UTC
"""
    
    # Define section markers
    start_comment = f"<!--START_SECTION:{section_name}-->"
    end_comment = f"<!--END_SECTION:{section_name}-->"
    section_regex = f"{start_comment}[\\s\\S]*?{end_comment}"
    
    # Check if markers exist
    if start_comment not in readme_content or end_comment not in readme_content:
        print(f"❌ ERROR: Section markers not found in README!")
        print(f"Please add the following to your README.md:")
        print(f"\n{start_comment}")
        print(f"{end_comment}\n")
        exit(1)
    
    # Replace section content
    new_section = f"{start_comment}\n{hello_message}\n{end_comment}"
    new_readme = re.sub(section_regex, new_section, readme_content)
    
    # Write updated README
    try:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_readme)
        print("✅ README updated successfully")
    except Exception as e:
        print(f"❌ Failed to write README: {e}")
        exit(1)
    
    # Commit changes
    print("💾 Committing changes...")
    try:
        repo.git.add(readme_path)
        
        # Check if there are changes to commit
        if repo.is_dirty():
            actor = Actor("hello-bot", "41898282+github-actions[bot]@users.noreply.github.com")
            repo.index.commit("Updated with Hello World message", author=actor, committer=actor)
            print("✅ Changes committed")
            
            # Push to remote
            print("📤 Pushing to remote...")
            repo.remotes.origin.push()
            print("✅ Changes pushed successfully!")
        else:
            print("ℹ️  No changes to commit")
    except Exception as e:
        print(f"❌ Failed to commit/push: {e}")
        exit(1)
    
    print("🎉 Hello World Action completed successfully!")

if __name__ == "__main__":
    main()

