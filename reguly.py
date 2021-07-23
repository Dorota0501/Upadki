

# ----------------------SŁOWNIK_REGULY----------------------
# kluczem jest zestawienie etykiet dla P40, HW, sigma, HHmax
# np.  0212 -> P40 - low
#             HW - high
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

slownik_nowe_reguly = {
    '020x' : ['notLy',1],
    '02x2' : ['notLy',2],
    '0x02' : ['notLy',3],
    'x202' : ['notLy',4],
    '0x01' : ['notLy',5],
    '0211' : ['notLy',6],
    '0112' : ['notLy',7],
    '1201' : ['notLy',8],
    '1212' : ['notLy',9],
    '1102' : ['notLy',10],
    '11x1' : ['mayLy',11],
    '001x' : ['mayLy',12],
    '100x' : ['mayLy',13],
    '221x' : ['mayLy',14],
    '012x' : ['mayLy',15],
    'x221' : ['mayLy',16],
    '1x22' : ['mayLy',17],
    '12x0' : ['mayLy',18],
    '21x2' : ['mayLy',19],
    '2002' : ['mayLy',20],
    '0022' : ['mayLy',21],
    '111x' : ['mayLy',22],
    'x012' : ['mayLy',23],
    'x210' : ['mayLy',24],
    '01x0' : ['mayLy',25],
    '2200' : ['mayLy',26],
    '00x1' : ['mayLy',27],
    'x111' : ['mayLy',28],
    '0000' : ['mayLy',29],
    '2222' : ['mayLy',30],
    '2x01' : ['mayLy',31],
    '0220' : ['mayLy',32],
    'x100' : ['mayLy',33],
    '1x11' : ['mayLy',34],
    '202x' : ['isLy',35],
    '2110' : ['isLy',36],
    '20x0' : ['isLy',37],
    '2x20' : ['isLy',38],
    'x020' : ['isLy',39],
    '2011' : ['isLy',40],
    '2121' : ['isLy',41],
    '1010' : ['isLy',42],
    '1120' : ['isLy',43],
    '1021' : ['isLy',44]    
    }
# słowniki zawierajace przynaleznosci do danej etykiety,
# wartosci wyznaczane sa na bazie slownika regul
isLy = {}
mayLy = {}
notLy = {}

isLy_pom = {}
mayLy_pom = {}
notLy_pom = {}

isLy_nowe = {}
mayLy_nowe = {}
notLy_nowe = {}
wszystkie_nowe = {}

def f_fun(tab):
    wynik = 0
    wynik = tab[0] - pow((max(0,tab[0] - tab[1])),2)
    wynik = tab[2] - pow((max(0,tab[2] - wynik)),2)
    wynik = tab[3] - pow((max(0,tab[3] - wynik)),2)
    return wynik


def f_fun3(tab):
    wynik = 0
    wynik = tab[0] - pow((max(0,tab[0] - tab[1])),2)            
    wynik = tab[2] - pow((max(0,tab[2] - wynik)),2)
    return wynik


def lehmer(tab, lam):
    wynik = 0
    if ((lam * (pow(tab[0],2))) + ((1 - lam) * pow(tab[1],2))) == 0 and ((lam * tab[0]) + ((1 - lam) * tab[1])) == 0:
        wynik = 0
    else:
        wynik = ((lam * (pow(tab[0],2))) + ((1 - lam) * pow(tab[1],2))) / ((lam * tab[0]) + ((1 - lam) * tab[1]))
    
    if ((lam * (pow(wynik,2))) + ((1 - lam) * pow(tab[2],2))) == 0 and ((lam * wynik) + ((1 - lam) * tab[2])) == 0:
        wynik = 0
    else:
        wynik = ((lam * (pow(wynik,2))) + ((1 - lam) * pow(tab[2],2))) / ((lam * wynik) + ((1 - lam) * tab[2]))
    
    if ((lam * (pow(wynik,2))) + ((1 - lam) * pow(tab[3],2))) == 0 and ((lam * wynik) + ((1 - lam) * tab[3])) == 0:
        wynik = 0
    else:
        wynik = ((lam * (pow(wynik,2))) + ((1 - lam) * pow(tab[3],2))) / ((lam * wynik) + ((1 - lam) * tab[3]))

    return wynik

