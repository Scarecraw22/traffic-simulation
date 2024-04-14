import xml.etree.ElementTree as ET

speeds = {
    "20": "5.55",
    "30": "8.33",
    "40": "11.11",
    "50": "13.89",
    "60": "16.67",
    "70": "19.44",
}
net_file_path = 'custom.net.xml'

for km_speed, speed in speeds.items():
    tree = ET.parse(net_file_path)
    root = tree.getroot()

    for lane in root.iter('lane'):
        lane.set('speed', speed)

    tree.write(f'{km_speed}/custom_{km_speed}.net.xml')

