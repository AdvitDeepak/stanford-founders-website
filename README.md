# Stanford Founders Website

Official website for Stanford Founders - Stanford's premier graduate entrepreneurship community.

## 🚀 Deployment Workflow

### Making Changes to the Live Site

1. **Pull the repo on your local machine**
   ```bash
   git clone https://github.com/AdvitDeepak/stanford-founders-website.git
   cd stanford-founders-website
   ```

2. **Make any changes**
   - Edit HTML, CSS, JS, or images as needed
   - Test locally by running: `python -m http.server 8000`
   - View at `http://localhost:8000`

3. **Commit and push changes**
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin main
   ```

4. **Deploy to live site**
   - Navigate to [https://domains.stanford.edu/dashboard/](https://domains.stanford.edu/dashboard/)
   - Click on **"Terminal"**
   - Run the following commands:
     ```bash
     cd stanfordfounders.stanford.edu
     git pull
     ```

5. **Done!** 
   - Anything in the `stanfordfounders.stanford.edu` folder on the remote machine is what's displayed live
   - Visit [https://stanfordfounders.stanford.edu](https://stanfordfounders.stanford.edu) to see your changes

## � Contact Form

The contact form on the website automatically populates a Google Spreadsheet located in the Stanford Founders shared drive:

**Location:** `2025-2026 / Website / Contact Form Submissions`

Form submissions include: timestamp, first name, last name, email, and message.

## �📝 License

© 2026 Stanford Founders. All rights reserved.
