ime = "Mark"
prezime = "Smith"
mjesto_rodenja = "Seattle"
mjesto_stanovanja = "Seattle"
datum_rodenja = "2305"
godina_rodenja = "1990"
korisnicko_ime = "admin" 
web_mjesto = "megacorp"
najdrazi_broj = "7"

p1 = ime [::-1] #često se koristi zaporka gdje se ime napiše unatrag, samo ili sa dodanim brojevima

p2 = p1 + datum_rodenja

p3 = p1 + godina_rodenja

p4 = p1 + str((int(godina_rodenja) % 100))

p5 = ime

p6 = p5 + datum_rodenja

p7 = p5 + godina_rodenja

p8 = p5 + str((int(godina_rodenja) % 100))

p9 = p5 + "1" #isto tako, često se na ime doda broj "1" u slučajevima gdje sustav zahtjeva brojeve u zaporki

p10 = p1 + "1"

p11 = prezime

p12 = prezime + datum_rodenja

p13 = prezime + godina_rodenja

p14 = prezime + str((int(godina_rodenja) % 100))

p15 = prezime + "1"

p16 = prezime + ime

p17 = ime + prezime

#kod zaporki koje sadrže geografska mjesta, isto tako se najčešće koriste same ili se dodaju brojevi ili u rijeđim slučajevima se koristi pisanje imena lokacije unatrag

p18 = mjesto_rodenja 

p19 = p18 + datum_rodenja

p20 = p18 + godina_rodenja

p21 = p18 + str((int(godina_rodenja) % 100))

p22 = mjesto_rodenja [::-1]

p23 = prezime [::-1]

p24 = mjesto_stanovanja

p25 = p24 + datum_rodenja

p26 = p24 + godina_rodenja

p27 = p24 + str((int(godina_rodenja) % 100))

p28 = mjesto_stanovanja [::-1]

p29 = ime + najdrazi_broj

p30 = ime [::-1] + najdrazi_broj

p31 = prezime + najdrazi_broj

p32 = prezime [::-1] + najdrazi_broj

p33 = mjesto_rodenja + najdrazi_broj

p34 = mjesto_rodenja [::-1] + najdrazi_broj

p35 = mjesto_stanovanja + najdrazi_broj

p36 = mjesto_stanovanja [::-1] + najdrazi_broj

p37 = datum_rodenja + godina_rodenja

p38 = datum_rodenja + godina_rodenja [::-1] 

p39 = godina_rodenja + datum_rodenja

p40 = godina_rodenja [::-1] + datum_rodenja #numeričke lozinke najčešće sadrže parni broj znakova, 4, 6 ili 8

p41 = godina_rodenja + godina_rodenja

p42 = ime + ime #duple riječi, čega je primjer dvaput napisano ime je isto tako česta zaporka kod sustava koji zahtjevaju određeni broj znakova

p43 = prezime + prezime 

p44 = korisnicko_ime

p45 = korisnicko_ime + web_mjesto

p46 = korisnicko_ime + najdrazi_broj

p47 = korisnicko_ime + godina_rodenja

p48 = korisnicko_ime + datum_rodenja

p49 = korisnicko_ime + godina_rodenja [::-1]

p50 = web_mjesto + najdrazi_broj

passwords = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,
p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,
p32,p33,p34,p35,p36,p37,p38,p39,p40,p41,p42,p43,p44,p45,p46,p47,p48,p49,p50]

for p in passwords:
	print(p)



