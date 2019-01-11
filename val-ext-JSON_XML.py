from json import loads
from sys import argv
import xml.etree.ElementTree as ET

#Debut de la fonction qui permet de valider le fichier Json
def validateJson(file):
        try: 
            json_data=open(file).read()
            json.loads(json_data)
            return True
        except: 
            print ('le fichier est mal formate')
            return False

#Fin de la fonction

#Debut de la fonction qui permet de valider le fichier XML
def validateXML(file):
    try: 
        xml_file = ET.ElementTree(file = file)
        return True
    except: 
        print ('le fichier est mal formate')
        return False

#Fin de la fonction

#Debut fonction extraction
def ExtraireXml(file):
    print (argv[1])
    validateXML(file)
    file_xml = ET.ElementTree(file = file)
    root = file_xml.getroot()
    print (root.attrib)

ExtraireXml(argv[1])
