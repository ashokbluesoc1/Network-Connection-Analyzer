file = open("network.log")
suspicious_ports={"4444","1337","31337"}
connection_count={}
CONNECTION_THRESHOLD = 5
alerted_connections = set()
for line in file:
    parts = line.split("|")
    src_ip = parts[0].strip().split("=")[1]
    src_port =parts[1].strip().split("=")[1]
    dest_ip = parts[2].strip().split("=")[1]
    dest_port = parts[3].strip().split("=")[1]
    protocol = parts[4].strip().split("=")[1]
    connection = (src_ip, dest_ip, dest_port)
    if connection in connection_count: 
        connection_count[connection] += 1
    else:
        connection_count[connection] = 1
    if dest_port in suspicious_ports and connection not in alerted_connections:
         print("⚠️  Connecetion to suspicious port ")
         print("Source IP:", src_ip)
         print("Destination IP:", dest_ip)
         print("Destination port:", dest_port)
         print("Connection count:", connection_count[connection])
         print("Action : investigate communication")
    if connection_count[connection] >= CONNECTION_THRESHOLD and connection not in alerted_connections:

        print("\n⚠️  REPEATED CONNECTION ALERT")
        print("Source IP:", src_ip)
        print("Destination IP:", dest_ip)
        print("Connection count:", connection_count[connection])
        print("Action: Investigate repeated communication")
        alerted_connections.add(connection)
