import reguly
import Dane
import math

from matplotlib import pyplot as mp
import numpy as np

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))



def fun_HW(HW):
    lmh = [0,0,0]

    #gaussian LOW
    #       s1, c1, s2, c2
    # f(x,[-0.160 0.544 0.500 0.300] ) = e ^ ( -(x-c1)^2 / 2(s1^2)

    #x_values = np.arange(0,4,0.05)
    #for mu, sig in [(0.500, 0.300),(2.000, 0.440),(3.230, 1.000)]:
    #    mp.plot(x_values, gaussian(x_values, mu, sig))

    #mp.show()


    #print("\nf:",f)
    ##print("xs")
    

    #---------------LOW---------------------
    if HW <= 0.5:
        lmh[0] = 1    
    if HW > 0.5 and HW <= 2:
        lmh[0] = (2 - HW) / 1.5 
    if HW > 2:
        lmh[0] = 0
    #---------------MEDIUM-------------------
    if HW <= 0.5 or HW > 3.2:
        lmh[1] = 0    
    if HW > 0.5 and HW <= 2:
        lmh[1] = (HW - 0.5) / 1.5
    if HW > 2 and HW <= 3.2:
        lmh[1] = (3.2 - HW) / 1.2   
    #---------------HIGH---------------------
    if HW <= 2:
        lmh[2] = 0
    if HW > 2 and HW <= 3.2:
        lmh[2] = (HW - 2) / 1.2
    if HW > 3.2:
        lmh[2] = 1
    
    return lmh

def fun_HHmax(HHmax):
    lmh = [0,0,0]
    #---------------LOW---------------------
    if HHmax <= 0.25:
        lmh[0] = 1    
    if HHmax > 0.25 and HHmax <= 0.6:
        lmh[0] = (0.6 - HHmax) / 0.35
    if HHmax > 0.6:
        lmh[0] = 0
    #---------------MEDIUM-------------------
    if HHmax <= 0.25 or HHmax > 1:
        lmh[1] = 0    
    if HHmax > 0.25 and HHmax <= 0.6:
        lmh[1] = (HHmax - 0.25) / 0.35
    if HHmax > 0.6 and HHmax <= 1:
        lmh[1] = (1 - HHmax) / 0.35
    
    #---------------HIGH---------------------
    if HHmax <= 0.6:
        lmh[2] = 0
    if HHmax > 0.6 and HHmax <= 1:
        lmh[2] = (HHmax - 0.6) / 0.4
    if HHmax > 1:
        lmh[2] = 1
    
    return lmh

def fun_SxSzmax(SxSzmax):   #z plikow
    lmh = [0,0,0]
    #---------------LOW---------------------
    if SxSzmax <= 260:
        lmh[0] = 1    
    if SxSzmax > 260 and SxSzmax <= 310:
        lmh[0] = (310 - SxSzmax) / (310 - 260)
    if SxSzmax > 310:
        lmh[0] = 0
    #---------------MEDIUM-------------------
    if SxSzmax <= 260 or SxSzmax > 410:
        lmh[1] = 0    
    if SxSzmax > 260 and SxSzmax <= 310:
        lmh[1] = (SxSzmax - 260) / (310 - 260)
    if SxSzmax > 310 and SxSzmax <= 410:
        lmh[1] = (410 - SxSzmax) / (410 - 310)
    
    #---------------HIGH---------------------
    if SxSzmax <= 310:
        lmh[2] = 0
    if SxSzmax > 310 and SxSzmax <= 410:
        lmh[2] = (SxSzmax - 310) / (410 - 310)
    if SxSzmax > 410:
        lmh[2] = 1
    
    return lmh

#def fun_SxSzmax(SxSzmax): #z wykresu
#    lmh=[0,0,0]
#    #---------------LOW---------------------
#    a_f_low = -1 / 230
#    b_f_low = 380 / 230
#    if SxSzmax < 150:
#        lmh[0] = 1
#    if SxSzmax >= 150 and SxSzmax <= 380:
#        #na podstawie y=ax+b wyznaczam wartosc
#        #etykiety "low"
#        lmh[0] = a_f_low * SxSzmax + b_f_low
#    if SxSzmax > 380:
#        lmh[0] = 0
#    #---------------MEDIUM-------------------
#    a_f_medL = 1 / 110
#    b_f_medL = -10/11
#    a_f_medR = -1 / 210
#    b_f_medR = 52/21
#    if SxSzmax < 100:
#        lmh[1] = 0
#    if SxSzmax >= 100 and SxSzmax <= 310:
#        lmh[1] = a_f_medL * SxSzmax + b_f_medL
#    if SxSzmax > 310 and SxSzmax <= 520:
#        lmh[1] = a_f_medR * SxSzmax + b_f_medR
#    if SxSzmax > 520:
#        lmh[1] = 0
#    #---------------HIGH---------------------
#    a_f_high = 1/340
#    b_f_high = - 150/340
#    if SxSzmax < 150:
#        lmh[2] = 0
#    if SxSzmax >= 150 and SxSzmax <= 490:
#        lmh[2] = a_f_high*SxSzmax + b_f_high
#    if SxSzmax > 490:
#        lmh[2] = 1
    
