# DECLARAR AS VARIÁVEIS
nome_do_aluno = ""
nota_bimestre_1 = 0.0
nota_bimestre_2 = 0.0
nota_bimestre_3 = 0.0
nota_bimestre_4 = 0.0
media_final = 0.0

print("**********************************")
print("*         MÉDIA FINAL            *")
print("**********************************")
print()

# ENTRADA DOS DADOS
nome_do_aluno = input("Qual o nome do aluno? ")
nota_bimestre_1 = float(input("Nota 1: "))
nota_bimestre_2 = float(input("Nota 2: "))
nota_bimestre_3 = float(input("Nota 3: "))
nota_bimestre_4 = float(input("Nota 4: "))

# CALCULAR A NOTA FINAL
media_final = (nota_bimestre_1 + nota_bimestre_2 + nota_bimestre_3 + nota_bimestre_4) / 4

# VERIFICA A SITUAÇÃO DO ALUNO
situacao = ""

if media_final >= 7.0:
    situacao = "APROVADO"
elif media_final < 5:
    situacao = "REPROVADO"
else:
    situacao = "EM RECUPERAÇÃO"

# EXIBIR O RESULTADO
print("------------------------------")
print(f"{nome_do_aluno}, você está {situacao}, com média {media_final}.")
print("------------------------------")
