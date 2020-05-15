//Main arduino 1 file
 

void setup() {
 Serial.begin(9600);
 pinMode(8, INPUT); // first sensor input
 pinMode(7, INPUT); // second sensor input
 pinMode(6, INPUT); // third sensor input
 pinMode(5, INPUT); // fourth sensor input

}

void loop()
{

    int sensordata_1 = digitalRead(8); // read status and store it into variable
     {
          if(sensordata_1 == LOW)        //  CAGE 1
          {
            Serial.println(String(1));  // 
          }
//          else
//          {
//            Serial.println(String(0));
//          }
          delay(200);
      
    }
    int sensordata_2 = digitalRead(7);
     {
          if(sensordata_2 == LOW)     //  CAGE 2
          {
            Serial.println(String(1));
          }
//          else
//          {
//            Serial.println(String(0));
//          }
          delay(200);
          
    }
//    int sensordata_3 = digitalRead(6);
//    {
//          if(sensordata_3 == LOW)    //  CAGE 3
//          {
//            Serial.println(String(1));
//          }
//          else
//          {
//            Serial.println(String(0));
//          }
//          delay(200);
//      
//    }
//    int sensordata_4 = digitalRead(5);
//    {
//          if(sensordata_4 == LOW)    //  CAGE 4
//          {
//            Serial.println(String(1));
//          }
//          else
//          {
//            Serial.println(String(0));
//          }
//          delay(200);
//      
//    }
//  
}
