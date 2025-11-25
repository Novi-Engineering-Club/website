# Automated Project Upload System

This system allows you to upload projects via a web panel, which automatically:
1. Extracts the ZIP file
2. Converts Markdown to MDX format
3. Organizes files into the correct directories
4. Updates the route configuration
5. Creates a Pull Request for review

## Setup

### 1. Create a GitHub Personal Access Token

1. Go to [GitHub Settings → Developer Settings → Personal Access Tokens](https://github.com/settings/tokens?type=beta)
2. Click "Generate new token"
3. Give it a name like "Project Upload Automation"
4. Select these scopes:
   - `repo` (full control of repositories)
   - `workflow` (update GitHub Action workflows)
5. Click "Generate token"
6. Copy the token

### 2. Add the Token to Repository Secrets

1. Go to your repository settings
2. Navigate to **Secrets and variables → Actions**
3. Click **New repository secret**
4. Name: `GITHUB_TOKEN`
5. Value: Paste the token you copied
6. Click **Add secret**

### 3. Verify Workflow Permissions

1. Go to repository settings
2. Navigate to **Actions → General**
3. Under "Workflow permissions", select:
   - ☑️ **Read and write permissions**
   - ☑️ **Allow GitHub Actions to create and approve pull requests**
4. Click **Save**

## Usage

### For End Users

1. Navigate to `/admin` on your website
2. Click the upload area or drag-and-drop a `.zip` file
3. The ZIP should contain:
   ```
   project-name/
   ├── project-name.md
   └── images/
       ├── image1.png
       ├── image2.jpg
       └── ...
   ```
4. Click "Upload Project"
5. A GitHub workflow will:
   - Extract the ZIP
   - Convert `project-name.md` → `project-name.mdx`
   - Move images to `public/images/project-name/`
   - Update the route configuration
   - Create a Pull Request
6. Review and merge the PR in GitHub

### Project Folder Structure

```
my-project/
├── my-project.md          # Required: Your project content (Markdown)
└── images/                # Optional: Your images
    ├── screenshot.png
    ├── diagram.jpg
    └── logo.svg
```

### Markdown Content Format

```markdown
# My Project Title

Description of the project.

![Project Screenshot](/images/my-project/screenshot.png)

## Features

- Feature 1
- Feature 2

## More Info

Additional content...
```

## How It Works

1. **Upload**: User uploads ZIP via `/admin` panel
2. **API Endpoint**: `/api/upload-project` receives the file
3. **GitHub Dispatch**: Sends base64-encoded ZIP to GitHub API
4. **Workflow Triggered**: `.github/workflows/process-project-upload.yml` runs
5. **Extraction**: Workflow extracts ZIP contents
6. **Setup**: Creates directories and converts files
7. **Updates**: Modifies `app/routes/projects.$projectName.tsx`
8. **Pull Request**: Creates PR with all changes for review

## Troubleshooting

### Workflow doesn't trigger
- Check `GITHUB_TOKEN` is set in repository secrets
- Verify token has `repo` and `workflow` scopes
- Check workflow permissions are set to "Read and write"

### PR creation fails
- Ensure `peter-evans/create-pull-request@v5` action is available
- Verify GitHub Actions are enabled in repository

### ZIP extraction issues
- Ensure project name (zip filename without .zip) matches folder name inside
- Verify all required files are present

## Security Note

This panel is currently public. For a production site, consider adding:
- Authentication check
- Rate limiting
- File size limits
- Allowed user list

Add to `app/routes/admin.tsx`:
```tsx
export async function loader() {
  const user = await getUser(); // Your auth logic
  if (!user?.isAdmin) {
    throw new Response("Unauthorized", { status: 401 });
  }
  return null;
}
```
