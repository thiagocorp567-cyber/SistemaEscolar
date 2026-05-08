class Pessoas():
    lista_alunos = [] #nessa lista será amarzenada cada aluno e suas informações, ela será organizada em ordem alfabetica, essa é a lista geral
    lista_alunos_materia = [] #essa será a lista por materia
    def __init__(self, nome, materia):
        self.nome = nome
        self.materia = materia
#self.emails_aluno =  {curso, nome, email}

    @classmethod
    def mostrar_alunos(cls):
        print(Pessoas.lista_alunos) #substituir por def do manipular_arquivo

    @classmethod
    def escrever_aluno(cls):
        pass #aqui 

    @classmethod
    def lancar_notas(cls):
        pass

class Professor(Pessoas):
    def __init__(self, nome, materia):
        super().__init__(nome, materia)
        self.alunos = []
    #o professor tera acesso ao self.email_aluno, para verificar seus alunos e lancar nota
    #fazer uma lista com alunos da materia *dele* com nome e email
    #fazer metodo para mostrar listan e lancar notas

 

    def lancar_nota(self, notas):
        pass

    def __str__(self):
        return f'Sou o {self.nome}, professor de {self.materia} sua matricula é {self.email}'

class Aluno(Pessoas):
    contador = 0
    def __init__(self, nome, materia):
        super().__init__(nome, materia)
        Aluno.contador += 1 
        self.matricula = Aluno.contador #matricula é para fazer o email, pode servir como id também 
        self.email = self.nome + str(self.matricula) + '@aluno.sp.com'
        self.materia = materia.title()
        self.notas = list()
        self.individuo = dict(nome = self.nome, curso = self.materia, email = self.email)
        Pessoas.lista_alunos.append(self.individuo)

#    def mostrar_alunos(self):
#        return super().mostrar_alunos()

    def __str__(self):
        return f'Sou o aluno {self.nome}, do curso {self.materia}, minhas notas são {self.notas}'
