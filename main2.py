from asyncio import protocols
from collections import defaultdict
from ctypes import sizeof
from curses.ascii import isspace
from ensurepip import version
import os
from pickle import FALSE, TRUE
import sys
from itertools import tee
import re
import fileCleaner as cleaner
import constants
import log
import pprint
import json

ip = "192.168.56.0"
filename3 = "nmapAutomator_192.168.56.0_All.txt"
filename2 = "test.txt"
filename = "nmapAutomator_" + ip + "_All.txt"
cleaned = "clean.txt"
fileout = "fileout.txt"
cdir = os.getcwd()
scanState = "START"

unknown = "?"
ports = "Ports"
protocol = "Protocol"
state = "State"
service = "Service"
vers = "Version"


tree = lambda: defaultdict(tree)


class Tree(defaultdict):
    def __init__(self, value=None):
        super(Tree, self).__init__(Tree)
        self.value = value
class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)() # retain local pointer to value
        return value                     # faster to return than dict lookup
dict = tree()

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def indentReader(lines):
    indentation = []
    data = []
    data.append([])
    indentation.append(0)
    depth = 0

    for line in lines:
        line = line[:-1]

        content = line.strip()
        content = content.rstrip(':')
        indent = len(line) - len(line.lstrip())
        if indent > indentation[-1]:
            depth += 1
            indentation.append(indent)
            data.append([])

        elif indent < indentation[-1]:
            while indent < indentation[-1]:
                depth -= 1
                indentation.pop()
                top = data.pop()
                data[-1].append(top)

            if indent != indentation[-1]:
                raise RuntimeError("Bad formatting")

        data[-1].append(content)

    while len(data) > 1:
        top = data.pop()
        data[-1].append(top)
    return data[0]

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
    data = []

    data.append(indentReader(lines))
    print(len(data))
    print_list(data[0])
    """portList = []
    for line in lines:
        if(line[:1].isdigit()):
            pss = line.split()
            pp = pss[0].strip().split("/")
            prt = pp[0]
            proto = pp[1]
            st = pss[1].strip()
            se = pss[2].strip()
            tmpList = (prt, proto, st, se)
            portList.append(tmpList)
            
            #ps = "portScan"
            #dict[ports][prt][protocol][ps] = proto
            #dict[ports][prt][state][ps] = st
            #dict[ports][prt][service][ps] = se
            #dict[ports][prt][vers][ps] = unknown
            
            #tmpDict["Protocol"].append(prot)
            #tmpDict["State"].append(st)
            #tmpDict["Service"].append(se)
            #tmpDict["Version"]
            #print("---------items------")
            #print(tmpDict.items())
            #dict[port] = tmpDict.items()
    print(portList)
    """
    #pprint.pprint(dict, indent = 1)
    #print(dict.items())
    #pprint.pp(json.dumps(dict))
    log.out("----- FINISHED portScan -----")
    return


""" 
def scriptRecurs(line, nextLine, lines):
    pList = []
    if (re.match('^\s', nextLine)):
        print(f'NXTLN:{nextLine}')
        line, nextLine = next(lines)
        pList.append(line)
        nextSpaces = tab_lvl(nextLine)
        currSpaces = tab_lvl(line)
        if nextSpaces > currSpaces:
            pass
        elif nextSpaces == currSpaces:
            pass
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
            #print(f'L:{line}, NL:{nextLine}')
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
                break
                
        
    print(portList)
    log.out("----- FINISHED scriptScan -----")
    return """

def print_list(lst, level=0):
    for l in lst:
        if type(l) is list:
            print_list(l, level + 1)
        else:
            print('\t' * level + l)

def scriptScan(lines):
    log.out("----- STARTING scriptScan -----")
    for line in lines:
        print(line)
    data = []

    data.append(indentReader(lines))
    print(len(data))
    print_list(data[0])
    #Om content börjar med 
    log.out("----- FINISHED scriptScan -----")

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
                newLines = []
                updatedLine = cleaner.replacer(line)
                if(type(updatedLine) is list):
                    newLines.extend(updatedLine)
                else:
                    newLines.append(updatedLine)
                for newLine in newLines:
                    #print("line: " + newLine)
                    if newLine and newLine.isspace():#om tom string
                        if oldLine.isspace():
                            continue
                    else: newLine= newLine.rstrip(" ")
                    oldLine = newLine
                    fout.write(newLine)
            

def stateChange(line):
    #Match line with scanState and change scanState
    global scanState
    for s in constants.Scans:
        if s in line.strip():
            scanState = s
            return TRUE
    
    return FALSE

def run():
    with open (cdir + "/" +cleaned, "rt" ) as fin:
        with open(fileout, "wt") as fout:
            lines = []
            for line in fin:
                if stateChange(line) == FALSE:
                    if not line.isspace():
                        lines.append(line)
                else:
                    log.out2(f'scanState is {scanState}')
                    if line and line.isspace():#om tom string
                        log.out("Error, line match is empty")
                    elif scanState == constants.PORTSCAN:
                        likelyHost(lines)
                    elif scanState == constants.SCRIPTSCAN:
                        portScan(lines)
                    elif scanState == constants.FULLSCAN:
                        scriptScanResult = scriptScan(lines)
                        print(scriptScanResult)
                    elif scanState == constants.UDPSCAN:
                        fullScan(lines)
                    elif scanState == constants.VULNSSCAN:
                        udpScan(lines)
                    elif scanState == constants.RECONREC:
                        vulnsScan(lines)
                    elif scanState == constants.RUNREC:
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