# fonction pour vaider la commande pour l'execution du code
def validateXJ(argv1,argv2,argv3,argv4,argv5,argv6):	
	
	try:
		if sys.argv[1]=="-i":
			print sys.argv[1]
	except Exception as e:
		argv1=False
		
	try:
		if sys.argv[2]=="xml" or sys.argv[2]=="json":
			print("")
	except Exception as e:
		argv2=False
	
	try:
		if sys.argv[3]=="-f" or sys.argv[3]=="-t":
			print("")
	except Exception as e:
		argv3=False
	
	try:
		if sys.argv[4]=="myfile.xml" or sys.argv[4]=="myfile.json" or sys.argv[4]=="f":
			print("")
	except Exception as e:
		argv4=False
	
	try:
		if sys.argv[5]=="-o" or sys.argv[5]=="myfile.xml" or sys.argv[5]=="myfile.json":
			print("")
	except Exception as e:
		argv5=False
