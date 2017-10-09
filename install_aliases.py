import subprocess
import os

current_user = os.getlogin()

aliases = '''
alias gs='git status'
alias ga='git add'
alias gb='git branch'
alias gc='git checkout'
alias gcb='git checkout -b'
alias gd='git diff'
alias gcom='git commit -m'
alias gac='git commit -a -m'
alias gpl='git pull'
alias gph='git push'
alias gpho='git push origin'
alias gf='git fetch'
alias gl='git log'
alias gm='git merge'
alias glg='git log --graph'
alias gupdate='(cd /Users/current_user && python git_update.py)'

alias lsof='lsof -i:8080'
alias pr='ps -ef | grep'
alias step='stepup notes add --section otherchanges --force -m'
alias javapid="ps -ef | grep java | grep -v grep | awk '{print \$2  \$8}'"

'''.replace('current_user',current_user)

with open(".bash_profile", "a") as myfile:
    myfile.write(aliases)
