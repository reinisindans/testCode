






 Database schema description
============================


Version 1.2 



 Content
--------


### [VMDData](#-vmddata--dataset)

####  [Biotops](#-biotops--feature-class)

####  [Biotopu koncentrācijas vieta](#-biotopu-koncentrācijas-vieta--feature-class)

####  [Ugunsgrēka teritorija](#-ugunsgrēka-teritorija--feature-class)

####  [Ugunsgrēka vieta](#-ugunsgrēka-vieta--feature-class)

####  [VMD dzīvnieku uzskaite](#-vmd-dzīvnieku-uzskaite--feature-class)

####  [Vides aizsardzības klasifikators](#-vides-aizsardzības-klasifikators--feature-class)

####  [Vides aizsardzības pazīmes](#-vides-aizsardzības-pazīmes--feature-class)

### [VMDDataView](#-vmddataview--dataset)

####  [Ugunsgrēka teritorijas skatījums](#-ugunsgrēka-teritorijas-skatījums--feature-class)

####  [VMD Ugunsgrēka vietas skatījums](#-vmd-ugunsgrēka-vietas-skatījums--feature-class)

###  [Common element and object classes](#-Common-element-and-object-classes-)

####  [Biotopa apsaimniekošana](#-biotopa-apsaimniekošana--object-class)

####  [Biotopa apsaimniekošana – izcērtama suga](#-biotopa-apsaimniekošana--izcērtama-suga--object-class)

####  [Biotopa apsaimniekošana – sugas izcirtes apjomi](#-biotopa-apsaimniekošana--sugas-izcirtes-apjomi--object-class)

####  [Biotopa atslēgas elementi](#-biotopa-atslēgas-elementi--object-class)

####  [Biotopa atslēgas elementu sugas](#-biotopa-atslēgas-elementu-sugas--object-class)

####  [Biotopa audzes raksturojumi](#-biotopa-audzes-raksturojumi--object-class)

####  [Biotopa indikatoru sugas](#-biotopa-indikatoru-sugas--object-class)

####  [Biotopa negatīvi traucējumi](#-biotopa-negatīvi-traucējumi--object-class)

####  [Biotopa īpašās iezīmes](#-biotopa-īpašās-iezīmes--object-class)

####  [Ugunsgrēki](#-ugunsgrēki--object-class)

####  [Ugunsgrēku platības uzskaite](#-ugunsgrēku-platības-uzskaite--object-class)

####  [Vides aizsardzības ierobežojumi](#-vides-aizsardzības-ierobežojumi--object-class)

####  [RC\_BIO\_KONC\_LINK](#-rc_bio_konc_link--relationship-class)

###  [Coded value domains](#-Coded-value-domains-)

####  [Augšanas apstākļu tipi](#-augšanas-apstākļu-tipi--coded-value-domain)

####  [Bināra izvēle](#-bināra-izvēle--coded-value-domain)

####  [Bioelementu veida apjomi](#-bioelementu-veida-apjomi--coded-value-domain)

####  [Biokoncentrācijas vietu infrastruktūras tips](#-biokoncentrācijas-vietu-infrastruktūras-tips--coded-value-domain)

####  [Biotopa atslēgas elementu veidi (Ar apjomu un sugu)](#-biotopa-atslēgas-elementu-veidi-ar-apjomu-un-sugu--coded-value-domain)

####  [Biotopa atslēgas elementu veidi (Ar apjomu)](#-biotopa-atslēgas-elementu-veidi-ar-apjomu--coded-value-domain)

####  [Biotopa atslēgas elementu veidi (Bez apjoma)](#-biotopa-atslēgas-elementu-veidi-bez-apjoma--coded-value-domain)

####  [Biotopa indikatoru sugu sastopamība](#-biotopa-indikatoru-sugu-sastopamība--coded-value-domain)

####  [Biotopa indikatoru sugu veidi](#-biotopa-indikatoru-sugu-veidi--coded-value-domain)

####  [Biotopa informācijas avoti](#-biotopa-informācijas-avoti--coded-value-domain)

####  [Biotopa nosaukumi](#-biotopa-nosaukumi--coded-value-domain)

####  [Biotopa traucējumu intensitāte](#-biotopa-traucējumu-intensitāte--coded-value-domain)

####  [Biotopa traucējumu veidi](#-biotopa-traucējumu-veidi--coded-value-domain)

####  [Biotopa īpašo iezīmju veidi](#-biotopa-īpašo-iezīmju-veidi--coded-value-domain)

####  [Dzīvnieku sugas](#-dzīvnieku-sugas--coded-value-domain)

####  [ES Biotopa tips](#-es-biotopa-tips--coded-value-domain)

####  [Izciršanas veidi](#-izciršanas-veidi--coded-value-domain)

####  [Izcērtamo apjomu veidi](#-izcērtamo-apjomu-veidi--coded-value-domain)

####  [Koku sugas](#-koku-sugas--coded-value-domain)

####  [Koku sugas](#-koku-sugas--coded-value-domain)

####  [Koku sugu klasifikators](#-koku-sugu-klasifikators--coded-value-domain)

####  [Krūmu sugu klasifikators](#-krūmu-sugu-klasifikators--coded-value-domain)

####  [LVM meža iecirkņi](#-lvm-meža-iecirkņi--coded-value-domain)

####  [LVM mežsaimniecības](#-lvm-mežsaimniecības--coded-value-domain)

####  [Meža piederība](#-meža-piederība--coded-value-domain)

####  [Putnu sugas](#-putnu-sugas--coded-value-domain)

####  [Putnu sugas](#-putnu-sugas--coded-value-domain)

####  [Pēdu skaita novērtējuma tipi](#-pēdu-skaita-novērtējuma-tipi--coded-value-domain)

####  [TemplateCodedValueDomain](#-templatecodedvaluedomain--coded-value-domain)

####  [Ugunsgrēka atklāšanas veids](#-ugunsgrēka-atklāšanas-veids--coded-value-domain)

####  [Ugunsgrēka cēloņi](#-ugunsgrēka-cēloņi--coded-value-domain)

####  [Ugunsgrēku platību uzskaites tips](#-ugunsgrēku-platību-uzskaites-tips--coded-value-domain)

####  [Vides aizsardzības ierobežojumu veidi](#-vides-aizsardzības-ierobežojumu-veidi--coded-value-domain)

####  [Vērtējums](#-vērtējums--coded-value-domain)

###  [Range domains](#-Range-domains-)

####  [Procenti (0-100%)](#-procenti-0-100--range-domain)

 -VMDData- [Dataset]
--------------------




|  |  |
| --- | --- |
| Name in DB | VMDData |


  

###  -Biotops- [Feature class]




|  |  |
| --- | --- |
| Name in DB | VMDBIOTOPI |
| Object type | Feature class |
| Geometry | Polygon |
| M coordinates | No |
| Z coordinates | No |

  
##### Object subtypes




