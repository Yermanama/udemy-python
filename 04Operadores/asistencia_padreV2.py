dia_libre: bool = True
es_vacaciones: bool = False

if not (dia_libre or es_vacaciones):
    print('El padre NO va a poder asistir a la función de su hijo, que pena.')
else:
    print('El padre va a poder asistir a la función de su hijo.')
