# Omeka-S per productCatalog

## Motivazioni della scelta dell'estensione

Tra le estensioni disponibili è stata scelta quella di Omeka-S, una piattaforma CMS
che è in tutto e per tutto una Linked Data Platform.

A differenza di GraphDB, Omeka ci ha dato molta più liberta di "giocare" con i dati
a disposizione e creare classi, resource templates e individuals utilizzando ciò
che avevamo già in input, ma con un grado di modificabilità e visibilità maggiore
rispetto a GraphDB

## Specifiche

La piattaforma è stata installata manualmente su un server pubblico dotato di 
Ubuntu 20.10, fatto un setup di MySql, phpmyadmin e tutti gli strumenti necessari
alla piattaforma per far lavorare il server senza intoppi.

Il link è pubblicamente accessibile [QUI](http://51.210.104.53/omeka/s/product-catalog/)

Dalla versione di base è stato modificato il tema pre-installato, giusto per dare
un "tocco più e-commerce" alla piattaforma.

## Items e Item sets

In Omeka gli individuals sono chiamati "items": ognuno di questi item fa riferimento
ad un template per la sua creazione chiamato il "resource template".

Sono stati creati, nel nostro caso, tre resource template rispettivamente per:

- brand: ovvero, le aziende che fanno dei prodotti
- inStock: ovvero, un prodotto che è correntemente nella condizione di essere in stock
- outOfStock: il complementare del precedente

Sono quindi stati definiti degli Item sets rispettivamente:

- inStockList: la lista degli item che sono inStock
- OutOfStockList: la lista degli item che sono outOfStock
- Brands: la lista dei brand

E poi, aggiunti degli items, come si può vedere nell'immagine:

![Item list](https://i.imgur.com/fJt2obp.png)
