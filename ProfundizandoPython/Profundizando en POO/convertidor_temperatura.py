class Convertidor_Temperatura:

    MAX_CELSIUS = 100
    MAX_FAHRENHEIT = 213

    @classmethod
    def celsius_fahrenheit(cls, celsius):
        if celsius > cls.MAX_CELSIUS:
            raise ValueError('Temperatura demasiado alta')
        return celsius * 9/5 +32
    
    @classmethod
    def f_c(cls, fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError('Temperatura demasiado alta')
        return (fahrenheit-32) * 5/9
    

if __name__ == '__main__':
    resultado = Convertidor_Temperatura.celsius_fahrenheit(15)
    print(resultado)
    resultado = Convertidor_Temperatura.f_c(10)
    print(resultado)