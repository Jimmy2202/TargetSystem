def fib(numero):
    fibonacci = [0,1]
    x,y = 0,1 #defino os dois últimos termos da sequência. Como a sequência está no começo, coincidentemente eles são também os dois primeiros
    
    while (numero > x+y): #enquanto o número do usuário for maior que a soma dos últimos dois termos da sequencia, eu vou continuar gerando. Quando for menor ou igual, eu paro de gerar.
        x = fibonacci[-2]
        y = fibonacci[-1]
        fibonacci.append(x+y)
        
    if(numero == x+y): #Depois de parar de gerar, eu verifico se o último termo da sequencia é igual ao numero do usuário, se sim, o numero dele pertence a sequencia, senão, não pertence
        return 1
    else:
        return 0
        
def main():
    numero = int(input("Digite o número: "))
    if fib(numero):
        print("PERTENCE")
    else:
        print("NÃO PERTENCE")
    
main()
