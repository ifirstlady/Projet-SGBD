#include <stdio.h>
#include <stdlib.h>
int main(){
	xmlDocPtr doc;
	xmlSchemaPtr schema = NULL;
	xmlSchemaParserCtxtPtr ctxt;
	char *XMLFileName = "fichier.xml";
	char *XSDFileName = "fichier.xsd";

	xmlLineNumbersDefault(1);

	ctxt = xmlSchemaNewParserCtxt(XSDFileName);

	xmlSchemaSetParserErrors(ctxt, (xmlSchemaValidityErrorFunc)fprintf, (xmlSchemaValidityWarningFunc)fprintf, stderr);
	schema = xmlSchemaParse(ctxt);
	xmlSchemaFreeParserCtxt();

	doc = xmlReadFile(XMLFileName);
	if(doc ==0)
	{
		fprintf(stderr, "Could not parse %s\n", XMLFileName);
	}
	else{
		xmlSchemaValidCtxtPtr ctxt;
		int ret;
		ctxt = xmlSchemaNewValidCtxt(schema);
		xmlSchemaSetValidErrors(ctxt, (xmlSchemaValidityErrorFunc)fprintf, (xmlSchemaValidityWarningFunc)fprintf, stderr);
		ret = xmlSchemaValidateDoc(ctxt, doc);
		if(ret ==0){
			printf("validate \n", XMLFileName);
		}
	}
}
