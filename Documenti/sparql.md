# SPARQL

## 1) Query che dato il nome dell'azienda tira fuori tutti i suoi prodotti

```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

SELECT ?prod WHERE{
	?prod rdf:type sipg:Product.	
	?company rdf:type sipg:Company;
		sipg:sells ?prod.
	FILTER(?company = sipg:Apple)
}
```

## 2) Query che dato il nome dell'azienda tira fuori tutte le altre aziende che lavorano per quella

```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

SELECT ?companyTo WHERE{
	?companyTo rdf:type sipg:Company.	
	?company rdf:type sipg:Company;
		sipg:manufacturesTo ?companyTo.
	FILTER(?company = sipg:Apple)
}
```

> Iterazione dell'utente "Giovanni"

## Vuole comprare uno smartphone ma l'unica sua richiesta è che deve spendere più di 600 euro e vuole vedere 
## dal meno costoso al più costoso 

```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
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
	FILTER (?v >= '600'^^xsd:float)
}
ORDER BY ?price
```

## Guarda gli smartwatch e vede con quali smartphone sono compatibili

```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
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
```

## Guarda se ci sono smartphone che coincidono con quelli che ha guardato prima

```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
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
```

## Ora ha scelto lo smartwatch e l'iphone12, vuole un altro cavo per lo smarphone e quindi ne cerca un'altro 
## uguale a quello in confezione

```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

SELECT ?smartp ?cable WHERE { 
	?cable rdf:type sipg:Cable.
	?smartp rdf:type sipg:Smartphone;
		sipg:containsInBox ?cable.
	FILTER(?smartp = sipg:iPhone12_64)
}
```

## Compra lo smartphone, lo smartwath e il cavo

> to check, insert non funziona in protege

```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

INSERT { 
	?buyer sipg:buysProduct ?smartp, ?smartw, ?cable.
} WHERE {
	?buyer rdf:type sipg:User.
	?smartp rdf:type sipg:Smartphone.
	?smartw rdf:type sipg:Smartwatch.
	?cable rdf:type sipg:Cable.
	FILTER(?buyer = sipg:Michela_CasualUser && ?smartp = sipg:iPhone12_64 && ?smartw = sipg:AppleWatchSeries6_40mm_GPS_Cellular_Nike && ?cable = sipg:Lightning_cable )
}
```

## Chiede a Siri se vendono anche cuffie della beats, la sua marca preferita (è fuori dallo store apple), 
## poi cambia idea perchè ha già passato 
## la cassa e non ha voglia di tornare dentro perchè la coda con 1m di distanza covid usciva fuori in strada

> to check, ask non funziona in protege

```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

ASK {
	?company sipg:sells ?earPlugs.
    ?earPlugs rdf:type sipg:EarPlugs.	
	?company rdf:type sipg:Company.	
	?brand rdf:type sipg:Company;
		sipg:isBrandOf ?earPlugs.
	FILTER(?company = sipg:Apple && ?brand = sipg:BeatsAudio).
}
```

## Presa dalla felicità del suo nuovo smartphone acquistato si chiede qual è il profilo ig per seguirlo

```SPARQL
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?company ?labelCompany ?labelbrand ?usernameIG WHERE {      
    ?device rdf:type sipg:Device;
            sipg:hasBrand ?brand.
    ?brand rdf:type sipg:Company;
           rdfs:label ?labelbrand.
    SERVICE <https://query.wikidata.org/sparql> {       
        ?company wdt:P31 wd:Q4830453;
            wdt:P2003 ?usernameIG;
            rdfs:label ?labelCompany.
        FILTER (?device = sipg:iPhone12_64 && lang(?labelCompany) = "it" && STR(?labelCompany) = STR(?labelbrand)).
    } 
}
```

## Fa il reso dello smartwatch 

```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

DELETE { 
	?buyer sipg:buysProduct ?smartw.
} WHERE {
	?smartw rdf:type sipg:Smartwatch.
	FILTER(?buyer = sipg:Michela_CasualUser && ?smartw = sipg:AppleWatchSeries6_40mm_GPS_Cellular_Nike)
}
```

## Cerca un tablet apple (solo se necessario)
> boh

## Compra un ipad e un altro cavo se è diverso da quello di iphone12 che ha già comprato (solo se necessario)
> boh


## dato l'iphone che ha appena comprato, vuole sapere quali altri dispositivi montano lo stesso chip

```SPARQL
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

SELECT ?prod ?label WHERE {      
    ?device sipg:CpuType ?cpu.
    SERVICE <https://query.wikidata.org/sparql> {       
        ?chip wdt:P31 wd:Q610398;
          rdfs:label ?label;
          wdt:P1535 ?prod.   
        FILTER (?device = sipg:iPhone12_64 && lang(?label) = "it" && regex(?label, ?cpu)).
    } 
}
```

## dato utente, return prods

```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

SELECT ?prod WHERE{	
	?user rdf:type sipg:User;
		sipg:buysProduct ?prod.
	FILTER (?user = sipg:Michela_CasualUser)
}
```