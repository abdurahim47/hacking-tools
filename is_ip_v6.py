import re

def is_ipv6(ip):
    try:
        if re.match(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ip):
            return True
    except:
        return False
