tupla = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO", "GRATIS", "ESTUDAR", "PRATICAR", "TRABALHAR", "MERCADO", "PROGRAMAR", "FUTURO")
for i in tupla:
    vogal = ''

    if "A" in i:
        vogal = "A"
    if "E" in i:
        vogal += "E"
    if "I" in i:
        vogal += "I"
    if "O" in i:
        vogal += "O"
    if "U" in i:
        vogal += "U"
    print(f"A palavra {i} tem as vogais {vogal}")