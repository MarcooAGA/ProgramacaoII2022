from config import *
from cripto import *
from servidor import *

@app.route("/login", methods=['POST'])
def login():

    dados = request.get_json(force=True)  
    login = dados['login']
    senha = dados['senha']
    
    encontrado = Pessoa.query.filter_by(email=login, senha=cifrar(senha)).first()
    if encontrado is None: 
        resposta = jsonify({"resultado": "erro", "detalhes":"usuario ou senha incorreto(s)"})

    else:
        # códigos HTTP:
        # https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status        

        # criar a json web token (JWT)
        access_token = create_access_token(identity=login)

        # retornar
        resposta =  jsonify({"resultado":"ok", "detalhes":access_token}) 
    
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*") #meuservidor)
    # permitir envio do cookie
    #resposta.headers.add("Access-Control-Allow-Credentials", "true")

    return resposta 

