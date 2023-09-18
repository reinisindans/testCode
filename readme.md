<!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <style>
        
        body {
            size: A4;
            margin: 15mm;
            padding: 0;
        }
        
        @page {
            size: A4;
            margin: 20mm 0mm 
        }
        
        tr{
            break-inside: avoid !important;
        }
        table {
            break-before: avoid!important;
        }
        @media print {
            #table-of-contents div a::after {
                  content: target-counter(attr(href), page);
                  float: right;
                  font-size: small;
                  position: absolute;
                  right: 30mm;
                }
            table {
            table-layout:fixed
            }
            td {
            word-wrap: break-word;
            }
        }
        </style>
        

        </head>
        <body>
        <div class="container">
        <h1 style='color: lightblue; font-size: 24px; text-align: left; '> Datu bāzes shēmas apraksts
                        </h1>
                        <h2 style='color: lightblue; font-size: 24px; text-align: left; '> Saturs
                        </h2>
                        <div id="table-of-contents">
                        <div class="toc_entry" ><a style='color: black; font-size: 18px; text-align: left; ' href="#VMDData">VMDData</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDBIOTOPI">Biotops</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDAnimalCount">VMD dzīvnieku uzskaite</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDUGUNSGREKPOLY">Ugunsgrēka teritorija</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDVAKLASIFIKATORS">Vides aizsardzības klasifikators</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDUGUNSGREKPOINT">Ugunsgrēka vieta</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDBIOKONCENTRACIJA">Biotopu koncentrācijas vieta</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDVAPAZIMES">Vides aizsardzības pazīmes</a></div> <br><div class="toc_entry" ><a style='color: black; font-size: 18px; text-align: left; ' href="#VMDDataView">VMDDataView</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDUGUNSGREKPOLYVIEW">Ugunsgrēka teritorijas skatījums</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDUGUNSGREKPOINTVIEW">VMD Ugunsgrēka vietas skatījums</a></div> <br><div class="toc_entry"><a href="#common_classes" style='color: black; font-size: 18px; text-align: left; '> Kopējās elementu un objektu klases</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDBIOAUDZESRAKSTUROJUM">Biotopa audzes raksturojumi</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDBIOINDIKATORUSUGAS">Biotopa indikatoru sugas</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDUGUNSGREKI">Ugunsgrēki</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDBIOATSLEGASELEMENTI">Biotopa atslēgas elementi</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDBIOIZCERTAMIAPJOMI">Biotopa apsaimniekošana – sugas izcirtes apjomi</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDBIOAPSAIMNIEKOSANA">Biotopa apsaimniekošana</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDUGUNSPLATIBAS">Ugunsgrēku platības uzskaite</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDBIOIEZIMES">Biotopa īpašās iezīmes</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDBIOIZCERTAMASUGA">Biotopa apsaimniekošana – izcērtama suga</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDBIOELEMENTASUGAS">Biotopa atslēgas elementu sugas</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDBIONEGATIVITRAUC">Biotopa negatīvi traucējumi</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMDVAIEROBEZOJUMI">Vides aizsardzības ierobežojumi</a></div><br><div class="toc_entry"><a href="#cvd" style='color: black; font-size: 18px; text-align: left; '> Klasifikatori</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#TemplateCodedValueDomain">TemplateCodedValueDomain</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_012_SugasVeids">Putnu sugas</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_020_Biosugu_veidi">Biotopa indikatoru sugu veidi</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_081_BioKoncentracija_Infrastruktura">Biokoncentrācijas vietu infrastruktūras tips</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_180_Koku_Sugas">Koku sugas</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_070_Biotopi_ES">ES Biotopa tips</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_093_UgunsAtklType">Ugunsgrēka atklāšanas veids</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_041_BioTraucējumu_Intensitate">Biotopa traucējumu intensitāte</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#LVM_MEDUS_00003k_ShrubSpecies">Krūmu sugu klasifikators</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_080_Vertejums">Vērtējums</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_010_BioInfoAvoti">Biotopa informācijas avoti</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_100_DzivnSugas">Dzīvnieku sugas</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_031_Bioelementa_Veidi_II">Biotopa atslēgas elementu veidi (Ar apjomu)</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_190_AAT">Augšanas apstākļu tipi</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#LVM_00202_LVMForestry">LVM mežsaimniecības</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_171_Bioizcertama_suga_Types">Izciršanas veidi</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_120_PeduSkaitaTips">Pēdu skaita novērtējuma tipi</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_090_Ugunsceloni">Ugunsgrēka cēloņi</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_050_Bioiezīmju_veidi">Biotopa īpašo iezīmju veidi</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_030_Bioelementa_Veidi_I">Biotopa atslēgas elementu veidi (Bez apjoma)</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#LVM_00201_LVMDistricts">LVM meža iecirkņi</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#LVM_MEDUS_00003_TreeSpecies">Koku sugu klasifikators</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_170_Bioizcertami_apjomi_Types">Izcērtamo apjomu veidi</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_035_Bioelementa_Veida_Apjoms">Bioelementu veida apjomi</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_000_Boolean">Bināra izvēle</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_091_Meza_piederiba">Meža piederība</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_161_KokuSugas">Koku sugas</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_013_StatussVeids">Putnu sugas</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_150_VA_IerobezojumuVeidi">Vides aizsardzības ierobežojumu veidi</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_021_BioSugu_Sastopamiba">Biotopa indikatoru sugu sastopamība</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_011_Bionosaukumi">Biotopa nosaukumi</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_040_BioTraucejumu_Veidi">Biotopa traucējumu veidi</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_092_UgunsPlatType">Ugunsgrēku platību uzskaites tips</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_032_Bioelementa_Veidi_III">Biotopa atslēgas elementu veidi (Ar apjomu un sugu)</a></div><div class="toc_entry"><a href="#range_domains" style='color: black; font-size: 18px; text-align: left; '> Vērtību robežas</a></div><div class="toc_entry" style= 'width: 100%; display: flex; flex-direction: row; align-items: center; '><p style='color: black; font-size: 14px; text-align: left; white-space: pre; '>&#9</p><a style='color: black; font-size: 14px; text-align: left; white-space: pre; ' href="#VMD_RD_Procenti">Procenti (0-100%)</a></div></div><h2 style='color: lightblue; font-size: 24px; text-align: left; ' id='VMDData'> VMDData [Datu kopa]
                        </h2>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDData</td>
                </tr>
            </table>
            <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDBIOTOPI'> Biotops [Elementu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDBIOTOPI</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Elementu klase</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Laukums</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>M koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Z koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Objekta apakštipi</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Apraksts</th>
                    <tr>
                </thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>1</td>
                <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>Potenciālais meža biotops</td>
            </tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>2</td>
                <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>Dabīgais meža biotops</td>
            </tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>starpaudze meža biotopu koncentrācijas vietā</td>
            </tr>
            </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotopa apsaimniekošana (VMDBIOAPSAIMNIEKOSANA)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotops].[Unikālais identifikators] <br> -> <br>[Biotopa apsaimniekošana].[Sasaiste ar BIOTOPI]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotopa atslēgas elementi (VMDBIOATSLEGASELEMENTI)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotops].[Unikālais identifikators] <br> -> <br>[Biotopa atslēgas elementi].[Sasaiste ar BIOTOPI]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotopa negatīvi traucējumi (VMDBIONEGATIVITRAUC)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotops].[Unikālais identifikators] <br> -> <br>[Biotopa negatīvi traucējumi].[Sasaiste ar BIOTOPI]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Vides aizsardzības pazīmes (VMDVAPAZIMES)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Vides aizsardzības pazīmes].[Unikālais identifikators] <br> -> <br>[Biotops].[Sasaiste ar vides aizsardzības klasifikatora pazīmēm]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotopa audzes raksturojumi (VMDBIOAUDZESRAKSTUROJUM)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotops].[Unikālais identifikators] <br> -> <br>[Biotopa audzes raksturojumi].[Sasaiste ar BIOTOPI]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotopa indikatoru sugas (VMDBIOINDIKATORUSUGAS)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotops].[Unikālais identifikators] <br> -> <br>[Biotopa indikatoru sugas].[Sasaiste ar BIOTOPI]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotopa īpašās iezīmes (VMDBIOIEZIMES)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotops].[Unikālais identifikators] <br> -> <br>[Biotopa īpašās iezīmes].[Sasaiste ar BIOTOPI]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotopu koncentrācijas vieta (VMDBIOKONCENTRACIJA)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>[Biotops].[Unikālais identifikators]<br> -> <br>[RC_BIO_KONC_LINK].[Biotopa identifikators (sasaistei)]<br><br>[Biotopu koncentrācijas vieta].[Unikālais identifikators] <br> -> <br>[RC_BIO_KONC_LINK].[Koncentrācijas vietas identifikators (sasaistei)]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>N:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Unikālais identifikators</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Biotops_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Apakštipa lauks</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Biotops_ST</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>1</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Biotopa Nr.</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Numurs</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Platība (situācijai dabā)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Platiba</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>6</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Audzes sastāva formula (situācijai dabā)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Formula</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Augšanas apstākļu tips</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_190_AAT">VMD_190_AAT</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>AAT</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>2</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sasaiste ar vides aizsardzības klasifikatora pazīmēm</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>VA_Paz_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Informācijas avots</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_010_BioInfoAvoti">VMD_010_BioInfoAvoti</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p><p style='font-size:smaller; line-height: 0.5;'>1: Meža valsts reģistrs</p><p style='font-size:smaller; line-height: 0.5;'>2: Topogrāfiskā karte</p><p style='font-size:smaller; line-height: 0.5;'>3: Vietējais mežsargs/iedzīvotājs</p><p style='font-size:smaller; line-height: 0.5;'>4: Citas kartes</p><p style='font-size:smaller; line-height: 0.5;'>5: Citi pētījumi</p><p style='font-size:smaller; line-height: 0.5;'>6: Atrasts nejauši lauku darbu gaitā</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>InfoAv</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Biotopa nosaukums I</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_011_Bionosaukumi">VMD_011_Bionosaukumi</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p><p style='font-size:smaller; line-height: 0.5;'>A1: Skujkoku mežs</p><p style='font-size:smaller; line-height: 0.5;'>A2: Mistrots skujkoku-lapukoku mežs</p><p style='font-size:smaller; line-height: 0.5;'>B1: Platlapju mežs</p><p style='font-size:smaller; line-height: 0.5;'>B2: Apšu mežs</p><p style='font-size:smaller; line-height: 0.5;'>B3: Cits lapukoku mežs</p><p style='font-size:smaller; line-height: 0.5;'>C1: Slapjš melnalkšņu mežs</p><p style='font-size:smaller; line-height: 0.5;'>C2: Egļu un mistrots egļu slapjais mežs</p><p style='font-size:smaller; line-height: 0.5;'>C3: Priežu un bērzu slapjais mežs</p><p style='font-size:smaller; line-height: 0.5;'>...</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums1</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Biotopa nosaukums II</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_011_Bionosaukumi">VMD_011_Bionosaukumi</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p><p style='font-size:smaller; line-height: 0.5;'>A1: Skujkoku mežs</p><p style='font-size:smaller; line-height: 0.5;'>A2: Mistrots skujkoku-lapukoku mežs</p><p style='font-size:smaller; line-height: 0.5;'>B1: Platlapju mežs</p><p style='font-size:smaller; line-height: 0.5;'>B2: Apšu mežs</p><p style='font-size:smaller; line-height: 0.5;'>B3: Cits lapukoku mežs</p><p style='font-size:smaller; line-height: 0.5;'>C1: Slapjš melnalkšņu mežs</p><p style='font-size:smaller; line-height: 0.5;'>C2: Egļu un mistrots egļu slapjais mežs</p><p style='font-size:smaller; line-height: 0.5;'>C3: Priežu un bērzu slapjais mežs</p><p style='font-size:smaller; line-height: 0.5;'>...</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums2</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Bioloģiskās daudzveidības apraksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Daudzveidiba</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Piezīmes</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Piezimes</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Apsekošanas datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Persona, kas veica apsekošanu</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Apsekoja</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Audzes status</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_013_StatussVeids">VMD_013_StatussVeids</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p><p style='font-size:smaller; line-height: 0.5;'>P: Paplašinājums (P)</p><p style='font-size:smaller; line-height: 0.5;'>P30-70: Paplašinājums (P30-70)</p><p style='font-size:smaller; line-height: 0.5;'>B: Buferjosla (B)</p><p style='font-size:smaller; line-height: 0.5;'>BP: Buferjosla (BP)</p><p style='font-size:smaller; line-height: 0.5;'>B30-70: Buferjosla (B30-70)</p><p style='font-size:smaller; line-height: 0.5;'>I: Ieslēgums (I)</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>SA_Statuss</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Audzes suga</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Īsais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>SA_Suga</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Audzes ierobežojumu intensitāte</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Īsais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>SA_Intensitate</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Piezīmes, suga</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>SA_Suga_Piezimes</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>DMB raksturīgo ekoloģisko rādītāju sasniegšanas laiks</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Īsais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>SA_Sasniegsana</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Novērtējums par audzes piemērotību paplašinājumiem</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_080_Vertejums">VMD_080_Vertejums</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p><p style='font-size:smaller; line-height: 0.5;'>1: Zems</p><p style='font-size:smaller; line-height: 0.5;'>2: Vidējs</p><p style='font-size:smaller; line-height: 0.5;'>3: Augsts</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>SA_Piemerotiba</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Apsaimniekošanas apraksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>SA_Apsaimn</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDAnimalCount'> VMD dzīvnieku uzskaite [Elementu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDAnimalCount</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Elementu klase</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Laukums</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>M koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Z koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Uzskaites vienība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Uzsk_vien</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Dzīvnieku suga</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_100_DzivnSugas">VMD_100_DzivnSugas</a><p style='font-size:smaller; line-height: 0.5;'>1: Alnis</p><p style='font-size:smaller; line-height: 0.5;'>2: Staltbriedis</p><p style='font-size:smaller; line-height: 0.5;'>3: Meža cūka</p><p style='font-size:smaller; line-height: 0.5;'>4: Stirna</p><p style='font-size:smaller; line-height: 0.5;'>5: Bebrs</p><p style='font-size:smaller; line-height: 0.5;'>6: Mednis</p><p style='font-size:smaller; line-height: 0.5;'>7: Rubenis</p><p style='font-size:smaller; line-height: 0.5;'>8: Lūsis</p><p style='font-size:smaller; line-height: 0.5;'>9: Vilks</p><p style='font-size:smaller; line-height: 0.5;'>...</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Suga</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>2</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Uzskaites vērtība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>UzskVertiba</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>5</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDUGUNSGREKPOLY'> Ugunsgrēka teritorija [Elementu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDUGUNSGREKPOLY</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Elementu klase</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Laukums</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>M koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Z koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Ugunsgrēki (VMDUGUNSGREKI)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Ugunsgrēki].[Unikālais identifikators] <br> -> <br>[Ugunsgrēka teritorija].[Sasaiste ar UGUNSGREKI]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sasaiste ar UGUNSGREKI</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Ug_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Mežsaimniecība </td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#LVM_00202_LVMForestry">LVM_00202_LVMForestry</a><p style='font-size:smaller; line-height: 0.5;'>!: Vērtības no slāņa LVMForestry</p><p style='font-size:smaller; line-height: 0.5;'>?: ???</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVMForestryCode</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Kv.apg. - kvartāls</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>BlockKey</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Nogabala numurs</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Īsais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>CompartmentNumber</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>2</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Iecirknis</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#LVM_00201_LVMDistricts">LVM_00201_LVMDistricts</a><p style='font-size:smaller; line-height: 0.5;'>kodi: Vērtības no slāņa LVMDistrict</p><p style='font-size:smaller; line-height: 0.5;'>???: ???</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVM_District_Code</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sugu sastāvs (M)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>SugasSastavs</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Meža tipa apzīmējums (M)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>AAT</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>1.sugas vecums (M)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>A10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>1.suga (M)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#LVM_MEDUS_00003_TreeSpecies">LVM_MEDUS_00003_TreeSpecies</a><p style='font-size:smaller; line-height: 0.5;'>1: 01 - Priede</p><p style='font-size:smaller; line-height: 0.5;'>3: 03 - Egle</p><p style='font-size:smaller; line-height: 0.5;'>4: 04 - Bērzs</p><p style='font-size:smaller; line-height: 0.5;'>6: 06 - Melnalksnis</p><p style='font-size:smaller; line-height: 0.5;'>8: 08 - Apse</p><p style='font-size:smaller; line-height: 0.5;'>9: 09 - Baltalksnis</p><p style='font-size:smaller; line-height: 0.5;'>10: 10 - Ozols</p><p style='font-size:smaller; line-height: 0.5;'>11: 11 - Osis</p><p style='font-size:smaller; line-height: 0.5;'>12: 12 - Liepa</p><p style='font-size:smaller; line-height: 0.5;'>...</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>S10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDVAKLASIFIKATORS'> Vides aizsardzības klasifikators [Elementu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDVAKLASIFIKATORS</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Elementu klase</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Laukums</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>M koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Z koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Vides aizsardzības ierobežojumi (VMDVAIEROBEZOJUMI)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Vides aizsardzības klasifikators].[Unikālais identifikators] <br> -> <br>[Vides aizsardzības ierobežojumi].[Sasaiste ar VA klasifikatoru]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Vides aizsardzības pazīmes (VMDVAPAZIMES)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Vides aizsardzības klasifikators].[Unikālais identifikators] <br> -> <br>[Vides aizsardzības pazīmes].[Sasaiste ar VA_KLASIFIKATORS]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Unikālais identifikators</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>VAK_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Hierarhijas sasaiste</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Parent_VAK_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Kods</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Kods</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Vai atļauts reģistrēt unikālās aizsardzības pazīmes?</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_000_Boolean">VMD_000_Boolean</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p><p style='font-size:smaller; line-height: 0.5;'>1: Jā</p><p style='font-size:smaller; line-height: 0.5;'>2: Nē</p><p style='font-size:smaller; line-height: 0.5;'>0: Nav ievadīts</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Unikalas_Pazimes</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>2</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Izveidošanas datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Izveidots</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Likvidēšanas datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Likvidets</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDUGUNSGREKPOINT'> Ugunsgrēka vieta [Elementu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDUGUNSGREKPOINT</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Elementu klase</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Punkts</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>M koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Z koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Ugunsgrēki (VMDUGUNSGREKI)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Ugunsgrēki].[Unikālais identifikators] <br> -> <br>[Ugunsgrēka vieta].[Sasaiste ar UGUNSGREKI]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Simbola leņķis</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Angval</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>5</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sasaiste ar UGUNSGREKI</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Ug_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Mežsaimniecība </td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#LVM_00202_LVMForestry">LVM_00202_LVMForestry</a><p style='font-size:smaller; line-height: 0.5;'>!: Vērtības no slāņa LVMForestry</p><p style='font-size:smaller; line-height: 0.5;'>?: ???</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVMForestryCode</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Kv.apg. - kvartāls</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>BlockKey</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Nogabala numurs</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Īsais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>CompartmentNumber</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>2</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Iecirknis</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#LVM_00201_LVMDistricts">LVM_00201_LVMDistricts</a><p style='font-size:smaller; line-height: 0.5;'>kodi: Vērtības no slāņa LVMDistrict</p><p style='font-size:smaller; line-height: 0.5;'>???: ???</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVM_District_Code</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Meža tipa apzīmējums (M)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>AAT</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sugu sastāvs (M)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>SugasSastavs</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>1.sugas vecums (M)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>A10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>1.suga (M)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#LVM_MEDUS_00003_TreeSpecies">LVM_MEDUS_00003_TreeSpecies</a><p style='font-size:smaller; line-height: 0.5;'>1: 01 - Priede</p><p style='font-size:smaller; line-height: 0.5;'>3: 03 - Egle</p><p style='font-size:smaller; line-height: 0.5;'>4: 04 - Bērzs</p><p style='font-size:smaller; line-height: 0.5;'>6: 06 - Melnalksnis</p><p style='font-size:smaller; line-height: 0.5;'>8: 08 - Apse</p><p style='font-size:smaller; line-height: 0.5;'>9: 09 - Baltalksnis</p><p style='font-size:smaller; line-height: 0.5;'>10: 10 - Ozols</p><p style='font-size:smaller; line-height: 0.5;'>11: 11 - Osis</p><p style='font-size:smaller; line-height: 0.5;'>12: 12 - Liepa</p><p style='font-size:smaller; line-height: 0.5;'>...</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>S10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDBIOKONCENTRACIJA'> Biotopu koncentrācijas vieta [Elementu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDBIOKONCENTRACIJA</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Elementu klase</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Laukums</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>M koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Z koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotops (VMDBIOTOPI)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>[Biotops].[Unikālais identifikators]<br> -> <br>[RC_BIO_KONC_LINK].[Biotopa identifikators (sasaistei)]<br><br>[Biotopu koncentrācijas vieta].[Unikālais identifikators] <br> -> <br>[RC_BIO_KONC_LINK].[Koncentrācijas vietas identifikators (sasaistei)]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>N:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Unikālais identifikators</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>BioKoncentracija_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Koncentrācijas Nr.</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Numurs</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Infrastruktūras tips</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_081_BioKoncentracija_Infrastruktura">VMD_081_BioKoncentracija_Infrastruktura</a><p style='font-size:smaller; line-height: 0.5;'>1: 1. Priežu meži ar dažādvecuma kokiem</p><p style='font-size:smaller; line-height: 0.5;'>2: 2. Lapu koku pionierfāzes meži</p><p style='font-size:smaller; line-height: 0.5;'>3: 3. Meži ar dažādu pašizrobošanās dinamiku</p><p style='font-size:smaller; line-height: 0.5;'>3A: 3a. Slapjie egļu meži un pārējie egļu meži</p><p style='font-size:smaller; line-height: 0.5;'>3B: 3b. Slapjie melnalkšņu un platlapju meži</p><p style='font-size:smaller; line-height: 0.5;'>3C: 3c. Platlapju meži</p><p style='font-size:smaller; line-height: 0.5;'>3AB: 3ab. Slapjie egļu meži un pārējie egļu meži; Slapjie melnalkšņu un platlapju meži</p><p style='font-size:smaller; line-height: 0.5;'>3AC: 3ac. Slapjie egļu meži un pārējie egļu meži; Platlapju meži</p><p style='font-size:smaller; line-height: 0.5;'>3BC: 3b. Slapjie melnalkšņu un platlapju meži; Platlapju meži</p><p style='font-size:smaller; line-height: 0.5;'>...</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Infrastruktura</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Atrodas nozīmīgajā apvidū?</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_000_Boolean">VMD_000_Boolean</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p><p style='font-size:smaller; line-height: 0.5;'>1: Jā</p><p style='font-size:smaller; line-height: 0.5;'>2: Nē</p><p style='font-size:smaller; line-height: 0.5;'>0: Nav ievadīts</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Nozimigs_Apvidus</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>1</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Nav nosusināts</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>NT_Nesusinats</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Nosusināts, bet sistēma nedarbojas</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>NT_SusNeDarb</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Nosusināšana darbojas</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>NT_SusDarb</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Biotopu koncentrācijas vietas vērtējums?</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_080_Vertejums">VMD_080_Vertejums</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p><p style='font-size:smaller; line-height: 0.5;'>1: Zems</p><p style='font-size:smaller; line-height: 0.5;'>2: Vidējs</p><p style='font-size:smaller; line-height: 0.5;'>3: Augsts</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Konc_Vert</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>1</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Nosusināšanas ilglaicīgā negatīvā ietekme uz bioloģiskajām vērtībām</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_080_Vertejums">VMD_080_Vertejums</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p><p style='font-size:smaller; line-height: 0.5;'>1: Zems</p><p style='font-size:smaller; line-height: 0.5;'>2: Vidējs</p><p style='font-size:smaller; line-height: 0.5;'>3: Augsts</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Sus_Ietekme</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>1</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Ietekme, slēdzot nosusināšanas sistēmu</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_080_Vertejums">VMD_080_Vertejums</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p><p style='font-size:smaller; line-height: 0.5;'>1: Zems</p><p style='font-size:smaller; line-height: 0.5;'>2: Vidējs</p><p style='font-size:smaller; line-height: 0.5;'>3: Augsts</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>SusSledz_Ietekme</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>1</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Ieguvums</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Ieguvums</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Piezīmes</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Piezimes</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Apsekoja</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Apsekoja</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDVAPAZIMES'> Vides aizsardzības pazīmes [Elementu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDVAPAZIMES</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Elementu klase</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Laukums</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>M koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Z koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Vides aizsardzības klasifikators (VMDVAKLASIFIKATORS)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Vides aizsardzības klasifikators].[Unikālais identifikators] <br> -> <br>[Vides aizsardzības pazīmes].[Sasaiste ar VA_KLASIFIKATORS]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotops (VMDBIOTOPI)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Vides aizsardzības pazīmes].[Unikālais identifikators] <br> -> <br>[Biotops].[Sasaiste ar vides aizsardzības klasifikatora pazīmēm]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Unikālais identifikators</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>VA_Paz_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sasaiste ar VA_KLASIFIKATORS</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>VAK_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Numurs</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Numurs</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Izveidošanas datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Izveidots</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Likvidēšanas datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Likvidets</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h2 style='color: lightblue; font-size: 24px; text-align: left; ' id='VMDDataView'> VMDDataView [Datu kopa]
                        </h2>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDDataView</td>
                </tr>
            </table>
            <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDUGUNSGREKPOLYVIEW'> Ugunsgrēka teritorijas skatījums [Elementu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDUGUNSGREKPOLYVIEW</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Elementu klase</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Laukums</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>M koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Z koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Uzsāk dzēšanu</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Usak</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Trauksmes laiks</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Trauksme</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Ierobežošanas laiks</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Ierobezo</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Likvidēšanas laiks</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Likvide</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Ugunsgrēka atklāšanas veids</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_093_UgunsAtklType">VMD_093_UgunsAtklType</a><p style='font-size:smaller; line-height: 0.5;'>1: No torņa</p><p style='font-size:smaller; line-height: 0.5;'>2: Ziņo trešā persona</p><p style='font-size:smaller; line-height: 0.5;'>3: Ziņo VUGD</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>UATKL_TYPE</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Ugunscēloņi</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_090_Ugunsceloni">VMD_090_Ugunsceloni</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Ucel_Type</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sasaiste ar UGUNSGREKI</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Ug_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>LVM meža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVM_MEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>LVM Jaunaudžu platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVM_JAUN_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>LVM Citu meža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVM_CITMEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>LVM Citu nemeža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVM_CITNEMEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Privātio meža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PRV_MEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Privātio Jaunaudžu platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PRV_JAUN_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Privātio citu meža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PRV_CITMEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Privātio Citu nemeža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PRV_CITNEMEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Valsts (ne LVM) meža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>VLS_MEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Valsts (ne LVM) Mežu platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>VLS_JAUN_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Valsts (ne LVM) citu meža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>VLS_CITMEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Valsts (ne LVM) Citu nemeža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>VLS_CITNEMEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Pašvaldību meža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PSV_MEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Pašvaldību Mežu platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PSV_JAUN_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Pašvaldību citu meža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PSV_CITMEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Pašvaldību nemeža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PSV_CITNEMEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Valsts (ne LVM) summārā platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>VLS_SUM_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Pašvaldību summārā platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PSV_SUM_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Privātio summārā platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PRV_SUM_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>LVM summārā platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVM_SUM_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Mežsaimniecība </td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#LVM_00202_LVMForestry">LVM_00202_LVMForestry</a><p style='font-size:smaller; line-height: 0.5;'>!: Vērtības no slāņa LVMForestry</p><p style='font-size:smaller; line-height: 0.5;'>?: ???</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVMForestryCode</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Kv.apg. - kvartāls</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>BlockKey</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Nogabala numurs</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Īsais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>CompartmentNumber</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>2</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Iecirknis</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#LVM_00201_LVMDistricts">LVM_00201_LVMDistricts</a><p style='font-size:smaller; line-height: 0.5;'>kodi: Vērtības no slāņa LVMDistrict</p><p style='font-size:smaller; line-height: 0.5;'>???: ???</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVM_District_Code</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Meža tipa apzīmējums (M)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>AAT</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sugu sastāvs (M)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>SugasSastavs</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>1.sugas vecums (M)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>A10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>1.suga (M)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#LVM_MEDUS_00003_TreeSpecies">LVM_MEDUS_00003_TreeSpecies</a><p style='font-size:smaller; line-height: 0.5;'>1: 01 - Priede</p><p style='font-size:smaller; line-height: 0.5;'>3: 03 - Egle</p><p style='font-size:smaller; line-height: 0.5;'>4: 04 - Bērzs</p><p style='font-size:smaller; line-height: 0.5;'>6: 06 - Melnalksnis</p><p style='font-size:smaller; line-height: 0.5;'>8: 08 - Apse</p><p style='font-size:smaller; line-height: 0.5;'>9: 09 - Baltalksnis</p><p style='font-size:smaller; line-height: 0.5;'>10: 10 - Ozols</p><p style='font-size:smaller; line-height: 0.5;'>11: 11 - Osis</p><p style='font-size:smaller; line-height: 0.5;'>12: 12 - Liepa</p><p style='font-size:smaller; line-height: 0.5;'>...</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>S10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDUGUNSGREKPOINTVIEW'> VMD Ugunsgrēka vietas skatījums [Elementu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDUGUNSGREKPOINTVIEW</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Elementu klase</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Punkts</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>M koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Z koordinātes</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Nē</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Ģeometrija</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Shape</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sasaiste ar UGUNSGREKI</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Ug_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Ierobežošanas laiks</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Ierobezo</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Likvidēšanas laiks</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Likvide</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Trauksmes laiks</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Trauksme</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Ugunsgrēka atklāšanas veids</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_093_UgunsAtklType">VMD_093_UgunsAtklType</a><p style='font-size:smaller; line-height: 0.5;'>1: No torņa</p><p style='font-size:smaller; line-height: 0.5;'>2: Ziņo trešā persona</p><p style='font-size:smaller; line-height: 0.5;'>3: Ziņo VUGD</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>UATKL_TYPE</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Ugunscēloņi</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_090_Ugunsceloni">VMD_090_Ugunsceloni</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Ucel_Type</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Uzsāk dzēšanu</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Usak</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>LVM meža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVM_MEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>LVM Jaunaudžu platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVM_JAUN_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>LVM Citu meža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVM_CITMEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>LVM Citu nemeža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVM_CITNEMEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>LVM summārā platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVM_SUM_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Privātio meža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PRV_MEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Privātio Jaunaudžu platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PRV_JAUN_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Privātio citu meža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PRV_CITMEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Privātio Citu nemeža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PRV_CITNEMEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Privātio summārā platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PRV_SUM_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Valsts (ne LVM) meža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>VLS_MEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Valsts (ne LVM) Mežu platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>VLS_JAUN_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Valsts (ne LVM) citu meža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>VLS_CITMEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Valsts (ne LVM) Citu nemeža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>VLS_CITNEMEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Valsts (ne LVM) summārā platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>VLS_SUM_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Pašvaldību meža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PSV_MEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Pašvaldību Mežu platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PSV_JAUN_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Pašvaldību citu meža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PSV_CITMEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Pašvaldību nemeža zemju platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PSV_CITNEMEZ_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Pašvaldību summārā platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PSV_SUM_PLATIBA</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>38</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Mežsaimniecība </td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#LVM_00202_LVMForestry">LVM_00202_LVMForestry</a><p style='font-size:smaller; line-height: 0.5;'>!: Vērtības no slāņa LVMForestry</p><p style='font-size:smaller; line-height: 0.5;'>?: ???</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVMForestryCode</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Kv.apg. - kvartāls</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>BlockKey</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Nogabala numurs</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Īsais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>CompartmentNumber</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>2</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Iecirknis</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#LVM_00201_LVMDistricts">LVM_00201_LVMDistricts</a><p style='font-size:smaller; line-height: 0.5;'>kodi: Vērtības no slāņa LVMDistrict</p><p style='font-size:smaller; line-height: 0.5;'>???: ???</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>LVM_District_Code</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Meža tipa apzīmējums (M)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>AAT</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sugu sastāvs (M)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>SugasSastavs</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>1.sugas vecums (M)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>A10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>1.suga (M)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#LVM_MEDUS_00003_TreeSpecies">LVM_MEDUS_00003_TreeSpecies</a><p style='font-size:smaller; line-height: 0.5;'>1: 01 - Priede</p><p style='font-size:smaller; line-height: 0.5;'>3: 03 - Egle</p><p style='font-size:smaller; line-height: 0.5;'>4: 04 - Bērzs</p><p style='font-size:smaller; line-height: 0.5;'>6: 06 - Melnalksnis</p><p style='font-size:smaller; line-height: 0.5;'>8: 08 - Apse</p><p style='font-size:smaller; line-height: 0.5;'>9: 09 - Baltalksnis</p><p style='font-size:smaller; line-height: 0.5;'>10: 10 - Ozols</p><p style='font-size:smaller; line-height: 0.5;'>11: 11 - Osis</p><p style='font-size:smaller; line-height: 0.5;'>12: 12 - Liepa</p><p style='font-size:smaller; line-height: 0.5;'>...</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>S10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h2 style='color: lightblue; font-size: 24px; text-align: left; ' id='common_classes'> Kopējās elementu un objektu klases
                        </h2><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDBIOAUDZESRAKSTUROJUM'> Biotopa audzes raksturojumi [Objektu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDBIOAUDZESRAKSTUROJUM</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Objektu klase</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotops (VMDBIOTOPI)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotops].[Unikālais identifikators] <br> -> <br>[Biotopa audzes raksturojumi].[Sasaiste ar BIOTOPI]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Unikālais identifikators</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Bioaudzes_Raksturojumi_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sasaiste ar BIOTOPI</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Bio_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>procentuālais sugas daudzums</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Īsais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Koeficients</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>2</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sugas vecums</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Īsais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Vecums</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Suga</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_180_Koku_Sugas">VMD_180_Koku_Sugas</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>KokSug</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDBIOINDIKATORUSUGAS'> Biotopa indikatoru sugas [Objektu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDBIOINDIKATORUSUGAS</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Objektu klase</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotops (VMDBIOTOPI)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotops].[Unikālais identifikators] <br> -> <br>[Biotopa indikatoru sugas].[Sasaiste ar BIOTOPI]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Unikālais identifikators</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>BioIndikatoru_Sugas_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sasaiste ar BIOTOPI</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Bio_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Biotopa indikatoru suga</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_020_Biosugu_veidi">VMD_020_Biosugu_veidi</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p><p style='font-size:smaller; line-height: 0.5;'>100: Cits</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>BioSug_Type</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Biotopa indikatoru sugas sastopamība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_021_BioSugu_Sastopamiba">VMD_021_BioSugu_Sastopamiba</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Sast_Type</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDUGUNSGREKI'> Ugunsgrēki [Objektu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDUGUNSGREKI</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Objektu klase</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Ugunsgrēka vieta (VMDUGUNSGREKPOINT)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Ugunsgrēki].[Unikālais identifikators] <br> -> <br>[Ugunsgrēka vieta].[Sasaiste ar UGUNSGREKI]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Ugunsgrēka teritorija (VMDUGUNSGREKPOLY)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Ugunsgrēki].[Unikālais identifikators] <br> -> <br>[Ugunsgrēka teritorija].[Sasaiste ar UGUNSGREKI]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Ugunsgrēku platības uzskaite (VMDUGUNSPLATIBAS)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Ugunsgrēki].[Unikālais identifikators] <br> -> <br>[Ugunsgrēku platības uzskaite].[Identifikators sasaistei]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Unikālais identifikators</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Ugunsgreki_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Ugunscēloņi</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_090_Ugunsceloni">VMD_090_Ugunsceloni</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Ucel_Type</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Trauksmes laiks</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Trauksme</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Uzsāk dzēšanu</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Usak</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Ierobežošanas laiks</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Ierobezo</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Likvidēšanas laiks</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Datums</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Likvide</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Ugunsgrēka atklāšanas veids</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_093_UgunsAtklType">VMD_093_UgunsAtklType</a><p style='font-size:smaller; line-height: 0.5;'>1: No torņa</p><p style='font-size:smaller; line-height: 0.5;'>2: Ziņo trešā persona</p><p style='font-size:smaller; line-height: 0.5;'>3: Ziņo VUGD</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>UATKL_TYPE</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDBIOATSLEGASELEMENTI'> Biotopa atslēgas elementi [Objektu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDBIOATSLEGASELEMENTI</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Objektu klase</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Objekta apakštipi</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Apraksts</th>
                    <tr>
                </thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>Ar apjomu un sugu</td>
            </tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>2</td>
                <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>Ar apjomu</td>
            </tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>1</td>
                <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>Bez apjoma</td>
            </tr>
            </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotops (VMDBIOTOPI)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotops].[Unikālais identifikators] <br> -> <br>[Biotopa atslēgas elementi].[Sasaiste ar BIOTOPI]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotopa atslēgas elementu sugas (VMDBIOELEMENTASUGAS)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotopa atslēgas elementi].[Unikālais identifikators] <br> -> <br>[Biotopa atslēgas elementu sugas].[Atslēgas identifikators (sasaistei)]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Unikālais identifikators</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>BioAtslegas_Elementi_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Atslēgas elementa apakštips</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>BioAtslegas_Elementi_ST</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>1</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sasaiste ar BIOTOPI</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Bio_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Atslēgas elementa veids</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_030_Bioelementa_Veidi_I">VMD_030_Bioelementa_Veidi_I</a><p style='font-size:smaller; line-height: 0.5;'>1: Dažādvecuma audze</p><p style='font-size:smaller; line-height: 0.5;'>2: Atvērumu vainaga klājā / lauces</p><p style='font-size:smaller; line-height: 0.5;'>3: Pašizretināšanās</p><p style='font-size:smaller; line-height: 0.5;'>4: Pastāvīgi pārplūstoši klajumi</p><p style='font-size:smaller; line-height: 0.5;'>5: Īslaicīgi pārplūstoši klajumi</p><p style='font-size:smaller; line-height: 0.5;'>6: Mirusi koksne dažās sadal. pakāpēs</p><p style='font-size:smaller; line-height: 0.5;'>7: Mirusi koksne vairākās sadal. pakāpēs</p><p style='font-size:smaller; line-height: 0.5;'>8: Daudz koksnes sēņu / piepju</p><p style='font-size:smaller; line-height: 0.5;'>9: Daudz vecu lazdu</p><p style='font-size:smaller; line-height: 0.5;'>...</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>ElemV_Type</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Atslēgas elementa apjoms</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_035_Bioelementa_Veida_Apjoms">VMD_035_Bioelementa_Veida_Apjoms</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav Zināms</p><p style='font-size:smaller; line-height: 0.5;'>1: 1-5</p><p style='font-size:smaller; line-height: 0.5;'>2: 6-10</p><p style='font-size:smaller; line-height: 0.5;'>3: >10</p><p style='font-size:smaller; line-height: 0.5;'>0: Nav definēts</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Apjoms_Type</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDBIOIZCERTAMIAPJOMI'> Biotopa apsaimniekošana – sugas izcirtes apjomi [Objektu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDBIOIZCERTAMIAPJOMI</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Objektu klase</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotopa apsaimniekošana – izcērtama suga (VMDBIOIZCERTAMASUGA)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotopa apsaimniekošana – izcērtama suga].[Unikālais identifikators] <br> -> <br>[Biotopa apsaimniekošana – sugas izcirtes apjomi].[Sasaiste ar BIOIZCERTAMA_SUGA]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sasaiste ar BIOIZCERTAMA_SUGA</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Izc_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>% no paaugas</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Īsais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>No_Paaugas</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>% no II stāva</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Īsais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>No_2Stava</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>% no I stāva</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Īsais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>No_1Stava</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Izcērtamo apjomu veids</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_170_Bioizcertami_apjomi_Types">VMD_170_Bioizcertami_apjomi_Types</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p><p style='font-size:smaller; line-height: 0.5;'>1: 100% platībā</p><p style='font-size:smaller; line-height: 0.5;'>2: 50% un > platībā</p><p style='font-size:smaller; line-height: 0.5;'>3: 50% un mazāk platībā</p><p style='font-size:smaller; line-height: 0.5;'>4: Paņēmienu skaits</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Apjoma_tipi</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDBIOAPSAIMNIEKOSANA'> Biotopa apsaimniekošana [Objektu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDBIOAPSAIMNIEKOSANA</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Objektu klase</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotops (VMDBIOTOPI)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotops].[Unikālais identifikators] <br> -> <br>[Biotopa apsaimniekošana].[Sasaiste ar BIOTOPI]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotopa apsaimniekošana – izcērtama suga (VMDBIOIZCERTAMASUGA)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotopa apsaimniekošana].[Unikālais identifikators] <br> -> <br>[Biotopa apsaimniekošana – izcērtama suga].[Sasaiste ar BIOAPSAIMNIEKOSANA]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Unikālais identifikators</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>BioApsaimniekosana_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sasaiste ar BIOTOPI</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Bio_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Bez saimnieciskās darbības?</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_000_Boolean">VMD_000_Boolean</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p><p style='font-size:smaller; line-height: 0.5;'>1: Jā</p><p style='font-size:smaller; line-height: 0.5;'>2: Nē</p><p style='font-size:smaller; line-height: 0.5;'>0: Nav ievadīts</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Bez_Darbibas</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>1</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Jāsaglabā buferjosla?</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_000_Boolean">VMD_000_Boolean</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p><p style='font-size:smaller; line-height: 0.5;'>1: Jā</p><p style='font-size:smaller; line-height: 0.5;'>2: Nē</p><p style='font-size:smaller; line-height: 0.5;'>0: Nav ievadīts</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Saglabat_Buferi</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>1</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Neizvākt sausos un kritušos kokus?</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_000_Boolean">VMD_000_Boolean</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p><p style='font-size:smaller; line-height: 0.5;'>1: Jā</p><p style='font-size:smaller; line-height: 0.5;'>2: Nē</p><p style='font-size:smaller; line-height: 0.5;'>0: Nav ievadīts</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Neizvakt_Sausos</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>1</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Nedrīkst nosusināt?</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_000_Boolean">VMD_000_Boolean</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p><p style='font-size:smaller; line-height: 0.5;'>1: Jā</p><p style='font-size:smaller; line-height: 0.5;'>2: Nē</p><p style='font-size:smaller; line-height: 0.5;'>0: Nav ievadīts</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Nenosusinat</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>1</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Jāizcērt pamežs?</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_000_Boolean">VMD_000_Boolean</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p><p style='font-size:smaller; line-height: 0.5;'>1: Jā</p><p style='font-size:smaller; line-height: 0.5;'>2: Nē</p><p style='font-size:smaller; line-height: 0.5;'>0: Nav ievadīts</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Jaizcert_Pamezs</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>1</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Piezīmes par apsaimniekošanu</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Piezimes</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDUGUNSPLATIBAS'> Ugunsgrēku platības uzskaite [Objektu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDUGUNSPLATIBAS</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Objektu klase</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Ugunsgrēki (VMDUGUNSGREKI)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Ugunsgrēki].[Unikālais identifikators] <br> -> <br>[Ugunsgrēku platības uzskaite].[Identifikators sasaistei]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Identifikators sasaistei</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Ugunsgreki_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Ugunscēloņi</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_091_Meza_piederiba">VMD_091_Meza_piederiba</a><p style='font-size:smaller; line-height: 0.5;'>PRV: Privātie</p><p style='font-size:smaller; line-height: 0.5;'>VLS: Valsts (izņemot AS ‘LVM’)</p><p style='font-size:smaller; line-height: 0.5;'>VAS: AS ‘Latvijas valsts meži’ meži</p><p style='font-size:smaller; line-height: 0.5;'>PSV: Pašvaldības</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Piedriba</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Platības zemes veids</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_092_UgunsPlatType">VMD_092_UgunsPlatType</a><p style='font-size:smaller; line-height: 0.5;'>1: Mežu platība</p><p style='font-size:smaller; line-height: 0.5;'>2: Jaunaudžu platība</p><p style='font-size:smaller; line-height: 0.5;'>3: Citu meža zemju platība</p><p style='font-size:smaller; line-height: 0.5;'>4: Citu nemeža zemju platība</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>PlatibaType</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Platība</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Precīzais daļskaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Platiba</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>7</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDBIOIEZIMES'> Biotopa īpašās iezīmes [Objektu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDBIOIEZIMES</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Objektu klase</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotops (VMDBIOTOPI)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotops].[Unikālais identifikators] <br> -> <br>[Biotopa īpašās iezīmes].[Sasaiste ar BIOTOPI]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Unikālais identifikators</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Bioiezimes_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sasaiste ar BIOTOPI</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Bio_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Īpašo iezīmju veids</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_050_Bioiezīmju_veidi">VMD_050_Bioiezīmju_veidi</a><p style='font-size:smaller; line-height: 0.5;'>1: Lielas ligzdas</p><p style='font-size:smaller; line-height: 0.5;'>2: Skudru pūžņi</p><p style='font-size:smaller; line-height: 0.5;'>3: Dzīvnieku alas</p><p style='font-size:smaller; line-height: 0.5;'>4: Dzīvnieku "vannas"</p><p style='font-size:smaller; line-height: 0.5;'>5: Laukakmeņi</p><p style='font-size:smaller; line-height: 0.5;'>6: Pamatieža atsegums</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>IezV_Type</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>2</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Skaits</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Īsais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Skaits</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>2</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Apraksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Teksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Apraksts</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDBIOIZCERTAMASUGA'> Biotopa apsaimniekošana – izcērtama suga [Objektu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDBIOIZCERTAMASUGA</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Objektu klase</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotopa apsaimniekošana – sugas izcirtes apjomi (VMDBIOIZCERTAMIAPJOMI)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotopa apsaimniekošana – izcērtama suga].[Unikālais identifikators] <br> -> <br>[Biotopa apsaimniekošana – sugas izcirtes apjomi].[Sasaiste ar BIOIZCERTAMA_SUGA]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotopa apsaimniekošana (VMDBIOAPSAIMNIEKOSANA)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotopa apsaimniekošana].[Unikālais identifikators] <br> -> <br>[Biotopa apsaimniekošana – izcērtama suga].[Sasaiste ar BIOAPSAIMNIEKOSANA]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Unikālais identifikators</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>BioIzcertamaSuga_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sasaiste ar BIOAPSAIMNIEKOSANA</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Aps_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Izcirtes veids</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_171_Bioizcertama_suga_Types">VMD_171_Bioizcertama_suga_Types</a><p style='font-size:smaller; line-height: 0.5;'>1: Izciršana</p><p style='font-size:smaller; line-height: 0.5;'>2: Izciršana ap biokokiem</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>BioIzcertamaSuga_tips</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>3</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Skaits</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Skaits</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Suga</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_180_Koku_Sugas">VMD_180_Koku_Sugas</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>KokSug</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDBIOELEMENTASUGAS'> Biotopa atslēgas elementu sugas [Objektu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDBIOELEMENTASUGAS</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Objektu klase</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotopa atslēgas elementi (VMDBIOATSLEGASELEMENTI)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotopa atslēgas elementi].[Unikālais identifikators] <br> -> <br>[Biotopa atslēgas elementu sugas].[Atslēgas identifikators (sasaistei)]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Suga</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_180_Koku_Sugas">VMD_180_Koku_Sugas</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>KokSug</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Atslēgas identifikators (sasaistei)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>BioAtslegas_Elementi_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDBIONEGATIVITRAUC'> Biotopa negatīvi traucējumi [Objektu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDBIONEGATIVITRAUC</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Objektu klase</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Biotops (VMDBIOTOPI)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Biotops].[Unikālais identifikators] <br> -> <br>[Biotopa negatīvi traucējumi].[Sasaiste ar BIOTOPI]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Unikālais identifikators</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>BioNegativiTraucejumi_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sasaiste ar BIOTOPI</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Bio_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Biotopa negatīvo traucējumu veids</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_040_BioTraucejumu_Veidi">VMD_040_BioTraucejumu_Veidi</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Trauc_Type</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Intensitāte</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_041_BioTraucējumu_Intensitate">VMD_041_BioTraucējumu_Intensitate</a><p style='font-size:smaller; line-height: 0.5;'>1: 1</p><p style='font-size:smaller; line-height: 0.5;'>2: 2</p><p style='font-size:smaller; line-height: 0.5;'>3: 3</p><p style='font-size:smaller; line-height: 0.5;'>4: 4</p><p style='font-size:smaller; line-height: 0.5;'>5: 5</p><p style='font-size:smaller; line-height: 0.5;'>6: 6</p><p style='font-size:smaller; line-height: 0.5;'>7: 7</p><p style='font-size:smaller; line-height: 0.5;'>8: 8</p><p style='font-size:smaller; line-height: 0.5;'>9: 9</p><p style='font-size:smaller; line-height: 0.5;'>...</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Intensitate</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>1</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMDVAIEROBEZOJUMI'> Vides aizsardzības ierobežojumi [Objektu klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>VMDVAIEROBEZOJUMI</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Objektu klase</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Relācijas</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Datu objekts</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Atslēgas atribūti</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Kardinalitāte</th>
                    <tr>
                <thead>
                
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '> Vides aizsardzības klasifikators (VMDVAKLASIFIKATORS)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><br>[Vides aizsardzības klasifikators].[Unikālais identifikators] <br> -> <br>[Vides aizsardzības ierobežojumi].[Sasaiste ar VA klasifikatoru]</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>1:N</td>
            <tr>
            </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Identifikators (OID)</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>OBJECTID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Ierobežojuma nosaukums</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_150_VA_IerobezojumuVeidi">VMD_150_VA_IerobezojumuVeidi</a><p style='font-size:smaller; line-height: 0.5;'>-1: Nav zināms</p></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Sasaiste ar VA klasifikatoru</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>VAK_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='RC_BIO_KONC_LINK'> RC_BIO_KONC_LINK [Relāciju klase]</h3>
        <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>    
        
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>RC_BIO_KONC_LINK</td>
                </tr>
                
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 85mm; border: 1px solid black; padding: 5px; '>Objekta tips</td>
                    <td style='text-align: left; background-color: #ffffff; width: 85mm; border: 1px solid black; padding: 5px; '>Relāciju klase</td>
                </tr>
                </table><br><h5 style='color: black; text-align: left; '>Datu objekta atribūti</h5>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <thead>
                    <tr>
                        <th style='text-align: left; background-color: #d3d3d3; width: 20mm; border: 1px solid black; padding: 5px; '>Nosaukums</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 40mm; border: 1px solid black; padding: 5px; '>Tips</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 25mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Precizitāte</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Noklusētā vērtība</th>
                        <th style='text-align: left; background-color: #d3d3d3; width: 10mm; border: 1px solid black; padding: 5px; '>Obligāts</th>
                    </tr>
                <thead>
            
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Biotopa identifikators (sasaistei)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>BiotopsFK_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>Koncentrācijas vietas identifikators (sasaistei)</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '>Garais skaitlis</td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>BioKoncentracijaFK_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>10</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '>Jā</td>
            </tr>
        
            <tr>
                <td style='text-align: left; background-color: #ffffff; width: 20mm; border: 1px solid black; padding: 5px; '>ES Biotops</td>
                <td style='text-align: left; background-color: #ffffff; width: 40mm; border: 1px solid black; padding: 5px; '><a href="#VMD_070_Biotopi_ES">VMD_070_Biotopi_ES</a></td>
                <td style='text-align: left; background-color: #ffffff; width: 25mm; border: 1px solid black; padding: 5px; '>Estips_ID</td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
                <td style='text-align: left; background-color: #ffffff; width: 10mm; border: 1px solid black; padding: 5px; '></td>
            </tr>
        </table><br><h2 style='color: lightblue; font-size: 24px; text-align: left; ' id='cvd'> Klasifikatori
                        </h2><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='TemplateCodedValueDomain'> TemplateCodedValueDomain </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>TemplateCodedValueDomain</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>1 - Code1 <br>2 - Code2 <br>3 - Code3 <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-</td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_012_SugasVeids'> Putnu sugas </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_012_SugasVeids</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-1 - Nav zināms <br>1 - Dzīvnieks <br>2 - Augs <br>3 - Sūna <br>4 - Ķērpis <br>5 - Sēne <br>6 - IAMB <br>100 - Cits <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDBIOTOPI'> Biotops </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_020_Biosugu_veidi'> Biotopa indikatoru sugu veidi </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_020_Biosugu_veidi</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-1 - Nav zināms <br>100 - Cits <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDBIOINDIKATORUSUGAS'> Biotopa indikatoru sugas </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_081_BioKoncentracija_Infrastruktura'> Biokoncentrācijas vietu infrastruktūras tips </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_081_BioKoncentracija_Infrastruktura</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>1 - 1. Priežu meži ar dažādvecuma kokiem <br>2 - 2. Lapu koku pionierfāzes meži <br>3 - 3. Meži ar dažādu pašizrobošanās dinamiku <br>3A - 3a. Slapjie egļu meži un pārējie egļu meži <br>3B - 3b. Slapjie melnalkšņu un platlapju meži <br>3C - 3c. Platlapju meži <br>3AB - 3ab. Slapjie egļu meži un pārējie egļu meži; Slapjie melnalkšņu un platlapju meži <br>3AC - 3ac. Slapjie egļu meži un pārējie egļu meži; Platlapju meži <br>3BC - 3b. Slapjie melnalkšņu un platlapju meži; Platlapju meži <br>3ABC - 3a. Slapjie egļu meži un pārējie egļu meži; Slapjie melnalkšņu un platlapju meži; Platlapju meži <br>4 - 4. Ģeoloģiskās uzbūves nosacītie lineārie biotopi <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDBIOKONCENTRACIJA'> Biotopu koncentrācijas vieta </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_180_Koku_Sugas'> Koku sugas </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_180_Koku_Sugas</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-1 - Nav zināms <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDBIOAUDZESRAKSTUROJUM'> Biotopa audzes raksturojumi </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDBIOIZCERTAMASUGA'> Biotopa apsaimniekošana – izcērtama suga </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDBIOELEMENTASUGAS'> Biotopa atslēgas elementu sugas </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_070_Biotopi_ES'> ES Biotopa tips </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_070_Biotopi_ES</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Relāciju klase:&nbsp</p><a href='#RC_BIO_KONC_LINK'> RC_BIO_KONC_LINK </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_093_UgunsAtklType'> Ugunsgrēka atklāšanas veids </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_093_UgunsAtklType</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>1 - No torņa <br>2 - Ziņo trešā persona <br>3 - Ziņo VUGD <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDUGUNSGREKPOLYVIEW'> Ugunsgrēka teritorijas skatījums </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDUGUNSGREKI'> Ugunsgrēki </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDUGUNSGREKPOINTVIEW'> VMD Ugunsgrēka vietas skatījums </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_041_BioTraucējumu_Intensitate'> Biotopa traucējumu intensitāte </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_041_BioTraucējumu_Intensitate</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>1 - 1 <br>2 - 2 <br>3 - 3 <br>4 - 4 <br>5 - 5 <br>6 - 6 <br>7 - 7 <br>8 - 8 <br>9 - 9 <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDBIONEGATIVITRAUC'> Biotopa negatīvi traucējumi </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='LVM_MEDUS_00003k_ShrubSpecies'> Krūmu sugu klasifikators </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>LVM_MEDUS_00003k_ShrubSpecies</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>30 - 30 - Kārkli <br>31 - 31 - Paegļi <br>33 - 33 - Krūkļi <br>34 - 34 - Lazdas <br>36 - 36 - Sausserži <br>37 - 37 - Irbenes <br>38 - 38 - Segliņi <br>39 - 39 - Ribes-sp. <br>40 - 40 - Korintes <br>41 - 41 - Vilkābeles <br>42 - 42 - Jasmīni <br>43 - 43 - Plūškoki <br>44 - 44 - Spirejas <br>45 - 45 - Ceriņi <br>46 - 46 - Klintenes <br>47 - 47 - Bārbeles <br>48 - 48 - Grimoņi <br>49 - 49 - Rozes <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-</td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_080_Vertejums'> Vērtējums </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_080_Vertejums</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-1 - Nav zināms <br>1 - Zems <br>2 - Vidējs <br>3 - Augsts <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDBIOTOPI'> Biotops </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDBIOKONCENTRACIJA'> Biotopu koncentrācijas vieta </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_010_BioInfoAvoti'> Biotopa informācijas avoti </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_010_BioInfoAvoti</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-1 - Nav zināms <br>1 - Meža valsts reģistrs <br>2 - Topogrāfiskā karte <br>3 - Vietējais mežsargs/iedzīvotājs <br>4 - Citas kartes <br>5 - Citi pētījumi <br>6 - Atrasts nejauši lauku darbu gaitā <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDBIOTOPI'> Biotops </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_100_DzivnSugas'> Dzīvnieku sugas </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_100_DzivnSugas</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>1 - Alnis <br>2 - Staltbriedis <br>3 - Meža cūka <br>4 - Stirna <br>5 - Bebrs <br>6 - Mednis <br>7 - Rubenis <br>8 - Lūsis <br>9 - Vilks <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDAnimalCount'> VMD dzīvnieku uzskaite </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_031_Bioelementa_Veidi_II'> Biotopa atslēgas elementu veidi (Ar apjomu) </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_031_Bioelementa_Veidi_II</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>14 - Ciņi ar pamatnēm <br>15 - Koki ar deguma rētām <br>16 - Dobumaini koki <br>17 - Dzeņveidīgo sakalti koki <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDBIOATSLEGASELEMENTI'> Biotopa atslēgas elementi </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_190_AAT'> Augšanas apstākļu tipi </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_190_AAT</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-1 - Nav zināms <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDBIOTOPI'> Biotops </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='LVM_00202_LVMForestry'> LVM mežsaimniecības </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>LVM_00202_LVMForestry</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>! - Vērtības no slāņa LVMForestry <br>? - ??? <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDUGUNSGREKPOLY'> Ugunsgrēka teritorija </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDUGUNSGREKPOLYVIEW'> Ugunsgrēka teritorijas skatījums </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDUGUNSGREKPOINT'> Ugunsgrēka vieta </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDUGUNSGREKPOINTVIEW'> VMD Ugunsgrēka vietas skatījums </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_171_Bioizcertama_suga_Types'> Izciršanas veidi </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_171_Bioizcertama_suga_Types</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>1 - Izciršana <br>2 - Izciršana ap biokokiem <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDBIOIZCERTAMASUGA'> Biotopa apsaimniekošana – izcērtama suga </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_120_PeduSkaitaTips'> Pēdu skaita novērtējuma tipi </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_120_PeduSkaitaTips</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>1 - Precīzi <br>2 - Neprecīzi <br>3 - Pieņēmums <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-</td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_090_Ugunsceloni'> Ugunsgrēka cēloņi </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_090_Ugunsceloni</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-1 - Nav zināms <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDUGUNSGREKPOLYVIEW'> Ugunsgrēka teritorijas skatījums </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDUGUNSGREKI'> Ugunsgrēki </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDUGUNSGREKPOINTVIEW'> VMD Ugunsgrēka vietas skatījums </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_050_Bioiezīmju_veidi'> Biotopa īpašo iezīmju veidi </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_050_Bioiezīmju_veidi</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>1 - Lielas ligzdas <br>2 - Skudru pūžņi <br>3 - Dzīvnieku alas <br>4 - Dzīvnieku "vannas" <br>5 - Laukakmeņi <br>6 - Pamatieža atsegums <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDBIOIEZIMES'> Biotopa īpašās iezīmes </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_030_Bioelementa_Veidi_I'> Biotopa atslēgas elementu veidi (Bez apjoma) </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_030_Bioelementa_Veidi_I</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>1 - Dažādvecuma audze <br>2 - Atvērumu vainaga klājā / lauces <br>3 - Pašizretināšanās <br>4 - Pastāvīgi pārplūstoši klajumi <br>5 - Īslaicīgi pārplūstoši klajumi <br>6 - Mirusi koksne dažās sadal. pakāpēs <br>7 - Mirusi koksne vairākās sadal. pakāpēs <br>8 - Daudz koksnes sēņu / piepju <br>9 - Daudz vecu lazdu <br>10 - Vismaz 4 dažādu sugu platlapji <br>11 - Avotu ietekme <br>12 - Bebru darbības pēdas <br>13 - Dabīgās ūdensteces <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDBIOATSLEGASELEMENTI'> Biotopa atslēgas elementi </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='LVM_00201_LVMDistricts'> LVM meža iecirkņi </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>LVM_00201_LVMDistricts</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>kodi - Vērtības no slāņa LVMDistrict <br>??? - ??? <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDUGUNSGREKPOLY'> Ugunsgrēka teritorija </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDUGUNSGREKPOLYVIEW'> Ugunsgrēka teritorijas skatījums </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDUGUNSGREKPOINT'> Ugunsgrēka vieta </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDUGUNSGREKPOINTVIEW'> VMD Ugunsgrēka vietas skatījums </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='LVM_MEDUS_00003_TreeSpecies'> Koku sugu klasifikators </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>LVM_MEDUS_00003_TreeSpecies</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>1 - 01 - Priede <br>3 - 03 - Egle <br>4 - 04 - Bērzs <br>6 - 06 - Melnalksnis <br>8 - 08 - Apse <br>9 - 09 - Baltalksnis <br>10 - 10 - Ozols <br>11 - 11 - Osis <br>12 - 12 - Liepa <br>13 - 13 - Lapegle <br>14 - 14 - Citas priedes <br>15 - 15 - Citas egles <br>16 - 16 - Goba,vīksna <br>17 - 17 - Dižskābardis <br>18 - 18 - Skābardis <br>19 - 19 - Papele <br>20 - 20 - Vītols <br>21 - 21 - Blīgzna <br>22 - 22 - Ciedru priede <br>23 - 23 - Baltegle <br>24 - 24 - Kļava <br>25 - 25 - Saldais ķirsis <br>26 - 26 - Mežābele <br>27 - 27 - Bumbiere <br>28 - 28 - Duglāzija <br>29 - 29 - Īve <br>32 - 32 - Pīlādži <br>35 - 35 - Ievas <br>50 - 50 - Dzeltenā akācija <br>61 - 61 - Citi ozoli <br>62 - 62 - Citas liepas <br>63 - 63 - Citas kļavas <br>64 - 64 - Citi oši <br>65 - 65 - Citas gobas, vīksnas <br>66 - 66 - Riekstkoki <br>67 - 67 - Zirgkastaņi <br>68 - 68 - Hibrīdā apse <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDUGUNSGREKPOLY'> Ugunsgrēka teritorija </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDUGUNSGREKPOLYVIEW'> Ugunsgrēka teritorijas skatījums </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDUGUNSGREKPOINT'> Ugunsgrēka vieta </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDUGUNSGREKPOINTVIEW'> VMD Ugunsgrēka vietas skatījums </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_170_Bioizcertami_apjomi_Types'> Izcērtamo apjomu veidi </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_170_Bioizcertami_apjomi_Types</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-1 - Nav zināms <br>1 - 100% platībā <br>2 - 50% un > platībā <br>3 - 50% un mazāk platībā <br>4 - Paņēmienu skaits <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDBIOIZCERTAMIAPJOMI'> Biotopa apsaimniekošana – sugas izcirtes apjomi </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_035_Bioelementa_Veida_Apjoms'> Bioelementu veida apjomi </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_035_Bioelementa_Veida_Apjoms</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-1 - Nav Zināms <br>1 - 1-5 <br>2 - 6-10 <br>3 - >10 <br>0 - Nav definēts <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDBIOATSLEGASELEMENTI'> Biotopa atslēgas elementi </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_000_Boolean'> Bināra izvēle </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_000_Boolean</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-1 - Nav zināms <br>1 - Jā <br>2 - Nē <br>0 - Nav ievadīts <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDVAKLASIFIKATORS'> Vides aizsardzības klasifikators </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDBIOAPSAIMNIEKOSANA'> Biotopa apsaimniekošana </a></div><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDBIOKONCENTRACIJA'> Biotopu koncentrācijas vieta </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_091_Meza_piederiba'> Meža piederība </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_091_Meza_piederiba</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>PRV - Privātie <br>VLS - Valsts (izņemot AS ‘LVM’) <br>VAS - AS ‘Latvijas valsts meži’ meži <br>PSV - Pašvaldības <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDUGUNSPLATIBAS'> Ugunsgrēku platības uzskaite </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_161_KokuSugas'> Koku sugas </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_161_KokuSugas</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-1 - Nav zināms <br>100 - Cits <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-</td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_013_StatussVeids'> Putnu sugas </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_013_StatussVeids</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-1 - Nav zināms <br>P - Paplašinājums (P) <br>P30-70 - Paplašinājums (P30-70) <br>B - Buferjosla (B) <br>BP - Buferjosla (BP) <br>B30-70 - Buferjosla (B30-70) <br>I - Ieslēgums (I) <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDBIOTOPI'> Biotops </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_150_VA_IerobezojumuVeidi'> Vides aizsardzības ierobežojumu veidi </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_150_VA_IerobezojumuVeidi</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-1 - Nav zināms <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDVAIEROBEZOJUMI'> Vides aizsardzības ierobežojumi </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_021_BioSugu_Sastopamiba'> Biotopa indikatoru sugu sastopamība </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_021_BioSugu_Sastopamiba</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-1 - Nav zināms <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDBIOINDIKATORUSUGAS'> Biotopa indikatoru sugas </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_011_Bionosaukumi'> Biotopa nosaukumi </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_011_Bionosaukumi</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-1 - Nav zināms <br>A1 - Skujkoku mežs <br>A2 - Mistrots skujkoku-lapukoku mežs <br>B1 - Platlapju mežs <br>B2 - Apšu mežs <br>B3 - Cits lapukoku mežs <br>C1 - Slapjš melnalkšņu mežs <br>C2 - Egļu un mistrots egļu slapjais mežs <br>C3 - Priežu un bērzu slapjais mežs <br>C4 - Platlapju slapjais mežs <br>D1 - Gravas mežs <br>D2 - Nogāzes mežs <br>D3 - Krastmalas mežs <br>D4 - Avotains mežs <br>D5 - Kaļķains skujkoku mežs <br>D6 - Kaļķains zāļu purvs vai pļava <br>D7 - Purva vai meža mozaīka <br>E1 - Dedzis mežs <br>E2 - Bioloģiski nozīmīga bebraine <br>E3 - Biokoks <br>E4 - Vējgāzes mežs <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Elementu klase:&nbsp</p><a href='#VMDBIOTOPI'> Biotops </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_040_BioTraucejumu_Veidi'> Biotopa traucējumu veidi </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_040_BioTraucejumu_Veidi</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-1 - Nav zināms <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDBIONEGATIVITRAUC'> Biotopa negatīvi traucējumi </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_092_UgunsPlatType'> Ugunsgrēku platību uzskaites tips </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_092_UgunsPlatType</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>1 - Mežu platība <br>2 - Jaunaudžu platība <br>3 - Citu meža zemju platība <br>4 - Citu nemeža zemju platība <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDUGUNSPLATIBAS'> Ugunsgrēku platības uzskaite </a></div></td>
                </tr>
            </table> <br>
            <h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_032_Bioelementa_Veidi_III'> Biotopa atslēgas elementu veidi (Ar apjomu un sugu) </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_032_Bioelementa_Veidi_III</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Vērtības</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>18 - Bioloģiski veci koki <br>19 - Mazu dimensiju lēni augoši veci koki <br>20 - Saulei atklāti veci platl. koki <br>21 - Krituši koki ar mizu <br>22 - Krituši koki bez mizas <br>23 - Nokrituši kaistoši koki <br>24 - Stumbeņi <br></td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '><div style='width: 100%; display: flex; flex-direction: row; align-items: center; ''><p>Objektu klase:&nbsp</p><a href='#VMDBIOATSLEGASELEMENTI'> Biotopa atslēgas elementi </a></div></td>
                </tr>
            </table> <br>
            <h2 style='color: lightblue; font-size: 24px; text-align: left; ' id='range_domains'> Vērtību robežas
                        </h2><h3 style='color: lightblue; font-size: 18px; text-align: left; ' id='VMD_RD_Procenti'> Procenti (0-100%) </h3>
            <table style='width: 180mm; border: 1px solid black; border-collapse: collapse; padding: 5px; '>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Nosaukums DB</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>VMD_RD_Procenti</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Minimālā vērtība</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>1</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Maksimālā vērtība</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>100</td>
                </tr>
                <tr>
                    <td style='text-align: left; background-color: #d3d3d3; width: 90mm; border: 1px solid black; padding: 5px; '>Izmantots objektu klasēs:</td>
                    <td style='text-align: left; background-color: #ffffff; width: 90mm; border: 1px solid black; padding: 5px; '>-</td>
                </tr>
            </table> <br>
            </div>
        </body>
        </html>
        