import xmltodict
import json
import requests
import xml.etree.ElementTree as ET
import pprint
route_data = []
response = requests.get('http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=umd&terse')
root = ET.fromstring(response.text)

pp = pprint.PrettyPrinter(indent=4)

for child in root:
	bus_number = child.attrib['tag']
	route_config_response = requests.get('http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=umd&r=' + bus_number + '&terse')
	route_config_xml = route_config_response.text
	route_json = xmltodict.parse(route_config_xml)['body']['route']
	route_data.append(route_json)

with open('route_config_data.json', 'w') as f:
	json.dump(route_data, f, indent=4, sort_keys=True)

schedule_data = []
for child in root:
	bus_number = child.attrib['tag']
	schedule_response = requests.get('http://webservices.nextbus.com/service/publicXMLFeed?command=schedule&a=umd&r=' + bus_number + '&terse')
	schedule_xml = schedule_response.text
	schedule_json = xmltodict.parse(schedule_xml)['body']['route']
	schedule_data.append(schedule_json)

with open('bus_schedule_data.json', 'w') as f:
	json.dump(schedule_data, f, indent=4, sort_keys=True)


# my_xml = response.text
# pp.pprint(json.dumps(xmltodict.parse(my_xml)))
	# root2 = ET.fromstring(response2.text)
	# for child in root2.iter('stop'):
	# 	print(child.attrib)

		# root3 = ET.fromstring(response3.text)
	# for child in root3.iter('stop'):
	# 	print(child)

# response2 = requests.get('http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=umd&r=118')
# root2 = ET.fromstring(response2.text)
# print(root2[0][1])
# print(root2.findall('*'))
# for child in root2.iter('stop'):
# 	print(child.attrib)	