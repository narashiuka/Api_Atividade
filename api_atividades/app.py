
from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from models import Pessoas, Atividades, Usuarios
import json

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

#USUARIOS = {
#            'Gabriel':'123',
#           'Rafael':'321'
#           }

#@auth.verify_password
#def verificacao(login, senha):
#    print('Validando o usuario')
#    print(USUARIOS.get(login) == senha)
#    if not (login, senha):
#        return False
#    return (USUARIOS.get(login) == senha)
    
@auth.verify_password
def verificacao(login, senha):

    if not (login, senha):
        return False
    return (Usuarios.query.filter_by(login=login, senha=senha)).first()

class Pessoa(Resource):
    @auth.login_required
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                        'nome':pessoa.nome,
                        'idade':pessoa.idade,
                        'id':pessoa.id
                       }

        except AttributeError:
            response = {
                        'status':'Erro',
                        'mensagem':'Nao existe o item solicitado'
                       }
        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json

        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']

        pessoa.save()

        response = {
                    'id':pessoa.id,
                    'nome':pessoa.nome,
                    'idade':pessoa.idade
                   }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = f'Pessoa {pessoa.nome} excluida com sucesso'
        pessoa.delete()
        return {'status':'Concluido','mensagem':mensagem}

class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()

        response = {
                    'id':pessoa.id,
                    'nome':pessoa.nome,
                    'idade':pessoa.idade
                   }
        return response


class Listaatividades(Resource):
    def get(self):
        atividad = Atividades.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'pessoa':i.pessoa.nome} for i in atividad]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()

        response = {
                    'id':atividade.id,
                    'pessoa':atividade.pessoa.nome,
                    'nome':atividade.nome
                   }
        return response


api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(Listaatividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)