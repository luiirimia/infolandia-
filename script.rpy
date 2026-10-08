# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#intrebarile 

screen gata(): #ala gol
    pass

screen qdavid1():
    tag question
    vbox:
        align (0.5, 0.8)
        spacing 20

        add "qdavid1.png" xalign 0.5

screen qdavid3():
    tag question
    vbox:
        align (0.5, 0.8)
        spacing 20

        add "qdavid3.png" xalign 0.5

screen qandreea1():
    tag question
    vbox:
        align (0.5, 0.8)
        spacing 20

        add "qandreea1.png" xalign 0.5

screen qandreea2():
    tag question
    vbox:
        align (0.5, 0.8)
        spacing 20

        add "qandreea2.png" xalign 0.5

screen qandreea3():
    tag question
    vbox:
        align (0.5, 0.8)
        spacing 20

        add "qandreea3.png" xalign 0.5

screen qmaria1():
    tag question
    vbox:
        align (0.5, 1)
        spacing 20

        add "qmaria1.png" xalign 0.5
screen qmaria2():
    tag question
    vbox:
        align (0.5, 1)
        spacing 20

        add "qmaria2.png" xalign 0.5
screen qmaria3():
    tag question
    vbox:
        align (0.5, 0.9)
        spacing 20

        add "qmaria3.png" xalign 0.5

screen outrotab():
    tag question
    vbox:
        text "INFOLANDIA \nCreated by Luiza Irimia" at truecenter size 80




#definire grafici 
image scena:
    "scena.png"
    zoom 1.5
image outro:
    "outro.png"
    zoom 10.0

define la = Character("Frank")
define mc = Character("[mcname]")
define d = Character("David Șamanul Șirurilor")
define a = Character("Andreea Regina Recursivității")
define m = Character("Maria Cuceritoarea Codurilor")

default score = 0
# The game starts here.

label start:
    $ score = 0
    #nume personajul tau
    $ mcname = renpy.input("Cine va fi urmatorul campion al Infolandiei?")
    $ mcname = mcname.strip()

    if mcname == "":
        $ mcname = "Tu"


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene scena
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show frank okk
    with dissolve

    # These display lines of dialogue.

    la "Buna seara tuturor!"
    hide frank okk
    show frank vb
    with dissolve
    la "Buna seara spectatori!"
    la "Bine v-am gasit la cea mai noua si spectaculoasa editie a Campionatului de Cod din Infolandia!"
    hide frank vb
    show frank okk
    with dissolve
    "*se aud aplauze in fundal*"

    la "In aceasta seara, cei mai priceputi maestri ai codurilor vor putea sa-si arate abilitatile in fata dumneavoastra printr-o serie de probleme pe care le vor rezolva..."
    la "Cu foarte multa pricepere!"
    la "Ii invitam pe aceasta scena pe campionii pe care ii cunoasteti din editiile trecute!"

    hide frank okk 

    show david okk
    with dissolve 

    la "David Șamanul Șirurilor!"
    hide david okk

    show andreea okk
    with dissolve

    la "Andreea Regina Recursivitatii!" 
    hide andreea okk

    show larisa okk
    with dissolve

    la "Maria Cuceritoarea Codurilor!"

    hide larisa okk 

    show frank vb
    with dissolve
    la "Iar spre surprinderea voastra lista nu se termina aici!"
    la "In acest an avem si un NOU luptator al informaticii!"
    hide frank vb
    show frank okk
    la "Sa-l primim cu aplauze calde pe..."
    la "[mcname]!"
    la "Toata lumea se intreaba..."
    la "Oare se va ridica la nivelul campionilor renumiti?"
    hide frank okk
    show frank vb
    with dissolve
    la "Vom afla in aceasta seara!"

    la "Este timpul pentru prima lupta a lui [mcname], impreuna cu David Samanul Sirurilor!"
    la "Fie ca cel mai bun sa castige!"

    hide frank vb
    with fade

## TE LUPTI CU DAVID 
label primaprovocare:

    show david okk
    with dissolve

    d "Crezi ca ma poti invinge tu?"

label david1im:
    show screen qdavid1
    hide david okk
    show david neutral
    with dissolve

