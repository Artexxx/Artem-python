## <center>Изменяемые типы данных</center>

* [PyListObject](#Списки)

## Списки

Списки как динамические массивы
Списки в Python являются обычными [динамическими массивами](https://en.wikipedia.org/wiki/Dynamic_array) (vector в C++) и обладают всеми их свойствами с точки зрения производительности: в частности, обращение к элементу по его индексу имеет сложность *O(1)*, а поиск элемента имеет сложность *O(N)*.

Списки в CPython определены с помощью следующей структуры [PyListObject](https://github.com/python/cpython/blob/main/Include/listobject.h#L23):

```c 
typedef struct {
    PyObject_VAR_HEAD
    /* Vector of pointers to list elements.  list[0] is ob_item[0], etc. */
    PyObject **ob_item;

    /* ob_item contains space for 'allocated' elements.  The number
     * currently in use is ob_size.
     * Invariants:
     *     0 <= ob_size <= allocated
     *     len(list) == ob_size
     *     ob_item == NULL implies ob_size == allocated == 0
     * list.sort() temporarily sets allocated to -1 to detect mutations.
     *
     * Items must normally not be NULL, except during construction when
     * the list is not yet visible outside the function that builds it.
     */
    Py_ssize_t allocated;
} PyListObject;
```
Где:
  * `ob_item` - массив указателей на `PyObject`;
  * `allocated` - емкость массива (размер буффера), то есть сколько элементов можно поместить в массив `ob_item` до его увеличения, в то время как `ob_size` - текущее количество элементов в массиве.

![LIST](Sciences/images/cpython/mutable-types/listobject.svg)

Если мы добавляем новый элемент в массив и при этом размер массива совпадает с размером буффера, то есть, `ob_size == allocated`, то происходит увеличение размера буффера путем перераспределения памяти по следующему правилу:

```c 
/* This over-allocates proportional to the list size, making room
 * for additional growth.  The over-allocation is mild, but is
 * enough to give linear-time amortized behavior over a long
 * sequence of appends() in the presence of a poorly-performing
 * system realloc().
 * The growth pattern is:  0, 4, 8, 16, 25, 35, 46, 58, 72, 88, ...
 * Note: new_allocated won't overflow because the largest possible value
 *       is PY_SSIZE_T_MAX * (9 / 8) + 6 which always fits in a size_t.
 */
new_allocated = (size_t)newsize + (newsize >> 3) + (newsize < 9 ? 3 : 6);
```
Процесс перераспределения памяти в действии с помощью модуля ctypes:

```python
class ListStruct(ctypes.Structure):
    _fields_ = [("ob_refcnt", ctypes.c_ssize_t),
                ("ob_type", ctypes.c_void_p),
                ("ob_size", ctypes.c_ssize_t),
                ("ob_item", ctypes.c_long),  # PyObject** pointer cast to long
                ("allocated", ctypes.c_ssize_t)]

    def __repr__(self):
        return f"ListStruct(ob_size={self.ob_size}, allocated={self.allocated})"
```
Создадим пустой список:
```python
>>> L = []
>>> ls = ListStruct.from_address(id(L))
>>> ls
ListStruct(ob_size=0, allocated=0)
```
![LIST1](Sciences/images/cpython/mutable-types/listobject4.svg)

Добавим в список один элемент:
```python
>>> L.append(1)
>>> ls
ListStruct(ob_size=1, allocated=4)
```
![LIST1](Sciences/images/cpython/mutable-types/listobject3.svg)

Как мы видим и размер и емкость списка изменились в соответствии с правилом роста. Добавим еще несколько элементов в список:
```python
>>> L.extend([2,3,4])
>>> ls
ListStruct(ob_size=4, allocated=4)
>>> L.append(5)
>>> ls
ListStruct(ob_size=5, allocated=8)
```
![LIST1](Sciences/images/cpython/mutable-types/listobject2.svg)

**Итак**, основные различия между кортежами и списками:

- С точки зрения внутреннего представления кортежи являются статическими массивами, а списки динамическими;
- Кортежи занимают меньше места в памяти, так как имеют фиксированную длину;
- Кортежи неизменяемые (*immutable*) и могут быть выступать в качестве ключей словарей или элементов множеств;
- Кортежи обычно представляют абстрактные объекты, обладающие некоторой структурой (`collections.namedtuple`).


---
## Словари

Словари являются одной из самых важных и сложных структур в Python. Словари представляют собой множество упорядоченных пар вида «ключ:значение».

Иногда словари называют [ассоциативными массивами](https://ru.wikipedia.org/wiki/Ассоциативный_массив), иногда отображениями (имеется ввиду отображение множества ключей словаря в множество его значений).

Как и списки, словари имеют переменную длину, произвольную вложенность и могут хранить значения произвольных типов.

Тем не менее следует знать, что ключами словарей могут быть только хешируемые объекты, то есть те объекты, для которых определена хеш-функция (обычно это числа, строки и кортежи).

Хеш-функция это такая функция, которая задает правило отображания объектов в целые числа.
Существует множество видов хеш-функций и они должны обладать рядом свойств, например, «если два объекта равны, то их хеши должны быть одинаковыми» или «если объекты имеют одинаковый хеш, то вероятно это один и тот же объект».
Для наглядности рассмотрим простой пример. Зададим хеш-функцию для строк, которая вычисляет хеш как сумму произведений позиции символа на его кодовый знак, и будем использовать эту функцию для определения индекса в списке куда следует поместить строку:

<iframe width="1000" height="600" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20my_hash%28astring%29%3A%0A%20%20%20%20h%20%3D%200%0A%20%20%20%20for%20pos,%20ch%20in%20enumerate%28astring%29%3A%0A%20%20%20%20%20%20%20%20h%20%2B%3D%20pos%20*%20ord%28ch%29%0A%20%20%20%20return%20h%0A%0AL%20%3D%20%5BNone,%20None,%20None,%20None,%20None%5D%0A%0Aindex%20%3D%20my_hash%28'%D0%AF'%29%20%25%20len%28L%29%0AL%5Bindex%5D%20%3D%20'%D0%AF'%0A%0Aindex%20%3D%20my_hash%28'%D0%BD%D0%B8%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0'%29%20%25%20len%28L%29%0AL%5Bindex%5D%20%3D%20'%D0%BD%D0%B8%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0'%0A%0Aindex%20%3D%20my_hash%28'%D0%BD%D0%B5'%29%20%25%20len%28L%29%0AL%5Bindex%5D%20%3D%20'%D0%BD%D0%B5'%0A%0Aindex%20%3D%20my_hash%28'%D0%BF%D0%BE%D0%B2%D1%82%D0%BE%D1%80%D1%8F%D1%8E%D1%81%D1%8C'%29%20%25%20len%28L%29%0AL%5Bindex%5D%20%3D%20'%D0%BF%D0%BE%D0%B2%D1%82%D0%BE%D1%80%D1%8F%D1%8E%D1%81%D1%8C'&codeDivHeight=400&codeDivWidth=400&cumulative=false&curInstr=0&heapPrimitives=false&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>
