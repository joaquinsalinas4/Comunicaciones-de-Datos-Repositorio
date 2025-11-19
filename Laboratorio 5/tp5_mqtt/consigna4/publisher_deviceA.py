import paho.mqtt.client as mqtt
import time
import json

# --- Tus Datos de Conexión ---
BROKER_HOST = "wan-piece-5075909d.a02.usw2.aws.hivemq.cloud"
BROKER_PORT = 8883
USERNAME = "luffy"
PASSWORD = "WanPiece5"

# --- Tópico 
TOPICO = "lan/deviceA/status"
CLIENT_ID = "Dispositivo-A"

# --- Código del Publisher ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[+] '{CLIENT_ID}' conectado al broker.")
    else:
        print(f"[-] Fallo al conectar, código de error: {rc}")

client = mqtt.Client(client_id=CLIENT_ID)
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
print(f"[*] {CLIENT_ID} (Publisher) iniciado. Publicando en '{TOPICO}'...")
print("[*] Presiona CTRL+C para detener.")

try:
    while True:
        payload = {
            "status": "online",
            "timestamp": int(time.time())
        }
        msg = json.dumps(payload)
        client.publish(TOPICO, msg)
        print(f"   > Enviado: {msg}")
        time.sleep(3)
        
except KeyboardInterrupt:
    print("\n[*] Simulación detenida.")

client.loop_stop()
client.disconnect()
print(f"[*] {CLIENT_ID} desconectado.")
