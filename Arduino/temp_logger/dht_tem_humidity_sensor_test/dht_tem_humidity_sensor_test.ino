#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN 2
DHT dht(DHTPIN, DHT22);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();
  Serial.print("DHT Initiated");
}

void loop() {
  // put your main code here, to run repeatedly:

  delay(1000);
  Serial.println(dht.readTemperature() * 1.8 + 32.0);
  Serial.println(dht.readHumidity());

}