def lehmer3(tab, lam):
    wynik = 0
    if ((lam * (pow(tab[0],2))) + ((1 - lam) * pow(tab[1],2))) == 0 and ((lam * tab[0]) + ((1 - lam) * tab[1])) == 0:
        wynik = 0
    else:
        wynik = ((lam * (pow(tab[0],2))) + ((1 - lam) * pow(tab[1],2))) / ((lam * tab[0]) + ((1 - lam) * tab[1]))
    
    if (((lam * (pow(wynik,2))) + ((1 - lam) * pow(tab[2],2)))) == 0 and ((lam * wynik) + ((1 - lam) * tab[2])) == 0:
        wynik = 0
    else:
        wynik = ((lam * (pow(wynik,2))) + ((1 - lam) * pow(tab[2],2))) / ((lam * wynik) + ((1 - lam) * tab[2]))

    return wynik    

def agregacja(klucz, P40, HW, sigma, HHmax):
    minimum = min(P40[int(klucz[0])], HW[int(klucz[1])], sigma[int(klucz[2])], HHmax[int(klucz[3])])
    tp = P40[int(klucz[0])] * HW[int(klucz[1])] * sigma[int(klucz[2])] * HHmax[int(klucz[3])]
    a_mean = (P40[int(klucz[0])] + HW[int(klucz[1])] + sigma[int(klucz[2])] + HHmax[int(klucz[3])]) / 4
    ag_mean = pow(tp, 1 / 4)
    sorted_owa = [P40[int(klucz[0])] ,HW[int(klucz[1])] ,  sigma[int(klucz[2])] ,HHmax[int(klucz[3])]]
    sorted_owa.sort()
    owa = (sorted_owa[0] * 0.5) + (sorted_owa[1] * 0.3) + (sorted_owa[2] * 0.1) + (sorted_owa[3] * 0.1)   
    f = f_fun([P40[int(klucz[0])], HW[int(klucz[1])], sigma[int(klucz[2])], HHmax[int(klucz[3])]])
    leh = lehmer([P40[int(klucz[0])], HW[int(klucz[1])], sigma[int(klucz[2])], HHmax[int(klucz[3])]],0.7)
    return minimum 

