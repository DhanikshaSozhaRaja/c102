import cv2
import dropbox
import time
import random

start_time = time.time()
print(start_time)

def take_snap():
    number = random.randint(0,100)
    vco = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = vco.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time()
        result = False
    return(img_name)
    print("Snap taken!")
    vco.release()
    cv2.destroyAllWindows()
def upload_file(img_name): 
    access_token = "sl.A_fqfBlOoVvCUGY5fo_L8QGouZ9iNDxEeGV-ZZ_JN3vM2WCQxCzo1QFeMezdXgt2Rtap1Hwt1Nq3ULHEg6Vn_PGJ9FOx-XGLnuSv4oiXgqBcwGUYwMS6ST_H7Vgw-DR3Pjuz73c" 
    file =img_name 
    file_from = file 
    file_to="/testFolder/"+(img_name) 
    dbx = dropbox.Dropbox(access_token) 
    with open(file_from, 'rb') as f: 
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite) 
        print("file uploaded")

def main(): 
    while(True): 
        if ((time.time() - start_time) >= 5): 
            name = take_snap() 
            upload_file(name)
main()