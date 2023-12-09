lista = [[1,2,3], [4,5,6], [7,8,9]]
for sub_sequence_nr in reversed(range(len(lista)-1)):
    next_value = lista[sub_sequence_nr + 1][-1] + lista[sub_sequence_nr][-1]
    lista[sub_sequence_nr].append(next_value)
    print(next_value)


# for i in range(len(lista)-1):
#     print(i)