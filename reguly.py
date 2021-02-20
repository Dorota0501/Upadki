

# ----------------------SŁOWNIK_REGULY----------------------
# kluczem jest zestawienie etykiet dla P40, HW, sigma, HHmax
# np. 0212 -> P40   - low
#             HW    - high
#             sigma - medium
#             HHmax - high 
slownik_reguly = {  
    '0202' : ['notLy',1],
    '0201' : ['notLy',2],
    '0200' : ['notLy',3],
    '0212' : ['notLy',4],
    '0211' : ['notLy',5],
    '0210' : ['mayLy',6],
    '0222' : ['notLy',7],
    '0221' : ['mayLy',8],
    '0220' : ['mayLy',9],
    '0102' : ['notLy',10],
    '0101' : ['notLy',11],
    '0100' : ['mayLy',12],
    '0112' : ['notLy',13],
    '0111' : ['mayLy',14],
    '0110' : ['mayLy',15],
    '0122' : ['mayLy',16],
    '0121' : ['mayLy',17],
    '0120' : ['mayLy',18],
    '0002' : ['notLy',19],
    '0001' : ['mayLy',20],
    '0000' : ['mayLy',21],
    '0012' : ['mayLy',22],
    '0011' : ['mayLy',23],
    '0010' : ['mayLy',24],
    '0022' : ['mayLy',25],
    '0021' : ['mayLy',26],
    '0020' : ['isLy',27],
    '1202' : ['notLy',28],
    '1201' : ['notLy',29],
    '1200' : ['mayLy',30],
    '1212' : ['notLy',31],
    '1211' : ['mayLy',32],
    '1210' : ['mayLy',33],
    '1222' : ['mayLy',34],
    '1221' : ['mayLy',35],
    '1220' : ['mayLy',36],
    '1102' : ['notLy',37],
    '1101' : ['mayLy',38],
    '1100' : ['mayLy',39],
    '1112' : ['mayLy',40],
    '1111' : ['mayLy',41],
    '1110' : ['mayLy',42],
    '1122' : ['mayLy',43],
    '1121' : ['mayLy',44],
    '1120' : ['isLy',45],
    '1002' : ['mayLy',46],
    '1001' : ['mayLy',47],
    '1000' : ['mayLy',48],
    '1012' : ['mayLy',49],
    '1011' : ['mayLy',50],
    '1010' : ['isLy',51],
    '1022' : ['mayLy',52],
    '1021' : ['isLy',53],
    '1020' : ['isLy',54],
    '2202' : ['notLy',55],
    '2201' : ['mayLy',56],
    '2200' : ['mayLy',57],
    '2212' : ['mayLy',58],
    '2211' : ['mayLy',59],
    '2210' : ['mayLy',60],
    '2222' : ['mayLy',61],
    '2221' : ['mayLy',62],
    '2220' : ['isLy',63],
    '2102' : ['mayLy',64],
    '2101' : ['mayLy',65],
    '2100' : ['mayLy',66],
    '2112' : ['mayLy',67],
    '2111' : ['mayLy',68],
    '2110' : ['isLy',69],
    '2122' : ['mayLy',70],
    '2121' : ['isLy',71],
    '2120' : ['isLy',72],
    '2002' : ['mayLy',73],
    '2001' : ['mayLy',74],
    '2000' : ['isLy',75],
    '2012' : ['mayLy',76],
    '2011' : ['isLy',77],
    '2010' : ['isLy',78],
    '2022' : ['isLy',79],
    '2021' : ['isLy',80],
    '2020' : ['isLy',81] }

# słowniki zawierajace przynaleznosci do danej etykiety,
# wartosci wyznaczane sa na bazie regul
isLy = {}
mayLy = {}
notLy = {}


def fun(klucz, P40, HW, sigma, HHmax):
    minimum = min(P40[int(klucz[0])], HW[int(klucz[1])], sigma[int(klucz[2])], HHmax[int(klucz[3])])
    return minimum
    


def przynal_do_pozycji(P40, HW, sigma, HHmax):
    for iP40 in range(3):
        for iHW in range(3):
            for isigma in range(3):
                for iHHmax in range(3):
                    klucz = str(iP40)+str(iHW)+str(isigma)+str(iHHmax)
                    wartosc_slownik = slownik_reguly.get(klucz)
                    print("klucz: ",klucz)
                    print("wartosc slownik: ",wartosc_slownik)
                    nr_reguly = wartosc_slownik[1]
                    pozycja = wartosc_slownik[0]
                    if pozycja == 'isLy':
                        print()
                        isLy[nr_reguly] = fun(klucz,P40, HW, sigma, HHmax) #wrzuc aktualne wartosci tablic parametrow
                    elif pozycja == 'mayLy':
                        print()
                        mayLy[nr_reguly] = fun(klucz,P40, HW, sigma, HHmax) #wrzuc aktualne wartosci tablic parametrow
                    elif pozycja == 'notLy':
                        print()
                        notLy[nr_reguly] = fun(klucz,P40, HW, sigma, HHmax) #wrzuc aktualne wartosci tablic parametrow


def defuzyfikacja():
    max_isLy = max(i for i in isLy.values())
    max_mayLy = max(i for i in mayLy.values())
    max_notLy = max(i for i in notLy.values())
    
    print("max_isLy: ",max_isLy)
    print("max_mayLy: ",max_mayLy)
    print("max_notLy: ",max_notLy)

    wynik = ((0.11 * max_isLy) + (0.5 * max_mayLy) + ( 0.115 * max_notLy) ) / (max_isLy + max_mayLy + max_notLy)
    print("wynik: ",wynik)