import paho.mqtt.client as mqtt
import json

# --- Tus Datos de Conexión ---
BROKER_HOST = "wan-piece-5075909d.a02.usw2.aws.hivemq.cloud"
BROKER_PORT = 8883
USERNAME = "luffy"
PASSWORD = "WanPiece5"

# --- Tópico
TOPICO_A_ESCUCHAR = "lan/broadcast/#"
CLIENT_ID = "Suscriber-2"

# --- Código del Subscriber ---
def on_connect(client, userdata, flags, rc):
    """Esta función se llama al conectarse."""
    if rc == 0:
        print(f"[+] '{CLIENT_ID}' conectado al broker.")
        # ¡IMPORTANTE! Nos suscribimos al tópico al conectarnos.
        client.subscribe(TOPICO_A_ESCUCHAR)
        print(f"[*] Suscrito a '{TOPICO_A_ESCUCHAR}'. Esperando mensajes...")
    else:
        print(f"[-] Fallo al conectar, código de error: {rc}")

def on_message(client, userdata, msg):
    """Esta función se llama CADA VEZ que llega un mensaje."""
    # msg.topic es el tópico
    # msg.payload es el mensaje (en bytes, hay que decodificarlo)
    try:
        payload_str = msg.payload.decode('utf-8')
        # Si sabemos que es JSON, lo podemos "cargar"
        datos = json.loads(payload_str)
        print(f"   < Recibido: {datos} (en tópico '{msg.topic}')")
    except Exception as e:
        # Si no es JSON, solo imprimimos el texto
        print(f"   < Recibido (raw): {msg.payload.decode('utf-8')} (en tópico '{msg.topic}')")


# Configurar el cliente
client = mqtt.Client(client_id=CLIENT_ID)
client.on_connect = on_connect  # Asignamos la función de conexión
client.on_message = on_message  # Asignamos la función de mensaje

# Configurar credenciales y TLS
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()

# Conectar
try:
    client.connect(BROKER_HOST, BROKER_PORT)
except Exception as e:
    print(f"[-] Error al conectar: {e}")
    exit()

# loop_forever() es un loop bloqueante.
# Mantiene el script vivo para escuchar mensajes por siempre.
print(f"[*] {CLIENT_ID} (Subscriber) iniciado. Presiona CTRL+C para detener.")
client.loop_forever()
