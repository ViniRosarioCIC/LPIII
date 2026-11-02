#5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# • A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# • A mensagem "Reprovado", se a média for menor do que sete;
# • A mensagem "Aprovado com Distinção", se a média for igual a dez.

x = float(input("Digite a primeira nota do aluno: "))
y = float(input("Digite a segunda nota do aluno: "))

media = (x+y)/2

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    media = (nota1 + nota2) / 2
    print(f"Média: {media:.1f}")

    if media == 10:
        print("Aprovado com Distinção")
    elif media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
else:
    print("Notas inválidas! Insira valores entre 0 e 10.")
    