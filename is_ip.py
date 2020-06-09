def is_ip(ip):
    try:
        ip = ip.split(".")
        check_count = 0
        for i in ip:
            if int(i) in range(0,256):
                check_count += 1
                if check_count == 4:
                    return True
    except:
        return False
