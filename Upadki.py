import reguly

def pose_value(HW, HHmax, SxSzmax, P40, operator):
    if operator == 1: #AND
        return HW * HHmax * SxSzmax * P40
    if operator == 2:
        return (HW + HHmax + SxSzmax + P40) / 4


def fun_HW(HW):
    lmh=[0,0,0]
    #---------------LOW---------------------
    a_f_low = -1 / 1.5
    b_f_low = 2 / 1.5

    if HW <= 0.5:
        lmh[0] = 1    
    if HW > 0.5 and HW <= 2:
        #na podstawie y=ax+b wyznaczam wartosc
        #etykiety "low"
        lmh[0] = a_f_low * HW + b_f_low 
    if HW > 2:
        lmh[0] = 0
    #---------------MEDIUM-------------------
    a_f_medL = 1 / 1.4
    b_f_medL = - 1 / 2.8
    a_f_medR = -1 / 1.5
    b_f_medR =  3.4 / 1.5
    if HW < 0.5:
        lmh[1] = 0    
    if HW >= 0.5 and HW <= 1.9:
        lmh[1] = a_f_medL * HW + b_f_medL
    if HW > 1.9 and HW <= 3.4:
        lmh[1] = a_f_medR * HW + b_f_medR
    if HW > 3.4 :
        lmh[1] = 0
    #---------------HIGH---------------------
    a_f_high = 1/2
    b_f_high = - 3/4
    if HW < 1.5:
        lmh[2] = 0
    if HW >= 1.5 and HW <= 3.5:
        lmh[2] = a_f_high*HW + b_f_high
    if HW > 3.5:
        lmh[2] = 1
    
    return lmh

def fun_HHmax(HHmax):
    lmh=[0,0,0]
    #---------------LOW---------------------
    a_f_low = -1 / 0.2
    b_f_low = 0.45 / 0.2

    if HHmax < 0.25:
        lmh[0] = 1    
    if HHmax >= 0.25 and HHmax <= 0.45:
        #na podstawie y=ax+b wyznaczam wartosc
        #etykiety "low"
        lmh[0] = a_f_low * HHmax + b_f_low 
    if HHmax > 0.45:
        lmh[0] = 0
    #---------------MEDIUM-------------------
    a_f_medL = 1 / 0.6
    b_f_medL = 0
    a_f_medR = -1 / 0.6
    b_f_medR =  2
    if HHmax < 0:
        lmh[1] = 0    
    if HHmax >= 0 and HHmax <= 0.6:
        lmh[1] = a_f_medL * HHmax + b_f_medL
    if HHmax > 0.6 and HHmax <= 1.2:
        lmh[1] = a_f_medR * HHmax + b_f_medR
    if HHmax > 1.2:
        lmh[1] = 0
    #---------------HIGH---------------------
    a_f_high = 1/0.35
    b_f_high = - 0.6/0.35
    if HHmax < 0.6:
        lmh[2] = 0
    if HHmax >= 0.6 and HHmax <= 0.95:
        lmh[2] = a_f_high*HHmax + b_f_high
    if HHmax > 0.95:
        lmh[2] = 1
    
    return lmh

def fun_SxSzmax(SxSzmax):
    lmh=[0,0,0]
    #---------------LOW---------------------
    a_f_low = -1 / 230
    b_f_low = 380 / 230

    if SxSzmax < 150:
        lmh[0] = 1    
    if SxSzmax >= 150 and SxSzmax <= 380:
        #na podstawie y=ax+b wyznaczam wartosc
        #etykiety "low"
        lmh[0] = a_f_low * SxSzmax + b_f_low 
    if SxSzmax > 380:
        lmh[0] = 0
    #---------------MEDIUM-------------------
    a_f_medL = 1 / 110
    b_f_medL = -10/11
    a_f_medR = -1 / 210
    b_f_medR =  52/21
    if SxSzmax < 100:
        lmh[1] = 0    
    if SxSzmax >= 100 and SxSzmax <= 310:
        lmh[1] = a_f_medL * SxSzmax + b_f_medL
    if SxSzmax > 310 and SxSzmax <= 520:
        lmh[1] = a_f_medR * SxSzmax + b_f_medR
    if SxSzmax > 520:
        lmh[1] = 0
    #---------------HIGH---------------------
    a_f_high = 1/340
    b_f_high = - 150/340
    if SxSzmax < 150:
        lmh[2] = 0
    if SxSzmax >= 150 and SxSzmax <= 490:
        lmh[2] = a_f_high*SxSzmax + b_f_high
    if SxSzmax > 490:
        lmh[2] = 1
    
    return lmh

