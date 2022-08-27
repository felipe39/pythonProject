#Média de um aluno

matéria1 = int(input('Introduza a primeira nota do aluno: '))
matéria2 = int(input('Introduza a segunda nota do  aluno: '))
matéria3 = int(input('Introduza a terceira nota do aluno: '))

média = (matéria1 + matéria2 + matéria3) / 3

if média > 7:
    print('Aluno Aprovado!')
else:
    print('Aluno Reprovado')