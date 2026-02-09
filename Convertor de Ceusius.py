while True:
    try:
        c = int(input("Digite quantos graus Celsius estão agora: "))
        f = (c * 1.8) + 32 ## Celcius para Fahrenheit
        k = c + 273.15 ## Celcius pra Kelvin
        print(f'Em Fahrenheit está {f}')
        print(f'Em Kelvin está {k}')
        break
    except ValueError:
        print("Entrada inválida. Tente novamente.")
