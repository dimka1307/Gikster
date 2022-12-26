#include <Servo.h>

Servo servos[3];
//Servo myServo2;
//Servo myServo5;
//


bool pozicija_servo[3] = {false, false, false};
void setup() {
  Serial.begin(9600);
  
  servos[0].attach(3);
  servos[1].attach(5);
  servos[2].attach(6);
  
  //inicijalni pozicii za site 3 servo motori
  servos[0].write(0);
  servos[1].write(0);
  servos[2].write(0);

  
}




//int* vrati_kusur(int kusur)
//{
//  int denominacii[3] = {5, 2, 1};
//  // kolku pati da se pridvizhat
//  static int servo_dvizhenja[3] = {0, 0, 0};
//  
//  for (int i = 0; i < 3; i++)
//  {
//    while (kusur >= denominacii[i])
//    {
//      servo_dvizhenja[i]++;
//      kusur -= denominacii[i];
//    }
//  }
//  
//  return servo_dvizhenja;
//}


bool pridvizhi_edno_servo(Servo Servo_motor, int povtoruvanja, bool pozicija_servo)
{
  int pos;
  while (povtoruvanja != 0)
  {
    if (pozicija_servo == false)
    {
      for (pos = 180; pos >= 0; pos -= 1)
      {
        Servo_motor.write(pos);
        delay(15);
      }
      pozicija_servo = true;
    }
    
    else
    {
      for (pos = 0; pos <= 180; pos += 1)
      {
        Servo_motor.write(pos);
        delay(15);
      }
      pozicija_servo = false;
    }
    
    povtoruvanja--;
  }
  return pozicija_servo;
}


bool* pridvizhi_servo_motori(int* povtoruvanja_lista, bool* prethodna_sostojba)
{
  for (int i = 0; i < 3; i++)
  {
    prethodna_sostojba[i] = pridvizhi_edno_servo(servos[i], povtoruvanja_lista[i], prethodna_sostojba[i]);
  }
  return prethodna_sostojba;
}

int* read_servo_dvizhenja()
{
  // Proveri dali ima data za chitanje
    while (Serial.available() == 0)
    {
    } 
    String x1_string = Serial.readString();
    while (Serial.available() == 0)
    {
    }
    String x2_string = Serial.readString();
    while (Serial.available() == 0)
    {
    }
    String x3_string = Serial.readString();
    int x1_int = x1_string.toInt();
    int x2_int = x2_string.toInt();
    int x3_int = x3_string.toInt();
    int servo_dvizhenja[3] = {x1,x2,x3};
    return servo_dvizhenja;
}











void loop() 
{
  // Proveri dali ima data za chitanje
//    while (Serial.available() == 0)
//    {
//    } 
//    String cena_string = Serial.readString();
//    int cena_int = cena_string.toInt();
//    Serial.println("Kolku platil klientot: ");
//    while (Serial.available() == 0)
//    {
//    }   
//  
//    //  int cena_int = 16; 
//    
//    // Prochitaj integer
//    String naplata_string = Serial.readString();
//    //  String naplata_string = "20";
//    int naplata_int = naplata_string.toInt();
//
//  
//    int kusur = naplata_int - cena_int;
//    //    Serial.println(String(kusur));
//    int* servo_dvizhenja;
//    
//    servo_dvizhenja = vrati_kusur(kusur);
    int* servo_dvizhenja[3]={0,0,0};
    servo_dvizhenja = read_servo_dvizhenja();
    //    bool* pozicija_servo;
    *pozicija_servo = pridvizhi_servo_motori(servo_dvizhenja, pozicija_servo);
}
