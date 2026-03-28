import os
import time
import random
from datetime import datetime

# ================== CONFIG ==================
NUM_COMMITS = 100           # Change to 30 first if you want to test
MIN_DELAY = 6               # Minimum seconds between commits
MAX_DELAY = 12              # Maximum seconds between commits

FILES = ["app.py", "utils.py", "README.md", "data.txt"]
# ===========================================

def ensure_files():
    for filename in FILES:
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as f:
                if filename == "README.md":
                    f.write("# Base Builder Project\n\nBuilding in public for Base.\n")
                else:
                    f.write(f"# {filename} - created for Base Builders role\n\n")

def make_realistic_change():
    file = random.choice(FILES)
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    ideas = [
        f"Added comment for better readability - {timestamp}",
        f"Updated function documentation",
        f"Small code cleanup and formatting",
        f"Added TODO for future feature",
        f"Improved variable naming",
        f"Added basic error handling note",
        f"Minor refactor for clarity",
        f"Updated project description",
        f"Added new helper comment",
        f"Fixed small typo in comment"
    ]
    
    content = random.choice(ideas) + "\n"
    
    with open(file, "a", encoding="utf-8") as f:
        f.write(content)
    
    return file

def commit():
    try:
        os.system("git add .")
        commit_msg = f"chore: small improvement #{random.randint(100,9999)}"
        os.system(f'git commit -m "{commit_msg}"')
        print(f"✅ Commit #{os.popen('git rev-list --count HEAD').read().strip()} - {commit_msg}")
        return True
    except:
        return False

def main():
    ensure_files()
    print(f"🚀 Starting {NUM_COMMITS} commits on public repo 'base-builder'")
    print("Make sure the repo is PUBLIC on GitHub!\n")
    
    for i in range(1, NUM_COMMITS + 1):
        make_realistic_change()
        commit()
        
        # Random delay to look natural
        delay = random.randint(MIN_DELAY, MAX_DELAY)
        print(f"   → Waiting {delay} seconds before next commit...\n")
        time.sleep(delay)
        
        # Push every 10 commits to avoid rate limits
        if i % 10 == 0:
            print("Pushing to GitHub...")
            os.system("git push")
    
    # Final push
    os.system("git push")
    print(f"\n🎉 Finished! Made {NUM_COMMITS} commits.")
    print("Wait 5-10 minutes, then check your role on Guild.xyz")

if __name__ == "__main__":
    main()
