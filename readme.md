 body { size: A4; margin: 15mm; padding: 0; } @page { size: A4; margin: 20mm 0mm } tr{ break-inside: avoid !important; } table { break-before: avoid!important; } @media print { #table-of-contents div a::after { content: target-counter(attr(href), page); float: right; font-size: small; position: absolute; right: 30mm; } table { table-layout:fixed } td { word-wrap: break-word; } }

Datu bāzes shēmas apraksts
==========================

Saturs
------

[VMDData](#VMDData)

[Biotops](#VMDBIOTOPI)

[VMD dzīvnieku uzskaite](#VMDAnimalCount)

[Ugunsgrēka teritorija](#VMDUGUNSGREKPOLY)

[Vides aizsardzības klasifikators](#VMDVAKLASIFIKATORS)

[Ugunsgrēka vieta](#VMDUGUNSGREKPOINT)

[Biotopu koncentrācijas vieta](#VMDBIOKONCENTRACIJA)

[Vides aizsardzības pazīmes](#VMDVAPAZIMES)

  

[VMDDataView](#VMDDataView)

[Ugunsgrēka teritorijas skatījums](#VMDUGUNSGREKPOLYVIEW)

[VMD Ugunsgrēka vietas skatījums](#VMDUGUNSGREKPOINTVIEW)

  

[Kopējās elementu un objektu klases](#common_classes)

[Biotopa audzes raksturojumi](#VMDBIOAUDZESRAKSTUROJUM)

[Biotopa indikatoru sugas](#VMDBIOINDIKATORUSUGAS)

[Ugunsgrēki](#VMDUGUNSGREKI)

[Biotopa atslēgas elementi](#VMDBIOATSLEGASELEMENTI)

[Biotopa apsaimniekošana – sugas izcirtes apjomi](#VMDBIOIZCERTAMIAPJOMI)

[Biotopa apsaimniekošana](#VMDBIOAPSAIMNIEKOSANA)

[Ugunsgrēku platības uzskaite](#VMDUGUNSPLATIBAS)

[Biotopa īpašās iezīmes](#VMDBIOIEZIMES)

[Biotopa apsaimniekošana – izcērtama suga](#VMDBIOIZCERTAMASUGA)

[Biotopa atslēgas elementu sugas](#VMDBIOELEMENTASUGAS)

[Biotopa negatīvi traucējumi](#VMDBIONEGATIVITRAUC)

[Vides aizsardzības ierobežojumi](#VMDVAIEROBEZOJUMI)

  

[Klasifikatori](#cvd)

[TemplateCodedValueDomain](#TemplateCodedValueDomain)

[Putnu sugas](#VMD_012_SugasVeids)

[Biotopa indikatoru sugu veidi](#VMD_020_Biosugu_veidi)

[Biokoncentrācijas vietu infrastruktūras tips](#VMD_081_BioKoncentracija_Infrastruktura)

[Koku sugas](#VMD_180_Koku_Sugas)

[ES Biotopa tips](#VMD_070_Biotopi_ES)

[Ugunsgrēka atklāšanas veids](#VMD_093_UgunsAtklType)

[Biotopa traucējumu intensitāte](#VMD_041_BioTraucējumu_Intensitate)

[Krūmu sugu klasifikators](#LVM_MEDUS_00003k_ShrubSpecies)

[Vērtējums](#VMD_080_Vertejums)

[Biotopa informācijas avoti](#VMD_010_BioInfoAvoti)

[Dzīvnieku sugas](#VMD_100_DzivnSugas)

[Biotopa atslēgas elementu veidi (Ar apjomu)](#VMD_031_Bioelementa_Veidi_II)

[Augšanas apstākļu tipi](#VMD_190_AAT)

[LVM mežsaimniecības](#LVM_00202_LVMForestry)

[Izciršanas veidi](#VMD_171_Bioizcertama_suga_Types)

[Pēdu skaita novērtējuma tipi](#VMD_120_PeduSkaitaTips)

[Ugunsgrēka cēloņi](#VMD_090_Ugunsceloni)

[Biotopa īpašo iezīmju veidi](#VMD_050_Bioiezīmju_veidi)

[Biotopa atslēgas elementu veidi (Bez apjoma)](#VMD_030_Bioelementa_Veidi_I)

[LVM meža iecirkņi](#LVM_00201_LVMDistricts)

[Koku sugu klasifikators](#LVM_MEDUS_00003_TreeSpecies)

[Izcērtamo apjomu veidi](#VMD_170_Bioizcertami_apjomi_Types)

[Bioelementu veida apjomi](#VMD_035_Bioelementa_Veida_Apjoms)

[Bināra izvēle](#VMD_000_Boolean)

[Meža piederība](#VMD_091_Meza_piederiba)

[Koku sugas](#VMD_161_KokuSugas)

[Putnu sugas](#VMD_013_StatussVeids)

[Vides aizsardzības ierobežojumu veidi](#VMD_150_VA_IerobezojumuVeidi)

[Biotopa indikatoru sugu sastopamība](#VMD_021_BioSugu_Sastopamiba)

[Biotopa nosaukumi](#VMD_011_Bionosaukumi)

[Biotopa traucējumu veidi](#VMD_040_BioTraucejumu_Veidi)

[Ugunsgrēku platību uzskaites tips](#VMD_092_UgunsPlatType)

[Biotopa atslēgas elementu veidi (Ar apjomu un sugu)](#VMD_032_Bioelementa_Veidi_III)

[Vērtību robežas](#range_domains)

[Procenti (0-100%)](#VMD_RD_Procenti)

VMDData \[Datu kopa\]
---------------------

Nosaukums DB

VMDData

  

### Biotops \[Elementu klase\]

Nosaukums DB

VMDBIOTOPI

Objekta tips

Elementu klase

Ģeometrija

Laukums

M koordinātes

Nē

Z koordinātes

Nē

  

##### Objekta apakštipi

Vērtība

Apraksts

1

Potenciālais meža biotops

2

Dabīgais meža biotops

3

starpaudze meža biotopu koncentrācijas vietā

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Biotopa apsaimniekošana (VMDBIOAPSAIMNIEKOSANA)

  
\[Biotops\].\[Unikālais identifikators\]  
\->  
\[Biotopa apsaimniekošana\].\[Sasaiste ar BIOTOPI\]

1:N

Biotopa atslēgas elementi (VMDBIOATSLEGASELEMENTI)

  
\[Biotops\].\[Unikālais identifikators\]  
\->  
\[Biotopa atslēgas elementi\].\[Sasaiste ar BIOTOPI\]

1:N

Biotopa negatīvi traucējumi (VMDBIONEGATIVITRAUC)

  
\[Biotops\].\[Unikālais identifikators\]  
\->  
\[Biotopa negatīvi traucējumi\].\[Sasaiste ar BIOTOPI\]

1:N

Vides aizsardzības pazīmes (VMDVAPAZIMES)

  
\[Vides aizsardzības pazīmes\].\[Unikālais identifikators\]  
\->  
\[Biotops\].\[Sasaiste ar vides aizsardzības klasifikatora pazīmēm\]

1:N

Biotopa audzes raksturojumi (VMDBIOAUDZESRAKSTUROJUM)

  
\[Biotops\].\[Unikālais identifikators\]  
\->  
\[Biotopa audzes raksturojumi\].\[Sasaiste ar BIOTOPI\]

1:N

Biotopa indikatoru sugas (VMDBIOINDIKATORUSUGAS)

  
\[Biotops\].\[Unikālais identifikators\]  
\->  
\[Biotopa indikatoru sugas\].\[Sasaiste ar BIOTOPI\]

1:N

Biotopa īpašās iezīmes (VMDBIOIEZIMES)

  
\[Biotops\].\[Unikālais identifikators\]  
\->  
\[Biotopa īpašās iezīmes\].\[Sasaiste ar BIOTOPI\]

1:N

Biotopu koncentrācijas vieta (VMDBIOKONCENTRACIJA)

\[Biotops\].\[Unikālais identifikators\]  
\->  
\[RC\_BIO\_KONC\_LINK\].\[Biotopa identifikators (sasaistei)\]  
  
\[Biotopu koncentrācijas vieta\].\[Unikālais identifikators\]  
\->  
\[RC\_BIO\_KONC\_LINK\].\[Koncentrācijas vietas identifikators (sasaistei)\]

N:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Shape

Ģeometrija

Shape

Jā

Unikālais identifikators

Garais skaitlis

Biotops\_ID

10

Apakštipa lauks

Garais skaitlis

Biotops\_ST

10

1

Biotopa Nr.

Teksts

Numurs

Platība (situācijai dabā)

Daļskaitlis

Platiba

6

Audzes sastāva formula (situācijai dabā)

Teksts

Formula

Augšanas apstākļu tips

[VMD\_190\_AAT](#VMD_190_AAT)

\-1: Nav zināms

AAT

2

Sasaiste ar vides aizsardzības klasifikatora pazīmēm

Garais skaitlis

VA\_Paz\_ID

10

Informācijas avots

[VMD\_010\_BioInfoAvoti](#VMD_010_BioInfoAvoti)

\-1: Nav zināms

1: Meža valsts reģistrs

2: Topogrāfiskā karte

3: Vietējais mežsargs/iedzīvotājs

4: Citas kartes

5: Citi pētījumi

6: Atrasts nejauši lauku darbu gaitā

InfoAv

3

Biotopa nosaukums I

[VMD\_011\_Bionosaukumi](#VMD_011_Bionosaukumi)

\-1: Nav zināms

A1: Skujkoku mežs

A2: Mistrots skujkoku-lapukoku mežs

B1: Platlapju mežs

B2: Apšu mežs

B3: Cits lapukoku mežs

C1: Slapjš melnalkšņu mežs

C2: Egļu un mistrots egļu slapjais mežs

C3: Priežu un bērzu slapjais mežs

...

Nosaukums1

Biotopa nosaukums II

[VMD\_011\_Bionosaukumi](#VMD_011_Bionosaukumi)

\-1: Nav zināms

A1: Skujkoku mežs

A2: Mistrots skujkoku-lapukoku mežs

B1: Platlapju mežs

B2: Apšu mežs

B3: Cits lapukoku mežs

C1: Slapjš melnalkšņu mežs

C2: Egļu un mistrots egļu slapjais mežs

C3: Priežu un bērzu slapjais mežs

...

Nosaukums2

Bioloģiskās daudzveidības apraksts

Teksts

Daudzveidiba

Piezīmes

Teksts

Piezimes

Apsekošanas datums

Datums

Datums

Persona, kas veica apsekošanu

Teksts

Apsekoja

Audzes status

[VMD\_013\_StatussVeids](#VMD_013_StatussVeids)

\-1: Nav zināms

P: Paplašinājums (P)

P30-70: Paplašinājums (P30-70)

B: Buferjosla (B)

BP: Buferjosla (BP)

B30-70: Buferjosla (B30-70)

I: Ieslēgums (I)

SA\_Statuss

Audzes suga

Īsais skaitlis

SA\_Suga

3

Audzes ierobežojumu intensitāte

Īsais skaitlis

SA\_Intensitate

3

Piezīmes, suga

Teksts

SA\_Suga\_Piezimes

DMB raksturīgo ekoloģisko rādītāju sasniegšanas laiks

Īsais skaitlis

SA\_Sasniegsana

3

Novērtējums par audzes piemērotību paplašinājumiem

[VMD\_080\_Vertejums](#VMD_080_Vertejums)

\-1: Nav zināms

1: Zems

2: Vidējs

3: Augsts

SA\_Piemerotiba

3

Apsaimniekošanas apraksts

Teksts

SA\_Apsaimn

  

### VMD dzīvnieku uzskaite \[Elementu klase\]

Nosaukums DB

VMDAnimalCount

Objekta tips

Elementu klase

Ģeometrija

Laukums

M koordinātes

Nē

Z koordinātes

Nē

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Shape

Ģeometrija

Shape

Jā

Uzskaites vienība

Teksts

Uzsk\_vien

Nosaukums

Teksts

Nosaukums

Dzīvnieku suga

[VMD\_100\_DzivnSugas](#VMD_100_DzivnSugas)

1: Alnis

2: Staltbriedis

3: Meža cūka

4: Stirna

5: Bebrs

6: Mednis

7: Rubenis

8: Lūsis

9: Vilks

...

Suga

2

Uzskaites vērtība

Daļskaitlis

UzskVertiba

5

  

### Ugunsgrēka teritorija \[Elementu klase\]

Nosaukums DB

VMDUGUNSGREKPOLY

Objekta tips

Elementu klase

Ģeometrija

Laukums

M koordinātes

Nē

Z koordinātes

Nē

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Ugunsgrēki (VMDUGUNSGREKI)

  
\[Ugunsgrēki\].\[Unikālais identifikators\]  
\->  
\[Ugunsgrēka teritorija\].\[Sasaiste ar UGUNSGREKI\]

1:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Shape

Ģeometrija

Shape

Jā

Sasaiste ar UGUNSGREKI

Garais skaitlis

Ug\_ID

10

Mežsaimniecība

[LVM\_00202\_LVMForestry](#LVM_00202_LVMForestry)

!: Vērtības no slāņa LVMForestry

?: ???

LVMForestryCode

Kv.apg. - kvartāls

Teksts

BlockKey

Nogabala numurs

Īsais skaitlis

CompartmentNumber

2

Iecirknis

[LVM\_00201\_LVMDistricts](#LVM_00201_LVMDistricts)

kodi: Vērtības no slāņa LVMDistrict

???: ???

LVM\_District\_Code

Sugu sastāvs (M)

Teksts

SugasSastavs

Meža tipa apzīmējums (M)

Teksts

AAT

1.sugas vecums (M)

Garais skaitlis

A10

10

1.suga (M)

[LVM\_MEDUS\_00003\_TreeSpecies](#LVM_MEDUS_00003_TreeSpecies)

1: 01 - Priede

3: 03 - Egle

4: 04 - Bērzs

6: 06 - Melnalksnis

8: 08 - Apse

9: 09 - Baltalksnis

10: 10 - Ozols

11: 11 - Osis

12: 12 - Liepa

...

S10

10

  

### Vides aizsardzības klasifikators \[Elementu klase\]

Nosaukums DB

VMDVAKLASIFIKATORS

Objekta tips

Elementu klase

Ģeometrija

Laukums

M koordinātes

Nē

Z koordinātes

Nē

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Vides aizsardzības ierobežojumi (VMDVAIEROBEZOJUMI)

  
\[Vides aizsardzības klasifikators\].\[Unikālais identifikators\]  
\->  
\[Vides aizsardzības ierobežojumi\].\[Sasaiste ar VA klasifikatoru\]

1:N

Vides aizsardzības pazīmes (VMDVAPAZIMES)

  
\[Vides aizsardzības klasifikators\].\[Unikālais identifikators\]  
\->  
\[Vides aizsardzības pazīmes\].\[Sasaiste ar VA\_KLASIFIKATORS\]

1:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Shape

Ģeometrija

Shape

Jā

Unikālais identifikators

Garais skaitlis

VAK\_ID

10

Hierarhijas sasaiste

Garais skaitlis

Parent\_VAK\_ID

10

Kods

Teksts

Kods

Nosaukums

Teksts

Nosaukums

Vai atļauts reģistrēt unikālās aizsardzības pazīmes?

[VMD\_000\_Boolean](#VMD_000_Boolean)

\-1: Nav zināms

1: Jā

2: Nē

0: Nav ievadīts

Unikalas\_Pazimes

2

Izveidošanas datums

Datums

Izveidots

Likvidēšanas datums

Datums

Likvidets

  

### Ugunsgrēka vieta \[Elementu klase\]

Nosaukums DB

VMDUGUNSGREKPOINT

Objekta tips

Elementu klase

Ģeometrija

Punkts

M koordinātes

Nē

Z koordinātes

Nē

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Ugunsgrēki (VMDUGUNSGREKI)

  
\[Ugunsgrēki\].\[Unikālais identifikators\]  
\->  
\[Ugunsgrēka vieta\].\[Sasaiste ar UGUNSGREKI\]

1:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Shape

Ģeometrija

Shape

Jā

Simbola leņķis

Daļskaitlis

Angval

5

Sasaiste ar UGUNSGREKI

Garais skaitlis

Ug\_ID

10

Mežsaimniecība

[LVM\_00202\_LVMForestry](#LVM_00202_LVMForestry)

!: Vērtības no slāņa LVMForestry

?: ???

LVMForestryCode

Kv.apg. - kvartāls

Teksts

BlockKey

Nogabala numurs

Īsais skaitlis

CompartmentNumber

2

Iecirknis

[LVM\_00201\_LVMDistricts](#LVM_00201_LVMDistricts)

kodi: Vērtības no slāņa LVMDistrict

???: ???

LVM\_District\_Code

Meža tipa apzīmējums (M)

Teksts

AAT

Sugu sastāvs (M)

Teksts

SugasSastavs

1.sugas vecums (M)

Garais skaitlis

A10

10

1.suga (M)

[LVM\_MEDUS\_00003\_TreeSpecies](#LVM_MEDUS_00003_TreeSpecies)

1: 01 - Priede

3: 03 - Egle

4: 04 - Bērzs

6: 06 - Melnalksnis

8: 08 - Apse

9: 09 - Baltalksnis

10: 10 - Ozols

11: 11 - Osis

12: 12 - Liepa

...

S10

10

  

### Biotopu koncentrācijas vieta \[Elementu klase\]

Nosaukums DB

VMDBIOKONCENTRACIJA

Objekta tips

Elementu klase

Ģeometrija

Laukums

M koordinātes

Nē

Z koordinātes

Nē

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Biotops (VMDBIOTOPI)

\[Biotops\].\[Unikālais identifikators\]  
\->  
\[RC\_BIO\_KONC\_LINK\].\[Biotopa identifikators (sasaistei)\]  
  
\[Biotopu koncentrācijas vieta\].\[Unikālais identifikators\]  
\->  
\[RC\_BIO\_KONC\_LINK\].\[Koncentrācijas vietas identifikators (sasaistei)\]

N:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Shape

Ģeometrija

Shape

Jā

Unikālais identifikators

Garais skaitlis

BioKoncentracija\_ID

10

Koncentrācijas Nr.

Teksts

Numurs

Infrastruktūras tips

[VMD\_081\_BioKoncentracija\_Infrastruktura](#VMD_081_BioKoncentracija_Infrastruktura)

1: 1. Priežu meži ar dažādvecuma kokiem

2: 2. Lapu koku pionierfāzes meži

3: 3. Meži ar dažādu pašizrobošanās dinamiku

3A: 3a. Slapjie egļu meži un pārējie egļu meži

3B: 3b. Slapjie melnalkšņu un platlapju meži

3C: 3c. Platlapju meži

3AB: 3ab. Slapjie egļu meži un pārējie egļu meži; Slapjie melnalkšņu un platlapju meži

3AC: 3ac. Slapjie egļu meži un pārējie egļu meži; Platlapju meži

3BC: 3b. Slapjie melnalkšņu un platlapju meži; Platlapju meži

...

Infrastruktura

Atrodas nozīmīgajā apvidū?

[VMD\_000\_Boolean](#VMD_000_Boolean)

\-1: Nav zināms

1: Jā

2: Nē

0: Nav ievadīts

Nozimigs\_Apvidus

1

Nav nosusināts

Garais skaitlis

NT\_Nesusinats

3

Nosusināts, bet sistēma nedarbojas

Garais skaitlis

NT\_SusNeDarb

3

Nosusināšana darbojas

Garais skaitlis

NT\_SusDarb

3

Biotopu koncentrācijas vietas vērtējums?

[VMD\_080\_Vertejums](#VMD_080_Vertejums)

\-1: Nav zināms

1: Zems

2: Vidējs

3: Augsts

Konc\_Vert

1

Nosusināšanas ilglaicīgā negatīvā ietekme uz bioloģiskajām vērtībām

[VMD\_080\_Vertejums](#VMD_080_Vertejums)

\-1: Nav zināms

1: Zems

2: Vidējs

3: Augsts

Sus\_Ietekme

1

Ietekme, slēdzot nosusināšanas sistēmu

[VMD\_080\_Vertejums](#VMD_080_Vertejums)

\-1: Nav zināms

1: Zems

2: Vidējs

3: Augsts

SusSledz\_Ietekme

1

Ieguvums

Teksts

Ieguvums

Piezīmes

Teksts

Piezimes

Apsekoja

Teksts

Apsekoja

Datums

Datums

Datums

  

### Vides aizsardzības pazīmes \[Elementu klase\]

Nosaukums DB

VMDVAPAZIMES

Objekta tips

Elementu klase

Ģeometrija

Laukums

M koordinātes

Nē

Z koordinātes

Nē

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Vides aizsardzības klasifikators (VMDVAKLASIFIKATORS)

  
\[Vides aizsardzības klasifikators\].\[Unikālais identifikators\]  
\->  
\[Vides aizsardzības pazīmes\].\[Sasaiste ar VA\_KLASIFIKATORS\]

1:N

Biotops (VMDBIOTOPI)

  
\[Vides aizsardzības pazīmes\].\[Unikālais identifikators\]  
\->  
\[Biotops\].\[Sasaiste ar vides aizsardzības klasifikatora pazīmēm\]

1:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Shape

Ģeometrija

Shape

Jā

Unikālais identifikators

Garais skaitlis

VA\_Paz\_ID

10

Sasaiste ar VA\_KLASIFIKATORS

Garais skaitlis

VAK\_ID

10

Numurs

Teksts

Numurs

Izveidošanas datums

Datums

Izveidots

Likvidēšanas datums

Datums

Likvidets

  

VMDDataView \[Datu kopa\]
-------------------------

Nosaukums DB

VMDDataView

  

### Ugunsgrēka teritorijas skatījums \[Elementu klase\]

Nosaukums DB

VMDUGUNSGREKPOLYVIEW

Objekta tips

Elementu klase

Ģeometrija

Laukums

M koordinātes

Nē

Z koordinātes

Nē

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Shape

Ģeometrija

Shape

Jā

Uzsāk dzēšanu

Datums

Usak

Trauksmes laiks

Datums

Trauksme

Ierobežošanas laiks

Datums

Ierobezo

Likvidēšanas laiks

Datums

Likvide

Ugunsgrēka atklāšanas veids

[VMD\_093\_UgunsAtklType](#VMD_093_UgunsAtklType)

1: No torņa

2: Ziņo trešā persona

3: Ziņo VUGD

UATKL\_TYPE

3

Ugunscēloņi

[VMD\_090\_Ugunsceloni](#VMD_090_Ugunsceloni)

\-1: Nav zināms

Ucel\_Type

3

Sasaiste ar UGUNSGREKI

Garais skaitlis

Ug\_ID

10

LVM meža zemju platība

Precīzais daļskaitlis

LVM\_MEZ\_PLATIBA

38

LVM Jaunaudžu platība

Precīzais daļskaitlis

LVM\_JAUN\_PLATIBA

38

LVM Citu meža zemju platība

Precīzais daļskaitlis

LVM\_CITMEZ\_PLATIBA

38

LVM Citu nemeža zemju platība

Precīzais daļskaitlis

LVM\_CITNEMEZ\_PLATIBA

38

Privātio meža zemju platība

Precīzais daļskaitlis

PRV\_MEZ\_PLATIBA

38

Privātio Jaunaudžu platība

Precīzais daļskaitlis

PRV\_JAUN\_PLATIBA

38

Privātio citu meža zemju platība

Precīzais daļskaitlis

PRV\_CITMEZ\_PLATIBA

38

Privātio Citu nemeža zemju platība

Precīzais daļskaitlis

PRV\_CITNEMEZ\_PLATIBA

38

Valsts (ne LVM) meža zemju platība

Precīzais daļskaitlis

VLS\_MEZ\_PLATIBA

38

Valsts (ne LVM) Mežu platība

Precīzais daļskaitlis

VLS\_JAUN\_PLATIBA

38

Valsts (ne LVM) citu meža zemju platība

Precīzais daļskaitlis

VLS\_CITMEZ\_PLATIBA

38

Valsts (ne LVM) Citu nemeža zemju platība

Precīzais daļskaitlis

VLS\_CITNEMEZ\_PLATIBA

38

Pašvaldību meža zemju platība

Precīzais daļskaitlis

PSV\_MEZ\_PLATIBA

38

Pašvaldību Mežu platība

Precīzais daļskaitlis

PSV\_JAUN\_PLATIBA

38

Pašvaldību citu meža zemju platība

Precīzais daļskaitlis

PSV\_CITMEZ\_PLATIBA

38

Pašvaldību nemeža zemju platība

Precīzais daļskaitlis

PSV\_CITNEMEZ\_PLATIBA

38

Valsts (ne LVM) summārā platība

Precīzais daļskaitlis

VLS\_SUM\_PLATIBA

38

Pašvaldību summārā platība

Precīzais daļskaitlis

PSV\_SUM\_PLATIBA

38

Privātio summārā platība

Precīzais daļskaitlis

PRV\_SUM\_PLATIBA

38

LVM summārā platība

Precīzais daļskaitlis

LVM\_SUM\_PLATIBA

38

Mežsaimniecība

[LVM\_00202\_LVMForestry](#LVM_00202_LVMForestry)

!: Vērtības no slāņa LVMForestry

?: ???

LVMForestryCode

Kv.apg. - kvartāls

Teksts

BlockKey

Nogabala numurs

Īsais skaitlis

CompartmentNumber

2

Iecirknis

[LVM\_00201\_LVMDistricts](#LVM_00201_LVMDistricts)

kodi: Vērtības no slāņa LVMDistrict

???: ???

LVM\_District\_Code

Meža tipa apzīmējums (M)

Teksts

AAT

Sugu sastāvs (M)

Teksts

SugasSastavs

1.sugas vecums (M)

Garais skaitlis

A10

10

1.suga (M)

[LVM\_MEDUS\_00003\_TreeSpecies](#LVM_MEDUS_00003_TreeSpecies)

1: 01 - Priede

3: 03 - Egle

4: 04 - Bērzs

6: 06 - Melnalksnis

8: 08 - Apse

9: 09 - Baltalksnis

10: 10 - Ozols

11: 11 - Osis

12: 12 - Liepa

...

S10

10

  

### VMD Ugunsgrēka vietas skatījums \[Elementu klase\]

Nosaukums DB

VMDUGUNSGREKPOINTVIEW

Objekta tips

Elementu klase

Ģeometrija

Punkts

M koordinātes

Nē

Z koordinātes

Nē

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Shape

Ģeometrija

Shape

Jā

Sasaiste ar UGUNSGREKI

Garais skaitlis

Ug\_ID

10

Ierobežošanas laiks

Datums

Ierobezo

Likvidēšanas laiks

Datums

Likvide

Trauksmes laiks

Datums

Trauksme

Ugunsgrēka atklāšanas veids

[VMD\_093\_UgunsAtklType](#VMD_093_UgunsAtklType)

1: No torņa

2: Ziņo trešā persona

3: Ziņo VUGD

UATKL\_TYPE

3

Ugunscēloņi

[VMD\_090\_Ugunsceloni](#VMD_090_Ugunsceloni)

\-1: Nav zināms

Ucel\_Type

3

Uzsāk dzēšanu

Datums

Usak

LVM meža zemju platība

Precīzais daļskaitlis

LVM\_MEZ\_PLATIBA

38

LVM Jaunaudžu platība

Precīzais daļskaitlis

LVM\_JAUN\_PLATIBA

38

LVM Citu meža zemju platība

Precīzais daļskaitlis

LVM\_CITMEZ\_PLATIBA

38

LVM Citu nemeža zemju platība

Precīzais daļskaitlis

LVM\_CITNEMEZ\_PLATIBA

38

LVM summārā platība

Precīzais daļskaitlis

LVM\_SUM\_PLATIBA

38

Privātio meža zemju platība

Precīzais daļskaitlis

PRV\_MEZ\_PLATIBA

38

Privātio Jaunaudžu platība

Precīzais daļskaitlis

PRV\_JAUN\_PLATIBA

38

Privātio citu meža zemju platība

Precīzais daļskaitlis

PRV\_CITMEZ\_PLATIBA

38

Privātio Citu nemeža zemju platība

Precīzais daļskaitlis

PRV\_CITNEMEZ\_PLATIBA

38

Privātio summārā platība

Precīzais daļskaitlis

PRV\_SUM\_PLATIBA

38

Valsts (ne LVM) meža zemju platība

Precīzais daļskaitlis

VLS\_MEZ\_PLATIBA

38

Valsts (ne LVM) Mežu platība

Precīzais daļskaitlis

VLS\_JAUN\_PLATIBA

38

Valsts (ne LVM) citu meža zemju platība

Precīzais daļskaitlis

VLS\_CITMEZ\_PLATIBA

38

Valsts (ne LVM) Citu nemeža zemju platība

Precīzais daļskaitlis

VLS\_CITNEMEZ\_PLATIBA

38

Valsts (ne LVM) summārā platība

Precīzais daļskaitlis

VLS\_SUM\_PLATIBA

38

Pašvaldību meža zemju platība

Precīzais daļskaitlis

PSV\_MEZ\_PLATIBA

38

Pašvaldību Mežu platība

Precīzais daļskaitlis

PSV\_JAUN\_PLATIBA

38

Pašvaldību citu meža zemju platība

Precīzais daļskaitlis

PSV\_CITMEZ\_PLATIBA

38

Pašvaldību nemeža zemju platība

Precīzais daļskaitlis

PSV\_CITNEMEZ\_PLATIBA

38

Pašvaldību summārā platība

Precīzais daļskaitlis

PSV\_SUM\_PLATIBA

38

Mežsaimniecība

[LVM\_00202\_LVMForestry](#LVM_00202_LVMForestry)

!: Vērtības no slāņa LVMForestry

?: ???

LVMForestryCode

Kv.apg. - kvartāls

Teksts

BlockKey

Nogabala numurs

Īsais skaitlis

CompartmentNumber

2

Iecirknis

[LVM\_00201\_LVMDistricts](#LVM_00201_LVMDistricts)

kodi: Vērtības no slāņa LVMDistrict

???: ???

LVM\_District\_Code

Meža tipa apzīmējums (M)

Teksts

AAT

Sugu sastāvs (M)

Teksts

SugasSastavs

1.sugas vecums (M)

Garais skaitlis

A10

10

1.suga (M)

[LVM\_MEDUS\_00003\_TreeSpecies](#LVM_MEDUS_00003_TreeSpecies)

1: 01 - Priede

3: 03 - Egle

4: 04 - Bērzs

6: 06 - Melnalksnis

8: 08 - Apse

9: 09 - Baltalksnis

10: 10 - Ozols

11: 11 - Osis

12: 12 - Liepa

...

S10

10

  

Kopējās elementu un objektu klases
----------------------------------

### Biotopa audzes raksturojumi \[Objektu klase\]

Nosaukums DB

VMDBIOAUDZESRAKSTUROJUM

Objekta tips

Objektu klase

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Biotops (VMDBIOTOPI)

  
\[Biotops\].\[Unikālais identifikators\]  
\->  
\[Biotopa audzes raksturojumi\].\[Sasaiste ar BIOTOPI\]

1:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Unikālais identifikators

Garais skaitlis

Bioaudzes\_Raksturojumi\_ID

10

Sasaiste ar BIOTOPI

Garais skaitlis

Bio\_ID

10

procentuālais sugas daudzums

Īsais skaitlis

Koeficients

2

Sugas vecums

Īsais skaitlis

Vecums

3

Suga

[VMD\_180\_Koku\_Sugas](#VMD_180_Koku_Sugas)

\-1: Nav zināms

KokSug

  

### Biotopa indikatoru sugas \[Objektu klase\]

Nosaukums DB

VMDBIOINDIKATORUSUGAS

Objekta tips

Objektu klase

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Biotops (VMDBIOTOPI)

  
\[Biotops\].\[Unikālais identifikators\]  
\->  
\[Biotopa indikatoru sugas\].\[Sasaiste ar BIOTOPI\]

1:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Unikālais identifikators

Garais skaitlis

BioIndikatoru\_Sugas\_ID

10

Sasaiste ar BIOTOPI

Garais skaitlis

Bio\_ID

10

Biotopa indikatoru suga

[VMD\_020\_Biosugu\_veidi](#VMD_020_Biosugu_veidi)

\-1: Nav zināms

100: Cits

BioSug\_Type

Biotopa indikatoru sugas sastopamība

[VMD\_021\_BioSugu\_Sastopamiba](#VMD_021_BioSugu_Sastopamiba)

\-1: Nav zināms

Sast\_Type

  

### Ugunsgrēki \[Objektu klase\]

Nosaukums DB

VMDUGUNSGREKI

Objekta tips

Objektu klase

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Ugunsgrēka vieta (VMDUGUNSGREKPOINT)

  
\[Ugunsgrēki\].\[Unikālais identifikators\]  
\->  
\[Ugunsgrēka vieta\].\[Sasaiste ar UGUNSGREKI\]

1:N

Ugunsgrēka teritorija (VMDUGUNSGREKPOLY)

  
\[Ugunsgrēki\].\[Unikālais identifikators\]  
\->  
\[Ugunsgrēka teritorija\].\[Sasaiste ar UGUNSGREKI\]

1:N

Ugunsgrēku platības uzskaite (VMDUGUNSPLATIBAS)

  
\[Ugunsgrēki\].\[Unikālais identifikators\]  
\->  
\[Ugunsgrēku platības uzskaite\].\[Identifikators sasaistei\]

1:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Unikālais identifikators

Garais skaitlis

Ugunsgreki\_ID

10

Ugunscēloņi

[VMD\_090\_Ugunsceloni](#VMD_090_Ugunsceloni)

\-1: Nav zināms

Ucel\_Type

3

Trauksmes laiks

Datums

Trauksme

Uzsāk dzēšanu

Datums

Usak

Ierobežošanas laiks

Datums

Ierobezo

Likvidēšanas laiks

Datums

Likvide

Ugunsgrēka atklāšanas veids

[VMD\_093\_UgunsAtklType](#VMD_093_UgunsAtklType)

1: No torņa

2: Ziņo trešā persona

3: Ziņo VUGD

UATKL\_TYPE

3

  

### Biotopa atslēgas elementi \[Objektu klase\]

Nosaukums DB

VMDBIOATSLEGASELEMENTI

Objekta tips

Objektu klase

  

##### Objekta apakštipi

Vērtība

Apraksts

3

Ar apjomu un sugu

2

Ar apjomu

1

Bez apjoma

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Biotops (VMDBIOTOPI)

  
\[Biotops\].\[Unikālais identifikators\]  
\->  
\[Biotopa atslēgas elementi\].\[Sasaiste ar BIOTOPI\]

1:N

Biotopa atslēgas elementu sugas (VMDBIOELEMENTASUGAS)

  
\[Biotopa atslēgas elementi\].\[Unikālais identifikators\]  
\->  
\[Biotopa atslēgas elementu sugas\].\[Atslēgas identifikators (sasaistei)\]

1:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Unikālais identifikators

Garais skaitlis

BioAtslegas\_Elementi\_ID

10

Atslēgas elementa apakštips

Garais skaitlis

BioAtslegas\_Elementi\_ST

10

1

Sasaiste ar BIOTOPI

Garais skaitlis

Bio\_ID

10

Atslēgas elementa veids

[VMD\_030\_Bioelementa\_Veidi\_I](#VMD_030_Bioelementa_Veidi_I)

1: Dažādvecuma audze

2: Atvērumu vainaga klājā / lauces

3: Pašizretināšanās

4: Pastāvīgi pārplūstoši klajumi

5: Īslaicīgi pārplūstoši klajumi

6: Mirusi koksne dažās sadal. pakāpēs

7: Mirusi koksne vairākās sadal. pakāpēs

8: Daudz koksnes sēņu / piepju

9: Daudz vecu lazdu

...

ElemV\_Type

3

Atslēgas elementa apjoms

[VMD\_035\_Bioelementa\_Veida\_Apjoms](#VMD_035_Bioelementa_Veida_Apjoms)

\-1: Nav Zināms

1: 1-5

2: 6-10

3: >10

0: Nav definēts

Apjoms\_Type

3

  

### Biotopa apsaimniekošana – sugas izcirtes apjomi \[Objektu klase\]

Nosaukums DB

VMDBIOIZCERTAMIAPJOMI

Objekta tips

Objektu klase

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Biotopa apsaimniekošana – izcērtama suga (VMDBIOIZCERTAMASUGA)

  
\[Biotopa apsaimniekošana – izcērtama suga\].\[Unikālais identifikators\]  
\->  
\[Biotopa apsaimniekošana – sugas izcirtes apjomi\].\[Sasaiste ar BIOIZCERTAMA\_SUGA\]

1:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Sasaiste ar BIOIZCERTAMA\_SUGA

Garais skaitlis

Izc\_ID

10

% no paaugas

Īsais skaitlis

No\_Paaugas

3

% no II stāva

Īsais skaitlis

No\_2Stava

3

% no I stāva

Īsais skaitlis

No\_1Stava

3

Izcērtamo apjomu veids

[VMD\_170\_Bioizcertami\_apjomi\_Types](#VMD_170_Bioizcertami_apjomi_Types)

\-1: Nav zināms

1: 100% platībā

2: 50% un > platībā

3: 50% un mazāk platībā

4: Paņēmienu skaits

Apjoma\_tipi

3

  

### Biotopa apsaimniekošana \[Objektu klase\]

Nosaukums DB

VMDBIOAPSAIMNIEKOSANA

Objekta tips

Objektu klase

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Biotops (VMDBIOTOPI)

  
\[Biotops\].\[Unikālais identifikators\]  
\->  
\[Biotopa apsaimniekošana\].\[Sasaiste ar BIOTOPI\]

1:N

Biotopa apsaimniekošana – izcērtama suga (VMDBIOIZCERTAMASUGA)

  
\[Biotopa apsaimniekošana\].\[Unikālais identifikators\]  
\->  
\[Biotopa apsaimniekošana – izcērtama suga\].\[Sasaiste ar BIOAPSAIMNIEKOSANA\]

1:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Unikālais identifikators

Garais skaitlis

BioApsaimniekosana\_ID

10

Sasaiste ar BIOTOPI

Garais skaitlis

Bio\_ID

10

Bez saimnieciskās darbības?

[VMD\_000\_Boolean](#VMD_000_Boolean)

\-1: Nav zināms

1: Jā

2: Nē

0: Nav ievadīts

Bez\_Darbibas

1

Jāsaglabā buferjosla?

[VMD\_000\_Boolean](#VMD_000_Boolean)

\-1: Nav zināms

1: Jā

2: Nē

0: Nav ievadīts

Saglabat\_Buferi

1

Neizvākt sausos un kritušos kokus?

[VMD\_000\_Boolean](#VMD_000_Boolean)

\-1: Nav zināms

1: Jā

2: Nē

0: Nav ievadīts

Neizvakt\_Sausos

1

Nedrīkst nosusināt?

[VMD\_000\_Boolean](#VMD_000_Boolean)

\-1: Nav zināms

1: Jā

2: Nē

0: Nav ievadīts

Nenosusinat

1

Jāizcērt pamežs?

[VMD\_000\_Boolean](#VMD_000_Boolean)

\-1: Nav zināms

1: Jā

2: Nē

0: Nav ievadīts

Jaizcert\_Pamezs

1

Piezīmes par apsaimniekošanu

Teksts

Piezimes

  

### Ugunsgrēku platības uzskaite \[Objektu klase\]

Nosaukums DB

VMDUGUNSPLATIBAS

Objekta tips

Objektu klase

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Ugunsgrēki (VMDUGUNSGREKI)

  
\[Ugunsgrēki\].\[Unikālais identifikators\]  
\->  
\[Ugunsgrēku platības uzskaite\].\[Identifikators sasaistei\]

1:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Identifikators sasaistei

Garais skaitlis

Ugunsgreki\_ID

10

Ugunscēloņi

[VMD\_091\_Meza\_piederiba](#VMD_091_Meza_piederiba)

PRV: Privātie

VLS: Valsts (izņemot AS ‘LVM’)

VAS: AS ‘Latvijas valsts meži’ meži

PSV: Pašvaldības

Piedriba

Platības zemes veids

[VMD\_092\_UgunsPlatType](#VMD_092_UgunsPlatType)

1: Mežu platība

2: Jaunaudžu platība

3: Citu meža zemju platība

4: Citu nemeža zemju platība

PlatibaType

3

Platība

Precīzais daļskaitlis

Platiba

7

  

### Biotopa īpašās iezīmes \[Objektu klase\]

Nosaukums DB

VMDBIOIEZIMES

Objekta tips

Objektu klase

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Biotops (VMDBIOTOPI)

  
\[Biotops\].\[Unikālais identifikators\]  
\->  
\[Biotopa īpašās iezīmes\].\[Sasaiste ar BIOTOPI\]

1:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Unikālais identifikators

Garais skaitlis

Bioiezimes\_ID

10

Sasaiste ar BIOTOPI

Garais skaitlis

Bio\_ID

10

Īpašo iezīmju veids

[VMD\_050\_Bioiezīmju\_veidi](#VMD_050_Bioiezīmju_veidi)

1: Lielas ligzdas

2: Skudru pūžņi

3: Dzīvnieku alas

4: Dzīvnieku "vannas"

5: Laukakmeņi

6: Pamatieža atsegums

IezV\_Type

2

Skaits

Īsais skaitlis

Skaits

2

Apraksts

Teksts

Apraksts

  

### Biotopa apsaimniekošana – izcērtama suga \[Objektu klase\]

Nosaukums DB

VMDBIOIZCERTAMASUGA

Objekta tips

Objektu klase

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Biotopa apsaimniekošana – sugas izcirtes apjomi (VMDBIOIZCERTAMIAPJOMI)

  
\[Biotopa apsaimniekošana – izcērtama suga\].\[Unikālais identifikators\]  
\->  
\[Biotopa apsaimniekošana – sugas izcirtes apjomi\].\[Sasaiste ar BIOIZCERTAMA\_SUGA\]

1:N

Biotopa apsaimniekošana (VMDBIOAPSAIMNIEKOSANA)

  
\[Biotopa apsaimniekošana\].\[Unikālais identifikators\]  
\->  
\[Biotopa apsaimniekošana – izcērtama suga\].\[Sasaiste ar BIOAPSAIMNIEKOSANA\]

1:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Unikālais identifikators

Garais skaitlis

BioIzcertamaSuga\_ID

10

Sasaiste ar BIOAPSAIMNIEKOSANA

Garais skaitlis

Aps\_ID

10

Izcirtes veids

[VMD\_171\_Bioizcertama\_suga\_Types](#VMD_171_Bioizcertama_suga_Types)

1: Izciršana

2: Izciršana ap biokokiem

BioIzcertamaSuga\_tips

3

Skaits

Garais skaitlis

Skaits

10

Suga

[VMD\_180\_Koku\_Sugas](#VMD_180_Koku_Sugas)

\-1: Nav zināms

KokSug

  

### Biotopa atslēgas elementu sugas \[Objektu klase\]

Nosaukums DB

VMDBIOELEMENTASUGAS

Objekta tips

Objektu klase

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Biotopa atslēgas elementi (VMDBIOATSLEGASELEMENTI)

  
\[Biotopa atslēgas elementi\].\[Unikālais identifikators\]  
\->  
\[Biotopa atslēgas elementu sugas\].\[Atslēgas identifikators (sasaistei)\]

1:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Suga

[VMD\_180\_Koku\_Sugas](#VMD_180_Koku_Sugas)

\-1: Nav zināms

KokSug

Atslēgas identifikators (sasaistei)

Garais skaitlis

BioAtslegas\_Elementi\_ID

10

Jā

  

### Biotopa negatīvi traucējumi \[Objektu klase\]

Nosaukums DB

VMDBIONEGATIVITRAUC

Objekta tips

Objektu klase

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Biotops (VMDBIOTOPI)

  
\[Biotops\].\[Unikālais identifikators\]  
\->  
\[Biotopa negatīvi traucējumi\].\[Sasaiste ar BIOTOPI\]

1:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Unikālais identifikators

Garais skaitlis

BioNegativiTraucejumi\_ID

10

Sasaiste ar BIOTOPI

Garais skaitlis

Bio\_ID

10

Biotopa negatīvo traucējumu veids

[VMD\_040\_BioTraucejumu\_Veidi](#VMD_040_BioTraucejumu_Veidi)

\-1: Nav zināms

Trauc\_Type

Intensitāte

[VMD\_041\_BioTraucējumu\_Intensitate](#VMD_041_BioTraucējumu_Intensitate)

1: 1

2: 2

3: 3

4: 4

5: 5

6: 6

7: 7

8: 8

9: 9

...

Intensitate

1

  

### Vides aizsardzības ierobežojumi \[Objektu klase\]

Nosaukums DB

VMDVAIEROBEZOJUMI

Objekta tips

Objektu klase

  

##### Relācijas

Datu objekts

Atslēgas atribūti

Kardinalitāte

Vides aizsardzības klasifikators (VMDVAKLASIFIKATORS)

  
\[Vides aizsardzības klasifikators\].\[Unikālais identifikators\]  
\->  
\[Vides aizsardzības ierobežojumi\].\[Sasaiste ar VA klasifikatoru\]

1:N

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

OBJECTID

Identifikators (OID)

OBJECTID

Jā

Ierobežojuma nosaukums

[VMD\_150\_VA\_IerobezojumuVeidi](#VMD_150_VA_IerobezojumuVeidi)

\-1: Nav zināms

Nosaukums

Sasaiste ar VA klasifikatoru

Garais skaitlis

VAK\_ID

10

  

### RC\_BIO\_KONC\_LINK \[Relāciju klase\]

Nosaukums DB

RC\_BIO\_KONC\_LINK

Objekta tips

Relāciju klase

  

##### Datu objekta atribūti

Nosaukums

Tips

Nosaukums DB

Precizitāte

Noklusētā vērtība

Obligāts

Biotopa identifikators (sasaistei)

Garais skaitlis

BiotopsFK\_ID

10

Jā

Koncentrācijas vietas identifikators (sasaistei)

Garais skaitlis

BioKoncentracijaFK\_ID

10

Jā

ES Biotops

[VMD\_070\_Biotopi\_ES](#VMD_070_Biotopi_ES)

Estips\_ID

  

Klasifikatori
-------------

### TemplateCodedValueDomain

Nosaukums DB

TemplateCodedValueDomain

Vērtības

1 - Code1  
2 - Code2  
3 - Code3  

Izmantots objektu klasēs:

\-

  

### Putnu sugas

Nosaukums DB

VMD\_012\_SugasVeids

Vērtības

\-1 - Nav zināms  
1 - Dzīvnieks  
2 - Augs  
3 - Sūna  
4 - Ķērpis  
5 - Sēne  
6 - IAMB  
100 - Cits  

Izmantots objektu klasēs:

Elementu klase: 

[Biotops](#VMDBIOTOPI)

  

### Biotopa indikatoru sugu veidi

Nosaukums DB

VMD\_020\_Biosugu\_veidi

Vērtības

\-1 - Nav zināms  
100 - Cits  

Izmantots objektu klasēs:

Objektu klase: 

[Biotopa indikatoru sugas](#VMDBIOINDIKATORUSUGAS)

  

### Biokoncentrācijas vietu infrastruktūras tips

Nosaukums DB

VMD\_081\_BioKoncentracija\_Infrastruktura

Vērtības

1 - 1. Priežu meži ar dažādvecuma kokiem  
2 - 2. Lapu koku pionierfāzes meži  
3 - 3. Meži ar dažādu pašizrobošanās dinamiku  
3A - 3a. Slapjie egļu meži un pārējie egļu meži  
3B - 3b. Slapjie melnalkšņu un platlapju meži  
3C - 3c. Platlapju meži  
3AB - 3ab. Slapjie egļu meži un pārējie egļu meži; Slapjie melnalkšņu un platlapju meži  
3AC - 3ac. Slapjie egļu meži un pārējie egļu meži; Platlapju meži  
3BC - 3b. Slapjie melnalkšņu un platlapju meži; Platlapju meži  
3ABC - 3a. Slapjie egļu meži un pārējie egļu meži; Slapjie melnalkšņu un platlapju meži; Platlapju meži  
4 - 4. Ģeoloģiskās uzbūves nosacītie lineārie biotopi  

Izmantots objektu klasēs:

Elementu klase: 

[Biotopu koncentrācijas vieta](#VMDBIOKONCENTRACIJA)

  

### Koku sugas

Nosaukums DB

VMD\_180\_Koku\_Sugas

Vērtības

\-1 - Nav zināms  

Izmantots objektu klasēs:

Objektu klase: 

[Biotopa audzes raksturojumi](#VMDBIOAUDZESRAKSTUROJUM)

Objektu klase: 

[Biotopa atslēgas elementu sugas](#VMDBIOELEMENTASUGAS)

Objektu klase: 

[Biotopa apsaimniekošana – izcērtama suga](#VMDBIOIZCERTAMASUGA)

  

### ES Biotopa tips

Nosaukums DB

VMD\_070\_Biotopi\_ES

Vērtības

Izmantots objektu klasēs:

Relāciju klase: 

[RC\_BIO\_KONC\_LINK](#RC_BIO_KONC_LINK)

  

### Ugunsgrēka atklāšanas veids

Nosaukums DB

VMD\_093\_UgunsAtklType

Vērtības

1 - No torņa  
2 - Ziņo trešā persona  
3 - Ziņo VUGD  

Izmantots objektu klasēs:

Elementu klase: 

[Ugunsgrēka teritorijas skatījums](#VMDUGUNSGREKPOLYVIEW)

Objektu klase: 

[Ugunsgrēki](#VMDUGUNSGREKI)

Elementu klase: 

[VMD Ugunsgrēka vietas skatījums](#VMDUGUNSGREKPOINTVIEW)

  

### Biotopa traucējumu intensitāte

Nosaukums DB

VMD\_041\_BioTraucējumu\_Intensitate

Vērtības

1 - 1  
2 - 2  
3 - 3  
4 - 4  
5 - 5  
6 - 6  
7 - 7  
8 - 8  
9 - 9  

Izmantots objektu klasēs:

Objektu klase: 

[Biotopa negatīvi traucējumi](#VMDBIONEGATIVITRAUC)

  

### Krūmu sugu klasifikators

Nosaukums DB

LVM\_MEDUS\_00003k\_ShrubSpecies

Vērtības

30 - 30 - Kārkli  
31 - 31 - Paegļi  
33 - 33 - Krūkļi  
34 - 34 - Lazdas  
36 - 36 - Sausserži  
37 - 37 - Irbenes  
38 - 38 - Segliņi  
39 - 39 - Ribes-sp.  
40 - 40 - Korintes  
41 - 41 - Vilkābeles  
42 - 42 - Jasmīni  
43 - 43 - Plūškoki  
44 - 44 - Spirejas  
45 - 45 - Ceriņi  
46 - 46 - Klintenes  
47 - 47 - Bārbeles  
48 - 48 - Grimoņi  
49 - 49 - Rozes  

Izmantots objektu klasēs:

\-

  

### Vērtējums

Nosaukums DB

VMD\_080\_Vertejums

Vērtības

\-1 - Nav zināms  
1 - Zems  
2 - Vidējs  
3 - Augsts  

Izmantots objektu klasēs:

Elementu klase: 

[Biotops](#VMDBIOTOPI)

Elementu klase: 

[Biotopu koncentrācijas vieta](#VMDBIOKONCENTRACIJA)

  

### Biotopa informācijas avoti

Nosaukums DB

VMD\_010\_BioInfoAvoti

Vērtības

\-1 - Nav zināms  
1 - Meža valsts reģistrs  
2 - Topogrāfiskā karte  
3 - Vietējais mežsargs/iedzīvotājs  
4 - Citas kartes  
5 - Citi pētījumi  
6 - Atrasts nejauši lauku darbu gaitā  

Izmantots objektu klasēs:

Elementu klase: 

[Biotops](#VMDBIOTOPI)

  

### Dzīvnieku sugas

Nosaukums DB

VMD\_100\_DzivnSugas

Vērtības

1 - Alnis  
2 - Staltbriedis  
3 - Meža cūka  
4 - Stirna  
5 - Bebrs  
6 - Mednis  
7 - Rubenis  
8 - Lūsis  
9 - Vilks  

Izmantots objektu klasēs:

Elementu klase: 

[VMD dzīvnieku uzskaite](#VMDAnimalCount)

  

### Biotopa atslēgas elementu veidi (Ar apjomu)

Nosaukums DB

VMD\_031\_Bioelementa\_Veidi\_II

Vērtības

14 - Ciņi ar pamatnēm  
15 - Koki ar deguma rētām  
16 - Dobumaini koki  
17 - Dzeņveidīgo sakalti koki  

Izmantots objektu klasēs:

Objektu klase: 

[Biotopa atslēgas elementi](#VMDBIOATSLEGASELEMENTI)

  

### Augšanas apstākļu tipi

Nosaukums DB

VMD\_190\_AAT

Vērtības

\-1 - Nav zināms  

Izmantots objektu klasēs:

Elementu klase: 

[Biotops](#VMDBIOTOPI)

  

### LVM mežsaimniecības

Nosaukums DB

LVM\_00202\_LVMForestry

Vērtības

! - Vērtības no slāņa LVMForestry  
? - ???  

Izmantots objektu klasēs:

Elementu klase: 

[Ugunsgrēka teritorija](#VMDUGUNSGREKPOLY)

Elementu klase: 

[Ugunsgrēka teritorijas skatījums](#VMDUGUNSGREKPOLYVIEW)

Elementu klase: 

[Ugunsgrēka vieta](#VMDUGUNSGREKPOINT)

Elementu klase: 

[VMD Ugunsgrēka vietas skatījums](#VMDUGUNSGREKPOINTVIEW)

  

### Izciršanas veidi

Nosaukums DB

VMD\_171\_Bioizcertama\_suga\_Types

Vērtības

1 - Izciršana  
2 - Izciršana ap biokokiem  

Izmantots objektu klasēs:

Objektu klase: 

[Biotopa apsaimniekošana – izcērtama suga](#VMDBIOIZCERTAMASUGA)

  

### Pēdu skaita novērtējuma tipi

Nosaukums DB

VMD\_120\_PeduSkaitaTips

Vērtības

1 - Precīzi  
2 - Neprecīzi  
3 - Pieņēmums  

Izmantots objektu klasēs:

\-

  

### Ugunsgrēka cēloņi

Nosaukums DB

VMD\_090\_Ugunsceloni

Vērtības

\-1 - Nav zināms  

Izmantots objektu klasēs:

Elementu klase: 

[Ugunsgrēka teritorijas skatījums](#VMDUGUNSGREKPOLYVIEW)

Objektu klase: 

[Ugunsgrēki](#VMDUGUNSGREKI)

Elementu klase: 

[VMD Ugunsgrēka vietas skatījums](#VMDUGUNSGREKPOINTVIEW)

  

### Biotopa īpašo iezīmju veidi

Nosaukums DB

VMD\_050\_Bioiezīmju\_veidi

Vērtības

1 - Lielas ligzdas  
2 - Skudru pūžņi  
3 - Dzīvnieku alas  
4 - Dzīvnieku "vannas"  
5 - Laukakmeņi  
6 - Pamatieža atsegums  

Izmantots objektu klasēs:

Objektu klase: 

[Biotopa īpašās iezīmes](#VMDBIOIEZIMES)

  

### Biotopa atslēgas elementu veidi (Bez apjoma)

Nosaukums DB

VMD\_030\_Bioelementa\_Veidi\_I

Vērtības

1 - Dažādvecuma audze  
2 - Atvērumu vainaga klājā / lauces  
3 - Pašizretināšanās  
4 - Pastāvīgi pārplūstoši klajumi  
5 - Īslaicīgi pārplūstoši klajumi  
6 - Mirusi koksne dažās sadal. pakāpēs  
7 - Mirusi koksne vairākās sadal. pakāpēs  
8 - Daudz koksnes sēņu / piepju  
9 - Daudz vecu lazdu  
10 - Vismaz 4 dažādu sugu platlapji  
11 - Avotu ietekme  
12 - Bebru darbības pēdas  
13 - Dabīgās ūdensteces  

Izmantots objektu klasēs:

Objektu klase: 

[Biotopa atslēgas elementi](#VMDBIOATSLEGASELEMENTI)

  

### LVM meža iecirkņi

Nosaukums DB

LVM\_00201\_LVMDistricts

Vērtības

kodi - Vērtības no slāņa LVMDistrict  
??? - ???  

Izmantots objektu klasēs:

Elementu klase: 

[Ugunsgrēka teritorija](#VMDUGUNSGREKPOLY)

Elementu klase: 

[Ugunsgrēka teritorijas skatījums](#VMDUGUNSGREKPOLYVIEW)

Elementu klase: 

[Ugunsgrēka vieta](#VMDUGUNSGREKPOINT)

Elementu klase: 

[VMD Ugunsgrēka vietas skatījums](#VMDUGUNSGREKPOINTVIEW)

  

### Koku sugu klasifikators

Nosaukums DB

LVM\_MEDUS\_00003\_TreeSpecies

Vērtības

1 - 01 - Priede  
3 - 03 - Egle  
4 - 04 - Bērzs  
6 - 06 - Melnalksnis  
8 - 08 - Apse  
9 - 09 - Baltalksnis  
10 - 10 - Ozols  
11 - 11 - Osis  
12 - 12 - Liepa  
13 - 13 - Lapegle  
14 - 14 - Citas priedes  
15 - 15 - Citas egles  
16 - 16 - Goba,vīksna  
17 - 17 - Dižskābardis  
18 - 18 - Skābardis  
19 - 19 - Papele  
20 - 20 - Vītols  
21 - 21 - Blīgzna  
22 - 22 - Ciedru priede  
23 - 23 - Baltegle  
24 - 24 - Kļava  
25 - 25 - Saldais ķirsis  
26 - 26 - Mežābele  
27 - 27 - Bumbiere  
28 - 28 - Duglāzija  
29 - 29 - Īve  
32 - 32 - Pīlādži  
35 - 35 - Ievas  
50 - 50 - Dzeltenā akācija  
61 - 61 - Citi ozoli  
62 - 62 - Citas liepas  
63 - 63 - Citas kļavas  
64 - 64 - Citi oši  
65 - 65 - Citas gobas, vīksnas  
66 - 66 - Riekstkoki  
67 - 67 - Zirgkastaņi  
68 - 68 - Hibrīdā apse  

Izmantots objektu klasēs:

Elementu klase: 

[Ugunsgrēka teritorija](#VMDUGUNSGREKPOLY)

Elementu klase: 

[Ugunsgrēka teritorijas skatījums](#VMDUGUNSGREKPOLYVIEW)

Elementu klase: 

[Ugunsgrēka vieta](#VMDUGUNSGREKPOINT)

Elementu klase: 

[VMD Ugunsgrēka vietas skatījums](#VMDUGUNSGREKPOINTVIEW)

  

### Izcērtamo apjomu veidi

Nosaukums DB

VMD\_170\_Bioizcertami\_apjomi\_Types

Vērtības

\-1 - Nav zināms  
1 - 100% platībā  
2 - 50% un > platībā  
3 - 50% un mazāk platībā  
4 - Paņēmienu skaits  

Izmantots objektu klasēs:

Objektu klase: 

[Biotopa apsaimniekošana – sugas izcirtes apjomi](#VMDBIOIZCERTAMIAPJOMI)

  

### Bioelementu veida apjomi

Nosaukums DB

VMD\_035\_Bioelementa\_Veida\_Apjoms

Vērtības

\-1 - Nav Zināms  
1 - 1-5  
2 - 6-10  
3 - >10  
0 - Nav definēts  

Izmantots objektu klasēs:

Objektu klase: 

[Biotopa atslēgas elementi](#VMDBIOATSLEGASELEMENTI)

  

### Bināra izvēle

Nosaukums DB

VMD\_000\_Boolean

Vērtības

\-1 - Nav zināms  
1 - Jā  
2 - Nē  
0 - Nav ievadīts  

Izmantots objektu klasēs:

Elementu klase: 

[Vides aizsardzības klasifikators](#VMDVAKLASIFIKATORS)

Elementu klase: 

[Biotopu koncentrācijas vieta](#VMDBIOKONCENTRACIJA)

Objektu klase: 

[Biotopa apsaimniekošana](#VMDBIOAPSAIMNIEKOSANA)

  

### Meža piederība

Nosaukums DB

VMD\_091\_Meza\_piederiba

Vērtības

PRV - Privātie  
VLS - Valsts (izņemot AS ‘LVM’)  
VAS - AS ‘Latvijas valsts meži’ meži  
PSV - Pašvaldības  

Izmantots objektu klasēs:

Objektu klase: 

[Ugunsgrēku platības uzskaite](#VMDUGUNSPLATIBAS)

  

### Koku sugas

Nosaukums DB

VMD\_161\_KokuSugas

Vērtības

\-1 - Nav zināms  
100 - Cits  

Izmantots objektu klasēs:

\-

  

### Putnu sugas

Nosaukums DB

VMD\_013\_StatussVeids

Vērtības

\-1 - Nav zināms  
P - Paplašinājums (P)  
P30-70 - Paplašinājums (P30-70)  
B - Buferjosla (B)  
BP - Buferjosla (BP)  
B30-70 - Buferjosla (B30-70)  
I - Ieslēgums (I)  

Izmantots objektu klasēs:

Elementu klase: 

[Biotops](#VMDBIOTOPI)

  

### Vides aizsardzības ierobežojumu veidi

Nosaukums DB

VMD\_150\_VA\_IerobezojumuVeidi

Vērtības

\-1 - Nav zināms  

Izmantots objektu klasēs:

Objektu klase: 

[Vides aizsardzības ierobežojumi](#VMDVAIEROBEZOJUMI)

  

### Biotopa indikatoru sugu sastopamība

Nosaukums DB

VMD\_021\_BioSugu\_Sastopamiba

Vērtības

\-1 - Nav zināms  

Izmantots objektu klasēs:

Objektu klase: 

[Biotopa indikatoru sugas](#VMDBIOINDIKATORUSUGAS)

  

### Biotopa nosaukumi

Nosaukums DB

VMD\_011\_Bionosaukumi

Vērtības

\-1 - Nav zināms  
A1 - Skujkoku mežs  
A2 - Mistrots skujkoku-lapukoku mežs  
B1 - Platlapju mežs  
B2 - Apšu mežs  
B3 - Cits lapukoku mežs  
C1 - Slapjš melnalkšņu mežs  
C2 - Egļu un mistrots egļu slapjais mežs  
C3 - Priežu un bērzu slapjais mežs  
C4 - Platlapju slapjais mežs  
D1 - Gravas mežs  
D2 - Nogāzes mežs  
D3 - Krastmalas mežs  
D4 - Avotains mežs  
D5 - Kaļķains skujkoku mežs  
D6 - Kaļķains zāļu purvs vai pļava  
D7 - Purva vai meža mozaīka  
E1 - Dedzis mežs  
E2 - Bioloģiski nozīmīga bebraine  
E3 - Biokoks  
E4 - Vējgāzes mežs  

Izmantots objektu klasēs:

Elementu klase: 

[Biotops](#VMDBIOTOPI)

  

### Biotopa traucējumu veidi

Nosaukums DB

VMD\_040\_BioTraucejumu\_Veidi

Vērtības

\-1 - Nav zināms  

Izmantots objektu klasēs:

Objektu klase: 

[Biotopa negatīvi traucējumi](#VMDBIONEGATIVITRAUC)

  

### Ugunsgrēku platību uzskaites tips

Nosaukums DB

VMD\_092\_UgunsPlatType

Vērtības

1 - Mežu platība  
2 - Jaunaudžu platība  
3 - Citu meža zemju platība  
4 - Citu nemeža zemju platība  

Izmantots objektu klasēs:

Objektu klase: 

[Ugunsgrēku platības uzskaite](#VMDUGUNSPLATIBAS)

  

### Biotopa atslēgas elementu veidi (Ar apjomu un sugu)

Nosaukums DB

VMD\_032\_Bioelementa\_Veidi\_III

Vērtības

18 - Bioloģiski veci koki  
19 - Mazu dimensiju lēni augoši veci koki  
20 - Saulei atklāti veci platl. koki  
21 - Krituši koki ar mizu  
22 - Krituši koki bez mizas  
23 - Nokrituši kaistoši koki  
24 - Stumbeņi  

Izmantots objektu klasēs:

Objektu klase: 

[Biotopa atslēgas elementi](#VMDBIOATSLEGASELEMENTI)

  

Vērtību robežas
---------------

### Procenti (0-100%)

Nosaukums DB

VMD\_RD\_Procenti

Minimālā vērtība

1

Maksimālā vērtība

100

Izmantots objektu klasēs:

\-
