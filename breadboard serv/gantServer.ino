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

const char* mqtt_user = "esp";
const char* mqtt_mdp = "esp";

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
    if (client.connect("esp", mqtt_user, mqtt_mdp)) {
      Serial.println("Connecte au Broker !");
    } else {
      Serial.print("Echec, code d'erreur = ");
      Serial.print(client.state());
      Serial.println(" Reessai dans 5 secondes");
      delay(2500);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);

  pinMode(btn1, INPUT_PULLUP); //initialisation des boutons
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
  if (digitalRead(btn1) == LOW) { // Si le bouton 1 est appuyé
    client.publish("gantServer/index", "btn1"); // On publie sur un topic précis
    Serial.println("Action: Index");
    // On ajoute yield() pour éviter les rebonds du bouton
    while(digitalRead(btn1) == LOW) { 
      yield(); 
    } 
    delay(5000); // On ajoute un temps de recharge aux boutons
  }

  if (digitalRead(btn2) == LOW) { // Si le bouton 2 est appuyé
    client.publish("gantServer/majeur", "btn2");
    Serial.println("Action: Majeur");
    while(digitalRead(btn2) == LOW) { 
      yield(); 
    }
    delay(5000);
  }

  if (digitalRead(btn3) == LOW) { // Si le bouton 3 est appuyé
    client.publish("gantServer/annulaire", "btn3");
    Serial.println("Action: Annulaire");
    while(digitalRead(btn3) == LOW) { 
      yield(); 
    }
    delay(5000);
  }

  if (digitalRead(btn4) == LOW) { // Si le bouton 4 est appuyé
    client.publish("gantServer/auriculaire", "btn4");
    Serial.println("Action: Auriculaire");
    while(digitalRead(btn4) == LOW) { 
      yield(); 
    }
    delay(5000);
  }
}
