import serial 
import time 
 
try: 
        ser = serial.Serial('COM4', 9600, timeout=1)
        time.sleep(2)
 
        while True: 
            if ser.in_waiting > 0: 
                line = ser.readline().decode('utf-8').rstrip() 
                try: 
                    sensor_value = int(line) 
                    print(f"Valor del sensor: {sensor_value}") 
 
                    if sensor_value > 500:  # Umbral para encender el LED 
                        ser.write(b'1\n')  # Envía '1' para encender el LED 
                    else: 
                        ser.write(b'0\n')  # Envía '0' para apagar el LED 
                except ValueError: 
                    print(f"Dato recibido no es un entero: {line}") 
            time.sleep(0.1)  # Espera 0.1 segundos 
 
except serial.SerialException as e: 
        print(f"Error de puerto serie: {e}") 
except KeyboardInterrupt: 
        print("Programa terminado por el usuario.") 
finally: 
        if 'ser' in locals() and ser.is_open: 
            ser.close() 
        
#Python linux
# Villafuerte de Lara Erik Gabriel
# Rios Perez Angel Fernando
# Zamittiz Camacho Irving Fernando
# Ezquivel Rodriguez Guillermo
# Rubio Martinez Jesus Rafael
# Sanchez Garcia Jose Arturo
# Badillo Navarro Edgar Santiago
# Hernandez de La Cruz Jean Brandon
