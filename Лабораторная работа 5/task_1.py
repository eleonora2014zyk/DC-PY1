from pprint import pprint

list_dictionaries = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)}
                     for i in range(16)]
pprint(list_dictionaries)
