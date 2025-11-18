import paho.mqtt.client as mqtt
import time

# --- Datos de Conexión ---
BROKER_HOST = "wan-piece-5075909d.a02.usw2.aws.hivemq.cloud"
BROKER_PORT = 8883
USERNAME = "luffy"
PASSWORD = "WanPiece5"

# --- Tópico de Prueba ---
TOPICO_PRUEBA = "sensores/prueba"
MENSAJE = "¡Hola, broker! Este es un mensaje de prueba."

# --- Código de Prueba ---

def on_connect(client, userdata, flags, rc):
    """Función que se llama al conectar."""
    if rc == 0:
        print(f"[+] Conectado exitosamente al broker ({BROKER_HOST})")
        # Una vez conectados, publicamos nuestro mensaje
        print(f"[*] Publicando '{MENSAJE}' en el tópico '{TOPICO_PRUEBA}'...")
        client.publish(TOPICO_PRUEBA, MENSAJE)
    else:
        print(f"[-] Fallo al conectar, código de error: {rc}")

def on_publish(client, userdata, mid):
    """Función que se llama después de publicar."""
    print("[+] Mensaje publicado exitosamente.")

# Configurar el cliente
client = mqtt.Client(client_id="sensor-prueba-01")
client.on_connect = on_connect
client.on_publish = on_publish

# Configurar credenciales y TLS
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()

# Conectar
try:
    print(f"[*] Conectando...")
    client.connect(BROKER_HOST, BROKER_PORT)
except Exception as e:
    print(f"[-] Error al conectar: {e}")
    exit()

# Iniciamos el loop para manejar los callbacks (on_connect, on_publish)
client.loop_start()

# Esperamos 3 segundos para dar tiempo a que se conecte y publique
print("[*] Esperando 3 segundos...")
time.sleep(3)

# Detenemos el loop y desconectamos
client.loop_stop()
client.disconnect()
print("[*] Desconectado.")
