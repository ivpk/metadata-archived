Lietuvos valstybinių įstaigų duomenų inventorizacija
####################################################

Čia rasite informaciją apie tai, kaip atlikti turimų duomenų inventorizaciją ir
kaip pateikti prašymą duomenims gauti.

Duomenų inventorizacija bus atliekama skaičiuoklės failuose, šiuo metu
palaikomi formatai yra ODS ir XSLX. XLS formato naudoti nerekomenduojama,
kadangi tai yra nebepalaikomas ir uždaras formatas, kurį sudėtingai nuskaityti
automatinėmis priemonėmis. Ateityje planuojam išplėsti formatų palaikymą
suteikiant galimybę inventorizuoti duomenis JSON ir YAML formatais, pateikianti
prašymus ar inventorizacijos rezultatus per API.

Ši iniciatyva yra eksperimentinėje stadijoje, kurioje keli atrinkti duomenų
tiekėjai ir naudotojai atliks savo duomenų inventorizacija ir pateiks prašymus
gauti duomenis. Proceso metu aprašytos instrukcijos ir skaičiuoklės lentelių
struktūra gali keistis.

Skaičiuoklėje turi būti trys lakštai tokiais pavadinimais:

- **Inventorizacija**

- **Žodynas**

- **Poreikis**


Skaičiuoklės lakštas „Inventorizacija“
======================================

Šiame lakšte ``A`` stulpelyje turi būti rašomi laukų pavadinimai, o ``B`` ir
kituose stulpeliuose rašomos ``A`` stulpelyje nurodyto lauko reikšmės. Kokia
tiksliai reikšmė ir kaip ją įrašyti priklauso nuo lauko pavadinimo.

Lentelės pavyzdys:

+----+-------------------+-----------------+-----------+-------------+------------------+-------------------+-------------------+-------------------+-------------+-------------+
|    | A                 | B               | C         | D           | E                | F                 | G                 | H                 | I           | J           |
+----+-------------------+-----------------+-----------+-------------+------------------+-------------------+-------------------+-------------------+-------------+-------------+
| 1  | **Tiekėjas**      | Informacinės visuomenės plėtros komitetas prie susisiekimo ministerijos                                                                              |
+----+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2  | **Paketas**       | Informacijos rinkmenų sąrašas                                                                                                                        |
+----+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3  | **DCAT URI**      | http://ckan.opendata.gov.lt/dataset/informacijos-rinkmen-sraas                                                                                       |
+----+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 4  | **Resursas**      | Rinkmenos                                                                                                                                            |
+----+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 5  | **DCAT URI**      |                                                                                                                                                      |
+----+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 6  | **Formatas**      | mysql                                                                                                                                                |
+----+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 7  | **Adresas (DSN)** |                                                                                                                                                      |
+----+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 8  | **Klasė**         | DuomenųPaketas                                                                                                                                       |
+----+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 9  | **Tas pats kaip** | dcat:Dataset                                                                                                                                         |
+----+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 10 | **Šaltinis**      | t_rinkmena                                                                                                                                           |
+----+-------------------+-----------------+-----------+-------------+------------------+-------------------+-------------------+-------------------+-------------+-------------+
| 11 | **Schema**        | **Pavadinimas** | **Klasė** | **Nuoroda** | **Šaltinis**     | **Duomenų tipas** | **Tas pats kaip** | **Brandos lygis** | **Pradžia** | **Pabaiga** |
+----+-------------------+-----------------+-----------+-------------+------------------+-------------------+-------------------+-------------------+-------------+-------------+
| 12 |                   | pavadinimas     | str       |             | PAVADINIMIAS     | str               | dct:title         |                   |             |             |
+----+-------------------+-----------------+-----------+-------------+------------------+-------------------+-------------------+-------------------+-------------+-------------+
| 13 |                   | žymė            | str       |             | R_ZODZIAI        | str               | dcat:keyword      | 1                 |             |             |
+----+-------------------+-----------------+-----------+-------------+------------------+-------------------+-------------------+-------------------+-------------+-------------+


