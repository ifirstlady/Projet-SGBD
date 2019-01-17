import svgwrite
from creationSVG import creationSVG
#fonction pour l'extraction des donnes au niveau du fichier XML
def extractionXML(root,arg3):
	
	#PARCOURIR LE FICHIER XML AFIN DE RECUPERER LES ENTITES ET LES ASSOCIATIONS ET LEURS ATTRIBUTS

	for entite1 in root.findall('entite1'):
	 
	    
	    nomEntite = entite1.find('nomEntite').text
	    for attribut in entite1.findall('attribut'):
	     	ide = attribut.find('id').text
	     	nom = attribut.find('nom').text
	    	prenom = attribut.find('prenom').text
	    card1 = entite1.find('cardinalite').text
	
	
	for entite2 in root.findall('entite2'):
	     
	    
	    nomEntite2 = entite2.find('nomEntite').text
	    for attribut in entite2.findall('attribut'):
	     	ide2 = attribut.find('id').text
	     	nom = attribut.find('nom').text
	    	prenom = attribut.find('prenom').text
	    card2 = entite2.find('cardinalite').text
	
	for association in root.findall('association'):
	     
	    
	    nomAssos = association.find('nomAssos').text
	    for attribut in association.findall('attribut'):
	    	date = attribut.find('date').text
	
	#trace du fichier xml
	if arg3=="-t" :
	  	print nomEntite
		print ide
		print nom
		print prenom
		print card1
		
	  	print nomEntite2
		print ide2
		print nom
		print prenom
		print card2
	
		print nomAssos
		print date
		#CREATION DU FICHIER SVG
	formt="XML"
        creationSVG(nomEntite,nom,prenom,card1,nomEntite2,card2,nomAssos,date,formt)
