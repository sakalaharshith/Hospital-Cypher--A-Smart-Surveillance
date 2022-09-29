import cv2
import numpy as np
import face_recognition
import requests
import os

def imgrecog():
    #face=cv2.VideoCapture(0);
    #ret,frame=face.read()
    #cv2.imwrite("imagetesting/imagetesting4.jpg",frame)
    #1elon=face_recognition.load_image_file('images/elonmusk1.jpg');
    #1elon=cv2.cvtColor(elon,cv2.COLOR_BGR2RGB)
    elon_test=face_recognition.load_image_file('imagetesting/vinod.jpeg');
    elon_test=cv2.cvtColor(elon_test,cv2.COLOR_BGR2RGB)
    elon_test_encodings=face_recognition.face_encodings(elon_test)
    print('face encodings', len(elon_test_encodings))
    elon_test_face_location=face_recognition.face_locations(elon_test)
    print(len(elon_test_face_location))
    print(elon_test_face_location)
    for dirpaths,dirnames,fnames in os.walk('./images'):
        for f in fnames:
            if f.endswith('.png') or f.endswith('.jpg'):
                face=face_recognition.load_image_file('images/'+f)
                face=cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
                encoding=face_recognition.face_encodings(face)[0]
                res=face_recognition.compare_faces(encoding,elon_test_encodings)
                #print(f)
                
                if len(res)>1:
                    
                    if res[0]:
                        i=cv2.rectangle(elon_test,(elon_test_face_location[0][3],elon_test_face_location[0][0]),(elon_test_face_location[0][1],elon_test_face_location[0][2]),(0,0,255),3)
                        cv2.imwrite('imagetesting/'+'check1.jpg',i)
                    
                    if res[1]:
                        i=cv2.rectangle(elon_test,(elon_test_face_location[1][3],elon_test_face_location[1][0]),(elon_test_face_location[1][1],elon_test_face_location[1][2]),(0,0,255),3)
                        cv2.imwrite('imagetesting/'+'check1.jpg',i)
                else:
                    if res[0]:
                        print(f)
                        print('here')
                        i=cv2.rectangle(elon_test,(elon_test_face_location[0][3],elon_test_face_location[0][0]),(elon_test_face_location[0][1],elon_test_face_location[0][2]),(0,0,255),3)
                        cv2.imwrite('imagetesting/'+'check1.jpg',i)
                
    requests.get('https://api.telegram.org/bot1728553627:AAG3NoQ36_12EJuC9nxsQFqT9DX8soKOz7s/sendMessage?chat_id=-552939894&text=" covid patient escaping the hospital "')
      #  print("here")
    img={'photo':open('imagetesting/check1.jpg','rb')}
    requests.post('https://api.telegram.org/bot1728553627:AAG3NoQ36_12EJuC9nxsQFqT9DX8soKOz7s/sendPhoto?chat_id=-552939894',files=img)           
                
    #for dirpaths,dirnames,fnames in os.walk('./images'):
     #   for f in fnames:
      #      if f.endswith('.png') or f.endswith('.jpg'):
                #face=face_recognition.load_image_file("images/"+f)
                #face=cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
                #encoding=face_recognition.face_encodings(face)
                #known_face_encodings.append(encoding)
       #         face_names.append(f)
                
    #print(face_names)
    #resu=0
    #face_captured=face_recognition.load_image_file('images/'+face_names[0])
    #face_captured=cv2.cvtColor(face_captured,cv2.COLOR_BGR2RGB)
    #img=face_captured
    #for x in face_names:
        
     #   encode=face_recognition.face_encodings(face_captured)[0]
      #  face_test=face_recognition.load_image_file('images/'+x)
       # face_test=cv2.cvtColor(face_test,cv2.COLOR_BGR2RGB)
        #encode_test=face_recognition.face_encodings(face_test)[0]
        #resu=face_recognition.compare_faces([encode], encode_test)
        #if resu:
         #   face_location=face_recognition.face_locations(face_captured)[0]
        #count=0   
        #for res in resu:
         #   if res:
          #      print(x)
           #     print(res)
            #    img= cv2.rectangle(img,(face_location[3],face_location[0]),(face_location[1],face_location[2]),(0,0,255),2)
             #   print(img)
              #  break
               # count=count+1
    #print(len(resu))
    #cv2.imwrite('imagetesting/img1.jpg',img) 
    #print(count)           
    #print(face_names) 
    #known_image=face_recognition.load_image_file('images/'+face_names[1])
    #known_image=cv2.cvtColor(elon_test,cv2.COLOR_BGR2RGB)
    #encodes=face_recognition.face_encodings(known_image)
    #print(face_recognition.compare_faces(encodes,elon_test_encodings)) 
    #for x in face_names:
        
        #known_image=face_recognition.load_image_file('images/'+x)
        #known_image=cv2.cvtColor(elon_test,cv2.COLOR_BGR2RGB)
        #encodes=face_recognition.face_encodings(known_image)
        #print(face_recognition.compare_faces(encodes,elon_test_encodings))
        #print(result)
     #   print(x)
      #  count=0
        #for res in result:
         #   if res:
          #      print(x)
           #     display_image=cv2.rectangle(elon_test,(elon_test_face_location[count][3],elon_test_face_location[count][0]),(elon_test_face_location[count][1],elon_test_face_location[count][2]),(0,0,255),2)
            #    name="testimage1.jpg"
             #   cv2.imwrite('imagetesting/'+name,display_image)
              #   requests.get('https://api.telegram.org/bot1728553627:AAG3NoQ36_12EJuC9nxsQFqT9DX8soKOz7s/sendMessage?chat_id=-552939894&text="patient escaping the hospital "')
               # print("here")
                #img={'photo':open('imagetesting/'+name,'rb')}
                #requests.post('https://api.telegram.org/bot1728553627:AAG3NoQ36_12EJuC9nxsQFqT9DX8soKOz7s/sendPhoto?chat_id=-552939894',files=img)
                #break
    #1face_location=face_recognition.face_locations(elon)[0]
    #1face_encodings=face_recognition.face_encodings(elon)[0]
    #1cv2.rectangle(elon,(face_location[3],face_location[0]),(face_location[1],face_location[2]),(0,0,255),2)
    
    #face_location_test=face_recognition.face_locations(elon_test)[0]
    #face_encodings_test=face_recognition.face_encodings(elon_test)[0]
    #results=face_recognition.compare_faces([known_face_encodings],face_encodings_test)
    #print(results)
    #cv2.rectangle(elon_test,(face_location_test[3],face_location_test[0]),(face_location_test[1],face_location_test[2]),(0,0,255),2)
    #results=face_recognition.compare_faces([face_encodings],face_encodings_test)
    #results=[]
    #print(known_face_encodings)
    #for encodes in known_face_encodings:
     #  res=face_recognition.compare_faces(encodes,face_encodings_test)
      # results.append(res)
    #print(results)
    #display_image=elon_test
    #count=0
    #for x in results:
        #if x:
          #display_image=cv2.rectangle(display_image,(face_location_test[count][3],face_location_test[count][0]),(face_location_test[count][1],face_location_test[count][2]),(0,0,255),2)
          #count=count+1
    #cv2.imwrite('images/result1.jpg',display_image)
    #1cv2.putText(elon_test,f'{results}',(50,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0))
    #1cv2.imshow('elon musk',elon)
    ##cv2.waitKey(0)
    #cv2.destroyAllWindows()  
    #a=True
    #1print(results[0])
    #if results[0]:
     #   requests.get('https://api.telegram.org/bot1728553627:AAG3NoQ36_12EJuC9nxsQFqT9DX8soKOz7s/sendMessage?chat_id=-552939894&text="patient escaping the hospital "')
      #  print("here")
       # img={'photo':open('images/elonmusk2.jpg','rb')}
        #requests.post('https://api.telegram.org/bot1728553627:AAG3NoQ36_12EJuC9nxsQFqT9DX8soKOz7s/sendPhoto?chat_id=-552939894',files=img)
    # chat id- -552939894
    #print('outside if ')
    #base_url='https://api.telegram.org/bot1799283123:AAGTfSeJdR6t3sbkRMwQjzqUyS8tJfIyUwI/sendMessage?chat_id=-559510565&text="sending this message using python code"'
    
imgrecog()        