def query1(company: str):
    return "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\
            PREFIX owl: <http://www.w3.org/2002/07/owl#>\
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\
            PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>\
            SELECT ?prod WHERE{\
                ?prod rdf:type sipg:Product.\
                ?company rdf:type sipg:Company;\
                sipg:sells ?prod.\
            FILTER(?company = sipg:" + company + ")\
            }"


def query2(company: str):
    return "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\
            PREFIX owl: <http://www.w3.org/2002/07/owl#>\
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\
            PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>\
            SELECT ?companyTo WHERE{\
                ?companyTo rdf:type sipg:Company.\
                ?company rdf:type sipg:Company;\
                sipg:manufacturesTo ?companyTo.\
                FILTER(?company = sipg:" + company + ")\
            }"
