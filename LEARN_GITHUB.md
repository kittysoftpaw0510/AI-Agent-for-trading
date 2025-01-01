# 🌙 Practical GitHub Guide

## Daily Commands You'll Actually Use

git checkout -b branch_name    # Creates AND switches to new branch
git checkout branch_name       # Just switches to existing branch

Think of it like this:
main is like the master copy of your code
git checkout -b develop is like saying "make me a copy of whatever branch I'm on (main) and name it 'develop'"
The -b flag means "create new branch"

# Someone finding your repo could do:
git clone https://github.com/moondevonyt/moon-dev-ai-agents-for-trading.git
git checkout -b their-feature-name

# You working on your repo:
git checkout -b develop        # Create development branch
git checkout main             # Switch back to main
git checkout develop          # Switch to develop again

# check which branch you're on 
git branch


====

