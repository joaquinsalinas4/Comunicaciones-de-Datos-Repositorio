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
TOPICO_DATOS = "lan/sala1/sensor/temp"
# Tópico donde ESCUCHAMOS las órdenes
TOPICO_COMANDOS = "lan/broadcast/comandos"

SENSOR_ID = "sensor-temp-sala1"

# --- Bandera de Control ---
# Empieza en False (apagado) hasta recibir orden
simulacion_activa = False 

# --- Callbacks ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[+] '{SENSOR_ID}' conectado al broker.")
        # ¡IMPORTANTE! Nos suscribimos para escuchar órdenes
        client.subscribe(TOPICO_COMANDOS)
        print(f"[*] Escuchando órdenes en '{TOPICO_COMANDOS}'...")
    else:
        print(f"[-] Fallo al conectar, código de error: {rc}")

def on_message(client, userdata, msg):
    """Recibe las órdenes del controlador"""
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
client.on_message = on_message # <--- Vinculamos la función de escucha
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()

try:
    client.connect(BROKER_HOST, BROKER_PORT)
except Exception as e:
    print(f"[-] Error al conectar: {e}")
    exit()

client.loop_start()

print(f"[*] {SENSOR_ID} listo. Esperando orden 'START'...")
print("[*] Presiona CTRL+C para salir.")

# --- Bucle Principal ---
try:
    while True:
        # Solo publicamos si la bandera es True
        if simulacion_activa:
            # 1. Generar lectura simulada
            valor = round(random.uniform(20.0, 30.0), 2)
            
            payload = {
                "sensor_id": SENSOR_ID,
                "valor": valor,
                "unidad": "°C",
                "timestamp": int(time.time())
            }
            
            # 2. Publicar en el tópico
            client.publish(TOPICO_DATOS, json.dumps(payload))
            print(f"   Enviado: {valor}°C a '{TOPICO_DATOS}'")
            
            # 3. Esperar (1 segundo)
            time.sleep(1) 
        else:
            # Si está apagado, esperamos sin consumir recursos
            time.sleep(1)
            
except KeyboardInterrupt:
    print("\n[*] Simulación detenida.")

client.loop_stop()
client.disconnect()
