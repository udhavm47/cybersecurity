import nmap;
import sys;
import socket;
from tabulate import tabulate;
from prettytable import PrettyTable;

target =str(sys.argv[1])
target_ip = socket.gethostbyname(target);
ports = [21,22,80,139,443,8080]

scan = nmap.PortScanner();

print(f'\nScanning {target} for well known ports and services........')
print("\n")
print(f'Target IP: {target_ip}')
print('\n')
#print(f' Port\t\t\tService\t\t\tstatus ')
rows = PrettyTable(["Port", "Service", "Status"])


for port in ports:
    try:
        scan_result = scan.scan(target_ip,str(port))
        service = scan_result['scan'][target_ip]['tcp'][port]['name']
        status = scan_result['scan'][target_ip]['tcp'][port]['state']
        print(f'Port {port} is {status} ')
        # data = [port,service,status]
        # print(tabulate(data,headers=rows, tablefmt="grid"))
        rows.add_row([port,service,status])
        #print(rows);
    except KeyboardInterrupt:
        print("\n Exitting!!")
        sys.exit()
print(rows);        
print(f"Target {target} is up")