menu david1:

    "A.  1b438":
        d "Nu e bine! Tu chiar credeai ca ai vreo sansa impotriva mea?"
        jump david1imd
    "B.  1bcd8":
        d "Nu e bine! Tu chiar credeai ca ai vreo sansa impotriva mea?"
        jump david1imd
    "C.  ba2":
        d "Nu e bine! Tu chiar credeai ca ai vreo sansa impotriva mea?"
        jump david1imd
    "D.  bcd":
        d "Este...corect. Nu ma asteptam de la un incepator ca tine"
        $ score +=1
        jump david1imd
label david1imd:
    hide screen qdavid1
menu david2:
    "Care din următoarele expresii are valoarea 1 dacă și numai dacă șirul de caractere s, format din exact 10 caractere, este obținut prin concatenarea a două șiruri identice?"

    "A.  strcmp(s, s+5)==0":
        d "Nu e bine! Tu chiar credeai ca ai vreo sansa impotriva mea?"
        jump imdavid3
    "B. s==strstr(s,s+5)":
        d "Este...corect! Nu ma asteptam de la un incepator ca tine"
        $ score +=1
        jump imdavid3
    "C.  s==s+5":
        d "Nu e bine! Tu chiar credeai ca ai vreo sansa impotriva mea?"
        jump imdavid3
    "D. strcmp(s, sttrcat(s, s+5))==0":
        d "Nu e bine! Tu chiar credeai ca ai vreo sansa impotriva mea?"
        jump imdavid3

label imdavid3:
    show screen qdavid3
menu david3:
    "A.  ENXAME":
        d "Nu e bine! Tu chiar credeai ca ai vreo sansa impotriva mea?"
        jump davidfinal
    "B.  EAENMX":
        d "Este...corect! Nu ma asteptam de la un incepator ca tine"
        $ score +=1
        jump davidfinal
    "C. NEEXMA":
        d "Nu e bine! Tu chiar credeai ca ai vreo sansa impotriva mea?"
        jump davidfinal
    "D.  NEXAME":
        d "Nu e bine! Tu chiar credeai ca ai vreo sansa impotriva mea?"
        jump davidfinal

label davidfinal:

    hide screen qdavid3
    show screen gata
    hide david neutral
    show david okk
    with dissolve

    if score == 3:
        hide david okk
        show david sad
        with dissolve
        d "Nu imi vine sa cred... m-a invins cineva dupa atata timp!"
        hide david sad
        show david neutral
        with dissolve
        d "Cineva atat de nou in ale informaticii..."
        hide david neutral
        show david okk
        with dissolve
        d "Te respect din toata inima. Sincer. Adica, sa ma invingi pe MINE..."
        d "Este o realizare mare."
    else:
        d "Stiam ca sunt o provocare prea mare pentru cineva ca tine!"
        d "Nu-i nicio problema. Nu ma asteptam ca cineva sa ma invinga oricum."
        hide david okk
        show david neutral
        with dissolve
        d "Dar sa nu crezi ca ti-am vazut potentialul."
        hide david neutral
        show david okk
        with dissolve
        d "Iti mai dau o sansa. Doar pentru ca am incredere ca vei putea deveni un campion al Infolandiei. Vad asta in ochii tai"
        $ score = 0 
        jump david1im
    
    hide david okk
    with fade

label dupadavid:
    
    $ score = 3
    show frank okk
    with dissolve
    la "Spectaculos! Minunat!"
    hide frank okk
    show frank vb
    with dissolve
    la "Vedem in fata ochilor nostri cum se ridica o legenda!"
    la "Dar oare va reusi sa treaca peste provocarile celorlalti doi maestri?"
    hide frank vb
    show frank okk
    with dissolve
    la "Urmeaza a doua proba, intre Andreea Regina Recursivitatii si [mcname]!"
## TE LUPTI CU ANDREEA 

label andreea:

    hide frank okk
    with fade
    show andreea okk
    with dissolve
    a "Ai trecut peste provocarea lui David..."
    a "Nu ma mira."
    hide andreea okk
    show andreea sad
    with dissolve
    a "Se da mare dar nu a fost niciodata cine stie ce"
    hide andreea sad
    show andreea okk
    with dissolve
    a "Hai sa vedem daca ma poti invinge aici"

label imandreea1:
    show screen qandreea1
