#! /usr/bin/python3

import ftplib
import time ,os, xml.etree.ElementTree as et
import xml.dom.minidom, secrets



def getFile():
    username = 'admin'
    password= secrets.token_hex(16)
    file_name = input("Enter the name of the file along with it's extension: ")

    ftp = ftplib.FTP('<IP-ADDRESS>')
    ftp.login(username, password)
    ftp.cwd('Jeff_1/PYTHON_STUFF')

    time.sleep(1)
    ftp.dir()

    with open(file_name, 'wb') as ftp_file:
        ftp.retrbinary(f'RETR {file_name}', lambda data: ftp_file.write(data))

    with open(file_name, 'a') as file_update:
        file_update.writelines("\nline2")


base_path = os.path.dirname(os.path.realpath(__file__))
xml_path = 'G:\\<PATH>\\000000000000-directory.xml'

xml_file = os.path.join(base_path, xml_path)
tree = et.parse(xml_file)

root = tree.getroot()

item_list = root.find('item_list')
item = et.SubElement(item_list, 'item')

fn = et.SubElement(item, 'fn')
fn.text = 'Jeffrey McIntyre'

ct = et.SubElement(item, 'ct')
ct.text = "9688"

output = tree.write(xml_path)

with open('000000000000-directory.xml','r') as xmlfile:
    myxml = xml.dom.minidom.parseString(xmlfile.read())
    prettified = myxml.toprettyxml()

print(prettified)


