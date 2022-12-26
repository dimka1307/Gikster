import publisher
import publisher1
import publisher2
import publisher5
import subscribe_cena
import kusur
#import send_data_ard
# import auto_transfer
# import photo_capture

# Vnesuvanje na pocetni vrednosti na sharzerot
s1=int(input("Vnesi vrednost za sharzer 1 "))
s2=int(input("Vnesi vrednost za sharzer 2 "))
s3=int(input("Vnesi vrednost za sharzer 3 "))
promet=0
s = True
while s == True:
    #proveruva dali nekoj od shrzerite e prazen
    if s1<3:
        publisher1.main()
    if s2<3:
        publisher2.main()
    if s3<3:
        publisher5.main()
    #ceka da pritisneme enter da za napravi slika
    input("Press enter when ready to take a photo ")
    #slika
    #photo_capture.main()
    #isprakja slika na kompjuter
    #auto_transfer.main()
    #prima cena od mqtt
    cena = subscribe_cena.main()
    #cena=25
    #vnesuvame pari preku tastatura
    pari = input("Vnesete pari na kupuvach ")
    #presmetuva kusur
    k=int(pari)-int(cena)
    if k<0:
        print("Not enough money ")
    elif k==0:
        print("No change ")
        promet = promet+int(cena)
        publisher.main(s1,s2,s3,promet)
    else:
        print("Change: " + str(k))
        #presmetuva servo dvizenja [x1,x2,x5]
        servo_dvizhenja=kusur.main(k)
        #isprakja info preku serial port na arduino
        #send_data_ard.main(servo_dvizhenja)
        #presmetuva novi vrednosti na sharzeri
        s1=s1-servo_dvizhenja[0];s2=s2-servo_dvizhenja[1];s3=s3-servo_dvizhenja[2]
        #presmetuva promet
        promet= promet+int(cena)
        #publish na mqtt
        publisher.main(s1,s2,s3,promet)
    f = input("Press 0 to continue ")
    if int(f)==0:
        s=True
    else:
        s=False