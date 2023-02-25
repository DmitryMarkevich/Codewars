import string


def bar_chart(f: str) -> None:
    """
    The function takes a string.
    Prints a histogram of '#' characters to the console.

    """

    def read_file(new_f: str) -> str:
        with open(new_f, 'r', encoding='utf-8') as file:
            return ''.join(i.strip() for i in file.readlines())

    st_ = read_file(f)
    sort_list = [(i, st_.count(i)) for i in set(st_) if i not in (' ',)]
    sort_list.sort(key=lambda d: ord(d[0]))
    count = max([j[-1] for j in sort_list])
    for _ in range(count, -1, -1):
        for i in sort_list:
            if count != 0:
                print('#' if i[-1] >= count else ' ', end='')
            else:
                print(i[0], end='')
        print()
        count -= 1


# new_f = 'bar_chart.txt'
# bar_chart(new_f)


def order(sentence: str) -> list:
    """
    функция на вход принимает строку, в каждом слове которой спрятана цифра от 0 до 9.
    Возвращает список слов, отсортированный по имеющейся цифре.

    """

    def return_a_digit(st_: str) -> int:
        for i in range(1, 10):
            if str(i) in st_:
                return i

    result = sentence.split()
    result.sort(key=return_a_digit)
    return ' '.join(result)


# print(order("An9d 5the mo6me raths4 outg2rabe"))


def accum(s: str) -> str:
    """
    Функция на вход принимает строку.
    Возвращает строку в которой через тере прописаны символы исходной строки, умноженные на индекс,
    первый символ находится в верхнем регистре.

    """
    return '-'.join([el.upper() + el.lower() * ind for ind, el in enumerate(s)])


# print(accum('abcd'))


def likes(names: list) -> str:
    """
    Функция на вход принимает список с именами.
    Возвращает строку, в зависимости от количества имен в списке, с подстановкой имен.

    """
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n - 2)


# for ls in [["Alex"], ["Alex", "Jacob"], ["Alex", "Jacob", "Mark"], ["Alex", "Jacob", "Mark", "Max"]]:
#     print(likes(ls))

def is_pangram(s: str) -> bool:
    """
    Метод sets.issubset(other) позволяет проверить находится ли каждый элемент множества sets в
    последовательности other. Метод возвращает True, если множество sets является подмножеством
    итерируемого объекта other, если нет, то вернет False.

    """
    return set(string.ascii_lowercase).issubset(s.lower())


# print(is_pangram("The quick, brown fox jumps over the lazy dog!"),
#       is_pangram("And the mome raths outgrabe."), sep='\n')


def is_valid_walk(walk: list) -> bool:
    """
    Вы живете в городе Картезия, где все дороги выложены идеальной сеткой.
    Вы пришли на встречу на десять минут раньше назначенного срока,
    поэтому решили воспользоваться возможностью прогуляться.
    Город предоставляет своим горожанам приложение Walk Generating на их телефонах — каждый раз,
    когда вы нажимаете кнопку, оно отправляет вам массив строк из одной буквы,
    представляющих направления ходьбы (например, ['n', 's', 'w', «е»]).
    Вы всегда проходите только один квартал для каждой буквы (направления),
    и вы знаете, что вам потребуется одна минута, чтобы пройти один городской квартал,
    поэтому создайте функцию, которая будет возвращать true, если прогулка, которую предлагает вам приложение,
    займет у вас ровно десять минут (вы не хочу ни рано, ни поздно!) и, конечно же, вернет вас в исходную точку.
    В противном случае верните false.

    """
    dict_direction = {'n': 1, 's': -1, 'w': 1, 'e': -1}
    direction1, direction2 = sum(dict_direction[i] for i in walk if i in ('n', 's')), \
                             sum(dict_direction[i] for i in walk if i in ('w', 'e'))

    return True if len(walk) == 10 and direction1 == 0 and direction2 == 0 else False


# for route in [['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e'],
#               ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'],
#               ['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']]:
#     print(is_valid_walk(route))


def cakes(recipe: dict, available: dict) -> int:
    """
    Напишите функцию cakes(), которая принимает рецепт (dict) и
    доступные ингредиенты (dict) и возвращает максимальное количество пирожных,
    которые Пит может испечь (целое число). Для простоты нет единиц измерения количества (например,
    1 фунт муки или 200 г сахара — это просто 1 или 200). Ингредиенты, отсутствующие в объектах,
    можно считать равными 0.

    """
    count = []
    for key in recipe:
        if key not in available:
            return 0
        count.append(available[key] // recipe[key])

    return min(count)


# print(cakes({'a': 2, 'b': 10, 'c': 1}, {'a': 10, 'b': 20, 'c': 30, 'd': 100}),
#       cakes({'a': 2, 'b': 10, 'c': 1}, {'b': 20, 'c': 30, 'd': 100}),
#       cakes({'a': 2, 'b': 10, 'c': 1}, {'a': 50, 'b': 50, 'c': 30, 'd': 100}), sep='\n')


def digital_root(n: int) -> int:
    """
    Цифровой корень — это рекурсивная сумма всех цифр числа.
    Учитывая n, возьмите сумму цифр n. Если это значение имеет более одной цифры,
    продолжайте уменьшать таким образом, пока не будет получено однозначное число.
    Ввод будет неотрицательным целым числом.
    (942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6)
    (132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6)
    (493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2)

    """
    if len(str(n)) == 1:
        return n
    return digital_root(sum(map(int, str(n))))


# print(digital_root(942))
# print(digital_root(132189))
# print(digital_root(493193))

def duplicate_encode(word: str) -> str:
    """
    Цель этого упражнения — преобразовать строку в новую строку,
    где каждый символ в новой строке соответствует
    "("тому, если этот символ появляется только один раз в исходной строке или ")"
    если этот символ появляется в исходной строке более одного раза.
    Игнорировать заглавные буквы при определении, является ли символ дубликатом.
    ("recede"   =>  "()()()"), ("din"      =>  "(((")

    """
    word = word.lower()
    return ''.join(['(' if word.count(el) == 1 else ')' for el in word])


# print(duplicate_encode('recede'))
# print(duplicate_encode('din'))


def compare_lists(l1: list, l2: list) -> bool:
    """
    Функция принимает на вход два списка.
    Возвращает True, если структура входных списков одинаковая,
    если разная возвращает False.

    """
    return all(map(lambda y, z: y == z, [i for i in str(l1) if i in ('[', ']', ',', ' ')],
                   [j for j in str(l2) if j in ('[', ']', ',', ' ')]))


# print(compare_lists([2, [[]]], [1, [], [2, []]]))
# print(compare_lists([1, [], [2, []]], [1, [], [2, []]]))
# print(compare_lists([2, [[]]], [1, [[1]]]))
