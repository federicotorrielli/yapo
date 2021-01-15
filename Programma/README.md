# Simple IT Product Catalog Program

Programma terminale "sipcp" che permette non solo di fare delle query al SIPC ma
di utilizzare l'endpoint GraphDB per interfacciarsi con SPARQL verso fonti esterne
come WikiData etc.. etc..

Il programma è completamente fatto in Python e non include una GUI.

Per utilizzarlo basta installarlo con il comando `pip install sipcp` ed utilizzarlo
direttamente nel terminale nel seguente modo:

- `sipcp query "query qui"` effettua una query in-line, non sono permessi caratteri come virgolette
  quindi l'utilizzo rimane limitato alle query veloci e tipo "listing"
- `sipcp query-from-text` effettua tutte le query prendendole da un file di testo chiamato "do.txt"
  il file deve essere nella directory in cui si sta attualmente per eseguire il programma sipcp
- `sipcp query-product Compagnia` interroga il productCatalog alla ricerca di tutti i prodotti dalla
  compagnia Compagnia. es: `sipcp query-product Apple` restituisce tutti i prodotti venduti dalla Apple
- `sipcp query-subcompanies Compagnia` similare a quello prima, interroga il productCatalog restituendo
  tutte le compagnie che lavorano per la compagnia Compagnia.
- `sipcp myproducts User` effettua la ricerca di tutti i prodotti comprati da un utente nel productCatalog,
  molto utile per il comando seguente
- `sipcp cputype Prodotto` effettua la ricerca del tipo di cpu del prodotto Prodotto

Per invocare un help in formato internazionale, basta digitare `sipcp --help`
Supporta Python3.6 e le versioni successive.

## Note di esecuzione

sipcp nasce per essere eseguito su un terminale UNIX-like (Linux, MacOS...) e supporta 
la maggior parte dei terminali in circolazione, eseguendo anche output colorato.
Su Windows funziona in ogni caso, ma le differenze principali sono:

- Non si possono incollare sul terminale Query multi-lines per il comando `sipcp query ""`
- L'output non è colorato (sembra banale ma rende l'interazione interessante)
