import sqlite3

con = sqlite3.connect("meu_banco.db")

try:
    con = sqlite3.connect("meu_banco.db")
    cur = con.cursor() # abrindo o curso
    #cur.execute("CREATE TABLE pessoa(id, nome, idade, cpf)") # criando tabela pessoa
    #cur.execute("INSERT INTO pessoa VALUES(1, 'aryel', 17, '532.775.XXX-80')")
    res = cur.execute("SELECT * FROM pessoa")
    pessoas = res.fetchone()

    print(pessoas)
    #cur.execute("DELETE FROM pessoa Where id = 1")
    con.commit()

except ConnectionRefusedError as c:
    print('erro de conexao com o banco')    