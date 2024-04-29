# Cadastro de alunos
# Otávio V. F

ComandoRegistrarAlunos = 1;
ComandoImprimirAlunos = 0;
ComandoSairPrograma = 2;

Alunos = [];

print(f'BEM VINDO\n\n Comando para registrar um aluno novo: {ComandoRegistrarAlunos}\n\n Comando para imprimir os alunos registrados: {ComandoImprimirAlunos}\n\n Comando para sair do programa: {ComandoSairPrograma}\n\n\n\n')

while(True):
    comandoRecebido = int(input("\nComando: "));

    if comandoRecebido == ComandoSairPrograma:
        print("Volte sempre!");
        break;
    elif comandoRecebido == ComandoRegistrarAlunos:
        nomeDoAluno = input("Qual o nome do aluno que você quer registrar?\n");
        Alunos.append(nomeDoAluno);
    
    elif comandoRecebido == ComandoImprimirAlunos:
        for aluno in Alunos:
            print(aluno);
            print("\n------------------------\n")

