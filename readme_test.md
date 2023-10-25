





 Datu bāzes shēmas apraksts
===========================


Version 2.0.0 



 Saturs
-------


[VMDData](#vmddata-datu-kopa)  
* [Biotops](#biotops-elementu-klase)
* [Biotopu koncentrācijas vieta](#biotopu-koncentrācijas-vieta-elementu-klase)
* [Ugunsgrēka teritorija](#ugunsgrēka-teritorija-elementu-klase)
* [Ugunsgrēka vieta](#ugunsgrēka-vieta-elementu-klase)
* [VMD dzīvnieku uzskaite](#vmd-dzīvnieku-uzskaite-elementu-klase)
* [Vides aizsardzības klasifikators](#vides-aizsardzības-klasifikators-elementu-klase)
* [Vides aizsardzības pazīmes](#vides-aizsardzības-pazīmes-elementu-klase)
  
[VMDDataView](#vmddataview-datu-kopa)  
* [Ugunsgrēka teritorijas skatījums](#ugunsgrēka-teritorijas-skatījums-elementu-klase)
* [VMD Ugunsgrēka vietas skatījums](#vmd-ugunsgrēka-vietas-skatījums-elementu-klase)
  
 [Kopējās elementu un objektu klases](#Kopējās-elementu-un-objektu-klases)  
* [Biotopa apsaimniekošana](#biotopa-apsaimniekošana-objektu-klase)
* [Biotopa apsaimniekošana – izcērtama suga](#biotopa-apsaimniekošana--izcērtama-suga-objektu-klase)
* [Biotopa apsaimniekošana – sugas izcirtes apjomi](#biotopa-apsaimniekošana--sugas-izcirtes-apjomi-objektu-klase)
* [Biotopa atslēgas elementi](#biotopa-atslēgas-elementi-objektu-klase)
* [Biotopa atslēgas elementu sugas](#biotopa-atslēgas-elementu-sugas-objektu-klase)
* [Biotopa audzes raksturojumi](#biotopa-audzes-raksturojumi-objektu-klase)
* [Biotopa indikatoru sugas](#biotopa-indikatoru-sugas-objektu-klase)
* [Biotopa negatīvi traucējumi](#biotopa-negatīvi-traucējumi-objektu-klase)
* [Biotopa īpašās iezīmes](#biotopa-īpašās-iezīmes-objektu-klase)
* [Ugunsgrēki](#ugunsgrēki-objektu-klase)
* [Ugunsgrēku platības uzskaite](#ugunsgrēku-platības-uzskaite-objektu-klase)
* [Vides aizsardzības ierobežojumi](#vides-aizsardzības-ierobežojumi-objektu-klase)
* [RC\_BIO\_KONC\_LINK](#rc_bio_konc_link-relāciju-klase)
  
[Klasifikatori](#Klasifikatori)  
* [Augšanas apstākļu tipi](#augšanas-apstākļu-tipi-klasifikators)
* [Bināra izvēle](#bināra-izvēle-klasifikators)
* [Bioelementu veida apjomi](#bioelementu-veida-apjomi-klasifikators)
* [Biokoncentrācijas vietu infrastruktūras tips](#biokoncentrācijas-vietu-infrastruktūras-tips-klasifikators)
* [Biotopa atslēgas elementu veidi (Ar apjomu un sugu)](#biotopa-atslēgas-elementu-veidi-ar-apjomu-un-sugu-klasifikators)
* [Biotopa atslēgas elementu veidi (Ar apjomu)](#biotopa-atslēgas-elementu-veidi-ar-apjomu-klasifikators)
* [Biotopa atslēgas elementu veidi (Bez apjoma)](#biotopa-atslēgas-elementu-veidi-bez-apjoma-klasifikators)
* [Biotopa indikatoru sugu sastopamība](#biotopa-indikatoru-sugu-sastopamība-klasifikators)
* [Biotopa indikatoru sugu veidi](#biotopa-indikatoru-sugu-veidi-klasifikators)
* [Biotopa informācijas avoti](#biotopa-informācijas-avoti-klasifikators)
* [Biotopa nosaukumi](#biotopa-nosaukumi-klasifikators)
* [Biotopa traucējumu intensitāte](#Biotopa-traucējumu-intensitāte)
* [Biotopa traucējumu veidi](#biotopa-traucējumu-veidi-klasifikators)
* [Biotopa īpašo iezīmju veidi](#Biotopa-īpašo-iezīmju-veidi)
* [Dzīvnieku sugas](#dzīvnieku-sugas-klasifikators)
* [ES Biotopa tips](#es-biotopa-tips-klasifikators)
* [Izciršanas veidi](#izciršanas-veidi-klasifikators)
* [Izcērtamo apjomu veidi](#izcērtamo-apjomu-veidi-klasifikators)
* [Koku sugas](#koku-sugas-klasifikators)
* [Koku sugas](#koku-sugas-klasifikators)
* [Koku sugu klasifikators](#koku-sugu-klasifikators-klasifikators)
* [Krūmu sugu klasifikators](#krūmu-sugu-klasifikators-klasifikators)
* [LVM meža iecirkņi](#lvm-meža-iecirkņi-klasifikators)
* [LVM mežsaimniecības](#lvm-mežsaimniecības-klasifikators)
* [Meža piederība](#meža-piederība-klasifikators)
* [Putnu sugas](#putnu-sugas-klasifikators)
* [Putnu sugas](#putnu-sugas-klasifikators)
* [Pēdu skaita novērtējuma tipi](#pēdu-skaita-novērtējuma-tipi-klasifikators)
* [TemplateCodedValueDomain](#templatecodedvaluedomain-klasifikators)
* [Ugunsgrēka atklāšanas veids](#ugunsgrēka-atklāšanas-veids-klasifikators)
* [Ugunsgrēka cēloņi](#ugunsgrēka-cēloņi-klasifikators)
* [Ugunsgrēku platību uzskaites tips](#ugunsgrēku-platību-uzskaites-tips-klasifikators)
* [Vides aizsardzības ierobežojumu veidi](#vides-aizsardzības-ierobežojumu-veidi-klasifikators)
* [Vērtējums](#vērtējums-klasifikators)
 [Vērtību robežas](#Vērtību-robežas)  
* [Procenti (0-100%)](#procenti-0-100-vērtību-robežas)

  
VMDData [Datu kopa]
-------------------




|  |  |
| --- | --- |
| Nosaukums DB | VMDData |


  

### Biotops [Elementu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDBIOTOPI |
| Objekta tips | Elementu klase |
| Ģeometrija | Laukums |
| M koordinātes | Nē |
| Z koordinātes | Nē |

  
##### Objekta apakštipi




| Vērtība | Apraksts |
| --- | --- |
| 3 | starpaudze meža biotopu koncentrācijas vietā |
| 1 | Potenciālais meža biotops |
| 2 | Dabīgais meža biotops |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Biotopa atslēgas elementi (VMDBIOATSLEGASELEMENTI)](#biotopa-atslēgas-elementi-objektu-klase)  | [Biotops](#biotops-elementu-klase).Unikālais identifikators  -> [Biotopa atslēgas elementi](#biotopa-atslēgas-elementi-objektu-klase).Sasaiste ar BIOTOPI | 1:N |
|  [Biotopu koncentrācijas vieta (VMDBIOKONCENTRACIJA)](#biotopu-koncentrācijas-vieta-elementu-klase) | [Biotops](#biotops-elementu-klase).Unikālais identifikators -> [RC\_BIO\_KONC\_LINK](#rc_bio_konc_link-relāciju-klase).Biotopa identifikators (sasaistei)[Biotopu koncentrācijas vieta](#biotopu-koncentrācijas-vieta-elementu-klase).Unikālais identifikators  -> [Biotops](#biotops-elementu-klase).Koncentrācijas vietas identifikators (sasaistei) | N:N |
|  [Biotopa īpašās iezīmes (VMDBIOIEZIMES)](#biotopa-īpašās-iezīmes-objektu-klase)  | [Biotops](#biotops-elementu-klase).Unikālais identifikators  -> [Biotopa īpašās iezīmes](#biotopa-īpašās-iezīmes-objektu-klase).Sasaiste ar BIOTOPI | 1:N |
|  [Biotopa apsaimniekošana (VMDBIOAPSAIMNIEKOSANA)](#biotopa-apsaimniekošana-objektu-klase)  | [Biotops](#biotops-elementu-klase).Unikālais identifikators  -> [Biotopa apsaimniekošana](#biotopa-apsaimniekošana-objektu-klase).Sasaiste ar BIOTOPI | 1:N |
|  [Biotopa negatīvi traucējumi (VMDBIONEGATIVITRAUC)](#biotopa-negatīvi-traucējumi-objektu-klase)  | [Biotops](#biotops-elementu-klase).Unikālais identifikators  -> [Biotopa negatīvi traucējumi](#biotopa-negatīvi-traucējumi-objektu-klase).Sasaiste ar BIOTOPI | 1:N |
|  [Biotopa indikatoru sugas (VMDBIOINDIKATORUSUGAS)](#biotopa-indikatoru-sugas-objektu-klase)  | [Biotops](#biotops-elementu-klase).Unikālais identifikators  -> [Biotopa indikatoru sugas](#biotopa-indikatoru-sugas-objektu-klase).Sasaiste ar BIOTOPI | 1:N |
|  [Biotopa audzes raksturojumi (VMDBIOAUDZESRAKSTUROJUM)](#biotopa-audzes-raksturojumi-objektu-klase)  | [Biotops](#biotops-elementu-klase).Unikālais identifikators  -> [Biotopa audzes raksturojumi](#biotopa-audzes-raksturojumi-objektu-klase).Sasaiste ar BIOTOPI | 1:N |
|  [Vides aizsardzības pazīmes (VMDVAPAZIMES)](#vides-aizsardzības-pazīmes-elementu-klase) | [Vides aizsardzības pazīmes](#vides-aizsardzības-pazīmes-elementu-klase).Unikālais identifikators  -> [Biotops](#biotops-elementu-klase).Sasaiste ar vides aizsardzības klasifikatora pazīmēm | 1:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Shape | Ģeometrija | Shape |  |  | Jā |
| Unikālais identifikators | Garais skaitlis | Biotops\_ID | 10 |  |  |
| Apakštipa lauks | Garais skaitlis | Biotops\_ST | 10 | 1 |  |
| Biotopa Nr. | Teksts | Numurs |  |  |  |
| Platība (situācijai dabā) | Daļskaitlis | Platiba | 6 |  |  |
| Audzes sastāva formula (situācijai dabā) | Teksts | Formula |  |  |  |
| Augšanas apstākļu tips | [VMD\_190\_AAT](#augšanas-apstākļu-tipi-klasifikators) | AAT | 2 |  |  |
| Sasaiste ar vides aizsardzības klasifikatora pazīmēm | Garais skaitlis | VA\_Paz\_ID | 10 |  |  |
| Informācijas avots | [VMD\_010\_BioInfoAvoti](#biotopa-informācijas-avoti-klasifikators) | InfoAv | 3 |  |  |
| Biotopa nosaukums I | [VMD\_011\_Bionosaukumi](#biotopa-nosaukumi-klasifikators) | Nosaukums1 |  |  |  |
| Biotopa nosaukums II | [VMD\_011\_Bionosaukumi](#biotopa-nosaukumi-klasifikators) | Nosaukums2 |  |  |  |
| Bioloģiskās daudzveidības apraksts | Teksts | Daudzveidiba |  |  |  |
| Piezīmes | Teksts | Piezimes |  |  |  |
| Apsekošanas datums | Datums | Datums |  |  |  |
| Persona, kas veica apsekošanu | Teksts | Apsekoja |  |  |  |
| Audzes status | [VMD\_013\_StatussVeids](#putnu-sugas-klasifikators) | SA\_Statuss |  |  |  |
| Audzes suga | Īsais skaitlis | SA\_Suga | 3 |  |  |
| Audzes ierobežojumu intensitāte | Īsais skaitlis | SA\_Intensitate | 3 |  |  |
| Piezīmes, suga | Teksts | SA\_Suga\_Piezimes |  |  |  |
| DMB raksturīgo ekoloģisko rādītāju sasniegšanas laiks | Īsais skaitlis | SA\_Sasniegsana | 3 |  |  |
| Novērtējums par audzes piemērotību paplašinājumiem | [VMD\_080\_Vertejums](#vērtējums-klasifikators) | SA\_Piemerotiba | 3 |  |  |
| Apsaimniekošanas apraksts | Teksts | SA\_Apsaimn |  |  |  |

  
### Biotopu koncentrācijas vieta [Elementu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDBIOKONCENTRACIJA |
| Objekta tips | Elementu klase |
| Ģeometrija | Laukums |
| M koordinātes | Nē |
| Z koordinātes | Nē |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Biotops (VMDBIOTOPI)](#biotops-elementu-klase)  | [Biotops](#biotops-elementu-klase).Unikālais identifikators -> [RC\_BIO\_KONC\_LINK](#rc_bio_konc_link-relāciju-klase).Biotopa identifikators (sasaistei)[Biotopu koncentrācijas vieta](#biotopu-koncentrācijas-vieta-elementu-klase).Unikālais identifikators  -> [Biotops](#biotops-elementu-klase).Koncentrācijas vietas identifikators (sasaistei) | N:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Shape | Ģeometrija | Shape |  |  | Jā |
| Unikālais identifikators | Garais skaitlis | BioKoncentracija\_ID | 10 |  |  |
| Koncentrācijas Nr. | Teksts | Numurs |  |  |  |
| Infrastruktūras tips | [VMD\_081\_BioKoncentracija\_Infrastruktura](#biokoncentrācijas-vietu-infrastruktūras-tips-klasifikators) | Infrastruktura |  |  |  |
| Atrodas nozīmīgajā apvidū? | [VMD\_000\_Boolean](#bināra-izvēle-klasifikators) | Nozimigs\_Apvidus | 1 |  |  |
| Nav nosusināts | Garais skaitlis | NT\_Nesusinats | 3 |  |  |
| Nosusināts, bet sistēma nedarbojas | Garais skaitlis | NT\_SusNeDarb | 3 |  |  |
| Nosusināšana darbojas | Garais skaitlis | NT\_SusDarb | 3 |  |  |
| Biotopu koncentrācijas vietas vērtējums? | [VMD\_080\_Vertejums](#vērtējums-klasifikators) | Konc\_Vert | 1 |  |  |
| Nosusināšanas ilglaicīgā negatīvā ietekme uz bioloģiskajām vērtībām | [VMD\_080\_Vertejums](#vērtējums-klasifikators) | Sus\_Ietekme | 1 |  |  |
| Ietekme, slēdzot nosusināšanas sistēmu | [VMD\_080\_Vertejums](#vērtējums-klasifikators) | SusSledz\_Ietekme | 1 |  |  |
| Ieguvums | Teksts | Ieguvums |  |  |  |
| Piezīmes | Teksts | Piezimes |  |  |  |
| Apsekoja | Teksts | Apsekoja |  |  |  |
| Datums | Datums | Datums |  |  |  |

  
### Ugunsgrēka teritorija [Elementu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDUGUNSGREKPOLY |
| Objekta tips | Elementu klase |
| Ģeometrija | Laukums |
| M koordinātes | Nē |
| Z koordinātes | Nē |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Ugunsgrēki (VMDUGUNSGREKI)](#ugunsgrēki-objektu-klase) | [Ugunsgrēki](#ugunsgrēki-objektu-klase).Unikālais identifikators  -> [Ugunsgrēka teritorija](#ugunsgrēka-teritorija-elementu-klase).Sasaiste ar UGUNSGREKI | 1:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Shape | Ģeometrija | Shape |  |  | Jā |
| Sasaiste ar UGUNSGREKI | Garais skaitlis | Ug\_ID | 10 |  |  |
| Mežsaimniecība  | [LVM\_00202\_LVMForestry](#lvm-mežsaimniecības-klasifikators) | LVMForestryCode |  |  |  |
| Kv.apg. - kvartāls | Teksts | BlockKey |  |  |  |
| Nogabala numurs | Īsais skaitlis | CompartmentNumber | 2 |  |  |
| Iecirknis | [LVM\_00201\_LVMDistricts](#lvm-meža-iecirkņi-klasifikators) | LVM\_District\_Code |  |  |  |
| Sugu sastāvs (M) | Teksts | SugasSastavs |  |  |  |
| Meža tipa apzīmējums (M) | Teksts | AAT |  |  |  |
| 1.sugas vecums (M) | Garais skaitlis | A10 | 10 |  |  |
| 1.suga (M) | [LVM\_MEDUS\_00003\_TreeSpecies](#koku-sugu-klasifikators-klasifikators) | S10 | 10 |  |  |

  
### Ugunsgrēka vieta [Elementu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDUGUNSGREKPOINT |
| Objekta tips | Elementu klase |
| Ģeometrija | Punkts |
| M koordinātes | Nē |
| Z koordinātes | Nē |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Ugunsgrēki (VMDUGUNSGREKI)](#ugunsgrēki-objektu-klase) | [Ugunsgrēki](#ugunsgrēki-objektu-klase).Unikālais identifikators  -> [Ugunsgrēka vieta](#ugunsgrēka-vieta-elementu-klase).Sasaiste ar UGUNSGREKI | 1:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Shape | Ģeometrija | Shape |  |  | Jā |
| Simbola leņķis | Daļskaitlis | Angval | 5 |  |  |
| Sasaiste ar UGUNSGREKI | Garais skaitlis | Ug\_ID | 10 |  |  |
| Mežsaimniecība  | [LVM\_00202\_LVMForestry](#lvm-mežsaimniecības-klasifikators) | LVMForestryCode |  |  |  |
| Kv.apg. - kvartāls | Teksts | BlockKey |  |  |  |
| Nogabala numurs | Īsais skaitlis | CompartmentNumber | 2 |  |  |
| Iecirknis | [LVM\_00201\_LVMDistricts](#lvm-meža-iecirkņi-klasifikators) | LVM\_District\_Code |  |  |  |
| Meža tipa apzīmējums (M) | Teksts | AAT |  |  |  |
| Sugu sastāvs (M) | Teksts | SugasSastavs |  |  |  |
| 1.sugas vecums (M) | Garais skaitlis | A10 | 10 |  |  |
| 1.suga (M) | [LVM\_MEDUS\_00003\_TreeSpecies](#koku-sugu-klasifikators-klasifikators) | S10 | 10 |  |  |

  
### VMD dzīvnieku uzskaite [Elementu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDAnimalCount |
| Objekta tips | Elementu klase |
| Ģeometrija | Laukums |
| M koordinātes | Nē |
| Z koordinātes | Nē |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Shape | Ģeometrija | Shape |  |  | Jā |
| Uzskaites vienība | Teksts | Uzsk\_vien |  |  |  |
| Nosaukums | Teksts | Nosaukums |  |  |  |
| Dzīvnieku suga | [VMD\_100\_DzivnSugas](#dzīvnieku-sugas-klasifikators) | Suga | 2 |  |  |
| Uzskaites vērtība | Daļskaitlis | UzskVertiba | 5 |  |  |

  
### Vides aizsardzības klasifikators [Elementu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDVAKLASIFIKATORS |
| Objekta tips | Elementu klase |
| Ģeometrija | Laukums |
| M koordinātes | Nē |
| Z koordinātes | Nē |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Vides aizsardzības ierobežojumi (VMDVAIEROBEZOJUMI)](#vides-aizsardzības-ierobežojumi-objektu-klase)  | [Vides aizsardzības klasifikators](#vides-aizsardzības-klasifikators-elementu-klase).Unikālais identifikators  -> [Vides aizsardzības ierobežojumi](#vides-aizsardzības-ierobežojumi-objektu-klase).Sasaiste ar VA klasifikatoru | 1:N |
|  [Vides aizsardzības pazīmes (VMDVAPAZIMES)](#vides-aizsardzības-pazīmes-elementu-klase)  | [Vides aizsardzības klasifikators](#vides-aizsardzības-klasifikators-elementu-klase).Unikālais identifikators  -> [Vides aizsardzības pazīmes](#vides-aizsardzības-pazīmes-elementu-klase).Sasaiste ar VA\_KLASIFIKATORS | 1:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Shape | Ģeometrija | Shape |  |  | Jā |
| Unikālais identifikators | Garais skaitlis | VAK\_ID | 10 |  |  |
| Hierarhijas sasaiste | Garais skaitlis | Parent\_VAK\_ID | 10 |  |  |
| Kods | Teksts | Kods |  |  |  |
| Nosaukums | Teksts | Nosaukums |  |  |  |
| Vai atļauts reģistrēt unikālās aizsardzības pazīmes? | [VMD\_000\_Boolean](#bināra-izvēle-klasifikators) | Unikalas\_Pazimes | 2 |  |  |
| Izveidošanas datums | Datums | Izveidots |  |  |  |
| Likvidēšanas datums | Datums | Likvidets |  |  |  |

  
### Vides aizsardzības pazīmes [Elementu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDVAPAZIMES |
| Objekta tips | Elementu klase |
| Ģeometrija | Laukums |
| M koordinātes | Nē |
| Z koordinātes | Nē |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Vides aizsardzības klasifikators (VMDVAKLASIFIKATORS)](#vides-aizsardzības-klasifikators-elementu-klase) | [Vides aizsardzības klasifikators](#vides-aizsardzības-klasifikators-elementu-klase).Unikālais identifikators  -> [Vides aizsardzības pazīmes](#vides-aizsardzības-pazīmes-elementu-klase).Sasaiste ar VA\_KLASIFIKATORS | 1:N |
|  [Biotops (VMDBIOTOPI)](#biotops-elementu-klase)  | [Vides aizsardzības pazīmes](#vides-aizsardzības-pazīmes-elementu-klase).Unikālais identifikators  -> [Biotops](#biotops-elementu-klase).Sasaiste ar vides aizsardzības klasifikatora pazīmēm | 1:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Shape | Ģeometrija | Shape |  |  | Jā |
| Unikālais identifikators | Garais skaitlis | VA\_Paz\_ID | 10 |  |  |
| Sasaiste ar VA\_KLASIFIKATORS | Garais skaitlis | VAK\_ID | 10 |  |  |
| Numurs | Teksts | Numurs |  |  |  |
| Izveidošanas datums | Datums | Izveidots |  |  |  |
| Likvidēšanas datums | Datums | Likvidets |  |  |  |

  
VMDDataView [Datu kopa]
-----------------------




|  |  |
| --- | --- |
| Nosaukums DB | VMDDataView |


  

### Ugunsgrēka teritorijas skatījums [Elementu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDUGUNSGREKPOLYVIEW |
| Objekta tips | Elementu klase |
| Ģeometrija | Laukums |
| M koordinātes | Nē |
| Z koordinātes | Nē |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Shape | Ģeometrija | Shape |  |  | Jā |
| Uzsāk dzēšanu | Datums | Usak |  |  |  |
| Trauksmes laiks | Datums | Trauksme |  |  |  |
| Ierobežošanas laiks | Datums | Ierobezo |  |  |  |
| Likvidēšanas laiks | Datums | Likvide |  |  |  |
| Ugunsgrēka atklāšanas veids | [VMD\_093\_UgunsAtklType](#ugunsgrēka-atklāšanas-veids-klasifikators) | UATKL\_TYPE | 3 |  |  |
| Ugunscēloņi | [VMD\_090\_Ugunsceloni](#ugunsgrēka-cēloņi-klasifikators) | Ucel\_Type | 3 |  |  |
| Sasaiste ar UGUNSGREKI | Garais skaitlis | Ug\_ID | 10 |  |  |
| LVM meža zemju platība | Precīzais daļskaitlis | LVM\_MEZ\_PLATIBA | 38 |  |  |
| LVM Jaunaudžu platība | Precīzais daļskaitlis | LVM\_JAUN\_PLATIBA | 38 |  |  |
| LVM Citu meža zemju platība | Precīzais daļskaitlis | LVM\_CITMEZ\_PLATIBA | 38 |  |  |
| LVM Citu nemeža zemju platība | Precīzais daļskaitlis | LVM\_CITNEMEZ\_PLATIBA | 38 |  |  |
| Privātio meža zemju platība | Precīzais daļskaitlis | PRV\_MEZ\_PLATIBA | 38 |  |  |
| Privātio Jaunaudžu platība | Precīzais daļskaitlis | PRV\_JAUN\_PLATIBA | 38 |  |  |
| Privātio citu meža zemju platība | Precīzais daļskaitlis | PRV\_CITMEZ\_PLATIBA | 38 |  |  |
| Privātio Citu nemeža zemju platība | Precīzais daļskaitlis | PRV\_CITNEMEZ\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) meža zemju platība | Precīzais daļskaitlis | VLS\_MEZ\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) Mežu platība | Precīzais daļskaitlis | VLS\_JAUN\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) citu meža zemju platība | Precīzais daļskaitlis | VLS\_CITMEZ\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) Citu nemeža zemju platība | Precīzais daļskaitlis | VLS\_CITNEMEZ\_PLATIBA | 38 |  |  |
| Pašvaldību meža zemju platība | Precīzais daļskaitlis | PSV\_MEZ\_PLATIBA | 38 |  |  |
| Pašvaldību Mežu platība | Precīzais daļskaitlis | PSV\_JAUN\_PLATIBA | 38 |  |  |
| Pašvaldību citu meža zemju platība | Precīzais daļskaitlis | PSV\_CITMEZ\_PLATIBA | 38 |  |  |
| Pašvaldību nemeža zemju platība | Precīzais daļskaitlis | PSV\_CITNEMEZ\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) summārā platība | Precīzais daļskaitlis | VLS\_SUM\_PLATIBA | 38 |  |  |
| Pašvaldību summārā platība | Precīzais daļskaitlis | PSV\_SUM\_PLATIBA | 38 |  |  |
| Privātio summārā platība | Precīzais daļskaitlis | PRV\_SUM\_PLATIBA | 38 |  |  |
| LVM summārā platība | Precīzais daļskaitlis | LVM\_SUM\_PLATIBA | 38 |  |  |
| Mežsaimniecība  | [LVM\_00202\_LVMForestry](#lvm-mežsaimniecības-klasifikators) | LVMForestryCode |  |  |  |
| Kv.apg. - kvartāls | Teksts | BlockKey |  |  |  |
| Nogabala numurs | Īsais skaitlis | CompartmentNumber | 2 |  |  |
| Iecirknis | [LVM\_00201\_LVMDistricts](#lvm-meža-iecirkņi-klasifikators) | LVM\_District\_Code |  |  |  |
| Meža tipa apzīmējums (M) | Teksts | AAT |  |  |  |
| Sugu sastāvs (M) | Teksts | SugasSastavs |  |  |  |
| 1.sugas vecums (M) | Garais skaitlis | A10 | 10 |  |  |
| 1.suga (M) | [LVM\_MEDUS\_00003\_TreeSpecies](#koku-sugu-klasifikators-klasifikators) | S10 | 10 |  |  |

  
### VMD Ugunsgrēka vietas skatījums [Elementu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDUGUNSGREKPOINTVIEW |
| Objekta tips | Elementu klase |
| Ģeometrija | Punkts |
| M koordinātes | Nē |
| Z koordinātes | Nē |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Shape | Ģeometrija | Shape |  |  | Jā |
| Sasaiste ar UGUNSGREKI | Garais skaitlis | Ug\_ID | 10 |  |  |
| Ierobežošanas laiks | Datums | Ierobezo |  |  |  |
| Likvidēšanas laiks | Datums | Likvide |  |  |  |
| Trauksmes laiks | Datums | Trauksme |  |  |  |
| Ugunsgrēka atklāšanas veids | [VMD\_093\_UgunsAtklType](#ugunsgrēka-atklāšanas-veids-klasifikators) | UATKL\_TYPE | 3 |  |  |
| Ugunscēloņi | [VMD\_090\_Ugunsceloni](#ugunsgrēka-cēloņi-klasifikators) | Ucel\_Type | 3 |  |  |
| Uzsāk dzēšanu | Datums | Usak |  |  |  |
| LVM meža zemju platība | Precīzais daļskaitlis | LVM\_MEZ\_PLATIBA | 38 |  |  |
| LVM Jaunaudžu platība | Precīzais daļskaitlis | LVM\_JAUN\_PLATIBA | 38 |  |  |
| LVM Citu meža zemju platība | Precīzais daļskaitlis | LVM\_CITMEZ\_PLATIBA | 38 |  |  |
| LVM Citu nemeža zemju platība | Precīzais daļskaitlis | LVM\_CITNEMEZ\_PLATIBA | 38 |  |  |
| LVM summārā platība | Precīzais daļskaitlis | LVM\_SUM\_PLATIBA | 38 |  |  |
| Privātio meža zemju platība | Precīzais daļskaitlis | PRV\_MEZ\_PLATIBA | 38 |  |  |
| Privātio Jaunaudžu platība | Precīzais daļskaitlis | PRV\_JAUN\_PLATIBA | 38 |  |  |
| Privātio citu meža zemju platība | Precīzais daļskaitlis | PRV\_CITMEZ\_PLATIBA | 38 |  |  |
| Privātio Citu nemeža zemju platība | Precīzais daļskaitlis | PRV\_CITNEMEZ\_PLATIBA | 38 |  |  |
| Privātio summārā platība | Precīzais daļskaitlis | PRV\_SUM\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) meža zemju platība | Precīzais daļskaitlis | VLS\_MEZ\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) Mežu platība | Precīzais daļskaitlis | VLS\_JAUN\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) citu meža zemju platība | Precīzais daļskaitlis | VLS\_CITMEZ\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) Citu nemeža zemju platība | Precīzais daļskaitlis | VLS\_CITNEMEZ\_PLATIBA | 38 |  |  |
| Valsts (ne LVM) summārā platība | Precīzais daļskaitlis | VLS\_SUM\_PLATIBA | 38 |  |  |
| Pašvaldību meža zemju platība | Precīzais daļskaitlis | PSV\_MEZ\_PLATIBA | 38 |  |  |
| Pašvaldību Mežu platība | Precīzais daļskaitlis | PSV\_JAUN\_PLATIBA | 38 |  |  |
| Pašvaldību citu meža zemju platība | Precīzais daļskaitlis | PSV\_CITMEZ\_PLATIBA | 38 |  |  |
| Pašvaldību nemeža zemju platība | Precīzais daļskaitlis | PSV\_CITNEMEZ\_PLATIBA | 38 |  |  |
| Pašvaldību summārā platība | Precīzais daļskaitlis | PSV\_SUM\_PLATIBA | 38 |  |  |
| Mežsaimniecība  | [LVM\_00202\_LVMForestry](#lvm-mežsaimniecības-klasifikators) | LVMForestryCode |  |  |  |
| Kv.apg. - kvartāls | Teksts | BlockKey |  |  |  |
| Nogabala numurs | Īsais skaitlis | CompartmentNumber | 2 |  |  |
| Iecirknis | [LVM\_00201\_LVMDistricts](#lvm-meža-iecirkņi-klasifikators) | LVM\_District\_Code |  |  |  |
| Meža tipa apzīmējums (M) | Teksts | AAT |  |  |  |
| Sugu sastāvs (M) | Teksts | SugasSastavs |  |  |  |
| 1.sugas vecums (M) | Garais skaitlis | A10 | 10 |  |  |
| 1.suga (M) | [LVM\_MEDUS\_00003\_TreeSpecies](#koku-sugu-klasifikators-klasifikators) | S10 | 10 |  |  |

  
Kopējās elementu un objektu klases
----------------------------------

### Biotopa apsaimniekošana [Objektu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDBIOAPSAIMNIEKOSANA |
| Objekta tips | Objektu klase |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Biotops (VMDBIOTOPI)](#biotops-elementu-klase) | [Biotops](#biotops-elementu-klase).Unikālais identifikators  -> [Biotopa apsaimniekošana](#biotopa-apsaimniekošana-objektu-klase).Sasaiste ar BIOTOPI | 1:N |
|  [Biotopa apsaimniekošana – izcērtama suga (VMDBIOIZCERTAMASUGA)](#biotopa-apsaimniekošana--izcērtama-suga-objektu-klase)  | [Biotopa apsaimniekošana](#biotopa-apsaimniekošana-objektu-klase).Unikālais identifikators  -> [Biotopa apsaimniekošana – izcērtama suga](#biotopa-apsaimniekošana--izcērtama-suga-objektu-klase).Sasaiste ar BIOAPSAIMNIEKOSANA | 1:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Unikālais identifikators | Garais skaitlis | BioApsaimniekosana\_ID | 10 |  |  |
| Sasaiste ar BIOTOPI | Garais skaitlis | Bio\_ID | 10 |  |  |
| Bez saimnieciskās darbības? | [VMD\_000\_Boolean](#bināra-izvēle-klasifikators) | Bez\_Darbibas | 1 |  |  |
| Jāsaglabā buferjosla? | [VMD\_000\_Boolean](#bināra-izvēle-klasifikators) | Saglabat\_Buferi | 1 |  |  |
| Neizvākt sausos un kritušos kokus? | [VMD\_000\_Boolean](#bināra-izvēle-klasifikators) | Neizvakt\_Sausos | 1 |  |  |
| Nedrīkst nosusināt? | [VMD\_000\_Boolean](#bināra-izvēle-klasifikators) | Nenosusinat | 1 |  |  |
| Jāizcērt pamežs? | [VMD\_000\_Boolean](#bināra-izvēle-klasifikators) | Jaizcert\_Pamezs | 1 |  |  |
| Piezīmes par apsaimniekošanu | Teksts | Piezimes |  |  |  |

  
### Biotopa apsaimniekošana – izcērtama suga [Objektu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDBIOIZCERTAMASUGA |
| Objekta tips | Objektu klase |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Biotopa apsaimniekošana – sugas izcirtes apjomi (VMDBIOIZCERTAMIAPJOMI)](#biotopa-apsaimniekošana--sugas-izcirtes-apjomi-objektu-klase)  | [Biotopa apsaimniekošana – izcērtama suga](#biotopa-apsaimniekošana--izcērtama-suga-objektu-klase).Unikālais identifikators  -> [Biotopa apsaimniekošana – sugas izcirtes apjomi](#biotopa-apsaimniekošana--sugas-izcirtes-apjomi-objektu-klase).Sasaiste ar BIOIZCERTAMA\_SUGA | 1:N |
|  [Biotopa apsaimniekošana (VMDBIOAPSAIMNIEKOSANA)](#biotopa-apsaimniekošana-objektu-klase) | [Biotopa apsaimniekošana](#biotopa-apsaimniekošana-objektu-klase).Unikālais identifikators  -> [Biotopa apsaimniekošana – izcērtama suga](#biotopa-apsaimniekošana--izcērtama-suga-objektu-klase).Sasaiste ar BIOAPSAIMNIEKOSANA | 1:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Unikālais identifikators | Garais skaitlis | BioIzcertamaSuga\_ID | 10 |  |  |
| Sasaiste ar BIOAPSAIMNIEKOSANA | Garais skaitlis | Aps\_ID | 10 |  |  |
| Izcirtes veids | [VMD\_171\_Bioizcertama\_suga\_Types](#izciršanas-veidi-klasifikators) | BioIzcertamaSuga\_tips | 3 |  |  |
| Skaits | Garais skaitlis | Skaits | 10 |  |  |
| Suga | [VMD\_180\_Koku\_Sugas](#koku-sugas-klasifikators) | KokSug |  |  |  |

  
### Biotopa apsaimniekošana – sugas izcirtes apjomi [Objektu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDBIOIZCERTAMIAPJOMI |
| Objekta tips | Objektu klase |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Biotopa apsaimniekošana – izcērtama suga (VMDBIOIZCERTAMASUGA)](#biotopa-apsaimniekošana--izcērtama-suga-objektu-klase) | [Biotopa apsaimniekošana – izcērtama suga](#biotopa-apsaimniekošana--izcērtama-suga-objektu-klase).Unikālais identifikators  -> [Biotopa apsaimniekošana – sugas izcirtes apjomi](#biotopa-apsaimniekošana--sugas-izcirtes-apjomi-objektu-klase).Sasaiste ar BIOIZCERTAMA\_SUGA | 1:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Sasaiste ar BIOIZCERTAMA\_SUGA | Garais skaitlis | Izc\_ID | 10 |  |  |
| % no paaugas | Īsais skaitlis | No\_Paaugas | 3 |  |  |
| % no II stāva | Īsais skaitlis | No\_2Stava | 3 |  |  |
| % no I stāva | Īsais skaitlis | No\_1Stava | 3 |  |  |
| Izcērtamo apjomu veids | [VMD\_170\_Bioizcertami\_apjomi\_Types](#izcērtamo-apjomu-veidi-klasifikators) | Apjoma\_tipi | 3 |  |  |

  
### Biotopa atslēgas elementi [Objektu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDBIOATSLEGASELEMENTI |
| Objekta tips | Objektu klase |

  
##### Objekta apakštipi




| Vērtība | Apraksts |
| --- | --- |
| 2 | Ar apjomu |
| 1 | Bez apjoma |
| 3 | Ar apjomu un sugu |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Biotops (VMDBIOTOPI)](#biotops-elementu-klase) | [Biotops](#biotops-elementu-klase).Unikālais identifikators  -> [Biotopa atslēgas elementi](#biotopa-atslēgas-elementi-objektu-klase).Sasaiste ar BIOTOPI | 1:N |
|  [Biotopa atslēgas elementu sugas (VMDBIOELEMENTASUGAS)](#biotopa-atslēgas-elementu-sugas-objektu-klase)  | [Biotopa atslēgas elementi](#biotopa-atslēgas-elementi-objektu-klase).Unikālais identifikators  -> [Biotopa atslēgas elementu sugas](#biotopa-atslēgas-elementu-sugas-objektu-klase).Atslēgas identifikators (sasaistei) | 1:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Unikālais identifikators | Garais skaitlis | BioAtslegas\_Elementi\_ID | 10 |  |  |
| Atslēgas elementa apakštips | Garais skaitlis | BioAtslegas\_Elementi\_ST | 10 | 1 |  |
| Sasaiste ar BIOTOPI | Garais skaitlis | Bio\_ID | 10 |  |  |
| Atslēgas elementa veids | [VMD\_030\_Bioelementa\_Veidi\_I](#biotopa-atslēgas-elementu-veidi-bez-apjoma-klasifikators) | ElemV\_Type | 3 |  |  |
| Atslēgas elementa apjoms | [VMD\_035\_Bioelementa\_Veida\_Apjoms](#bioelementu-veida-apjomi-klasifikators) | Apjoms\_Type | 3 |  |  |

  
### Biotopa atslēgas elementu sugas [Objektu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDBIOELEMENTASUGAS |
| Objekta tips | Objektu klase |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Biotopa atslēgas elementi (VMDBIOATSLEGASELEMENTI)](#biotopa-atslēgas-elementi-objektu-klase) | [Biotopa atslēgas elementi](#biotopa-atslēgas-elementi-objektu-klase).Unikālais identifikators  -> [Biotopa atslēgas elementu sugas](#biotopa-atslēgas-elementu-sugas-objektu-klase).Atslēgas identifikators (sasaistei) | 1:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Suga | [VMD\_180\_Koku\_Sugas](#koku-sugas-klasifikators) | KokSug |  |  |  |
| Atslēgas identifikators (sasaistei) | Garais skaitlis | BioAtslegas\_Elementi\_ID | 10 |  | Jā |

  
### Biotopa audzes raksturojumi [Objektu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDBIOAUDZESRAKSTUROJUM |
| Objekta tips | Objektu klase |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Biotops (VMDBIOTOPI)](#biotops-elementu-klase) | [Biotops](#biotops-elementu-klase).Unikālais identifikators  -> [Biotopa audzes raksturojumi](#biotopa-audzes-raksturojumi-objektu-klase).Sasaiste ar BIOTOPI | 1:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Unikālais identifikators | Garais skaitlis | Bioaudzes\_Raksturojumi\_ID | 10 |  |  |
| Sasaiste ar BIOTOPI | Garais skaitlis | Bio\_ID | 10 |  |  |
| procentuālais sugas daudzums | Īsais skaitlis | Koeficients | 2 |  |  |
| Sugas vecums | Īsais skaitlis | Vecums | 3 |  |  |
| Suga | [VMD\_180\_Koku\_Sugas](#koku-sugas-klasifikators) | KokSug |  |  |  |

  
### Biotopa indikatoru sugas [Objektu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDBIOINDIKATORUSUGAS |
| Objekta tips | Objektu klase |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Biotops (VMDBIOTOPI)](#biotops-elementu-klase) | [Biotops](#biotops-elementu-klase).Unikālais identifikators  -> [Biotopa indikatoru sugas](#biotopa-indikatoru-sugas-objektu-klase).Sasaiste ar BIOTOPI | 1:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Unikālais identifikators | Garais skaitlis | BioIndikatoru\_Sugas\_ID | 10 |  |  |
| Sasaiste ar BIOTOPI | Garais skaitlis | Bio\_ID | 10 |  |  |
| Biotopa indikatoru suga | [VMD\_020\_Biosugu\_veidi](#biotopa-indikatoru-sugu-veidi-klasifikators) | BioSug\_Type |  |  |  |
| Biotopa indikatoru sugas sastopamība | [VMD\_021\_BioSugu\_Sastopamiba](#biotopa-indikatoru-sugu-sastopamība-klasifikators) | Sast\_Type |  |  |  |

  
### Biotopa negatīvi traucējumi [Objektu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDBIONEGATIVITRAUC |
| Objekta tips | Objektu klase |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Biotops (VMDBIOTOPI)](#biotops-elementu-klase) | [Biotops](#biotops-elementu-klase).Unikālais identifikators  -> [Biotopa negatīvi traucējumi](#biotopa-negatīvi-traucējumi-objektu-klase).Sasaiste ar BIOTOPI | 1:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Unikālais identifikators | Garais skaitlis | BioNegativiTraucejumi\_ID | 10 |  |  |
| Sasaiste ar BIOTOPI | Garais skaitlis | Bio\_ID | 10 |  |  |
| Biotopa negatīvo traucējumu veids | [VMD\_040\_BioTraucejumu\_Veidi](#biotopa-traucējumu-veidi-klasifikators) | Trauc\_Type |  |  |  |
| Intensitāte | [VMD\_041\_BioTraucējumu\_Intensitate](#Biotopa-traucējumu-intensitāte) | Intensitate | 1 |  |  |

  
### Biotopa īpašās iezīmes [Objektu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDBIOIEZIMES |
| Objekta tips | Objektu klase |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Biotops (VMDBIOTOPI)](#biotops-elementu-klase) | [Biotops](#biotops-elementu-klase).Unikālais identifikators  -> [Biotopa īpašās iezīmes](#biotopa-īpašās-iezīmes-objektu-klase).Sasaiste ar BIOTOPI | 1:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Unikālais identifikators | Garais skaitlis | Bioiezimes\_ID | 10 |  |  |
| Sasaiste ar BIOTOPI | Garais skaitlis | Bio\_ID | 10 |  |  |
| Īpašo iezīmju veids | [VMD\_050\_Bioiezīmju\_veidi](#Biotopa-īpašo-iezīmju-veidi) | IezV\_Type | 2 |  |  |
| Skaits | Īsais skaitlis | Skaits | 2 |  |  |
| Apraksts | Teksts | Apraksts |  |  |  |

  
### Ugunsgrēki [Objektu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDUGUNSGREKI |
| Objekta tips | Objektu klase |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Ugunsgrēku platības uzskaite (VMDUGUNSPLATIBAS)](#ugunsgrēku-platības-uzskaite-objektu-klase)  | [Ugunsgrēki](#ugunsgrēki-objektu-klase).Unikālais identifikators  -> [Ugunsgrēku platības uzskaite](#ugunsgrēku-platības-uzskaite-objektu-klase).Identifikators sasaistei | 1:N |
|  [Ugunsgrēka vieta (VMDUGUNSGREKPOINT)](#ugunsgrēka-vieta-elementu-klase)  | [Ugunsgrēki](#ugunsgrēki-objektu-klase).Unikālais identifikators  -> [Ugunsgrēka vieta](#ugunsgrēka-vieta-elementu-klase).Sasaiste ar UGUNSGREKI | 1:N |
|  [Ugunsgrēka teritorija (VMDUGUNSGREKPOLY)](#ugunsgrēka-teritorija-elementu-klase)  | [Ugunsgrēki](#ugunsgrēki-objektu-klase).Unikālais identifikators  -> [Ugunsgrēka teritorija](#ugunsgrēka-teritorija-elementu-klase).Sasaiste ar UGUNSGREKI | 1:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Unikālais identifikators | Garais skaitlis | Ugunsgreki\_ID | 10 |  |  |
| Ugunscēloņi | [VMD\_090\_Ugunsceloni](#ugunsgrēka-cēloņi-klasifikators) | Ucel\_Type | 3 |  |  |
| Trauksmes laiks | Datums | Trauksme |  |  |  |
| Uzsāk dzēšanu | Datums | Usak |  |  |  |
| Ierobežošanas laiks | Datums | Ierobezo |  |  |  |
| Likvidēšanas laiks | Datums | Likvide |  |  |  |
| Ugunsgrēka atklāšanas veids | [VMD\_093\_UgunsAtklType](#ugunsgrēka-atklāšanas-veids-klasifikators) | UATKL\_TYPE | 3 |  |  |

  
### Ugunsgrēku platības uzskaite [Objektu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDUGUNSPLATIBAS |
| Objekta tips | Objektu klase |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Ugunsgrēki (VMDUGUNSGREKI)](#ugunsgrēki-objektu-klase) | [Ugunsgrēki](#ugunsgrēki-objektu-klase).Unikālais identifikators  -> [Ugunsgrēku platības uzskaite](#ugunsgrēku-platības-uzskaite-objektu-klase).Identifikators sasaistei | 1:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Identifikators sasaistei | Garais skaitlis | Ugunsgreki\_ID | 10 |  |  |
| Ugunscēloņi | [VMD\_091\_Meza\_piederiba](#meža-piederība-klasifikators) | Piedriba |  |  |  |
| Platības zemes veids | [VMD\_092\_UgunsPlatType](#ugunsgrēku-platību-uzskaites-tips-klasifikators) | PlatibaType | 3 |  |  |
| Platība | Precīzais daļskaitlis | Platiba | 7 |  |  |

  
### Vides aizsardzības ierobežojumi [Objektu klase]




|  |  |
| --- | --- |
| Nosaukums DB | VMDVAIEROBEZOJUMI |
| Objekta tips | Objektu klase |

  
##### Relācijas




| Datu objekts | Atslēgas atribūti | Kardinalitāte |
| --- | --- | --- |
|  [Vides aizsardzības klasifikators (VMDVAKLASIFIKATORS)](#vides-aizsardzības-klasifikators-elementu-klase) | [Vides aizsardzības klasifikators](#vides-aizsardzības-klasifikators-elementu-klase).Unikālais identifikators  -> [Vides aizsardzības ierobežojumi](#vides-aizsardzības-ierobežojumi-objektu-klase).Sasaiste ar VA klasifikatoru | 1:N |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| OBJECTID | Identifikators (OID) | OBJECTID |  |  | Jā |
| Ierobežojuma nosaukums | [VMD\_150\_VA\_IerobezojumuVeidi](#vides-aizsardzības-ierobežojumu-veidi-klasifikators) | Nosaukums |  |  |  |
| Sasaiste ar VA klasifikatoru | Garais skaitlis | VAK\_ID | 10 |  |  |

  
### RC\_BIO\_KONC\_LINK [Relāciju klase]




|  |  |
| --- | --- |
| Nosaukums DB | RC\_BIO\_KONC\_LINK |
| Objekta tips | Relāciju klase |

  
##### Datu objekta atribūti




| Nosaukums | Tips | Nosaukums DB | Precizitāte | Noklusētā vērtība | Obligāts |
| --- | --- | --- | --- | --- | --- |
| Biotopa identifikators (sasaistei) | Garais skaitlis | BiotopsFK\_ID | 10 |  | Jā |
| Koncentrācijas vietas identifikators (sasaistei) | Garais skaitlis | BioKoncentracijaFK\_ID | 10 |  | Jā |
| ES Biotops | [VMD\_070\_Biotopi\_ES](#es-biotopa-tips-klasifikators) | Estips\_ID |  |  |  |

  
Klasifikatori
-------------

### Augšanas apstākļu tipi [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_190\_AAT |
| Vērtības | -1 : Nav zināms |
| Izmantots objektu klasēs: | Elementu klase:  [Biotops](#biotops-elementu-klase)  |

   

### Bināra izvēle [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_000\_Boolean |
| Vērtības | -1 : Nav zināms |
|  | 1 : Jā |
|  | 2 : Nē |
|  | 0 : Nav ievadīts |
| Izmantots objektu klasēs: | Elementu klase:  [Biotopu koncentrācijas vieta](#biotopu-koncentrācijas-vieta-elementu-klase)  |
|  | Objektu klase:  [Biotopa apsaimniekošana](#biotopa-apsaimniekošana-objektu-klase)  |
|  | Elementu klase:  [Vides aizsardzības klasifikators](#vides-aizsardzības-klasifikators-elementu-klase)  |

   

### Bioelementu veida apjomi [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_035\_Bioelementa\_Veida\_Apjoms |
| Vērtības | -1 : Nav Zināms |
|  | 1 : 1-5 |
|  | 2 : 6-10 |
|  | 3 : >10 |
|  | 0 : Nav definēts |
| Izmantots objektu klasēs: | Objektu klase:  [Biotopa atslēgas elementi](#biotopa-atslēgas-elementi-objektu-klase)  |

   

### Biokoncentrācijas vietu infrastruktūras tips [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_081\_BioKoncentracija\_Infrastruktura |
| Vērtības | 1 : 1. Priežu meži ar dažādvecuma kokiem |
|  | 2 : 2. Lapu koku pionierfāzes meži |
|  | 3 : 3. Meži ar dažādu pašizrobošanās dinamiku |
|  | 3A : 3a. Slapjie egļu meži un pārējie egļu meži |
|  | 3B : 3b. Slapjie melnalkšņu un platlapju meži |
|  | 3C : 3c. Platlapju meži |
|  | 3AB : 3ab. Slapjie egļu meži un pārējie egļu meži; Slapjie melnalkšņu un platlapju meži |
|  | 3AC : 3ac. Slapjie egļu meži un pārējie egļu meži; Platlapju meži |
|  | 3BC : 3b. Slapjie melnalkšņu un platlapju meži; Platlapju meži |
|  | 3ABC : 3a. Slapjie egļu meži un pārējie egļu meži; Slapjie melnalkšņu un platlapju meži; Platlapju meži |
|  | 4 : 4. Ģeoloģiskās uzbūves nosacītie lineārie biotopi |
| Izmantots objektu klasēs: | Elementu klase:  [Biotopu koncentrācijas vieta](#biotopu-koncentrācijas-vieta-elementu-klase)  |

   

### Biotopa atslēgas elementu veidi (Ar apjomu un sugu) [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_032\_Bioelementa\_Veidi\_III |
| Vērtības | 18 : Bioloģiski veci koki |
|  | 19 : Mazu dimensiju lēni augoši veci koki |
|  | 20 : Saulei atklāti veci platl. koki |
|  | 21 : Krituši koki ar mizu |
|  | 22 : Krituši koki bez mizas |
|  | 23 : Nokrituši kaistoši koki |
|  | 24 : Stumbeņi |
| Izmantots objektu klasēs: | Objektu klase:  [Biotopa atslēgas elementi](#biotopa-atslēgas-elementi-objektu-klase)  |

   

### Biotopa atslēgas elementu veidi (Ar apjomu) [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_031\_Bioelementa\_Veidi\_II |
| Vērtības | 14 : Ciņi ar pamatnēm |
|  | 15 : Koki ar deguma rētām |
|  | 16 : Dobumaini koki |
|  | 17 : Dzeņveidīgo sakalti koki |
| Izmantots objektu klasēs: | Objektu klase:  [Biotopa atslēgas elementi](#biotopa-atslēgas-elementi-objektu-klase)  |

   

### Biotopa atslēgas elementu veidi (Bez apjoma) [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_030\_Bioelementa\_Veidi\_I |
| Vērtības | 1 : Dažādvecuma audze |
|  | 2 : Atvērumu vainaga klājā / lauces |
|  | 3 : Pašizretināšanās |
|  | 4 : Pastāvīgi pārplūstoši klajumi |
|  | 5 : Īslaicīgi pārplūstoši klajumi |
|  | 6 : Mirusi koksne dažās sadal. pakāpēs |
|  | 7 : Mirusi koksne vairākās sadal. pakāpēs |
|  | 8 : Daudz koksnes sēņu / piepju |
|  | 9 : Daudz vecu lazdu |
|  | 10 : Vismaz 4 dažādu sugu platlapji |
|  | 11 : Avotu ietekme |
|  | 12 : Bebru darbības pēdas |
|  | 13 : Dabīgās ūdensteces |
| Izmantots objektu klasēs: | Objektu klase:  [Biotopa atslēgas elementi](#biotopa-atslēgas-elementi-objektu-klase)  |

   

### Biotopa indikatoru sugu sastopamība [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_021\_BioSugu\_Sastopamiba |
| Vērtības | -1 : Nav zināms |
| Izmantots objektu klasēs: | Objektu klase:  [Biotopa indikatoru sugas](#biotopa-indikatoru-sugas-objektu-klase)  |

   

### Biotopa indikatoru sugu veidi [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_020\_Biosugu\_veidi |
| Vērtības | -1 : Nav zināms |
|  | 100 : Cits |
| Izmantots objektu klasēs: | Objektu klase:  [Biotopa indikatoru sugas](#biotopa-indikatoru-sugas-objektu-klase)  |

   

### Biotopa informācijas avoti [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_010\_BioInfoAvoti |
| Vērtības | -1 : Nav zināms |
|  | 1 : Meža valsts reģistrs |
|  | 2 : Topogrāfiskā karte |
|  | 3 : Vietējais mežsargs/iedzīvotājs |
|  | 4 : Citas kartes |
|  | 5 : Citi pētījumi |
|  | 6 : Atrasts nejauši lauku darbu gaitā |
| Izmantots objektu klasēs: | Elementu klase:  [Biotops](#biotops-elementu-klase)  |

   

### Biotopa nosaukumi [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_011\_Bionosaukumi |
| Vērtības | -1 : Nav zināms |
|  | A1 : Skujkoku mežs |
|  | A2 : Mistrots skujkoku-lapukoku mežs |
|  | B1 : Platlapju mežs |
|  | B2 : Apšu mežs |
|  | B3 : Cits lapukoku mežs |
|  | C1 : Slapjš melnalkšņu mežs |
|  | C2 : Egļu un mistrots egļu slapjais mežs |
|  | C3 : Priežu un bērzu slapjais mežs |
|  | C4 : Platlapju slapjais mežs |
|  | D1 : Gravas mežs |
|  | D2 : Nogāzes mežs |
|  | D3 : Krastmalas mežs |
|  | D4 : Avotains mežs |
|  | D5 : Kaļķains skujkoku mežs |
|  | D6 : Kaļķains zāļu purvs vai pļava |
|  | D7 : Purva vai meža mozaīka |
|  | E1 : Dedzis mežs |
|  | E2 : Bioloģiski nozīmīga bebraine |
|  | E3 : Biokoks |
|  | E4 : Vējgāzes mežs |
| Izmantots objektu klasēs: | Elementu klase:  [Biotops](#biotops-elementu-klase)  |

   

### Biotopa traucējumu intensitāte [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_041\_BioTraucējumu\_Intensitate |
| Vērtības | 1 : 1 |
|  | 2 : 2 |
|  | 3 : 3 |
|  | 4 : 4 |
|  | 5 : 5 |
|  | 6 : 6 |
|  | 7 : 7 |
|  | 8 : 8 |
|  | 9 : 9 |
| Izmantots objektu klasēs: | Objektu klase:  [Biotopa negatīvi traucējumi](#biotopa-negatīvi-traucējumi-objektu-klase)  |

   

### Biotopa traucējumu veidi [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_040\_BioTraucejumu\_Veidi |
| Vērtības | -1 : Nav zināms |
| Izmantots objektu klasēs: | Objektu klase:  [Biotopa negatīvi traucējumi](#biotopa-negatīvi-traucējumi-objektu-klase)  |

   

### Biotopa īpašo iezīmju veidi [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_050\_Bioiezīmju\_veidi |
| Vērtības | 1 : Lielas ligzdas |
|  | 2 : Skudru pūžņi |
|  | 3 : Dzīvnieku alas |
|  | 4 : Dzīvnieku "vannas" |
|  | 5 : Laukakmeņi |
|  | 6 : Pamatieža atsegums |
| Izmantots objektu klasēs: | Objektu klase:  [Biotopa īpašās iezīmes](#biotopa-īpašās-iezīmes-objektu-klase)  |

   

### Dzīvnieku sugas [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_100\_DzivnSugas |
| Vērtības | 1 : Alnis |
|  | 2 : Staltbriedis |
|  | 3 : Meža cūka |
|  | 4 : Stirna |
|  | 5 : Bebrs |
|  | 6 : Mednis |
|  | 7 : Rubenis |
|  | 8 : Lūsis |
|  | 9 : Vilks |
| Izmantots objektu klasēs: | Elementu klase:  [VMD dzīvnieku uzskaite](#vmd-dzīvnieku-uzskaite-elementu-klase)  |

   

### ES Biotopa tips [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_070\_Biotopi\_ES |
| Vērtības |  |
| Izmantots objektu klasēs: | Relāciju klase:  [RC\_BIO\_KONC\_LINK](#rc_bio_konc_link-relāciju-klase)  |

   

### Izciršanas veidi [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_171\_Bioizcertama\_suga\_Types |
| Vērtības | 1 : Izciršana |
|  | 2 : Izciršana ap biokokiem |
| Izmantots objektu klasēs: | Objektu klase:  [Biotopa apsaimniekošana – izcērtama suga](#biotopa-apsaimniekošana--izcērtama-suga-objektu-klase)  |

   

### Izcērtamo apjomu veidi [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_170\_Bioizcertami\_apjomi\_Types |
| Vērtības | -1 : Nav zināms |
|  | 1 : 100% platībā |
|  | 2 : 50% un > platībā |
|  | 3 : 50% un mazāk platībā |
|  | 4 : Paņēmienu skaits |
| Izmantots objektu klasēs: | Objektu klase:  [Biotopa apsaimniekošana – sugas izcirtes apjomi](#biotopa-apsaimniekošana--sugas-izcirtes-apjomi-objektu-klase)  |

   

### Koku sugas [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_180\_Koku\_Sugas |
| Vērtības | -1 : Nav zināms |
| Izmantots objektu klasēs: | Objektu klase:  [Biotopa audzes raksturojumi](#biotopa-audzes-raksturojumi-objektu-klase)  |
|  | Objektu klase:  [Biotopa atslēgas elementu sugas](#biotopa-atslēgas-elementu-sugas-objektu-klase)  |
|  | Objektu klase:  [Biotopa apsaimniekošana – izcērtama suga](#biotopa-apsaimniekošana--izcērtama-suga-objektu-klase)  |

   

### Koku sugas [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_161\_KokuSugas |
| Vērtības | -1 : Nav zināms |
|  | 100 : Cits |
| Izmantots objektu klasēs: | - |

   

### Koku sugu klasifikators [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | LVM\_MEDUS\_00003\_TreeSpecies |
| Vērtības | 1 : 01 - Priede |
|  | 3 : 03 - Egle |
|  | 4 : 04 - Bērzs |
|  | 6 : 06 - Melnalksnis |
|  | 8 : 08 - Apse |
|  | 9 : 09 - Baltalksnis |
|  | 10 : 10 - Ozols |
|  | 11 : 11 - Osis |
|  | 12 : 12 - Liepa |
|  | 13 : 13 - Lapegle |
|  | 14 : 14 - Citas priedes |
|  | 15 : 15 - Citas egles |
|  | 16 : 16 - Goba,vīksna |
|  | 17 : 17 - Dižskābardis |
|  | 18 : 18 - Skābardis |
|  | 19 : 19 - Papele |
|  | 20 : 20 - Vītols |
|  | 21 : 21 - Blīgzna |
|  | 22 : 22 - Ciedru priede |
|  | 23 : 23 - Baltegle |
|  | 24 : 24 - Kļava |
|  | 25 : 25 - Saldais ķirsis |
|  | 26 : 26 - Mežābele |
|  | 27 : 27 - Bumbiere |
|  | 28 : 28 - Duglāzija |
|  | 29 : 29 - Īve |
|  | 32 : 32 - Pīlādži |
|  | 35 : 35 - Ievas |
|  | 50 : 50 - Dzeltenā akācija |
|  | 61 : 61 - Citi ozoli |
|  | 62 : 62 - Citas liepas |
|  | 63 : 63 - Citas kļavas |
|  | 64 : 64 - Citi oši |
|  | 65 : 65 - Citas gobas, vīksnas |
|  | 66 : 66 - Riekstkoki |
|  | 67 : 67 - Zirgkastaņi |
|  | 68 : 68 - Hibrīdā apse |
| Izmantots objektu klasēs: | Elementu klase:  [Ugunsgrēka teritorijas skatījums](#ugunsgrēka-teritorijas-skatījums-elementu-klase)  |
|  | Elementu klase:  [Ugunsgrēka teritorija](#ugunsgrēka-teritorija-elementu-klase)  |
|  | Elementu klase:  [Ugunsgrēka vieta](#ugunsgrēka-vieta-elementu-klase)  |
|  | Elementu klase:  [VMD Ugunsgrēka vietas skatījums](#vmd-ugunsgrēka-vietas-skatījums-elementu-klase)  |

   

### Krūmu sugu klasifikators [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | LVM\_MEDUS\_00003k\_ShrubSpecies |
| Vērtības | 30 : 30 - Kārkli |
|  | 31 : 31 - Paegļi |
|  | 33 : 33 - Krūkļi |
|  | 34 : 34 - Lazdas |
|  | 36 : 36 - Sausserži |
|  | 37 : 37 - Irbenes |
|  | 38 : 38 - Segliņi |
|  | 39 : 39 - Ribes-sp. |
|  | 40 : 40 - Korintes |
|  | 41 : 41 - Vilkābeles |
|  | 42 : 42 - Jasmīni |
|  | 43 : 43 - Plūškoki |
|  | 44 : 44 - Spirejas |
|  | 45 : 45 - Ceriņi |
|  | 46 : 46 - Klintenes |
|  | 47 : 47 - Bārbeles |
|  | 48 : 48 - Grimoņi |
|  | 49 : 49 - Rozes |
| Izmantots objektu klasēs: | - |

   

### LVM meža iecirkņi [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | LVM\_00201\_LVMDistricts |
| Vērtības | kodi : Vērtības no slāņa LVMDistrict |
|  | ??? : ??? |
| Izmantots objektu klasēs: | Elementu klase:  [Ugunsgrēka teritorijas skatījums](#ugunsgrēka-teritorijas-skatījums-elementu-klase)  |
|  | Elementu klase:  [Ugunsgrēka teritorija](#ugunsgrēka-teritorija-elementu-klase)  |
|  | Elementu klase:  [Ugunsgrēka vieta](#ugunsgrēka-vieta-elementu-klase)  |
|  | Elementu klase:  [VMD Ugunsgrēka vietas skatījums](#vmd-ugunsgrēka-vietas-skatījums-elementu-klase)  |

   

### LVM mežsaimniecības [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | LVM\_00202\_LVMForestry |
| Vērtības | ! : Vērtības no slāņa LVMForestry |
|  | ? : ??? |
| Izmantots objektu klasēs: | Elementu klase:  [Ugunsgrēka teritorijas skatījums](#ugunsgrēka-teritorijas-skatījums-elementu-klase)  |
|  | Elementu klase:  [Ugunsgrēka teritorija](#ugunsgrēka-teritorija-elementu-klase)  |
|  | Elementu klase:  [Ugunsgrēka vieta](#ugunsgrēka-vieta-elementu-klase)  |
|  | Elementu klase:  [VMD Ugunsgrēka vietas skatījums](#vmd-ugunsgrēka-vietas-skatījums-elementu-klase)  |

   

### Meža piederība [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_091\_Meza\_piederiba |
| Vērtības | PRV : Privātie |
|  | VLS : Valsts (izņemot AS ‘LVM’) |
|  | VAS : AS ‘Latvijas valsts meži’ meži |
|  | PSV : Pašvaldības |
| Izmantots objektu klasēs: | Objektu klase:  [Ugunsgrēku platības uzskaite](#ugunsgrēku-platības-uzskaite-objektu-klase)  |

   

### Putnu sugas [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_013\_StatussVeids |
| Vērtības | -1 : Nav zināms |
|  | P : Paplašinājums (P) |
|  | P30-70 : Paplašinājums (P30-70) |
|  | B : Buferjosla (B) |
|  | BP : Buferjosla (BP) |
|  | B30-70 : Buferjosla (B30-70) |
|  | I : Ieslēgums (I) |
| Izmantots objektu klasēs: | Elementu klase:  [Biotops](#biotops-elementu-klase)  |

   

### Putnu sugas [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_012\_SugasVeids |
| Vērtības | -1 : Nav zināms |
|  | 1 : Dzīvnieks |
|  | 2 : Augs |
|  | 3 : Sūna |
|  | 4 : Ķērpis |
|  | 5 : Sēne |
|  | 6 : IAMB |
|  | 100 : Cits |
| Izmantots objektu klasēs: | Elementu klase:  [Biotops](#biotops-elementu-klase)  |

   

### Pēdu skaita novērtējuma tipi [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_120\_PeduSkaitaTips |
| Vērtības | 1 : Precīzi |
|  | 2 : Neprecīzi |
|  | 3 : Pieņēmums |
| Izmantots objektu klasēs: | - |

   

### TemplateCodedValueDomain [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | TemplateCodedValueDomain |
| Vērtības | 1 : Code1 |
|  | 2 : Code2 |
|  | 3 : Code3 |
| Izmantots objektu klasēs: | - |

   

### Ugunsgrēka atklāšanas veids [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_093\_UgunsAtklType |
| Vērtības | 1 : No torņa |
|  | 2 : Ziņo trešā persona |
|  | 3 : Ziņo VUGD |
| Izmantots objektu klasēs: | Elementu klase:  [Ugunsgrēka teritorijas skatījums](#ugunsgrēka-teritorijas-skatījums-elementu-klase)  |
|  | Objektu klase:  [Ugunsgrēki](#ugunsgrēki-objektu-klase)  |
|  | Elementu klase:  [VMD Ugunsgrēka vietas skatījums](#vmd-ugunsgrēka-vietas-skatījums-elementu-klase)  |

   

### Ugunsgrēka cēloņi [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_090\_Ugunsceloni |
| Vērtības | -1 : Nav zināms |
| Izmantots objektu klasēs: | Elementu klase:  [Ugunsgrēka teritorijas skatījums](#ugunsgrēka-teritorijas-skatījums-elementu-klase)  |
|  | Objektu klase:  [Ugunsgrēki](#ugunsgrēki-objektu-klase)  |
|  | Elementu klase:  [VMD Ugunsgrēka vietas skatījums](#vmd-ugunsgrēka-vietas-skatījums-elementu-klase)  |

   

### Ugunsgrēku platību uzskaites tips [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_092\_UgunsPlatType |
| Vērtības | 1 : Mežu platība |
|  | 2 : Jaunaudžu platība |
|  | 3 : Citu meža zemju platība |
|  | 4 : Citu nemeža zemju platība |
| Izmantots objektu klasēs: | Objektu klase:  [Ugunsgrēku platības uzskaite](#ugunsgrēku-platības-uzskaite-objektu-klase)  |

   

### Vides aizsardzības ierobežojumu veidi [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_150\_VA\_IerobezojumuVeidi |
| Vērtības | -1 : Nav zināms |
| Izmantots objektu klasēs: | Objektu klase:  [Vides aizsardzības ierobežojumi](#vides-aizsardzības-ierobežojumi-objektu-klase)  |

   

### Vērtējums [Klasifikators]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_080\_Vertejums |
| Vērtības | -1 : Nav zināms |
|  | 1 : Zems |
|  | 2 : Vidējs |
|  | 3 : Augsts |
| Izmantots objektu klasēs: | Elementu klase:  [Biotopu koncentrācijas vieta](#biotopu-koncentrācijas-vieta-elementu-klase)  |
|  | Elementu klase:  [Biotops](#biotops-elementu-klase)  |

   

Vērtību robežas
---------------

### Procenti (0-100%) [Vērtību robežas]




|  |  |
| --- | --- |
| Nosaukums DB | VMD\_RD\_Procenti |
| Minimālā vērtība | 1 |
| Maksimālā vērtība | 100 |
| Izmantots objektu klasēs: | - |


  



