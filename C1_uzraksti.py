import sys

if len(sys.argv) < 2:
    print("Lietošana: python c1_uzraksti.py <serviss>")
    sys.exit()

serviss = sys.argv[1]
rindas = []

for r in open("sistema.log", encoding="utf-8"):
    if serviss in r and "ERROR" in r:
        rindas.append(r.strip())

print("ERROR skaits:", len(rindas))
print("Pirmās 2:")
for r in rindas[:2]:
    print(r)
