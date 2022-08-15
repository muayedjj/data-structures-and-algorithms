from data_structures_py.hash_tables.hash_table import HashTable


def left_join(ht1, ht2):
    output = []

    for g in ht1.key():
        if ht2.contains(g):
            output.append([g, ht1.get(g), ht2.get(g)])

        else:
            output.append([g, ht1.get(g), 'Null'])

    return output


if __name__ == "__main__":

    ht1 = HashTable()
    ht2 = HashTable()

    arr1 = [
        ["font", "enamored"],
        ["wrath", "anger"],
        ["diligent", "employed"],
        ["outfit", "garb"],
        ["guide", "usher"]
        ]

    arr2 = [
        ["font", "averse"],
        ["wrath", "delight"],
        ["diligent", "idle"],
        ["flow", "jam"],
        ["guide", "follow"]
    ]

    for i in range(len(arr1)):

        ht1.set(arr1[i][0], arr1[i][1])
        ht2.set(arr2[i][0], arr2[i][1])

    print(left_join(ht1, ht2))

    # print(ht1.key())
