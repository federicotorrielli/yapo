# Documentazione di dominio

> Qua verranno mostrati documenti informali, specifiche e standard esistenti ed
> un esempio reale che mostri il funzionamento della nostra ontologia.

## Ontologie similari ed ispirazione

Per trarre ispirazione della Simple IT Product Ontology siamo partiti dalla già nota 
necessità di avere un ontologia dei prodotti, di nostra fantasia, che potesse esplicare
concetti come "catalogo", "prodotto" e "device".
Ci siamo quindi accorti che durante la costruzione della stessa si stava virando sempre
più verso il concetto di "ontologia per l'e-commerce": abbiamo quindi preso spunto da
esempi come la [Good Relations](http://www.heppnetz.de/projects/goodrelations/) ontology,
un vocabolario web appositamente creato per questo genere di utilizzi, sia da aziende
che da altre ontologie che ne fanno utilizzo.

Nonostante Good Relations fosse un buon punto di partenza, si palesava il fatto che
fosse nata principalmente a scopo di SEO Tool per siti web che possedevano CMS
(ad esempio un SEO per Wordpress!).

Figlia della già nota Good Relations, abbiamo la [Product Ontology](http://www.productontology.org/)
un'ontologia, autoesplicativa nel nome, che fa riferimento a Wikipedia per esplicare i singoli
prodotti, cui abbiamo deciso di allinare parecchie nostre definizioni per avere anche un punto
di vista interessante su una ontologia pre-esistente. La Product Ontology è davvero particolare
in quanto non ha bisogno di manualmente "integrare" la sua T-BOX ed A-BOX per l'ontologia,
ma, come già accennato, prende in prestito le sue definizioni da Wikipedia, e le ordina come la comunità ha deciso
di allineare i concetti di partenza.

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

Abbiamo notato che la classificazione dei prodotti data da Apple è confusa e chiaramente
tende a far notare a primo impatto i prodotti più nuovi invece che i più venduti, cosa 
che invece siti come MediaWorld fanno, non essendo legati ad un marchio soltanto.

### Samsung

![Samsung1](https://i.postimg.cc/SsFCmm95/image-2021-01-10-17-20-49.png)

Sul sito di Samsung si può già notare la differenziazione tra dispositivi portatili e
non, cosa che faremo anche notare all'interno della nostra ontologia e che chiaramente
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

