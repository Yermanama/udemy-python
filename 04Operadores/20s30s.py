edad_input: int = int(input("Por favor, introduce tu edad: \n"))
edad_superior_20 = 30
edad_inferior = 20
edad_superior_30 = 40

if edad_inferior >= edad_input > edad_superior_20:
    print('Esta persona está en sus 20s.')
else:
    if edad_superior_20 >= edad_input > edad_superior_30:
        print('La persona está en sus 30s.')
    else:
        if edad_input >= edad_superior_30:
            print('Tiene 40 o más.')
        else:
            print('Tiene menos de 20 años.')
