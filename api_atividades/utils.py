from models import Pessoas


#Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome="Gabriel", idade=23)
    pessoa.save()
    print(pessoa)

#Consulta dados na tabela pessoa
def consulta_pessoas():
    #pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Gabriel').first()
    print(pessoa.idade)

#Altera dados da tabela pessoa
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Gabriel').first()
    pessoa.idade = 29
    pessoa.save()

#Exclui dados da tabela pessoa
def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Gabriel').first()
    pessoa.delete()



if __name__ == '__main__':
    consulta_pessoas()
    #insere_pessoas()
    exclui_pessoas()
    consulta_pessoas()
