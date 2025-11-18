import paho.mqtt.client as mqtt
import random
import json # Para enviar los datos
import time

# --- Datos de conexion ---
BROKER_HOST = "wan-piece-5075909d.a02.usw2.aws.hivemq.cloud"
BROKER_PORT = 8883 
USERNAME = "luffy"
PASSWORD = "WanPiece5"

# -- Configuracion del sensor 
TOPICO = "sensores/habitacion1/temperatura"  # Etiqueta para las suscripciones. las / indican jerarquia logica
SENSOR_ID = "sensor-temp-01"

# Codigo del propio sensor

# Funcion que se llama cuando nos conectamos exitosamente
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[+] Sensor '{SENSOR_ID}' conectado exitosamente al broker!")
    else:
        print(f"[-] fallo al conectar, codigo de error: {rc}")

# Configurar el cliente MQTT
client = mqtt.Client(client_id=SENSOR_ID)
client.on_connect = on_connect

# Configurar user, password y TLS (para conexion segura con el puerto 8883)
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set() # Habilitar la encriptacion SSL/TLS

# Conectar al Broker
try:
    print(f"[*] Conectando a {BROKER_HOST}...")
    client.connect(BROKER_HOST, BROKER_PORT)
except Exception as e:
    print(f"[-] Error al conectar: {e}")
    exit()  # Salir si no se puede conectar

# Iniciar el loop del cliente en un hilo separado
client.loop_start()

# Loop principal para principar datos
print(f"[*] Iniciando simulación... Presiona CTRL+C para detener.")
while True:
    try:
        # 1. Generar lectura simulada
        temperatura = round(random.uniform(18.0, 25.0), 2)

        # Crear el mensaje (payload) en formato JSON
        payload = {
            "sensor_id": SENSOR_ID,
            "valor": temperatura,
            "unidad": "°C",
            "timestamp": int(time.time())
        }

        # 2. Publicar en el tópico
        client.publish(TOPICO, json.dumps(payload)) 

        print(f"   Publicado en '{TOPICO}': {payload}")

        # 3. Esperar (más de 500ms)
        tiempo_espera = random.uniform(1.0, 5.0) 
        time.sleep(tiempo_espera)

    except KeyboardInterrupt:
        print("\n[*] Simulación detenida.")
        break

# Detener el loop del cliente y desconectar
client.loop_stop()
client.disconnect()
print("[*] Desconectado del broker.")

