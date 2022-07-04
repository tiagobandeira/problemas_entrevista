def e_fibonacci(n):
    a, b = 0, 1
    aux = 0
    boleano = False
    while b <= n:
        aux = a + b
        a = b 
        b = aux
    if a == n:
        boleano = True
    return boleano
try:
    n = int(input("Digite um número inteiro: "))
    if e_fibonacci(n):
        print("%d PERTENCE a Seguência de Fibonacci!" %n)
    else:
        print("%d NÃO PERTENCE a Seguência de Fibonacci!"%n)
except ValueError:
    print("A entrada não é um número inteiro!")
    