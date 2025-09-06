## TRABAJO PRÁCTICO N° 2 ~ Más conceptos fundamentales de capa física y capa de enlace de datos.

## Introducción 

## Desarrollo

### Consigna 1: 
**a ~ Fenómeno físico representado y sus características principales:**

En la siguiente imagen podemos observar como un satélite establece una comunicación con una barco, este tipo de comunicación se denomina enlace satelital y se encarga de transmitir información a través de ondas electromagnéticas. Este fenómeno físico tiene como característica la propagación de ondas electromagnéticas en el espacio, y asociado ello hay otros fenómenos como:

- Atenuación por espacio libre (Free space path loss, FSPL): Es cuando, la potencia recibida disminuye con el cuadrado de la distancia y con la frecuencia.
  
- Dispersión y absorción atmosférica: Esto sucede cuando el vapor de agua, el oxígeno y distintas partículas absorben energía de la onda electromagnética transmitida.
  
- Desvanecimiento (Fading): Son fluctuaciones rápidas en la potencia, amplitud o fase causado por la multitrayectoria o condiciones atmosféricas, es decir ,esto sucede debido a que la señal llega por varios camino (reflexión,refracción,difracción) y las distintas señales generadas interfieren entre sí. También puede ser por la interferencia de nubes, lluvias las cuales pueden atenuar o distorsionar la señal.
  
- Retardo de propagación: Esto es debido a la gran distancia entre el receptor y el emisor(aprox 36.000 km de distancia).

**b ~ Tipos de transmisión más afectados y más resilientes:**

Las transmisiones más afectadas por el desvanecimiento y la atenuación atmosférica son aquellas que operan en frecuencias elevadas, especialmente en banda Ku (aprox. 12~18 GHz) y banda Ka (aprox. 26,5 ~ 40 GHz). En estas bandas, la lluvia, la humedad y las variaciones rápidas de fase o amplitud pueden degradar significativamente la calidad de la señal, provocando pérdidas de varios decibelios y requiriendo márgenes de enlace mayores o técnicas de mitigación como diversidad de frecuencia o modulación adaptativa.

Por el contrario, las transmisiones en frecuencias más bajas, como la banda L (1~2 GHz) y la banda C (4~8 GHz), resultan más resistentes a estos fenómenos, ya que presentan menor atenuación por lluvia y menor sensibilidad a la multitrayectoria. Sin embargo, aunque estas últimas soportan mejor las condiciones adversas, no están exentas del retardo de propagación inherente a la gran distancia de los satélites geoestacionarios, que impacta por igual a todas las bandas.

**c ~ Por qué no se debe encender el celular en un avión y su relación con el fenómeno:**

El uso de teléfonos móviles a bordo de una aeronave puede generar diversos problemas técnicos y de seguridad. En primer lugar, existe el riesgo de interferencia electromagnética, ya que los celulares transmiten en bandas UHF, aproximadamente entre 800 MHz y 2,6 GHz. Estas señales pueden acoplarse a los sistemas de navegación y comunicación del avión, que operan en frecuencias cercanas o en armónicas de estas, afectando potencialmente su correcto funcionamiento.

En segundo lugar, se presenta un problema de gestión de la red celular: a gran altitud, un teléfono puede detectar simultáneamente múltiples estaciones base en tierra, lo que provoca intentos de conexión y traspasos (handover) constantes, generando sobrecarga en la red terrestre y dificultando su operación. Por último, la normativa aeronáutica —establecida por organismos como la FAA, EASA o ANAC— prohíbe el uso de transmisores activos no autorizados durante el vuelo para minimizar cualquier riesgo de interferencia con sistemas críticos.

En cuanto a su relación con el fenómeno anterior, aunque no se trata exactamente del mismo caso que la atenuación por espacio libre o el rain fade, sí está vinculado con la capa física y la propagación de ondas electromagnéticas. En ambos contextos, el objetivo es controlar y gestionar la propagación de señales para evitar degradación o interferencia en sistemas esenciales para la operación segura.