def agregacja_nowe(klucz, P40, HW, sigma, HHmax):
    if klucz[0] == 'x':
        minimum = min(HW[int(klucz[1])], sigma[int(klucz[2])], HHmax[int(klucz[3])])
        tp = HW[int(klucz[1])] * sigma[int(klucz[2])] * HHmax[int(klucz[3])]
        a_mean = (HW[int(klucz[1])] + sigma[int(klucz[2])] + HHmax[int(klucz[3])]) / 3
        ag_mean = pow(tp, 1 / 3)
        sorted_owa = [HW[int(klucz[1])] ,  sigma[int(klucz[2])] ,HHmax[int(klucz[3])]]
        sorted_owa.sort()
        owa = (sorted_owa[0] * 0.5) + (sorted_owa[1] * 0.3) + (sorted_owa[2] * 0.1) 
        f = f_fun3([HW[int(klucz[1])], sigma[int(klucz[2])], HHmax[int(klucz[3])]])
        leh = lehmer3([HW[int(klucz[1])], sigma[int(klucz[2])], HHmax[int(klucz[3])]],0.7)

    elif klucz[1] == 'x':
        minimum = min(P40[int(klucz[0])], sigma[int(klucz[2])], HHmax[int(klucz[3])])
        tp = P40[int(klucz[0])] * sigma[int(klucz[2])] * HHmax[int(klucz[3])]
        a_mean = (P40[int(klucz[0])] + sigma[int(klucz[2])] + HHmax[int(klucz[3])]) / 3
        ag_mean = pow(tp, 1 / 3)
        sorted_owa = [P40[int(klucz[0])] ,  sigma[int(klucz[2])] ,HHmax[int(klucz[3])]]
        sorted_owa.sort()
        owa = (sorted_owa[0] * 0.5) + (sorted_owa[1] * 0.3) + (sorted_owa[2] * 0.1) 
        f = f_fun3([P40[int(klucz[0])], sigma[int(klucz[2])], HHmax[int(klucz[3])]])
        leh = lehmer3([P40[int(klucz[0])], sigma[int(klucz[2])], HHmax[int(klucz[3])]],0.7)

    elif klucz[2] == 'x':
        minimum = min(P40[int(klucz[0])], HW[int(klucz[1])], HHmax[int(klucz[3])])
        tp = P40[int(klucz[0])] * HW[int(klucz[1])] * HHmax[int(klucz[3])]
        a_mean = (P40[int(klucz[0])] + HW[int(klucz[1])] + HHmax[int(klucz[3])]) / 3
        ag_mean = pow(tp, 1 / 3)
        sorted_owa = [P40[int(klucz[0])] ,HW[int(klucz[1])] , HHmax[int(klucz[3])]]
        sorted_owa.sort()
        owa = (sorted_owa[0] * 0.5) + (sorted_owa[1] * 0.3) + (sorted_owa[2] * 0.1) 
        f = f_fun3([P40[int(klucz[0])], HW[int(klucz[1])], HHmax[int(klucz[3])]])
        leh = lehmer3([P40[int(klucz[0])], HW[int(klucz[1])], HHmax[int(klucz[3])]],0.7)


    elif klucz[3] == 'x':
        minimum = min(P40[int(klucz[0])], HW[int(klucz[1])], sigma[int(klucz[2])])
        tp = P40[int(klucz[0])] * HW[int(klucz[1])] * sigma[int(klucz[2])]
        a_mean = (P40[int(klucz[0])] + HW[int(klucz[1])] + sigma[int(klucz[2])]) / 3
        ag_mean = pow(tp, 1 / 3)
        sorted_owa = [P40[int(klucz[0])] ,HW[int(klucz[1])] ,  sigma[int(klucz[2])]]
        sorted_owa.sort()
        owa = (sorted_owa[0] * 0.5) + (sorted_owa[1] * 0.3) + (sorted_owa[2] * 0.1) 
        f = f_fun3([P40[int(klucz[0])], HW[int(klucz[1])], sigma[int(klucz[2])]])
        leh = lehmer3([P40[int(klucz[0])], HW[int(klucz[1])], sigma[int(klucz[2])]],0.7)

    else:
        minimum = min(P40[int(klucz[0])], HW[int(klucz[1])], sigma[int(klucz[2])], HHmax[int(klucz[3])])
        tp = P40[int(klucz[0])] * HW[int(klucz[1])] * sigma[int(klucz[2])] * HHmax[int(klucz[3])]
        a_mean = (P40[int(klucz[0])] + HW[int(klucz[1])] + sigma[int(klucz[2])] + HHmax[int(klucz[3])]) / 4
        ag_mean = pow(tp, 1 / 4)
        sorted_owa = [P40[int(klucz[0])] ,HW[int(klucz[1])] ,  sigma[int(klucz[2])] ,HHmax[int(klucz[3])]]
        sorted_owa.sort()
        owa = (sorted_owa[0] * 0.5) + (sorted_owa[1] * 0.3) + (sorted_owa[2] * 0.1) + (sorted_owa[3] * 0.1)
        f = f_fun([P40[int(klucz[0])], HW[int(klucz[1])], sigma[int(klucz[2])], HHmax[int(klucz[3])]])
        leh = lehmer([P40[int(klucz[0])], HW[int(klucz[1])], sigma[int(klucz[2])], HHmax[int(klucz[3])]],0.7)

    return minimum

def przynal_do_pozycji(P40, HW, sigma, HHmax):
    for iP40 in range(3):
        for iHW in range(3):
            for isigma in range(3):
                for iHHmax in range(3):
                    klucz = str(iP40) + str(iHW) + str(isigma) + str(iHHmax)
                    wartosc_slownik = slownik_reguly.get(klucz)
                    #print("klucz: ",klucz)
                    #print("wartosc slownik: ",wartosc_slownik)
                    nr_reguly = wartosc_slownik[1]
                    pozycja = wartosc_slownik[0]
                    if pozycja == 'isLy':
                        isLy[nr_reguly] = agregacja(klucz,P40, HW, sigma, HHmax) #wrzuc aktualne wartosci tablic parametrow
                    elif pozycja == 'mayLy':                        
                        mayLy[nr_reguly] = agregacja(klucz,P40, HW, sigma, HHmax) #wrzuc aktualne wartosci tablic parametrow
                    elif pozycja == 'notLy':                       
                        notLy[nr_reguly] = agregacja(klucz,P40, HW, sigma, HHmax) #wrzuc aktualne wartosci tablic parametrow
