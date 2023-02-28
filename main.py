import pandas as pd

data_one = pd.read_csv('C:\\Switch_Charts\\Switch_50.csv')

addresses = []
names = []
ports = []
name_ip_list = []
# generate list of dictionaries for IP address and Port pairs
for index, row in data_one.iterrows():
    ip_add = row[0]
    switch_port = row[5]
    port_ip_pair = {ip_add: switch_port}


site_health = pd.read_csv('C:\\data_pull_downloads\\IslandView.csv', skiprows=198)
# generate list of all device IP's and their Device Names
for index, row in site_health.iterrows():
    device_name = row[1]
    ip = row[8]
    name_ip_pair = {ip: device_name}
    name_ip_list.append(name_ip_pair)

print(name_ip_list)

# for each in ip_port_list:
#     for ip, port in each.items():
#         # if value is null, replace with  X
#         if pd.isna(port):
#             port = 'x'


'''IF IP IS IN NAME_IP_LIST --> GRAB NAME AND REPLACE IP WITH NAME
    Make list of IP Address and PORT to the side {dictionary?}
    Loop through name_IP list, if IP is in list, replace IP of IP:PORT pair with Device name'''



