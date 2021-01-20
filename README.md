# Modellazione concettuale per il web semantico (2020/21)
# Progetto: IT Catalog
### Docente: Prof.ssa Rossana Damiano
### Studenti: Ivan Spada e Federico Torrielli

---

# PARTE I

# Motivazioni
> Rilevanza del dominio scelto dal punto di vista culturale, professionale, sociale, ecc.

## Argomento scelto

Catalogo di prodotti e servizi di una generica azienda nell'ambito di vendita e noleggio di prodotti tecnologici. In 
particolare, nel seguente documento analizziamo il caso di una multinazionale e la gestione del suo catalogo. Di 
seguito, mostriamo una breve descrizione e la principale motivazione di sviluppo:

> Prendiamo in analisi i principali prodotti dell'azienda Apple, collocata nell'ambito tecnologico.

Sono trattati alcuni prodotti progettati e venduti in Italia a partire dall'anno 2016.

Alcuni esempi di prodotti venduti sono:
  - iPhone
  - iPad
  - MacBook air & pro
  - Apple Watch
  - Accessori più venduti (vd. AirPods)

## Motivazione 1: catalogare per vendere più in fretta

All'interno di una grande azienda come Apple, che principalmente ha il focus di produrre **pochi** dispositivi
con simile design ma funzioni nettamente separate è utile avere un punto di riferimento dal punto di vista
dell'organizzazione della conoscenza per svariate motivazioni:
 - Guidare il potenziale *buyer* a comprare il prodotto
 - Evitare la confusione che è naturalmente generata dalla nomenclatura dei prodotti
 - Offrire la possibilità di consultare l'archivio del prodotti

La motivazione principale della creazione di questa ontologia nasce, in verità, da qualcosa che Apple **non** mette
a disposizione dell'utente: un tool per confrontare dispositivi simili. Per essere più chiari, proponiamo un esempio:
> L'utente *x* ha la necessità di comprare un telefono iPhone ma ha a disposizione un budget limitato e ha il desiderio 
> di alcune specifiche che solo la serie iPhone X propone: si trova però davanti ad al bivio che nasce dalla 
> possibilità di comprare l'iPhone XS oppure XR. Oggi come oggi, non esiste alcun tool (che non sia una ricerca 
> manuale) per effettuare questo tipo di confronto, nonostante la loro accurata catalogazione che provvedono a dare 
> sul sito. Ovvero, sul sito Apple il confronto avviene esclusivamente in maniera testuale ma non è possibile, ad
> esempio, filtrare i contenuti per CPU.

Se il povero utente avesse avuto la possibilità di confrontare i prodotti per prezzo, si sarebbe accorto che 
l'azienda vende il modello XR ad una cifra minore con (più o meno) la stessa qualità di prodotto.

## Motivazione 2: aggiornamento del catalogo
L'azienda ha deciso di riproporre i propri dispositivi anche gli anni successivi mutando la fascia di clientela a 
cui erano precedentemente venduti. Alcuni dispositivi top di gamma dell'anno N risultano appartenenti 
alla fascia media dell'anno N+1 permettendo il riutilizzo dei *vecchi device* allungando la vita degli articoli e
riducendo le scorte avanzate in magazzino allo stesso tempo. L'organizzazione del catalogo attraverso una 
rappresentazione della conoscenza, aggiornabile nel tempo, permette la riorganizzazione delle proposte degli anni 
successivi in base alle scelte di *marketing* stabilite dal *team* addetto all'interno dell'azienda.

# Requirements
> Requisiti per la creazione dell'ontologia: finalità, task, contesto e tipo di utenti a cui si rivolge

## Finalità
> Finalità generali della codifica formale del dominio

La costruzione del dominio della seguente ontologia ha come finalità l'utilizzo della stessa al fine di 
creare cataloghi di prodotti facilmente aggiornabili, flessibili alle modifiche e su
cui si possano effettuare delle operazioni di ricerca (sia come applicazione, sia simil-DB).
Dal punto di vista aziendale, diventa sempre più complicato gestire cataloghi di prodotti, soprattutto
se risultano simili se non identici: organizzando i dati secondo un'ontologia gerarchica consultabile non
solo si può usufruire più facilmente del catalogo (da cliente) ma diventa altrettanto aggiornabile.

## Task e contesto
> I task specifici a cui è orientata e il contesto in cui si collocano

