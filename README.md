# 🤖 Daily Commit Bot

A GitHub Actions-powered bot that automatically commits daily software development advice and git commands to maintain a consistent contribution graph.

## 📋 Overview

This bot automatically:
- 📅 Runs daily at **9:00 AM IST** (3:30 AM UTC)
- 🎯 Selects a random software development tip from a curated list
- 📝 Updates `daily_advice.md` with today's advice
- 💾 Commits the changes automatically
- 🚀 Pushes to your repository
- 📊 Maintains a consistent GitHub contribution graph

## 🗂️ Project Structure

```
github-daily-bot/
├── .github/
│   └── workflows/
│       └── daily_commit.yml    # GitHub Actions workflow
├── advices.txt                 # Collection of software development advice
├── daily_advice.md            # Updated daily with current advice
├── bot.py                     # Main Python bot script
└── README.md                  # This file
```

## 🎯 Features

### 💡 Software Development Focus
- **Git Commands**: Practical git tips for daily development
- **Best Practices**: Code quality, testing, and documentation advice
- **Development Workflow**: Tips for efficient software development

### 🔄 Automation
- **Scheduled Execution**: Runs automatically every day
- **Manual Trigger**: Can be triggered manually via GitHub Actions
- **Consistent Timing**: Uses date-based seed for consistent daily advice

### 📊 Benefits
- **Contribution Graph**: Maintains daily green squares on your GitHub profile
- **Learning**: Daily exposure to software development best practices
- **Professional Presence**: Shows consistent activity on your GitHub profile

## ⚙️ Setup Instructions

### 1. Repository Setup
1. Fork or clone this repository
2. Push the code to your GitHub repository

### 2. Enable GitHub Actions Permissions
1. Go to your repository **Settings** → **Actions** → **General**
2. Under **Workflow permissions**, select:
   - ✅ **"Read and write permissions"**
   - ✅ **"Allow GitHub Actions to create and approve pull requests"**
3. Click **"Save"**

### 3. Workflow Configuration
The workflow is pre-configured to run at **9:00 AM IST** daily. To modify:

```yaml
schedule:
  - cron: '30 3 * * *'  # 9:00 AM IST (3:30 AM UTC)
```

**Common Schedule Examples:**
```yaml
- cron: '0 0 * * *'    # Midnight UTC
- cron: '0 9 * * *'    # 9:00 AM UTC
- cron: '0 12 * * 1-5' # Weekdays only at noon UTC
```

## 🚀 Usage

### Automatic Execution
- The bot runs automatically at the scheduled time
- No manual intervention required
- View execution logs in the **Actions** tab

### Manual Execution
1. Go to your repository's **Actions** tab
2. Click **"Daily Commit Bot"** workflow
3. Click **"Run workflow"**
4. Select branch and click **"Run workflow"**

### Local Testing
```bash
cd github-daily-bot
python bot.py
```
*Note: Running locally only updates the file but doesn't commit to git*

## 📝 Sample Advice

The bot provides practical software development advice:

- **Git Tips**: `Use git stash to temporarily save changes: git stash push -m "work in progress"`
- **Best Practices**: `Write unit tests before implementing your features (TDD approach)`
- **Code Quality**: `Use meaningful variable names - code should read like English`
- **Development Workflow**: `Always handle errors gracefully in your applications`

## 🔧 Customization

### Adding New Advice
Edit `advices.txt` and add new lines of advice:
```
Your new software development tip here.
Another git command or best practice.
```

### Changing Schedule
Modify the cron expression in `.github/workflows/daily_commit.yml`:
```yaml
schedule:
  - cron: 'MINUTE HOUR DAY MONTH DAYOFWEEK'
```

### Customizing Commit Messages
Edit the workflow file to change commit message format:
```yaml
git commit -m "🚀 Daily dev tip: $(date +%Y-%m-%d)"
```

## 📊 Monitoring

### View Workflow Runs
- **Actions Tab**: Monitor execution status and logs
- **Commits**: View generated commits in repository history
- **Contribution Graph**: Check your GitHub profile for daily activity

### Troubleshooting
- **Workflow not running**: Check repository permissions
- **Permission errors**: Ensure GitHub Actions has write permissions
- **No commits**: Verify workflow file is in `.github/workflows/` directory

## 🛠️ Technical Details

### Dependencies
- **Python 3.9+**: For running the bot script
- **GitHub Actions**: For automation
- **Git**: For version control operations

### How It Works
1. **GitHub Actions** triggers the workflow at scheduled time
2. **Python script** reads advice from `advices.txt`
3. **Date-based seed** ensures consistent daily advice
4. **Markdown file** gets updated with current date and advice
5. **Git operations** commit and push changes automatically

### Security
- Uses GitHub's built-in `GITHUB_TOKEN` for authentication
- No external API calls or sensitive data handling
- All operations contained within your repository

## 📈 Benefits

- **🎯 Learning**: Daily exposure to software development best practices
- **📊 Profile**: Consistent GitHub contribution activity
- **🤖 Automation**: Set-and-forget daily commits
- **💡 Knowledge**: Curated collection of practical development advice
- **🔄 Consistency**: Reliable daily updates without manual effort

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new software development advice to `advices.txt`
- Improve the bot functionality
- Enhance the documentation
- Report bugs or suggest features

---

**Made with ❤️ for the developer community**
