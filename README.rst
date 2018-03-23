Lietuvos valstybinių įstaigų duomenų inventorizacija
####################################################

Čia rasite informaciją apie tai, kaip atlikti turimų duomenų inventorizaciją ir
kaip pateikti prašymą duomenims gauti.

Duomenų inventorizacija bus atliekama skaičiuoklės failuose, šiuo metu
palaikomi formatai yra ODS ir XSLX. XLS formato naudoti nerekomenduojama,
kadangi tai yra nebepalaikomas ir uždaras formatas, kurį sudėtingai nuskaityti
automatinėmis priemonėmis.

Skaičiuoklėje turi būti trys lakštai tokiais pavadinimais:

- **Inventorizacija**

- **Schema**

- **Poreikis**


Skaičiuoklės lakštas „Inventorizacija“
======================================

Šiame lakšte ``A`` stulpelyje turi būti rašomi laukų pavadinimai, o ``B`` ir
kituose stulpeliuose rašomos ``A`` stulpelyje nurodyto lauko reikšmės. Kokia
tiksliai reikšmė ir kaip ją įrašyti priklauso nuo lauko pavadinimo.

Lentelės pavyzdys:

===  =============  ===========  =====  =======  ============  =============  =============  =============  =======  =======
     A              B            C      D        E             F              G              H              I        J
===  =============  ===========  =====  =======  ============  =============  =============  =============  =======  =======
 1   Tiekėjas       Informacinės visuomenės plėtros komitetas prie susisiekimo ministerijos
===  -------------  --------------------------------------------------------------------------------------------------------
 2   Paketas        Informacijos rinkmenų sąrašas
===  -------------  --------------------------------------------------------------------------------------------------------
 3   DCAT URI
===  -------------  -----------  -----  -------  ------------  -------------  -------------  -------------  -------  -------
 4   Resursas       Rinkmenos
===  -------------  -----------  -----  -------  ------------  -------------  -------------  -------------  -------  -------
 5   DCAT URI
===  -------------  -----------  -----  -------  ------------  -------------  -------------  -------------  -------  -------
 6   Formatas       mysql
===  -------------  -----------  -----  -------  ------------  -------------  -------------  -------------  -------  -------
 7   Adresas (DSN)
===  -------------  -----------  -----  -------  ------------  -------------  -------------  -------------  -------  -------
 8   Klasė          DuomenųPaketas
===  -------------  --------------------------------------------------------------------------------------------------------
 9   Šaltinis       t_rinkmena
===  -------------  -----------  -----  -------  ------------  -------------  -------------  -------------  -------  -------
10   Schema         Pavadinimas  Klasė  Nuoroda  Šaltinis      Duomenų tipas  Tas pats kaip  Brandos lygis  Pradžia  Pabaiga
===  -------------  -----------  -----  -------  ------------  -------------  -------------  -------------  -------  -------
11                  pavadinimas  str             PAVADINIMIAS  str            dct:title
===  -------------  -----------  -----  -------  ------------  -------------  -------------  -------------  -------  -------
12                  žymė         str             R_ZODZIAI     str            dcat:keyword   1
===  =============  ===========  =====  =======  ============  =============  =============  =============  =======  =======


``A`` stulpelyje esantys laukai yra kontekstiniai, tai reiškia, kad pavyzdžiui **DCAT URI** esantis 3-ioje eilutėje yra
paketo DCAT URI, tas pats laukas 5-oje eilutėje yra Resurso **DCAT URI**. Žemiau rasite visų laukų sąrašą ir jų
konteksto ribas::

  Tiekėjas
    Paketas
      DCAT URI
      Resursas
        DCAT URI
        Formatas
        Adresas (DSN)
        Klasė
        Šaltinis
        Schema

Aprašymas, ką reiškia kiekvienas laukas:

Tiekėjas
  Įstaigos, kuri teikia duomenis pavadinimas.

Paketas
  Duomenų paketas, DCAT ontologijoje vadinamas `dcat:Dataset`_, CKAN terminologijoje taip pat vadinamas Dataset_.

Resursas
  Duomenų rinkmena, konkretus CSV failas, lentelė ar kita esybė, DCAT ontologijoje vadinamas `dcat:Distribution`_, CKAN terminologijoje
  vadinamas Resource_.

DCAT URI
  Nuoroda į paketą arba resursą priklausomai nuo konteksto, kuriame šis laukyas yra panaudotas.

Formatas
  Nurodo kokiu formatu duomenys yra saugomi. Galimi variantai:

  - csv
  - html
  - json
  - mysql
  - ods
  - oracle
  - postgresql
  - tsv
  - xls
  - xlsx
  - xml


.. _`dcat:Dataset`: https://www.w3.org/TR/vocab-dcat/#class-dataset
.. _`dcat:Distribution`: https://www.w3.org/TR/vocab-dcat/#class-distribution
.. _Dataset: http://docs.ckan.org/en/latest/user-guide.html#datasets-and-resources
.. _Resource: http://docs.ckan.org/en/latest/user-guide.html#datasets-and-resources
