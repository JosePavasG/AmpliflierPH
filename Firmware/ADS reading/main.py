from machine import I2C, Pin
import ads1x15
import time

addr = 0x48
gain = 1
i2c = I2C(0, pins=('P9', 'P10'), baudrate=400000)
ads = ads1x15.ADS1115(i2c, addr, gain)

ledGreen = Pin('P22', mode=Pin.OUT)
ledRed = Pin('P23', mode=Pin.OUT)
    
while True:
    ledRed.value(0)
    # Leer y mostrar los valores de los canales individuales
    for canal in range(1): # Numero de canales
        valor = ads.read(rate=4, channel1=canal)  # Leer el canal
        print("Valor del canal {}: {}".format(canal, valor))
        
    ledGreen.value(1)
    time.sleep(0.5)  # Espera medio segundo
    ledGreen.value(0)# Apagar el LED
    
    time.sleep(.2)
'''
Si obtienes lecturas elevadas en los canales del ADS1115 cuando no hay nada conectado
(es decir, los pines de entrada están "flotando"), es un comportamiento normal en muchos ADCs.
Cuando un pin de entrada de un ADC no está conectado a nada, se considera un "pin flotante".
Un pin flotante puede recoger ruido eléctrico del ambiente o de otros componentes del circuito,
lo que resulta en lecturas aparentemente aleatorias y altas.

Aquí hay algunas formas de abordar este comportamiento:

Conectar a Tierra (GND) para Lecturas Inactivas:
Si no estás usando un canal, es una buena práctica conectarlo a tierra (GND).
Esto dará una lectura estable y cercana a 0.

Usar Resistencias Pull-Down:
Puedes conectar una resistencia pull-down (por ejemplo, 10kΩ) entre cada entrada del ADC y tierra.
Esto asegura que, en ausencia de una señal, la entrada se mantenga a un nivel bajo.

Software de Filtrado:
Si no puedes modificar el hardware, podrías implementar un filtro en el software que ignore las lecturas que no tienen sentido para tu aplicación.
Por ejemplo, si sabes que tus señales válidas siempre estarán por debajo de cierto umbral,
puedes configurar tu software para tratar cualquier lectura por encima de ese umbral como un valor de "no lectura".

Verificar el Diseño del Circuito: Asegúrate de que tu circuito esté diseñado correctamente, con todas las conexiones de tierra y alimentación adecuadamente implementadas, y que no haya rutas para que el ruido eléctrico entre en el sistema.

Lecturas por Defecto en Canales No Utilizados:
Si hay canales que no planeas utilizar, considera mantenerlos conectados a un nivel de voltaje conocido (como GND)
para evitar lecturas aleatorias.
'''
'''
Importación de Librerías:
from machine import I2C: Importa la clase I2C del módulo machine. Esta clase se utiliza para la comunicación I2C con el ADS1115.

import ads1x15: Importa la librería ads1x15, que proporciona funcionalidades específicas para interactuar con el módulo ADC ADS1115.

import time: Importa el módulo time, que se utiliza para crear retrasos en la ejecución del programa.

Configuración Inicial:
addr = 72: Define la dirección I2C del módulo ADS1115. La dirección 72 en decimal corresponde a 0x48 en hexadecimal.

gain = 1: Establece la ganancia del amplificador del ADS1115. La ganancia determina el rango de voltaje que el ADC puede medir.

i2c = I2C(0, pins=('P9', 'P10'), baudrate=400000): Inicializa el bus I2C en el microcontrolador. pins=('P9', 'P10') define los pines
utilizados para SDA y SCL,respectivamente, y baudrate=400000 establece la velocidad de la comunicación I2C.

ads = ads1x15.ADS1115(i2c, addr, gain): Crea una instancia de ADS1115, pasando el objeto I2C, la dirección del ADS1115 y la ganancia.

Bucle Principal:
while True:: Un bucle infinito que hace que el código se ejecute continuamente.

Dentro del bucle, se itera sobre cada uno de los 4 canales del ADS1115 (for canal in range(4):).

valor = ads.read(rate=4, channel1=canal): Lee el valor del canal especificado del ADS1115.
El parámetro rate=4 podría estar relacionado con la tasa de muestreo del ADC,
aunque esto dependerá de la implementación específica de la librería ads1x15.

print("Valor del canal {}: {}".format(canal, valor)): Imprime el valor leído de cada canal.

time.sleep(5): Crea una pausa de 5 segundos antes de la próxima iteración del bucle. Esto reduce la frecuencia de las lecturas y la salida impresa.
'''
