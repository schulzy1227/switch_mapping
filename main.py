import pandas as pd
import os
import shutil

switches = ['Switch_50', 'Switch_51', 'Switch_60', 'Switch_70', 'Switch_80',
            'Switch_90', 'Switch_200', 'Switch_201', 'Switch_202', 'Switch_203']
#
parent_directory = "C:\\Switch_Charts\\"
data_file = input("Which swich needs to be mapped? (format ex: ""Switch_50"")")
# data_file = 'Switch_50'
path = os.path.join(parent_directory, data_file + '\\')
if os.path.exists(path):
    shutil.rmtree(path)
os.mkdir(path)

data_one = pd.read_csv(parent_directory + data_file + '.csv')

addresses = []
names = []
ports = []
name_ip_list = []
# generate list of dictionaries for IP address and Port pairs
def map_switches(current_switch):
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

    list_zip = zip(addresses, ports)
    final_list = list(list_zip)
    print(*final_list, sep="\n")

    with open(path + '\\' + data_file + '_final.csv', 'w') as final_file:
        for line in final_list:
            final_file.write(f"{line}\n")

    os.remove(parent_directory + data_file + '.csv')

# def main():
#     print("Mapping...")
#     for switch in switches:
#         map_switches(switch)
#
# main()


