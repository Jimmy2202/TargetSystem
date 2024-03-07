def reverse(palavra):
    tam_palavra = len(palavra)
    nova_palavra = []
    rever_palavra = ""
    
    for i in range(tam_palavra - 1, -1, -1):
        nova_palavra.append(palavra[i])
        
    rever_palavra = ''.join(nova_palavra)
    print(rever_palavra)
    
def main():
    reverse(input("Digite a palavra a ser revertida: "))
    
main()
