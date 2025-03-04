#include <SPI.h>
#include <LoRa.h>
#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "";
const char* password = "";
const char* serverUrl = "http://192.168.2.134:8000/api/data/gps/";

// LoRa pins
#define LORA_SCK 18
#define LORA_MISO 19
#define LORA_MOSI 23
#define LORA_CS 5
#define LORA_RST 14
#define LORA_IRQ 26

void setup() {
  // Disable Bluetooth (no WiFi or BT will be used)
  btStop();         // Turn off Bluetooth

  // Initialize Serial Monitor
  Serial.begin(115200);

  delay(10);
  Serial.println();
  Serial.println();
  Serial.print("Connecting to");
  Serial.println(ssid);

  WiFi.begin(ssid,password);
  while (WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi Connected");

  // Initialize LoRa with best parameters for a moving vehicle
  Serial.println("Initializing LoRa...");
  delay(500);  // Small delay to stabilize peripheralsg
  LoRa.setPins(LORA_CS, LORA_RST, LORA_IRQ);
  
  // Set LoRa parameters for moving vehicle (SF7, Bandwidth 125kHz, CR 4/5)
  LoRa.setSpreadingFactor(7);  // SF7 for fast transmission
  LoRa.setSignalBandwidth(125E3);  // 125 kHz bandwidth for reliability
  LoRa.setTxPower(20);          // Set transmission power to 20 dBm
  LoRa.setCodingRate4(5);       // Coding rate 4/5 for good error correction

  if (!LoRa.begin(433E6)) {  // Set frequency to match transmitter (433 MHz)
    Serial.println("LoRa initialization failed!");
    while (1);  // Halt if LoRa initialization fails
  }
  Serial.println("LoRa Initialized.");
}

void loop() {
  // Check if LoRa data is available
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    String receivedData = "";
    while (LoRa.available()) {
      receivedData += (char)LoRa.read();
    }
    Serial.println("Received: " + receivedData);  // Print received data
  }

  WiFiClient client;
  HTTPClient http;

  Serial.print("Connecting to Server: ");
  Serial.println(serverUrl);

  http.begin(client, serverUrl);
  http.addHeader("Content-Type", "application/json");
  int httpResponseCode = http.POST(payload);
  
  if (httpResponseCode > 0) {
    Serial.print("HTTP Response Code: ");
    Serial.print("httpResponseCode");
  } else {
    Serial.print("Error During HTTP Post: ");
    Serial.println(httpResponseCode);
  }
  http.end();

}