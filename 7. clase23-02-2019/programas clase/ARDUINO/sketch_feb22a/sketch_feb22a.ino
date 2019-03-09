#define MRA 0
#define MRB 1
#define PWM 2

#define ST1 4
#define ST2 9
char incomingByte;

void move_right(int pwm) {
  if( pwm<0 ){
    pwm = 0-pwm;
    digitalWrite(ST1+MRA, LOW);
    digitalWrite(ST1+MRB, HIGH);
  } else {
    digitalWrite(ST1+MRA, HIGH);
    digitalWrite(ST1+MRB, LOW);
  }
  analogWrite(ST1+PWM, pwm);
}

void move_left(int pwm) {
  if( pwm<0 ){
    pwm = 0-pwm;
    digitalWrite(ST2+MRA, LOW);
    digitalWrite(ST2+MRB, HIGH);
  } else {
    digitalWrite(ST2+MRA, HIGH);
    digitalWrite(ST2+MRB, LOW);
  }
  analogWrite(ST2+PWM, pwm);
}


void setup() {
  // put your setup code here, to run once:
 for(int i=0; i<3; i++){
    pinMode((ST1+i), OUTPUT);
    pinMode((ST2+i), OUTPUT);
  }
  Serial.begin(9600); //Inicializo el puerto serial a 9600 baudios
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
   Serial.flush();
   incomingByte = Serial.read();
   if(incomingByte == '0'){
     move_right(0);
     move_left(0);
   }
   if(incomingByte == '1'){
     move_right(100);
     move_left(100);
   }
   if(incomingByte == '2'){
     move_right(110);
     move_left(-110);
   }
   if(incomingByte == '3'){
     move_right(-110);
     move_left(110);
   }
   delay(100);
 }
}