menu andreea1:
    
    "A. F(2015,2015)":
        a "Hai mai incearca! Poate alta data vei reusi."
        jump a1imd
    "B.  F(2015,1)":
        a "Hai mai incearca! Poate altadata vei reusi."
        jump a1imd
    "C.  F(2015, 2)":
        a "Incredibil! Ai reusit sa raspunzi corect dupa ce am stat atat sa fac un exercitiu imposibil?"
        $ score +=1
        jump a1imd
    "D.  F(2015, d)":
        a "Hai mai incearca! Poate alta data vei reusi"
        jump a1imd
label a1imd:
    hide screen qandreea1
    show screen qandreea2
    hide andreea okk
    show andreea neutral
    with dissolve

menu andreea2:
    "A. abcd":
        a "Hai mai incearca! Poate alta data vei reusi."
        jump a2imd
    "B.  dcba":
        a "Incredibil! Ai reusit sa raspunzi corect dupa ce am stat atat sa fac un exercitiu imposibil?"
        $ score +=1
        jump a2imd
    "C.  dcb":
        a "Hai mai incearca! Poate alta data vei reusi"
        jump a2imd 
    "D.  bcd":
        a "Hai mai incearca! Poate alta data vei reusi"
        jump a2imd 

label a2imd:
    hide screen qandreea2
    hide andreea neutral
    show andreea okk
    with dissolve
    show screen qandreea3

menu andreea3:
    "A. 1":
        a "Hai mai incearca! Poate alta data vei reusi."
        jump andreeafinal
    "B.  7":
        a "Incredibil! Ai reusit sa raspunzi corect dupa ce am stat atat sa fac un exercitiu imposibil?"
        $ score +=1
        jump andreeafinal
    "C.  8":
        a "Hai mai incearca! Poate alta data vei reusi"
        jump andreeafinal 
    "D.  10":
        a "Hai mai incearca! Poate alta data vei reusi"
        jump andreeafinal
    
label andreeafinal:

    hide screen qandreea3
    screen gata():
        pass
    if score == 6:
        hide andreea okk
        show andreea neutral
        with dissolve
        a "Tu ai....ce?"
        a "Ai reusit sa completezi provocarea si sa ma invingi?"
        hide andreea neutral
        show andreea okk
        with dissolve
        a "Nu-mi vine sa cred! Felicitari!"
        a "Pentru cineva ca tine sunt dispusa sa-mi impart locul de campioana."
        a "Esti legendar!"
        $ score = 6
        jump dupaandreea
    else:
        hide andreea okk
        show andreea neutral
        with dissolve
        a "Hm..."
        hide andreea okk
        show andreea sad
        with dissolve
        a "Pare ca nu te-ai descurcat prea bine."
        a "Chiar imi pare rau."
        a "Parca ti-as mai da sansa sa mai concurezi cu mine o data."
        hide andreea sad
        show andreea okk
        with dissolve
        a "Ai sanse imense sa ma invingi."
        a "Si Infolandia are nevoie de cat mai multi campioni."
        $ score = 3
        jump imandreea1

    

label dupaandreea:

    $ score = 6 
    hide andreea okk
    with fade
    show frank okk
    with dissolve
    la "Senzational! Ati vazut si voi, spectatorii de acasa?"
    hide frank okk
    show frank vb
    with dissolve
    la "[mcname] este pe drumul de a deveni al PATRULEA campion informatic al Infolandiei!"
    la "Dar sa nu ne grabim!"
    la "Cea mai grea provocare a lui inca il asteapta"
    hide frank vb
    show frank okk
    with dissolve
    la "[mcname], tu ramai pe scena. Este timpul pentru marea finala, unde o intampinam pe..."
    la "Maria Cuceritoarea Codurilor!"

## TE LUPTI CU MARIA
label maria:
    hide frank okk
    with fade
    show larisa okk
    with dissolve

    m "Deci tu doresti sa devii un mare campion al Codurilor"
    m "Dar inainte de asta..."
    m "Trebuie sa treci de provocarea mea"
    m "Sper ca esti gata."

label immaria:
    $ score = 6
    show screen qmaria1
    hide larisa okk
    with fade
    show larisa neutral
    with dissolve

menu maria1: 

    "A.  35 100 125 1000":
        m "Raspuns gresit! Stii ca ultima provocare e mereu cea mai grea"
        jump m1imd
    "B.  35 100 123 1000":
        m "Raspuns gresit! Stii ca ultima provocare e mereu cea mai grea"
        jump m1imd
    "C.  35 123 125 1000":
        m "Bravo! Imi dau seama cum ai ajuns atat de departe"
        $ score +=1
        jump m1imd
    "D.  35 34 23 1":
        m "Raspuns gresit! Stii ca ultima provocare e mereu cea mai grea"
        jump m1imd

