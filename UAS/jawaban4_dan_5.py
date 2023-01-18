import os
import sqlite3

db = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'hewan.db')

conn = sqlite3.connect(db)
curs = conn.cursor()
curs.execute('CREATE TABLE IF NOT EXISTS kucing (nama, jenis, jenis_kelamin)')
values = [('Piki', 'Anggora', 'Laki-Laki'), ('Copa', 'Persia', 'Perempuan')]
curs.executemany('INSERT INTO kucing VALUES (?, ?, ?)', values)
conn.commit()
rows = curs.execute("SELECT * FROM kucing").fetchall()
print(rows)
conn.close()