``A`` stulpelyje esantys laukai yra kontekstiniai, tai reiškia, kad pavyzdžiui
**DCAT URI** esantis 3-ioje eilutėje yra paketo DCAT URI, tas pats laukas 5-oje
eilutėje yra Resurso **DCAT URI**. Žemiau rasite visų laukų sąrašą ir jų
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
  Duomenų paketas, DCAT ontologijoje vadinamas `dcat:Dataset`_, CKAN
  terminologijoje taip pat vadinamas Dataset_.

Resursas
  Duomenų rinkmena, konkretus CSV failas, lentelė ar kita esybė, DCAT
  ontologijoje vadinamas `dcat:Distribution`_, CKAN terminologijoje vadinamas
  Resource_.

DCAT URI
  Nuoroda į paketą arba resursą priklausomai nuo konteksto, kuriame šis laukyas
  yra panaudotas.

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

Adresas (DSN)
  Adresas iki duomenų šaltinio (`Data Source Name`_). Tam, kad įsitikinti, ar
  tai, kas pateikta schemoje, reikalingas veikiantis duomenų šaltinio adresas,
  kad automatizuoti įrankiai, galėtų prisijungti prie duomenų šaltinio ir
  patikrinti, ar schemoje pateikti duomenys yra teisingi.

  Be to, turint schema ir duomenų šaltinio adresą, galima iš karto atverti
  duomenis, jie duomenims nereikalinga jokia transformacija, susiejimas ar
  nuasmeninimas.

  Jei duomenų šaltinis yra uždara duomenų bazė, tokiu atveju, galima pateikti
  tam tikrą sutartinį duomenų šaltinio pavadinimą, pagal kurį būtų galima
  nustatyti prisijungimo prie duomenų bazės duomenis.

Klasė
  `Klasė`_ yra pavadinimas suteiktas objektų aibei, turinčių tas pačias
  savybes. Klasės pavadinimas turi būti aprašytas skaičiuoklės **Žodynas**
  lakšte.

Šaltinis
  Šaltinis objekto klasės tikslus adresas, taip kaip pateikta šaltinio duomenų
  struktūroje. Jei šaltinis yra reliacinė duomenų bazė, tuomet šaltinio
  pavadinimas turi būti lentelės pavadinimas, jei šaltinis yra XML arba HTML
  failas, tada šaltinis turi būti XPath kelias iki duomenų.

  Turint tikslų šaltinio pavadinimą, duomenys gali būti patikrinami
  automatizuotai, tada pagal nurodytą klasę susiejami su kitais duomenimis iš
  kitų šaltinių.

  Keli skirtingi šaltiniai gali turėti tą pačią klasę.

