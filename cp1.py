# RM: 98943 Nome: Gustvao Fernandes Gonzalez Magalhaes

# codigo cp1, para fazer uma compra
# numa vinheria

print("Seja bem vindo ao site!!!")

nome = input("Nome completo: ")
idade = int(input("Sua idade: "))
endereço_do_cliente = input("endereço: ")
endereço_de_entrega = input("endereço de entrega: ")

if endereço_do_cliente  != endereço_de_entrega:
    z  = int(input("O endereço de entrega difere do endereço do cliente, caso esteja correto digite 1: "))
    if z == 1:
        print("OK!")
    else:
        print("corrija o endereço!!!")

# 2 se a compra estiver sendo feita por um menor de idade
while True:
    if idade < 18:
        print("A compra so pode ser realizada por um cliente maior de idade")
    break
if idade >= 18:  
    
    a = print("[vinhos: \n] 1 para vinho1(R$50) \n 2 para vinho2(R$70) \n 3 para vinho3(R$25) \n 4 para vinho4(R$80) \n 5 para vinho5(R$110)")
    carrinho = 0
    vinho1 = 50
    vinho2 = 70
    vinho3 = 25
    vinho4 = 80
    vinho5 = 110
    estoque = 350
    x = 1

    while x < estoque:
        vinhos = int(input("digite o(s) numero(s) do(s) vinho(s) que você deseja comprar e 0 para finalizar a compra \n"))

        if vinhos == 0:
            break
   
        
        else:
            if vinhos == 1:
                carrinho = carrinho + vinho1
                
            elif vinhos == 2:        
                carrinho = carrinho + vinho2
            
            elif vinhos == 3:        
                carrinho = carrinho + vinho3
            
            elif vinhos == 4:        
                carrinho = carrinho + vinho4
                
            elif vinhos == 5:        
                carrinho = carrinho + vinho5
                
            x += 1
            
        if vinhos > 5:
            print("digite apenas um dos numeors pedidos")
            
    if carrinho <= 100:
            print("o valor minimo para realizar a compra é de r$100")
            
    elif carrinho >= 200:
            print("O seu frete nao sera combrado")
            
    else:
            carrinho = carrinho + 15
            print("o valor do seu frete sera de R$15")
    
    print("para que possamos finalizar sua compra porfavor complete com as informaçoes abaixo:")

    cpf = str(input("Seu CPF: "))
    cep = str(input("o CEP do local de entrega: "))

    print("foram comprados %d produtos" % x)
    print("o valor final da sua compra sera de R$%d"% carrinho)
    print("seu(s) produto(s) serao entregues no(a) "+ endereço_de_entrega)

    a = int(input("Para finalizar a compra digite 1: "))
    
    if a == 1:
        print("obrigado pela compra")
        
    else:
        print("Compra cancelada")
        

   
            


























