#include <IRremote.hpp>

const int RECEIVER_PIN = 7;
const int led = 5;

void setup(){
  Serial.begin(9600);
  IrReceiver.begin(RECEIVER_PIN, ENABLE_LED_FEEDBACK);
  pinMode(led, OUTPUT);
  digitalWrite(led, LOW); 
}

void loop(){
  if(IrReceiver.decode()){
    digitalWrite(led, HIGH);
    Serial.println(IrReceiver.decodedIRData.decodedRawData, HEX);
    delay(800);  
    digitalWrite(led, LOW);
    IrReceiver.resume();
  }
}