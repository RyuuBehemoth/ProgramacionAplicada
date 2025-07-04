#include <TinyGPS++.h>
#include <HardwareSerial.h>

TinyGPSPlus gps;
HardwareSerial gpsSerial(1); // Usamos UART1

void setup() {
  Serial.begin(115200);
  gpsSerial.begin(9600, SERIAL_8N1, 16, 17); // TX=16, RX=17

  Serial.println("Esperando datos GPS...");
}

void loop() {
  while (gpsSerial.available() > 0) {
    gps.encode(gpsSerial.read());

    if (gps.location.isUpdated()) {
      Serial.print("Latitud: ");
      Serial.println(gps.location.lat(), 6);
      Serial.print("Longitud: ");
      Serial.println(gps.location.lng(), 6);
      Serial.print("Satélites: ");
      Serial.println(gps.satellites.value());
      Serial.print("Altura: ");
      Serial.print(gps.altitude.meters());
      Serial.println(" m");
      Serial.println("------------------------");
    }
  }
}
