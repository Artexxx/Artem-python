import string
import textwrap
import os
import sys
import time

textwrap_example = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
class format():
    """format используется тогда, когда требуется подставить значения в общий шаблон"""

    """ Метод safe_substitute перехватывает исключение KeyError и оставляет в тексте само выражение переменной"""
    template = string.Template("a = $b + $c")
    template.safe_substitute({'b': 123, 'c': 21})
    # Выхлоп / a = 123 + $c /

    """Метод format подставляет значения переменных внутрь фигурных скобок"""
    template = "{m} and {a}"
    template.format(a="cat", m="dog")  # Выхлоп / 'cat and dog' / # Можем передавать пустые переменные

    "{:.3}".format(0.3141932)  # Выхлоп / 0.314 / # Округляет число до 3х знаков после запятой
    '{:,}'.format(1234)  # Выхлоп / 1,234 / # Включение разделитель разрядов

    "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
    #  Выхлоп / int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010/

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
class textwrap():
    """Модуль textwrap — это простой способ очистить текст и сделать вывод под размеры терминала"""

    """Метод dedent удаляет все общие начальные пробелы из каждой строки в "тексте"."""
    dedented_text = textwrap.dedent(textwrap_example)
    """                 Before                 |               After dedent            |
    |——————————————————————————————————————————|———————————————————————————————————————|
    |    The textwrap module can be used to    | The textwrap module can be used to    |
    |    format text for output in situations  | format text for output in situations  |
    |    where pretty-printing is desired.     | where pretty-printing is desired.     |
    """

    """Метод fill изменяет ширину области вывода, создает висячие отступы, добавляет префикс"""
    print(textwrap.fill(dedented_text, initial_indent='', subsequent_indent=' ' * 4, width=50))
    """            Before                 |          After fill          |
    |—————————————————————————————————————|——————————————————————————————|
    |The textwrap module can be used to   |The textwrap module can be    |
    |format text for output in situations |    used to format text for   |
    |where pretty-printing is desired.    |    output in situations where|
    |                                     |    pretty-printing is        |
    |                                     |    desired.                  |
    """

    """Метод indent управляет префиксом."""
    wrapped = textwrap.fill(dedented_text, width=30)
    final = textwrap.indent(wrapped, '> ', predicate=lambda line: True)
    """            Before                 |      After fill + indent       |
    |—————————————————————————————————————|————————————————————————————————|
    |The textwrap module can be used to   |> The textwrap module can be    |
    |format text for output in situations |> used to format text for output|
    |where pretty-printing is desired.    |> in situations where pretty-   |
    |                                     |> printing is desired.          |
    """

    """Метод shorten сжимает пробелы и обрезает по ширине"""
    shortened = textwrap.shorten(dedented_text, 100)
    shortened_wrapped = textwrap.fill(shortened, width=50)
    """            Before                 |     After fill + shorten     |
    |—————————————————————————————————————|——————————————————————————————|
    |  The  textwrap   module can   be    |The textwrap module can be    |
    | used to   format text for  output   |used to format text for output|
    | in situations where pretty-printing |in situations [...]           |
    """

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
class sys():
    """ Секундомер в терминале [динамически обновляется]"""
    for i in range(1, 4):
        a = f"\r{'.' * i}{i}"
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rtime out")
