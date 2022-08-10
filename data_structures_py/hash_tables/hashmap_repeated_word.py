from data_structures_py.hash_tables.hash_table import HashTable


def hashmap_repeated_word(par):
    if len(par) == 0:
        raise Exception("Can't search without a text!")

    hash_ready = par.strip(',:.!?').upper().split()
    length = len(hash_ready)

    hashed_par = HashTable(length)
    for word in hash_ready:
        if hashed_par.contains(word.strip(',:.!?')):
            return word.strip(',:.!?').lower()
        else:
            hashed_par.set(word.strip(',:.!?'), hashed_par._HashTable__hash(word.strip(',:.!?')))

    return 'There are no repetitions in this text'


par_1 = 'Once upon a time, there was a brave princess who...'

par_2 = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of ' \
        'foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of' \
        ' Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, ' \
        'we had everything before us, we had nothing before us, we were all going direct to Heaven, we were' \
        ' all going direct the other way – in short, the period was so far like the present period, that some ' \
        'of its noisiest authorities insisted on its being received, for good or for evil, in the superlative' \
        ' degree of comparison only...'

par_3 = 'It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I ' \
        'was doing in New York...'

if __name__ == "__main__":
    a = hashmap_repeated_word(par_1)
    print(a)

    b = hashmap_repeated_word(par_2)
    print(b)

    c = hashmap_repeated_word(par_3)
    print(c)
