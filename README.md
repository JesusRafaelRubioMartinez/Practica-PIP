import serial 
import time 
 
try: 
        ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
        time.sleep(2)
 
        while True: 
            if ser.in_waiting > 0: 
                line = ser.readline().decode('utf-8').rstrip() 
                try: 
                    sensor_value = int(line) 
                    print(f"Valor del sensor: {sensor_value}") 
 
                    if sensor_value < 500:  # Umbral para encender el LED 
                        ser.write(b'2\n')  # Envía '1' para encender el LED 
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

#include <stdio.h> 
    #include <stdlib.h> 
    #include <string.h> 
    #include <unistd.h> 
    #include <fcntl.h> 
    #include <termios.h> 
 
    int main() { 
      int serial_port = open("/dev/ttyUSB0", O_RDWR); // Abre el puerto serie 
      if (serial_port < 0) { 
        perror("Error al abrir el puerto serie"); 
        return 1; 
      } 
 
      struct termios tty; 
      memset(&tty, 0, sizeof(tty)); 
      if (tcgetattr(serial_port, &tty) != 0) { 
        perror("Error al obtener atributos del puerto serie"); 
        return 1; 
      } 
 
      tty.c_cflag = CS8 | CREAD | CLOCAL; // Configura el puerto serie 
      tty.c_cc[VMIN] = 1; // Lee al menos 1 carÃ¡cter 
      tty.c_cc[VTIME] = 5; // Espera hasta 0.5 segundos para la entrada 
 
      if (tcsetattr(serial_port, TCSANOW, &tty) != 0) { 
        perror("Error al establecer atributos del puerto serie"); 
        return 1; 
      } 
 
      char buffer[256]; 
      int bytes_read; 
      int sensorValue; 
 
      while (1) { 
        bytes_read = read(serial_port, buffer, sizeof(buffer)); 
        if (bytes_read > 0) { 
          buffer[bytes_read] = '\0'; // Termina la cadena 
          sensorValue = atoi(buffer); // Convierte la cadena a entero 
          printf("Valor del sensor: %d\n", sensorValue); 
 
          if (sensorValue > 500) { // Umbral para encender el LED 
            write(serial_port, "1\n", 2); // EnvÃ­a "1" para encender el LED 
          } else { 
            write(serial_port, "0\n", 2); // EnvÃ­a "0" para apagar el LED 
} 
} 
usleep(100000); // Espera 0.1 segundos 
} 
close(serial_port); 
return 0; 
}

//irving fernando zamittiz camacho
//jesus rafael rubio martinez
//villafuerte de lara erik gabriel
//jean brandon hernandez de la cruz
//edgar santiago badillo navarro
//guillermo esquivel rodriguez
//jose arturo sanchez garcia
//rios perez angel fernando
//codigo en C


