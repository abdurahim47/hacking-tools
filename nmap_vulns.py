import os
import subprocess as sp
import re

def get_whatever():
	try:
		print("="*20,"Test for ssl-heartbleed or smb","="*20)
		url    = input("Type Url(Type like www.google.com)      >> ")
		script = input("Type Script Name(type hb or smb)        >> ")

		if re.search(r"(www\.([\w.]+))",url):
			result = []
			for x in sp.check_output(["ping",url]).split():
				try:
					result.append(bytes.decode(x))
				except:
					pass
			ip = []
			for x in result:
				if re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",x):
					if ("[" or "]") not in x:
						ip.append(x)
			ip = list(set(ip))
		if script == "hb" or script == "smb":
			script = "ssl-heartbleed" if "hb" else "smb-vuln-cve2009-3103"
		if ip and script:
			if script == "ssl-heartbleed":
				for x in range(len(ip)):
					os.system("nmap -sS -n -p 443 --script ssl-heartbleed " + ip[x])
			elif script == "smb-vuln-cve2009-3103":
				for x in range(len(ip)):
					os.system("nmap -n -p 445 --script smb-vuln-cve2009-3103 " + ip[x])
	except Exception as e:
		raise e

get_whatever()
