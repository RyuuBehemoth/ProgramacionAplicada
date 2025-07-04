int POT_sp = 32; //Potenciometro
int PWM_salida = 27; //Motor puente h
int pinA = 33; //Encoder
float sp;
float pv;

volatile int contador = 0;
unsigned long pMillis = 0;
long interval = 100;

void setup() {
  pinMode(pinA,INPUT);
  pinMode(PWM_salida,OUTPUT);
  Serial.begin(115200);
  attachInterrupt(digitalPinToInterrupt(pinA),interrupcion,RISING);
}

void loop() {
  unsigned long cMillis = millis();
  if ((cMillis - pMillis) >= interval){
    pMillis = cMillis;
    pv = 10*contador*(60.0/144.0);
    contador = 0;
  }

  sp = analogRead(POT_sp)*(100.0/4095.0);
  analogWrite(PWM_salida,sp*(255.0/100.0));

  Serial.print("SP: ");
  Serial.print(sp);
  Serial.print("PV: ");
  Serial.println(pv);
}

void interrupcion(){
  contador++;
}