Schema
  Schema yra dar viena lentelė, kurioje pateikiamas šaltinio laukų sąrašas.

  Pavadinimas
    Lauko pavadinimas, naudojant pavadinimą iš **Žodynas** skaičiuoklės lakšto,
    ten pat yra aprašyti ir **Klasių** pavadinimai.

  Klasė
    Laukai gali būti skaliariniai ir rodantys į kitas klases. Tais atvejais,
    kai laukas rodo į kitą klasę, reikia nurodyti klasės pavadinimą, vėl iš
    „Žodynas“ lakšte aprašyto žodyno. Jei laukas yra skaliarinis, tada reikia
    nurodyti vieną iš šių tipų:

    - bool
    - bytes
    - float
    - int
    - str

  Nuoroda
    Tais atvejais, kai laukas rodo į kitą klasę, sąsaja su objektu į kurį
    rodoma žinoma pagal globalų objekto identifikatorių, tačiau dažniausiai yra
    naudojami ne globalūs, o lokalūs objekto identifikatoriai. Tokiu atveju,
    kai naudojamas lokalus objekto identifikatorius, nuoroda turi būti lauko
    pavadinimas iš klasės į kurią rodoma.

    Nuorodos lauko pavadinimas taip pat turi būti iš „Žodynas“ lakšto žodyno.

    Skaliariniai tipai nuorodų neturi.

  Šaltinis
    Lauko pavadinimas toks, kokį naudoja duomenų šaltinis.

  Duomenų tipas
    Lauko duomenų tipas, toks koks nurodytas šaltinyje.

  Tas pats kaip
    Ryšys su savybe iš žinomo išorinio žodyno, šio laukė prasmė atitinka
    `owl:sameAs`_ reikšmę ir šio lauko pagalba vidinį schemos žodyną galima
    susieti su `išoriniais žinomais žodynais`_.

  Brandos lygis
    Brandos lygiui naudojama `5stardata.info`_ vertinimo skalė, tik ji yra šiek
    tiek išplėsta įvertinant tarinio schemos žodyno naudojimą.

    +-----+-------------------------------------------------------------------------+
    | 0.0 | Duomenys nekaupiami, viešai neprieinami arba jų laisvą naudojamą        |
    |     | riboja licencija.                                                       |
    +-----+-------------------------------------------------------------------------+
    | 1.0 | Duomenys teikiami pagal atvirą licenciją, tačiau jie yra                |
    |     | nestruktūruoti.                                                         |
    +-----+-------------------------------------------------------------------------+
    | 2.0 | Duomenys yra struktūruoti, tačiau pateikti naudojant uždarus            |
    |     | ar nestandartizuotus formatus.                                          |
    +-----+-------------------------------------------------------------------------+
    | 3.0 | Duomenys yra struktūruoti ir teikiami atvirais formatais.               |
    +-----+-------------------------------------------------------------------------+
    | 3.5 | Duomenys susieti naudojant lokalius identifikatorius.                   |
    +-----+-------------------------------------------------------------------------+
    | 4.0 | Duomenys susieti naudojant globalius identifikatorius.                  |
    +-----+-------------------------------------------------------------------------+
    | 4.5 | Duomenų schema yra susieta su Lietuvos atvirų duomenų schemos žodynu.   |
    +-----+-------------------------------------------------------------------------+
    | 5.0 | Duomenų schema yra susieta su išoriniais ir plačiai naudojamais         |
    |     | žodynais.                                                               |
    +-----+-------------------------------------------------------------------------+

    Negalima suteikti didesnio brandos lygio balo, jei netenkinami vis žemiau
    esančių balų reikalavimai.

    Lietuvos atvirų duomenų schemos žodynas yra „Žodynas“ lakšte pateiktas
    žodynas.

  Pradžia ir Pabaiga
    Laikotarpis kurio metu šaltinio duomenų laukas buvo atvertas būtent tokiu
    brandos lygiu. Jei konkretaus lauko brandos lygis pasikeitė, tada laukas,
    tokiu pačiu pavadinimu turi būti įtrauktas į lentelę dar kartą, nurodant
    kitą pradžios ir pabaigos data.


Skaičiuoklės lakštas „Žodynas“
==============================

Žodyno lakšto lentelės pavyzdys:

+---+---+---+---+---+---+---+---+---+---+---+---+-----------+-------------------+
|   | A | B | C | D | E | F | G | H | I | J | K | L         | M                 |
+---+---+---+---+---+---+---+---+---+---+---+---+-----------+-------------------+
| 1 | **Klasių medis**                          | **Tipas** | **Tas pats kaip** |
+---+---+---+---+---+---+---+---+---+---+---+---+-----------+-------------------+
| 2 | **DuomenųPaketas**                        | Klasė     | dcat:Dataset      |
+---+---+---+---+---+---+---+---+---+---+---+---+-----------+-------------------+
| 3 |   | pavadinimas                           | str       | dct:title         |
+---+---+---+---+---+---+---+---+---+---+---+---+-----------+-------------------+
| 4 |   | žymė                                  | str       | dcat:keyword      |
+---+---+---+---+---+---+---+---+---+---+---+---+-----------+-------------------+
| 5 | **Asmuo**                                 | Klasė     | foaf:Person       |
+---+---+---+---+---+---+---+---+---+---+---+---+-----------+-------------------+
| 6 |   | vardas                                | Vardas    | foaf:firstName    |
+---+---+---+---+---+---+---+---+---+---+---+---+-----------+-------------------+
| 7 |   | pavardė                               | Pavardė   | foaf:familyName   |
+---+---+---+---+---+---+---+---+---+---+---+---+-----------+-------------------+
| 8 |   | **SeimoNarys**                        | Klasė     |                   |
+---+---+---+---+---+---+---+---+---+---+---+---+-----------+-------------------+
| 9 |   |   | frakcija                          | Frakcija  |                   |
+---+---+---+---+---+---+---+---+---+---+---+---+-----------+-------------------+

