import reguly
import Dane

def fun_HW(HW):
    lmh = [0,0,0]
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

def fun_SxSzmax(SxSzmax):
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
for i in prepared_data.keys():
    print(i)
    for j in prepared_data[i]:
        #print(j)
        Pose = j[0]
        HW = fun_HW(j[2])
        HHmax = fun_HHmax(j[4])
        sigma = fun_SxSzmax(j[3])
        P40 = fun_P40(j[1])
        
        reguly.przynal_do_pozycji(P40, HW, sigma, HHmax)
        wynik = reguly.defuzyfikacja()
        
        reguly.przynal_do_poz_nowe(P40, HW, sigma, HHmax)
        wynik_nowe = reguly.defuzyfikacja_nowe()
        #print("wynik: ",wynik)
        #print("pose: ",Pose)
        if Pose != 0:
            if wynik == 'notLy':
                if Pose == -1:
                    results.append("TP")
                else:
                    results.append("FP")
            elif wynik != 'notLy':
                if Pose == -1: 
                    results.append("FN")
                else:
                    results.append("TN")

            if wynik_nowe == 'notLy':
                if Pose == -1:
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