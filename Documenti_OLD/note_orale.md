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

