'''
4 - Crie um programa que simule a validação de uma senha de acesso.
Defina uma senha correta e salve em uma variável, depois peça para o usuário 
digitar a senha, enquanto a senha digitada estiver incorreta, exiba a 
mensagem "Senha incorreta! Tente novamente." e peça a senha novamente.
Quando o usuário acertar, exiba "Acesso liberado!".
'''

senha_correta = "67428922"
senha_digitada = input("Digite a senha de acesso: ")
while senha_digitada != senha_correta:
    print("Senha incorreta! Tente novamente.")
    senha_digitada = input("Digite a senha de acesso: ")

print("Acesso Liberado!")
