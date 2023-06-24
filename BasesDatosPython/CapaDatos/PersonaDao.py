from Conexion import Conexion
from Persona import Persona
from logger_base import log

class PersonaDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _DELETE = 'DELETE FROM persona WHERE id_persona= %s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas
            
    @classmethod
    def insertar(cls, persona: Persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona insertada: {persona}')
                return cursor.rowcount
    
    @classmethod
    def actualizar(cls, persona: Persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Valores actualizados: {persona}')
                return cursor.rowcount
            
    @classmethod
    def eliminar(cls, persona: Persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valor = persona.id_persona
                cursor.execute(cls._DELETE, (valor, ))
                log.debug(f'Se ha eliminado a la persona -> {persona}')
                return cursor.rowcount
            
    
if __name__ == "__main__":
    

    # Insertar persona 
    persona1 = Persona(1, 'Marcos', 'Soriano', 'msoriano@mail.com')
    persona_insertada = PersonaDAO.insertar(persona=persona1)
    log.debug(f'Persona insertada: {persona1}')

    # Seleccionar base de datos
    datos_seleccionados = PersonaDAO.seleccionar()
    for persona in datos_seleccionados:
        log.debug(persona)


    # Actualizar persona
    persona1 = Persona(1, 'Pablo', 'Martinez', 'pmartinez@mail.com')
    persona_actualizada = PersonaDAO.actualizar(persona1)
    log.debug(f'Persona actualizada-> {persona1}')

    # Seleccionar base de datos
    datos_seleccionados = PersonaDAO.seleccionar()
    for persona in datos_seleccionados:
        log.debug(persona)

    # Eliminar persona
    persona_a_eliminar = Persona(id_persona=1)
    persona_eliminada = PersonaDAO.eliminar(persona_a_eliminar)
    log.debug(f'Persona eliminada -> {persona_eliminada}')

    # Seleccionar base de datos
    datos_seleccionados = PersonaDAO.seleccionar()
    for persona in datos_seleccionados:
        log.debug(persona)