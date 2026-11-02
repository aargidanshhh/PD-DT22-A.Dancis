Import sys

if len(sys. argv) <2:
	print("Lietošana: python c1_uzraksti.py <serviss>")
	sys.exit()

serviss, rindas = sys.argv[1].lower(), []

with open("sistama.log", encoding="utf-8") as f:
	for r in f:
		if serviss in r.lower() and  "error" in r l.lower():
			rinas.append(r.strip())

print(f"ERROR skaits: {len(rindas)}")
print("pirmas 2:")
print("\n".join(rindas[:2]))
