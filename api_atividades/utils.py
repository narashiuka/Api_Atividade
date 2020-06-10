from models import Pessoas, Usuarios


#Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome="Pablo", idade=15)
    pessoa.save()
    print(pessoa)

#Consulta dados na tabela pessoa
def consulta_pessoas():
    #pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Gabriel').first()
    print(pessoa.nome)

#Altera dados da tabela pessoa
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Gabriel').first()
    pessoa.idade = 29
    pessoa.save()

#Exclui dados da tabela pessoa
def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Gabriel').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    insere_usuario('Gabriel','1234')
    insere_usuario('Rafael','123')
    consulta_todos_usuarios()
    #insere_pessoas()
    #exclui_pessoas()
    #consulta_pessoas()