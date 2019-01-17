import json
import svgwrite
from creationSVG import creationSVG
from pprint import pprint 
def extractionJSON(monFchier):
   tab=[]
   i=0
   with open(monFchier) as f_read:
      lst_dico = json.load(f_read)
      for key, tab in lst_dico.iteritems():
         print key
         if i==0:
            nomEntite2=key
            nom=tab
            prenom=tab
            card2=tab
         if i==1:
               nomEntite=key
               nom=tab
               prenom=tab
               card1=tab
         if i==2 :
            nomAssos=key 
            date=tab
         i=i+1
   formt="JSON"      
   creationSVG(nomEntite,nom,prenom,card1,nomEntite2,card2,nomAssos,date,formt)
   print nomEntite2
