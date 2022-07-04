string = input("Digite um texto: ")
lista, string = [string[len(string)-i-1] for i in range(len(string))], ""
for i in lista:
    string += i
print(string)