#    return lmh
def fun_P40(P40):
    lmh = [0,0,0]
    #---------------LOW---------------------
    if P40 <= 0.18:
        lmh[0] = 1    
    if P40 > 0.18 and P40 <= 0.42:
        lmh[0] = (0.42 - P40) / (0.42 - 0.18)
    if P40 > 0.42:
        lmh[0] = 0
    #---------------MEDIUM-------------------
    if P40 <= 0.18 or P40 > 0.68:
        lmh[1] = 0    
    if P40 > 0.18 and P40 <= 0.42:
        lmh[1] = (P40 - 0.18) / (0.42 - 0.18)
    if P40 > 0.42 and P40 <= 0.68:
        lmh[1] = (0.68 - P40) / (0.68 - 0.42)
    #---------------HIGH---------------------
    if P40 <= 0.42:
        lmh[2] = 0
    if P40 > 0.42 and P40 <= 0.68:
        lmh[2] = (P40 - 0.42) / (0.68 - 0.42)
    if P40 > 0.68:
        lmh[2] = 1  
    
    return lmh

results = []
results_nowe = []
prepared_data = Dane.readFeatures()
#Dane.cut_data(prepared_data)
nr_klatki = 1
for i in prepared_data.keys():
    print(i)
    for j in prepared_data[i]:
        #print(j)
        Pose = j[0]
        HW = fun_HW(j[2])
        HHmax = fun_HHmax(j[4])
        sigma = fun_SxSzmax(j[3])
        P40 = fun_P40(j[1])
        

        filepath0 = "dane_stare_reg.txt"
        filepath1 = "dane_nowe_reg.txt"
        #print("wynik: ",wynik)
        #print("pose: ",Pose)
        if Pose != 0:
            #f0 = open(filepath0, "a")
            #f0.write(str([i,j[5],j[0],j[1],j[2],j[3],j[4]])[1:-1] + ', ')
            #f0.close()

            #f1 = open(filepath1, "a")
            #f1.write(str([i,j[5],j[0],j[1],j[2],j[3],j[4]])[1:-1] + ', ')
            #f1.close()


            print(str([j[0],j[1],j[2],j[3],j[4]])[1:-1] + ',')

            reguly.przynal_do_pozycji(P40, HW, sigma, HHmax)
            wynik = reguly.defuzyfikacja()
        
            reguly.przynal_do_poz_nowe(P40, HW, sigma, HHmax,nr_klatki)
            
            wynik_nowe = reguly.defuzyfikacja_nowe()


            filepath_k_r = "klasyfikacja_regula.txt"
            f_k_r = open(filepath_k_r, "a")
    
            if wynik == 'notLy':
                if Pose == -1:
                    results.append("TP")
                    f_k_r.write(", TP, klatka: " + str(nr_klatki))
                else:
                    results.append("FP")
                    f_k_r.write(", FP, klatka: " + str(nr_klatki))
            elif wynik != 'notLy':
                if Pose == -1: 
                    results.append("FN")
                    f_k_r.write(", FN, klatka: " + str(nr_klatki))
                else:
                    results.append("TN")
                    f_k_r.write(", TN, klatka: " + str(nr_klatki))
            f_k_r.close()
            nr_klatki +=1

            if wynik_nowe == 'notLy':
                if Pose == -1:      #pozycja rzeczywista
                    results_nowe.append("TP")
                else:
                    results_nowe.append("FP")
            elif wynik_nowe != 'notLy':
                if Pose == -1: 
                    results_nowe.append("FN")
                else:
                    results_nowe.append("TN")

        
print("---------------")
TN = 0
FN = 0
TP = 0
FP = 0

for i in results:
    if i == 'TN':
        TN+=1
    elif i == 'FN':
        FN+=1
    elif i == 'TP':
        TP+=1
    elif i == 'FP':
        FP+=1

print("results, stare reguly")
print("TP: ",TP)
print("TN: ",TN)
print("FP: ",FP)
print("FN: ",FN)

print("---------------")
TN = 0
FN = 0
TP = 0
FP = 0
for i in results_nowe:
    if i == 'TN':
        TN+=1
    elif i == 'FN':
        FN+=1
    elif i == 'TP':
        TP+=1
    elif i == 'FP':
        FP+=1

print("results, nowe reguly")
print("TP: ",TP)
print("TN: ",TN)
print("FP: ",FP)
print("FN: ",FN)


