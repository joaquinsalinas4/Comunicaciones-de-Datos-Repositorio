# Trabajo Práctico N°5  ~ Simulación de una Red Local utilizando MQTT

## Consigna 1

### Resumir brevemente las características del protocolo MQTT. Incluir ventajas, desventajas y principales usos. Responder: ¿Qué es el patrón de diseño PubSub?

Para hablar del protocolo MQTT, primero hay que definir el **patrón** de diseño PubSUb.

### **Patrón** de diseño PubSub

El **patrón** PubSub es un modelo de **comunicación**, donde los que **envían** mensajes (publishers) no se comunican directamente con los que los reciben (suscribers), sino que se hace a **través** de un intermediario central llamado Broker. Los publishers publican mensajes en **Tópicos** (**categorías**), y el broker **reenvía** esos mensajes a todos los Suscribers que se hayan suscrito a esos **tópicos**.

La principal ventaja que provee este **patrón** de diseño es el desacoplamiento de los componentes. Los publishers y suscribers no se conocen. No necesitan saber su **dirección** IP. Estos pueden estar en redes diferentes. **Además**, no necesitan estar conectados al mismo tiempo (el Broker puede guardar el mensaje si el suscriptor **está** offline, dependiendo de la **configuración**);

### ¿Qué es MQTT?

MQTT (Message Queuing **Telemetry** Transport) es un protocolo de **mensajería** (un conjunto de reglas) que usa el **patrón** Pub/Sub. Su **característica** principal es que es extremadamente ligero y eficiente. Fue **diseñado** para usar la menor **cantidad** de datos (ancho de banda) posible.

### Ventajas:

- Es muy liviano (perfecto para redes lentas o inestables, como redes **móviles** o **satelitales**)

- Bajo consumo de **batería** (ideal para dispositivos IoT)

- Maneja niveles de calidad de servicio (QoS) para asegurar que un mensaje llegue (al menos una vez, como **máximo** una vez, o exactamente una vez)

- Es desacoplado y escalable (**fácil** añadir **más** sensores o apps)

### Desventajas:

- Depende 100% del Broker. Si el Broker se cae, todo el sistema de **comunicación** se detiene (es un "**punto** **único** de fallo").

- **Está** pensado para mensajes cortos y datos pequeños (**telemetría**), no para enviar archivos grandes o hacer streaming de video.

### Usos principales

- Internet of Things (IoT): Es el **estándar** de la industria. Sensores en el campo, luces inteligentes para el hogar, medidores de agua, GPS de **vehículos**, etc.

- Notificaciones push: Muchas apps **móviles** lo usan para enviar notificaciones.

- Apps de chat: Facebook Messenger lo **usó** durante mucho tiempo.

## Consigna 2

### Instalar/desplegar y ejecutar un broker MQTT.

Para eso, tenemos que ir a la pagina web https://console.hivemq.cloud/. Nos registramos, solicitamos el pack starter, el cual es gratuito, y abrimos nuestro primer Cluster:

Se puede apreciar la URL del host del broker y el puerto de conexión (TLS) asignado.

![](consigna2/cluster-info.jpeg)

Con los siguientes parametros de red (colocados por defecto):

![](consigna2/info.png)

Finalmente, para la autenticación, se crea el usuario 'luffy', con su respectiva contraseña dentro de la gestión de acceso del cluster:

![](consigna2/user.jpg)


## Consigna 3

### Verificar que el broker funciona, suscribiendote con un cliente

Para llevar a cabo este paso, tenemos que dirigirnos hacia la Web Client, dentro de HiveMQ Cloud.

![](consigna3/apartado.jpeg)

Luego, se procede a conectarse al cluster en la nube con las credenciales que generamos anteriormente. username: luffy, password: WanPiece5

![](consigna3/web-server-conf.jpeg)

Ahora, se realiza la simulacion, tanto del suscriber como el publisher. Dentro de HiveQM Cloud, se tiene integrado un cliente Web, el cual utilizaremos para suscribirnos. Por el otro lado, tenemos una simulacion en Python de un publisher, el cual envia los datos hacia el Broker. El cliente web, al estar escuchando el mismo topico que el publisher, debe recibir los datos enviados desde el publisher de Python.
El codigo de Python se adjunta en el directorio "tp5_mqtt" con el nombre de "prueba.py"

En el publisher, se configura la conexion hacia el Broker, con los datos de conexion, como la URL del broker, el puerto 8883, las credenciales para el acceso. Luego, se configuran los datos para la recepcion, como el topico, el cual se debe especificar para que los clientes se suscriban a ese tema en especifico. En este caso, se eligio "sensores/prueba" como topico. Por ultimo, el mensaje a enviar por parte del publisher es "Hola, broker! Este es un mensaje de prueba."

**Recepcion del cliente web en el Broker**

![](consigna3/recepcion-broker.jpeg)

## Consigna 4

### Una vez que tenemos nuestra arquitectura funcionando:

### a) Simular una comunicación directa entre dos nodos de una red local. Para ello crear dos clientes: Dispositivo A, que publica en lan/deviceA/status, Dispositivo B se suscribe a ese tópico y muestra los mensajes recibidos. Capturar y documentar resultados.

Para realizar la simulacion, se crean ambos nodos publisher y suscriber en python, en los archivos publisher_deviceA.py y suscriber_deviceB.py respectivamente, dentro del directorio "tp5_mqtt". Ambos deben utilizar las credenciales utilizadas en las consignas anteriores (username = luffy, password = WanPiece5), para poder acceder al Broker. 
El suscriber se suscribe al topico "lan/deviceA/status" y se queda escuchando, esperando mensajes, mientras que el publisher publica en el mismo topico. 

