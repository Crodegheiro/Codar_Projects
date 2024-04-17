from flask import Flask , jsonify , json , make_response , abort , request
from classes import Alunos

app = Flask(__name__)

a = Alunos("Carlos", 3 ,4, 5)   
b = Alunos("João", 8, 9 ,10)
c = Alunos("Pedro",10, 7, 9)
a.calcular()
b.calcular()
c.calcular()
sala = [ a, b, c]

@app.route("/")
def index():
    return "<h1>Flask esta funcionando!!!</h1>"

def get_aluno_or_404(id):
    for list in sala:
        if list.id == id:
            return list
    abort(404, "Aluno não encontrado!")

@app.route("/api/notas/")
def lista_notas():
    lista_nota=[]
    for lis in sala:
        lista_nota.append(lis.__dict__)
    return jsonify(lista_nota)

@app.route("/api/notas/<int:id>/")
def detalhar_aluno(id):
    list = get_aluno_or_404(id)
    return jsonify(list.__dict__)
    

@app.route("/api/notas/", methods=["POST"])
def criar_aluno():
    #Parsing
    data= json.loads(request.data)
    nome=data.get("nome")
    g1=data.get("g1")
    g2=data.get("g2")
    g3=data.get("g3")

    if not nome or not g1 or not g2 or not g3 :
        abort(400, "Informações do aluno faltando!")
    
    aluno = Alunos(nome=nome,g1=g1,g2=g2,g3=g3)
    aluno.calcular()
    sala.append(aluno)
    return {
        "id": aluno.id,
        "url":f"/api/notas/{aluno.id}"
        }

@app.route("/api/notas/<int:id>/", methods=["DELETE"])
def deletar_aluno(id):
    list = get_aluno_or_404(id)
    sala.remove(list)
    return jsonify(id=id)

@app.route("/api/notas/<int:id>/", methods=["PUT"])
def modificar_aluno(id):
    #Parsing
    data= request.get_json()
    nome=data.get("nome")
    g1=data.get("g1")
    g2=data.get("g2")
    g3=data.get("g3")
    if not nome or not g1 or not g2 or not g3 :
        abort(400, "Informações do aluno faltando!")
    
    aluno = get_aluno_or_404(id)
    aluno.nome = nome
    aluno.g1 = g1
    aluno.g2 = g2
    aluno.g3 = g3
    aluno.calcular()
    return jsonify(aluno.__dict__)

@app.route("/api/notas/<int:id>/", methods=["PATCH"])
def editar_aluno(id):
    #Parsing
    data= request.get_json()
    aluno = get_aluno_or_404(id)
    if "nome" in data.keys():
        name=data.get("nome")
        if not name:
            abort(400, "Informações do aluno faltando!")
        aluno.nome=name

    if "g1" in data.keys():
        g1=data.get("g1")
        if not g1:
            abort(400, "Informações do aluno faltando!")
        aluno.g1=g1

    if "g2" in data.keys():
        g2=data.get("g2")
        if not g2:
            abort(400, "Informações do aluno faltando!")
        aluno.g2=g2

    if "g3" in data.keys():
        g3=data.get("g3")
        if not g3:
            abort(400, "Informações do aluno faltando!")
        aluno.g3=g3
        
    aluno.calcular()
    return jsonify(aluno.__dict__)



@app.errorhandler(404)
def get_or_ERRO_404(erro):
    data={"erro":str(erro)}
    return (jsonify(data), 404)

@app.errorhandler(400)
def get_or_ERRO_404(erro):
    data={"erro":str(erro)}
    return (jsonify(data), 400)