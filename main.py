import pandas as pd
import os
import shutil

# parent_directory = "C:\\Switch_Charts\\"
# file = input("which switch are we mapping?")
# data_file = 'Switch_50.csv'
# path = os.path.join(parent_directory, data_file + '\\')
# if os.path.exists(path):
#     shutil.rmtree(path)
# os.mkdir(path)

data_one = pd.read_csv("C:\\Switch_Charts\\Switch_50.csv", skiprows=2)

addresses = []
names = []
ports = []
name_ip_list = []
# generate list of dictionaries for IP address and Port pairs
for index, row in data_one.iterrows():
    ip_add = row[0]
    switch_port = row[5]
    ports.append(switch_port)
    addresses.append(ip_add)

    port_ip_pair = (ip_add, switch_port)


site_health = pd.read_csv('C:\\data_pull_downloads\\IslandView.csv', skiprows=198)
# generate list of all device IP's and their Device Names
for index, row in site_health.iterrows():
    device_name = row[1]
    ip = row[8]

    name_ip_pair = (ip, device_name)
    name_ip_list.append(name_ip_pair)

    for i in range(len(addresses)):
        if addresses[i] == ip:
            addresses[i] = device_name

# print(addresses)
# print(ports)
list_zip = zip(addresses, ports)
final_list = list(list_zip)
print(*final_list, sep="\n")

with open('C:\\Switch_Charts\\ports_list\\' + '50_final.txt', 'w') as final_file:
    for line in final_list:
        final_file.write(f"{line}\n")




# for each in ip_port_list:
#     for ip, port in each.items():
#         # if value is null, replace with  X
#         if pd.isna(port):
#             port = 'x'


'''IF IP IS IN NAME_IP_LIST --> GRAB NAME AND REPLACE IP WITH NAME
    Make list of IP Address and PORT to the side {dictionary?}
    Loop through name_IP list, if IP is in list, replace IP of IP:PORT pair with Device name'''



