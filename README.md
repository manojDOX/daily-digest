# Daily Backend Learning Digest 📧

Sends a beautiful HTML email every morning at **6:00 AM IST** with that day's
learning topic, curated blog posts, and YouTube videos — automatically via GitHub Actions.

## Project Structure

```
daily-mailer/
├── .github/
│   └── workflows/
│       └── daily_digest.yml    ← GitHub Actions cron job
├── templates/
│   └── email_template.html     ← HTML email layout
├── curriculum.py               ← All 30 days of topics + links
├── send_email.py               ← Main script: builds + sends email
└── README.md
```

---

## ⚙️ Setup — Step by Step

### Step 1: Create a Gmail App Password

Your regular Gmail password won't work with SMTP. You need an **App Password**.

1. Go to your Google Account → **Security**
2. Enable **2-Step Verification** (required)
3. Search for **"App passwords"** in the search bar
4. Select app: **Mail** → device: **Other** → name it `daily-digest`
5. Copy the 16-character password shown (format: `xxxx xxxx xxxx xxxx`)
6. Save it — you'll only see it once

### Step 2: Create a GitHub Repository

```bash
# In the daily-mailer/ folder:
git init
git add .
git commit -m "Initial commit: daily learning digest"

# Create a new repo on github.com, then:
git remote add origin https://github.com/YOUR_USERNAME/daily-mailer.git
git push -u origin main
```

### Step 3: Add GitHub Secrets

Go to your GitHub repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Add these 4 secrets:

| Secret Name | Value | Example |
|---|---|---|
| `GMAIL_USER` | Your Gmail address | `yourname@gmail.com` |
| `GMAIL_APP_PASS` | The 16-char app password from Step 1 | `abcd efgh ijkl mnop` |
| `TO_EMAIL` | Where to send the email | `yourname@gmail.com` |
| `START_DATE` | The day you start (ISO format) | `2025-05-19` |

> **Tip:** `TO_EMAIL` can be the same as `GMAIL_USER` to send to yourself.

### Step 4: Verify the Workflow File Exists

Make sure `.github/workflows/daily_digest.yml` is committed and pushed.
GitHub Actions only triggers from files in the default branch.

```bash
git push origin main
```

### Step 5: Test It Manually

Before waiting for 6am, trigger a manual run:

1. Go to your repo on GitHub
2. Click **Actions** tab
3. Click **Daily Learning Digest** in the left sidebar
4. Click **Run workflow** (top right)
5. Optionally enter a day number (e.g. `1`) to test a specific day
6. Click the green **Run workflow** button
7. Watch the logs — should show ✅ Email sent

Check your inbox. The email should arrive within 30 seconds.

---

## 🕕 Schedule

The cron is set to `30 0 * * *` (UTC) = **6:00 AM IST** every day.

```
IST 06:00 AM = UTC 00:30 AM
```

**Day calculation is automatic:** The script computes which day of the roadmap
you're on based on `START_DATE`. Day 1 = start date, Day 2 = next day, etc.

---

## 🧪 Testing Locally

```bash
# Export the required env vars
export GMAIL_USER="yourname@gmail.com"
export GMAIL_APP_PASS="abcd efgh ijkl mnop"
export TO_EMAIL="yourname@gmail.com"
export START_DATE="2025-05-19"

# Send today's auto-detected day
python send_email.py

# Send a specific day (for testing)
python send_email.py 5
```

---

## 🔧 Customization

### Change the schedule time

Edit `.github/workflows/daily_digest.yml`:
```yaml
- cron: "30 0 * * *"   # current: 6:00 AM IST (00:30 UTC)
- cron: "30 1 * * *"   # 7:00 AM IST (01:30 UTC)
- cron: "0 2 * * 1-5"  # 7:30 AM IST, weekdays only
```

### Add a new topic day

In `curriculum.py`, append a new dict to the `CURRICULUM` list:
```python
{
    "phase": 2,
    "topic_title": "Your Topic",
    "topic_description": "What this day covers...",
    "daily_goal": "What to build/do today",
    "blogs": [
        {"title": "...", "url": "https://...", "desc": "..."},
    ],
    "youtube": [
        {"title": "...", "url": "https://youtube.com/watch?v=...", "desc": "..."},
    ],
}
```

---

## 🐛 Troubleshooting

| Problem | Fix |
|---|---|
| `SMTPAuthenticationError` | Re-generate Gmail App Password. Regular password won't work. |
| Email goes to spam | Add your Gmail as a contact in the recipient account |
| Workflow not triggering | Check the workflow file is on the `main` branch. GitHub only schedules from default branch. |
| Wrong day number | Verify `START_DATE` secret is in `YYYY-MM-DD` format |
| `KeyError: 'GMAIL_USER'` | Secrets not set — check Settings → Secrets in your repo |