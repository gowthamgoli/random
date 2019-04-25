import re
from collections import defaultdict
from pprint import pprint

with open('Staden_link.txt') as f:
    data = f.read()

matches = re.findall(r"([A-za-z0-9]+)\/(?:([A-Za-z']+)\/)?([A-Za-z']+)\/\/", data)
enzymes_dict = {}
for m in matches:
    # print(f'enzyme: {m[0]}', end=' ')
    enzymes_dict[m[0]] = []
    if m[1]:
        # print(m[1])
        enzymes_dict[m[0]].append({
            'pattern': m[1],
            'cut_index': m[1].index("'") if "'" in m[1] else -1,
            'regex': m[1].replace("'", '').replace('N', '[ACGT]') 
        })
    if m[2]:
        enzymes_dict[m[0]].append({
            'pattern': m[2],
            'cut_index': m[2].index("'") if "'" in m[2] else -1,
            'regex': m[2].replace("'", '').replace('N', '[ACGT]') 
        })

with open('SeqLibrary.txt') as f:
    data = f.readlines()
    data = [line.strip() for line in data]

sequences = []
for line in data:
    if line.startswith('>'): 
        new_sequence = ''
        continue
    if line == '||': 
        sequences.append(new_sequence)
    else:
        new_sequence += line
# pprint(sequences)
         
for i, sequence in enumerate(sequences):
    if i > 0: continue
    print(f'Sequence {i + 1} Results:')
    for enzyme, enzymes_info in enzymes_dict.items():
        cut_indices = []
        for info in enzymes_info:
            matches = re.finditer(info['regex'], sequence)
            for m in matches:
                cut_indices.append(m.start() + info['cut_index'])
        if cut_indices:
            print(f'{enzyme}: {cut_indices}')
