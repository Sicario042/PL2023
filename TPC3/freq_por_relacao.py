
import re

relationship_freq = {}

with open('processos.txt', 'r') as f:
    for line in f:
        relation = re.findall(r'(?:irmãos?|filhos?|netos?|bisnetos?|sobrinhos?|primos?|genros?|sogros?|cunhados?|tios?|avôs?|bisavôs?|sobrinhos-netos?|primo-netos?)', line, re.IGNORECASE)

        if relation:
            for r in relation:
                if r in relationship_freq:
                    relationship_freq[r] += 1
                else:
                    relationship_freq[r] = 1

for r, freq in sorted(relationship_freq.items(), key=lambda x: x[1], reverse=True):
    print(f'{r}: {freq}')