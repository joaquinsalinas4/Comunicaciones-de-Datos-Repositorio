import paho.mqtt.client as mqtt
import time

# --- Tus Datos de Conexión (Los mismos que el sensor) ---
BROKER_HOST = "wan-piece-5075909d.a02.usw2.aws.hivemq.cloud"
BROKER_PORT = 8883
USERNAME = "luffy"
PASSWORD = "WanPiece5"

# --- Tópico de Comandos ---
# A este tópico enviaremos las órdenes "START" y "STOP"
TOPICO_COMANDOS = "lan/broadcast/comandos"

CLIENT_ID = "Controlador_Central"

# --- Callbacks (Igual que tu sensor) ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[+] '{CLIENT_ID}' conectado al broker.")
    else:
        print(f"[-] Fallo al conectar, código de error: {rc}")

# --- Configuración del Cliente (Sintaxis idéntica a tu código) ---
# Usamos client_id explicito como en tu ejemplo
client = mqtt.Client(client_id=CLIENT_ID) 

client.on_connect = on_connect
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()

# --- Conexión ---
try:
    client.connect(BROKER_HOST, BROKER_PORT)
except Exception as e:
    print(f"[-] Error al conectar: {e}")
    exit()

# Iniciamos el bucle en segundo plano
client.loop_start()

# --- Menú de Control ---
print("\n" + "="*40)
print(f"[*] {CLIENT_ID} listo.")
print("Este script controla a TODOS los sensores.")
print("="*40)

try:
    while True:
        print("\nOpciones:")
        print("1. Iniciar Simulación (Enviar 'START')")
        print("2. Detener Simulación (Enviar 'STOP')")
        print("3. Salir")
        
        opcion = input(">>> Elige una opción: ")

        if opcion == "1":
            print(f"[>] Enviando orden 'START' a '{TOPICO_COMANDOS}'...")
            client.publish(TOPICO_COMANDOS, "START")
            
        elif opcion == "2":
            print(f"[>] Enviando orden 'STOP' a '{TOPICO_COMANDOS}'...")
            client.publish(TOPICO_COMANDOS, "STOP")
            
        elif opcion == "3":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Intenta con 1 o 2.")
            
        # Pequeña pausa para evitar rebotes
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\n[*] Controlador cerrado.")

client.loop_stop()
client.disconnect()