def przynal_do_poz_nowe(P40, HW, sigma, HHmax,nr):
    filepath11 = "wyniki_s_r.txt"
    f11 = open(filepath11, "a")
    f11.write("\nklatka: " + str(nr) + "\n")
    for k in slownik_nowe_reguly.keys():
        wartosc_slownik = slownik_nowe_reguly.get(k)
        nr_reguly = wartosc_slownik[1]
        pozycja = wartosc_slownik[0]
        if pozycja == 'isLy':
            isLy_nowe[nr_reguly] = agregacja_nowe(k,P40, HW, sigma, HHmax) #wrzuc aktualne wartosci tablic parametrow
        elif pozycja == 'mayLy':                        
            mayLy_nowe[nr_reguly] = agregacja_nowe(k,P40, HW, sigma, HHmax) #wrzuc aktualne wartosci tablic parametrow
        elif pozycja == 'notLy':                       
            notLy_nowe[nr_reguly] = agregacja_nowe(k,P40, HW, sigma, HHmax) #wrzuc aktualne wartosci tablic parametrow
        wszystkie_nowe[nr_reguly] = agregacja_nowe(k,P40, HW, sigma, HHmax)
        f11.write(str(nr_reguly) + "," + str(wszystkie_nowe[nr_reguly]) + '\n')  
    #utwórz plik i przepisz do niego wyniki ze slownikow
    
      
    f11.close
            
def defuzyfikacja():
    
    max_isLy = max(i for i in isLy.values()) 

    
    max_isLy1 = -1
    isLy_key = 0
    for i in isLy.keys():
        if max_isLy1 < isLy.get(i):
            max_isLy1 = isLy.get(i)
            isLy_key = i
    print(" max_isLy1: ",  max_isLy1)
    print("isLy_key: ", isLy_key)

    # z tego maxa sprawdzic dla jakiej wartosci ono wychodzi
    # i ogarnac do tego maxa przedzialy i z nich cetrum trzeba (srodek
    # dziedziny)
    max_mayLy = max(i for i in mayLy.values())
    max_mayLy1 = -1
    mayLy_key = 0
    for i in mayLy.keys():
        if max_mayLy1 < mayLy.get(i):
            max_mayLy1 = mayLy.get(i)
            mayLy_key = i
    print(" max_mayLy1: ",  max_mayLy1)
    print("mayLy_key: ", mayLy_key)

    #-------------------------------------------------------
    max_notLy = max(i for i in notLy.values())
    max_notLy1 = -1
    notLy_key = 0
    for i in notLy.keys():
        if max_notLy1 < notLy.get(i):
            max_notLy1 = notLy.get(i)
            notLy_key = i
    print(" max_notLy1: ",  max_notLy1)
    print("notLy_key: ", notLy_key)

    filepath_k_r = "klasyfikacja_regula.txt"
    f_k_r = open(filepath_k_r, "a")
    


    if max_mayLy1 > max_isLy1 and max_mayLy1 > max_notLy1:
        print("mayLy: ",max_mayLy1, ", r",mayLy_key)
        f_k_r.write("\nmayLy, " + str(max_mayLy1) + ", r" + str(mayLy_key))
    if max_isLy1 > max_mayLy1 and max_isLy1 > max_notLy1:
        print("isLy: ",max_isLy1, ", r",isLy_key)
        f_k_r.write("\nisLy, " + str(max_isLy1) + ", r" + str(isLy_key))
    if max_notLy1 > max_isLy1 and max_notLy1 > max_mayLy1:
        print("notLy: ",max_notLy1, ", r",notLy_key)
        f_k_r.write("\nnotLy, " + str(max_notLy1) + ", r" + str(notLy_key))

    f_k_r.close

    #print("max_isLy: ",max_isLy)
    #print("max_mayLy: ",max_mayLy)
    #print("max_notLy: ",max_notLy)
    wynik = ((0.11 * max_isLy) + (0.5 * max_mayLy) + (0.885 * max_notLy)) / (max_isLy + max_mayLy + max_notLy)
    
    filepath0 = "dane_stare_reg.txt"
    f0 = open(filepath0, "a")
    f0.write(str(wynik) + '\n')    
    f0.close

    print(str(wynik) + '\n')
    
    if wynik >= 0.5:
        return 'notLy'
    else:
        return wynik

def defuzyfikacja_nowe():

    max_isLy = max(i for i in isLy_nowe.values())
    max_mayLy = max(i for i in mayLy_nowe.values())
    max_notLy = max(i for i in notLy_nowe.values())
    
    #print("max_isLy_nowe: ",max_isLy_nowe)
    #print("max_mayLy_nowe: ",max_mayLy_nowe)
    #print("max_notLy_nowe: ",max_notLy_nowe)
    #
    wynik = ((0.11 * max_isLy) + (0.5 * max_mayLy) + (0.885 * max_notLy)) / (max_isLy + max_mayLy + max_notLy)  
    
    filepath0 = "dane_nowe_reg.txt"
    f0 = open(filepath0, "a")
    f0.write(str(wynik) + '\n')    
    f0.close
    
    if wynik >= 0.5:
        return 'notLy'
    else:
        return wynik