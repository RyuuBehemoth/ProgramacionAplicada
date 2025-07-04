int POT_sp = 32; //Potenciometro
int PWM_salida = 27; //Motor puente h
int pinA = 33; //Encoder
float sp;
float pv;

volatile int contador = 0;
unsigned long pMillis = 0;
long interval = 100;

float cv;
float cv1;
float error;
float error1;
float error2;

float Kp = 1;
float Ki = 1;
float Kd = 0.01;
float Tm = 0.1;

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
  //------SET POINT----
  sp = analogRead(POT_sp)*(380.0/4095.0);

  error = sp - pv;

  //-----ECUACION DE DIFERENCIAS-----
  cv = cv1 + (Kp + Kd/Tm)*error + (-Kp + Ki*Tm - 2*Kd/Tm)*error1 + (Kd/Tm)*error2;
  cv1 = cv;
  error2 = error1;
  error1 = error;

  //-----SATURAMOS LA SALIDA DEL PID-----
  if (cv > 500.0){
    cv = 500.0;
  }
  if (cv > 30.0){
    cv = 500.0;
  }

  analogWrite(PWM_salida,cv*(255.0/500.0));

  Serial.print("SP: ");
  Serial.print(sp);
  Serial.print("PV: ");
  Serial.println(pv);

  delay(100);
}

void interrupcion(){
  contador++;
}