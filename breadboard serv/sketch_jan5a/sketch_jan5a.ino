#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// --- CONFIGURATION ---
const char* ssid = "binome_1";
//const char* password = "tpRT9025";
const char* mqtt_server = "192.168.1.106";

const int btn1 = 2; // D4
const int btn2 = 5; // D1
const int btn3 = 4; // D2
const int btn4 = 0; // D3

WiFiClient esp;
PubSubClient client(esp);

//mdp esp

void setup_wifi() {
  delay(10);
  Serial.print("\nConnexion a ");
  Serial.println(ssid);
  WiFi.begin(ssid); //, password
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connecte !");
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Tentative de connexion MQTT...");
    if (client.connect("esp")) {
      Serial.println("Connecte au Broker !");
    } else {
      Serial.print("Echec, code d'erreur = ");
      Serial.print(client.state());
      Serial.println(" Reessai dans 5 secondes");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);

  pinMode(btn1, INPUT_PULLUP);
  pinMode(btn2, INPUT_PULLUP);
  pinMode(btn3, INPUT_PULLUP);
  pinMode(btn4, INPUT_PULLUP);

  Serial.println("Systeme pret !");
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // --- LOGIQUE DES BOUTONS ---
//gantServeur/index
//gantServeur/majeur
//gantServeur/annulaire
//gantServeur/auriculaire
  if (digitalRead(btn1) == LOW) {
    client.publish("gantServeur/index", "btn1");
    Serial.println("Action Envoyee: Bouton 1");
    while(digitalRead(btn1) == LOW); delay(50);
  }

  if (digitalRead(btn2) == LOW) {
    client.publish("gantServeur/majeur", "btn2");
    Serial.println("Action Envoyee: Bouton 2");
    while(digitalRead(btn2) == LOW); delay(50);
  }

  if (digitalRead(btn3) == LOW) {
    client.publish("gantServeur/annulaire", "btn3");
    Serial.println("Action Envoyee: Bouton 3");
    while(digitalRead(btn3) == LOW); delay(50);
  }

  if (digitalRead(btn4) == LOW) {
    client.publish("gantServeur/auriculaire", "btn4");
    Serial.println("Action Envoyee: Bouton 4");
    while(digitalRead(btn4) == LOW); delay(50);
  }
}