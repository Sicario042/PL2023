import json

with open('processos.txt', 'r') as f:
    data = []
    for i, line in enumerate(f):
        if i >= 20:
            break
        fields = line.strip().split("::")
        record = {
            "id": fields[0],
            "data": fields[1],
            "requerente": fields[2],
            "requerido": fields[3],
            "testemunhas": fields[4:],
        }
        data.append(record)

with open('registros.json', 'w') as f:
    json.dump(data, f, indent=4)