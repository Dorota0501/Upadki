import pickle
import random

# ------------ prepared_data ------------
# 'fall01': [ [Pose, P40, HW, sigma, HHmax],
#             [Pose, P40, HW, sigma, HHmax]
#                          ...  ]
# 'fall02': [ [Pose, P40, HW, sigma, HHmax],
#             [Pose, P40, HW, sigma, HHmax]
#                          ...  ]
#                   ...

def readFeatures():                                                    
    # -------- Reading a data --------
    features2D_in = open('features2D.pickle', 'rb')                    
    features2D = pickle.load(features2D_in)                            
                                                                      
    features3D_in = open('features3D.pickle', 'rb')
    features3D = pickle.load(features3D_in)

    classes_in = open('classes.pickle', 'rb')
    classes = pickle.load(classes_in)
    del(features2D_in)
    del(features3D_in)
    del(classes_in)
    #print("fetures 2D",features2D.keys())
    #print("fetures 3D",features3D)
    #print("classes",classes)

   
   # -------- Preparing a data --------

    raw_data = {}
    prepared_data = {} 
    for k in features2D.keys():
        all_frames2D = features2D[k]
        all_frames3D = features3D[k]
        all_framesClass = classes[k]

        Pose = all_framesClass.get('class')
        HW = all_frames2D.get('HeightWidthRatio')
        P40 = all_frames3D.get('P40')                                       
        HHmax = all_frames3D.get('HHmaxRatio')                              
        sigma = all_frames3D.get('MaxStdXZ')                                
                                                                            
        raw_data[k] = [Pose, P40, HW, sigma, HHmax]                         
        #print("raw_data: ",raw_data)
   
    
    
    for k in raw_data.keys():                                                  
        prepared_data[k] = []  
        i = 1
        for p,l,m,n,o in zip(raw_data[k][0],raw_data[k][1],                    
                             raw_data[k][2],raw_data[k][3],raw_data[k][4]):    
            #print("number: ",i,": ",p,l,m,n,o)
            prepared_data[k].append([p,l,m,n,o,i])                    #format explained at top
            i += 1    
    
    #for i in prepared_data.keys():
    #    print(i)
    #    for j in prepared_data[i]:
    #        print(j)
    return prepared_data



def cut_data(prepared_data):
    new_prepared=[]
    new_prepared = dict(prepared_data)
    lenght = 0
    tablica = []
    
    for i in new_prepared:
        lenght += len(new_prepared[i])
        for j in new_prepared[i]:
            tablica.append(j)
       
    print("\n\n",tablica[1])

    percent = lenght * 0.05
    cut_record = []
    i = 0
    while i < percent:
        record = random.randint(0,lenght)
        if record in cut_record:
            print("record juz jest : ", record)
        else:
            print("wycinam: ", record)
            i+=1
            losuj = random.randint(1,4)
            tablica[record][losuj] = None
            cut_record.append(record)      

    #usuwanie numeru klatki
    filepath_cut = "cut_data.txt"
    f_cut = open(filepath_cut, "a")
    for i in range(len(tablica)):
        tablica[i].remove(tablica[i][5])   #po wywołaniu tej linijki zmienia sie oryginał prepared_data
        f_cut.write(str(tablica[i]) + '\n')    
    f_cut.close

            
    