Skirtingi duomenų tiekėjai naudoja skirtingus žodžius toms pačioms klasės ar jų
savybėms apibūdinti. Standartizuoti žodynai dengia gan nedidelę dalį visų
sričių ir žodynų sudarymas naudojant OWL_ arba RDFS_ priemones reikalauja daug
pastangų ir laiko.

Todėl, kad išspręsti bendrojo žodyno problemą ir labai neapsisunkinti su
standartizuotais žodynais, naudojamas tarpinis Lietuvos atvirų duomenų žodynas
(LADŽ).

Kiekviena įstaiga inventorizuodama savo duomenis, turėtų naudoti žodyną, kuris
turėtų būti suvienodintas tarp skirtingų įstaigų.

Žodyne A-K stulpeliuose yra galimybė aprašyti klasių hierarchiją, tačiau
užtenka bent jau susitarti vienodus pavadinimus, naudojamus skirtinguose
duomenų šaltiniuose, o hierarchiją bus galima sutvarkyti vėliau, turint
pakankamai duomenų apie klases ir jų savybes.

Lakšte „Inventorizacija“, atliekamas susiejimas su LADŽ, kai jau susiejimas
padarytas, klasių hierarchiją galima pertvarkyti, nedarant įtakos
inventorizacijai.

Žinoma, jei keičiamas pavadinimas žodyne, reikėtų atitinkamai pakeisti
pavadinimus ir inventorizacijos lakštuose arba galima nurodyti, kad tam tikras
pavadinimas buvo pakeistas į naują pavadinimą ir senasis pavadinimas yra
nebenaudotinas.


Skaičiuoklės lakštas „Poreikis“
===============================

Lentelės pavyzdys:

+----+----------------------------+-----------------+-----------+-----------------+------------------+-------------------+
|    | A                          | B               | C         | D               | E                | F                 |
+----+----------------------------+-----------------+-----------+-----------------+------------------+-------------------+
| 1  | **Projektas**              | Atvirų duomenų portalas                                                              |
+----+----------------------------+--------------------------------------------------------------------------------------+
| 2  | **Aprašymas**              | Atvirų duomenų portalo tikslas atverti duomenis ir suteikti galimybę jais naudotis   |
|    |                            | visuomenei.                                                                          |
+----+----------------------------+--------------------------------------------------------------------------------------+
| 3  | **Naudotojų skaičius**     | **2015**        | **2016**  | **2017**        | **2018**         |                   |
+----+----------------------------+-----------------+-----------+-----------------+------------------+-------------------+
| 4  |                            | 100             | 2000      | 2500            | 3000             |                   |
+----+----------------------------+-----------------+-----------+-----------------+------------------+-------------------+
| 5  | **Ekonominė nauda**        | **2015**        | **2016**  | **2017**        | **2018**         |                   |
+----+----------------------------+-----------------+-----------+-----------------+------------------+-------------------+
| 6  |                            | 0               | 50        | 5000            | 7000             |                   |
+----+----------------------------+-----------------+-----------+-----------------+------------------+-------------------+
| 7  | **Klasė**                  | DuomenųPaketas                                                                       |
+----+----------------------------+-----------------+-----------+-----------------+------------------+-------------------+
| 8  | **Schema**                 | **Pavadinimas** | **Klasė** | **Prioritetas** | **Pradžia**      | **Pabaiga**       |
+----+----------------------------+-----------------+-----------+-----------------+------------------+-------------------+
| 9  |                            | pavadinimas     | str       |                 |                  |                   |
+----+----------------------------+-----------------+-----------+-----------------+------------------+-------------------+
| 10 |                            | žymė            | str       |                 |                  |                   |
+----+----------------------------+-----------------+-----------+-----------------+------------------+-------------------+

Labai panašiai kaip ir inventorizacijos lakšte, poreikio lakšte yra aprašomi
projektai, kurie naudoja arba naudotų atvirus duomenis.

Tokiu pavidalu, prašymus gauti duomenis gali teikti visuomenės atstovai, tačiau
taip pat pačios valstybinės įstaigos gali pateikti potencialių projektų
aprašymus vadovaujantis strateginėmis kryptimis, tokiu būdu nustatant duomenų
poreikį ir duomenų atvėrimo prioritetus.

