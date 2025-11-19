import paho.mqtt.client as mqtt
import time
import json
import random

# --- Tus Datos de Conexión ---
BROKER_HOST = "wan-piece-5075909d.a02.usw2.aws.hivemq.cloud"
BROKER_PORT = 8883
USERNAME = "luffy"
PASSWORD = "WanPiece5"

# --- Tópicos ---
# Tópico donde PUBLICAMOS los datos
TOPICO_DATOS = "lan/sala1/sensor/hum"
# Tópico donde ESCUCHAMOS las órdenes
TOPICO_COMANDOS = "lan/broadcast/comandos"

SENSOR_ID = "sensor-hum-sala1"

# Esta variable decide si enviamos datos o no. Empieza en False (apagado).
simulacion_activa = False 

# --- Callbacks ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[+] '{SENSOR_ID}' conectado al broker.")
        # ¡IMPORTANTE! Nos suscribimos para escuchar órdenes del Controlador
        client.subscribe(TOPICO_COMANDOS)
        print(f"[*] Escuchando órdenes en '{TOPICO_COMANDOS}'...")
    else:
        print(f"[-] Fallo al conectar, código de error: {rc}")

def on_message(client, userdata, msg):
    """Esta función se activa cuando llega una orden (START/STOP)"""
    global simulacion_activa
    comando = msg.payload.decode('utf-8')
    
    if comando == "START":
        simulacion_activa = True
        print(f"\n [>>>] ORDEN RECIBIDA: START. Iniciando envíos...")
    elif comando == "STOP":
        simulacion_activa = False
        print(f"\n [>>>] ORDEN RECIBIDA: STOP. Deteniendo envíos...")

# --- Configuración del Cliente ---
client = mqtt.Client(client_id=SENSOR_ID)
client.on_connect = on_connect
client.on_message = on_message  # <--- Vinculamos la función de escucha
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()

try:
    client.connect(BROKER_HOST, BROKER_PORT)
except Exception as e:
    print(f"[-] Error al conectar: {e}")
    exit()

client.loop_start()

print(f"[*] {SENSOR_ID} listo. Esperando orden 'START' para comenzar...")
print("[*] Presiona CTRL+C para salir totalmente.")

try:
    while True:
        # Solo entramos aquí si la bandera es True (recibimos START)
        if simulacion_activa:
            # 1. Generar lectura simulada
            humedad = round(random.uniform(20.0, 30.0), 2)
            
            payload = {
                "sensor_id": SENSOR_ID,
                "valor": humedad,
                "unidad": "%",
                "timestamp": int(time.time())
            }
            
            # 2. Publicar en el tópico de datos
            client.publish(TOPICO_DATOS, json.dumps(payload))
            print(f"   Enviado: {humedad}% a '{TOPICO_DATOS}'")
            
            # 3. Esperar
            time.sleep(2) 
        else:
            # Si está en STOP, esperamos un poco para no quemar el procesador
            time.sleep(1)
            
except KeyboardInterrupt:
    print("\n[*] Programa cerrado.")

client.loop_stop()
client.disconnect()
