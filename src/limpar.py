import sqlite3

conn = sqlite3.connect('../data/pagamentos.db')
cursor = conn.cursor()

cursor.execute ("DELETE FROM pagamentos WHERE valor_brl = 0")
conn.commit()
conn.close()

print ("Registros com valor_brl = 0 removidos.")