label m1imd:
    hide screen qmaria1
    hide larisa neutral
    show larisa okk
    with dissolve
    show screen qmaria2

menu maria2:
    "A.  303 120 2":
        m "Raspuns gresit! Stii ca ultima provocare e mereu cea mai grea"
        jump m2imd
    "B.  303 356 12345":
        m "Raspuns gresit! Stii ca ultima provocare e mereu cea mai grea"
        jump m2imd
    "C.  303 940 1001 12345":
        m "Raspuns gresit! Stii ca ultima provocare e mereu cea mai grea"
        jump m2imd
    "D.  303 1001 12345":
        m "Bravo! Imi dau seama cum ai ajuns atat de departe"
        $ score +=1
        jump m2imd

label m2imd:
    hide screen qmaria2
    hide larisa okk
    show larisa sad
    with dissolve
    show screen qmaria3

menu maria3:
    "A.  2":
        m "Raspuns gresit! Stii ca ultima provocare e mereu cea mai grea"
        jump mariafinal
    "B.  3":
        m "Bravo! Imi dau seama cum ai ajuns atat de departe"
        $ score +=1
        jump mariafinal
    "C.  4":
        m "Raspuns gresit! Stii ca ultima provocare e mereu cea mai grea"
        jump mariafinal
    "D.  5":
        m "Raspuns gresit! Stii ca ultima provocare e mereu cea mai grea"
        jump mariafinal

label mariafinal:
    
    hide screen qmaria3

    if score == 9:
        hide larisa sad
        show larisa neutral
        with dissolve
        m "Ce...?"
        m "Ai...rezolvat totul!"
        m "Si eu care credeam ca am compus cea mai grea proba din existenta Campionatului de Cod"
        hide larisa neutral
        show larisa okk
        with dissolve
        m "Eu cred cu toata inima ca meriti sa fii numit urmatorul campion!"
        $ score = 9
        jump dupamaria
    else:
        hide larisa sad
        show larisa neutral
        with dissolve
        m "Stai asa..."
        hide larisa neutral
        show larisa sad
        with dissolve
        m "Nu ai rezolvat totul cum trebuie"
        m "Asta inseamna sfarsitul banuiesc.."
        m "Dar totusi ai fost atat de aproape!"
        hide larisa sad
        show larisa okk
        with dissolve
        m "Cred cu tarie ca daca te concentrezi mai tare o sa poti reusi!"
        m "Hai ca iti mai dau totusi o sansa..."
        $ score == 6
        jump immaria

label dupamaria:

    hide larisa okk 
    with fade
    show frank okk
    with dissolve

    la "Dragi spectatori, nu imi vine sa cred!"
    hide frank okk
    show frank vb
    with dissolve
    la "In aceasta editie a Campionatului de Cod, nu numai ca am asistat la o provocare intensa intre cele mai mari minti ale Infolandiei"
    la "Dar avem si un campion nou printre cei renumiti!"
    hide frank vb
    show frank vb:
        zoom 1.25
    la "APLAUZE PENTRU [mcname] !!!"
    hide frank vb
    show frank okk
    with dissolve
    la "Va multumim foarte mult ca ati fost prezenti"
    la "Si pentru ca v-ati aratat interestul fata de informatica"
    la "Inainte sa incheiem aceasta editie, vreau sa va spun doar atat"
    la "..."
    hide frank okk
    show frank vb
    with dissolve
    la "Nu renuntati niciodata! Si voi puteti deveni campioni!"
    la "Va urez o seara minunata si plina de distractii!"
    hide frank vb
    show frank okk
    with dissolve
    la "Si Infolandia va asteapta si la urmatorul campionat!"

    hide frank okk
    with fade

## SFARSITUL
label sfarsit:
 
    scene outro
    with fade
    "FELICITARI!"
    "Ai devenit un campion al Infolandiei!"
    "(poate incerci sa devii si campion la bac)"
    "(sigur vei reusi)"

    show screen outrotab
    "Grafica: Luiza Irimia \nImagine fundal: Pixabay \nGrile informatica: pbinfo.ro"
    return
