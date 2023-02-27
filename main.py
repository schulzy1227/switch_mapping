import pandas as pd

data_one = pd.read_csv('C:\\Switch_Charts\\Switch_50.csv')

name_ip_list = []
ip_port_list = []

for index, row in data_one.iterrows():
    ip_add = row[0]
    switch_port = row[5]
    port_ip_pair = {ip_add: switch_port}
    ip_port_list.append(port_ip_pair)


site_health = pd.read_csv('C:\\data_pull_downloads\\IslandView.csv', skiprows=198)
for index, row in site_health.iterrows():
    device_name = row[1]
    ip = row[8]
    dev_ip_pair = {ip: device_name}
    name_ip_list.append(dev_ip_pair)

for each in name_ip_list:
    for k, v in each.items():
        print(k, v)
        print("hello")

# loop through selecting keys and values
# for each in ip_port_list:
#     for k, v in each.items():
#         # if value is null, replace with  X
#         if pd.isna(v):
#             v = 'x'
#     print(f'Key: {k}, Value:{v}')
