# Hello World GitHub Action

A simple GitHub Action that updates your README with a Hello World message and timestamp.

## Usage

Add this to your workflow:

```yaml
name: Hello World
on:
  schedule:
    - cron: "0 0 * * *" # Run daily
jobs:
  hello:
    runs-on: ubuntu-latest
    steps:
      - uses: your-username/hello-action@v1
        with:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          SECTION_NAME: "hello" # Optional, defaults to "hello"
```

## Setup

1. Add section markers to your README.md:

   ```markdown
   <!--START_SECTION:hello-->
   <!--END_SECTION:hello-->
   ```

2. The action will automatically update this section with a Hello World message and timestamp.

## Inputs

- `GH_TOKEN`: GitHub token with repo scope (required)
- `SECTION_NAME`: Section name to update (optional, defaults to "hello")

## Example Output

The action will insert:

```markdown
## 👋 Hello World!

This section was automatically updated by a GitHub Action.

**Message:** Hello from GitHub Actions! 🎉

**Last Updated:** 2024-01-01 12:00:00 UTC
```
