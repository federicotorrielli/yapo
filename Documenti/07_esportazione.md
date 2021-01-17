# Esportazione in Turtle

```turtle
@prefix : <http://evilscript.altervista.org/productCatalog.owl#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://evilscript.altervista.org/productCatalog.owl> .

<http://evilscript.altervista.org/productCatalog.owl> rdf:type owl:Ontology ;
                                                       <http://purl.org/dc/elements/1.1/creator> "Federico Torrielli"^^xsd:string ,
                                                                                                 "Ivan Spada"^^xsd:string ;
                                                       <http://purl.org/dc/elements/1.1/date> 2021 ;
                                                       <http://purl.org/dc/elements/1.1/description> "The \"Simple IT Product Catalog\" is a product management/catalog ontology to demonstrate a fairly simple product catalog and how a reasoner shoud work with Company nodes and devices. It could also be applied as a model for other companies product catalogs"@en ;
                                                       <http://purl.org/vocab/vann/preferredNamespacePrefix> "sipg" ;
                                                       <http://purl.org/vocab/vann/preferredNamespaceUri> "https://evilscript.altervista.org/productCatalog.owl" ;
                                                       <http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#coversRequirements> "What are the items (elements) in this list?"^^xsd:string ,
                                                                                                                                                 "What are the items contained in this bag? "^^xsd:string ,
                                                                                                                                                 "What bag is this item an element of?"^^xsd:string ,
                                                                                                                                                 "What is before what?,What's next?,What's immediately following this?" ,
                                                                                                                                                 "What is the first/last item in this list?"^^xsd:string ,
                                                                                                                                                 "What is the length (size) of this list?"^^xsd:string ,
                                                                                                                                                 "What is the size of this bag?"^^xsd:string ,
                                                                                                                                                 "What it the next/previous item in the list?"^^xsd:string ,
                                                                                                                                                 "What resource does this item refer to?"^^xsd:string ,
                                                                                                                                                 "What resource does this list item contain?"^^xsd:string ,
                                                                                                                                                 "What things are contained in this collection (community, collective)? What collections this thing is member of?" ;
                                                       <http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#extractedFrom> "http://swan.mindinformatics.org/ontologies/1.2/collections.owl"^^xsd:string ,
                                                                                                                                            "http://www.ontologydesignpatterns.org/ont/dul/DUL.owl" ;
                                                       <http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#hasAuthor> "Aldo Gangemi" ,
                                                                                                                                        "PaoloCiccarese"^^xsd:string ,
                                                                                                                                        "Sara Bernardini" ,
                                                                                                                                        "Valentina Presutti" ;
                                                       <http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#hasComponent> "http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl"^^xsd:string ,
                                                                                                                                           "http://www.ontologydesignpatterns.org/cp/owl/sequence.owl"^^xsd:string ;
                                                       <http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#hasConsequences> "Collections and their members can be associated. Time-indexed membership cannot be represented though (you need a situation-based pattern)." ,
                                                                                                                                              "We can represent and reason over transitive or intransitive sequences of any kind. However, since coreference cannot be expressed in OWL, it is not possible to represent and reason over loops and other sequences involving coreference." ;
                                                       <http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#hasIntent> "To model bags of items (elements). The Bag is characterized by a collection that can have multiple copies of each object. "^^xsd:string ,
                                                                                                                                        "To represent domain (not set theory) membership." ,
                                                                                                                                        "To represent ordered collections, i.e. lists."^^xsd:string ,
                                                                                                                                        """To represent sequence schemas. It defines the notion of transitive and intransitive precedence and their inverses. 
It can then be used between tasks, processes, time intervals, spatially locate objects, situations, etc.""" ;
                                                       <http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#isSpecializationOf> "http://www.ontologydesignpatterns.org/cp/owl/sequence.owl"^^xsd:string ;
                                                       <http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#reengineeredFrom> "http://swan.mindinformatics.org/ontologies/1.2/collections.owl"^^xsd:string ;
                                                       <http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#relatedCPs> "TimeIndexedMembership" ,
                                                                                                                                         "http://www.ontologydesignpatterns.org/cp/owl/bag.owl"^^xsd:string ,
                                                                                                                                         "http://www.ontologydesignpatterns.org/cp/owl/list.owl"^^xsd:string ,
                                                                                                                                         "http://www.ontologydesignpatterns.org/cp/owl/set.owl"^^xsd:string ;
                                                       <http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#scenarios> "My saxophone collection includes a Mark VI tenor, a Balanced Action alto, and a Conn Transitional bari." ;
                                                       rdfs:comment """The collection entity pattern. 
It is extracted from DOLCE-UltraLite by partial clone of elements.""" ,
                                                                    "The price content ontology design pattern. This CP represents the price of an entity in a certain currency." ;
                                                       rdfs:label "ITCatalog" ,
                                                                  "collection entity" ,
                                                                  "membership" ,
                                                                  "ordering" ,
                                                                  "precedence" ,
                                                                  "sequence" ;
                                                       owl:versionInfo """1.1
- Revised and annotated for ODP submission by Aldo Gangemi
1.0
- Created by Valentina Presutti and Sara Bernardini""" ,
                                                                       "1.1 added rdfs:isDefinedBy for all named entities"^^xsd:string ,
                                                                       "Created by Aldo Gangemi and Valentina Presutti"^^xsd:string ,
                                                                       "Created by Valentina Presutti"^^xsd:string ,
                                                                       "Created with TopBraid Composer"^^xsd:string .

#################################################################
#    Annotation properties
#################################################################

###  http://purl.org/dc/elements/1.1/creator
<http://purl.org/dc/elements/1.1/creator> rdf:type owl:AnnotationProperty .


###  http://purl.org/dc/elements/1.1/date
<http://purl.org/dc/elements/1.1/date> rdf:type owl:AnnotationProperty .


###  http://purl.org/dc/elements/1.1/description
<http://purl.org/dc/elements/1.1/description> rdf:type owl:AnnotationProperty .


###  http://purl.org/vocab/vann/preferredNamespacePrefix
<http://purl.org/vocab/vann/preferredNamespacePrefix> rdf:type owl:AnnotationProperty .


###  http://purl.org/vocab/vann/preferredNamespaceUri
<http://purl.org/vocab/vann/preferredNamespaceUri> rdf:type owl:AnnotationProperty .


###  http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#coversRequirements
<http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#coversRequirements> rdf:type owl:AnnotationProperty ;
                                                                                          rdfs:comment "This annotation property is used for exemplifying possible requirements the content pattern provides a solution for. Requirements are expressed as natural language competency questions." .


###  http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#extractedFrom
<http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#extractedFrom> rdf:type owl:AnnotationProperty ;
                                                                                     rdfs:comment "This annotation property should be assigned with a URI, which points to the possible reference ontology which the annotated pattern was extracted from (i.e. the reference ontology that the ontology elements have been deeply or partially cloned by). The range is not explicit in the definition of the annotation property because it would turn the ontology to OWL Full. E.g. The participation pattern is extracted from the Dolce Ultra Lite ontology, hence the value for this annotation property is http://www.ontologydesignpatterns.org/ont/dul/DUL.owl" .


###  http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#hasAuthor
<http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#hasAuthor> rdf:type owl:AnnotationProperty .


###  http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#hasComponent
<http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#hasComponent> rdf:type owl:AnnotationProperty ;
                                                                                    rdfs:comment "This annotation property is useful for content ontology design patterns. Its value is a URI, which refers to another content ontology design pattern which is a component of the annotated one." .


###  http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#hasConsequences
<http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#hasConsequences> rdf:type owl:AnnotationProperty ;
                                                                                       rdfs:comment "This annotation property is used for briefly describing the benefits and/or possible trade-offs when using the CP." .


###  http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#hasIntent
<http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#hasIntent> rdf:type owl:AnnotationProperty ;
                                                                                 rdfs:comment "This annotation property is used in order to describe the intent of the content pattern." .


###  http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#isSpecializationOf
<http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#isSpecializationOf> rdf:type owl:AnnotationProperty ;
                                                                                          rdfs:comment "This annotation property is useful for content ontology design patterns and its elements. Its value is a URI, which refers either to a content ontology design pattern that is specialized by the annotated one, or to an ontology element that is specialized by the annotated one." .


###  http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#reengineeredFrom
<http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#reengineeredFrom> rdf:type owl:AnnotationProperty ;
                                                                                        rdfs:comment "This annotation property should be assigned with a URI, which points to the concept schema, page, or anything else from which the annotated pattern was reengineered.  If the source does not have any URI e.g., a printed book, this property value should provide information as precise as possible in order to identify the source. This property is alternative to the extractedFrom property because it is used when the pattern come from a concept schema which is not an owl ontology. For example content ontology design patterns, which are reengineered from data model patterns, rdf schemas, etc. should be annotatd with this property. E.g. The basicpersonalfoaf pattern is extracted from the rdf FOAF specification, hence the value for this annotation property is http://xmlns.com/foaf/spec/20071002.rdf" .


###  http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#relatedCPs
<http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#relatedCPs> rdf:type owl:AnnotationProperty ;
                                                                                  rdfs:comment "This annotation property can be used to indicate other CPs (if any) that specialize, generalize, inlcude, or are components of the CP. Furthermore, this field may indicate other CPs that are typically used in conjunction with the described one. Important similarities and differences with other patterns can be also described here." .


###  http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#scenarios
<http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#scenarios> rdf:type owl:AnnotationProperty ;
                                                                                 rdfs:comment "This annotation property is used for describing examples of instantiation of the Content OP. For example, for the part-of Content OP (which represents part-whole relations) a possible scenario is the sentence: \"the brain is part of the human body\". Scenarios are expressed as natural language sentences." .


#################################################################
#    Object Properties
#################################################################

###  http://www.ontologydesignpatterns.org/cp/owl/bag.owl#hasItem
<http://www.ontologydesignpatterns.org/cp/owl/bag.owl#hasItem> rdf:type owl:ObjectProperty ;
                                                               rdfs:subPropertyOf <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#hasMember> ;
                                                               owl:inverseOf <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> ;
                                                               rdfs:domain <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Bag> ;
                                                               rdfs:range <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ;
                                                               rdfs:comment "has item - The link to every item of the Bag"^^xsd:string ;
                                                               rdfs:label "has item"^^xsd:string .


###  http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemContent
<http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemContent> rdf:type owl:ObjectProperty ;
                                                                   rdfs:domain <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ;
                                                                   rdfs:range [ rdf:type owl:Class ;
                                                                                owl:complementOf <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item>
                                                                              ] ;
                                                                   rdfs:comment "itemContent - The link to the actual resource to which the item refers."^^xsd:string ;
                                                                   rdfs:label "item content"^^xsd:string .


###  http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf
<http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> rdf:type owl:ObjectProperty ;
                                                              rdfs:subPropertyOf <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> ;
                                                              rdfs:domain <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ;
                                                              rdfs:range <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Bag> ;
                                                              rdfs:comment "item of - The link from an item to the Bag where it is contained"^^xsd:string ;
                                                              rdfs:label "item of"^^xsd:string .


###  http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#hasMember
<http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#hasMember> rdf:type owl:ObjectProperty ;
                                                                              owl:inverseOf <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> ;
                                                                              rdfs:domain <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> ;
                                                                              rdfs:range owl:Thing ;
                                                                              rdfs:comment "A relation between collections and entities, e.g. 'my collection of saxophones includes an old Adolphe Sax original alto' (i.e. my collection has member an Adolphe Sax alto)." ;
                                                                              rdfs:isDefinedBy <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl> ;
                                                                              rdfs:label "has member"@en .


###  http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf
<http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> rdf:type owl:ObjectProperty ;
                                                                               rdfs:domain owl:Thing ;
                                                                               rdfs:range <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> ;
                                                                               rdfs:isDefinedBy <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl> ;
                                                                               rdfs:label "is member of"@en .


###  http://www.ontologydesignpatterns.org/cp/owl/list.owl#firstItemOf
<http://www.ontologydesignpatterns.org/cp/owl/list.owl#firstItemOf> rdf:type owl:ObjectProperty ;
                                                                    rdfs:subPropertyOf <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> ;
                                                                    owl:inverseOf <http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasFirstItem> ;
                                                                    rdfs:domain <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ;
                                                                    rdfs:range <http://www.ontologydesignpatterns.org/cp/owl/list.owl#List> ;
                                                                    rdfs:label "first item of"^^xsd:string .


###  http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasFirstItem
<http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasFirstItem> rdf:type owl:ObjectProperty ;
                                                                     rdfs:subPropertyOf <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#hasItem> ;
                                                                     rdf:type owl:FunctionalProperty ;
                                                                     rdfs:domain <http://www.ontologydesignpatterns.org/cp/owl/list.owl#List> ;
                                                                     rdfs:range <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ;
                                                                     rdfs:comment "first item - The link to the first item of the list"^^xsd:string ;
                                                                     rdfs:label "has first item"^^xsd:string .


###  http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasLastItem
<http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasLastItem> rdf:type owl:ObjectProperty ;
                                                                    rdfs:subPropertyOf <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#hasItem> ;
                                                                    owl:inverseOf <http://www.ontologydesignpatterns.org/cp/owl/list.owl#lastItemOf> ;
                                                                    rdf:type owl:FunctionalProperty ;
                                                                    rdfs:domain <http://www.ontologydesignpatterns.org/cp/owl/list.owl#List> ;
                                                                    rdfs:range <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ;
                                                                    rdfs:comment "last item - The link to the last item of the list"^^xsd:string ;
                                                                    rdfs:label "has last item"^^xsd:string .


###  http://www.ontologydesignpatterns.org/cp/owl/list.owl#lastItemOf
<http://www.ontologydesignpatterns.org/cp/owl/list.owl#lastItemOf> rdf:type owl:ObjectProperty ;
                                                                   rdfs:subPropertyOf <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> ;
                                                                   rdfs:domain <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ;
                                                                   rdfs:range <http://www.ontologydesignpatterns.org/cp/owl/list.owl#List> ;
                                                                   rdfs:label "last item of"^^xsd:string .


###  http://www.ontologydesignpatterns.org/cp/owl/list.owl#nextItem
<http://www.ontologydesignpatterns.org/cp/owl/list.owl#nextItem> rdf:type owl:ObjectProperty ;
                                                                 rdfs:subPropertyOf <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyFollows> ;
                                                                 owl:inverseOf <http://www.ontologydesignpatterns.org/cp/owl/list.owl#previousItem> ;
                                                                 rdf:type owl:FunctionalProperty ;
                                                                 rdfs:domain <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ;
                                                                 rdfs:range <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ;
                                                                 rdfs:comment "next item - The link to the next item in a list (ordered collection)"^^xsd:string ;
                                                                 rdfs:label "next item"^^xsd:string .


###  http://www.ontologydesignpatterns.org/cp/owl/list.owl#previousItem
<http://www.ontologydesignpatterns.org/cp/owl/list.owl#previousItem> rdf:type owl:ObjectProperty ;
                                                                     rdfs:subPropertyOf <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyPrecedes> ;
                                                                     rdf:type owl:FunctionalProperty ;
                                                                     rdfs:domain <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ;
                                                                     rdfs:range <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ;
                                                                     rdfs:comment "previous item - The link to the previous item in a list (ordered collection)"^^xsd:string ;
                                                                     rdfs:label "previous item"^^xsd:string .


###  http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasCurrency
<http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasCurrency> rdf:type owl:ObjectProperty ;
                                                                     rdfs:domain <http://www.ontologydesignpatterns.org/cp/owl/price.owl#Price> ;
                                                                     rdfs:range <http://www.ontologydesignpatterns.org/cp/owl/price.owl#Currency> ;
                                                                     rdfs:isDefinedBy <http://www.ontologydesignpatterns.org/cp/owl/price.owl> ;
                                                                     rdfs:label "has currency"@en .


###  http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasPrice
<http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasPrice> rdf:type owl:ObjectProperty ;
                                                                  owl:inverseOf <http://www.ontologydesignpatterns.org/cp/owl/price.owl#isPriceOf> ;
                                                                  rdfs:domain owl:Thing ;
                                                                  rdfs:range <http://www.ontologydesignpatterns.org/cp/owl/price.owl#Price> ;
                                                                  rdfs:isDefinedBy <http://www.ontologydesignpatterns.org/cp/owl/price.owl> ;
                                                                  rdfs:label "has price"@en .


###  http://www.ontologydesignpatterns.org/cp/owl/price.owl#isPriceOf
<http://www.ontologydesignpatterns.org/cp/owl/price.owl#isPriceOf> rdf:type owl:ObjectProperty ;
                                                                   rdfs:domain <http://www.ontologydesignpatterns.org/cp/owl/price.owl#Price> ;
                                                                   rdfs:range owl:Thing ;
                                                                   rdfs:isDefinedBy <http://www.ontologydesignpatterns.org/cp/owl/price.owl> ;
                                                                   rdfs:label "is price of"@en .


###  http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyFollows
<http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyFollows> rdf:type owl:ObjectProperty ;
                                                                            rdfs:subPropertyOf <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#follows> ;
                                                                            owl:inverseOf <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyPrecedes> ;
                                                                            rdfs:domain owl:Thing ;
                                                                            rdfs:range owl:Thing ;
                                                                            rdfs:comment "The intransitive follows relation. For example, Wednesday directly precedes Thursday. Directness of precedence depends on the designer conceptualization." ;
                                                                            rdfs:isDefinedBy <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl> ;
                                                                            rdfs:label "directly follows"@en ,
                                                                                       "segue direttamente"@it .


###  http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyPrecedes
<http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyPrecedes> rdf:type owl:ObjectProperty ;
                                                                             rdfs:subPropertyOf <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#precedes> ;
                                                                             rdfs:domain owl:Thing ;
                                                                             rdfs:range owl:Thing ;
                                                                             rdfs:comment "The intransitive precedes relation. For example, Monday directly precedes Tuesday. Directness of precedence depends on the designer conceptualization." ;
                                                                             rdfs:isDefinedBy <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl> ;
                                                                             rdfs:label "directly precedes"@en ,
                                                                                        "precede direttamente"@it .


###  http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#follows
<http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#follows> rdf:type owl:ObjectProperty ;
                                                                    owl:inverseOf <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#precedes> ;
                                                                    rdf:type owl:TransitiveProperty ;
                                                                    rdfs:domain owl:Thing ;
                                                                    rdfs:range owl:Thing ;
                                                                    rdfs:comment """A relation between entities, expressing a 'sequence' schema. 
E.g. 'year 2000 follows 1999', 'preparing coffee' follows 'deciding what coffee to use', 'II World War follows I World War', etc. 
It can be used between tasks, processes or time intervals, and subproperties would fit best in order to distinguish the different uses."""^^xsd:string ;
                                                                    rdfs:isDefinedBy <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl> ;
                                                                    rdfs:label "follows"@en ,
                                                                               "segue"@it .


###  http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#precedes
<http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#precedes> rdf:type owl:ObjectProperty ,
                                                                              owl:TransitiveProperty ;
                                                                     rdfs:domain owl:Thing ;
                                                                     rdfs:range owl:Thing ;
                                                                     rdfs:comment """A relation between entities, expressing a 'sequence' schema. 
E.g. 'year 1999 precedes 2000', 'deciding what coffee to use' precedes 'preparing coffee', 'World War II follows World War I', 'in the Milan to Rome autoroute, Bologna precedes Florence', etc.
It can then be used between tasks, processes, time intervals, spatially locate objects, situations, etc. 
Subproperties can be defined in order to distinguish the different uses."""^^xsd:string ;
                                                                     rdfs:isDefinedBy <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl> ;
                                                                     rdfs:label "precede"@it ,
                                                                                "precedes"@en .


###  http://www.w3.org/2002/07/owl#topObjectProperty
owl:topObjectProperty rdfs:subPropertyOf owl:topObjectProperty ;
                      rdf:type owl:SymmetricProperty ,
                               owl:TransitiveProperty ,
                               owl:ReflexiveProperty .


###  https://evilscript.altervista.org/productCatalog.owl#brandContainedIn
<https://evilscript.altervista.org/productCatalog.owl#brandContainedIn> rdf:type owl:ObjectProperty ;
                                                                        rdfs:subPropertyOf owl:topObjectProperty ;
                                                                        owl:inverseOf <https://evilscript.altervista.org/productCatalog.owl#containsBrand> ;
                                                                        rdf:type owl:TransitiveProperty ;
                                                                        rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Company> ;
                                                                        rdfs:range <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ;
                                                                        rdfs:comment "Shows if a company is listed on a Selling Catalog"@en ;
                                                                        rdfs:label "brandContainedIn"@en .


###  https://evilscript.altervista.org/productCatalog.owl#buysFrom
<https://evilscript.altervista.org/productCatalog.owl#buysFrom> rdf:type owl:ObjectProperty ;
                                                                rdfs:subPropertyOf owl:topObjectProperty ;
                                                                rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#User> ;
                                                                rdfs:range <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ;
                                                                owl:propertyChainAxiom ( <https://evilscript.altervista.org/productCatalog.owl#buysProduct>
                                                                                         <https://evilscript.altervista.org/productCatalog.owl#isContainedIn>
                                                                                       ) ;
                                                                rdfs:comment "Shows what user is buying from the X selling catalog"@en ;
                                                                rdfs:label "buysFrom"@en .


###  https://evilscript.altervista.org/productCatalog.owl#buysProduct
<https://evilscript.altervista.org/productCatalog.owl#buysProduct> rdf:type owl:ObjectProperty ;
                                                                   rdfs:subPropertyOf owl:topObjectProperty ;
                                                                   rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#User> ;
                                                                   rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                   rdfs:comment "Shows what product is the user buying"@en ;
                                                                   rdfs:label "buysProduct"@en .


###  https://evilscript.altervista.org/productCatalog.owl#collabsWith
<https://evilscript.altervista.org/productCatalog.owl#collabsWith> rdf:type owl:ObjectProperty ;
                                                                   rdfs:subPropertyOf owl:topObjectProperty ;
                                                                   owl:inverseOf <https://evilscript.altervista.org/productCatalog.owl#collabsWith> ;
                                                                   rdf:type owl:SymmetricProperty ;
                                                                   rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Company> ;
                                                                   rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Company> ;
                                                                   owl:propertyChainAxiom ( <https://evilscript.altervista.org/productCatalog.owl#sells>
                                                                                            <https://evilscript.altervista.org/productCatalog.owl#inCollabWith>
                                                                                          ) ;
                                                                   rdfs:comment "Shows company collaborations to create a certain product"@en ;
                                                                   rdfs:label "collabsWith"@en .


###  https://evilscript.altervista.org/productCatalog.owl#compatibleWith
<https://evilscript.altervista.org/productCatalog.owl#compatibleWith> rdf:type owl:ObjectProperty ;
                                                                      rdfs:subPropertyOf owl:topObjectProperty ;
                                                                      rdfs:domain [ rdf:type owl:Class ;
                                                                                    owl:unionOf ( <https://evilscript.altervista.org/productCatalog.owl#Accessory>
                                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Device>
                                                                                                )
                                                                                  ] ;
                                                                      rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Device> ;
                                                                      rdfs:comment "Checking the compatibility between accessories and devices"@en ;
                                                                      rdfs:label "compatibleWith"@en .


###  https://evilscript.altervista.org/productCatalog.owl#contains
<https://evilscript.altervista.org/productCatalog.owl#contains> rdf:type owl:ObjectProperty ;
                                                                rdfs:subPropertyOf owl:topObjectProperty ;
                                                                owl:inverseOf <https://evilscript.altervista.org/productCatalog.owl#isContainedIn> ;
                                                                rdf:type owl:AsymmetricProperty ,
                                                                         owl:TransitiveProperty ,
                                                                         owl:IrreflexiveProperty ;
                                                                rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ;
                                                                rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                owl:propertyChainAxiom ( <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#hasMember>
                                                                                         <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#hasItem>
                                                                                       ) ;
                                                                rdfs:comment "Availability of a product in a product catalog"@en ;
                                                                rdfs:label "contains"@en .


###  https://evilscript.altervista.org/productCatalog.owl#containsBrand
<https://evilscript.altervista.org/productCatalog.owl#containsBrand> rdf:type owl:ObjectProperty ;
                                                                     rdfs:subPropertyOf owl:topObjectProperty ;
                                                                     rdf:type owl:TransitiveProperty ;
                                                                     rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ;
                                                                     rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Company> ;
                                                                     owl:propertyChainAxiom ( <https://evilscript.altervista.org/productCatalog.owl#contains>
                                                                                              <https://evilscript.altervista.org/productCatalog.owl#hasBrand>
                                                                                            ) ;
                                                                     rdfs:comment "Company that sells products in SellingCatalog"@en ;
                                                                     rdfs:label "containsBrand"@en .


###  https://evilscript.altervista.org/productCatalog.owl#containsInBox
<https://evilscript.altervista.org/productCatalog.owl#containsInBox> rdf:type owl:ObjectProperty ;
                                                                     rdfs:subPropertyOf owl:topObjectProperty ;
                                                                     owl:inverseOf <https://evilscript.altervista.org/productCatalog.owl#inBoxOf> ;
                                                                     rdf:type owl:TransitiveProperty ;
                                                                     rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                     rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Accessory> ;
                                                                     rdfs:comment "Shows the items inside a product box"@en ;
                                                                     rdfs:label "containsInBox"@en .


###  https://evilscript.altervista.org/productCatalog.owl#designedBy
<https://evilscript.altervista.org/productCatalog.owl#designedBy> rdf:type owl:ObjectProperty ;
                                                                  rdfs:subPropertyOf owl:topObjectProperty ;
                                                                  owl:inverseOf <https://evilscript.altervista.org/productCatalog.owl#designs> ;
                                                                  rdf:type owl:FunctionalProperty ;
                                                                  rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                  rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Engineering> ;
                                                                  rdfs:comment "Who made the design of a product"@en ;
                                                                  rdfs:label "designedBy"@en .


###  https://evilscript.altervista.org/productCatalog.owl#designs
<https://evilscript.altervista.org/productCatalog.owl#designs> rdf:type owl:ObjectProperty ;
                                                               rdfs:subPropertyOf owl:topObjectProperty ;
                                                               rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Engineering> ;
                                                               rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                               rdfs:comment "Who made the design of a product"@en ;
                                                               rdfs:label "designs"@en .


###  https://evilscript.altervista.org/productCatalog.owl#fitFor
<https://evilscript.altervista.org/productCatalog.owl#fitFor> rdf:type owl:ObjectProperty ;
                                                              rdfs:subPropertyOf owl:topObjectProperty ;
                                                              rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Cover> ;
                                                              rdfs:range <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ;
                                                              rdfs:comment "Checking the compatibility between a cover and its device"@en ;
                                                              rdfs:label "fitFor"@en .


###  https://evilscript.altervista.org/productCatalog.owl#hasBrand
<https://evilscript.altervista.org/productCatalog.owl#hasBrand> rdf:type owl:ObjectProperty ;
                                                                rdfs:subPropertyOf owl:topObjectProperty ;
                                                                owl:inverseOf <https://evilscript.altervista.org/productCatalog.owl#isBrandOf> ;
                                                                rdf:type owl:FunctionalProperty ;
                                                                rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Company> ;
                                                                rdfs:comment "Shows the brand of the product"@en ;
                                                                rdfs:label "hasBrand"@en .


###  https://evilscript.altervista.org/productCatalog.owl#hasCatalog
<https://evilscript.altervista.org/productCatalog.owl#hasCatalog> rdf:type owl:ObjectProperty ;
                                                                  rdfs:subPropertyOf owl:topObjectProperty ;
                                                                  rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Company> ;
                                                                  rdfs:range <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ;
                                                                  rdfs:comment "Shows what catalog X Company has available"@en ;
                                                                  rdfs:label "hasCatalog"@en .


###  https://evilscript.altervista.org/productCatalog.owl#hasProducer
<https://evilscript.altervista.org/productCatalog.owl#hasProducer> rdf:type owl:ObjectProperty ;
                                                                   rdfs:subPropertyOf owl:topObjectProperty ;
                                                                   rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Engineering> ;
                                                                   rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Factory> ;
                                                                   rdfs:comment "Checking what engineering produced the design to be produced in a factory"@en ;
                                                                   rdfs:label "hasProducer"@en .


###  https://evilscript.altervista.org/productCatalog.owl#inBoxOf
<https://evilscript.altervista.org/productCatalog.owl#inBoxOf> rdf:type owl:ObjectProperty ;
                                                               rdfs:subPropertyOf owl:topObjectProperty ;
                                                               rdf:type owl:TransitiveProperty ;
                                                               rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Accessory> ;
                                                               rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                               rdfs:comment "What products has a device's box in"@en ;
                                                               rdfs:label "inBoxOf"@en .


###  https://evilscript.altervista.org/productCatalog.owl#inCollabWith
<https://evilscript.altervista.org/productCatalog.owl#inCollabWith> rdf:type owl:ObjectProperty ;
                                                                    rdfs:subPropertyOf owl:topObjectProperty ;
                                                                    rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                    rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Company> ;
                                                                    rdfs:comment "Shows company collaborations to create a certain product"@en ;
                                                                    rdfs:label "inCollabWith"@en .


###  https://evilscript.altervista.org/productCatalog.owl#isBrandOf
<https://evilscript.altervista.org/productCatalog.owl#isBrandOf> rdf:type owl:ObjectProperty ;
                                                                 rdfs:subPropertyOf owl:topObjectProperty ;
                                                                 rdf:type owl:InverseFunctionalProperty ;
                                                                 rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Company> ;
                                                                 rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                 rdfs:comment "Shows the products of the brand"@en ;
                                                                 rdfs:label "isBrandOf"@en .


###  https://evilscript.altervista.org/productCatalog.owl#isContainedIn
<https://evilscript.altervista.org/productCatalog.owl#isContainedIn> rdf:type owl:ObjectProperty ;
                                                                     rdfs:subPropertyOf owl:topObjectProperty ;
                                                                     rdf:type owl:AsymmetricProperty ,
                                                                              owl:TransitiveProperty ,
                                                                              owl:IrreflexiveProperty ;
                                                                     rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                     rdfs:range <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ;
                                                                     rdfs:comment "Availability of a product in a product catalog"@en ;
                                                                     rdfs:label "isContainedIn"@en .


###  https://evilscript.altervista.org/productCatalog.owl#isManifacturerOf
<https://evilscript.altervista.org/productCatalog.owl#isManifacturerOf> rdf:type owl:ObjectProperty ;
                                                                        rdfs:subPropertyOf owl:topObjectProperty ;
                                                                        owl:inverseOf <https://evilscript.altervista.org/productCatalog.owl#manufacturesTo> ;
                                                                        rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Manufacturer> ;
                                                                        rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Company> ;
                                                                        rdfs:comment "Keeps track of who is manifacturing this company for"@en ;
                                                                        rdfs:label "isManufacturerOf"@en .


###  https://evilscript.altervista.org/productCatalog.owl#manufacturesTo
<https://evilscript.altervista.org/productCatalog.owl#manufacturesTo> rdf:type owl:ObjectProperty ;
                                                                      rdfs:subPropertyOf owl:topObjectProperty ;
                                                                      rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Company> ;
                                                                      rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Manufacturer> ;
                                                                      owl:propertyChainAxiom ( <https://evilscript.altervista.org/productCatalog.owl#sells>
                                                                                               <https://evilscript.altervista.org/productCatalog.owl#designedBy>
                                                                                             ) ,
                                                                                             ( <https://evilscript.altervista.org/productCatalog.owl#sells>
                                                                                               <https://evilscript.altervista.org/productCatalog.owl#producedBy>
                                                                                             ) ;
                                                                      rdfs:comment "Keeps track of who is manifacturing this company for"@en ;
                                                                      rdfs:label "manufacturersTo"@en .


###  https://evilscript.altervista.org/productCatalog.owl#needsConnectionWith
<https://evilscript.altervista.org/productCatalog.owl#needsConnectionWith> rdf:type owl:ObjectProperty ;
                                                                           rdfs:subPropertyOf owl:topObjectProperty ;
                                                                           rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ;
                                                                           rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ;
                                                                           rdfs:comment "Checking the wireless compatibility between a smarwatch and a smartphone"@en ;
                                                                           rdfs:label "needsConnectionWith"@en .


###  https://evilscript.altervista.org/productCatalog.owl#predecessorOf
<https://evilscript.altervista.org/productCatalog.owl#predecessorOf> rdf:type owl:ObjectProperty ;
                                                                     rdfs:subPropertyOf owl:topObjectProperty ;
                                                                     owl:inverseOf <https://evilscript.altervista.org/productCatalog.owl#successorOf> ;
                                                                     rdf:type owl:InverseFunctionalProperty ;
                                                                     rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                     rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                     rdfs:comment "Previous device version"@en ;
                                                                     rdfs:label "predecessorOf"@en .


###  https://evilscript.altervista.org/productCatalog.owl#producedBy
<https://evilscript.altervista.org/productCatalog.owl#producedBy> rdf:type owl:ObjectProperty ;
                                                                  rdfs:subPropertyOf owl:topObjectProperty ;
                                                                  owl:inverseOf <https://evilscript.altervista.org/productCatalog.owl#produces> ;
                                                                  rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                  rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Factory> ;
                                                                  rdfs:comment "Checking what factory produced the X device"@en ;
                                                                  rdfs:label "producedBy"@en .


###  https://evilscript.altervista.org/productCatalog.owl#produces
<https://evilscript.altervista.org/productCatalog.owl#produces> rdf:type owl:ObjectProperty ;
                                                                rdfs:subPropertyOf owl:topObjectProperty ;
                                                                rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Factory> ;
                                                                rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                rdfs:comment "Checking what factory produced the X device"@en ;
                                                                rdfs:label "produces"@en .


###  https://evilscript.altervista.org/productCatalog.owl#putInBoxes
<https://evilscript.altervista.org/productCatalog.owl#putInBoxes> rdf:type owl:ObjectProperty ;
                                                                  rdfs:subPropertyOf owl:topObjectProperty ;
                                                                  rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Company> ;
                                                                  rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Accessory> ;
                                                                  owl:propertyChainAxiom ( <https://evilscript.altervista.org/productCatalog.owl#sells>
                                                                                           <https://evilscript.altervista.org/productCatalog.owl#containsInBox>
                                                                                         ) ;
                                                                  rdfs:comment "Shows what items are put in a product's box"@en ;
                                                                  rdfs:label "putInBoxes"@en .


###  https://evilscript.altervista.org/productCatalog.owl#sells
<https://evilscript.altervista.org/productCatalog.owl#sells> rdf:type owl:ObjectProperty ;
                                                             rdfs:subPropertyOf owl:topObjectProperty ;
                                                             owl:inverseOf <https://evilscript.altervista.org/productCatalog.owl#soldBy> ;
                                                             rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Company> ;
                                                             rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                             owl:propertyChainAxiom ( <https://evilscript.altervista.org/productCatalog.owl#hasCatalog>
                                                                                      <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#hasMember>
                                                                                      <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#hasItem>
                                                                                    ) ;
                                                             rdfs:comment "Product is sold by X company"@en ;
                                                             rdfs:label "sells"@en .


###  https://evilscript.altervista.org/productCatalog.owl#soldBy
<https://evilscript.altervista.org/productCatalog.owl#soldBy> rdf:type owl:ObjectProperty ;
                                                              rdfs:subPropertyOf owl:topObjectProperty ;
                                                              rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                              rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Company> ;
                                                              rdfs:comment "Product is sold by X company"@en ;
                                                              rdfs:label "soldBy"@en .


###  https://evilscript.altervista.org/productCatalog.owl#successorOf
<https://evilscript.altervista.org/productCatalog.owl#successorOf> rdf:type owl:ObjectProperty ;
                                                                   rdfs:subPropertyOf owl:topObjectProperty ;
                                                                   rdf:type owl:FunctionalProperty ;
                                                                   rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                   rdfs:range <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                   rdfs:comment "Next device version"@en ;
                                                                   rdfs:label "successorOf"@en .


#################################################################
#    Data properties
#################################################################

###  http://www.ontologydesignpatterns.org/cp/owl/bag.owl#size
<http://www.ontologydesignpatterns.org/cp/owl/bag.owl#size> rdf:type owl:DatatypeProperty ;
                                                            rdfs:domain <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> ;
                                                            rdfs:range xsd:integer ;
                                                            rdfs:comment "size - The number of items belonging to a collection"^^xsd:string ;
                                                            rdfs:label "size"^^xsd:string .


###  http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasValue
<http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasValue> rdf:type owl:DatatypeProperty ;
                                                                  rdfs:domain <http://www.ontologydesignpatterns.org/cp/owl/price.owl#Price> ;
                                                                  rdfs:range xsd:float ;
                                                                  rdfs:isDefinedBy <http://www.ontologydesignpatterns.org/cp/owl/price.owl> ;
                                                                  rdfs:label "has value"@en .


###  https://evilscript.altervista.org/productCatalog.owl#CameraMP
<https://evilscript.altervista.org/productCatalog.owl#CameraMP> rdf:type owl:DatatypeProperty ;
                                                                rdfs:subPropertyOf owl:topDataProperty ;
                                                                rdfs:domain [ rdf:type owl:Class ;
                                                                              owl:unionOf ( <https://evilscript.altervista.org/productCatalog.owl#Computer>
                                                                                            <https://evilscript.altervista.org/productCatalog.owl#PortableDevice>
                                                                                          )
                                                                            ] ;
                                                                rdfs:range [ rdf:type rdfs:Datatype ;
                                                                             owl:onDatatype xsd:double ;
                                                                             owl:withRestrictions ( [ xsd:minInclusive "0.0"^^xsd:double
                                                                                                    ]
                                                                                                  )
                                                                           ] ;
                                                                rdfs:comment "Number of megapixels in a camera's device"@en ;
                                                                rdfs:label "CameraMegaPixels"@en .


###  https://evilscript.altervista.org/productCatalog.owl#ChargingPortType
<https://evilscript.altervista.org/productCatalog.owl#ChargingPortType> rdf:type owl:DatatypeProperty ;
                                                                        rdfs:subPropertyOf owl:topDataProperty ;
                                                                        rdfs:domain [ rdf:type owl:Class ;
                                                                                      owl:unionOf ( <https://evilscript.altervista.org/productCatalog.owl#EarPlugs>
                                                                                                    <https://evilscript.altervista.org/productCatalog.owl#PortableDevice>
                                                                                                  )
                                                                                    ] ;
                                                                        rdfs:range [ rdf:type rdfs:Datatype ;
                                                                                     owl:oneOf [ rdf:type rdf:List ;
                                                                                                 rdf:first "Lightning" ;
                                                                                                 rdf:rest [ rdf:type rdf:List ;
                                                                                                            rdf:first "MicroUSB" ;
                                                                                                            rdf:rest [ rdf:type rdf:List ;
                                                                                                                       rdf:first "Proprietary" ;
                                                                                                                       rdf:rest [ rdf:type rdf:List ;
                                                                                                                                  rdf:first "USB-C" ;
                                                                                                                                  rdf:rest rdf:nil
                                                                                                                                ]
                                                                                                                     ]
                                                                                                          ]
                                                                                               ]
                                                                                   ] ;
                                                                        rdfs:comment "Charging port type"@en ;
                                                                        rdfs:label "ChargingPortType"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Color
<https://evilscript.altervista.org/productCatalog.owl#Color> rdf:type owl:DatatypeProperty ;
                                                             rdfs:subPropertyOf owl:topDataProperty ;
                                                             rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                             rdfs:range xsd:string ;
                                                             rdfs:comment "Color of the product"@en ;
                                                             rdfs:label "Color"@en .


###  https://evilscript.altervista.org/productCatalog.owl#CpuType
<https://evilscript.altervista.org/productCatalog.owl#CpuType> rdf:type owl:DatatypeProperty ;
                                                               rdfs:subPropertyOf owl:topDataProperty ;
                                                               rdfs:domain [ rdf:type owl:Class ;
                                                                             owl:unionOf ( <https://evilscript.altervista.org/productCatalog.owl#Device>
                                                                                           <https://evilscript.altervista.org/productCatalog.owl#EarPlugs>
                                                                                         )
                                                                           ] ;
                                                               rdfs:range xsd:string ;
                                                               rdfs:comment "Cpu name"@en ;
                                                               rdfs:label "CpuType"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Depth
<https://evilscript.altervista.org/productCatalog.owl#Depth> rdf:type owl:DatatypeProperty ;
                                                             rdfs:subPropertyOf owl:topDataProperty ;
                                                             rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                             rdfs:range [ rdf:type rdfs:Datatype ;
                                                                          owl:onDatatype xsd:double ;
                                                                          owl:withRestrictions ( [ xsd:minInclusive "0.0"^^xsd:double
                                                                                                 ]
                                                                                               )
                                                                        ] ;
                                                             rdfs:comment "Depth in mm of a product"@en ;
                                                             rdfs:label "Depth"@en .


###  https://evilscript.altervista.org/productCatalog.owl#EAN
<https://evilscript.altervista.org/productCatalog.owl#EAN> rdf:type owl:DatatypeProperty ;
                                                           rdfs:subPropertyOf owl:topDataProperty ;
                                                           rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                           rdfs:range xsd:string ;
                                                           rdfs:comment "Unique product code of a device"@en ;
                                                           rdfs:label "EAN"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Height
<https://evilscript.altervista.org/productCatalog.owl#Height> rdf:type owl:DatatypeProperty ;
                                                              rdfs:subPropertyOf owl:topDataProperty ;
                                                              rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                              rdfs:range [ rdf:type rdfs:Datatype ;
                                                                           owl:onDatatype xsd:double ;
                                                                           owl:withRestrictions ( [ xsd:minInclusive "0.0"^^xsd:double
                                                                                                  ]
                                                                                                )
                                                                         ] ;
                                                              rdfs:comment "Height of the product"@en ;
                                                              rdfs:label "Height"@en .


###  https://evilscript.altervista.org/productCatalog.owl#MemorySize
<https://evilscript.altervista.org/productCatalog.owl#MemorySize> rdf:type owl:DatatypeProperty ;
                                                                  rdfs:subPropertyOf owl:topDataProperty ;
                                                                  rdfs:domain [ rdf:type owl:Class ;
                                                                                owl:unionOf ( <https://evilscript.altervista.org/productCatalog.owl#Computer>
                                                                                              <https://evilscript.altervista.org/productCatalog.owl#PortableDevice>
                                                                                            )
                                                                              ] ;
                                                                  rdfs:range xsd:nonNegativeInteger ;
                                                                  rdfs:comment "Total \"Hard Disk\" size"@en ;
                                                                  rdfs:label "MemorySize"@en .


###  https://evilscript.altervista.org/productCatalog.owl#OperativeSystem
<https://evilscript.altervista.org/productCatalog.owl#OperativeSystem> rdf:type owl:DatatypeProperty ;
                                                                       rdfs:subPropertyOf owl:topDataProperty ;
                                                                       rdfs:domain [ rdf:type owl:Class ;
                                                                                     owl:unionOf ( <https://evilscript.altervista.org/productCatalog.owl#Computer>
                                                                                                   <https://evilscript.altervista.org/productCatalog.owl#PortableDevice>
                                                                                                 )
                                                                                   ] ;
                                                                       rdfs:range xsd:string ;
                                                                       rdfs:comment "Operating System installed in a product"@en ;
                                                                       rdfs:label "OperatingSystem"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Price
<https://evilscript.altervista.org/productCatalog.owl#Price> rdf:type owl:DatatypeProperty ;
                                                             rdfs:subPropertyOf owl:topDataProperty ;
                                                             rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                             rdfs:range [ rdf:type rdfs:Datatype ;
                                                                          owl:onDatatype xsd:double ;
                                                                          owl:withRestrictions ( [ xsd:minInclusive "0.0"^^xsd:double
                                                                                                 ]
                                                                                               )
                                                                        ] ;
                                                             rdfs:comment "Price in euros of a product"@en ;
                                                             rdfs:label "Price"@en .


###  https://evilscript.altervista.org/productCatalog.owl#ProductName
<https://evilscript.altervista.org/productCatalog.owl#ProductName> rdf:type owl:DatatypeProperty ;
                                                                   rdfs:subPropertyOf owl:topDataProperty ;
                                                                   rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                   rdfs:range xsd:string ;
                                                                   rdfs:comment "Shared name of the product"@en ;
                                                                   rdfs:label "ProductName"@en .


###  https://evilscript.altervista.org/productCatalog.owl#RamSize
<https://evilscript.altervista.org/productCatalog.owl#RamSize> rdf:type owl:DatatypeProperty ;
                                                               rdfs:subPropertyOf owl:topDataProperty ;
                                                               rdfs:domain [ rdf:type owl:Class ;
                                                                             owl:unionOf ( <https://evilscript.altervista.org/productCatalog.owl#Computer>
                                                                                           <https://evilscript.altervista.org/productCatalog.owl#PortableDevice>
                                                                                         )
                                                                           ] ;
                                                               rdfs:range xsd:nonNegativeInteger ;
                                                               rdfs:comment "Size in GB of the RAM"@en ;
                                                               rdfs:label "RamSize"@en .


###  https://evilscript.altervista.org/productCatalog.owl#RamType
<https://evilscript.altervista.org/productCatalog.owl#RamType> rdf:type owl:DatatypeProperty ;
                                                               rdfs:subPropertyOf owl:topDataProperty ;
                                                               rdfs:domain [ rdf:type owl:Class ;
                                                                             owl:unionOf ( <https://evilscript.altervista.org/productCatalog.owl#Computer>
                                                                                           <https://evilscript.altervista.org/productCatalog.owl#Laptop>
                                                                                           <https://evilscript.altervista.org/productCatalog.owl#2in1>
                                                                                         )
                                                                           ] ;
                                                               rdfs:range xsd:string ;
                                                               rdfs:comment "Generic labeling of Ram Type"@en ;
                                                               rdfs:label "RamType"@en .


###  https://evilscript.altervista.org/productCatalog.owl#RollOutDate
<https://evilscript.altervista.org/productCatalog.owl#RollOutDate> rdf:type owl:DatatypeProperty ;
                                                                   rdfs:subPropertyOf owl:topDataProperty ;
                                                                   rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                   rdfs:range xsd:dateTime ;
                                                                   rdfs:comment "First date of the roll out"@en ;
                                                                   rdfs:label "RollOutDate"@en .


###  https://evilscript.altervista.org/productCatalog.owl#ScreenSize
<https://evilscript.altervista.org/productCatalog.owl#ScreenSize> rdf:type owl:DatatypeProperty ;
                                                                  rdfs:subPropertyOf owl:topDataProperty ;
                                                                  rdfs:domain [ rdf:type owl:Class ;
                                                                                owl:unionOf ( <https://evilscript.altervista.org/productCatalog.owl#Computer>
                                                                                              <https://evilscript.altervista.org/productCatalog.owl#PortableDevice>
                                                                                            )
                                                                              ] ;
                                                                  rdfs:range [ rdf:type rdfs:Datatype ;
                                                                               owl:onDatatype xsd:double ;
                                                                               owl:withRestrictions ( [ xsd:minInclusive "0.0"^^xsd:double
                                                                                                      ]
                                                                                                    )
                                                                             ] ;
                                                                  rdfs:comment "Screen size in inches"@en ;
                                                                  rdfs:label "ScreenSize"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Weight
<https://evilscript.altervista.org/productCatalog.owl#Weight> rdf:type owl:DatatypeProperty ;
                                                              rdfs:subPropertyOf owl:topDataProperty ;
                                                              rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                              rdfs:range [ rdf:type rdfs:Datatype ;
                                                                           owl:onDatatype xsd:double ;
                                                                           owl:withRestrictions ( [ xsd:minInclusive "0.0"^^xsd:double
                                                                                                  ]
                                                                                                )
                                                                         ] ;
                                                              rdfs:comment "Weight in grams of a product"@en ;
                                                              rdfs:label "Weight"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Width
<https://evilscript.altervista.org/productCatalog.owl#Width> rdf:type owl:DatatypeProperty ;
                                                             rdfs:subPropertyOf owl:topDataProperty ;
                                                             rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                             rdfs:range [ rdf:type rdfs:Datatype ;
                                                                          owl:onDatatype xsd:double ;
                                                                          owl:withRestrictions ( [ xsd:minInclusive "0.0"^^xsd:double
                                                                                                 ]
                                                                                               )
                                                                        ] ;
                                                             rdfs:comment "Witdh in mm of a product"@en ;
                                                             rdfs:label "Width"@en .


###  https://evilscript.altervista.org/productCatalog.owl#isInRange
<https://evilscript.altervista.org/productCatalog.owl#isInRange> rdf:type owl:DatatypeProperty ;
                                                                 rdfs:subPropertyOf owl:topDataProperty ;
                                                                 rdfs:domain <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                 rdfs:range [ rdf:type rdfs:Datatype ;
                                                                              owl:oneOf [ rdf:type rdf:List ;
                                                                                          rdf:first "High" ;
                                                                                          rdf:rest [ rdf:type rdf:List ;
                                                                                                     rdf:first "Low" ;
                                                                                                     rdf:rest [ rdf:type rdf:List ;
                                                                                                                rdf:first "Medium" ;
                                                                                                                rdf:rest rdf:nil
                                                                                                              ]
                                                                                                   ]
                                                                                        ]
                                                                            ] ;
                                                                 rdfs:label "Customer's range the product is made to"@en ,
                                                                            "isInRange"@en .


###  https://evilscript.altervista.org/productCatalog.owl#isTouchScreen
<https://evilscript.altervista.org/productCatalog.owl#isTouchScreen> rdf:type owl:DatatypeProperty ;
                                                                     rdfs:subPropertyOf owl:topDataProperty ;
                                                                     rdf:type owl:FunctionalProperty ;
                                                                     rdfs:domain [ rdf:type owl:Class ;
                                                                                   owl:unionOf ( <https://evilscript.altervista.org/productCatalog.owl#Computer>
                                                                                                 <https://evilscript.altervista.org/productCatalog.owl#PortableDevice>
                                                                                               )
                                                                                 ] ;
                                                                     rdfs:range xsd:boolean ;
                                                                     rdfs:comment "Checking if a device is touch screen"@en ;
                                                                     rdfs:label "isTouchScreen"@en .


#################################################################
#    Classes
#################################################################

###  http://purl.org/dc/dcmitype/PhysicalObject
<http://purl.org/dc/dcmitype/PhysicalObject> rdf:type owl:Class .


###  http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Bag
<http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Bag> rdf:type owl:Class ;
                                                           rdfs:subClassOf <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                           <https://www.w3.org/ns/dcat#Catalog> ;
                                                           owl:disjointWith <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ,
                                                                            <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ,
                                                                            <http://www.productontology.org/id/Headphones> ,
                                                                            <http://www.productontology.org/id/Laptop> ,
                                                                            <http://www.productontology.org/id/Loudspeaker> ,
                                                                            <http://www.productontology.org/id/Personal_computer> ,
                                                                            <http://www.productontology.org/id/Power_cable> ,
                                                                            <http://www.productontology.org/id/Smartphone> ,
                                                                            <http://www.productontology.org/id/Smartwatch> ,
                                                                            <http://www.productontology.org/id/Tablet_computer> ,
                                                                            <http://www.productontology.org/id/2-in-1_PC> ,
                                                                            <http://www.productontology.org/id/Housing_(engineering)> ,
                                                                            <http://www.productontology.org/id/Product_(business)> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#Accessory> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#Cable> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#Computer> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#Cover> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#HardCover> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#Laptop> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#Product> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#ProductHigh> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#ProductLow> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#ProductMedium> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#2in1> ;
                                                           rdfs:comment "Bag - Collection that can have a number of copies of each object"^^xsd:string ;
                                                           rdfs:label "(collections) Bag"^^xsd:string .


###  http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item
<http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> rdf:type owl:Class ;
                                                            rdfs:subClassOf owl:Thing ,
                                                                            [ rdf:type owl:Restriction ;
                                                                              owl:onProperty <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemContent> ;
                                                                              owl:cardinality "1"^^xsd:nonNegativeInteger
                                                                            ] ;
                                                            owl:disjointWith <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> ,
                                                                             <http://www.ontologydesignpatterns.org/cp/owl/list.owl#List> ,
                                                                             <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                             <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                             <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                             <https://www.w3.org/ns/dcat#Catalog> ;
                                                            rdfs:comment "Item - Element belonging to a Bag"^^xsd:string ;
                                                            rdfs:label "item"^^xsd:string .


###  http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection
<http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> rdf:type owl:Class ;
                                                                               owl:equivalentClass <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ;
                                                                               owl:disjointWith <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ,
                                                                                                <http://www.productontology.org/id/Headphones> ,
                                                                                                <http://www.productontology.org/id/Laptop> ,
                                                                                                <http://www.productontology.org/id/Loudspeaker> ,
                                                                                                <http://www.productontology.org/id/Personal_computer> ,
                                                                                                <http://www.productontology.org/id/Power_cable> ,
                                                                                                <http://www.productontology.org/id/Smartphone> ,
                                                                                                <http://www.productontology.org/id/Smartwatch> ,
                                                                                                <http://www.productontology.org/id/Tablet_computer> ,
                                                                                                <http://www.productontology.org/id/2-in-1_PC> ,
                                                                                                <http://www.productontology.org/id/Housing_(engineering)> ,
                                                                                                <http://www.productontology.org/id/Product_(business)> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Accessory> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Cable> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Computer> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Cover> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#HardCover> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Laptop> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Product> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#ProductHigh> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#ProductLow> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#ProductMedium> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#2in1> ;
                                                                               rdfs:comment "Any container for entities that share one or more common properties. E.g. \"stone objects\", \"the nurses\", \"the Louvre Aegyptian collection\". A collection is not a logical class: a collection is a first-order entity, while a class is a second-order one." ;
                                                                               rdfs:isDefinedBy <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl> ;
                                                                               rdfs:label "Collection"@en .


###  http://www.ontologydesignpatterns.org/cp/owl/list.owl#List
<http://www.ontologydesignpatterns.org/cp/owl/list.owl#List> rdf:type owl:Class ;
                                                             rdfs:subClassOf <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Bag> ;
                                                             owl:disjointWith <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ,
                                                                              <http://www.productontology.org/id/Headphones> ,
                                                                              <http://www.productontology.org/id/Laptop> ,
                                                                              <http://www.productontology.org/id/Loudspeaker> ,
                                                                              <http://www.productontology.org/id/Personal_computer> ,
                                                                              <http://www.productontology.org/id/Power_cable> ,
                                                                              <http://www.productontology.org/id/Smartphone> ,
                                                                              <http://www.productontology.org/id/Smartwatch> ,
                                                                              <http://www.productontology.org/id/Tablet_computer> ,
                                                                              <http://www.productontology.org/id/2-in-1_PC> ,
                                                                              <http://www.productontology.org/id/Housing_(engineering)> ,
                                                                              <http://www.productontology.org/id/Product_(business)> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Accessory> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Cable> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Computer> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Cover> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#HardCover> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Laptop> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Product> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#ProductHigh> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#ProductLow> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#ProductMedium> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#2in1> ;
                                                             rdfs:comment "List - An ordered array of items, that can be present in multiple copies"^^xsd:string ;
                                                             rdfs:label "list"^^xsd:string .


###  http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem
<http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> rdf:type owl:Class ;
                                                                 rdfs:subClassOf <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ;
                                                                 owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                                  <https://www.w3.org/ns/dcat#Catalog> ;
                                                                 rdfs:comment "ListItem - Element belonging to a list"^^xsd:string ;
                                                                 rdfs:label "list item"^^xsd:string .


###  http://www.ontologydesignpatterns.org/cp/owl/price.owl#Currency
<http://www.ontologydesignpatterns.org/cp/owl/price.owl#Currency> rdf:type owl:Class ;
                                                                  owl:disjointWith <http://www.ontologydesignpatterns.org/cp/owl/price.owl#Price> ;
                                                                  rdfs:comment "A system of money in general use in a particular country." ;
                                                                  rdfs:isDefinedBy <http://www.ontologydesignpatterns.org/cp/owl/price.owl> ;
                                                                  rdfs:label "Currency"@en .


###  http://www.ontologydesignpatterns.org/cp/owl/price.owl#Price
<http://www.ontologydesignpatterns.org/cp/owl/price.owl#Price> rdf:type owl:Class ;
                                                               rdfs:subClassOf [ rdf:type owl:Restriction ;
                                                                                 owl:onProperty <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasCurrency> ;
                                                                                 owl:cardinality "1"^^xsd:nonNegativeInteger
                                                                               ] ,
                                                                               [ rdf:type owl:Restriction ;
                                                                                 owl:onProperty <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasValue> ;
                                                                                 owl:minCardinality "1"^^xsd:nonNegativeInteger
                                                                               ] ;
                                                               rdfs:comment "The amount of money expected, required, or given in payment for something." ;
                                                               rdfs:isDefinedBy <http://www.ontologydesignpatterns.org/cp/owl/price.owl> ;
                                                               rdfs:label "Price"@en .


###  http://www.productontology.org/id/Headphones
<http://www.productontology.org/id/Headphones> rdf:type owl:Class ;
                                               owl:equivalentClass <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ;
                                               rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#Accessory> ;
                                               owl:disjointWith <http://www.productontology.org/id/Laptop> ,
                                                                <http://www.productontology.org/id/Loudspeaker> ,
                                                                <http://www.productontology.org/id/Personal_computer> ,
                                                                <http://www.productontology.org/id/Power_cable> ,
                                                                <http://www.productontology.org/id/Smartphone> ,
                                                                <http://www.productontology.org/id/Smartwatch> ,
                                                                <http://www.productontology.org/id/Tablet_computer> ,
                                                                <http://www.productontology.org/id/2-in-1_PC> ,
                                                                <http://www.productontology.org/id/Housing_(engineering)> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Cable> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Computer> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Cover> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#HardCover> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Laptop> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                <https://www.w3.org/ns/dcat#Catalog> .


###  http://www.productontology.org/id/Laptop
<http://www.productontology.org/id/Laptop> rdf:type owl:Class ;
                                           owl:equivalentClass <https://evilscript.altervista.org/productCatalog.owl#Laptop> ;
                                           rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ;
                                           owl:disjointWith <http://www.productontology.org/id/Loudspeaker> ,
                                                            <http://www.productontology.org/id/Personal_computer> ,
                                                            <http://www.productontology.org/id/Power_cable> ,
                                                            <http://www.productontology.org/id/Smartphone> ,
                                                            <http://www.productontology.org/id/Smartwatch> ,
                                                            <http://www.productontology.org/id/Housing_(engineering)> ,
                                                            <https://evilscript.altervista.org/productCatalog.owl#Accessory> ,
                                                            <https://evilscript.altervista.org/productCatalog.owl#Cable> ,
                                                            <https://evilscript.altervista.org/productCatalog.owl#Computer> ,
                                                            <https://evilscript.altervista.org/productCatalog.owl#Cover> ,
                                                            <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                            <https://evilscript.altervista.org/productCatalog.owl#HardCover> ,
                                                            <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                            <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                            <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                            <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                            <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                            <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                            <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                            <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                            <https://www.w3.org/ns/dcat#Catalog> .


###  http://www.productontology.org/id/Loudspeaker
<http://www.productontology.org/id/Loudspeaker> rdf:type owl:Class ;
                                                owl:equivalentClass <https://evilscript.altervista.org/productCatalog.owl#Stereo> ;
                                                rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ;
                                                owl:disjointWith <http://www.productontology.org/id/Personal_computer> ,
                                                                 <http://www.productontology.org/id/Power_cable> ,
                                                                 <http://www.productontology.org/id/Smartphone> ,
                                                                 <http://www.productontology.org/id/Smartwatch> ,
                                                                 <http://www.productontology.org/id/Tablet_computer> ,
                                                                 <http://www.productontology.org/id/2-in-1_PC> ,
                                                                 <http://www.productontology.org/id/Housing_(engineering)> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#Accessory> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#Cable> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#Computer> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#Cover> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#HardCover> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#Laptop> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                 <https://www.w3.org/ns/dcat#Catalog> .


###  http://www.productontology.org/id/Personal_computer
<http://www.productontology.org/id/Personal_computer> rdf:type owl:Class ;
                                                      owl:equivalentClass <https://evilscript.altervista.org/productCatalog.owl#Computer> ;
                                                      rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ;
                                                      owl:disjointWith <http://www.productontology.org/id/Power_cable> ,
                                                                       <http://www.productontology.org/id/Smartphone> ,
                                                                       <http://www.productontology.org/id/Smartwatch> ,
                                                                       <http://www.productontology.org/id/Tablet_computer> ,
                                                                       <http://www.productontology.org/id/2-in-1_PC> ,
                                                                       <http://www.productontology.org/id/Housing_(engineering)> ,
                                                                       <https://evilscript.altervista.org/productCatalog.owl#Accessory> ,
                                                                       <https://evilscript.altervista.org/productCatalog.owl#Cable> ,
                                                                       <https://evilscript.altervista.org/productCatalog.owl#Cover> ,
                                                                       <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                                       <https://evilscript.altervista.org/productCatalog.owl#HardCover> ,
                                                                       <https://evilscript.altervista.org/productCatalog.owl#Laptop> ,
                                                                       <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                       <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                       <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                       <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                       <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                       <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                       <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                       <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                       <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                       <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                       <https://www.w3.org/ns/dcat#Catalog> .


###  http://www.productontology.org/id/Power_cable
<http://www.productontology.org/id/Power_cable> rdf:type owl:Class ;
                                                owl:equivalentClass <https://evilscript.altervista.org/productCatalog.owl#Cable> ;
                                                rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#Accessory> ;
                                                owl:disjointWith <http://www.productontology.org/id/Smartphone> ,
                                                                 <http://www.productontology.org/id/Smartwatch> ,
                                                                 <http://www.productontology.org/id/Tablet_computer> ,
                                                                 <http://www.productontology.org/id/2-in-1_PC> ,
                                                                 <http://www.productontology.org/id/Housing_(engineering)> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#Computer> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#Cover> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#HardCover> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#Laptop> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                 <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                 <https://www.w3.org/ns/dcat#Catalog> .


###  http://www.productontology.org/id/Smartphone
<http://www.productontology.org/id/Smartphone> rdf:type owl:Class ;
                                               owl:equivalentClass <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ;
                                               rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ;
                                               owl:disjointWith <http://www.productontology.org/id/Smartwatch> ,
                                                                <http://www.productontology.org/id/Tablet_computer> ,
                                                                <http://www.productontology.org/id/2-in-1_PC> ,
                                                                <http://www.productontology.org/id/Housing_(engineering)> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Accessory> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Cable> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Computer> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Cover> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#HardCover> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Laptop> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                <https://www.w3.org/ns/dcat#Catalog> .


###  http://www.productontology.org/id/Smartwatch
<http://www.productontology.org/id/Smartwatch> rdf:type owl:Class ;
                                               owl:equivalentClass <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ;
                                               rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ;
                                               owl:disjointWith <http://www.productontology.org/id/Tablet_computer> ,
                                                                <http://www.productontology.org/id/2-in-1_PC> ,
                                                                <http://www.productontology.org/id/Housing_(engineering)> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Accessory> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Cable> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Computer> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Cover> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#HardCover> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Laptop> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                <https://www.w3.org/ns/dcat#Catalog> .


###  http://www.productontology.org/id/Tablet_computer
<http://www.productontology.org/id/Tablet_computer> rdf:type owl:Class ;
                                                    owl:equivalentClass <https://evilscript.altervista.org/productCatalog.owl#Tablet> ;
                                                    rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ;
                                                    owl:disjointWith <http://www.productontology.org/id/Housing_(engineering)> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#Accessory> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#Cable> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#Computer> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#Cover> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#HardCover> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                     <https://www.w3.org/ns/dcat#Catalog> .


###  http://www.productontology.org/id/2-in-1_PC
<http://www.productontology.org/id/2-in-1_PC> rdf:type owl:Class ;
                                              owl:equivalentClass <https://evilscript.altervista.org/productCatalog.owl#2in1> ;
                                              rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ;
                                              owl:disjointWith <http://www.productontology.org/id/Housing_(engineering)> ,
                                                               <https://evilscript.altervista.org/productCatalog.owl#Accessory> ,
                                                               <https://evilscript.altervista.org/productCatalog.owl#Cable> ,
                                                               <https://evilscript.altervista.org/productCatalog.owl#Computer> ,
                                                               <https://evilscript.altervista.org/productCatalog.owl#Cover> ,
                                                               <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                               <https://evilscript.altervista.org/productCatalog.owl#HardCover> ,
                                                               <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                               <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                               <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                               <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                               <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                               <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                               <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                               <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                               <https://www.w3.org/ns/dcat#Catalog> .


###  http://www.productontology.org/id/Housing_(engineering)
<http://www.productontology.org/id/Housing_(engineering)> rdf:type owl:Class ;
                                                          owl:equivalentClass <https://evilscript.altervista.org/productCatalog.owl#Cover> ;
                                                          rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#Accessory> ;
                                                          owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#Cable> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Computer> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Laptop> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                           <https://www.w3.org/ns/dcat#Catalog> .


###  http://www.productontology.org/id/Product_(business)
<http://www.productontology.org/id/Product_(business)> rdf:type owl:Class ;
                                                       owl:equivalentClass <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                       rdfs:subClassOf <http://purl.org/dc/dcmitype/PhysicalObject> ,
                                                                       <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ;
                                                       owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                        <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                        <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                        <https://www.w3.org/ns/dcat#Catalog> .


###  http://xmlns.com/foaf/0.1/Organization
<http://xmlns.com/foaf/0.1/Organization> rdf:type owl:Class .


###  http://xmlns.com/foaf/0.1/Person
<http://xmlns.com/foaf/0.1/Person> rdf:type owl:Class .


###  https://evilscript.altervista.org/productCatalog.owl#Accessory
<https://evilscript.altervista.org/productCatalog.owl#Accessory> rdf:type owl:Class ;
                                                                 rdfs:subClassOf <http://www.productontology.org/id/Product_(business)> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                 owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#Computer> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Laptop> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                                  <https://www.w3.org/ns/dcat#Catalog> ;
                                                                 rdfs:comment "A product used with or within the device use"@en ;
                                                                 rdfs:label "Accessory"@en .


###  https://evilscript.altervista.org/productCatalog.owl#BigEngineering
<https://evilscript.altervista.org/productCatalog.owl#BigEngineering> rdf:type owl:Class ;
                                                                      owl:equivalentClass [ rdf:type owl:Restriction ;
                                                                                            owl:onProperty <https://evilscript.altervista.org/productCatalog.owl#designs> ;
                                                                                            owl:minQualifiedCardinality "3"^^xsd:nonNegativeInteger ;
                                                                                            owl:onClass <https://evilscript.altervista.org/productCatalog.owl#Product>
                                                                                          ] ;
                                                                      rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#Engineering> ;
                                                                      owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#Factory> ;
                                                                      rdfs:comment "A part of the engineering process that is eventually bigger than the normal one"@en ;
                                                                      rdfs:label "BigEngineering"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Cable
<https://evilscript.altervista.org/productCatalog.owl#Cable> rdf:type owl:Class ;
                                                             rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#Accessory> ;
                                                             owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#Computer> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Cover> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#HardCover> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Laptop> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                              <https://www.w3.org/ns/dcat#Catalog> .


###  https://evilscript.altervista.org/productCatalog.owl#CasualUser
<https://evilscript.altervista.org/productCatalog.owl#CasualUser> rdf:type owl:Class ;
                                                                  rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#User> ;
                                                                  owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#PowerUser> ;
                                                                  rdfs:comment "An individual using a product which is not used to technology"@en ;
                                                                  rdfs:label "CasualUser"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Company
<https://evilscript.altervista.org/productCatalog.owl#Company> rdf:type owl:Class ;
                                                               rdfs:subClassOf <http://xmlns.com/foaf/0.1/Organization> ;
                                                               rdfs:comment "The company that has the project, the engineering process and the manifacturing to produce the product"@en ;
                                                               rdfs:label "Company"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Computer
<https://evilscript.altervista.org/productCatalog.owl#Computer> rdf:type owl:Class ;
                                                                rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ;
                                                                owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#Cover> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#HardCover> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#Laptop> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                                 <https://www.w3.org/ns/dcat#Catalog> ;
                                                                rdfs:comment "Just a computer"@en ;
                                                                rdfs:label "Computer"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Cover
<https://evilscript.altervista.org/productCatalog.owl#Cover> rdf:type owl:Class ;
                                                             rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#Accessory> ;
                                                             owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Laptop> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                              <https://www.w3.org/ns/dcat#Catalog> ;
                                                             rdfs:comment "A product made for protecting a device from accidental falls"@en ;
                                                             rdfs:label "Cover"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Device
<https://evilscript.altervista.org/productCatalog.owl#Device> rdf:type owl:Class ;
                                                              rdfs:subClassOf <http://www.productontology.org/id/Product_(business)> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                              owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                                               <https://evilscript.altervista.org/productCatalog.owl#HardCover> ,
                                                                               <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                               <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                               <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                               <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                               <https://www.w3.org/ns/dcat#Catalog> ;
                                                              rdfs:comment "An electronic product"@en ;
                                                              rdfs:label "Device"@en .


###  https://evilscript.altervista.org/productCatalog.owl#EarPlugs
<https://evilscript.altervista.org/productCatalog.owl#EarPlugs> rdf:type owl:Class ;
                                                                rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#Accessory> ;
                                                                owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#HardCover> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#Laptop> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                                 <https://www.w3.org/ns/dcat#Catalog> ;
                                                                rdfs:comment "A small accessory device made for listening to music"@en ;
                                                                rdfs:label "EarPlugs"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Engineering
<https://evilscript.altervista.org/productCatalog.owl#Engineering> rdf:type owl:Class ;
                                                                   owl:equivalentClass [ rdf:type owl:Restriction ;
                                                                                         owl:onProperty <https://evilscript.altervista.org/productCatalog.owl#designs> ;
                                                                                         owl:someValuesFrom <https://evilscript.altervista.org/productCatalog.owl#Product>
                                                                                       ] ;
                                                                   rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#Manufacturer> ;
                                                                   owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#Factory> ;
                                                                   rdfs:comment "The part of the Manufacturer process that creates the design of the product"@en ;
                                                                   rdfs:label "Engineering"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Factory
<https://evilscript.altervista.org/productCatalog.owl#Factory> rdf:type owl:Class ;
                                                               owl:equivalentClass [ rdf:type owl:Restriction ;
                                                                                     owl:onProperty <https://evilscript.altervista.org/productCatalog.owl#produces> ;
                                                                                     owl:someValuesFrom <https://evilscript.altervista.org/productCatalog.owl#Product>
                                                                                   ] ;
                                                               rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#Manufacturer> ;
                                                               owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#ITEngineering> ;
                                                               rdfs:comment "The part of the Manufactorer process that phisically produces the product"@en ;
                                                               rdfs:label "Factory"@en .


###  https://evilscript.altervista.org/productCatalog.owl#HardCover
<https://evilscript.altervista.org/productCatalog.owl#HardCover> rdf:type owl:Class ;
                                                                 rdfs:subClassOf <http://www.productontology.org/id/Housing_(engineering)> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#Cover> ;
                                                                 owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#Laptop> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                                  <https://www.w3.org/ns/dcat#Catalog> ;
                                                                 rdfs:comment "An hard cover"@en ;
                                                                 rdfs:label "HardCover"@en .


###  https://evilscript.altervista.org/productCatalog.owl#ITEngineering
<https://evilscript.altervista.org/productCatalog.owl#ITEngineering> rdf:type owl:Class ;
                                                                     owl:equivalentClass [ rdf:type owl:Restriction ;
                                                                                           owl:onProperty <https://evilscript.altervista.org/productCatalog.owl#designs> ;
                                                                                           owl:minQualifiedCardinality "1"^^xsd:nonNegativeInteger ;
                                                                                           owl:onClass <https://evilscript.altervista.org/productCatalog.owl#Device>
                                                                                         ] ;
                                                                     rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#Engineering> ;
                                                                     rdfs:comment "An Engineering part of the Manufacturer process that specifically contributes to making machines and IT devices"@en ;
                                                                     rdfs:label "ITEngineering"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Laptop
<https://evilscript.altervista.org/productCatalog.owl#Laptop> rdf:type owl:Class ;
                                                              rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ;
                                                              owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                                               <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                               <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                               <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                               <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                               <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                               <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                               <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                               <https://www.w3.org/ns/dcat#Catalog> ;
                                                              rdfs:comment "A small portable personal computer"@en ;
                                                              rdfs:label "Laptop"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Manufacturer
<https://evilscript.altervista.org/productCatalog.owl#Manufacturer> rdf:type owl:Class ;
                                                                    owl:equivalentClass [ rdf:type owl:Class ;
                                                                                          owl:oneOf ( <https://evilscript.altervista.org/productCatalog.owl#Apple>
                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#Asus>
                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#BeatsAudio>
                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#Foxconn>
                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#Huáshuò>
                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#Qualcomm>
                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#Samsung>
                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#ShortEngineer>
                                                                                                    )
                                                                                        ] ;
                                                                    rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#Company> ;
                                                                    rdfs:comment "The part of the company specifically addressed to engineer and produce the X product"@en ;
                                                                    rdfs:label "Manufacturer"@en .


###  https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice
<https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> rdf:type owl:Class ;
                                                                         rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#Device> ;
                                                                         owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                                          <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                                          <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                                          <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                                          <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                                          <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                                          <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                                          <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                                          <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                                          <https://www.w3.org/ns/dcat#Catalog> ;
                                                                         rdfs:comment "A device that is not made to be moved from the initial position"@en ;
                                                                         rdfs:label "NotPortableDevice"@en .


###  https://evilscript.altervista.org/productCatalog.owl#PortableDevice
<https://evilscript.altervista.org/productCatalog.owl#PortableDevice> rdf:type owl:Class ;
                                                                      rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#Device> ;
                                                                      owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                                       <https://www.w3.org/ns/dcat#Catalog> ;
                                                                      rdfs:comment "A device made for everyday life"@en ;
                                                                      rdfs:label "PortableDevice"@en .


###  https://evilscript.altervista.org/productCatalog.owl#PowerUser
<https://evilscript.altervista.org/productCatalog.owl#PowerUser> rdf:type owl:Class ;
                                                                 owl:equivalentClass [ rdf:type owl:Restriction ;
                                                                                       owl:onProperty <https://evilscript.altervista.org/productCatalog.owl#buysProduct> ;
                                                                                       owl:someValuesFrom <https://evilscript.altervista.org/productCatalog.owl#ProductHigh>
                                                                                     ] ;
                                                                 rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#User> ;
                                                                 rdfs:comment "An expert individual using a product"@en ;
                                                                 rdfs:label "PowerUser"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Product
<https://evilscript.altervista.org/productCatalog.owl#Product> rdf:type owl:Class ;
                                                               owl:equivalentClass [ owl:intersectionOf ( <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem>
                                                                                                          [ rdf:type owl:Restriction ;
                                                                                                            owl:onProperty <https://evilscript.altervista.org/productCatalog.owl#isContainedIn> ;
                                                                                                            owl:someValuesFrom <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog>
                                                                                                          ]
                                                                                                        ) ;
                                                                                     rdf:type owl:Class
                                                                                   ] ;
                                                               rdfs:subClassOf <http://purl.org/dc/dcmitype/PhysicalObject> ,
                                                                               <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ;
                                                               owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                                <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                                <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                                <https://www.w3.org/ns/dcat#Catalog> ;
                                                               rdfs:comment "Something that is produced and used"@en ;
                                                               rdfs:label "Product"@en .


###  https://evilscript.altervista.org/productCatalog.owl#ProductCatalog
<https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> rdf:type owl:Class ;
                                                                      owl:equivalentClass <https://www.w3.org/ns/dcat#Catalog> ,
                                                                                          [ rdf:type owl:Restriction ;
                                                                                            owl:onProperty <https://evilscript.altervista.org/productCatalog.owl#contains> ;
                                                                                            owl:someValuesFrom <https://evilscript.altervista.org/productCatalog.owl#Product>
                                                                                          ] ;
                                                                      rdfs:subClassOf owl:Thing ;
                                                                      owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#ProductHigh> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#ProductLow> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#ProductMedium> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#2in1> ;
                                                                      rdfs:comment "A catalog of products"@en ;
                                                                      rdfs:label "ProductCatalog"@en .


###  https://evilscript.altervista.org/productCatalog.owl#ProductHigh
<https://evilscript.altervista.org/productCatalog.owl#ProductHigh> rdf:type owl:Class ;
                                                                   owl:equivalentClass [ owl:intersectionOf ( <https://evilscript.altervista.org/productCatalog.owl#Product>
                                                                                                              [ rdf:type owl:Restriction ;
                                                                                                                owl:onProperty <https://evilscript.altervista.org/productCatalog.owl#isInRange> ;
                                                                                                                owl:hasValue "High"^^xsd:string
                                                                                                              ]
                                                                                                            ) ;
                                                                                         rdf:type owl:Class
                                                                                       ] ;
                                                                   rdfs:subClassOf <http://www.productontology.org/id/Product_(business)> ,
                                                                                   <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                   owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                                    <https://www.w3.org/ns/dcat#Catalog> .


###  https://evilscript.altervista.org/productCatalog.owl#ProductLow
<https://evilscript.altervista.org/productCatalog.owl#ProductLow> rdf:type owl:Class ;
                                                                  owl:equivalentClass [ owl:intersectionOf ( <https://evilscript.altervista.org/productCatalog.owl#Product>
                                                                                                             [ rdf:type owl:Restriction ;
                                                                                                               owl:onProperty <https://evilscript.altervista.org/productCatalog.owl#isInRange> ;
                                                                                                               owl:hasValue "Low"^^xsd:string
                                                                                                             ]
                                                                                                           ) ;
                                                                                        rdf:type owl:Class
                                                                                      ] ;
                                                                  rdfs:subClassOf <http://www.productontology.org/id/Product_(business)> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                  owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                                   <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                                   <https://www.w3.org/ns/dcat#Catalog> .


###  https://evilscript.altervista.org/productCatalog.owl#ProductMedium
<https://evilscript.altervista.org/productCatalog.owl#ProductMedium> rdf:type owl:Class ;
                                                                     owl:equivalentClass [ owl:intersectionOf ( <https://evilscript.altervista.org/productCatalog.owl#Product>
                                                                                                                [ rdf:type owl:Restriction ;
                                                                                                                  owl:onProperty <https://evilscript.altervista.org/productCatalog.owl#isInRange> ;
                                                                                                                  owl:hasValue "Medium"^^xsd:string
                                                                                                                ]
                                                                                                              ) ;
                                                                                           rdf:type owl:Class
                                                                                         ] ;
                                                                     rdfs:subClassOf <http://www.productontology.org/id/Product_(business)> ,
                                                                                     <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                     owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                                      <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                                      <https://www.w3.org/ns/dcat#Catalog> .


###  https://evilscript.altervista.org/productCatalog.owl#SellingCatalog
<https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> rdf:type owl:Class ;
                                                                      rdfs:subClassOf <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> ,
                                                                                      <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                                      <https://www.w3.org/ns/dcat#Catalog> ;
                                                                      owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#2in1> ;
                                                                      rdfs:comment "A catalog of products made to be sold"@en ;
                                                                      rdfs:label "SellingCatalog"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Smartphone
<https://evilscript.altervista.org/productCatalog.owl#Smartphone> rdf:type owl:Class ;
                                                                  rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ;
                                                                  owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ,
                                                                                   <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                                   <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                                   <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                                   <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                                   <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                                   <https://www.w3.org/ns/dcat#Catalog> ;
                                                                  rdfs:comment "Mobile device that combines cellular and mobile computing functions into one unit"@en ;
                                                                  rdfs:label "Smartphone"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Smartwatch
<https://evilscript.altervista.org/productCatalog.owl#Smartwatch> rdf:type owl:Class ;
                                                                  rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ;
                                                                  owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#SoftCover> ,
                                                                                   <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                                   <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                                   <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                                   <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                                   <https://www.w3.org/ns/dcat#Catalog> ;
                                                                  rdfs:comment "Wearable computer in the form of a watch"@en ;
                                                                  rdfs:label "Smartwatch"@en .


###  https://evilscript.altervista.org/productCatalog.owl#SoftCover
<https://evilscript.altervista.org/productCatalog.owl#SoftCover> rdf:type owl:Class ;
                                                                 rdfs:subClassOf <http://www.productontology.org/id/Housing_(engineering)> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#Cover> ;
                                                                 owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#Stereo> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                                  <https://www.w3.org/ns/dcat#Catalog> ;
                                                                 rdfs:comment "A soft cover"@en ;
                                                                 rdfs:label "SoftCover"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Stereo
<https://evilscript.altervista.org/productCatalog.owl#Stereo> rdf:type owl:Class ;
                                                              rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ;
                                                              owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#StockCatalog> ,
                                                                               <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                               <https://evilscript.altervista.org/productCatalog.owl#2in1> ,
                                                                               <https://www.w3.org/ns/dcat#Catalog> ;
                                                              rdfs:comment "A big device made for listening to music"@en ;
                                                              rdfs:label "Stereo"@en .


###  https://evilscript.altervista.org/productCatalog.owl#StockCatalog
<https://evilscript.altervista.org/productCatalog.owl#StockCatalog> rdf:type owl:Class ;
                                                                    rdfs:subClassOf <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> ,
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                                    <https://www.w3.org/ns/dcat#Catalog> ;
                                                                    owl:disjointWith <https://evilscript.altervista.org/productCatalog.owl#Tablet> ,
                                                                                     <https://evilscript.altervista.org/productCatalog.owl#2in1> ;
                                                                    rdfs:comment "A catalog of products made to keep track of stock coverage"@en ;
                                                                    rdfs:label "StockCatalog"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Tablet
<https://evilscript.altervista.org/productCatalog.owl#Tablet> rdf:type owl:Class ;
                                                              rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ;
                                                              owl:disjointWith <https://www.w3.org/ns/dcat#Catalog> ;
                                                              rdfs:comment "Mobile device, typically with a mobile operating system and touchscreen display processing circuitry, and a rechargeable battery in a single, thin and flat package"@en ;
                                                              rdfs:label "Tablet"@en .


###  https://evilscript.altervista.org/productCatalog.owl#User
<https://evilscript.altervista.org/productCatalog.owl#User> rdf:type owl:Class ;
                                                            rdfs:subClassOf <http://xmlns.com/foaf/0.1/Person> ;
                                                            rdfs:comment "An individual using a product"@en ;
                                                            rdfs:label "User"@en .


###  https://evilscript.altervista.org/productCatalog.owl#2in1
<https://evilscript.altervista.org/productCatalog.owl#2in1> rdf:type owl:Class ;
                                                            rdfs:subClassOf <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ;
                                                            owl:disjointWith <https://www.w3.org/ns/dcat#Catalog> ;
                                                            rdfs:comment "A portable computer that has features of both tablets and laptops"@en ;
                                                            rdfs:label "2in1"@en .


###  https://www.w3.org/ns/dcat#Catalog
<https://www.w3.org/ns/dcat#Catalog> rdf:type owl:Class .


#################################################################
#    Individuals
#################################################################

###  https://evilscript.altervista.org/productCatalog.owl#AirPods_wirelessCharge
<https://evilscript.altervista.org/productCatalog.owl#AirPods_wirelessCharge> rdf:type owl:NamedIndividual ,
                                                                                       <http://purl.org/dc/dcmitype/PhysicalObject> ,
                                                                                       <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ,
                                                                                       <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ,
                                                                                       <http://www.productontology.org/id/Headphones> ,
                                                                                       <http://www.productontology.org/id/Product_(business)> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#Accessory> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                                                       <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                              <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> <https://evilscript.altervista.org/productCatalog.owl#AppleAccessories> ;
                                                                              <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#AppleAccessories> ;
                                                                              <http://www.ontologydesignpatterns.org/cp/owl/list.owl#nextItem> <https://evilscript.altervista.org/productCatalog.owl#AppleWatchSeries6_40mm_GPS_Cellular_Nike> ;
                                                                              <http://www.ontologydesignpatterns.org/cp/owl/list.owl#previousItem> <https://evilscript.altervista.org/productCatalog.owl#Lightning_cable> ;
                                                                              <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasPrice> <https://evilscript.altervista.org/productCatalog.owl#200Euro> ;
                                                                              <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyFollows> <https://evilscript.altervista.org/productCatalog.owl#AppleWatchSeries6_40mm_GPS_Cellular_Nike> ;
                                                                              <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyPrecedes> <https://evilscript.altervista.org/productCatalog.owl#Lightning_cable> ;
                                                                              <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#follows> <https://evilscript.altervista.org/productCatalog.owl#AppleWatchSeries6_40mm_GPS_Cellular_Nike> ;
                                                                              <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#precedes> <https://evilscript.altervista.org/productCatalog.owl#Lightning_cable> ;
                                                                              <https://evilscript.altervista.org/productCatalog.owl#containsInBox> <https://evilscript.altervista.org/productCatalog.owl#Lightning_cable> ;
                                                                              <https://evilscript.altervista.org/productCatalog.owl#designedBy> <https://evilscript.altervista.org/productCatalog.owl#Foxconn> ;
                                                                              <https://evilscript.altervista.org/productCatalog.owl#hasBrand> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                              <https://evilscript.altervista.org/productCatalog.owl#isContainedIn> <https://evilscript.altervista.org/productCatalog.owl#AppleCatalog> ;
                                                                              <https://evilscript.altervista.org/productCatalog.owl#producedBy> <https://evilscript.altervista.org/productCatalog.owl#Qualcomm> ;
                                                                              <https://evilscript.altervista.org/productCatalog.owl#soldBy> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                              <https://evilscript.altervista.org/productCatalog.owl#ChargingPortType> "Lightning"^^xsd:string ;
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Color> "White"^^xsd:string ;
                                                                              <https://evilscript.altervista.org/productCatalog.owl#CpuType> "Chip H1"^^xsd:string ;
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Depth> "21.3"^^xsd:double ;
                                                                              <https://evilscript.altervista.org/productCatalog.owl#EAN> "A1938"^^xsd:string ;
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Height> "53.5"^^xsd:double ;
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Price> "229.0"^^xsd:double ;
                                                                              <https://evilscript.altervista.org/productCatalog.owl#ProductName> "AirPods Wireless Charge Case"^^xsd:string ;
                                                                              <https://evilscript.altervista.org/productCatalog.owl#RollOutDate> "2019-03-20T00:00:00"^^xsd:dateTime ;
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Weight> "40.0"^^xsd:double ;
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Width> "44.3"^^xsd:double ;
                                                                              rdfs:comment "EarPlugs with wireless charge case made by Apple"@en ;
                                                                              rdfs:label "AirPods_wirelessCharge"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Apple
<https://evilscript.altervista.org/productCatalog.owl#Apple> rdf:type owl:NamedIndividual ,
                                                                      <http://xmlns.com/foaf/0.1/Organization> ,
                                                                      <https://evilscript.altervista.org/productCatalog.owl#Company> ,
                                                                      <https://evilscript.altervista.org/productCatalog.owl#Manufacturer> ;
                                                             <https://evilscript.altervista.org/productCatalog.owl#collabsWith> <https://evilscript.altervista.org/productCatalog.owl#Nike> ;
                                                             <https://evilscript.altervista.org/productCatalog.owl#hasCatalog> <https://evilscript.altervista.org/productCatalog.owl#AppleCatalog> ;
                                                             <https://evilscript.altervista.org/productCatalog.owl#isBrandOf> <https://evilscript.altervista.org/productCatalog.owl#AirPods_wirelessCharge> ,
                                                                                                                              <https://evilscript.altervista.org/productCatalog.owl#AppleWatchSeries6_40mm_GPS_Cellular_Nike> ,
                                                                                                                              <https://evilscript.altervista.org/productCatalog.owl#IpadAir_2020> ,
                                                                                                                              <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ,
                                                                                                                              <https://evilscript.altervista.org/productCatalog.owl#Lightning_cable> ,
                                                                                                                              <https://evilscript.altervista.org/productCatalog.owl#MacBookAir_M1> ,
                                                                                                                              <https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256> ,
                                                                                                                              <https://evilscript.altervista.org/productCatalog.owl#iPhone12_64> ,
                                                                                                                              <https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64> ;
                                                             <https://evilscript.altervista.org/productCatalog.owl#manufacturesTo> <https://evilscript.altervista.org/productCatalog.owl#BeatsAudio> ,
                                                                                                                                   <https://evilscript.altervista.org/productCatalog.owl#Foxconn> ,
                                                                                                                                   <https://evilscript.altervista.org/productCatalog.owl#Qualcomm> ,
                                                                                                                                   <https://evilscript.altervista.org/productCatalog.owl#ShortFactory> ;
                                                             <https://evilscript.altervista.org/productCatalog.owl#putInBoxes> <https://evilscript.altervista.org/productCatalog.owl#Lightning_cable> ,
                                                                                                                               <https://evilscript.altervista.org/productCatalog.owl#USBC_cable> ;
                                                             <https://evilscript.altervista.org/productCatalog.owl#sells> <https://evilscript.altervista.org/productCatalog.owl#AirPods_wirelessCharge> ,
                                                                                                                          <https://evilscript.altervista.org/productCatalog.owl#AppleWatchSeries6_40mm_GPS_Cellular_Nike> ,
                                                                                                                          <https://evilscript.altervista.org/productCatalog.owl#Beats_cuffie> ,
                                                                                                                          <https://evilscript.altervista.org/productCatalog.owl#IpadAir_2020> ,
                                                                                                                          <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ,
                                                                                                                          <https://evilscript.altervista.org/productCatalog.owl#Lightning_cable> ,
                                                                                                                          <https://evilscript.altervista.org/productCatalog.owl#MacBookAir_M1> ,
                                                                                                                          <https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256> ,
                                                                                                                          <https://evilscript.altervista.org/productCatalog.owl#iPhone12_64> ,
                                                                                                                          <https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64> ;
                                                             rdfs:comment "Famous company that design and sell electronic devices"@en ;
                                                             rdfs:label "Apple"@en .


###  https://evilscript.altervista.org/productCatalog.owl#AppleAccessories
<https://evilscript.altervista.org/productCatalog.owl#AppleAccessories> rdf:type owl:NamedIndividual ,
                                                                                 <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Bag> ,
                                                                                 <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> ,
                                                                                 <http://www.ontologydesignpatterns.org/cp/owl/list.owl#List> ,
                                                                                 <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                                 <https://www.w3.org/ns/dcat#Catalog> ;
                                                                        <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#hasItem> <https://evilscript.altervista.org/productCatalog.owl#AirPods_wirelessCharge> ,
                                                                                                                                       <https://evilscript.altervista.org/productCatalog.owl#AppleWatchSeries6_40mm_GPS_Cellular_Nike> ,
                                                                                                                                       <https://evilscript.altervista.org/productCatalog.owl#Lightning_cable> ;
                                                                        <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#hasMember> <https://evilscript.altervista.org/productCatalog.owl#AirPods_wirelessCharge> ,
                                                                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#AppleWatchSeries6_40mm_GPS_Cellular_Nike> ,
                                                                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#Lightning_cable> ;
                                                                        <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#AppleCatalog> ;
                                                                        <http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasFirstItem> <https://evilscript.altervista.org/productCatalog.owl#Lightning_cable> ;
                                                                        <http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasLastItem> <https://evilscript.altervista.org/productCatalog.owl#AppleWatchSeries6_40mm_GPS_Cellular_Nike> ;
                                                                        rdfs:comment "Section of the Apple Product List that covers Accessories"@en ;
                                                                        rdfs:label "AppleAccessories"@en .


###  https://evilscript.altervista.org/productCatalog.owl#AppleCatalog
<https://evilscript.altervista.org/productCatalog.owl#AppleCatalog> rdf:type owl:NamedIndividual ,
                                                                             <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> ,
                                                                             <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                             <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                             <https://www.w3.org/ns/dcat#Catalog> ;
                                                                    <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#hasMember> <https://evilscript.altervista.org/productCatalog.owl#AppleAccessories> ,
                                                                                                                                                  <https://evilscript.altervista.org/productCatalog.owl#AppleMobile> ,
                                                                                                                                                  <https://evilscript.altervista.org/productCatalog.owl#ApplePC> ,
                                                                                                                                                  <https://evilscript.altervista.org/productCatalog.owl#BeatsEarPlugs> ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#contains> <https://evilscript.altervista.org/productCatalog.owl#AirPods_wirelessCharge> ,
                                                                                                                                    <https://evilscript.altervista.org/productCatalog.owl#AppleWatchSeries6_40mm_GPS_Cellular_Nike> ,
                                                                                                                                    <https://evilscript.altervista.org/productCatalog.owl#Beats_cuffie> ,
                                                                                                                                    <https://evilscript.altervista.org/productCatalog.owl#IpadAir_2020> ,
                                                                                                                                    <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ,
                                                                                                                                    <https://evilscript.altervista.org/productCatalog.owl#Lightning_cable> ,
                                                                                                                                    <https://evilscript.altervista.org/productCatalog.owl#MacBookAir_M1> ,
                                                                                                                                    <https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256> ,
                                                                                                                                    <https://evilscript.altervista.org/productCatalog.owl#iPhone12_64> ,
                                                                                                                                    <https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64> ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#containsBrand> <https://evilscript.altervista.org/productCatalog.owl#Apple> ,
                                                                                                                                         <https://evilscript.altervista.org/productCatalog.owl#BeatsAudio> ;
                                                                    rdfs:comment "Apple web site catalog"@en ;
                                                                    rdfs:label "AppleCatalog"@en .


###  https://evilscript.altervista.org/productCatalog.owl#AppleMobile
<https://evilscript.altervista.org/productCatalog.owl#AppleMobile> rdf:type owl:NamedIndividual ,
                                                                            <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Bag> ,
                                                                            <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> ,
                                                                            <http://www.ontologydesignpatterns.org/cp/owl/list.owl#List> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                            <https://www.w3.org/ns/dcat#Catalog> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#hasItem> <https://evilscript.altervista.org/productCatalog.owl#IpadAir_2020> ,
                                                                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ,
                                                                                                                                  <https://evilscript.altervista.org/productCatalog.owl#iPhone12_64> ,
                                                                                                                                  <https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#hasMember> <https://evilscript.altervista.org/productCatalog.owl#IpadAir_2020> ,
                                                                                                                                                 <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ,
                                                                                                                                                 <https://evilscript.altervista.org/productCatalog.owl#iPhone12_64> ,
                                                                                                                                                 <https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#AppleCatalog> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasFirstItem> <https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasLastItem> <https://evilscript.altervista.org/productCatalog.owl#IpadAir_2020> ;
                                                                   rdfs:comment "Section of the Apple Product List that covers Mobile Phones"@en ;
                                                                   rdfs:label "AppleMobile"@en .


###  https://evilscript.altervista.org/productCatalog.owl#ApplePC
<https://evilscript.altervista.org/productCatalog.owl#ApplePC> rdf:type owl:NamedIndividual ,
                                                                        <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Bag> ,
                                                                        <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> ,
                                                                        <http://www.ontologydesignpatterns.org/cp/owl/list.owl#List> ,
                                                                        <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                        <https://www.w3.org/ns/dcat#Catalog> ;
                                                               <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#hasItem> <https://evilscript.altervista.org/productCatalog.owl#MacBookAir_M1> ,
                                                                                                                              <https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256> ;
                                                               <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#hasMember> <https://evilscript.altervista.org/productCatalog.owl#MacBookAir_M1> ,
                                                                                                                                             <https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256> ;
                                                               <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#AppleCatalog> ;
                                                               <http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasFirstItem> <https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256> ;
                                                               <http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasLastItem> <https://evilscript.altervista.org/productCatalog.owl#MacBookAir_M1> ;
                                                               rdfs:comment "Section of the Apple Product List that covers PCs"@en ;
                                                               rdfs:label "ApplePC"@en .


###  https://evilscript.altervista.org/productCatalog.owl#AppleWatchSeries6_40mm_GPS_Cellular_Nike
<https://evilscript.altervista.org/productCatalog.owl#AppleWatchSeries6_40mm_GPS_Cellular_Nike> rdf:type owl:NamedIndividual ,
                                                                                                         <http://purl.org/dc/dcmitype/PhysicalObject> ,
                                                                                                         <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ,
                                                                                                         <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ,
                                                                                                         <http://www.productontology.org/id/Smartwatch> ,
                                                                                                         <http://www.productontology.org/id/Product_(business)> ,
                                                                                                         <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                                                         <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                                                         <https://evilscript.altervista.org/productCatalog.owl#Product> ,
                                                                                                         <https://evilscript.altervista.org/productCatalog.owl#ProductHigh> ,
                                                                                                         <https://evilscript.altervista.org/productCatalog.owl#Smartwatch> ;
                                                                                                <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> <https://evilscript.altervista.org/productCatalog.owl#AppleAccessories> ;
                                                                                                <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#AppleAccessories> ;
                                                                                                <http://www.ontologydesignpatterns.org/cp/owl/list.owl#lastItemOf> <https://evilscript.altervista.org/productCatalog.owl#AppleAccessories> ;
                                                                                                <http://www.ontologydesignpatterns.org/cp/owl/list.owl#previousItem> <https://evilscript.altervista.org/productCatalog.owl#AirPods_wirelessCharge> ;
                                                                                                <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasPrice> <https://evilscript.altervista.org/productCatalog.owl#500Euro> ;
                                                                                                <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyPrecedes> <https://evilscript.altervista.org/productCatalog.owl#AirPods_wirelessCharge> ;
                                                                                                <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#precedes> <https://evilscript.altervista.org/productCatalog.owl#AirPods_wirelessCharge> ,
                                                                                                                                                                     <https://evilscript.altervista.org/productCatalog.owl#Lightning_cable> ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#compatibleWith> <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ,
                                                                                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#iPhone12_64> ,
                                                                                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64> ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#designedBy> <https://evilscript.altervista.org/productCatalog.owl#Foxconn> ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#hasBrand> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#inCollabWith> <https://evilscript.altervista.org/productCatalog.owl#Nike> ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#isContainedIn> <https://evilscript.altervista.org/productCatalog.owl#AppleCatalog> ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#needsConnectionWith> <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ,
                                                                                                                                                                           <https://evilscript.altervista.org/productCatalog.owl#iPhone12_64> ,
                                                                                                                                                                           <https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64> ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#producedBy> <https://evilscript.altervista.org/productCatalog.owl#Qualcomm> ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#soldBy> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Color> "Silver, Graphite (DLC), Gold (PVD)"^^xsd:string ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#CpuType> "Dual-core"^^xsd:string ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Depth> "10.4"^^xsd:double ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#EAN> "A2293"^^xsd:string ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Height> "40.0"^^xsd:double ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#MemorySize> "32"^^xsd:nonNegativeInteger ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#OperativeSystem> "watchOS 7.0"^^xsd:string ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Price> "539.0"^^xsd:double ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#ProductName> "Apple Watch 6 Nike 40mm GPS+Cellular"^^xsd:string ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#RamSize> "1"^^xsd:nonNegativeInteger ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#RollOutDate> "2020-09-19T00:00:00"^^xsd:dateTime ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#ScreenSize> "1.57"^^xsd:double ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Weight> "39.7"^^xsd:double ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Width> "34.0"^^xsd:double ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#isInRange> "High"^^xsd:string ;
                                                                                                <https://evilscript.altervista.org/productCatalog.owl#isTouchScreen> "true"^^xsd:boolean ;
                                                                                                rdfs:comment "Top 2020 smartwatch made by Apple"@en ;
                                                                                                rdfs:label "AppleWatchSeries6_40mm_GPS_Cellular"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Asus
<https://evilscript.altervista.org/productCatalog.owl#Asus> rdf:type owl:NamedIndividual ,
                                                                     <http://xmlns.com/foaf/0.1/Organization> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#Company> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#Engineering> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#ITEngineering> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#Manufacturer> ;
                                                            <https://evilscript.altervista.org/productCatalog.owl#designs> <https://evilscript.altervista.org/productCatalog.owl#ZenBookFlip_S_UX371> ;
                                                            <https://evilscript.altervista.org/productCatalog.owl#hasCatalog> <https://evilscript.altervista.org/productCatalog.owl#AsusCatalog> ;
                                                            <https://evilscript.altervista.org/productCatalog.owl#isBrandOf> <https://evilscript.altervista.org/productCatalog.owl#ZenBookFlip_S_UX371> ;
                                                            <https://evilscript.altervista.org/productCatalog.owl#manufacturesTo> <https://evilscript.altervista.org/productCatalog.owl#Asus> ,
                                                                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Huáshuò> ;
                                                            <https://evilscript.altervista.org/productCatalog.owl#sells> <https://evilscript.altervista.org/productCatalog.owl#ZenBookFlip_S_UX371> ;
                                                            rdfs:comment "AsusTek is a Taiwanese multinational computer and phone hardware and electronics company headquartered in Beitou District, Taipei, Taiwan."@en ;
                                                            rdfs:label "Asus"@en .


###  https://evilscript.altervista.org/productCatalog.owl#AsusCatalog
<https://evilscript.altervista.org/productCatalog.owl#AsusCatalog> rdf:type owl:NamedIndividual ,
                                                                            <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                            <https://www.w3.org/ns/dcat#Catalog> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#hasMember> <https://evilscript.altervista.org/productCatalog.owl#AsusPC> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#contains> <https://evilscript.altervista.org/productCatalog.owl#ZenBookFlip_S_UX371> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#containsBrand> <https://evilscript.altervista.org/productCatalog.owl#Asus> ;
                                                                   rdfs:comment "Asus web site catalog"@en ;
                                                                   rdfs:label "AsusCatalog"@en .


###  https://evilscript.altervista.org/productCatalog.owl#AsusPC
<https://evilscript.altervista.org/productCatalog.owl#AsusPC> rdf:type owl:NamedIndividual ,
                                                                       <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Bag> ,
                                                                       <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> ,
                                                                       <http://www.ontologydesignpatterns.org/cp/owl/list.owl#List> ,
                                                                       <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                       <https://www.w3.org/ns/dcat#Catalog> ;
                                                              <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#hasItem> <https://evilscript.altervista.org/productCatalog.owl#ZenBookFlip_S_UX371> ;
                                                              <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#hasMember> <https://evilscript.altervista.org/productCatalog.owl#ZenBookFlip_S_UX371> ;
                                                              <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#AsusCatalog> ;
                                                              <http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasFirstItem> <https://evilscript.altervista.org/productCatalog.owl#ZenBookFlip_S_UX371> ;
                                                              <http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasLastItem> <https://evilscript.altervista.org/productCatalog.owl#ZenBookFlip_S_UX371> ;
                                                              rdfs:comment "Section of the Asus Product List that covers PCs"@en ;
                                                              rdfs:label "AsusPC"@en .


###  https://evilscript.altervista.org/productCatalog.owl#BeatsAudio
<https://evilscript.altervista.org/productCatalog.owl#BeatsAudio> rdf:type owl:NamedIndividual ,
                                                                           <http://xmlns.com/foaf/0.1/Organization> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Company> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Engineering> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Manufacturer> ;
                                                                  <https://evilscript.altervista.org/productCatalog.owl#designs> <https://evilscript.altervista.org/productCatalog.owl#Beats_cuffie> ;
                                                                  <https://evilscript.altervista.org/productCatalog.owl#isBrandOf> <https://evilscript.altervista.org/productCatalog.owl#Beats_cuffie> ;
                                                                  rdfs:comment "Company that sells audio products"@en ;
                                                                  rdfs:label "BeatsAudio"@en .


###  https://evilscript.altervista.org/productCatalog.owl#BeatsEarPlugs
<https://evilscript.altervista.org/productCatalog.owl#BeatsEarPlugs> rdf:type owl:NamedIndividual ,
                                                                              <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Bag> ,
                                                                              <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> ,
                                                                              <http://www.ontologydesignpatterns.org/cp/owl/list.owl#List> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                              <https://www.w3.org/ns/dcat#Catalog> ;
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#hasItem> <https://evilscript.altervista.org/productCatalog.owl#Beats_cuffie> ;
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#hasMember> <https://evilscript.altervista.org/productCatalog.owl#Beats_cuffie> ;
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#AppleCatalog> ;
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasFirstItem> <https://evilscript.altervista.org/productCatalog.owl#Beats_cuffie> ;
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasLastItem> <https://evilscript.altervista.org/productCatalog.owl#Beats_cuffie> ;
                                                                     rdfs:comment "Section of the Beats Product List that covers Earplugs"@en ;
                                                                     rdfs:label "BeatsEarPlugs"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Beats_cuffie
<https://evilscript.altervista.org/productCatalog.owl#Beats_cuffie> rdf:type owl:NamedIndividual ,
                                                                             <http://purl.org/dc/dcmitype/PhysicalObject> ,
                                                                             <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ,
                                                                             <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ,
                                                                             <http://www.productontology.org/id/Headphones> ,
                                                                             <http://www.productontology.org/id/Product_(business)> ,
                                                                             <https://evilscript.altervista.org/productCatalog.owl#Accessory> ,
                                                                             <https://evilscript.altervista.org/productCatalog.owl#EarPlugs> ,
                                                                             <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                    <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> <https://evilscript.altervista.org/productCatalog.owl#BeatsEarPlugs> ;
                                                                    <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#BeatsEarPlugs> ;
                                                                    <http://www.ontologydesignpatterns.org/cp/owl/list.owl#firstItemOf> <https://evilscript.altervista.org/productCatalog.owl#BeatsEarPlugs> ;
                                                                    <http://www.ontologydesignpatterns.org/cp/owl/list.owl#lastItemOf> <https://evilscript.altervista.org/productCatalog.owl#BeatsEarPlugs> ;
                                                                    <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasPrice> <https://evilscript.altervista.org/productCatalog.owl#200Euro> ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#designedBy> <https://evilscript.altervista.org/productCatalog.owl#BeatsAudio> ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#hasBrand> <https://evilscript.altervista.org/productCatalog.owl#BeatsAudio> ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#isContainedIn> <https://evilscript.altervista.org/productCatalog.owl#AppleCatalog> ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#producedBy> <https://evilscript.altervista.org/productCatalog.owl#ShortFactory> ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#soldBy> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                    rdfs:comment "Over ear made by BeatsAudio"@en ;
                                                                    rdfs:label "Beats_cuffie"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Euro
<https://evilscript.altervista.org/productCatalog.owl#Euro> rdf:type owl:NamedIndividual ,
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/price.owl#Currency> ;
                                                            rdfs:comment "European Currency"@en ;
                                                            rdfs:label "Euro"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Foxconn
<https://evilscript.altervista.org/productCatalog.owl#Foxconn> rdf:type owl:NamedIndividual ,
                                                                        <http://xmlns.com/foaf/0.1/Organization> ,
                                                                        <https://evilscript.altervista.org/productCatalog.owl#BigEngineering> ,
                                                                        <https://evilscript.altervista.org/productCatalog.owl#Company> ,
                                                                        <https://evilscript.altervista.org/productCatalog.owl#Engineering> ,
                                                                        <https://evilscript.altervista.org/productCatalog.owl#ITEngineering> ,
                                                                        <https://evilscript.altervista.org/productCatalog.owl#Manufacturer> ;
                                                               <https://evilscript.altervista.org/productCatalog.owl#designs> <https://evilscript.altervista.org/productCatalog.owl#AirPods_wirelessCharge> ,
                                                                                                                              <https://evilscript.altervista.org/productCatalog.owl#AppleWatchSeries6_40mm_GPS_Cellular_Nike> ,
                                                                                                                              <https://evilscript.altervista.org/productCatalog.owl#IpadAir_2020> ,
                                                                                                                              <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ,
                                                                                                                              <https://evilscript.altervista.org/productCatalog.owl#MacBookAir_M1> ,
                                                                                                                              <https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256> ,
                                                                                                                              <https://evilscript.altervista.org/productCatalog.owl#iPhone12_64> ;
                                                               rdfs:comment "ITengineering company that designs CPUs for Apple"@en ;
                                                               rdfs:label "Foxconn"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Giovanni_PowerUser
<https://evilscript.altervista.org/productCatalog.owl#Giovanni_PowerUser> rdf:type owl:NamedIndividual ,
                                                                                   <http://xmlns.com/foaf/0.1/Person> ,
                                                                                   <https://evilscript.altervista.org/productCatalog.owl#PowerUser> ,
                                                                                   <https://evilscript.altervista.org/productCatalog.owl#User> ;
                                                                          <https://evilscript.altervista.org/productCatalog.owl#buysProduct> <https://evilscript.altervista.org/productCatalog.owl#MacBookAir_M1> ,
                                                                                                                                             <https://evilscript.altervista.org/productCatalog.owl#iPhone12_64> ;
                                                                          rdfs:label "Giovanni"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Huáshuò
<https://evilscript.altervista.org/productCatalog.owl#Huáshuò> rdf:type owl:NamedIndividual ,
                                                                        <http://xmlns.com/foaf/0.1/Organization> ,
                                                                        <https://evilscript.altervista.org/productCatalog.owl#Company> ,
                                                                        <https://evilscript.altervista.org/productCatalog.owl#Factory> ,
                                                                        <https://evilscript.altervista.org/productCatalog.owl#Manufacturer> ;
                                                               <https://evilscript.altervista.org/productCatalog.owl#isManifacturerOf> <https://evilscript.altervista.org/productCatalog.owl#Samsung> ;
                                                               <https://evilscript.altervista.org/productCatalog.owl#produces> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS10_global> ,
                                                                                                                               <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS20_5G_global> ,
                                                                                                                               <https://evilscript.altervista.org/productCatalog.owl#ZenBookFlip_S_UX371> ;
                                                               rdfs:comment "Huáshuò is a company under the favor of Samsung that produces many products"@en ;
                                                               rdfs:label "Huáshuò"@en .


###  https://evilscript.altervista.org/productCatalog.owl#IpadAir_2020
<https://evilscript.altervista.org/productCatalog.owl#IpadAir_2020> rdf:type owl:NamedIndividual ,
                                                                             <http://purl.org/dc/dcmitype/PhysicalObject> ,
                                                                             <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ,
                                                                             <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ,
                                                                             <http://www.productontology.org/id/Tablet_computer> ,
                                                                             <http://www.productontology.org/id/Product_(business)> ,
                                                                             <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                             <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                             <https://evilscript.altervista.org/productCatalog.owl#Product> ,
                                                                             <https://evilscript.altervista.org/productCatalog.owl#ProductMedium> ,
                                                                             <https://evilscript.altervista.org/productCatalog.owl#Tablet> ;
                                                                    <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> <https://evilscript.altervista.org/productCatalog.owl#AppleMobile> ;
                                                                    <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#AppleMobile> ;
                                                                    <http://www.ontologydesignpatterns.org/cp/owl/list.owl#lastItemOf> <https://evilscript.altervista.org/productCatalog.owl#AppleMobile> ;
                                                                    <http://www.ontologydesignpatterns.org/cp/owl/list.owl#previousItem> <https://evilscript.altervista.org/productCatalog.owl#iPhone12_64> ;
                                                                    <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasPrice> <https://evilscript.altervista.org/productCatalog.owl#600Euro> ;
                                                                    <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyPrecedes> <https://evilscript.altervista.org/productCatalog.owl#iPhone12_64> ;
                                                                    <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#precedes> <https://evilscript.altervista.org/productCatalog.owl#iPhone12_64> ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#containsInBox> <https://evilscript.altervista.org/productCatalog.owl#USBC_cable> ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#designedBy> <https://evilscript.altervista.org/productCatalog.owl#Foxconn> ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#hasBrand> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#isContainedIn> <https://evilscript.altervista.org/productCatalog.owl#AppleCatalog> ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#producedBy> <https://evilscript.altervista.org/productCatalog.owl#Qualcomm> ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#soldBy> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#CameraMP> "12.0"^^xsd:double ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#ChargingPortType> "USB-C"^^xsd:string ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#Color> "Space Gray, Silver, Rose Gold, Green, Sky Blue"^^xsd:string ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#CpuType> "Apple A14 Bionic (5 nm)"^^xsd:string ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#Depth> "6.1"^^xsd:double ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#Height> "247.6"^^xsd:double ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#MemorySize> "64"^^xsd:nonNegativeInteger ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#OperativeSystem> "iPadOS 14.1"^^xsd:string ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#Price> "640.0"^^xsd:double ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#ProductName> "Apple iPad Air (2020)"^^xsd:string ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#RamSize> "3"^^xsd:nonNegativeInteger ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#RollOutDate> "2020-09-15T00:00:00"^^xsd:dateTime ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#ScreenSize> "10.9"^^xsd:double ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#Weight> "458.0"^^xsd:double ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#Width> "178.5"^^xsd:double ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#isInRange> "Medium"^^xsd:string ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#isTouchScreen> "true"^^xsd:boolean ;
                                                                    rdfs:comment "Tablet made by Apple"@en ;
                                                                    rdfs:label "iPadAir_2020"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Iphone11_64
<https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> rdf:type owl:NamedIndividual ,
                                                                            <http://purl.org/dc/dcmitype/PhysicalObject> ,
                                                                            <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ,
                                                                            <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ,
                                                                            <http://www.productontology.org/id/Smartphone> ,
                                                                            <http://www.productontology.org/id/Product_(business)> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#Product> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#ProductMedium> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> <https://evilscript.altervista.org/productCatalog.owl#AppleMobile> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#AppleMobile> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/list.owl#nextItem> <https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/list.owl#previousItem> <https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasPrice> <https://evilscript.altervista.org/productCatalog.owl#600Euro> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyFollows> <https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyPrecedes> <https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#follows> <https://evilscript.altervista.org/productCatalog.owl#MacBookAir_M1> ,
                                                                                                                                       <https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#precedes> <https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#containsInBox> <https://evilscript.altervista.org/productCatalog.owl#Lightning_cable> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#designedBy> <https://evilscript.altervista.org/productCatalog.owl#Foxconn> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#hasBrand> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#isContainedIn> <https://evilscript.altervista.org/productCatalog.owl#AppleCatalog> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#predecessorOf> <https://evilscript.altervista.org/productCatalog.owl#iPhone12_64> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#producedBy> <https://evilscript.altervista.org/productCatalog.owl#Qualcomm> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#soldBy> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#successorOf> <https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#CameraMP> "12.0"^^xsd:double ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#ChargingPortType> "Lightning"^^xsd:string ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#Color> "Black, Green, Yellow, Purple, Red, White"^^xsd:string ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#CpuType> "Apple A13 Bionic"^^xsd:string ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#Depth> "8.3"^^xsd:double ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#EAN> "A2221"^^xsd:string ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#Height> "150.9"^^xsd:double ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#MemorySize> 64 ,
                                                                                                                                     "64"^^xsd:nonNegativeInteger ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#OperativeSystem> "iOS 13"^^xsd:string ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#Price> "719.0"^^xsd:double ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#ProductName> "Iphone 11 64GB"^^xsd:string ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#RamSize> "4"^^xsd:nonNegativeInteger ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#RollOutDate> "2019-09-20T00:00:00"^^xsd:dateTime ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#ScreenSize> "6.1"^^xsd:double ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#Weight> "194.0"^^xsd:double ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#Width> "75.7"^^xsd:double ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#isInRange> "Medium"^^xsd:string ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#isTouchScreen> "true"^^xsd:boolean ;
                                                                   rdfs:comment "Top 2019 smartphone made by Apple"@en ;
                                                                   rdfs:label "iPhone11_64"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Lightning_cable
<https://evilscript.altervista.org/productCatalog.owl#Lightning_cable> rdf:type owl:NamedIndividual ,
                                                                                <http://purl.org/dc/dcmitype/PhysicalObject> ,
                                                                                <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ,
                                                                                <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ,
                                                                                <http://www.productontology.org/id/Power_cable> ,
                                                                                <http://www.productontology.org/id/Product_(business)> ,
                                                                                <https://evilscript.altervista.org/productCatalog.owl#Accessory> ,
                                                                                <https://evilscript.altervista.org/productCatalog.owl#Cable> ,
                                                                                <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                       <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> <https://evilscript.altervista.org/productCatalog.owl#AppleAccessories> ;
                                                                       <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#AppleAccessories> ;
                                                                       <http://www.ontologydesignpatterns.org/cp/owl/list.owl#firstItemOf> <https://evilscript.altervista.org/productCatalog.owl#AppleAccessories> ;
                                                                       <http://www.ontologydesignpatterns.org/cp/owl/list.owl#nextItem> <https://evilscript.altervista.org/productCatalog.owl#AirPods_wirelessCharge> ;
                                                                       <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasPrice> <https://evilscript.altervista.org/productCatalog.owl#10Euro> ;
                                                                       <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyFollows> <https://evilscript.altervista.org/productCatalog.owl#AirPods_wirelessCharge> ;
                                                                       <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#follows> <https://evilscript.altervista.org/productCatalog.owl#AirPods_wirelessCharge> ,
                                                                                                                                           <https://evilscript.altervista.org/productCatalog.owl#AppleWatchSeries6_40mm_GPS_Cellular_Nike> ;
                                                                       <https://evilscript.altervista.org/productCatalog.owl#hasBrand> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                       <https://evilscript.altervista.org/productCatalog.owl#inBoxOf> <https://evilscript.altervista.org/productCatalog.owl#AirPods_wirelessCharge> ,
                                                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ,
                                                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#iPhone12_64> ,
                                                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64> ;
                                                                       <https://evilscript.altervista.org/productCatalog.owl#isContainedIn> <https://evilscript.altervista.org/productCatalog.owl#AppleCatalog> ;
                                                                       <https://evilscript.altervista.org/productCatalog.owl#soldBy> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                       rdfs:comment "The standard cable for iPhones"@en ;
                                                                       rdfs:label "Lightning_cable"@en .


###  https://evilscript.altervista.org/productCatalog.owl#MacBookAir_M1
<https://evilscript.altervista.org/productCatalog.owl#MacBookAir_M1> rdf:type owl:NamedIndividual ,
                                                                              <http://purl.org/dc/dcmitype/PhysicalObject> ,
                                                                              <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ,
                                                                              <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ,
                                                                              <http://www.productontology.org/id/Laptop> ,
                                                                              <http://www.productontology.org/id/Product_(business)> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Laptop> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Product> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#ProductMedium> ;
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> <https://evilscript.altervista.org/productCatalog.owl#ApplePC> ;
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#ApplePC> ;
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/list.owl#lastItemOf> <https://evilscript.altervista.org/productCatalog.owl#ApplePC> ;
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/list.owl#previousItem> <https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256> ;
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasPrice> <https://evilscript.altervista.org/productCatalog.owl#1000Euro> ;
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyPrecedes> <https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256> ;
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#precedes> <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ,
                                                                                                                                          <https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256> ,
                                                                                                                                          <https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64> ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#designedBy> <https://evilscript.altervista.org/productCatalog.owl#Foxconn> ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#hasBrand> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#isContainedIn> <https://evilscript.altervista.org/productCatalog.owl#AppleCatalog> ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#producedBy> <https://evilscript.altervista.org/productCatalog.owl#Qualcomm> ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#soldBy> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#ChargingPortType> "USB-C"^^xsd:string ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#Color> "Gold, Silver, Space Gray"^^xsd:string ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#CpuType> "Apple M1 chip"^^xsd:string ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#Depth> "212.4"^^xsd:double ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#Height> "16.1"^^xsd:double ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#MemorySize> "256"^^xsd:nonNegativeInteger ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#OperativeSystem> "macOS Big Sur"^^xsd:string ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#Price> "1159.0"^^xsd:double ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#ProductName> "MacBook Air (M1, 2020)"^^xsd:string ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#RamSize> "8"^^xsd:nonNegativeInteger ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#RamType> "DDR4"^^xsd:string ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#RollOutDate> "2020-11-17T00:00:00"^^xsd:dateTime ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#ScreenSize> "13.3"^^xsd:double ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#Weight> "1.29"^^xsd:double ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#Width> "304.1"^^xsd:double ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#isInRange> "Medium"^^xsd:string ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#isTouchScreen> "false"^^xsd:boolean ;
                                                                     rdfs:comment "Laptop with M1 Chip made by Apple"@en ;
                                                                     rdfs:label "MacBookAir_M1"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Michela_CasualUser
<https://evilscript.altervista.org/productCatalog.owl#Michela_CasualUser> rdf:type owl:NamedIndividual ,
                                                                                   <http://xmlns.com/foaf/0.1/Person> ,
                                                                                   <https://evilscript.altervista.org/productCatalog.owl#User> ;
                                                                          <https://evilscript.altervista.org/productCatalog.owl#buysFrom> <https://evilscript.altervista.org/productCatalog.owl#SamsungCatalag> ;
                                                                          <https://evilscript.altervista.org/productCatalog.owl#buysProduct> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS10_global> ;
                                                                          rdfs:label "Michela"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Nike
<https://evilscript.altervista.org/productCatalog.owl#Nike> rdf:type owl:NamedIndividual ,
                                                                     <http://xmlns.com/foaf/0.1/Organization> ,
                                                                     <https://evilscript.altervista.org/productCatalog.owl#Company> ;
                                                            rdfs:comment "A company that sells sports products"@en ;
                                                            rdfs:label "Nike"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Qualcomm
<https://evilscript.altervista.org/productCatalog.owl#Qualcomm> rdf:type owl:NamedIndividual ,
                                                                         <http://xmlns.com/foaf/0.1/Organization> ,
                                                                         <https://evilscript.altervista.org/productCatalog.owl#Company> ,
                                                                         <https://evilscript.altervista.org/productCatalog.owl#Factory> ,
                                                                         <https://evilscript.altervista.org/productCatalog.owl#Manufacturer> ;
                                                                <https://evilscript.altervista.org/productCatalog.owl#produces> <https://evilscript.altervista.org/productCatalog.owl#AirPods_wirelessCharge> ,
                                                                                                                                <https://evilscript.altervista.org/productCatalog.owl#AppleWatchSeries6_40mm_GPS_Cellular_Nike> ,
                                                                                                                                <https://evilscript.altervista.org/productCatalog.owl#IpadAir_2020> ,
                                                                                                                                <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ,
                                                                                                                                <https://evilscript.altervista.org/productCatalog.owl#MacBookAir_M1> ,
                                                                                                                                <https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256> ,
                                                                                                                                <https://evilscript.altervista.org/productCatalog.owl#iPhone12_64> ;
                                                                rdfs:comment "Factory company that produces CPUs for Apple"@en ;
                                                                rdfs:label "Qualcomm"@en .


###  https://evilscript.altervista.org/productCatalog.owl#Samsung
<https://evilscript.altervista.org/productCatalog.owl#Samsung> rdf:type owl:NamedIndividual ,
                                                                        <http://xmlns.com/foaf/0.1/Organization> ,
                                                                        <https://evilscript.altervista.org/productCatalog.owl#Company> ,
                                                                        <https://evilscript.altervista.org/productCatalog.owl#Manufacturer> ;
                                                               <https://evilscript.altervista.org/productCatalog.owl#brandContainedIn> <https://evilscript.altervista.org/productCatalog.owl#SamsungCatalag> ;
                                                               <https://evilscript.altervista.org/productCatalog.owl#hasCatalog> <https://evilscript.altervista.org/productCatalog.owl#SamsungCatalag> ;
                                                               <https://evilscript.altervista.org/productCatalog.owl#isBrandOf> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS10_global> ,
                                                                                                                                <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS20_5G_global> ,
                                                                                                                                <https://evilscript.altervista.org/productCatalog.owl#USBC_cable> ;
                                                               <https://evilscript.altervista.org/productCatalog.owl#manufacturesTo> <https://evilscript.altervista.org/productCatalog.owl#Huáshuò> ,
                                                                                                                                     <https://evilscript.altervista.org/productCatalog.owl#ShortEngineer> ;
                                                               <https://evilscript.altervista.org/productCatalog.owl#putInBoxes> <https://evilscript.altervista.org/productCatalog.owl#USBC_cable> ;
                                                               <https://evilscript.altervista.org/productCatalog.owl#sells> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS10_global> ,
                                                                                                                            <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS20_5G_global> ,
                                                                                                                            <https://evilscript.altervista.org/productCatalog.owl#USBC_cable> ;
                                                               rdfs:comment "Samsung is a South Korean multinational electronics company headquartered in the Yeongtong District of Suwon"@en ;
                                                               rdfs:label "Samsung"@en .


###  https://evilscript.altervista.org/productCatalog.owl#SamsungAccessories
<https://evilscript.altervista.org/productCatalog.owl#SamsungAccessories> rdf:type owl:NamedIndividual ,
                                                                                   <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Bag> ,
                                                                                   <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> ,
                                                                                   <http://www.ontologydesignpatterns.org/cp/owl/list.owl#List> ,
                                                                                   <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                                   <https://www.w3.org/ns/dcat#Catalog> ;
                                                                          <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#hasItem> <https://evilscript.altervista.org/productCatalog.owl#USBC_cable> ;
                                                                          <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#hasMember> <https://evilscript.altervista.org/productCatalog.owl#USBC_cable> ;
                                                                          <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#SamsungCatalag> ;
                                                                          <http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasFirstItem> <https://evilscript.altervista.org/productCatalog.owl#USBC_cable> ;
                                                                          <http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasLastItem> <https://evilscript.altervista.org/productCatalog.owl#USBC_cable> ;
                                                                          rdfs:comment "Section of the Samsung Product List that covers Accessories"@en ;
                                                                          rdfs:label "SamsungAccessories"@en .


###  https://evilscript.altervista.org/productCatalog.owl#SamsungCatalag
<https://evilscript.altervista.org/productCatalog.owl#SamsungCatalag> rdf:type owl:NamedIndividual ,
                                                                               <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> ,
                                                                               <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                               <https://evilscript.altervista.org/productCatalog.owl#SellingCatalog> ,
                                                                               <https://www.w3.org/ns/dcat#Catalog> ;
                                                                      <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#hasMember> <https://evilscript.altervista.org/productCatalog.owl#SamsungAccessories> ,
                                                                                                                                                    <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxy> ;
                                                                      <https://evilscript.altervista.org/productCatalog.owl#contains> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS10_global> ,
                                                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS20_5G_global> ,
                                                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#USBC_cable> ;
                                                                      <https://evilscript.altervista.org/productCatalog.owl#containsBrand> <https://evilscript.altervista.org/productCatalog.owl#Samsung> ;
                                                                      rdfs:comment "Samsung web site catalog"@en ;
                                                                      rdfs:label "SamsungCatalog"@en .


###  https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxy
<https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxy> rdf:type owl:NamedIndividual ,
                                                                              <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Bag> ,
                                                                              <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#Collection> ,
                                                                              <http://www.ontologydesignpatterns.org/cp/owl/list.owl#List> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#ProductCatalog> ,
                                                                              <https://www.w3.org/ns/dcat#Catalog> ;
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#hasItem> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS10_global> ,
                                                                                                                                    <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS20_5G_global> ;
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#hasMember> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS10_global> ,
                                                                                                                                                   <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS20_5G_global> ;
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#SamsungCatalag> ;
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasFirstItem> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS10_global> ;
                                                                     <http://www.ontologydesignpatterns.org/cp/owl/list.owl#hasLastItem> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS20_5G_global> ;
                                                                     rdfs:comment "Section of the Samsung Product List that covers Phones"@en ;
                                                                     rdfs:label "SamsungGalaxy"@en .


###  https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS10_global
<https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS10_global> rdf:type owl:NamedIndividual ,
                                                                                        <http://purl.org/dc/dcmitype/PhysicalObject> ,
                                                                                        <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ,
                                                                                        <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ,
                                                                                        <http://www.productontology.org/id/Smartphone> ,
                                                                                        <http://www.productontology.org/id/Product_(business)> ,
                                                                                        <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                                        <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                                        <https://evilscript.altervista.org/productCatalog.owl#Product> ,
                                                                                        <https://evilscript.altervista.org/productCatalog.owl#ProductMedium> ,
                                                                                        <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ;
                                                                               <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxy> ;
                                                                               <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxy> ;
                                                                               <http://www.ontologydesignpatterns.org/cp/owl/list.owl#firstItemOf> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxy> ;
                                                                               <http://www.ontologydesignpatterns.org/cp/owl/list.owl#nextItem> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS20_5G_global> ;
                                                                               <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasPrice> <https://evilscript.altervista.org/productCatalog.owl#500Euro> ;
                                                                               <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyFollows> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS20_5G_global> ;
                                                                               <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#follows> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS20_5G_global> ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#containsInBox> <https://evilscript.altervista.org/productCatalog.owl#USBC_cable> ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#designedBy> <https://evilscript.altervista.org/productCatalog.owl#ShortEngineer> ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#hasBrand> <https://evilscript.altervista.org/productCatalog.owl#Samsung> ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#isContainedIn> <https://evilscript.altervista.org/productCatalog.owl#SamsungCatalag> ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#predecessorOf> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS20_5G_global> ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#producedBy> <https://evilscript.altervista.org/productCatalog.owl#Huáshuò> ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#soldBy> <https://evilscript.altervista.org/productCatalog.owl#Samsung> ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#CameraMP> "16.0"^^xsd:double ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#ChargingPortType> "USB-C"^^xsd:string ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#Color> "Prism White, Prism Black, Prism Green, Prism Blue, Canary Yellow, Flamingo Pink, Cardinal Red, Smoke Blue"^^xsd:string ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#CpuType> "Exynos 9820 (8 nm)"^^xsd:string ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#Depth> "7.8"^^xsd:double ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#EAN> "SM-G973F/DS"^^xsd:string ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#Height> "149.9"^^xsd:double ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#MemorySize> "128"^^xsd:nonNegativeInteger ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#OperativeSystem> "Android9"^^xsd:string ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#Price> "549.0"^^xsd:double ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#ProductName> "Samsung Galaxy S10 128"^^xsd:string ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#RamSize> "8"^^xsd:nonNegativeInteger ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#RollOutDate> "2019-03-09T00:00:00"^^xsd:dateTime ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#ScreenSize> "6.1"^^xsd:double ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#Weight> "157.0"^^xsd:double ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#Width> "70.4"^^xsd:double ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#isInRange> "Medium"^^xsd:string ;
                                                                               <https://evilscript.altervista.org/productCatalog.owl#isTouchScreen> "true"^^xsd:boolean ;
                                                                               rdfs:label "SamsungGalaxyS10_global"@en ,
                                                                                          "Smarphone made by Samsung"@en .


###  https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS20_5G_global
<https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS20_5G_global> rdf:type owl:NamedIndividual ,
                                                                                           <http://purl.org/dc/dcmitype/PhysicalObject> ,
                                                                                           <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ,
                                                                                           <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ,
                                                                                           <http://www.productontology.org/id/Smartphone> ,
                                                                                           <http://www.productontology.org/id/Product_(business)> ,
                                                                                           <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                                           <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                                           <https://evilscript.altervista.org/productCatalog.owl#Product> ,
                                                                                           <https://evilscript.altervista.org/productCatalog.owl#ProductHigh> ,
                                                                                           <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ;
                                                                                  <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxy> ;
                                                                                  <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxy> ;
                                                                                  <http://www.ontologydesignpatterns.org/cp/owl/list.owl#lastItemOf> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxy> ;
                                                                                  <http://www.ontologydesignpatterns.org/cp/owl/list.owl#previousItem> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS10_global> ;
                                                                                  <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasPrice> <https://evilscript.altervista.org/productCatalog.owl#800Euro> ;
                                                                                  <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyPrecedes> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS10_global> ;
                                                                                  <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#precedes> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS10_global> ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#containsInBox> <https://evilscript.altervista.org/productCatalog.owl#USBC_cable> ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#designedBy> <https://evilscript.altervista.org/productCatalog.owl#ShortEngineer> ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#hasBrand> <https://evilscript.altervista.org/productCatalog.owl#Samsung> ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#isContainedIn> <https://evilscript.altervista.org/productCatalog.owl#SamsungCatalag> ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#producedBy> <https://evilscript.altervista.org/productCatalog.owl#Huáshuò> ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#soldBy> <https://evilscript.altervista.org/productCatalog.owl#Samsung> ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#successorOf> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS10_global> ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#CameraMP> "64.0"^^xsd:double ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#ChargingPortType> "USB-C"^^xsd:string ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Color> "Cosmic Grey, Cloud Blue, Cloud Pink, Cloud White, Aura Red"^^xsd:string ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#CpuType> "Exynos 990 (7 nm+)"^^xsd:string ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Depth> "7.9"^^xsd:double ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#EAN> "SM-G981F"^^xsd:string ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Height> "15.7"^^xsd:double ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#MemorySize> "128"^^xsd:nonNegativeInteger ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#OperativeSystem> "Android10"^^xsd:string ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Price> "1029.0"^^xsd:double ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#ProductName> "Samsung Galaxy S20 5G 128"^^xsd:string ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#RamSize> "8"^^xsd:nonNegativeInteger ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#RollOutDate> "2020-03-06T00:00:00"^^xsd:dateTime ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#ScreenSize> "6.2"^^xsd:double ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Weight> "163.0"^^xsd:double ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Width> "69.1"^^xsd:double ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#isInRange> "High"^^xsd:string ;
                                                                                  <https://evilscript.altervista.org/productCatalog.owl#isTouchScreen> "true"^^xsd:boolean ;
                                                                                  rdfs:comment "Smarphone made by Samsung"@en ;
                                                                                  rdfs:label "SamsungGalaxyS20_5G_global"@en .


###  https://evilscript.altervista.org/productCatalog.owl#ShortEngineer
<https://evilscript.altervista.org/productCatalog.owl#ShortEngineer> rdf:type owl:NamedIndividual ,
                                                                              <http://xmlns.com/foaf/0.1/Organization> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Company> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Engineering> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#ITEngineering> ,
                                                                              <https://evilscript.altervista.org/productCatalog.owl#Manufacturer> ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#designs> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS10_global> ,
                                                                                                                                    <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS20_5G_global> ;
                                                                     <https://evilscript.altervista.org/productCatalog.owl#isManifacturerOf> <https://evilscript.altervista.org/productCatalog.owl#Samsung> ;
                                                                     rdfs:comment "A company that does not exist"@en ;
                                                                     rdfs:label "ShortEngineer"@en .


###  https://evilscript.altervista.org/productCatalog.owl#ShortFactory
<https://evilscript.altervista.org/productCatalog.owl#ShortFactory> rdf:type owl:NamedIndividual ,
                                                                             <http://xmlns.com/foaf/0.1/Organization> ,
                                                                             <https://evilscript.altervista.org/productCatalog.owl#Company> ,
                                                                             <https://evilscript.altervista.org/productCatalog.owl#Factory> ,
                                                                             <https://evilscript.altervista.org/productCatalog.owl#Manufacturer> ;
                                                                    <https://evilscript.altervista.org/productCatalog.owl#produces> <https://evilscript.altervista.org/productCatalog.owl#Beats_cuffie> ;
                                                                    rdfs:comment "A small product factory that only produces Beats!"@en ;
                                                                    rdfs:label "ShortFactory"@en .


###  https://evilscript.altervista.org/productCatalog.owl#USBC_cable
<https://evilscript.altervista.org/productCatalog.owl#USBC_cable> rdf:type owl:NamedIndividual ,
                                                                           <http://purl.org/dc/dcmitype/PhysicalObject> ,
                                                                           <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ,
                                                                           <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ,
                                                                           <http://www.productontology.org/id/Power_cable> ,
                                                                           <http://www.productontology.org/id/Product_(business)> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Accessory> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Cable> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Product> ;
                                                                  <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> <https://evilscript.altervista.org/productCatalog.owl#SamsungAccessories> ;
                                                                  <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#SamsungAccessories> ;
                                                                  <http://www.ontologydesignpatterns.org/cp/owl/list.owl#firstItemOf> <https://evilscript.altervista.org/productCatalog.owl#SamsungAccessories> ;
                                                                  <http://www.ontologydesignpatterns.org/cp/owl/list.owl#lastItemOf> <https://evilscript.altervista.org/productCatalog.owl#SamsungAccessories> ;
                                                                  <https://evilscript.altervista.org/productCatalog.owl#hasBrand> <https://evilscript.altervista.org/productCatalog.owl#Samsung> ;
                                                                  <https://evilscript.altervista.org/productCatalog.owl#inBoxOf> <https://evilscript.altervista.org/productCatalog.owl#IpadAir_2020> ,
                                                                                                                                 <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS10_global> ,
                                                                                                                                 <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS20_5G_global> ;
                                                                  <https://evilscript.altervista.org/productCatalog.owl#isContainedIn> <https://evilscript.altervista.org/productCatalog.owl#SamsungCatalag> ;
                                                                  <https://evilscript.altervista.org/productCatalog.owl#soldBy> <https://evilscript.altervista.org/productCatalog.owl#Samsung> ;
                                                                  <https://evilscript.altervista.org/productCatalog.owl#ProductName> "USB-C Cable"^^xsd:string ;
                                                                  rdfs:comment "The new world standard for USB communication"@en ;
                                                                  rdfs:label "USBC_cable"@en .


###  https://evilscript.altervista.org/productCatalog.owl#ZenBookFlip_S_UX371
<https://evilscript.altervista.org/productCatalog.owl#ZenBookFlip_S_UX371> rdf:type owl:NamedIndividual ,
                                                                                    <http://purl.org/dc/dcmitype/PhysicalObject> ,
                                                                                    <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ,
                                                                                    <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ,
                                                                                    <http://www.productontology.org/id/2-in-1_PC> ,
                                                                                    <http://www.productontology.org/id/Product_(business)> ,
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#Product> ,
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#2in1> ;
                                                                           <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> <https://evilscript.altervista.org/productCatalog.owl#AsusPC> ;
                                                                           <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#AsusPC> ;
                                                                           <http://www.ontologydesignpatterns.org/cp/owl/list.owl#firstItemOf> <https://evilscript.altervista.org/productCatalog.owl#AsusPC> ;
                                                                           <http://www.ontologydesignpatterns.org/cp/owl/list.owl#lastItemOf> <https://evilscript.altervista.org/productCatalog.owl#AsusPC> ;
                                                                           <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasPrice> <https://evilscript.altervista.org/productCatalog.owl#1800Euro> ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#designedBy> <https://evilscript.altervista.org/productCatalog.owl#Asus> ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#hasBrand> <https://evilscript.altervista.org/productCatalog.owl#Asus> ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#isContainedIn> <https://evilscript.altervista.org/productCatalog.owl#AsusCatalog> ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#producedBy> <https://evilscript.altervista.org/productCatalog.owl#Huáshuò> ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#soldBy> <https://evilscript.altervista.org/productCatalog.owl#Asus> ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#CameraMP> "1.2"^^xsd:double ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#ChargingPortType> "USB-C"^^xsd:string ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Color> "Nero jada"^^xsd:string ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#CpuType> "Intel Core i7-1165G7"^^xsd:string ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Depth> "1.19"^^xsd:double ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#EAN> "UX371EA"^^xsd:string ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Height> "21.1"^^xsd:double ,
                                                                                                                                         "30.5"^^xsd:double ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#MemorySize> "1000"^^xsd:nonNegativeInteger ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#OperativeSystem> "Windows 10 Home"^^xsd:string ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Price> "1599.0"^^xsd:double ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#ProductName> "ZenBook Flip S UX371"^^xsd:string ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#RamSize> "16"^^xsd:nonNegativeInteger ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#RamType> "LPDDR4X on-board"^^xsd:string ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#RollOutDate> "2020-08-21T00:00:00"^^xsd:dateTime ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#ScreenSize> "13.3"^^xsd:double ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Weight> "1200.0"^^xsd:double ;
                                                                           <https://evilscript.altervista.org/productCatalog.owl#isTouchScreen> "true"^^xsd:boolean ;
                                                                           rdfs:comment "2-in-1 made by Asus"@en ;
                                                                           rdfs:label "ZenBookFlip_S_UX371"@en .


###  https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256
<https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256> rdf:type owl:NamedIndividual ,
                                                                                             <http://purl.org/dc/dcmitype/PhysicalObject> ,
                                                                                             <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ,
                                                                                             <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ,
                                                                                             <http://www.productontology.org/id/Personal_computer> ,
                                                                                             <http://www.productontology.org/id/Product_(business)> ,
                                                                                             <https://evilscript.altervista.org/productCatalog.owl#Computer> ,
                                                                                             <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                                             <https://evilscript.altervista.org/productCatalog.owl#NotPortableDevice> ,
                                                                                             <https://evilscript.altervista.org/productCatalog.owl#Product> ,
                                                                                             <https://evilscript.altervista.org/productCatalog.owl#ProductHigh> ;
                                                                                    <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> <https://evilscript.altervista.org/productCatalog.owl#ApplePC> ;
                                                                                    <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#ApplePC> ;
                                                                                    <http://www.ontologydesignpatterns.org/cp/owl/list.owl#firstItemOf> <https://evilscript.altervista.org/productCatalog.owl#ApplePC> ;
                                                                                    <http://www.ontologydesignpatterns.org/cp/owl/list.owl#nextItem> <https://evilscript.altervista.org/productCatalog.owl#MacBookAir_M1> ;
                                                                                    <http://www.ontologydesignpatterns.org/cp/owl/list.owl#previousItem> <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ;
                                                                                    <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasPrice> <https://evilscript.altervista.org/productCatalog.owl#1800Euro> ;
                                                                                    <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyFollows> <https://evilscript.altervista.org/productCatalog.owl#MacBookAir_M1> ;
                                                                                    <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyPrecedes> <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ;
                                                                                    <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#follows> <https://evilscript.altervista.org/productCatalog.owl#MacBookAir_M1> ;
                                                                                    <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#precedes> <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ,
                                                                                                                                                         <https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64> ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#designedBy> <https://evilscript.altervista.org/productCatalog.owl#Foxconn> ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#hasBrand> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#isContainedIn> <https://evilscript.altervista.org/productCatalog.owl#AppleCatalog> ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#producedBy> <https://evilscript.altervista.org/productCatalog.owl#Qualcomm> ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#soldBy> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#Color> "Silver"^^xsd:string ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#CpuType> "Intel Core i5 6‑core 10gen 3.1GHz (Turbo Boost 4.5GHz)"^^xsd:string ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#Depth> "203.0"^^xsd:double ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#EAN> "MXWT2LL/A"^^xsd:string ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#Height> "516.0"^^xsd:double ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#MemorySize> "256"^^xsd:nonNegativeInteger ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#OperativeSystem> "macOS Big Sur"^^xsd:string ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#Price> "1349.0"^^xsd:double ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#ProductName> "iMac 27 5K 256GB"^^xsd:string ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#RamSize> "8"^^xsd:nonNegativeInteger ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#RamType> "DDR4"^^xsd:string ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#RollOutDate> "2020-08-04T00:00:00"^^xsd:dateTime ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#ScreenSize> "27.0"^^xsd:double ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#Weight> "8920.0"^^xsd:double ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#Width> "650.0"^^xsd:double ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#isInRange> "High"^^xsd:string ;
                                                                                    <https://evilscript.altervista.org/productCatalog.owl#isTouchScreen> "false"^^xsd:boolean ;
                                                                                    rdfs:comment "All-in-one computer made by Apple"@en ;
                                                                                    rdfs:label "iMac_27_RetinaDisplay_5k_256"@en .


###  https://evilscript.altervista.org/productCatalog.owl#iPhone12_64
<https://evilscript.altervista.org/productCatalog.owl#iPhone12_64> rdf:type owl:NamedIndividual ,
                                                                            <http://purl.org/dc/dcmitype/PhysicalObject> ,
                                                                            <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ,
                                                                            <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ,
                                                                            <http://www.productontology.org/id/Smartphone> ,
                                                                            <http://www.productontology.org/id/Product_(business)> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#Product> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#ProductHigh> ,
                                                                            <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> <https://evilscript.altervista.org/productCatalog.owl#AppleMobile> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#AppleMobile> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/list.owl#nextItem> <https://evilscript.altervista.org/productCatalog.owl#IpadAir_2020> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasPrice> <https://evilscript.altervista.org/productCatalog.owl#800Euro> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyFollows> <https://evilscript.altervista.org/productCatalog.owl#IpadAir_2020> ;
                                                                   <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#follows> <https://evilscript.altervista.org/productCatalog.owl#IpadAir_2020> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#containsInBox> <https://evilscript.altervista.org/productCatalog.owl#Lightning_cable> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#designedBy> <https://evilscript.altervista.org/productCatalog.owl#Foxconn> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#hasBrand> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#isContainedIn> <https://evilscript.altervista.org/productCatalog.owl#AppleCatalog> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#producedBy> <https://evilscript.altervista.org/productCatalog.owl#Qualcomm> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#soldBy> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#successorOf> <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#CameraMP> "12.0"^^xsd:double ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#ChargingPortType> "Lightning"^^xsd:string ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#Color> "Black, White, Red, Green, Blue"^^xsd:string ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#CpuType> "A14 Bionic"^^xsd:string ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#Depth> "7.4"^^xsd:double ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#EAN> "A2172"^^xsd:string ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#Height> "146.7"^^xsd:double ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#MemorySize> 64 ,
                                                                                                                                     "64"^^xsd:nonNegativeInteger ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#OperativeSystem> "iOS 14"^^xsd:string ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#Price> "939.0"^^xsd:double ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#ProductName> "Iphone12 64 GB"^^xsd:string ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#RamSize> "4"^^xsd:nonNegativeInteger ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#RollOutDate> "2020-10-23T00:00:00"^^xsd:dateTime ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#ScreenSize> "6.1"^^xsd:double ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#Weight> "162.0"^^xsd:double ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#Width> "71.5"^^xsd:double ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#isInRange> "High"^^xsd:string ;
                                                                   <https://evilscript.altervista.org/productCatalog.owl#isTouchScreen> "true"^^xsd:boolean ;
                                                                   rdfs:comment "Top 2020 smarphone made by Apple"@en ;
                                                                   rdfs:label "iPhone12_64"@en .


###  https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64
<https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64> rdf:type owl:NamedIndividual ,
                                                                           <http://purl.org/dc/dcmitype/PhysicalObject> ,
                                                                           <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#Item> ,
                                                                           <http://www.ontologydesignpatterns.org/cp/owl/list.owl#ListItem> ,
                                                                           <http://www.productontology.org/id/Smartphone> ,
                                                                           <http://www.productontology.org/id/Product_(business)> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Device> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#PortableDevice> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Product> ,
                                                                           <https://evilscript.altervista.org/productCatalog.owl#Smartphone> ;
                                                                  <http://www.ontologydesignpatterns.org/cp/owl/bag.owl#itemOf> <https://evilscript.altervista.org/productCatalog.owl#AppleMobile> ;
                                                                  <http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#isMemberOf> <https://evilscript.altervista.org/productCatalog.owl#AppleMobile> ;
                                                                  <http://www.ontologydesignpatterns.org/cp/owl/list.owl#firstItemOf> <https://evilscript.altervista.org/productCatalog.owl#AppleMobile> ;
                                                                  <http://www.ontologydesignpatterns.org/cp/owl/list.owl#nextItem> <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ;
                                                                  <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasPrice> <https://evilscript.altervista.org/productCatalog.owl#500Euro> ;
                                                                  <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#directlyFollows> <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ;
                                                                  <http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#follows> <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ,
                                                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#MacBookAir_M1> ,
                                                                                                                                      <https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256> ;
                                                                  <https://evilscript.altervista.org/productCatalog.owl#containsInBox> <https://evilscript.altervista.org/productCatalog.owl#Lightning_cable> ;
                                                                  <https://evilscript.altervista.org/productCatalog.owl#hasBrand> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                  <https://evilscript.altervista.org/productCatalog.owl#isContainedIn> <https://evilscript.altervista.org/productCatalog.owl#AppleCatalog> ;
                                                                  <https://evilscript.altervista.org/productCatalog.owl#predecessorOf> <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ;
                                                                  <https://evilscript.altervista.org/productCatalog.owl#soldBy> <https://evilscript.altervista.org/productCatalog.owl#Apple> ;
                                                                  <https://evilscript.altervista.org/productCatalog.owl#ProductName> "iPhone X 64GB"^^xsd:string ;
                                                                  rdfs:comment "iPhone X, 64GB edition"@en ;
                                                                  rdfs:label "iPhoneX_64"@en .


###  https://evilscript.altervista.org/productCatalog.owl#10Euro
<https://evilscript.altervista.org/productCatalog.owl#10Euro> rdf:type owl:NamedIndividual ,
                                                                       <http://www.ontologydesignpatterns.org/cp/owl/price.owl#Price> ;
                                                              <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasCurrency> <https://evilscript.altervista.org/productCatalog.owl#Euro> ;
                                                              <http://www.ontologydesignpatterns.org/cp/owl/price.owl#isPriceOf> <https://evilscript.altervista.org/productCatalog.owl#Lightning_cable> ;
                                                              <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasValue> "10.0"^^xsd:float ;
                                                              rdfs:comment "10 Euro"@en ;
                                                              rdfs:label "10Euro"@en .


###  https://evilscript.altervista.org/productCatalog.owl#1000Euro
<https://evilscript.altervista.org/productCatalog.owl#1000Euro> rdf:type owl:NamedIndividual ,
                                                                         <http://www.ontologydesignpatterns.org/cp/owl/price.owl#Price> ;
                                                                <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasCurrency> <https://evilscript.altervista.org/productCatalog.owl#Euro> ;
                                                                <http://www.ontologydesignpatterns.org/cp/owl/price.owl#isPriceOf> <https://evilscript.altervista.org/productCatalog.owl#MacBookAir_M1> ;
                                                                <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasValue> "1000.0"^^xsd:float ;
                                                                rdfs:comment "1000 Euro"@en ;
                                                                rdfs:label "1000Euro"@en .


###  https://evilscript.altervista.org/productCatalog.owl#1800Euro
<https://evilscript.altervista.org/productCatalog.owl#1800Euro> rdf:type owl:NamedIndividual ,
                                                                         <http://www.ontologydesignpatterns.org/cp/owl/price.owl#Price> ;
                                                                <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasCurrency> <https://evilscript.altervista.org/productCatalog.owl#Euro> ;
                                                                <http://www.ontologydesignpatterns.org/cp/owl/price.owl#isPriceOf> <https://evilscript.altervista.org/productCatalog.owl#ZenBookFlip_S_UX371> ,
                                                                                                                                   <https://evilscript.altervista.org/productCatalog.owl#iMac_27_RetinaDisplay_5k_256> ;
                                                                <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasValue> "1800.0"^^xsd:float ;
                                                                rdfs:comment "1800 Euro"@en ;
                                                                rdfs:label "1800Euro"@en .


###  https://evilscript.altervista.org/productCatalog.owl#200Euro
<https://evilscript.altervista.org/productCatalog.owl#200Euro> rdf:type owl:NamedIndividual ,
                                                                        <http://www.ontologydesignpatterns.org/cp/owl/price.owl#Price> ;
                                                               <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasCurrency> <https://evilscript.altervista.org/productCatalog.owl#Euro> ;
                                                               <http://www.ontologydesignpatterns.org/cp/owl/price.owl#isPriceOf> <https://evilscript.altervista.org/productCatalog.owl#AirPods_wirelessCharge> ,
                                                                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Beats_cuffie> ;
                                                               <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasValue> "200.0"^^xsd:float ;
                                                               rdfs:comment "200 Euro"@en ;
                                                               rdfs:label "200Euro"@en .


###  https://evilscript.altervista.org/productCatalog.owl#500Euro
<https://evilscript.altervista.org/productCatalog.owl#500Euro> rdf:type owl:NamedIndividual ,
                                                                        <http://www.ontologydesignpatterns.org/cp/owl/price.owl#Price> ;
                                                               <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasCurrency> <https://evilscript.altervista.org/productCatalog.owl#Euro> ;
                                                               <http://www.ontologydesignpatterns.org/cp/owl/price.owl#isPriceOf> <https://evilscript.altervista.org/productCatalog.owl#AppleWatchSeries6_40mm_GPS_Cellular_Nike> ,
                                                                                                                                  <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS10_global> ,
                                                                                                                                  <https://evilscript.altervista.org/productCatalog.owl#iPhoneX_64> ;
                                                               <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasValue> "500.0"^^xsd:float ;
                                                               rdfs:comment "500 Euro"@en ;
                                                               rdfs:label "500Euro"@en .


###  https://evilscript.altervista.org/productCatalog.owl#600Euro
<https://evilscript.altervista.org/productCatalog.owl#600Euro> rdf:type owl:NamedIndividual ,
                                                                        <http://www.ontologydesignpatterns.org/cp/owl/price.owl#Price> ;
                                                               <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasCurrency> <https://evilscript.altervista.org/productCatalog.owl#Euro> ;
                                                               <http://www.ontologydesignpatterns.org/cp/owl/price.owl#isPriceOf> <https://evilscript.altervista.org/productCatalog.owl#IpadAir_2020> ,
                                                                                                                                  <https://evilscript.altervista.org/productCatalog.owl#Iphone11_64> ;
                                                               <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasValue> "600.0"^^xsd:float ;
                                                               rdfs:comment "600 Euro"@en ;
                                                               rdfs:label "600Euro"@en .


###  https://evilscript.altervista.org/productCatalog.owl#800Euro
<https://evilscript.altervista.org/productCatalog.owl#800Euro> rdf:type owl:NamedIndividual ,
                                                                        <http://www.ontologydesignpatterns.org/cp/owl/price.owl#Price> ;
                                                               <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasCurrency> <https://evilscript.altervista.org/productCatalog.owl#Euro> ;
                                                               <http://www.ontologydesignpatterns.org/cp/owl/price.owl#isPriceOf> <https://evilscript.altervista.org/productCatalog.owl#SamsungGalaxyS20_5G_global> ,
                                                                                                                                  <https://evilscript.altervista.org/productCatalog.owl#iPhone12_64> ;
                                                               <http://www.ontologydesignpatterns.org/cp/owl/price.owl#hasValue> "800.0"^^xsd:float ;
                                                               rdfs:comment "800 Euro"@en ;
                                                               rdfs:label "800Euro"@en .


#################################################################
#    Annotations
#################################################################

<http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#hasUnitTest> rdfs:comment "This property can be used to annotate a unit test (e.g. in the form of a SPARQL query) to be launched to evaluate an ontology against a requirement-based task." .


<http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#isCloneOf> rdfs:comment "This annotation property is used for referring a cloned ontology entity to its cloning source." .


###  Generated by the OWL API (version 4.5.9.2019-02-01T07:24:44Z) https://github.com/owlcs/owlapi

```