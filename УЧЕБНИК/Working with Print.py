import string
import textwrap
import os
import sys
textwrap_example = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''

# ----------------------------------------------------------------------------------------------------------------------
class format():
    """format используется тогда, когда требуется подставить значения в общий шаблон"""

    """ Метод safe_substitute вместо вызова исключения перехватывает его и оставляет в тексте само выражение переменной"""
    template = string.Template("a = $b + $c")
    template.safe_substitute({'b': 123, 'C': 21})
    # Выхлоп / a = 123 + $c /

    """Метод format подставляет те значения которые мы передали аргументами на то место, где фигурные скобки"""
    template = "{m} and {a}"
    template.format(a="cat", m="dog")  # Выхлоп / 'cat and dog' / # Можем передавать пустые переменные

    "{:.3}".format(0.3141932)  # Выхлоп / 0.314 / # Округляет число до 3х знаков после запятой
    '{:,}'.format(1234)  # Выхлоп / 1,234 / # Разделить число по сотням

    "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
    #  Выхлоп / int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010/

# ----------------------------------------------------------------------------------------------------------------------
class textwrap():
    """textwrap используется тогда, когда требуется красиво оформленный вывод"""

    """Метод dedent удаляет все общие начальные пробелы из каждой строки в "тексте"."""
    dedented_text = textwrap.dedent(textwrap_example)
    """                 raw                    |               after dedent
    |_________________________________________ | ______________________________________|
    |    The textwrap module can be used to    | The textwrap module can be used to    |
    |    format text for output in situations  | format text for output in situations  |
    |    where pretty-printing is desired.     | where pretty-printing is desired.     |
    """

    """Метод fill изменяет ширину области вывода, создает висячие отступы, добавляет префикс"""
    print(textwrap.fill(dedented_text, initial_indent='', subsequent_indent=' ' * 4, width=50))
    """            raw                    |          after fill          |
    |____________________________________ | _____________________________|
    |The textwrap module can be used to   |The textwrap module can be    |
    |format text for output in situations |    used to format text for   |
    |where pretty-printing is desired.    |    output in situations where|
    |                                     |    pretty-printing is        |
    |                                     |    desired.                  |
    """

    """Метод indent управляет префиксом."""
    wrapped = textwrap.fill(dedented_text, width=30)
    final = textwrap.indent(wrapped, '> ', predicate=lambda line: True)
    """            raw                    |        after fill + indent     |
    |____________________________________ | _______________________________|
    |The textwrap module can be used to   |> The textwrap module can be    |
    |format text for output in situations |> used to format text for output|
    |where pretty-printing is desired.    |> in situations where pretty-   |
    |                                     |> printing is desired.          |
    """

    shortened = textwrap.shorten(dedented_text, 100)
    shortened_wrapped = textwrap.fill(shortened, width=50)
    """            raw                    |     after fill + shorten     |
    |____________________________________ | _____________________________|
    |The textwrap module can be used to   |The textwrap module can be    |
    |format text for output in situations |used to format text for output|
    |where pretty-printing is desired.    |in situations [...]           |
    """

# ----------------------------------------------------------------------------------------------------------------------
class sys():
    """ Секундомер в терминале [динамически обновляется]"""
    for i in range(1, 4):
        a = f"\r{'.' * i}{i}"
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rtime out")
