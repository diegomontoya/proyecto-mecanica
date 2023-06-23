import math

def aceleracion_centripeta():
    radio = float(input("Ingrese el radio de la órbita (m): "))
    velocidad = float(input("Ingrese la velocidad del objeto (m/s): "))
    aceleracion = velocidad**2 / radio
    print("La aceleración centrípeta es:", aceleracion, "m/s^2")

def velocidad_centrifuga():
    radio = float(input("Ingrese el radio de la centrífuga (m): "))
    aceleracion = float(input("Ingrese la aceleración (g): ")) * 9.8
    velocidad = math.sqrt(aceleracion * radio)
    print("La velocidad del objeto es:", velocidad, "m/s")

def revoluciones_minuto():
    radio = float(input("Ingrese el radio de la centrífuga (m): "))
    aceleracion = float(input("Ingrese la aceleración (g): ")) * 9.8
    velocidad = math.sqrt(aceleracion * radio)
    revoluciones = velocidad / (2 * math.pi * radio) * 60
    print("Las revoluciones por minuto requeridas son:", revoluciones, "rpm")

def velocidad_satelite():
    altura = float(input("Ingrese la altura sobre la superficie de la Tierra (km): "))
    tiempo = float(input("Ingrese el tiempo para una revolución (min): "))
    radio = (640 + altura) * 1000
    tiempo_segundos = tiempo * 60
    velocidad = (2 * math.pi * radio) / tiempo_segundos
    print("La velocidad del satélite es:", velocidad, "m/s")

def aceleracion_caida_libre():
    altura = float(input("Ingrese la altura sobre la superficie de la Tierra (km): "))
    tiempo = float(input("Ingrese el tiempo para una revolución (min): "))
    radio = (640 + altura) * 1000
    tiempo_segundos = tiempo * 60
    velocidad = (2 * math.pi * radio) / tiempo_segundos
    aceleracion = velocidad**2 / radio
    print("La aceleración en caída libre en la órbita es:", aceleracion, "m/s^2")

def aceleracion_punto_mayor_altura():
    radio = float(input("Ingrese el radio de la rueda de feria (m): "))
    vueltas = float(input("Ingrese el número de vueltas por minuto: "))
    velocidad = 2 * math.pi * radio * (vueltas / 60)
    aceleracion = velocidad**2 / radio
    print("La aceleración en el punto más alto es:", aceleracion, "m/s^2")

def aceleracion_punto_menor_altura():
    radio = float(input("Ingrese el radio de la rueda de feria (m): "))
    vueltas = float(input("Ingrese el número de vueltas por minuto: "))
    velocidad = 2 * math.pi * radio * (vueltas / 60)
    aceleracion = velocidad**2 / radio
    print("La aceleración en el punto más bajo es:", aceleracion, "m/s^2")

def distancia_revolucion():
    radio = float(input("Ingrese el radio del aspa (m): "))
    revoluciones = float(input("Ingrese el número de revoluciones por minuto: "))
    distancia = 2 * math.pi * radio * (revoluciones / 60)
    print("La distancia que se mueve el punto en una revolución es:", distancia, "m")

def velocidad_punto():
    radio = float(input("Ingrese el radio del aspa (m): "))
    revoluciones = float(input("Ingrese el número de revoluciones por minuto: "))
    velocidad = 2 * math.pi * radio * (revoluciones / 60)
    print("La velocidad del punto es:", velocidad, "m/s")

def aceleracion_punto():
    radio = float(input("Ingrese el radio del aspa (m): "))
    revoluciones = float(input("Ingrese el número de revoluciones por minuto: "))
    velocidad = 2 * math.pi * radio * (revoluciones / 60)
    aceleracion = velocidad**2 / radio
    print("La aceleración del punto es:", aceleracion, "m/s^2")

def radio_curvatura():
    velocidad = float(input("Ingrese la velocidad del tren (km/h): "))
    aceleracion = float(input("Ingrese la aceleración máxima permitida (g): ")) * 9.8
    velocidad_m_s = velocidad * 1000 / 3600
    radio = velocidad_m_s**2 / aceleracion
    print("El radio de curvatura de la vía más pequeña que puede tolerarse es:", radio, "m")

def disminuir_velocidad():
    radio = float(input("Ingrese el radio de la curva (km): ")) * 1000
    velocidad = float(input("Ingrese la velocidad actual del tren (km/h): "))
    velocidad_m_s = velocidad * 1000 / 3600
    nueva_velocidad_m_s = math.sqrt(radio * aceleracion)
    nueva_velocidad_km_h = nueva_velocidad_m_s * 3600 / 1000
    print("El tren deberá disminuir su velocidad a:", nueva_velocidad_km_h, "km/h")

def velocidad_ecuador():
    radio = float(input("Ingrese el radio de la estrella (km): ")) * 1000
    revoluciones = 1
    velocidad = 2 * math.pi * radio * revoluciones
    print("La velocidad en el ecuador de la estrella es:", velocidad, "m/s")

def aceleracion_ecuador():
    radio = float(input("Ingrese el radio de la estrella (km): ")) * 1000
    revoluciones = 1
    velocidad = 2 * math.pi * radio * revoluciones
    aceleracion = velocidad**2 / radio
    print("La aceleración centrípeta en el ecuador de la estrella es:", aceleracion, "m/s^2")

def resolver_problema(numero_problema):
    if numero_problema == 51:
        aceleracion_centripeta()
    elif numero_problema == 52:
        velocidad_centrifuga()
        revoluciones_minuto()
    elif numero_problema == 53:
        velocidad_satelite()
        aceleracion_caida_libre()
    elif numero_problema == 54:
        aceleracion_punto_mayor_altura()
        aceleracion_punto_menor_altura()
    elif numero_problema == 55:
        distancia_revolucion()
        velocidad_punto()
        aceleracion_punto()
    elif numero_problema == 56:
        radio_curvatura()
        disminuir_velocidad()
    elif numero_problema == 57:
        velocidad_ecuador()
        aceleracion_ecuador()
    else:
        print("Número de problema inválido.")

print("Problemas que contiene este programa:")
print("51. Problema del modelo Bohr del átomo de hidrógeno")
print("52. Problema del astronauta en una centrífuga")
print("53. Problema del satélite en órbita")
print("54. Problema de la rueda de feria Ferris")
print("55. Problema del punto en el aspa del abanico")
print("56. Problema del TGV Atlantique")
print("57. Problema de la estrella de neutrones")

numero_problema = int(input("Ingrese el número del problema que desea resolver: "))

resolver_problema(numero_problema)
