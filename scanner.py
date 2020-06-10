import nmap

user_tgt = input("Enter a valid IP to scan: ")
target = str(user_tgt)

user_input = input("Enter ports you wish to scan separated by a space: ")
ports = [int(i) if i.isdigit() else i for i in user_input.split()]

scan_v = nmap.PortScanner()

print("\nScanning "+target+" on ports: "+str(ports))

for port in ports:
    portscan = scan_v.scan(target,str(port))
    print("Port",port,"is",portscan['scan'][target]['tcp'][port]['state'])

print("\nHost",target,"is",portscan['scan'][target]['status']['state'])
