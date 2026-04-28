# Deployment Guide

## Deploy to GitHub Pages

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Name your repository (e.g., `stanford-founders`)
3. Keep it public (required for free GitHub Pages)
4. Don't initialize with README (we already have one)
5. Click "Create repository"

### Step 2: Push Your Code

```bash
cd c:\advit\spring-26\stanford-founders

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Stanford Founders static site"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/stanford-founders.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top right)
3. Click **Pages** (left sidebar)
4. Under "Source":
   - Select branch: `main`
   - Select folder: `/ (root)`
5. Click **Save**
6. Wait 1-2 minutes for deployment

### Step 4: Access Your Site

Your site will be live at:
```
https://YOUR_USERNAME.github.io/stanford-founders/
```

## Custom Domain (Optional)

To use a custom domain like `stanfordfounders.com`:

1. In GitHub Pages settings, add your custom domain
2. In your domain registrar (e.g., GoDaddy, Namecheap):
   - Add a CNAME record pointing to `YOUR_USERNAME.github.io`
   - Or add A records pointing to GitHub's IPs:
     - 185.199.108.153
     - 185.199.109.153
     - 185.199.110.153
     - 185.199.111.153

## Updating Your Site

To make changes:

```bash
# Make your edits to HTML/CSS/JS files

# Commit and push
git add .
git commit -m "Update content"
git push
```

GitHub Pages will automatically rebuild and deploy your changes in 1-2 minutes.

## Troubleshooting

**Site not loading?**
- Wait 2-3 minutes after first deployment
- Check Settings → Pages to see deployment status
- Make sure repository is public

**Images not showing?**
- All images are loaded from the original WordPress site
- Requires internet connection
- Images are external URLs, not stored in this repo

**Need help?**
- GitHub Pages docs: https://docs.github.com/en/pages
