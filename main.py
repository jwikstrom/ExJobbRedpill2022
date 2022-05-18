from curses.ascii import isspace
from distutils.command.clean import clean
import os
from sre_parse import State
import sys
from tkinter.messagebox import NO

from sqlalchemy import false, true
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



def likelyHost(fin):
    #do stuff
    line = fin.readline().rstrip()
    #log.out("----- STARTING likelyHost -----")
    print("in likely")
    
    while (line):
        print("in while")
        print("+"+line)
        if (constants.LIKELYHOST in line):
            likelyHost = line.partition(constants.LIKELYHOST)[2].strip()
            print("LikelyHost : "+ likelyHost)
        else: print("No")
        line = fin.readline().rstrip()
        print("<" + line)
        for i in range(0,3):
            if not line:
                line = fin.readline().rstrip()
                print(">"+line)
                print(i)
            else: break

        
        if stateChange(line): break
        else: continue
    #log.out("----- FINISHED likelyHost -----")
    return fin
def portScan(line, fin):
    #do stuff
    #log.out("----- STARTING portScan -----")
    portList = []
    while line and not stateChange(line):
        if(line[:1].isdigit()):
            pss = line.split()
            port = pss[0].strip()
            state = pss[1].strip()
            service = pss[2].strip()
            tmpList = (port, state, service)
            portList.append(tmpList)
            #print(f'p: {port}, st: {state}, se: {service}')
        line = fin.readline()
        
    #log.out("----- FINISHED portScan -----")
    print(portList)
    return fin
def scriptScan(line, fin):
    #do stuff
    prevSpaces = 0
    #log.out("----- STARTING scriptScan -----")
    
    while line and not stateChange(line):
        currSpaces = len(line) - len(line.lstrip(" "))
        if prevSpaces > currSpaces:
            continue
        line = fin.readline()
        
    #log.out("----- FINISHED scriptScan -----")
    return fin
def fullScan(line, fin):
    #do stuff
    #log.out("----- STARTING fullScan -----")
    while line and not stateChange(line):
        line = fin.readline()
    #log.out("----- FINISHED fullScan -----")

    return fin
def udpScan(line, fin):
    #do stuff
    #log.out("----- STARTING udpScan -----")
    while line and not stateChange(line):
        line = fin.readline()
    #log.out("----- FINISHED udpScan -----")

    return fin
def vulnsScan(line, fin):
    #do stuff
    #log.out("----- STARTING vulnsScan -----")
    while line and not stateChange(line):
        line = fin.readline()
    #log.out("----- FINISHED vulnsScan -----")
    return fin
def reconRec(line, fin):
    #do stuff
    #log.out("----- STARTING reconRec -----")
    while line and not stateChange(line):
        line = fin.readline()
    #log.out("----- FINISHED reconRec -----")
    return fin

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
            

def stateChange(l):
    #Match line with state and change state
    global state
    line = l
    print("SC:" + line)
    if constants.RUNREC in line :
        state = "END"
        log.out2(f'State is {state}')
        return true
    for s in constants.Scans:
        if s in line:
            state = s
            log.out2(f'State is {state}')
            return true
    return false

def run():
    with open (cdir + "/" +cleaned, "rt" ) as fin:
        with open(fileout, "wt") as fout:
            line = fin.readline()
            print(state)
            
            while line:
                #print(newLine)
                if state == "START":
                    fin = likelyHost(fin)
                elif state == constants.PORTSCAN:
                    fin = portScan(line, fin)
                elif state == constants.SCRIPTSCAN:
                    return
                    fin = scriptScan(line, fin)
                elif state == constants.FULLSCAN:
                    fin = fullScan(line, fin)
                elif state == constants.UDPSCAN:
                    fin = udpScan(line, fin)
                elif state == constants.VULNSSCAN:
                    fin = vulnsScan(line, fin)
                elif state == constants.RECONREC:
                    fin = reconRec(line, fin)
                elif state == "END":
                    return
                line = fin.readline()
                #fout.write(line)
            

def main():
    print("Starting extraction...")
    clearJunk()
    run()
    print("Extraction complete")


if __name__ == '__main__':
    sys.exit(main())