# Báscara

print("y = a * x² + b * x + c")

a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))

print("y =", a, "* x² +", b,"* +", c)

delta = b**2 - 4 * a* c

if(delta <0):
    print("A equação não tem raiz real")
else:
    x1 = (-b + (delta**(1/2)))/2*a 
    x2 = (-b - (delta**(1/2)))/2*a