| Value | Description |
| --- | --- |
| 3 | starpaudze meža biotopu koncentrācijas vietā |
| 1 | Potenciālais meža biotops |
| 2 | Dabīgais meža biotops |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Biotopa atslēgas elementi (VMDBIOATSLEGASELEMENTI)](#-biotopa-atslēgas-elementi--object-class)  | [Biotops](#-biotops--feature-class).Unikālais identifikators  -> [Biotopa atslēgas elementi](#-biotopa-atslēgas-elementi--object-class).Sasaiste ar BIOTOPI | 1:N |
|  [Biotopu koncentrācijas vieta (VMDBIOKONCENTRACIJA)](#-biotopu-koncentrācijas-vieta--feature-class) | [Biotops](#-biotops--feature-class).Unikālais identifikators -> [RC\_BIO\_KONC\_LINK](#-rc_bio_konc_link--relationship-class).Biotopa identifikators (sasaistei)[Biotopu koncentrācijas vieta](#-biotopu-koncentrācijas-vieta--feature-class).Unikālais identifikators  -> [Biotops](#-biotops--feature-class).Koncentrācijas vietas identifikators (sasaistei) | N:N |
|  [Biotopa īpašās iezīmes (VMDBIOIEZIMES)](#-biotopa-īpašās-iezīmes--object-class)  | [Biotops](#-biotops--feature-class).Unikālais identifikators  -> [Biotopa īpašās iezīmes](#-biotopa-īpašās-iezīmes--object-class).Sasaiste ar BIOTOPI | 1:N |
|  [Biotopa apsaimniekošana (VMDBIOAPSAIMNIEKOSANA)](#-biotopa-apsaimniekošana--object-class)  | [Biotops](#-biotops--feature-class).Unikālais identifikators  -> [Biotopa apsaimniekošana](#-biotopa-apsaimniekošana--object-class).Sasaiste ar BIOTOPI | 1:N |
|  [Biotopa negatīvi traucējumi (VMDBIONEGATIVITRAUC)](#-biotopa-negatīvi-traucējumi--object-class)  | [Biotops](#-biotops--feature-class).Unikālais identifikators  -> [Biotopa negatīvi traucējumi](#-biotopa-negatīvi-traucējumi--object-class).Sasaiste ar BIOTOPI | 1:N |
|  [Biotopa indikatoru sugas (VMDBIOINDIKATORUSUGAS)](#-biotopa-indikatoru-sugas--object-class)  | [Biotops](#-biotops--feature-class).Unikālais identifikators  -> [Biotopa indikatoru sugas](#-biotopa-indikatoru-sugas--object-class).Sasaiste ar BIOTOPI | 1:N |
|  [Biotopa audzes raksturojumi (VMDBIOAUDZESRAKSTUROJUM)](#-biotopa-audzes-raksturojumi--object-class)  | [Biotops](#-biotops--feature-class).Unikālais identifikators  -> [Biotopa audzes raksturojumi](#-biotopa-audzes-raksturojumi--object-class).Sasaiste ar BIOTOPI | 1:N |
|  [Vides aizsardzības pazīmes (VMDVAPAZIMES)](#-vides-aizsardzības-pazīmes--feature-class) | [Vides aizsardzības pazīmes](#-vides-aizsardzības-pazīmes--feature-class).Unikālais identifikators  -> [Biotops](#-biotops--feature-class).Sasaiste ar vides aizsardzības klasifikatora pazīmēm | 1:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Shape | Geometry | Shape |  |  | Yes |
| Unikālais identifikators | Long integer | Biotops\_ID | 10 |  |  |
| Apakštipa lauks | Long integer | Biotops\_ST | 10 | 1 |  |
| Biotopa Nr. | Text | Numurs |  |  |  |
| Platība (situācijai dabā) | Float | Platiba | 6 |  |  |
| Audzes sastāva formula (situācijai dabā) | Text | Formula |  |  |  |
| Augšanas apstākļu tips | [VMD\_190\_AAT](#-augšanas-apstākļu-tipi--coded-value-domain) -1: Nav zināms; | AAT | 2 |  |  |
| Sasaiste ar vides aizsardzības klasifikatora pazīmēm | Long integer | VA\_Paz\_ID | 10 |  |  |
| Informācijas avots | [VMD\_010\_BioInfoAvoti](#-biotopa-informācijas-avoti--coded-value-domain) -1: Nav zināms; 1: Meža valsts reģistrs; 2: Topogrāfiskā karte; 3: Vietējais mežsargs/iedzīvotājs; 4: Citas kartes; 5: Citi pētījumi; 6: Atrasts nejauši lauku darbu gaitā; | InfoAv | 3 |  |  |
| Biotopa nosaukums I | [VMD\_011\_Bionosaukumi](#-biotopa-nosaukumi--coded-value-domain) -1: Nav zināms; A1: Skujkoku mežs; A2: Mistrots skujkoku-lapukoku mežs; B1: Platlapju mežs; B2: Apšu mežs; B3: Cits lapukoku mežs; C1: Slapjš melnalkšņu mežs; C2: Egļu un mistrots egļu slapjais mežs; C3: Priežu un bērzu slapjais mežs;... | Nosaukums1 |  |  |  |
| Biotopa nosaukums II | [VMD\_011\_Bionosaukumi](#-biotopa-nosaukumi--coded-value-domain) -1: Nav zināms; A1: Skujkoku mežs; A2: Mistrots skujkoku-lapukoku mežs; B1: Platlapju mežs; B2: Apšu mežs; B3: Cits lapukoku mežs; C1: Slapjš melnalkšņu mežs; C2: Egļu un mistrots egļu slapjais mežs; C3: Priežu un bērzu slapjais mežs;... | Nosaukums2 |  |  |  |
| Bioloģiskās daudzveidības apraksts | Text | Daudzveidiba |  |  |  |
| Piezīmes | Text | Piezimes |  |  |  |
| Apsekošanas datums | Date | Datums |  |  |  |
| Persona, kas veica apsekošanu | Text | Apsekoja |  |  |  |
| Audzes status | [VMD\_013\_StatussVeids](#-putnu-sugas--coded-value-domain) -1: Nav zināms; P: Paplašinājums (P); P30-70: Paplašinājums (P30-70); B: Buferjosla (B); BP: Buferjosla (BP); B30-70: Buferjosla (B30-70); I: Ieslēgums (I); | SA\_Statuss |  |  |  |
| Audzes suga | Short integer | SA\_Suga | 3 |  |  |
| Audzes ierobežojumu intensitāte | Short integer | SA\_Intensitate | 3 |  |  |
| Piezīmes, suga | Text | SA\_Suga\_Piezimes |  |  |  |
| DMB raksturīgo ekoloģisko rādītāju sasniegšanas laiks | Short integer | SA\_Sasniegsana | 3 |  |  |
| Novērtējums par audzes piemērotību paplašinājumiem | [VMD\_080\_Vertejums](#-vērtējums--coded-value-domain) -1: Nav zināms; 1: Zems; 2: Vidējs; 3: Augsts; | SA\_Piemerotiba | 3 |  |  |
| Apsaimniekošanas apraksts | Text | SA\_Apsaimn |  |  |  |

  
###  -Biotopu koncentrācijas vieta- [Feature class]




|  |  |
| --- | --- |
| Name in DB | VMDBIOKONCENTRACIJA |
| Object type | Feature class |
| Geometry | Polygon |
| M coordinates | No |
| Z coordinates | No |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Biotops (VMDBIOTOPI)](#-biotops--feature-class)  | [Biotops](#-biotops--feature-class).Unikālais identifikators -> [RC\_BIO\_KONC\_LINK](#-rc_bio_konc_link--relationship-class).Biotopa identifikators (sasaistei)[Biotopu koncentrācijas vieta](#-biotopu-koncentrācijas-vieta--feature-class).Unikālais identifikators  -> [Biotops](#-biotops--feature-class).Koncentrācijas vietas identifikators (sasaistei) | N:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Shape | Geometry | Shape |  |  | Yes |
| Unikālais identifikators | Long integer | BioKoncentracija\_ID | 10 |  |  |
| Koncentrācijas Nr. | Text | Numurs |  |  |  |
| Infrastruktūras tips | [VMD\_081\_BioKoncentracija\_Infrastruktura](#-biokoncentrācijas-vietu-infrastruktūras-tips--coded-value-domain) 1: 1. Priežu meži ar dažādvecuma kokiem; 2: 2. Lapu koku pionierfāzes meži; 3: 3. Meži ar dažādu pašizrobošanās dinamiku; 3A: 3a. Slapjie egļu meži un pārējie egļu meži; 3B: 3b. Slapjie melnalkšņu un platlapju meži; 3C: 3c. Platlapju meži; 3AB: 3ab. Slapjie egļu meži un pārējie egļu meži; Slapjie melnalkšņu un platlapju meži; 3AC: 3ac. Slapjie egļu meži un pārējie egļu meži; Platlapju meži; 3BC: 3b. Slapjie melnalkšņu un platlapju meži; Platlapju meži;... | Infrastruktura |  |  |  |
| Atrodas nozīmīgajā apvidū? | [VMD\_000\_Boolean](#-bināra-izvēle--coded-value-domain) -1: Nav zināms; 1: Jā; 2: Nē; 0: Nav ievadīts; | Nozimigs\_Apvidus | 1 |  |  |
| Nav nosusināts | Long integer | NT\_Nesusinats | 3 |  |  |
| Nosusināts, bet sistēma nedarbojas | Long integer | NT\_SusNeDarb | 3 |  |  |
| Nosusināšana darbojas | Long integer | NT\_SusDarb | 3 |  |  |
| Biotopu koncentrācijas vietas vērtējums? | [VMD\_080\_Vertejums](#-vērtējums--coded-value-domain) -1: Nav zināms; 1: Zems; 2: Vidējs; 3: Augsts; | Konc\_Vert | 1 |  |  |
| Nosusināšanas ilglaicīgā negatīvā ietekme uz bioloģiskajām vērtībām | [VMD\_080\_Vertejums](#-vērtējums--coded-value-domain) -1: Nav zināms; 1: Zems; 2: Vidējs; 3: Augsts; | Sus\_Ietekme | 1 |  |  |
| Ietekme, slēdzot nosusināšanas sistēmu | [VMD\_080\_Vertejums](#-vērtējums--coded-value-domain) -1: Nav zināms; 1: Zems; 2: Vidējs; 3: Augsts; | SusSledz\_Ietekme | 1 |  |  |
| Ieguvums | Text | Ieguvums |  |  |  |
| Piezīmes | Text | Piezimes |  |  |  |
| Apsekoja | Text | Apsekoja |  |  |  |
| Datums | Date | Datums |  |  |  |

  
###  -Ugunsgrēka teritorija- [Feature class]




|  |  |
| --- | --- |
| Name in DB | VMDUGUNSGREKPOLY |
| Object type | Feature class |
| Geometry | Polygon |
| M coordinates | No |
| Z coordinates | No |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Ugunsgrēki (VMDUGUNSGREKI)](#-ugunsgrēki--object-class) | [Ugunsgrēki](#-ugunsgrēki--object-class).Unikālais identifikators  -> [Ugunsgrēka teritorija](#-ugunsgrēka-teritorija--feature-class).Sasaiste ar UGUNSGREKI | 1:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Shape | Geometry | Shape |  |  | Yes |
| Sasaiste ar UGUNSGREKI | Long integer | Ug\_ID | 10 |  |  |
| Mežsaimniecība  | [LVM\_00202\_LVMForestry](#-lvm-mežsaimniecības--coded-value-domain) !: Vērtības no slāņa LVMForestry; ?: ???; | LVMForestryCode |  |  |  |
| Kv.apg. - kvartāls | Text | BlockKey |  |  |  |
| Nogabala numurs | Short integer | CompartmentNumber | 2 |  |  |
| Iecirknis | [LVM\_00201\_LVMDistricts](#-lvm-meža-iecirkņi--coded-value-domain) kodi: Vērtības no slāņa LVMDistrict; ???: ???; | LVM\_District\_Code |  |  |  |
| Sugu sastāvs (M) | Text | SugasSastavs |  |  |  |
| Meža tipa apzīmējums (M) | Text | AAT |  |  |  |
| 1.sugas vecums (M) | Long integer | A10 | 10 |  |  |
| 1.suga (M) | [LVM\_MEDUS\_00003\_TreeSpecies](#-koku-sugu-klasifikators--coded-value-domain) 1: 01 - Priede; 3: 03 - Egle; 4: 04 - Bērzs; 6: 06 - Melnalksnis; 8: 08 - Apse; 9: 09 - Baltalksnis; 10: 10 - Ozols; 11: 11 - Osis; 12: 12 - Liepa;... | S10 | 10 |  |  |

  
###  -Ugunsgrēka vieta- [Feature class]




|  |  |
| --- | --- |
| Name in DB | VMDUGUNSGREKPOINT |
| Object type | Feature class |
| Geometry | Point |
| M coordinates | No |
| Z coordinates | No |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Ugunsgrēki (VMDUGUNSGREKI)](#-ugunsgrēki--object-class) | [Ugunsgrēki](#-ugunsgrēki--object-class).Unikālais identifikators  -> [Ugunsgrēka vieta](#-ugunsgrēka-vieta--feature-class).Sasaiste ar UGUNSGREKI | 1:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Shape | Geometry | Shape |  |  | Yes |
| Simbola leņķis | Float | Angval | 5 |  |  |
| Sasaiste ar UGUNSGREKI | Long integer | Ug\_ID | 10 |  |  |
| Mežsaimniecība  | [LVM\_00202\_LVMForestry](#-lvm-mežsaimniecības--coded-value-domain) !: Vērtības no slāņa LVMForestry; ?: ???; | LVMForestryCode |  |  |  |
| Kv.apg. - kvartāls | Text | BlockKey |  |  |  |
| Nogabala numurs | Short integer | CompartmentNumber | 2 |  |  |
| Iecirknis | [LVM\_00201\_LVMDistricts](#-lvm-meža-iecirkņi--coded-value-domain) kodi: Vērtības no slāņa LVMDistrict; ???: ???; | LVM\_District\_Code |  |  |  |
| Meža tipa apzīmējums (M) | Text | AAT |  |  |  |
| Sugu sastāvs (M) | Text | SugasSastavs |  |  |  |
| 1.sugas vecums (M) | Long integer | A10 | 10 |  |  |
| 1.suga (M) | [LVM\_MEDUS\_00003\_TreeSpecies](#-koku-sugu-klasifikators--coded-value-domain) 1: 01 - Priede; 3: 03 - Egle; 4: 04 - Bērzs; 6: 06 - Melnalksnis; 8: 08 - Apse; 9: 09 - Baltalksnis; 10: 10 - Ozols; 11: 11 - Osis; 12: 12 - Liepa;... | S10 | 10 |  |  |

  
###  -VMD dzīvnieku uzskaite- [Feature class]




|  |  |
| --- | --- |
| Name in DB | VMDAnimalCount |
| Object type | Feature class |
| Geometry | Polygon |
| M coordinates | No |
| Z coordinates | No |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Shape | Geometry | Shape |  |  | Yes |
| Uzskaites vienība | Text | Uzsk\_vien |  |  |  |
| Nosaukums | Text | Nosaukums |  |  |  |
| Dzīvnieku suga | [VMD\_100\_DzivnSugas](#-dzīvnieku-sugas--coded-value-domain) 1: Alnis; 2: Staltbriedis; 3: Meža cūka; 4: Stirna; 5: Bebrs; 6: Mednis; 7: Rubenis; 8: Lūsis; 9: Vilks;... | Suga | 2 |  |  |
| Uzskaites vērtība | Float | UzskVertiba | 5 |  |  |

  
###  -Vides aizsardzības klasifikators- [Feature class]




|  |  |
| --- | --- |
| Name in DB | VMDVAKLASIFIKATORS |
| Object type | Feature class |
| Geometry | Polygon |
| M coordinates | No |
| Z coordinates | No |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Vides aizsardzības ierobežojumi (VMDVAIEROBEZOJUMI)](#-vides-aizsardzības-ierobežojumi--object-class)  | [Vides aizsardzības klasifikators](#-vides-aizsardzības-klasifikators--feature-class).Unikālais identifikators  -> [Vides aizsardzības ierobežojumi](#-vides-aizsardzības-ierobežojumi--object-class).Sasaiste ar VA klasifikatoru | 1:N |
|  [Vides aizsardzības pazīmes (VMDVAPAZIMES)](#-vides-aizsardzības-pazīmes--feature-class)  | [Vides aizsardzības klasifikators](#-vides-aizsardzības-klasifikators--feature-class).Unikālais identifikators  -> [Vides aizsardzības pazīmes](#-vides-aizsardzības-pazīmes--feature-class).Sasaiste ar VA\_KLASIFIKATORS | 1:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Shape | Geometry | Shape |  |  | Yes |
| Unikālais identifikators | Long integer | VAK\_ID | 10 |  |  |
| Hierarhijas sasaiste | Long integer | Parent\_VAK\_ID | 10 |  |  |
| Kods | Text | Kods |  |  |  |
| Nosaukums | Text | Nosaukums |  |  |  |
| Vai atļauts reģistrēt unikālās aizsardzības pazīmes? | [VMD\_000\_Boolean](#-bināra-izvēle--coded-value-domain) -1: Nav zināms; 1: Jā; 2: Nē; 0: Nav ievadīts; | Unikalas\_Pazimes | 2 |  |  |
| Izveidošanas datums | Date | Izveidots |  |  |  |
| Likvidēšanas datums | Date | Likvidets |  |  |  |

  
###  -Vides aizsardzības pazīmes- [Feature class]




|  |  |
| --- | --- |
| Name in DB | VMDVAPAZIMES |
| Object type | Feature class |
| Geometry | Polygon |
| M coordinates | No |
| Z coordinates | No |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Vides aizsardzības klasifikators (VMDVAKLASIFIKATORS)](#-vides-aizsardzības-klasifikators--feature-class) | [Vides aizsardzības klasifikators](#-vides-aizsardzības-klasifikators--feature-class).Unikālais identifikators  -> [Vides aizsardzības pazīmes](#-vides-aizsardzības-pazīmes--feature-class).Sasaiste ar VA\_KLASIFIKATORS | 1:N |
|  [Biotops (VMDBIOTOPI)](#-biotops--feature-class)  | [Vides aizsardzības pazīmes](#-vides-aizsardzības-pazīmes--feature-class).Unikālais identifikators  -> [Biotops](#-biotops--feature-class).Sasaiste ar vides aizsardzības klasifikatora pazīmēm | 1:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Shape | Geometry | Shape |  |  | Yes |
| Unikālais identifikators | Long integer | VA\_Paz\_ID | 10 |  |  |
| Sasaiste ar VA\_KLASIFIKATORS | Long integer | VAK\_ID | 10 |  |  |
| Numurs | Text | Numurs |  |  |  |
| Izveidošanas datums | Date | Izveidots |  |  |  |
| Likvidēšanas datums | Date | Likvidets |  |  |  |

  
 -VMDDataView- [Dataset]
------------------------




|  |  |
| --- | --- |
| Name in DB | VMDDataView |


  

###  -Ugunsgrēka teritorijas skatījums- [Feature class]




|  |  |
| --- | --- |
| Name in DB | VMDUGUNSGREKPOLYVIEW |
| Object type | Feature class |
| Geometry | Polygon |
| M coordinates | No |
| Z coordinates | No |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Shape | Geometry | Shape |  |  | Yes |
| Uzsāk dzēšanu | Date | Usak |  |  |  |
| Trauksmes laiks | Date | Trauksme |  |  |  |
| Ierobežošanas laiks | Date | Ierobezo |  |  |  |
| Likvidēšanas laiks | Date | Likvide |  |  |  |
| Ugunsgrēka atklāšanas veids | [VMD\_093\_UgunsAtklType](#-ugunsgrēka-atklāšanas-veids--coded-value-domain) 1: No torņa; 2: Ziņo trešā persona; 3: Ziņo VUGD; | UATKL\_TYPE | 3 |  |  |
| Ugunscēloņi | [VMD\_090\_Ugunsceloni](#-ugunsgrēka-cēloņi--coded-value-domain) -1: Nav zināms; | Ucel\_Type | 3 |  |  |
| Sasaiste ar UGUNSGREKI | Long integer | Ug\_ID | 10 |  |  |
| LVM meža zemju platība | Double | LVM\_MEZ\_PLATIBA | 38 |  |  |
| LVM Jaunaudžu platība | Double | LVM\_JAUN\_PLATIBA | 38 |  |  |
| LVM Citu meža zemju platība | Double | LVM\_CITMEZ\_PLATIBA | 38 |  |  |
| LVM Citu nemeža zemju platība | Double | LVM\_CITNEMEZ\_PLATIBA | 38 |  |  |
| Privātio meža zemju platība | Double | PRV\_MEZ\_PLATIBA | 38 |  |  |
| Privātio Jaunaudžu platība | Double | PRV\_JAUN\_PLATIBA | 38 |  |  |
| Privātio citu meža zemju platība | Double | PRV\_CITMEZ\_PLATIBA | 38 |  |  |
| Privātio Citu nemeža zemju platība | Double | PRV\_CITNEMEZ\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) meža zemju platība | Double | VLS\_MEZ\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) Mežu platība | Double | VLS\_JAUN\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) citu meža zemju platība | Double | VLS\_CITMEZ\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) Citu nemeža zemju platība | Double | VLS\_CITNEMEZ\_PLATIBA | 38 |  |  |
| Pašvaldību meža zemju platība | Double | PSV\_MEZ\_PLATIBA | 38 |  |  |
| Pašvaldību Mežu platība | Double | PSV\_JAUN\_PLATIBA | 38 |  |  |
| Pašvaldību citu meža zemju platība | Double | PSV\_CITMEZ\_PLATIBA | 38 |  |  |
| Pašvaldību nemeža zemju platība | Double | PSV\_CITNEMEZ\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) summārā platība | Double | VLS\_SUM\_PLATIBA | 38 |  |  |
| Pašvaldību summārā platība | Double | PSV\_SUM\_PLATIBA | 38 |  |  |
| Privātio summārā platība | Double | PRV\_SUM\_PLATIBA | 38 |  |  |
| LVM summārā platība | Double | LVM\_SUM\_PLATIBA | 38 |  |  |
| Mežsaimniecība  | [LVM\_00202\_LVMForestry](#-lvm-mežsaimniecības--coded-value-domain) !: Vērtības no slāņa LVMForestry; ?: ???; | LVMForestryCode |  |  |  |
| Kv.apg. - kvartāls | Text | BlockKey |  |  |  |
| Nogabala numurs | Short integer | CompartmentNumber | 2 |  |  |
| Iecirknis | [LVM\_00201\_LVMDistricts](#-lvm-meža-iecirkņi--coded-value-domain) kodi: Vērtības no slāņa LVMDistrict; ???: ???; | LVM\_District\_Code |  |  |  |
| Meža tipa apzīmējums (M) | Text | AAT |  |  |  |
| Sugu sastāvs (M) | Text | SugasSastavs |  |  |  |
| 1.sugas vecums (M) | Long integer | A10 | 10 |  |  |
| 1.suga (M) | [LVM\_MEDUS\_00003\_TreeSpecies](#-koku-sugu-klasifikators--coded-value-domain) 1: 01 - Priede; 3: 03 - Egle; 4: 04 - Bērzs; 6: 06 - Melnalksnis; 8: 08 - Apse; 9: 09 - Baltalksnis; 10: 10 - Ozols; 11: 11 - Osis; 12: 12 - Liepa;... | S10 | 10 |  |  |

  
###  -VMD Ugunsgrēka vietas skatījums- [Feature class]




|  |  |
| --- | --- |
| Name in DB | VMDUGUNSGREKPOINTVIEW |
| Object type | Feature class |
| Geometry | Point |
| M coordinates | No |
| Z coordinates | No |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Shape | Geometry | Shape |  |  | Yes |
| Sasaiste ar UGUNSGREKI | Long integer | Ug\_ID | 10 |  |  |
| Ierobežošanas laiks | Date | Ierobezo |  |  |  |
| Likvidēšanas laiks | Date | Likvide |  |  |  |
| Trauksmes laiks | Date | Trauksme |  |  |  |
| Ugunsgrēka atklāšanas veids | [VMD\_093\_UgunsAtklType](#-ugunsgrēka-atklāšanas-veids--coded-value-domain) 1: No torņa; 2: Ziņo trešā persona; 3: Ziņo VUGD; | UATKL\_TYPE | 3 |  |  |
| Ugunscēloņi | [VMD\_090\_Ugunsceloni](#-ugunsgrēka-cēloņi--coded-value-domain) -1: Nav zināms; | Ucel\_Type | 3 |  |  |
| Uzsāk dzēšanu | Date | Usak |  |  |  |
| LVM meža zemju platība | Double | LVM\_MEZ\_PLATIBA | 38 |  |  |
| LVM Jaunaudžu platība | Double | LVM\_JAUN\_PLATIBA | 38 |  |  |
| LVM Citu meža zemju platība | Double | LVM\_CITMEZ\_PLATIBA | 38 |  |  |
| LVM Citu nemeža zemju platība | Double | LVM\_CITNEMEZ\_PLATIBA | 38 |  |  |
| LVM summārā platība | Double | LVM\_SUM\_PLATIBA | 38 |  |  |
| Privātio meža zemju platība | Double | PRV\_MEZ\_PLATIBA | 38 |  |  |
| Privātio Jaunaudžu platība | Double | PRV\_JAUN\_PLATIBA | 38 |  |  |
| Privātio citu meža zemju platība | Double | PRV\_CITMEZ\_PLATIBA | 38 |  |  |
| Privātio Citu nemeža zemju platība | Double | PRV\_CITNEMEZ\_PLATIBA | 38 |  |  |
| Privātio summārā platība | Double | PRV\_SUM\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) meža zemju platība | Double | VLS\_MEZ\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) Mežu platība | Double | VLS\_JAUN\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) citu meža zemju platība | Double | VLS\_CITMEZ\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) Citu nemeža zemju platība | Double | VLS\_CITNEMEZ\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) summārā platība | Double | VLS\_SUM\_PLATIBA | 38 |  |  |
| Pašvaldību meža zemju platība | Double | PSV\_MEZ\_PLATIBA | 38 |  |  |
| Pašvaldību Mežu platība | Double | PSV\_JAUN\_PLATIBA | 38 |  |  |
| Pašvaldību citu meža zemju platība | Double | PSV\_CITMEZ\_PLATIBA | 38 |  |  |
| Pašvaldību nemeža zemju platība | Double | PSV\_CITNEMEZ\_PLATIBA | 38 |  |  |
| Pašvaldību summārā platība | Double | PSV\_SUM\_PLATIBA | 38 |  |  |
| Mežsaimniecība  | [LVM\_00202\_LVMForestry](#-lvm-mežsaimniecības--coded-value-domain) !: Vērtības no slāņa LVMForestry; ?: ???; | LVMForestryCode |  |  |  |
| Kv.apg. - kvartāls | Text | BlockKey |  |  |  |
| Nogabala numurs | Short integer | CompartmentNumber | 2 |  |  |
| Iecirknis | [LVM\_00201\_LVMDistricts](#-lvm-meža-iecirkņi--coded-value-domain) kodi: Vērtības no slāņa LVMDistrict; ???: ???; | LVM\_District\_Code |  |  |  |
| Meža tipa apzīmējums (M) | Text | AAT |  |  |  |
| Sugu sastāvs (M) | Text | SugasSastavs |  |  |  |
| 1.sugas vecums (M) | Long integer | A10 | 10 |  |  |
| 1.suga (M) | [LVM\_MEDUS\_00003\_TreeSpecies](#-koku-sugu-klasifikators--coded-value-domain) 1: 01 - Priede; 3: 03 - Egle; 4: 04 - Bērzs; 6: 06 - Melnalksnis; 8: 08 - Apse; 9: 09 - Baltalksnis; 10: 10 - Ozols; 11: 11 - Osis; 12: 12 - Liepa;... | S10 | 10 |  |  |

  
 -Common element and object classes-
------------------------------------

###  -Biotopa apsaimniekošana- [Object class]




|  |  |
| --- | --- |
| Name in DB | VMDBIOAPSAIMNIEKOSANA |
| Object type | Object class |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Biotops (VMDBIOTOPI)](#-biotops--feature-class) | [Biotops](#-biotops--feature-class).Unikālais identifikators  -> [Biotopa apsaimniekošana](#-biotopa-apsaimniekošana--object-class).Sasaiste ar BIOTOPI | 1:N |
|  [Biotopa apsaimniekošana – izcērtama suga (VMDBIOIZCERTAMASUGA)](#-biotopa-apsaimniekošana--izcērtama-suga--object-class)  | [Biotopa apsaimniekošana](#-biotopa-apsaimniekošana--object-class).Unikālais identifikators  -> [Biotopa apsaimniekošana – izcērtama suga](#-biotopa-apsaimniekošana--izcērtama-suga--object-class).Sasaiste ar BIOAPSAIMNIEKOSANA | 1:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Unikālais identifikators | Long integer | BioApsaimniekosana\_ID | 10 |  |  |
| Sasaiste ar BIOTOPI | Long integer | Bio\_ID | 10 |  |  |
| Bez saimnieciskās darbības? | [VMD\_000\_Boolean](#-bināra-izvēle--coded-value-domain) -1: Nav zināms; 1: Jā; 2: Nē; 0: Nav ievadīts; | Bez\_Darbibas | 1 |  |  |
| Jāsaglabā buferjosla? | [VMD\_000\_Boolean](#-bināra-izvēle--coded-value-domain) -1: Nav zināms; 1: Jā; 2: Nē; 0: Nav ievadīts; | Saglabat\_Buferi | 1 |  |  |
| Neizvākt sausos un kritušos kokus? | [VMD\_000\_Boolean](#-bināra-izvēle--coded-value-domain) -1: Nav zināms; 1: Jā; 2: Nē; 0: Nav ievadīts; | Neizvakt\_Sausos | 1 |  |  |
| Nedrīkst nosusināt? | [VMD\_000\_Boolean](#-bināra-izvēle--coded-value-domain) -1: Nav zināms; 1: Jā; 2: Nē; 0: Nav ievadīts; | Nenosusinat | 1 |  |  |
| Jāizcērt pamežs? | [VMD\_000\_Boolean](#-bināra-izvēle--coded-value-domain) -1: Nav zināms; 1: Jā; 2: Nē; 0: Nav ievadīts; | Jaizcert\_Pamezs | 1 |  |  |
| Piezīmes par apsaimniekošanu | Text | Piezimes |  |  |  |

  
###  -Biotopa apsaimniekošana – izcērtama suga- [Object class]




|  |  |
| --- | --- |
| Name in DB | VMDBIOIZCERTAMASUGA |
| Object type | Object class |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Biotopa apsaimniekošana – sugas izcirtes apjomi (VMDBIOIZCERTAMIAPJOMI)](#-biotopa-apsaimniekošana--sugas-izcirtes-apjomi--object-class)  | [Biotopa apsaimniekošana – izcērtama suga](#-biotopa-apsaimniekošana--izcērtama-suga--object-class).Unikālais identifikators  -> [Biotopa apsaimniekošana – sugas izcirtes apjomi](#-biotopa-apsaimniekošana--sugas-izcirtes-apjomi--object-class).Sasaiste ar BIOIZCERTAMA\_SUGA | 1:N |
|  [Biotopa apsaimniekošana (VMDBIOAPSAIMNIEKOSANA)](#-biotopa-apsaimniekošana--object-class) | [Biotopa apsaimniekošana](#-biotopa-apsaimniekošana--object-class).Unikālais identifikators  -> [Biotopa apsaimniekošana – izcērtama suga](#-biotopa-apsaimniekošana--izcērtama-suga--object-class).Sasaiste ar BIOAPSAIMNIEKOSANA | 1:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Unikālais identifikators | Long integer | BioIzcertamaSuga\_ID | 10 |  |  |
| Sasaiste ar BIOAPSAIMNIEKOSANA | Long integer | Aps\_ID | 10 |  |  |
| Izcirtes veids | [VMD\_171\_Bioizcertama\_suga\_Types](#-izciršanas-veidi--coded-value-domain) 1: Izciršana; 2: Izciršana ap biokokiem; | BioIzcertamaSuga\_tips | 3 |  |  |
| Skaits | Long integer | Skaits | 10 |  |  |
| Suga | [VMD\_180\_Koku\_Sugas](#-koku-sugas--coded-value-domain) -1: Nav zināms; | KokSug |  |  |  |

  
###  -Biotopa apsaimniekošana – sugas izcirtes apjomi- [Object class]




|  |  |
| --- | --- |
| Name in DB | VMDBIOIZCERTAMIAPJOMI |
| Object type | Object class |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Biotopa apsaimniekošana – izcērtama suga (VMDBIOIZCERTAMASUGA)](#-biotopa-apsaimniekošana--izcērtama-suga--object-class) | [Biotopa apsaimniekošana – izcērtama suga](#-biotopa-apsaimniekošana--izcērtama-suga--object-class).Unikālais identifikators  -> [Biotopa apsaimniekošana – sugas izcirtes apjomi](#-biotopa-apsaimniekošana--sugas-izcirtes-apjomi--object-class).Sasaiste ar BIOIZCERTAMA\_SUGA | 1:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Sasaiste ar BIOIZCERTAMA\_SUGA | Long integer | Izc\_ID | 10 |  |  |
| % no paaugas | Short integer | No\_Paaugas | 3 |  |  |
| % no II stāva | Short integer | No\_2Stava | 3 |  |  |
| % no I stāva | Short integer | No\_1Stava | 3 |  |  |
| Izcērtamo apjomu veids | [VMD\_170\_Bioizcertami\_apjomi\_Types](#-izcērtamo-apjomu-veidi--coded-value-domain) -1: Nav zināms; 1: 100% platībā; 2: 50% un > platībā; 3: 50% un mazāk platībā; 4: Paņēmienu skaits; | Apjoma\_tipi | 3 |  |  |

  
###  -Biotopa atslēgas elementi- [Object class]




|  |  |
| --- | --- |
| Name in DB | VMDBIOATSLEGASELEMENTI |
| Object type | Object class |

  
##### Object subtypes




| Value | Description |
| --- | --- |
| 2 | Ar apjomu |
| 1 | Bez apjoma |
| 3 | Ar apjomu un sugu |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Biotops (VMDBIOTOPI)](#-biotops--feature-class) | [Biotops](#-biotops--feature-class).Unikālais identifikators  -> [Biotopa atslēgas elementi](#-biotopa-atslēgas-elementi--object-class).Sasaiste ar BIOTOPI | 1:N |
|  [Biotopa atslēgas elementu sugas (VMDBIOELEMENTASUGAS)](#-biotopa-atslēgas-elementu-sugas--object-class)  | [Biotopa atslēgas elementi](#-biotopa-atslēgas-elementi--object-class).Unikālais identifikators  -> [Biotopa atslēgas elementu sugas](#-biotopa-atslēgas-elementu-sugas--object-class).Atslēgas identifikators (sasaistei) | 1:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Unikālais identifikators | Long integer | BioAtslegas\_Elementi\_ID | 10 |  |  |
| Atslēgas elementa apakštips | Long integer | BioAtslegas\_Elementi\_ST | 10 | 1 |  |
| Sasaiste ar BIOTOPI | Long integer | Bio\_ID | 10 |  |  |
| Atslēgas elementa veids | [VMD\_030\_Bioelementa\_Veidi\_I](#-biotopa-atslēgas-elementu-veidi-bez-apjoma--coded-value-domain) 1: Dažādvecuma audze; 2: Atvērumu vainaga klājā / lauces; 3: Pašizretināšanās; 4: Pastāvīgi pārplūstoši klajumi; 5: Īslaicīgi pārplūstoši klajumi; 6: Mirusi koksne dažās sadal. pakāpēs; 7: Mirusi koksne vairākās sadal. pakāpēs; 8: Daudz koksnes sēņu / piepju; 9: Daudz vecu lazdu;... | ElemV\_Type | 3 |  |  |
| Atslēgas elementa apjoms | [VMD\_035\_Bioelementa\_Veida\_Apjoms](#-bioelementu-veida-apjomi--coded-value-domain) -1: Nav Zināms; 1: 1-5; 2: 6-10; 3: >10; 0: Nav definēts; | Apjoms\_Type | 3 |  |  |

  
###  -Biotopa atslēgas elementu sugas- [Object class]




|  |  |
| --- | --- |
| Name in DB | VMDBIOELEMENTASUGAS |
| Object type | Object class |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Biotopa atslēgas elementi (VMDBIOATSLEGASELEMENTI)](#-biotopa-atslēgas-elementi--object-class) | [Biotopa atslēgas elementi](#-biotopa-atslēgas-elementi--object-class).Unikālais identifikators  -> [Biotopa atslēgas elementu sugas](#-biotopa-atslēgas-elementu-sugas--object-class).Atslēgas identifikators (sasaistei) | 1:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Suga | [VMD\_180\_Koku\_Sugas](#-koku-sugas--coded-value-domain) -1: Nav zināms; | KokSug |  |  |  |
| Atslēgas identifikators (sasaistei) | Long integer | BioAtslegas\_Elementi\_ID | 10 |  | Yes |

  
###  -Biotopa audzes raksturojumi- [Object class]




|  |  |
| --- | --- |
| Name in DB | VMDBIOAUDZESRAKSTUROJUM |
| Object type | Object class |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Biotops (VMDBIOTOPI)](#-biotops--feature-class) | [Biotops](#-biotops--feature-class).Unikālais identifikators  -> [Biotopa audzes raksturojumi](#-biotopa-audzes-raksturojumi--object-class).Sasaiste ar BIOTOPI | 1:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Unikālais identifikators | Long integer | Bioaudzes\_Raksturojumi\_ID | 10 |  |  |
| Sasaiste ar BIOTOPI | Long integer | Bio\_ID | 10 |  |  |
| procentuālais sugas daudzums | Short integer | Koeficients | 2 |  |  |
| Sugas vecums | Short integer | Vecums | 3 |  |  |
| Suga | [VMD\_180\_Koku\_Sugas](#-koku-sugas--coded-value-domain) -1: Nav zināms; | KokSug |  |  |  |

  
###  -Biotopa indikatoru sugas- [Object class]




|  |  |
| --- | --- |
| Name in DB | VMDBIOINDIKATORUSUGAS |
| Object type | Object class |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Biotops (VMDBIOTOPI)](#-biotops--feature-class) | [Biotops](#-biotops--feature-class).Unikālais identifikators  -> [Biotopa indikatoru sugas](#-biotopa-indikatoru-sugas--object-class).Sasaiste ar BIOTOPI | 1:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Unikālais identifikators | Long integer | BioIndikatoru\_Sugas\_ID | 10 |  |  |
| Sasaiste ar BIOTOPI | Long integer | Bio\_ID | 10 |  |  |
| Biotopa indikatoru suga | [VMD\_020\_Biosugu\_veidi](#-biotopa-indikatoru-sugu-veidi--coded-value-domain) -1: Nav zināms; 100: Cits; | BioSug\_Type |  |  |  |
| Biotopa indikatoru sugas sastopamība | [VMD\_021\_BioSugu\_Sastopamiba](#-biotopa-indikatoru-sugu-sastopamība--coded-value-domain) -1: Nav zināms; | Sast\_Type |  |  |  |

  
###  -Biotopa negatīvi traucējumi- [Object class]




|  |  |
| --- | --- |
| Name in DB | VMDBIONEGATIVITRAUC |
| Object type | Object class |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Biotops (VMDBIOTOPI)](#-biotops--feature-class) | [Biotops](#-biotops--feature-class).Unikālais identifikators  -> [Biotopa negatīvi traucējumi](#-biotopa-negatīvi-traucējumi--object-class).Sasaiste ar BIOTOPI | 1:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Unikālais identifikators | Long integer | BioNegativiTraucejumi\_ID | 10 |  |  |
| Sasaiste ar BIOTOPI | Long integer | Bio\_ID | 10 |  |  |
| Biotopa negatīvo traucējumu veids | [VMD\_040\_BioTraucejumu\_Veidi](#-biotopa-traucējumu-veidi--coded-value-domain) -1: Nav zināms; | Trauc\_Type |  |  |  |
| Intensitāte | [VMD\_041\_BioTraucējumu\_Intensitate](#-biotopa-traucējumu-intensitāte--coded-value-domain) 1: 1; 2: 2; 3: 3; 4: 4; 5: 5; 6: 6; 7: 7; 8: 8; 9: 9;... | Intensitate | 1 |  |  |

  
###  -Biotopa īpašās iezīmes- [Object class]




|  |  |
| --- | --- |
| Name in DB | VMDBIOIEZIMES |
| Object type | Object class |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Biotops (VMDBIOTOPI)](#-biotops--feature-class) | [Biotops](#-biotops--feature-class).Unikālais identifikators  -> [Biotopa īpašās iezīmes](#-biotopa-īpašās-iezīmes--object-class).Sasaiste ar BIOTOPI | 1:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Unikālais identifikators | Long integer | Bioiezimes\_ID | 10 |  |  |
| Sasaiste ar BIOTOPI | Long integer | Bio\_ID | 10 |  |  |
| Īpašo iezīmju veids | [VMD\_050\_Bioiezīmju\_veidi](#-biotopa-īpašo-iezīmju-veidi--coded-value-domain) 1: Lielas ligzdas; 2: Skudru pūžņi; 3: Dzīvnieku alas; 4: Dzīvnieku "vannas"; 5: Laukakmeņi; 6: Pamatieža atsegums; | IezV\_Type | 2 |  |  |
| Skaits | Short integer | Skaits | 2 |  |  |
| Apraksts | Text | Apraksts |  |  |  |

  
###  -Ugunsgrēki- [Object class]




|  |  |
| --- | --- |
| Name in DB | VMDUGUNSGREKI |
| Object type | Object class |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Ugunsgrēku platības uzskaite (VMDUGUNSPLATIBAS)](#-ugunsgrēku-platības-uzskaite--object-class)  | [Ugunsgrēki](#-ugunsgrēki--object-class).Unikālais identifikators  -> [Ugunsgrēku platības uzskaite](#-ugunsgrēku-platības-uzskaite--object-class).Identifikators sasaistei | 1:N |
|  [Ugunsgrēka vieta (VMDUGUNSGREKPOINT)](#-ugunsgrēka-vieta--feature-class)  | [Ugunsgrēki](#-ugunsgrēki--object-class).Unikālais identifikators  -> [Ugunsgrēka vieta](#-ugunsgrēka-vieta--feature-class).Sasaiste ar UGUNSGREKI | 1:N |
|  [Ugunsgrēka teritorija (VMDUGUNSGREKPOLY)](#-ugunsgrēka-teritorija--feature-class)  | [Ugunsgrēki](#-ugunsgrēki--object-class).Unikālais identifikators  -> [Ugunsgrēka teritorija](#-ugunsgrēka-teritorija--feature-class).Sasaiste ar UGUNSGREKI | 1:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Unikālais identifikators | Long integer | Ugunsgreki\_ID | 10 |  |  |
| Ugunscēloņi | [VMD\_090\_Ugunsceloni](#-ugunsgrēka-cēloņi--coded-value-domain) -1: Nav zināms; | Ucel\_Type | 3 |  |  |
| Trauksmes laiks | Date | Trauksme |  |  |  |
| Uzsāk dzēšanu | Date | Usak |  |  |  |
| Ierobežošanas laiks | Date | Ierobezo |  |  |  |
| Likvidēšanas laiks | Date | Likvide |  |  |  |
| Ugunsgrēka atklāšanas veids | [VMD\_093\_UgunsAtklType](#-ugunsgrēka-atklāšanas-veids--coded-value-domain) 1: No torņa; 2: Ziņo trešā persona; 3: Ziņo VUGD; | UATKL\_TYPE | 3 |  |  |

  
###  -Ugunsgrēku platības uzskaite- [Object class]




|  |  |
| --- | --- |
| Name in DB | VMDUGUNSPLATIBAS |
| Object type | Object class |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Ugunsgrēki (VMDUGUNSGREKI)](#-ugunsgrēki--object-class) | [Ugunsgrēki](#-ugunsgrēki--object-class).Unikālais identifikators  -> [Ugunsgrēku platības uzskaite](#-ugunsgrēku-platības-uzskaite--object-class).Identifikators sasaistei | 1:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Identifikators sasaistei | Long integer | Ugunsgreki\_ID | 10 |  |  |
| Ugunscēloņi | [VMD\_091\_Meza\_piederiba](#-meža-piederība--coded-value-domain) PRV: Privātie; VLS: Valsts (izņemot AS ‘LVM’); VAS: AS ‘Latvijas valsts meži’ meži; PSV: Pašvaldības; | Piedriba |  |  |  |
| Platības zemes veids | [VMD\_092\_UgunsPlatType](#-ugunsgrēku-platību-uzskaites-tips--coded-value-domain) 1: Mežu platība; 2: Jaunaudžu platība; 3: Citu meža zemju platība; 4: Citu nemeža zemju platība; | PlatibaType | 3 |  |  |
| Platība | Double | Platiba | 7 |  |  |

  
###  -Vides aizsardzības ierobežojumi- [Object class]




|  |  |
| --- | --- |
| Name in DB | VMDVAIEROBEZOJUMI |
| Object type | Object class |

  
##### Relationships




| Data object | Key fields | Cardinality |
| --- | --- | --- |
|  [Vides aizsardzības klasifikators (VMDVAKLASIFIKATORS)](#-vides-aizsardzības-klasifikators--feature-class) | [Vides aizsardzības klasifikators](#-vides-aizsardzības-klasifikators--feature-class).Unikālais identifikators  -> [Vides aizsardzības ierobežojumi](#-vides-aizsardzības-ierobežojumi--object-class).Sasaiste ar VA klasifikatoru | 1:N |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identificator (OID) | OBJECTID |  |  | Yes |
| Ierobežojuma nosaukums | [VMD\_150\_VA\_IerobezojumuVeidi](#-vides-aizsardzības-ierobežojumu-veidi--coded-value-domain) -1: Nav zināms; | Nosaukums |  |  |  |
| Sasaiste ar VA klasifikatoru | Long integer | VAK\_ID | 10 |  |  |

  
###  -RC\_BIO\_KONC\_LINK- [Relationship class]




|  |  |
| --- | --- |
| Name in DB | RC\_BIO\_KONC\_LINK |
| Object type | Relationship class |

  
##### Data object attributes




| Name | Type | Name in DB | Precision | Default value | Mandatory |
| --- | --- | --- | --- | --- | --- |
| Biotopa identifikators (sasaistei) | Long integer | BiotopsFK\_ID | 10 |  | Yes |
| Koncentrācijas vietas identifikators (sasaistei) | Long integer | BioKoncentracijaFK\_ID | 10 |  | Yes |
| ES Biotops | [VMD\_070\_Biotopi\_ES](#-es-biotopa-tips--coded-value-domain) | Estips\_ID |  |  |  |

  
 -Coded value domains-
----------------------

###  -Augšanas apstākļu tipi- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_190\_AAT |
| Values | -1 - Nav zināms;  |
| Used in object classes: | Feature class:  [Biotops](#-biotops--feature-class)  |

   

###  -Bināra izvēle- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_000\_Boolean |
| Values | -1 - Nav zināms; 1 - Jā; 2 - Nē; 0 - Nav ievadīts;  |
| Used in object classes: | Feature class:  [Vides aizsardzības klasifikators](#-vides-aizsardzības-klasifikators--feature-class) Object class:  [Biotopa apsaimniekošana](#-biotopa-apsaimniekošana--object-class) Feature class:  [Biotopu koncentrācijas vieta](#-biotopu-koncentrācijas-vieta--feature-class)  |

   

###  -Bioelementu veida apjomi- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_035\_Bioelementa\_Veida\_Apjoms |
| Values | -1 - Nav Zināms; 1 - 1-5; 2 - 6-10; 3 - >10; 0 - Nav definēts;  |
| Used in object classes: | Object class:  [Biotopa atslēgas elementi](#-biotopa-atslēgas-elementi--object-class)  |

   

###  -Biokoncentrācijas vietu infrastruktūras tips- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_081\_BioKoncentracija\_Infrastruktura |
| Values | 1 - 1. Priežu meži ar dažādvecuma kokiem; 2 - 2. Lapu koku pionierfāzes meži; 3 - 3. Meži ar dažādu pašizrobošanās dinamiku; 3A - 3a. Slapjie egļu meži un pārējie egļu meži; 3B - 3b. Slapjie melnalkšņu un platlapju meži; 3C - 3c. Platlapju meži; 3AB - 3ab. Slapjie egļu meži un pārējie egļu meži; Slapjie melnalkšņu un platlapju meži; 3AC - 3ac. Slapjie egļu meži un pārējie egļu meži; Platlapju meži; 3BC - 3b. Slapjie melnalkšņu un platlapju meži; Platlapju meži; 3ABC - 3a. Slapjie egļu meži un pārējie egļu meži; Slapjie melnalkšņu un platlapju meži; Platlapju meži; 4 - 4. Ģeoloģiskās uzbūves nosacītie lineārie biotopi;  |
| Used in object classes: | Feature class:  [Biotopu koncentrācijas vieta](#-biotopu-koncentrācijas-vieta--feature-class)  |

   

###  -Biotopa atslēgas elementu veidi (Ar apjomu un sugu)- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_032\_Bioelementa\_Veidi\_III |
| Values | 18 - Bioloģiski veci koki; 19 - Mazu dimensiju lēni augoši veci koki; 20 - Saulei atklāti veci platl. koki; 21 - Krituši koki ar mizu; 22 - Krituši koki bez mizas; 23 - Nokrituši kaistoši koki; 24 - Stumbeņi;  |
| Used in object classes: | Object class:  [Biotopa atslēgas elementi](#-biotopa-atslēgas-elementi--object-class)  |

   

###  -Biotopa atslēgas elementu veidi (Ar apjomu)- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_031\_Bioelementa\_Veidi\_II |
| Values | 14 - Ciņi ar pamatnēm; 15 - Koki ar deguma rētām; 16 - Dobumaini koki; 17 - Dzeņveidīgo sakalti koki;  |
| Used in object classes: | Object class:  [Biotopa atslēgas elementi](#-biotopa-atslēgas-elementi--object-class)  |

   

###  -Biotopa atslēgas elementu veidi (Bez apjoma)- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_030\_Bioelementa\_Veidi\_I |
| Values | 1 - Dažādvecuma audze; 2 - Atvērumu vainaga klājā / lauces; 3 - Pašizretināšanās; 4 - Pastāvīgi pārplūstoši klajumi; 5 - Īslaicīgi pārplūstoši klajumi; 6 - Mirusi koksne dažās sadal. pakāpēs; 7 - Mirusi koksne vairākās sadal. pakāpēs; 8 - Daudz koksnes sēņu / piepju; 9 - Daudz vecu lazdu; 10 - Vismaz 4 dažādu sugu platlapji; 11 - Avotu ietekme; 12 - Bebru darbības pēdas; 13 - Dabīgās ūdensteces;  |
| Used in object classes: | Object class:  [Biotopa atslēgas elementi](#-biotopa-atslēgas-elementi--object-class)  |

   

###  -Biotopa indikatoru sugu sastopamība- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_021\_BioSugu\_Sastopamiba |
| Values | -1 - Nav zināms;  |
| Used in object classes: | Object class:  [Biotopa indikatoru sugas](#-biotopa-indikatoru-sugas--object-class)  |

   

###  -Biotopa indikatoru sugu veidi- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_020\_Biosugu\_veidi |
| Values | -1 - Nav zināms; 100 - Cits;  |
| Used in object classes: | Object class:  [Biotopa indikatoru sugas](#-biotopa-indikatoru-sugas--object-class)  |

   

###  -Biotopa informācijas avoti- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_010\_BioInfoAvoti |
| Values | -1 - Nav zināms; 1 - Meža valsts reģistrs; 2 - Topogrāfiskā karte; 3 - Vietējais mežsargs/iedzīvotājs; 4 - Citas kartes; 5 - Citi pētījumi; 6 - Atrasts nejauši lauku darbu gaitā;  |
| Used in object classes: | Feature class:  [Biotops](#-biotops--feature-class)  |

   

###  -Biotopa nosaukumi- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_011\_Bionosaukumi |
| Values | -1 - Nav zināms; A1 - Skujkoku mežs; A2 - Mistrots skujkoku-lapukoku mežs; B1 - Platlapju mežs; B2 - Apšu mežs; B3 - Cits lapukoku mežs; C1 - Slapjš melnalkšņu mežs; C2 - Egļu un mistrots egļu slapjais mežs; C3 - Priežu un bērzu slapjais mežs; C4 - Platlapju slapjais mežs; D1 - Gravas mežs; D2 - Nogāzes mežs; D3 - Krastmalas mežs; D4 - Avotains mežs; D5 - Kaļķains skujkoku mežs; D6 - Kaļķains zāļu purvs vai pļava; D7 - Purva vai meža mozaīka; E1 - Dedzis mežs; E2 - Bioloģiski nozīmīga bebraine; E3 - Biokoks; E4 - Vējgāzes mežs;  |
| Used in object classes: | Feature class:  [Biotops](#-biotops--feature-class)  |

   

###  -Biotopa traucējumu intensitāte- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_041\_BioTraucējumu\_Intensitate |
| Values | 1 - 1; 2 - 2; 3 - 3; 4 - 4; 5 - 5; 6 - 6; 7 - 7; 8 - 8; 9 - 9;  |
| Used in object classes: | Object class:  [Biotopa negatīvi traucējumi](#-biotopa-negatīvi-traucējumi--object-class)  |

   

###  -Biotopa traucējumu veidi- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_040\_BioTraucejumu\_Veidi |
| Values | -1 - Nav zināms;  |
| Used in object classes: | Object class:  [Biotopa negatīvi traucējumi](#-biotopa-negatīvi-traucējumi--object-class)  |

   

###  -Biotopa īpašo iezīmju veidi- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_050\_Bioiezīmju\_veidi |
| Values | 1 - Lielas ligzdas; 2 - Skudru pūžņi; 3 - Dzīvnieku alas; 4 - Dzīvnieku "vannas"; 5 - Laukakmeņi; 6 - Pamatieža atsegums;  |
| Used in object classes: | Object class:  [Biotopa īpašās iezīmes](#-biotopa-īpašās-iezīmes--object-class)  |

   

###  -Dzīvnieku sugas- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_100\_DzivnSugas |
| Values | 1 - Alnis; 2 - Staltbriedis; 3 - Meža cūka; 4 - Stirna; 5 - Bebrs; 6 - Mednis; 7 - Rubenis; 8 - Lūsis; 9 - Vilks;  |
| Used in object classes: | Feature class:  [VMD dzīvnieku uzskaite](#-vmd-dzīvnieku-uzskaite--feature-class)  |

   

###  -ES Biotopa tips- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_070\_Biotopi\_ES |
| Values |  |
| Used in object classes: | Relationship class:  [RC\_BIO\_KONC\_LINK](#-rc_bio_konc_link--relationship-class)  |

   

###  -Izciršanas veidi- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_171\_Bioizcertama\_suga\_Types |
| Values | 1 - Izciršana; 2 - Izciršana ap biokokiem;  |
| Used in object classes: | Object class:  [Biotopa apsaimniekošana – izcērtama suga](#-biotopa-apsaimniekošana--izcērtama-suga--object-class)  |

   

###  -Izcērtamo apjomu veidi- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_170\_Bioizcertami\_apjomi\_Types |
| Values | -1 - Nav zināms; 1 - 100% platībā; 2 - 50% un > platībā; 3 - 50% un mazāk platībā; 4 - Paņēmienu skaits;  |
| Used in object classes: | Object class:  [Biotopa apsaimniekošana – sugas izcirtes apjomi](#-biotopa-apsaimniekošana--sugas-izcirtes-apjomi--object-class)  |

   

###  -Koku sugas- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_180\_Koku\_Sugas |
| Values | -1 - Nav zināms;  |
| Used in object classes: | Object class:  [Biotopa apsaimniekošana – izcērtama suga](#-biotopa-apsaimniekošana--izcērtama-suga--object-class) Object class:  [Biotopa audzes raksturojumi](#-biotopa-audzes-raksturojumi--object-class) Object class:  [Biotopa atslēgas elementu sugas](#-biotopa-atslēgas-elementu-sugas--object-class)  |

   

###  -Koku sugas- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_161\_KokuSugas |
| Values | -1 - Nav zināms; 100 - Cits;  |
| Used in object classes: | - |

   

###  -Koku sugu klasifikators- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | LVM\_MEDUS\_00003\_TreeSpecies |
| Values | 1 - 01 - Priede; 3 - 03 - Egle; 4 - 04 - Bērzs; 6 - 06 - Melnalksnis; 8 - 08 - Apse; 9 - 09 - Baltalksnis; 10 - 10 - Ozols; 11 - 11 - Osis; 12 - 12 - Liepa; 13 - 13 - Lapegle; 14 - 14 - Citas priedes; 15 - 15 - Citas egles; 16 - 16 - Goba,vīksna; 17 - 17 - Dižskābardis; 18 - 18 - Skābardis; 19 - 19 - Papele; 20 - 20 - Vītols; 21 - 21 - Blīgzna; 22 - 22 - Ciedru priede; 23 - 23 - Baltegle; 24 - 24 - Kļava; 25 - 25 - Saldais ķirsis; 26 - 26 - Mežābele; 27 - 27 - Bumbiere; 28 - 28 - Duglāzija; 29 - 29 - Īve; 32 - 32 - Pīlādži; 35 - 35 - Ievas; 50 - 50 - Dzeltenā akācija; 61 - 61 - Citi ozoli; 62 - 62 - Citas liepas; 63 - 63 - Citas kļavas; 64 - 64 - Citi oši; 65 - 65 - Citas gobas, vīksnas; 66 - 66 - Riekstkoki; 67 - 67 - Zirgkastaņi; 68 - 68 - Hibrīdā apse;  |
| Used in object classes: | Feature class:  [Ugunsgrēka teritorija](#-ugunsgrēka-teritorija--feature-class) Feature class:  [Ugunsgrēka teritorijas skatījums](#-ugunsgrēka-teritorijas-skatījums--feature-class) Feature class:  [Ugunsgrēka vieta](#-ugunsgrēka-vieta--feature-class) Feature class:  [VMD Ugunsgrēka vietas skatījums](#-vmd-ugunsgrēka-vietas-skatījums--feature-class)  |

   

###  -Krūmu sugu klasifikators- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | LVM\_MEDUS\_00003k\_ShrubSpecies |
| Values | 30 - 30 - Kārkli; 31 - 31 - Paegļi; 33 - 33 - Krūkļi; 34 - 34 - Lazdas; 36 - 36 - Sausserži; 37 - 37 - Irbenes; 38 - 38 - Segliņi; 39 - 39 - Ribes-sp.; 40 - 40 - Korintes; 41 - 41 - Vilkābeles; 42 - 42 - Jasmīni; 43 - 43 - Plūškoki; 44 - 44 - Spirejas; 45 - 45 - Ceriņi; 46 - 46 - Klintenes; 47 - 47 - Bārbeles; 48 - 48 - Grimoņi; 49 - 49 - Rozes;  |
| Used in object classes: | - |

   

###  -LVM meža iecirkņi- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | LVM\_00201\_LVMDistricts |
| Values | kodi - Vērtības no slāņa LVMDistrict; ??? - ???;  |
| Used in object classes: | Feature class:  [Ugunsgrēka teritorija](#-ugunsgrēka-teritorija--feature-class) Feature class:  [Ugunsgrēka teritorijas skatījums](#-ugunsgrēka-teritorijas-skatījums--feature-class) Feature class:  [Ugunsgrēka vieta](#-ugunsgrēka-vieta--feature-class) Feature class:  [VMD Ugunsgrēka vietas skatījums](#-vmd-ugunsgrēka-vietas-skatījums--feature-class)  |

   

###  -LVM mežsaimniecības- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | LVM\_00202\_LVMForestry |
| Values | ! - Vērtības no slāņa LVMForestry; ? - ???;  |
| Used in object classes: | Feature class:  [Ugunsgrēka teritorija](#-ugunsgrēka-teritorija--feature-class) Feature class:  [Ugunsgrēka teritorijas skatījums](#-ugunsgrēka-teritorijas-skatījums--feature-class) Feature class:  [Ugunsgrēka vieta](#-ugunsgrēka-vieta--feature-class) Feature class:  [VMD Ugunsgrēka vietas skatījums](#-vmd-ugunsgrēka-vietas-skatījums--feature-class)  |

   

###  -Meža piederība- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_091\_Meza\_piederiba |
| Values | PRV - Privātie; VLS - Valsts (izņemot AS ‘LVM’); VAS - AS ‘Latvijas valsts meži’ meži; PSV - Pašvaldības;  |
| Used in object classes: | Object class:  [Ugunsgrēku platības uzskaite](#-ugunsgrēku-platības-uzskaite--object-class)  |

   

###  -Putnu sugas- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_013\_StatussVeids |
| Values | -1 - Nav zināms; P - Paplašinājums (P); P30-70 - Paplašinājums (P30-70); B - Buferjosla (B); BP - Buferjosla (BP); B30-70 - Buferjosla (B30-70); I - Ieslēgums (I);  |
| Used in object classes: | Feature class:  [Biotops](#-biotops--feature-class)  |

   

###  -Putnu sugas- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_012\_SugasVeids |
| Values | -1 - Nav zināms; 1 - Dzīvnieks; 2 - Augs; 3 - Sūna; 4 - Ķērpis; 5 - Sēne; 6 - IAMB; 100 - Cits;  |
| Used in object classes: | Feature class:  [Biotops](#-biotops--feature-class)  |

   

###  -Pēdu skaita novērtējuma tipi- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_120\_PeduSkaitaTips |
| Values | 1 - Precīzi; 2 - Neprecīzi; 3 - Pieņēmums;  |
| Used in object classes: | - |

   

###  -TemplateCodedValueDomain- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | TemplateCodedValueDomain |
| Values | 1 - Code1; 2 - Code2; 3 - Code3;  |
| Used in object classes: | - |

   

###  -Ugunsgrēka atklāšanas veids- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_093\_UgunsAtklType |
| Values | 1 - No torņa; 2 - Ziņo trešā persona; 3 - Ziņo VUGD;  |
| Used in object classes: | Feature class:  [Ugunsgrēka teritorijas skatījums](#-ugunsgrēka-teritorijas-skatījums--feature-class) Feature class:  [VMD Ugunsgrēka vietas skatījums](#-vmd-ugunsgrēka-vietas-skatījums--feature-class) Object class:  [Ugunsgrēki](#-ugunsgrēki--object-class)  |

   

###  -Ugunsgrēka cēloņi- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_090\_Ugunsceloni |
| Values | -1 - Nav zināms;  |
| Used in object classes: | Feature class:  [Ugunsgrēka teritorijas skatījums](#-ugunsgrēka-teritorijas-skatījums--feature-class) Feature class:  [VMD Ugunsgrēka vietas skatījums](#-vmd-ugunsgrēka-vietas-skatījums--feature-class) Object class:  [Ugunsgrēki](#-ugunsgrēki--object-class)  |

   

###  -Ugunsgrēku platību uzskaites tips- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_092\_UgunsPlatType |
| Values | 1 - Mežu platība; 2 - Jaunaudžu platība; 3 - Citu meža zemju platība; 4 - Citu nemeža zemju platība;  |
| Used in object classes: | Object class:  [Ugunsgrēku platības uzskaite](#-ugunsgrēku-platības-uzskaite--object-class)  |

   

###  -Vides aizsardzības ierobežojumu veidi- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_150\_VA\_IerobezojumuVeidi |
| Values | -1 - Nav zināms;  |
| Used in object classes: | Object class:  [Vides aizsardzības ierobežojumi](#-vides-aizsardzības-ierobežojumi--object-class)  |

   

###  -Vērtējums- [Coded value domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_080\_Vertejums |
| Values | -1 - Nav zināms; 1 - Zems; 2 - Vidējs; 3 - Augsts;  |
| Used in object classes: | Feature class:  [Biotopu koncentrācijas vieta](#-biotopu-koncentrācijas-vieta--feature-class) Feature class:  [Biotops](#-biotops--feature-class)  |

   

 -Range domains-
----------------

###  -Procenti (0-100%)- [Range domain]




|  |  |
| --- | --- |
| Name in DB | VMD\_RD\_Procenti |
| Minimum | 1 |
| Maximum | 100 |
| Used in object classes: | - |

   




