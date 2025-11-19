import paho.mqtt.client as mqtt
import time
import json
import random

# --- Tus Datos de Conexión ---
BROKER_HOST = "wan-piece-5075909d.a02.usw2.aws.hivemq.cloud"
BROKER_PORT = 8883
USERNAME = "luffy"
PASSWORD = "WanPiece5"

# --- Tópico 
TOPICO = "lan/sala2/sensor/temp"
SENSOR_ID = "sensor-temp-sala2"

# --- Código del Publisher ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[+] '{SENSOR_ID}' conectado al broker.")
    else:
        print(f"[-] Fallo al conectar, código de error: {rc}")

client = mqtt.Client(client_id=SENSOR_ID)
client.on_connect = on_connect
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()

try:
    client.connect(BROKER_HOST, BROKER_PORT)
except Exception as e:
    print(f"[-] Error al conectar: {e}")
    exit()

client.loop_start()

# Loop para publicar un mensaje cada 3 segundos
print(f"[*] {SENSOR_ID} (Publisher) iniciado. Publicando en '{TOPICO}'...")
print("[*] Presiona CTRL+C para detener.")

try:
    while True:
        # 1. Generar lectura simulada
        valor = round(random.uniform(20.0, 30.0), 2)
        
        payload = {
            "sensor_id": SENSOR_ID,
            "valor": valor,
            "unidad": "°C",
            "timestamp": int(time.time())
        }
        
        # 2. Publicar en el tópico
        client.publish(TOPICO, json.dumps(payload))
        print(f"   Enviado: {valor}°C a '{TOPICO}'")
        
        # 3. Esperar
        time.sleep(1) 
        
except KeyboardInterrupt:
    print("\n[*] Simulación detenida.")

client.loop_stop()
client.disconnect()
