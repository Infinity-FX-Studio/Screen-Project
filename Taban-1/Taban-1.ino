#define ENCA 0
#define ENCB 1
#define PWM 3

int pos = 0;
int encoderValue = 0;
int lastEncoderValue = 0;
int b = digitalRead(ENCB);

void setup(){
  Serial.begin(9600);
  pinMode(PWM, OUTPUT);
  pinMode(ENCA, INPUT);
  pinMode(ENCB, INPUT);
  attachInterrupt(digitalPinToInterrupt(ENCA),readEncoder,RISING);
}

void loop(){
  encoderValue = pos;
  Serial.println(pos);
  if (encoderValue > 1100){
    digitalWrite(PWM, LOW);
    lastEncoderValue = encoderValue;
  }
  if (encoderValue{
    digitalWrite(PWM, HIGH);
  }
}

void readEncoder(){
  if(b>0){
    pos++;
  }
  else if (b<0){
    pos--; 
  }
}
