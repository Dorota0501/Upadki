import pickle


# ------------ prepared_data ------------
# 'fall01': [ [Pose, P40, HW, sigma, HHmax],
#             [Pose, P40, HW, sigma, HHmax] 
#                          ...              ]
# 'fall02': [ [Pose, P40, HW, sigma, HHmax],
#             [Pose, P40, HW, sigma, HHmax] 
#                          ...              ] 
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
        for p,l,m,n,o in zip(raw_data[k][0],raw_data[k][1],                    
                             raw_data[k][2],raw_data[k][3],raw_data[k][4]):    
            #print("number: ",i,": ",p,l,m,n,o)
            prepared_data[k].append([p,l,m,n,o])                    #format explained at top  
            
    print(prepared_data)
    
    
    #for i in prepared_data.keys():
    #    print(i)
    #    for j in prepared_data[i]:
    #        print(j)
    return prepared_data