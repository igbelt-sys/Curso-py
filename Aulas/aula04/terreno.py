# problrma terreno
# declaração de variaveis
largura:float
comprimento:float

# entrada de dados
largura  = float(input("\nDigite a largura do seu terreno em metros: "))
comprimento = float(input("\nDigite o comprimento do seu terreno em : "))
valor_metro_quadrado = float(input("\nDigite o valor do metro quadrado do terreno em R$: "))
# processamento de dados
area = largura * comprimento 

preco  = valor_metro_quadrado * area

# saida de dados
print(f"\n a area do terreno é de {area:.2f} e o preço total é de R$ {preco:.2f}\n")

