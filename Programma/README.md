# Simple IT Product Catalog Program

Programma terminale "sipcp" che permette non solo di fare delle query al SIPC ma
di utilizzare l'endpoint GraphDB per interfacciarsi con SPARQL verso fonti esterne
come WikiData etc.. etc..

Il programma è completamente fatto in Python e non include una GUI.

Per utilizzarlo basta installarlo con il comando `pip install sipcp` ed utilizzarlo
direttamente nel terminale nel seguente modo:

> NB: la prima esecuzione del programma chiederà all'utente di inizializzare un file
> config.ini che conterrà l'URL di GraphDB in locale (o su server), da quel momento
> in poi sarà registrato in locale *nella cartella in cui è stato eseguito*

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
- `sipcp compatible-cables Smartphone` cerca tutti i cavi compatibili con lo smartphone specificato
- `sipcp compatible-smartphones` cerca tutte le opzioni di compatibilità tra cavi e smartphones
- `sipcp query-smartphone Prezzo` cerca tutti gli smartphones che costano di piu' della cifra specificata
  e li ordina dal meno costoso al piu' costoso
- `sipcp search-brand Company Brand` cerca tutti i Brand che vendono venduti sul sito di Company
- `sipcp search-from-cpu Device` cerca tutti i devices su Wikidata che hanno la stessa CPU del
  device in input
- `sipcp search-ig-profile Device` cerca la pagina instagram su Wikidata della compagnia che vende
  il device Device.

Per invocare un help in formato internazionale, basta digitare `sipcp --help`
Supporta Python3.6 e le versioni successive.

## Note di esecuzione

sipcp nasce per essere eseguito su un terminale UNIX-like (Linux, MacOS...) e supporta 
la maggior parte dei terminali in circolazione, eseguendo anche output colorato.
Su Windows funziona in ogni caso, ma le differenze principali sono:

- Non si possono incollare sul terminale Query multi-lines per il comando `sipcp query ""`
- L'output non è colorato (sembra banale ma rende l'interazione interessante)
