# На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'),
# ..., ('ключ_N', 'значение_N'))
# Выводить на экран ничего не нужно, только преобразовать строку
# в кортеж с именем tp.
# Sample Input:
# house=дом car=машина men=человек tree=дерево
# Sample Output:
# (('house', 'дом'), ('car','машина'), ('men', 'человек'), ('tree', 'дерево'))


def string_conversion(text: str) -> tuple[tuple, ...]:
    pairs_lt = text.split(' ')
    return tuple(map(lambda pair: tuple(pair.split('=')), pairs_lt))


print(string_conversion('house=дом car=машина men=человек tree=дерево'))
