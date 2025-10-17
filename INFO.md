# Hello World GitHub Action

A minimal GitHub Action that automatically updates your profile README with a "Hello World" message and timestamp.

## 🎯 Purpose

This is a learning example demonstrating how to build a GitHub Action that:

- Runs on a schedule or manually
- Clones your profile repository
- Updates a specific section of your README
- Commits and pushes changes back

## 📋 Prerequisites

1. A GitHub profile repository (e.g., `username/username`)
2. A README.md file in that repository
3. A GitHub personal access token with `repo` scope

## 🚀 Usage

### Step 1: Add Section Markers to Your README

Add these comment markers to your `README.md` where you want the Hello World message to appear:

```markdown
# My Profile

Some content here...

<!--START_SECTION:hello-->
<!--END_SECTION:hello-->

More content...
```

### Step 2: Create Workflow File

Create `.github/workflows/hello-world.yml` in your profile repository:

```yaml
name: Hello World Updater

on:
  schedule:
    # Runs every hour
    - cron: "0 * * * *"
  workflow_dispatch: # Allows manual trigger

jobs:
  update-readme:
    name: Update README with Hello World
    runs-on: ubuntu-latest
    steps:
      - uses: YOUR_USERNAME/hello-action@main
        with:
          GH_TOKEN: ${{ secrets.GH_TOKEN }}
```

### Step 3: Set Up GitHub Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate a new token with `repo` scope
3. Go to your profile repository → Settings → Secrets and variables → Actions
4. Create a new secret named `GH_TOKEN` with your token

### Step 4: Run the Action

- **Manual trigger**: Go to Actions tab → Hello World Updater → Run workflow
- **Automatic**: Wait for the scheduled cron to run

## 🎨 Customization

### Change Section Name

```yaml
- uses: YOUR_USERNAME/hello-action@main
  with:
    GH_TOKEN: ${{ secrets.GH_TOKEN }}
    SECTION_NAME: "custom-section" # Default is "hello"
```

Then use in your README:

```markdown
<!--START_SECTION:custom-section-->
<!--END_SECTION:custom-section-->
```

## 🧪 Testing Locally

### Build Docker Image

```bash
cd hello-action
docker build -t hello-action .
```

### Run Locally

```bash
docker run \
  -e INPUT_GH_TOKEN="your_github_token" \
  -e INPUT_SECTION_NAME="hello" \
  hello-action
```

## 📁 Project Structure

```
hello-action/
├── action.yml        # Action metadata and inputs
├── Dockerfile        # Container definition
├── hello.py         # Main Python script
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## 🔧 How It Works

1. **GitHub Actions Runner** starts the workflow on schedule/manual trigger
2. **Docker Container** is built from the Dockerfile
3. **Python Script** executes with inputs as environment variables (`INPUT_*`)
4. **Authentication** uses the provided GitHub token
5. **Repository Clone** fetches your profile repository
6. **README Update** replaces content between comment markers
7. **Commit & Push** saves changes back to your repository

## 📚 Learning Resources

This action is based on patterns from [waka-readme-stats](https://github.com/anmol098/waka-readme-stats).

Key concepts:

- GitHub Actions metadata (`action.yml`)
- Docker-based actions
- Environment variable inputs (`INPUT_*` convention)
- Git operations with GitPython
- GitHub API with PyGithub
- README section replacement with regex

## 🤝 Contributing

Feel free to modify and extend this action for your own use cases!

## 📝 License

MIT License - Feel free to use this as a template for your own actions.

<!--START_SECTION:hello-->
<!--END_SECTION:hello-->
