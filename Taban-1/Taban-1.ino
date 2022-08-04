#define ENCA 8
#define ENCB 4
#define PWM 11

int pos = 0;
long encoderValue = 0L;
long lastEncoderValue = 0L;
int b = digitalRead(ENCB);

void setup(){
  Serial.begin(9600);
  pinMode(PWM, OUTPUT);
  pinMode(ENCA, INPUT);
  pinMode(ENCB, INPUT);
  attachInterrupt(digitalPinToInterrupt(ENCA),readEncoder,RISING);
}

void loop(){
  encoderValue = digitalRead(ENCA);
  Serial.println(b);
}

void readEncoder(){
  if(b>0){
    pos++;
  }
  else if (b<0){
    pos--; 
  }
  else{
    Serial.println("AAAAA");
  }
}

void finish(){
  digitalWrite(PWM, LOW);
}

void start(){
  digitalWrite(PWM, HIGH);
}

void turn(){
  if (encoderValue > 1100 + lastEncoderValue){
    finish();
    lastEncoderValue = encoderValue;
  }
  else{
    start();
  }
}
