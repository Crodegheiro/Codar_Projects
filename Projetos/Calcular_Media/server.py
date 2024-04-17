from http.server import HTTPServer, BaseHTTPRequestHandler
from classes import Alunos
import json

a = Alunos("Carlos", 3 ,4, 5)   
b = Alunos("João", 8, 9 ,10)
c = Alunos("Pedro",10, 7, 9)
a.calcular()
b.calcular()
c.calcular()
sala = [ a, b, c]

class SimplerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8" )
            self.end_headers()
            
            sala_cont= ""
            for al in sala:
                sala_cont += f"""
                <tr>
                    <th>{al.nome}</th>
                    <th>{al.g1}</th>
                    <th>{al.g2}</th>
                    <th>{al.g3}</th>
                    <th>{al.resultado}</th>
                <tr>
                """
            data= f"""
            <html> 
                <table>
                    <tr>
                        <th>Nome</th>
                        <th>G1</th>
                        <th>G2</th>
                        <th>G3</th>
                        <th>Nota Final</th>
                    <tr>
                    {sala_cont}
                </table>
            </html>
            """.encode()
            self.wfile.write(data)
        elif self.path == "/json":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8" )
            self.end_headers()
            list_alunos = []
            for al in sala:
                list_alunos.append({
                    "nome":al.nome,
                    "G1": al.g1,
                    "G2": al.g2,
                    "G3": al.g3,
                    "Nota Final": al.resultado 
                })
            data=json.dumps(list_alunos).encode()
            self.wfile.write(data)



server = HTTPServer(("localhost", 8000), SimplerHandler)
server.serve_forever()