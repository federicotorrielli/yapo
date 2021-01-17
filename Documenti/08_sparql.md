---

# PARTE II

# Flusso d'iterazione utente

## Iterazione Utente

![Operazioni utente](https://i.postimg.cc/pVcdKR4V/iteration-schema.png)

## Schema di interfaccia: CLI ed esempi reali

![CLI](https://i.postimg.cc/PfCHsZVh/cli.png)

## SPARQL

### Operazione 1

Descrizione:
dato il nome dell'azienda, restituisce tutti i prodotti che vende.

Query:
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

Return:
-   productCatalog:AirPods_wirelessCharge
-   productCatalog:AppleWatchSeries6_40mm_GPS_Cellular_Nike
-   productCatalog:Lightning_cable
-   productCatalog:IpadAir_2020
-   productCatalog:Iphone11_64
-   productCatalog:MacBookAir_M1
-   productCatalog:iMac_27_RetinaDisplay_5k_256
-   productCatalog:iPhone12_64
-   productCatalog:iPhoneX_64
-   productCatalog:Beats_cuffie

### Operazione 2

Descrizione:
data una soglia di prezzo base P, restituisce tutti gli smartphone 
con prezzo >= P e relativi azienda e prezzo prodotto ordinati per prezzo ASC.

Query:
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

Return:
-   productCatalog:Iphone11_64
    productCatalog:Apple
	productCatalog:600Euro
-   productCatalog:iPhone12_64
	productCatalog:Apple
	productCatalog:800Euro
-   productCatalog:SamsungGalaxyS20_5G_global
	productCatalog:Samsung
	productCatalog:800Euro

### Operazione 3

Descrizione:
restituisce gli smartwatch che sono compatibili con uno smartphone,
visualizza smartwatch, brand smartwatch, prezzo smartwatch, smartphone compatibile.

Query:
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

Return:
-   productCatalog:AppleWatchSeries6_40mm_GPS_Cellular_Nike
	productCatalog:Apple
	productCatalog:500Euro
	productCatalog:Iphone11_64
-   productCatalog:AppleWatchSeries6_40mm_GPS_Cellular_Nike
	productCatalog:Apple
	productCatalog:500Euro
	productCatalog:iPhone12_64
-   productCatalog:AppleWatchSeries6_40mm_GPS_Cellular_Nike
	productCatalog:Apple
	productCatalog:500Euro
	productCatalog:iPhoneX_64

### Operazione 4

Descrizione:
dato un prezzo base P per gli smarphone, restituisce gli smartwatch
compatibili con gli smartphone con prezzo >= P, il brand dello smartwatch e i prezzi
dei due dispositivi. Ordinato per prezzo smartphone crescente.

Query:
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

Return:
-   productCatalog:AppleWatchSeries6_40mm_GPS_Cellular_Nike
	productCatalog:Apple
	productCatalog:500Euro
	productCatalog:Iphone11_64
	productCatalog:600Euro
-   productCatalog:AppleWatchSeries6_40mm_GPS_Cellular_Nike
	productCatalog:Apple
	productCatalog:500Euro
	productCatalog:iPhone12_64
	productCatalog:800Euro

### Operazione 5

Descrizione:
data la scelta di uno smartphone in particolare, restituisce il cavo 
che è contenuto all'interno della confezione di vendita.

Query:
```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

SELECT ?smartp ?cable WHERE { 
	?cable rdf:type sipg:Cable.
	?smartp rdf:type sipg:Smartphone;
		sipg:containsInBox ?cable.
	FILTER(?smartp = sipg:Iphone11_64)
}
```

Return:
-   productCatalog:Iphone11_64
	productCatalog:Lightning_cable

### Operazione 6

Descrizione:
restituisce se nel catalogo Apple ci sono anche cuffie della BeatsAudio.

Query:
```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

ASK {
	?company rdf:type sipg:Company;
	    sipg:sells ?earPlugs.
    ?earPlugs rdf:type sipg:EarPlugs.	
	?brand rdf:type sipg:Company;
		sipg:isBrandOf ?earPlugs.
	FILTER(?company = sipg:Apple && ?brand = sipg:BeatsAudio).
}
```

Return:
-   YES

### Operazione 7

Descrizione:
data la scelta di uno device in particolare, restituisce gli altri
dispositivi che hanno montata la medesima cpu.

Query:
```SPARQL
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?prodLabel WHERE {      
    ?device rdf:type sipg:Device;
          sipg:CpuType ?cpu.
    SERVICE <https://query.wikidata.org/sparql> {       
        ?chip wdt:P31 wd:Q610398;
          rdfs:label ?label;
          wdt:P1535 ?prod.
        ?prod rdfs:label ?prodLabel.
        FILTER (?device = sipg:Iphone11_64 && lang(?prodLabel) = "it" && lang(?label) = "it" && regex(?label, ?cpu)).
    } 
}
```

Return:
-   "iPhone 11"@it
-   "iPhone 11 Pro"@it
-   "iPhone SE"@it

### Operazione 8

Descrizione:
data la scelta di un device in particolare, restituisce lo username
Instagram del brand del device.

Query:
```SPARQL
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?usernameIG WHERE {      
    ?device rdf:type sipg:Device;
            sipg:hasBrand ?brand.
    ?brand rdf:type sipg:Company;
           rdfs:label ?labelbrand.
    SERVICE <https://query.wikidata.org/sparql> {       
        ?company wdt:P31 wd:Q4830453;
            wdt:P2003 ?usernameIG;
            rdfs:label ?labelCompany.
        FILTER (?device = sipg:Iphone11_64 && lang(?labelCompany) = "it" && STR(?labelCompany) = STR(?labelbrand)).
    } 
}
```

Return:
- "apple"

### Operazione 9

Descrizione:
dato un utente, restituisce i prodotti che ha acquistato.

Query:
```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

SELECT ?prod WHERE{	
    ?prod rdf:type sipg:Product.
	?user rdf:type sipg:User;
		sipg:buysProduct ?prod.
	FILTER (?user = sipg:Giovanni_PowerUser)
}
```

Return:
-   productCatalog:MacBookAir_M1
-   productCatalog:iPhone12_64

---

## Altre query

### Query 1

Descrizione:
data un'azienda, restituisce le aziende che lavorano con la prima.

Query:
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

Return:
-   productCatalog:BeatsAudio
-   productCatalog:Foxconn
-   productCatalog:Qualcomm
-   productCatalog:ShortFactory

### Query 2

Descrizione:
dato un utente e uno specifico prodotto, registra l'acquisto del prodotto.

```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

INSERT { 
	?buyer sipg:buysProduct ?prod.
} WHERE {
	?buyer rdf:type sipg:User.
	?prod rdf:type sipg:Product.
	FILTER(?buyer = sipg:Giovanni_PowerUser && ?prod = sipg:Iphone11_64)
}
```

Return:
-   Added 1 statements.

### Query 3

Descrizione:
dato un utente e uno specifico prodotto, rimuove l'acquisto del prodotto.

```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>

DELETE { 
	?buyer sipg:buysProduct ?prod.
} WHERE {
	?buyer rdf:type sipg:User.
	?prod rdf:type sipg:Product.
	FILTER(?buyer = sipg:Giovanni_PowerUser && ?prod = sipg:Iphone11_64)
}
```

Return:
-   Removed 1 statements.

