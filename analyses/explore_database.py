#!/usr/bin/env python3
import duckdb

# Se connecter à la base
conn = duckdb.connect("database/local_birth_data.duckdb")

print("=== Tables disponibles ===")
tables = conn.execute("SHOW TABLES").fetchall()
for table in tables:
    print(f"- {table[0]}")

print("\n=== Aperçu des départements ===")
dept = conn.execute("SELECT * FROM departements LIMIT 5").fetchall()
for row in dept:
    print(row)

print("\n=== Nombre total de naissances ===")
count = conn.execute("SELECT COUNT(*) as total FROM donnees_naissances_2021").fetchall()
print(f"Total: {count[0][0]} naissances")

print("\n=== Top 5 départements par nombre de naissances ===")
top_dept = conn.execute(
    """
    SELECT d.NOM, COUNT(*) as nb_naissances
    FROM donnees_naissances_2021 n
    LEFT JOIN departements d ON n.DEPDOM = d.CODE
    GROUP BY d.NOM, d.CODE
    ORDER BY nb_naissances DESC
    LIMIT 5
"""
).fetchall()

for row in top_dept:
    print(f"{row[0]}: {row[1]} naissances")


conn.close()
