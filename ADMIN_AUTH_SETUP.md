# Admin Panel Authentication Setup

The admin panel at `/admin` now requires authentication to upload projects.

## Setting Up Authentication

### 1. Create an Admin Token

Choose a strong password/token. Examples:
- A random string: `abc123def456ghi789`
- A passphrase: `my-secret-admin-2024`
- Use a generator: `openssl rand -hex 32`

### 2. Add Token to Environment Variables

Add this to your `.env` file (or environment variables):

```bash
ADMIN_PASSWORD="your-secure-token-here"
```

### 3. Restart the Development Server

After adding the environment variable, restart:

```bash
npm run dev
```

## How It Works

**Without `ADMIN_PASSWORD` set:**
- Admin panel is accessible to everyone (development mode)

**With `ADMIN_PASSWORD` set:**
- Admin page requires authentication
- When you try to upload, you'll be prompted for the token
- Enter the same token you set in `ADMIN_PASSWORD`

## Using the Admin Panel

1. Go to `/admin`
2. If prompted, enter your admin token
3. Upload your project ZIP file
4. The workflow will process it automatically

## Changing the Token

1. Update `ADMIN_PASSWORD` in your `.env` file
2. Restart the server
3. Use the new token for uploads

## For Deployment

When deploying to production:

1. Set the environment variable on your hosting platform:
   - Vercel: Project Settings → Environment Variables
   - Netlify: Site Settings → Build & Deploy → Environment
   - Other platforms: Consult their documentation

2. Make sure the variable is available to both build and runtime:
   ```
   ADMIN_PASSWORD = your-secure-token
   ```

## Security Notes

- Keep your `ADMIN_PASSWORD` secret
- Use a strong, random token (at least 32 characters recommended)
- Change the password periodically
- Don't commit `.env` to git (it should be in `.gitignore`)
- For GitHub Actions: the workflow uses `GITHUB_TOKEN` (separate from admin password)
