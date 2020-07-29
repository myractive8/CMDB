import nmap
nm = nmap.PortScanner()
result = nm.scan(hosts='192.168.1.0/24',arguments='-n -sP')
print(result)

print("nmap的命令行：",nm.command_line())

print("主机清单：",nm.all_hosts())

print("查看指定主机的信息：",nm['192.168.1.30'])