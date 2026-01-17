import secure
import socket
import argparse
import requests

# Add Server Host, Server Port And Server List additional implementation of settings
SERVER_HOST = "192.168.87.129"
SERVER_PORT = 5003
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
    print("[!] A External Intrusive Third Party Service has been detected.")

    print("[*] Recommendation - Block them and then report it to the cybersecurity IT Team through Secure Report Channels.")
else:
    print("[-] Your devices has been compromised.")
