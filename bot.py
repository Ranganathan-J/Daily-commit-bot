#!/usr/bin/env python3
"""
Daily Commit Bot - Automatically updates daily advice and commits to GitHub
"""

import random
import datetime
import os

def load_advices():
    """Load all advice from the advices.txt file"""
    try:
        with open('advices.txt', 'r', encoding='utf-8') as f:
            advices = [line.strip() for line in f.readlines() if line.strip()]
        return advices
    except FileNotFoundError:
        print("Error: advices.txt file not found!")
        return []

def get_daily_advice():
    """Get a random advice for today"""
    advices = load_advices()
    if not advices:
        return "No advice available today. Stay positive!"
    
    # Use date as seed for consistent daily advice
    today = datetime.date.today()
    random.seed(today.toordinal())
    
    return random.choice(advices)

def update_daily_advice_file():
    """Update the daily_advice.md file with today's advice"""
    today = datetime.date.today()
    advice = get_daily_advice()
    
    content = f"""# Daily Advice

## Today's Advice
*This file is updated daily with new advice.*

---

**Date:** {today.strftime('%B %d, %Y')}  
**Advice:** {advice}

---

*This advice is automatically updated by the Daily Commit Bot.*
"""
    
    try:
        with open('daily_advice.md', 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully updated daily_advice.md for {today}")
        print(f"Today's advice: {advice}")
    except Exception as e:
        print(f"Error updating daily_advice.md: {e}")

def main():
    """Main function to run the daily bot"""
    print("🤖 Daily Commit Bot Starting...")
    print(f"📅 Date: {datetime.date.today()}")
    
    # Change to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Update the daily advice
    update_daily_advice_file()
    
    print("✅ Daily Commit Bot Completed!")

if __name__ == "__main__":
    main() 