Il catalogo permette l'organizzazione dei prodotti venduti dall'azienda, tiene in considerazione le fasce di clientela
a cui gli articoli sono indirizzati e le possibili variazioni nel tempo seguendo le scelte commerciali e rispettando
le relazioni fra *items*. È possibile la consultazione della raccolta da parte dei clienti usufruendo di filtri in 
grado di semplificare la ricerca, la lettura e il confronto con i *competitor*.
Il contesto è la vendita e la consultazione dei prodotti delle aziende.

## Utenti target
> Il tipo di utenti a cui si rivolge

- Utenti che devono consultare cataloghi ed effettuare ricerche su prodotti
- Aziende che devono catalogare prodotti e verificare/aggiornare la loro presenza in stock
- Altri utenti che devono confrontare prodotti diversi in base a specifiche caratteristiche dei singoli

# Descrizione
> Descrizione del dominio, con riferimenti bibliografici e/o sitografia

## Dominio
> Descrizione del dominio

Il dominio, collocato nell'ambito commerciale, ha come fine la rappresentazione dei prodotti delle aziende mettendoli 
in relazione tra loro in base a prestazioni, qualità e *target*. Contiene le descrizioni degli articoli e le specifiche 
tecniche, permette il confronto dei prodotti e la loro organizzazione utile alle aziende e ai clienti. Infine, mantiene 
traccia delle proposte annuali disponibili sul mercato.

## Fonti
> Riferimenti bibliografici e sitografia

### Sitografia
Apple (Italy). Available at: *https://www.apple.com/it/*

Asus (Italy). Available at: *https://www.asus.com/it/*

Samsung (Italy). Available at: *https://www.samsung.com/it/*

# Documentazione sul dominio

> Qua verranno mostrati documenti informali, specifiche e standard esistenti ed
> un esempio reale che mostri il funzionamento della nostra ontologia.

## Ontologie similari ed ispirazione

