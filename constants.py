LIKELYHOST = "Host is likely running"
#PORTSCAN = "---------------------Starting Port Scan-----------------------"
PORTSCAN = "--Starting Port Scan--"

PSS = "PORT     STATE SERVICE"
#SCRIPTSCAN = "---------------------Starting Script Scan-----------------------"
SCRIPTSCAN = "--Starting Script Scan--"

PSSV = "PORT     STATE SERVICE     VERSION"
SERVICEINFO = "Service Info:"
MACADD = "MAC Address:"
HOSTSCRIPT = "Host script results:"
#FULLSCAN = "---------------------Starting Full Scan------------------------"
FULLSCAN = "--Starting Full Scan--"

#PSS
SCRIPTEXTRA = "Making a script scan on .*"
#UDPSCAN = "----------------------Starting UDP Scan------------------------"
UDPSCAN = "--Starting UDP Scan--"

#PSS
UDPROOT = "UDP needs to be run as root, running with sudo..."
#SCRIPTEXTRA
#PSSV
VULNSSCAN = "--Starting Vulns Scan--"
RUNNINGCVE = "Running CVE scan on all ports"
#PSSV
VULNERS = "	 vulners:"
RUNVULNSCAN = "Running Vuln scan on all ports"
TAKETIME = "This may take a while, depending on the number of detected services.."
RECONREC = "--Recon Recommendations--"
WEBSERVERSRECON = "Web Servers Recon:"
SMBRECON = "SMB Recon:"
RUNREC = "--Running Recon Commands--"
Scans = (PORTSCAN, SCRIPTSCAN, FULLSCAN, UDPSCAN, VULNSSCAN, RECONREC)
