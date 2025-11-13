# Trabajo Práctico N°4 ~ Capas de Acceso en Redes Locales, Protocolos y Fundamentos

## Consigna 1
### A) Investigar como se clasifican las redes según su alcance. Mencionar brevemente las características principales de cada una y colocar en cada cuadro de la Figura el acrónimo de red que corresponda.

Clasificación de redes según su alcance
- PAN (Personal Area Network)
    - Alcance: hasta ~1–2 metros, alrededor de una persona.

    - Uso típico: conexión entre dispositivos personales (celular, auriculares BT, smartwatch, mouse, teclado).

    - Tecnologías: Bluetooth, USB, IR, etc.    
- LAN (Local Area Network)

    - Alcance: una habitación, oficina, laboratorio, casa o edificio.

    - Uso típico: conexión de PCs, impresoras, servidores dentro de la misma organización o domicilio.

    - Características: alta velocidad, baja latencia, suele ser de propiedad privada (empresa, hogar).

    - Tecnologías: Ethernet (IEEE 802.3), Wi-Fi (IEEE 802.11) dentro de un mismo ámbito.

- CAN (Campus Area Network) (a veces la engloban como un tipo de LAN grande)

    - Alcance: varios edificios cercanos, por ejemplo un campus universitario o planta industrial.
    - Es básicamente un conjunto de LAN interconectadas dentro de una misma institución en un área geográfica limitada.

- MAN (Metropolitan Area Network)

    - Alcance: una ciudad o área metropolitana.

    - Une muchas LAN (y/o CAN) dentro de una misma región urbana.

    - Suelen ser operadas por proveedores o grandes organizaciones (municipios, universidades grandes, etc.).

- WAN (Wide Area Network)

    - Alcance: países, continentes, o global (ej: Internet).

    - Une redes LAN/MAN a gran distancia usando enlaces de operadores (fibra, microondas, satélite, etc.).

    - Latencias más altas, gestión más compleja, tramos públicos o de proveedores.
### B)¿Qué es una VLAN? ¿Cómo se clasifican?
Una VLAN (Virtual Local Area Network) es una red lógica creada dentro de una red física, que permite separar dispositivos en distintos dominios de broadcast sin necesidad de usar switches físicos separados.

Características principales

- Segmentación lógica: divide una red LAN grande en redes más pequeñas y aisladas.

- Aíslan tráfico: el broadcast de una VLAN no puede pasar a otra VLAN.

- Mejoran seguridad: equipos de áreas distintas no pueden comunicarse directamente si están en VLAN diferentes.

- Usan etiquetas 802.1Q: los switches “marcan” cada frame para saber a qué VLAN pertenece.

- Más flexibilidad: se puede agrupar equipos por función, aunque estén en lugares distintos del edificio.
### C) Investigar y resumir el protocolo IEEE 802.1Q. ¿Cómo se relaciona con las VLAN?
El IEEE 802.1Q es el estándar que define cómo se identifican y transportan múltiples VLAN dentro de una misma red Ethernet. Su función principal es permitir que un enlace físico pueda llevar tráfico de varias VLAN simultáneamente mediante el uso de una etiqueta (tag) que indica a qué VLAN pertenece cada trama, manteniendo todas las VLAN separadas de manera lógica.
### D) En el contexto de los dos ítems anteriores ¿Qué es el Tagging?
El tagging es el proceso mediante el cual un switch agrega una etiqueta (tag) 802.1Q a una trama Ethernet para indicar a qué VLAN pertenece.
Este tag se inserta en la trama cuando debe viajar por un enlace configurado como trunk, donde circula tráfico de múltiples VLAN al mismo tiempo.