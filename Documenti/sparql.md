#SPARQL

## 1) Query che dato il nome dell'azienda tira fuori tutti i suoi prodotti
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

SELECT ?prod WHERE{
	?prod rdf:type sipg:Product.	
	?company rdf:type sipg:Company;
		sipg:sells ?prod.
	FILTER(?company = sipg:Apple)
}

## 2) Query che dato il nome dell'azienda tira fuori tutte le altre aziende che lavorano per quella
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

SELECT ?companyTo WHERE{
	?companyTo rdf:type sipg:Company.	
	?company rdf:type sipg:Company;
		sipg:manufacturesTo ?companyTo.
	FILTER(?company = sipg:Apple)
}

> Iterazione dell'utente "Giovanni"

## Vuole comprare uno smartphone ma l'unica sua richiesta è che deve spendere più di 600 euro e vuole vedere 
## dal meno costoso al più costoso 

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>
PREFIX price: <http://www.ontologydesignpatterns.org/cp/owl/price.owl#>

SELECT ?prod ?brand ?price WHERE { 
	?brand rdf:type sipg:Company.
	?price rdf:type price:Price;
		price:hasValue ?v.
	?prod rdf:type sipg:Smartphone;
		sipg:hasBrand ?brand;
		price:hasPrice ?price.
	FILTER (?v >= "600"^^xsd:float)
}
ORDER BY ?price

## guarda gli smartwatch e vede con quali smartphone sono compatibili
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>
PREFIX price: <http://www.ontologydesignpatterns.org/cp/owl/price.owl#>

SELECT ?smartw ?brand ?pricesmartw ?smartp WHERE { 
	?brand rdf:type sipg:Company.
	?pricesmartw rdf:type price:Price.
	?smartp rdf:type sipg:Smartphone.
	?smartw rdf:type sipg:Smartwatch;
		sipg:compatibleWith ?smartp;
		sipg:hasBrand ?brand;
		price:hasPrice ?pricesmartw.
}

## guarda se ci sono smartphone che coincidono con quelli che ha guardato prima
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>
PREFIX price: <http://www.ontologydesignpatterns.org/cp/owl/price.owl#>

SELECT ?smartw ?brand ?pricesmartw ?smartp ?pricesmartp WHERE { 
	?brand rdf:type sipg:Company.
	?pricesmartw rdf:type price:Price.
	?pricesmartp rdf:type price:Price;
		price:hasValue ?vsmartp.
	?smartp rdf:type sipg:Smartphone;
		price:hasPrice ?pricesmartp.
	?smartw rdf:type sipg:Smartwatch;
		sipg:compatibleWith ?smartp;
		sipg:hasBrand ?brand;
		price:hasPrice ?pricesmartw.
	FILTER (?vsmartp >= "600"^^xsd:float)
}

## ora ha scelto lo smartwatch e l'iphone12, vuole un altro cavo per lo smarphone e quindi ne cerca un'altro 
## uguale a quello in confezione
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

SELECT ?smartp ?cable WHERE { 
	?cable rdf:type sipg:Cable.
	?smartp rdf:type sipg:Smartphone;
		sipg:containsInBox ?cable.
	FILTER(?smartp = sipg:iPhone12_64)
}

## compra lo smartphone, lo smartwath e il cavo
> to check, insert non funziona in protege

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

INSERT DATA{ 
	?buyer sipg:buysProduct ?smartp.
	?buyer sipg:buysProduct ?smartw.
	?buyer sipg:buysProduct ?cable.
}
WHERE {
	?buyer rdf:type sipg:User.
	?smartp rdf:type sipg:Smartphone;
	?smartw rdf:type sipg:Smartwatch;
	?cable rdf:type sipg:Cable.
	FILTER(?buyer = sipg:Michela && ?smartp = sipg:iPhone12_64 && ?smartw = sipg:AppleWatchSeries6_40mm_GPS_Cellular_Nike && ?cable = sipg:Lightning_cable )
}


## chiede a Siri se vendono anche cuffie della beats, la sua marca preferita (è fuori dallo store apple), 
## poi cambia idea perchè ha già passato 
## la cassa e non ha voglia di tornare dentro perchè la coda con 1m di distanza covid usciva fuori in strada
> to check, ask non funziona in protege

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

ASK {
	?company sipg:sells ?earPlugs.
}
WHERE{
	?earPlugs rdf:type sipg:EarPlugs.	
	?company rdf:type sipg:Company.	
	?brand rdf:type sipg:Company;
		sipg:isBrandOf ?earPlugs.
	FILTER(?company = sipg:Apple && ?brand = sip:BeatsAudio)
}

## presa dalla felicità del suo nuovo smartphone acquistato si chiede qual è il profilo ig per seguirlo
> da fare

PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX p: <http://www.wikidata.org/prop/>
PREFIX v: <http://www.wikidata.org/prop/statement/>

SELECT ?usernameIG ?label WHERE {
	wd:Q312 wdt:P2003 ?usernameIG;
            rdfs:label ?label 
    FILTER (lang(?label) = "it").
}

## trovando apple su ig vede i prodotti della beats nella stessa pagina e trova il profilo ig di beats (trova lo user)
## si chiede quindi quali altri prodotti ha fatto l'azienda per fantasticare per il prossimo acquisto 
## (oppure il sito ufficiale)
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX p: <http://www.wikidata.org/prop/>
PREFIX v: <http://www.wikidata.org/prop/statement/>

SELECT ?company ?prod WHERE {
	?company wdt:P2003 ?usernameIG;
             wdt:P1056 ?prod.
    FILTER (?usernameIG = "beatsbydre").
}
> oppure

PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX p: <http://www.wikidata.org/prop/>
PREFIX v: <http://www.wikidata.org/prop/statement/>

SELECT ?company ?website WHERE {
	?company wdt:P2003 ?usernameIG; 
             wdt:P856 ?website.
    FILTER (?usernameIG = "beatsbydre").
}
## fa il reso dello smartwatch
DELETE buysProduct

## cerca un tablet apple
> boh

## compra un ipad e un altro cavo se è diverso da quello di iphone12 che ha già comprato
> boh
