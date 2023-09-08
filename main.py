import math

def resolver_equacao_segundo_grau(a, b, c):
    # Calcula o discriminante
    discriminante = b**2 - 4*a*c
    
    # Verifica o valor do discriminante para determinar o número de raízes reais
    if discriminante > 0:
        # Duas raízes reais distintas
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return (x1, x2)
    elif discriminante == 0:
        # Uma raiz real (raiz dupla)
        x = -b / (2*a)
        return (x,)
    else:
        # Não há raízes reais
        return ()

def main():
    # Solicita os coeficientes do usuário
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))

    raizes = resolver_equacao_segundo_grau(a, b, c)

    if len(raizes) == 0:
        print("A equação não possui raízes reais.")
    elif len(raizes) == 1:
        print(f"A equação possui uma raiz real: x = {raizes[0]}")
    else:
        print(f"A equação possui duas raízes reais: x1 = {raizes[0]}, x2 = {raizes[1]}")

if __name__ == "__main__":
    main()