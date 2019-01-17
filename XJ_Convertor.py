import sys
import xml.etree.ElementTree as ET
import requests
from extractionXML import extraciontXML
from validateXJ import validateXJ
from extractionJSON import extractionJSON

fichierJson="myfile.json"
argv1=True
argv2=True
argv3=True
argv4=True
argv5=True
argv6=True
#Fonction de validation de XJ_CONVERTOR
validateXJ(argv1,argv2,argv3,argv4,argv5,argv6)

#Validation et extraction du fichier XML
def validateXml():
		if sys.argv[4]=="myfile.xml":
			tree = ET.parse(sys.argv[4])
			root = tree.getroot()
			extractionXML(root,arg3)
		if sys.argv[5]=="myfile.xml":
			tree = ET.parse(sys.argv[5])
			root = tree.getroot()
			extractionXML(root,arg3)
	
#Verification des arguments en entrée
if (sys.argv[0]=="XJ_Convertor.py" and argv1 and argv2 and argv3 and argv4 and argv5 and argv6):
	if sys.argv[2]=="xml":
		arg3=sys.argv[3]
		validateXml()
	else:
		extractionJSON(fichierJson)

else :
	print (" Commande incorrecte!")
	print (" Elle est sous la forme : XJ_Convertor [-i] [xml/json] [-t] [-h url_FluxHTTP] [-f FichierInput] -o nomFichier.svg")
