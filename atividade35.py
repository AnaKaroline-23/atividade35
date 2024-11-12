#Ler uma lista de 10 número reais e mostre-os na ordem inversa
numeros = []
for i in range (10):
    numero = float(input(f"Digite o número {i+1}:"))
    numeros.append(numero)
print("Números na ordem inversa:")
for numero in reversed (numeros):
        print (numero)