Los datos para la conexion y el topico se muestran a continuacion. Son los mismos para ambos, excepto por el CLIENT_ID, que para el caso del publisher es "Dispositivo-A", mientras que para el suscriber es "Dispositivo-B".

![](consigna4/datos-c4.jpeg)


Se muestra a continuacion el bucle del publisher, el cual, cada 3 segundos, publica un mensaje con informacion de status y timestamp cada 3 segundos, hacia el topico correspondiente. Esto se hace con la instruccion "client.publish(TOPICO, msg)"

![](consigna4/publisher-loop.jpeg)

Luego, el bucle para el suscriber, para recibir los mensajes:

![](consigna4/suscriber-loop.jpeg)

Como resultado, se muestran las salidas de ambos programas, contenidos en dos terminales para cada uno:

![](consigna4/prueba-pubsub.jpeg)


### b) Crear un tópico general lan/broadcast/#. Configurar al menos dos clientes para suscribirse a lan/broadcast/#. Desde un cliente “central”, publicar mensajes en lan/broadcast/all. Capturar y documentar resultados. Con esto simularemos broadcasting en esta pequeña LAN.

Siguiendo la consigna, ahora se crean 3 clases .py para simular dos clientes suscribers y un publisher central, el cual envia un mensaje hacia todos los suscribers que escuchan en broadcast, ya que utilizan el comodin "#" para recibir todo lo que es publicado en lan/broadcast/. Mientras tanto, el publisher, simulando un broadcast en una red LAN chica, publica mensajes en lan/broadcast/all.

Configuracion de los suscribers: Ambos suscribers deben configurar su topico como "lan/broadcast/#"


![](consigna4/suscriber-b.jpeg)

Configuracion del cliente central: El cliente central debe settear su topico como "lan/broadcast/all"

![](consigna4/cliente-central-b.jpeg)


En las imagenes se pueden apreciar, en las dos terminales de la izquierda, los dos clientes. Mientras que en la terminal derecha se muestra el cliente central, el cual publica en broadcast hacia todos los clientes.

![](consigna4/consigna-4b.jpeg)

## Consigna 5

..

## Consigna 5. Preguntas

### a) ¿Sobre qué protocolos de capa de transporte están trabajando en esta actividad?

En este trabajo, se estuvo trabajando sobre el protocolo TCP de la capa de transporte. MQTT se diseñó para ejecutar este protocolo, debido a que se necesita una conexión ordenada, sin perdidas, y orientada a la conexión. Estas son las características principales que posee TCP frente a UDP. En el caso del programa en Python, cuando definimos el puerto 8883, estamos usando TCP seguro (con TLS/SSL). Si usáramos el puerto 1883 (estándar) seria TCP plano. En ambos casos, el protocolo de la capa de transporte es TCP.

### b) ¿Qué pueden decir sobre la garantía de Integridad, Confidencialidad y Disponibilidad en esta arquitectura?

Cuando hablamos de la garantía de Integridad, Confidencialidad y Disponibilidad, estamos hablando de la triada "CIA" de seguridad informática.

- Confidencialidad: Al utilizar el puerto 8883 y el comando client.tls_set(), se habilita la encriptación TLS/SSL. Esto significa que los datos viajan cifrados entre los sensores (publishers) y el Broker. Este desencripta el mensaje, para saber el tópico hacia donde debe enviar el mensaje, lo vuelve a cifrar, y lo envía hacia los suscribers del tópico. Si alguien captura el paquete en el camino (sniffing), no va a poder leer el contenido (el archivo JSON).
Por lo tanto, se puede afirmar que se puede garantizar confidencialidad.

- Integridad: Debido a que se utiliza el protocolo TCP, se garantiza por defecto que los paquetes lleguen ordenados y sin errores (checksums). Además, TLS añade mecanismos de hash para asegurar que el mensaje no fue modificado en el tránsito. Por ende, la integridad es lograda.

- Disponibilidad: Este es el punto débil. Al depender de un servicio en la nube gratuito como HiveMQ Cloud, y de mi conexión a internet, la disponibilidad no esta garantizada al 100%. Si por ejemplo, se caen los servidores de HiveMQ (AWS), mi sistema de sensores dejará de funcionar.

### c) ¿Qué rol juegan los niveles de QoS en la fiabilidad de los mensajes?

Los niveles de QoS (calidad de servicio) determinan la garantía de la entrega del mensaje entre el cliente y el Broker. Juegan un rol fundamental para balancear la fiabilidad contra el consumo de recursos. En MQTT existen tres niveles:

- QoS 0 (At most once): "Disparar y olvidar". Es rápido pero si el mensaje se pierde, no se reenvía.

- QoS 1 (At least once): Se garantiza que el mensaje llega, pero podría llegar duplicado. Requiere confirmación (ACK).

- QoS 2 (Exactly once): Se garantiza que llega exactamente una vez. Es el más seguro pero el más lento (mayor overhead).

Por lo tanto, se puede afirmar que los QoS permiten balancear entre velocidad/bajo consumo (QoS 0) y fiabilidad crítica (QoS 2).

### d) ¿Qué ventajas ofrece el modelo pub/sub frente al modelo cliente-servidor?

La principal ventaja que ofrece el modelo pub/sub frente al modelo cliente-servidor es el desacoplamiento, tanto espacial como temporal.

- Espacial: Ni el publisher (sensor) ni el suscriber (App) necesitan conocer la IP del otro, solo necesitan conocer al Broker. 

- Temporal: No necesitan estar configurados al mismo tiempo (si se configura la persistencia).

- Escalabilidad: Es mucho mas fácil agregar 20 nuevos sensores y que se sumen 50 nuevos suscriptores sin tocar la configuración de los dispositivos existentes. En un modelo cliente-servidor tradicional (petición-respuesta), el servidor podría saturarse atendiendo a cada cliente individualmente.