Aprašant reikalingus duomenis taip pat naudojamas LADŽ žodynas. Naudojant
bendrą žodyną, galima susieti duomenų poreikio ir inventorizacijos duomenis.
Turint tokį susiejimą galima tiksliai išsiaiškinti kokie duomenys jau atverti,
koks yra atvertų duomenų brandos lygis, kokių duomenų trūksta, kokia potenciali
atveriamų duomenų ekonominė nauda ir pan.

Visuomenės atstovai, pateikia prašymą gauti duomenis ir naudodami bendrą
žodyną, gali gauti visus jiems reikalingus duomenis viename duomenų pakete. Tai
labai palengvintų atvertų duomenų integraciją į projektus.

Lygiai taip pat, kaip ir inventorizacijos atveju, ``A`` stulpelyje esantys
pavadinimai priklauso nuo konteksto::

  Projektas
    Aprašymas
    Naudotojų skaičius
    Ekonominė nauda
    Klasė
      Schema

Aprašymas, ką reiškia kiekvienas laukas:

Projektas
  Projekto pavadinimas. Projektas gali būti:
  
  - egzistuojantis projektas, kuris jau naudoja atvirus duomenis,

  - numatomas projektas, kuris naudotų atvirus duomenis,

  - valstybinių įstaigų aprašytas hipotetinis projektas, paremtas strateginėmis
    kryptimis, kuris galėtų naudoti aprašytus duomenis.

Aprašymas
  Trumpas projekto aprašymas, laisvu tekstu.

Naudotojų skaičius
  Pamatuotas esamų arba numatomų projekto naudotojų skaičius. Šis rodiklis
  turėtų būti atnaujinamas kiekvienais metais.

Ekonominė nauda
  Projekto generuojamas arba numatomas pelnas.

Klasė
  Klasė yra objektų aibė turinčių tas pačias savybes. Klasės pavadinimas turi
  būti iš „Žodynas“ lakšte esančio žodyno.

Schema
  Klasės laukų schema.

  Pavadinimas
    Lauko pavadinimas iš „Žodynas“ lakšto.

  Klasė
    Laukai gali būti skaliariniai ir rodantys į kitus objektus. Jei lauko
    reikšmė rodo į kitą objektą, tada turi būti nurodyta klasė iš „Žodynas“
    lakšto.

    Skaliariniai tipai gali būti tokie:

    - bool
    - bytes
    - float
    - int
    - str

  Prioritetas
    Reikšmė nuo 1 iki 3, nurodanti kaip svarbus tam tikras duomuo yra
    projektui.

    1
      Labai svarbus duomuo, be kurio projektas negali veikti.

    2
      Duomuo yra svarus, tačiau projektas gali veikti ir be to.

    3
      Duomuo nėra labai svarbus, galėtų būti panaudotas kuriant papildomas
      funkcijas.

  Pradžia ir Pabaiga
    Laikotarpis, kada šis duomuo buvo reikalingas projektui.

    Jei tarkim tas pats laukas projektui iš pradžių buvo nelabai reikalingas,
    o po to tapo labai reikalingas, tada tas pats laukas turėtų turėti du
    įrašus su skirtingais prioritetais ir pradžios ir pabaigos datomis.

    Jei laukas nebenaudojamas projektą, turi būti nurodoma pabaigos data, bet
    pats laukas turi būti paliktas lentelėje.


.. _`dcat:Dataset`: https://www.w3.org/TR/vocab-dcat/#class-dataset
.. _`dcat:Distribution`: https://www.w3.org/TR/vocab-dcat/#class-distribution
.. _Dataset: http://docs.ckan.org/en/latest/user-guide.html#datasets-and-resources
.. _Resource: http://docs.ckan.org/en/latest/user-guide.html#datasets-and-resources
.. _Data Source Name: https://en.wikipedia.org/wiki/Data_source_name
.. _Klasė: https://en.wikipedia.org/wiki/Class_(knowledge_representation)
.. _`owl:sameAs`: https://www.w3.org/TR/owl-ref/#sameAs-def
.. _išoriniais žinomais žodynais: http://lov.okfn.org/
.. _5stardata.info: http://5stardata.info/
.. _OWL: https://en.wikipedia.org/wiki/Web_Ontology_Language
.. _RDFS: https://en.wikipedia.org/wiki/RDF_Schema