Per trarre ispirazione della Simple IT Product Catalog si è partiti dalla già nota necessità di avere un ontologia 
dei prodotti, di fantasia, che potesse esplicare concetti come "catalogo", "prodotto" e "device".
Ci si è quindi accorti che durante la costruzione della stessa si stava virando sempre più verso il concetto di 
"ontologia per l'e-commerce": è stato quindi preso spunto da esempi come la 
[Good Relations](http://www.heppnetz.de/projects/goodrelations/) ontology, un vocabolario web appositamente creato 
per questo genere di utilizzi, sia da aziende che da altre ontologie che ne fanno utilizzo.

Nonostante Good Relations fosse un buon punto di partenza, si palesava il fatto che fosse nata principalmente a 
scopo di SEO Tool per siti web che possedevano CMS (ad esempio un SEO per Wordpress!).

Figlia della già nota Good Relations, la [Product Ontology](http://www.productontology.org/) un'ontologia, 
autoesplicativa nel nome, che fa riferimento a Wikipedia per esplicare i singoli prodotti, cui si è deciso 
di allinare parecchie nostre definizioni per avere anche un punto di vista interessante su una ontologia pre-esistente. 
La Product Ontology è davvero particolare in quanto non ha bisogno di manualmente "integrare" la sua T-BOX ed A-BOX 
per l'ontologia, ma, come già accennato, prende in prestito le sue definizioni da Wikipedia, e le ordina come la 
comunità ha deciso di allineare i concetti di partenza.

## Documenti informali

### Apple

La creazione dell'ontolgia si è ispirata all'organizzazione dei prodotti in catalogo
di aziende come Apple, di cui è possibile trovare sotto alcuni esempi

![Accessori1](https://i.ibb.co/K5mc9rH/image-2021-01-10-17-05-25.png)

> Macbook e iMac

![Accessori2](https://i.ibb.co/XLzLPdB/image-2021-01-10-17-06-16.png)

> iPad

![Accessori3](https://i.ibb.co/s68d5M7/image-2021-01-10-17-06-32.png)

> iPhone

![Accessori4](https://i.ibb.co/jJf4c8c/image-2021-01-10-17-06-43.png)

> Accessori e Apple Watch

Si può chiaramente vedere come la prima divisione fatta sia tramite "tipologia" di
prodotto: i computer, poi i laptop, e ancora gli iPad, iPhone ed infine gli accessori
come Apple Watch e AirPods.

Accanto ad ogni categoria è poi possibile confrontare tipi equivalenti di prodotto
(ad es. laptop con laptop) tramite il menù "Confronta". Non è invece possibile
fare confronti di prezzo sulle intere categorie (che sarebbe uno degli obiettivi
della nostra ontologia!).

È stato notato che la classificazione dei prodotti data da Apple è confusa e chiaramente
tende a far notare a primo impatto i prodotti più nuovi invece che i più venduti, cosa 
che invece siti come MediaWorld fanno, non essendo legati ad un marchio soltanto.

### Samsung

![Samsung1](https://i.postimg.cc/SsFCmm95/image-2021-01-10-17-20-49.png)

Sul sito di Samsung si può già notare la differenziazione tra dispositivi portatili e
non, cosa presente anche all'interno della nostra ontologia e che chiaramente
rende più semplice la visualizzazione di un catalogo di Prodotti elettronici.

Il fatto che Samsung abbia un'organizzazione di questo tipo fa pensare che, a differenza
di Apple, i suoi prodotti non sono pensati per essere iconici, e che, ovviamente, il loro
catalogo sia ben più vasto della già citata azienda di Cupertino.

### Asus

![Asus1](https://i.postimg.cc/xCvHCByd/image-2021-01-10-17-22-25.png)

Qua è possibile visionare la divisione di vari computer da lavoro (sia fissi, che portatili,
che ibridi). Più o meno si adatta lo stesso pattern di Samsung, in quanto il modello
di azienda è equiparabile.

## Organizzazione aziendale

La presenza di molteplici compagnie che hanno preso parte al ciclo produttivo degli
articoli ha ispirato la classificazione delle stesse per ruolo: progettazione e produzione.

Ogni azienda, nel ramo IT, o:

- Rappresenta la company che commissiona produzione e design
- Progetta solamente i prodotti
- Produce solamente i prodotti

Un esempio già citato è la Apple, che commissiona il design dei prodotti a Foxconn e 
la sua produzione di Chipset a Qualcomm (non attualmente, ma è un buon esempio).

## Organizzazione user

I prodotti IT vengono spesso realizzati avendo in mente una tipologia (o target)
di clientela, come ad esempio la divisione delle serie (J,Z,M,A...) di Samsung.

In un catalogo di prodotti IT, più di altri, è importante ricordare che si tratta di vendere
prodotti che solitamente sono costosi: un catalogo che permetta la visualizzazione per
fascia di prezzo è spesso apprezzato e aiuta la clientela a scegliere prodotti
per feature/prezzo e qualità/prezzo.

## Comparare i prodotti

![GalaxyZ](https://i.postimg.cc/k5p0Yhkf/image-2021-01-10-17-55-26.png)

Nel mondo dei device tecnologici forse il più importante fattore di scelta 
di un prodotto piuttosto che un altro sono le sue specifiche tecniche.
Nella precedente immagina possiamo notare come le diverse caratteristiche
si dividano, a seconda del dispositivo, nelle sue componenti interne.

Le stesse vengono anche utilizzate per proporre "comparison" (confronti)
tra dispositivi in modo da poter fare una scelta più accurata.

![Comparison](https://i.postimg.cc/pT5gwJvx/image-2021-01-10-18-04-35.png)

# Lode

[Qui il report LODE](http://150.146.207.114/lode/extract?url=https%3A%2F%2Fevilscript.altervista.org%2FproductCatalog.owl&lang=en)

[Qui il report LODE in formato PDF](https://github.com/federicotorrielli/modsem/raw/master/Documenti/lode.pdf)

# Visualizzazione

## Tassonomia delle classi

![Tassonomia di progetto](https://i.postimg.cc/HWKvpPfY/tassonomia.png)

## Template utilizzati per i dati (GraphDB)

![Apple template](https://i.postimg.cc/13cL31hx/firefox-T1q-YKb-W2-Aj.png)

![iPhone12 64GB template](https://i.postimg.cc/QMFkncq6/firefox-BYsgoai6o-C.png)

## Triple di esempio

Si sono voluti selezionare due esempi (rispettivamente *productCatalog:Apple* e *productCatalog:iPhone12_X*)
per mostrare alcune delle triple più utilizzate nel progetto per descrivere istanze dell'ontologia

![Apple](https://i.postimg.cc/fRPkjTyk/graph01.png)

Sono state incluse, come si può notare, anche le inferenze, che tramite GraphDB vengono 
esplicitate qui in tabella.

Per quanto riguarda la colonna del contesto, è stata riportata ma il contesto accluso
è quello di default dell'applicazione.

![Apple2](https://i.postimg.cc/nLQrdb92/graph02.png)

## Esportazione Turtle

[L'esportazione Turtle si trova QUI](https://github.com/federicotorrielli/modsem/raw/master/Protege/turtle/productCatalog.owl)