def fun_P40(P40):
    lmh=[0,0,0]
    #---------------LOW---------------------
    a_f_low = -1 / 0.29
    b_f_low = 0.46 / 0.29

    if P40 < 0.17:
        lmh[0] = 1    
    if P40 >= 0.17 and P40 <= 0.46:
        #na podstawie y=ax+b wyznaczam wartosc
        #etykiety "low"
        lmh[0] = a_f_low * P40 + b_f_low 
    if P40 > 0.46:
        lmh[0] = 0
    #---------------MEDIUM-------------------
    a_f_medL = 1 / 0.31
    b_f_medL = - 0.12/0.31
    a_f_medR = -1 / 0.27
    b_f_medR =  0.7/0.27
    if P40 < 0.12:
        lmh[1] = 0    
    if P40 >= 0.12 and P40 <= 0.43:
        lmh[1] = a_f_medL * P40 + b_f_medL
    if P40 > 0.43 and P40 <= 0.7:
        lmh[1] = a_f_medR * P40 + b_f_medR
    if P40 > 0.7:
        lmh[1] = 0
    #---------------HIGH---------------------
    a_f_high = 1/0.27
    b_f_high = - 0.42/0.27
    if P40 < 0.42:
        lmh[2] = 0
    if P40 >= 0.42 and P40 <= 0.69:
        lmh[2] = a_f_high*P40 + b_f_high
    if P40 > 0.69:
        lmh[2] = 1
    
    return lmh

def fun_Pose(pose_Value):
    isMayNotLy =[0,0,0]
    #---------------IsLy---------------------
    a_f_isLy = -4
    b_f_isLy = 1.92

    if pose_Value < 0.23 :
        isMayNotLy[0] = 1
    if pose_Value >= 0.23 and pose_Value <= 0.48:
        isMayNotLy[0] = a_f_isLy * pose_Value + b_f_isLy
    if pose_Value > 0.48:
        isMayNotLy[0] = 0

    #---------------MayLy---------------------
    a_f_mayLyL = 1/0.38
    b_f_mayLyL = 0.12/0.38
    a_f_mayLyR = -1/0.39
    b_f_mayLyR = 0.89/0.39

    if pose_Value < 0.12 :
        isMayNotLy[1] = 0
    if pose_Value >= 0.12 and pose_Value <= 0.5:
        isMayNotLy[1] = a_f_isLyL * pose_Value + b_f_isLyL
    if pose_Value > 0.5 and pose_Value <= 0.89:
        isMayNotLy[1] = a_f_isLyR * pose_Value + b_f_isLyR
    if pose_Value > 0.89 :
        isMayNotLy[1] = 0
    #---------------NotLy---------------------
    a_f_notLy = 4
    b_f_notLy = 2.08

    if pose_Value < 0.52 :
        isMayNotLy[2] = 0
    if pose_Value >= 0.52 and pose_Value <= 0.77:
        isMayNotLy[2] = a_f_notLy * pose_Value + a_f_notLy
    if pose_Value > 0.77:
        isMayNotLy[2] = 1

    return isMayNotLy


HW = fun_HW(0.70)
HHmax = fun_HHmax(0.58)
sigma = fun_SxSzmax(480)
P40 = fun_P40(0.61)



print("HW: ",HW)
print("HHmax: ",HHmax)
print("max( sigma x, sigma z): ",sigma)
print("P40: ",P40)
print("-------------------")

reguly.przynal_do_pozycji(P40, HW, sigma, HHmax)
print(reguly.notLy)
print(reguly.mayLy)
print(reguly.isLy)

reguly.defuzyfikacja()