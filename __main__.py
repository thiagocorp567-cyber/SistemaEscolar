from pessoas import *
from rich import inspect
from rich import print

#criar um painel de exibição para o aluno e para o professor
#ao rodar o codigo, havera opcao 1 professor e opcao 2 aluno, ai o codigo vai mostrar metodo da respectiva escolha

def main():
    Antonio = Professor('Antonio', 'Matematica')
    Felipe = Professor('Felipe', 'Historia')
    Joao = Aluno('Joao', 'matematica')
    Andre = Aluno('Andre', 'Portugues')
    Jose = Aluno('Jose', 'Ciencias')
    Paulo = Aluno('Paulo', 'Filosofia')
    Sofia = Aluno('Sofia', 'matematica')
    Maria = Aluno('Maria', 'fisica')
    Pessoas.mostrar_alunos()

if __name__ == '__main__':
    main()
