
import socket
# Import abstract ip geolocation api module
import importlib
#import json
import requests

def getIPHost():
    hostname= socket.gethostname()
    ipaddress=socket.gethostbyname(hostname)
    #print(f"{hostname}:is the computer host which has IP->  {ipaddress}")
    return  str(ipaddress)



def ipadressTotDATA(ip=getIPHost()):
    url = "https://ipgeolocation.abstractapi.com/v1"

    querystring = {"api_key":"5c45fe32a31d4b3eb701c0cecd6f689e","ip_address":ip}

    response = requests.request("GET", url, params=querystring)

    datar=response.__dict__
    #datalist=[datar["city"],datar["postal_code"],datar["country"],datar["continent"],datar["autonomous_system_organization"],datar["current_time"],datar["security"],datar["currency"]]
    #print(datar.split(","),end="\n")
    print(datar)
    # datar=str(datar)

    return str(datar)
#ipadressTotDATA()