import sys
import re
import os


OK = '\033[0K'
RED='\033[0;31m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'
NC='\033[0m'
K2 = '\033[2K'
A2 = '[2A'#\e[2A
L = '|'

def replacer(line):    
    if(line.startswith('[#') or "In progress" in line):
        return ""

    replacements = {RED:"", YELLOW:"", GREEN:"",NC:"", OK:"", A2:"", L:"\t", K2:""}
    rep_sorted = sorted(replacements, key=len, reverse=True)
    rep_escaped = map(re.escape, rep_sorted)
    
    # Create a big OR regex that matches any of the substrings to replace
    pattern = re.compile("|".join(rep_escaped), 0)
    
    # For each match, look up the new string in the replacements, being the key the normalized old string
    newline = pattern.sub(lambda match: replacements[match.group(0)], line)
    return newline
    


