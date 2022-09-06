# import requests

# res = requests.get('https://172.15.255.128:54600')

# if res:
# print('Response OK')
# else:
# print('Response Failed')
# print(res.status_code)

import xml.etree.ElementTree as xml

def createXML(filename):
    # создаем XML файл
    root = xml.Element("zAppointments")
    appt = xml.Element("appointment")
    root.append(appt)

    # создаем дочерний элемент begin
    begin = xml.SubElement(appt, "begin")
    begin.text = "1181251680"

    # создаем дочерний элемент uid
    uid = xml.SubElement(appt, "uid")
    uid.text = "040000008200E000"

    # создаем дочерний элемент alarmTime
    alarmTime = xml.SubElement(appt, "alarmTime")
    alarmTime.text = "1181572063"

    # создаем дочерний элемент state
    state = xml.SubElement(appt, "state")

    # создаем дочерний элемент location
    location = xml.SubElement(appt, "location")

    # создаем дочерний элемент duration
    duration = xml.SubElement(appt, "duration")
    duration.text = "1800"

    # создаем дочерний элемент subject
    subject = xml.SubElement(appt, "subject")

    # записываем XML в файл
    tree = xml.ElementTree(root)
    tree.write("sample.xml")

createXML("appt.xml")
dir('createXML')
