import logging as log

# Crear un formatter personalizado para la consola
console_formatter = log.Formatter('%(asctime)s - %(levelname)s: %(message)s', datefmt='%I:%M:%S %p')

# Crear un formatter personalizado para el archivo de log
file_formatter = log.Formatter('%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s', datefmt='%I:%M:%S %p')

# Crear manejador para la consola
console_handler = log.StreamHandler()
console_handler.setFormatter(console_formatter)

# Crear manejador para el archivo de log
file_handler = log.FileHandler('pool_conexiones_python.log')
file_handler.setFormatter(file_formatter)

# Obtener el logger raíz y establecer el nivel
root_logger = log.getLogger()
root_logger.setLevel(log.DEBUG)

# Agregar los manejadores al logger raíz
root_logger.addHandler(console_handler)
root_logger.addHandler(file_handler)
