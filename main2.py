from curses.ascii import isspace
import os
from pickle import FALSE, TRUE
import sys
from itertools import tee
import re
import fileCleaner as cleaner
import constants
import log


ip = "192.168.56.0"
filename3 = "nmapAutomator_192.168.56.0_All.txt"
filename2 = "test.txt"
filename = "nmapAutomator_" + ip + "_All.txt"
cleaned = "clean.txt"
fileout = "fileout.txt"
cdir = os.getcwd()
state = "START"



def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def likelyHost(lines):
    #do stuff
    log.out("----- STARTING likelyHost -----")
    for line in lines:
        if constants.LIKELYHOST in line:
            likelyHost = line.partition(constants.LIKELYHOST)[2].strip()
            print("LikelyHost : "+ likelyHost)
    log.out("----- FINISHED likelyHost -----")
    return
def portScan(lines):
    lines = iter(lines)
    #do stuff
    log.out("----- STARTING portScan -----")
    portList = []
    for line in lines:
        if(line[:1].isdigit()):
            pss = line.split()
            p = pss[0].strip()
            st = pss[1].strip()
            se = pss[2].strip()
            tmpList = (p, st, se)
            portList.append(tmpList)
    print(portList)
    log.out("----- FINISHED portScan -----")
    return

def scriptRecurs(line, nextLine, lines):
    pList = []
    if (re.match('^\s', nextLine)):
        print(f'NXTLN:{nextLine}')
        line, nextLine = next(lines)
        pList.append(line)
        nextSpaces = len(nextLine) - len(nextLine.lstrip(" "))
        currSpaces = len(line) - len(line.lstrip(" "))
        if nextSpaces > currSpaces:
            lvl = lvl +1
        elif nextSpaces == currSpaces:
            lvl = lvl -1
            pass
        else:
            pass
    else:
        return pList
def scriptScan(lines):
    #do stuff
    log.out("----- STARTING scriptScan -----")
    prevSpaces = 0
    currSpaces = 0
    portList=[]
    lvl = 0
    lines = pairwise(iter(lines))
    for line, nextLine in lines:
        while (TRUE):
            print(f'L:{line}, NL:{nextLine}')
            if(line[:1].isdigit()):
                pss = line.split(maxsplit=3)
                p = pss[0].strip()
                st = pss[1].strip()
                se = pss[2].strip()
                v = pss[3].strip()
                tmpList = (p, st, se, v)
                
                #re.match(' +[^\s]+.*')
                continue
                rtrn = scriptRecurs(line, nextLine, lines)
                if len(rtrn) > 0:
                    tmpList.append(rtrn)
                portList.append(tmpList)
            else:
                continue
                
        
    print(portList)
    log.out("----- FINISHED scriptScan -----")
    return
def fullScan(lines):
    #do stuff
    log.out("----- STARTING fullScan -----")
    for line in lines:
        continue
    log.out("----- FINISHED fullScan -----")

    return
def udpScan(lines):
    #do stuff
    log.out("----- STARTING udpScan -----")
    for line in lines:
        continue
    log.out("----- FINISHED udpScan -----")

    return
def vulnsScan(lines):
    #do stuff
    log.out("----- STARTING vulnsScan -----")
    for line in lines:
        continue
    log.out("----- FINISHED vulnsScan -----")
    return
def reconRec(lines):
    #do stuff
    log.out("----- STARTING reconRec -----")
    for line in lines:
        continue
    log.out("----- FINISHED reconRec -----")
    
    return

def clearJunk():
    log.out("Clearing annoying characters and lines")
    oldLine = "a"
    with open (cdir +"/scan/"+filename, "rt" ) as fin:
        with open(cleaned, "wt") as fout:
            for line in fin:
                newLine = cleaner.replacer(line)
                #print(newLine)
                
                if newLine and newLine.isspace():#om tom string
                    if oldLine.isspace():
                        continue
                else: newLine= newLine.rstrip(" ")
                oldLine = newLine
                fout.write(newLine)
            

def stateChange(line):
    #Match line with state and change state
    global state
    for s in constants.Scans:
        if s in line.strip():
            state = s
            return TRUE
    
    return FALSE

def run():
    with open (cdir + "/" +cleaned, "rt" ) as fin:
        with open(fileout, "wt") as fout:
            lines = []
            for line in fin:
                if stateChange(line) == FALSE:
                    lines.append(line)
                else:
                    log.out2(f'State is {state}')
                    if line and line.isspace():#om tom string
                        log.out("Error, line match is empty")
                    elif state == constants.PORTSCAN:
                        likelyHost(lines)
                    elif state == constants.SCRIPTSCAN:
                        portScan(lines)
                    elif state == constants.FULLSCAN:
                        scriptScan(lines)
                    elif state == constants.UDPSCAN:
                        fullScan(lines)
                    elif state == constants.VULNSSCAN:
                        udpScan(lines)
                    elif state == constants.RECONREC:
                        vulnsScan(lines)
                    elif state == constants.RUNREC:
                        reconRec(lines)
                    lines = []
                    #fout.write(line)

def main():
    print("Starting extraction...")
    clearJunk()
    run()
    print("Extraction complete")


if __name__ == '__main__':
    sys.exit(main())