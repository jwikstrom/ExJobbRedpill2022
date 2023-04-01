from math import floor
import sys
import re
import os
import re
import string


OK = '\033[0K'
RED='\033[0;31m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'
NC='\033[0m'
K2 = '\033[2K'
A2 = '[2A'#\e[2A
L = '|'
U = '|_'
p = re.compile('[\s]*[\D]+.*: [^\s]+')
p2 = re.compile('.+: .+')
pc = re.compile('.*[^\s]*, .*:.*')
colon = re.compile(':')
comma = re.compile(',')

def format_string(str, startTabs):
    tab_str = ""
    for tab in range(startTabs):
        tab_str += ' '
    indent_num = floor(startTabs/2)
    prevc = ' '
    word = ""
    prevDivider = ''
    inPara = False
    for c in str:
        if(inPara):
            word += c
            if c == ')':
                inPara = False
                tab_str += word
                word = ''
            continue
        elif c == '(':
            word += c
            inPara = True
            continue

        if c == ' ':
            if prevc == ':' or prevc == ',' or prevc == ';' or prevc == ' ':
                prevc = c
                continue
        elif prevc == ':':
            tab_str = tab_str.rstrip()
            tab_str += prevc
        if c == ':' or c == ',' or c == ';':
            if c == ':':
                if prevDivider == ',':
                    tab_str = tab_str[:-2]
                else:
                    indent_num += 1
                tab_str += word
                tab_str += '\n'
            elif c == ',':
                tab_str += word
                tab_str += '\n'
            elif c == ';':
                tab_str += word
                tab_str += '\n'
                indent_num -= 1
            for tab in range(indent_num):
                tab_str += '  '
            prevDivider = c
            word = ''
        else:
            word += c 
        prevc = c
    tab_str += word
    return tab_str

def lineSplitter(line, tabs, startTab):
    #Vet att line innehålller ett x:y
    #Kolla om , eller : förekommer först?
    #Om : först
    ##  list.extend(tabs x)
    ##  Måste kolla y separat -> Om match i y, return list.extend(lineSplitter(y, tabs+1))
    ##  Om ingen match i y -> return list.extend(tabs+1 y)
    #Annars Om , först så splitta x till ->a,b:y
    ##  list.extend(tabs a)
    ##  list.extend(tabs-1 b)
    ##  Måste kolla y separat -> Om match i y, return list.extend(lineSplitter(y, tabs))
    ##  annars return list.extend(y, tabs)
    #Annars Error + return line

    tab = " "
    lines = []
    s = line.split(':', 1)
    s1 = s[1].strip()
    s0 = s[0].strip() + ":"
    #m = p.match(line)
    #mc = pc.match(line)
    m = line.find(":")
    mc = line.find(",")
    msc = line.find(";")
    if(mc == -1):
        mc = m
    else: 
        print("Found:" + line)
        print("m:", m)
        print("mc:", mc)
    #print("line - " + line)
    if(m <= mc and m <= msc):
        st = (tab*startTab + tab*tabs + s0 + '\n')
        lines.append(st)
        m1 = p2.match(s1)
        if(m1):
            lines.extend(lineSplitter(s1, tabs+2, startTab))
            return lines
        else:
            sr = (tab*startTab + tab*(tabs+2) + s1 + '\n')
            lines.append(sr)
            return lines
    else:
        print("ELSE")
        if(mc <= msc):
            sc = s0.split(',', 1)

        sc0 = (tab*startTab + tab*tabs + sc[0] + '\n')
        lines.append(sc0)

        sc1 = (tab*startTab + tab*(tabs-1) + sc[1] + '\n')
        lines.append(sc1)

        m1 = p2.match(s1)
        if(m1):
            lines.extend(lineSplitter(s1, tabs-2, startTab))
            return lines
        else:
            sr = (tab*startTab + tab*(tabs) + s1+ '\n')
            lines.append(sr)
            return lines


def replacer(line):    

    if(line.startswith('[#') or "In progress" in line):
        return ""

    replacements = {RED:"", YELLOW:"", GREEN:"",NC:"", OK:"", A2:"", L:" ", K2:"", U:"  "}
    rep_sorted = sorted(replacements, key=len, reverse=True)
    rep_escaped = map(re.escape, rep_sorted)
    
    # Create a big OR regex that matches any of the substrings to replace
    pattern = re.compile("|".join(rep_escaped), 0)
    
    # For each match, look up the new string in the replacements, being the key the normalized old string
    newline = pattern.sub(lambda match: replacements[match.group(0)], line)
    #newline is an updated line
    m = p.match(newline)
    if(m):
        startTab = (len(newline)- len(newline.lstrip()))
        #print(f'TABS - {0}|{1}',startTab, newline)
        #print("LINE -", newline)
       #print("M - " + m.group())
        #newline = lineSplitter(newline, 0, startTab)
        newline = format_string(newline, startTab)
       #print(newline)
    
    return newline
    


