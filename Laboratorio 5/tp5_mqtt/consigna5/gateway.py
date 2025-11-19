import paho.mqtt.client as mqtt
import json
import csv              
import os               
from datetime import datetime

# --- Tus Datos de Conexión (TUS DATOS ORIGINALES) ---
BROKER_HOST = "wan-piece-5075909d.a02.usw2.aws.hivemq.cloud"
BROKER_PORT = 8883
USERNAME = "luffy"
PASSWORD = "WanPiece5"

# --- Tópico y Archivo
TOPICO_A_ESCUCHAR = "lan/#"
CLIENT_ID = "Gateway"
NOMBRE_ARCHIVO = "registro_sensores.csv"

def guardar_en_csv(datos, topic):
    # Verificamos si el archivo existe (para saber si poner encabezados o no)
    archivo_existe = os.path.isfile(NOMBRE_ARCHIVO)
    
    with open(NOMBRE_ARCHIVO, mode='a', newline='') as f:
        writer = csv.writer(f)
        
        # Si el archivo es nuevo, escribimos los encabezados primero
        if not archivo_existe:
            writer.writerow(["Fecha", "Sensor ID", "Valor", "Unidad", "Topic"])
        
        # Convertimos el timestamp a fecha legible
        fecha_legible = datetime.fromtimestamp(datos['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
        
        # Escribimos la fila con los datos
        writer.writerow([fecha_legible, datos['sensor_id'], datos['valor'], datos['unidad'], topic])
        print(f"   [DISK] Guardado en CSV: {datos['valor']} {datos['unidad']} ({datos['sensor_id']})")

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
    try:
        payload_str = msg.payload.decode('utf-8')
        
        # Si sabemos que es JSON, lo podemos "cargar"
        datos = json.loads(payload_str)
        
        # --- AQUI ESTA EL CAMBIO: Llamamos a la funcion para guardar ---
        guardar_en_csv(datos, msg.topic)
        # ---------------------------------------------------------------
        
        print(f"   < Recibido: {datos} (en tópico '{msg.topic}')")
        
    except Exception as e:
        # Si no es JSON o falla algo, solo imprimimos el error
        print(f"   [!] Error o dato no JSON recibido: {e}")

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
print(f"[*] {CLIENT_ID} (Subscriber) iniciado. Presiona CTRL+C para detener.")
client.loop_forever()