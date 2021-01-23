# Class

## Enum
-   Manufacturer

## some
-   Factory
-   PowerUser
-   Product
-   ProductCatalog

## min
-   BigEngeneering
-   ITEngeneering

# Object properties

## Descrizione delle proprietà
-   Funzionale: 
    -   designBy
    -   hasBrand
    -   successorOf
-   Inversa-Funzionale:
    -   isBrandOf
    -   predecessorOf 
-   Simmetrico:
    -   collabsWith
-   Transitivo:
    -   brandcontainedIn
    -   contains
    -   containsBrand
    -   containsInBox
    -   inBoxOf
    -   isContainedIn

## Properties-chain
-   buysFrom: 
    
    (User -> SellingCatalog)
    -   buysProduct o isContainedIn
-   collabsWith: 
    
    (Company -> Company)
    -   hasCatalog o 'has member' o 'has item' o inCollabWith 
-   contains: 
    
    (ProductCatalog -> Product)
    -   'has member' o 'has item'
-   containsBrand: 
    
    (SellingCatalog -> Company)
    -   'has member' o 'has item' o hasBrand
-   manufacturesTo: 
    
    (Company -> Manufacturer)
    -   hasCatalog o 'has member' o 'has item' o producedBy
    -   hasCatalog o 'has member' o 'has item' o designedBy
-   putInBoxes: 
    
    (Company -> Accessory)
    -   hasCatalog o 'has member' o 'has item' o containsInBox
-   sells: 
    
    (Company -> Product)
    -   hasCatalog o 'has member' o 'has item'


#Pattern usati
-   List (e bag):
    -   Collection -> ProductCatalog (ex: AppleCatalog)
    -   Bag/list -> sotto liste del catalogo (ex: ApplePC)
-   Price

#Mapping
-   ProductOntology (per quanto riguarda i prodotti)
-   Foaf (per quanto riguarda gli user e organization)
-   Dublic Core (per i prodotti, PhisicalObj)
-   dcat (Catalog)
