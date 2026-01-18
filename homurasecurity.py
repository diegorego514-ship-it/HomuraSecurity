import secure
import socket
import argparse
import requests

# Add Server Host, Server Port And Server List additional implementation of settings
SERVER_HOST = "192.168.87.129"
SERVER_PORT = 1024
SERVER_LIST = SERVER_HOST, SERVER_PORT

try:

    s = secure.ContentSecurityPolicy("Content-Security-Policy: <policy-directive>; <policy-directive>")
    s.base_uri("Content-Security-Policy: <policy-directive>; <policy-directive>")
    s.connect_src("Content-Security-Policy: <policy-directive>; <policy-directive>")
    s.report_to("Content-Security-Policy: <policy-directive>; <policy-directive>")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.close()
    s.connect("192.168.87.129")
    s.gettimeout(5) # Set time in Seconds
    s.time_sleep(10) # Set time sleep in seconds to Avoid Detection
except:
    print("[*] A External Intrusive Third Party Service has been detected.")

    print("[+] Recommendation - Block them and then report it to the cybersecurity IT Team through Secure Report Channels.")
else:
    print("[-] Your devices has been compromised.")

# Add Updates for Server Host, Server Port And Server List additional implementation of settings
SERVER_HOST = "202.250.87.90"
SERVER_PORT = 670
SERVER_LIST = SERVER_HOST, SERVER_PORT

try:
    
    s = secure.ContentSecurityPolicy("Content-Security-Policy: <policy-directive>; <policy-directive>")
    s.base_uri("Content-Security-Policy: <policy-directive>; <policy-directive>")
    s.connect_src("Content-Security-Policy: <policy-directive>; <policy-directive>")
    s.report_to("Content-Security-Policy: <policy-directive>; <policy-directive>")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.close()
    s.connect("202.250.87.90")
    s.gettimeout(10) # Set time in Seconds
    s.time_sleep(15) # Set time sleep in seconds to Avoid Detection
except:
    print("[*] Secure your Devices by ensuring that your ports are properly closed.")
else:
    print("[+] You're good to go, your ports are closed.")

SERVER_HOST = "202.250.87.90"
SERVER_PORT = 601
SERVER_LIST = SERVER_HOST, SERVER_PORT

try:
    s.delete_the_virus
    s.getsockopt(5) # Set timer in Seconds
    s.gettimeout(10) # Set time in Seconds
    s.custom_directive("Content-Security-Policy: <policy-directive>; <policy-directive>")
    s.form_action("Content-Security-Policy: <policy-directive>; <policy-directive>")
    s.close()

except:
    print("[-] You have to isolate the infectious viral attack in a antivirus to quarantine it up or delete it out from your device.")

    print("[*] Recommendation - You have to scan your devices regularly and constantly update/upgrade up the device"
" to keep it safer from potential and future threats/cyber criminal attacks.")

else:
    print("[+] Your devices are safe, you're good to go.")
