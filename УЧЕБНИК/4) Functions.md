## <center>Функции</center>



**Функции** – это многократно используемые фрагменты программы. Они позволяют дать имя определенному блоку команд для того, чтобы выполнять этот блок по указанному имени в любом месте программы и сколь угодно много раз.


```python
def minimum(a: float, b: float) -> float:
    """ Function to get minimum of two arguments

    Returns:
    --------
    The smallest argument.

    Examples:
    ---------
    >>> minimum(0, 1)
    0
    """
    return a if a < b else b
```
Список инструкций, которые будут выполнены при вызове функции, также достаточно простой, на стек помещаются два значения, выполняется операция сравнения и, в зависимости от результата, возвращается значение `a` или `b`:

```python
>>> dis.dis(minimum)
 13           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 COMPARE_OP               0 (<)
              6 POP_JUMP_IF_FALSE       12
              8 LOAD_FAST                0 (a)
             10 RETURN_VALUE
        >>   12 LOAD_FAST                1 (b)
             14 RETURN_VALUE
```

### Функций в Python
Как мы уже говорили, все является объектом, включая функции. Функции представлены структурой [PyFunctionObject](https://github.com/python/cpython/blob/3.8/Include/funcobject.h#L21):
```c
typedef struct {
    PyObject_HEAD
    PyObject *func_code;        /* A code object, the __code__ attribute */
    PyObject *func_globals;     /* A dictionary (other mappings won't do) */
    PyObject *func_defaults;    /* NULL or a tuple */
    PyObject *func_kwdefaults;  /* NULL or a dict */
    PyObject *func_closure;     /* NULL or a tuple of cell objects */
    PyObject *func_doc;         /* The __doc__ attribute, can be anything */
    PyObject *func_name;        /* The __name__ attribute, a string object */
    PyObject *func_dict;        /* The __dict__ attribute, a dict or NULL */
    PyObject *func_weakreflist; /* List of weak references */
    PyObject *func_module;      /* The __module__ attribute, can be anything */
    PyObject *func_annotations; /* Annotations, a dict or NULL */
    PyObject *func_qualname;    /* The qualified name */
    vectorcallfunc vectorcall;

    /* Invariant:
     *     func_closure contains the bindings for func_code->co_freevars, so
     *     PyTuple_Size(func_closure) == PyCode_GetNumFree(func_code)
     *     (func_closure may be NULL if PyCode_GetNumFree(func_code) == 0).
     */
} PyFunctionObject;
```
Где: 
Поле `func_code (__code__)` хранит ссылку на структуру `PyCodeObject` («объект кода»), которая в свою очередь содержит инструкции для виртуальной машины Python, число аргументов, сами аргументы и т.д. 

```python
def square(x): 
    return x**2

>>> dis.dis(square)
  1           0 LOAD_FAST                0 (x)
              2 LOAD_CONST               1 (2)
              4 BINARY_POWER
              6 RETURN_VALUE
>>> square.__code__.co_code
b'|\x00d\x01\x13\x00S\x00'
>>> list(square.__code__.co_code)
[124, 0, 100, 1, 19, 0, 83, 0]
```
Список опкодов можно найти в файле [Include/opcode.h](https://github.com/python/cpython/blob/3.8/Include/opcode.h):
```c 
// ...
#define BINARY_POWER             19
// ...
#define RETURN_VALUE             83
// ...
#define LOAD_CONST              100
// ...
#define LOAD_FAST               124
```

> https://punchagan.muse-amuse.in/blog/python-globals/ 
> <br> Every function has an associated **globals** dictionary, which is the same as the module’s **dict** for the module where it was defined. This **globals** dict is the name-space that is looked up when trying to fetch globals within a function.
> 
```python
>>> square.__globals__
{ '__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'square': <function square at 0x1060a50d0
    }
```
Поля `func_defaults (__defaults__)` и `func_kwdefaults (__kwdefaults__)` содержат значения по умолчанию для позиционных и ключевых аргументов, соответственно:

```python
>>>def test(arg0, *, arg1=0, arg2=1, arg3=2):
...    pass
>>> test.__kwdefaults__
{'arg1': 0, 'arg2': 1, 'arg3': 2} # Только обязательные именованные аргументы
```

Важно отметить, что поля `__defaults__` и `__kwdefaults__` являются изменяемыми и инициализируются один раз при создании функции. Рассмотрим два примера:

```python
def buggy_append(value, L=[]):
    L.append(value)
    return L

>>> buggy_append.__defaults__
([],)
>>> buggy_append(1)
[1]
>>> buggy_append(2)
[1, 2]
>>> buggy_append.__defaults__
([1, 2],)
>>> buggy_append.__defaults__[0].append(3)
>>> buggy_append(4)
[1, 2, 3, 4]
```
```python
def square(*, x):
  return x * x

>>> square()
...
TypeError: foo() missing 1 required keyword-only argument: 'x'
>>> square.__kwdefaults__ = {'x': 5}
>>> square()
25
```
⚫ Значения, назначенные значениями по умолчанию, всегда должны быть неизменяемыми объектами (None, int, bool, tuple, str ...)
```python
def test(a, b=[]):
    print(a, b); return b

x = test(1)  # Выхлоп /1 [] /
x.append('О нет!!!')
test(1)  # Выхлоп /1 ['О нет!!!'] / Значение по умолчанию изменилось.
```

Поле `__closure__` содержит кортеж значений, а именно ячеек (cell objects), необходимых функции, но находящихся в объемлющем пространстве имен. Давайте рассмотрим следующий пример:

```python
def curry_pow(base=1):
    def power(x):
        return base**x
    return power

>>> pow2 = curry_pow2(2)
>>> pow2(3)
8
```
Приведенный пример иллюстрирует каррирование, то есть процесс, при котором функция от нескольких аргументов преобразуется в функцию (или набор функций) от одного аргумента.

```python
>>> pow2.__closure__
(<cell at ...: int object at ...>,)
>>> pow2.__closure__[0].cell_contents
2
```
```python
>>> dis.dis(curry_pow)
  2           0 LOAD_CLOSURE             0 (base)
              2 BUILD_TUPLE              1
              4 LOAD_CONST               1 (<code object power at 0x10a5e0810 ...>)
              6 LOAD_CONST               2 ('curry_pow.<locals>.power')
              8 MAKE_FUNCTION            8
             10 STORE_FAST               1 (power)

  4          12 LOAD_FAST                1 (power)
             14 RETURN_VALUE

Disassembly of <code object power at 0x10a5e0810 ...>:
  3           0 LOAD_DEREF               0 (base)
              2 LOAD_FAST                0 (x)
              4 BINARY_POWER
              6 RETURN_VALUE
```

Поле `func_name (__name__)` является изменяемым и содержит имя функции.
Значение этого атрибута обычно используется такими модулями как pydoc для генерирования документации:

```python
>>> square.__name__
'square'
>>> help(square)
Help on function square...
>>> square.__name__ = 'cube'
>>> help(square)
Help on function cube...
```
Необходимость в возможности изменения этого атрибута станет очевидной, когда мы будем говорить о декораторах, но мы всегда можем получить исходное имя функции через неизменяемый атрибут `co_name` у объекта кода:

```python
>>> square.__code__.co_name
'square'
```

Поле `func_dict (__dict__)` содержит ссылку на словарь с произвольными (пользовательскими) атрибутами ([PEP 232 - Function Attributes](https://www.python.org/dev/peps/pep-0232/)).
```python
>>> square.__dict__
{}
>>> sqaure.ru_doc = 'Функция возведения значния аргумента в квадрат'
>>> square.__dict__
{'ru_doc': 'Функция возведения значния аргумента в квадрат'}
```

Поле `func_module (__module__)` это имя модуля, в котором была определена функция:

```python
>>> globals()['__name__']
'__main__'
>>> sqaure.__module__
'__main__'
>>> globals()['__name__'] = '__secondary__'
>>> def cube(x): return x**3
>>> cube.__module__
'__secondary__'
```

Поле `func_annotations (__annotations__)` содержит аннотации и зачастую используется статистическими анализаторами кода, такими как [mypy](http://mypy-lang.org/) или [pyre](https://pyre-check.org/):
```python
>>> minimum.__annotations__
{
    'x': <class 'float'>,
    'values': <class 'float'>,
    'lower': <class 'float'>,
    'upper': <class 'float'>,
    'return': <class 'float'>
}
```
Поле `func_qualname (__qualname__)` содержит «расширенное» имя функции или класса и используется для интроспекции ([PEP 3155](https://www.python.org/dev/peps/pep-3155/)):
```python
class A:
    class B:
        def d(self):
            pass

>>> A.B.d.__name__
'd'
>>> A.B.d.__qualname__
'A.B.d'
```
### Вызов функций

Концепция callable-объекта является фундаментальной в Python. Когда мы думаем о том, что может быть «вызвано» (called), то первое, что приходит на ум, это функции. Но кроме функций есть еще методы и классы, а также любой объект, в типе которого определен магический метод __call__:

```python
class Joke:
    def __call__(self):
        return 'That what she said'

>>> joke = Joke()
>>> joke()
'That what she said'
```
В этом примере мы «вызываем» класс `Joke` для инстанцирования нового объекта, а затем осуществляем «вызов» экземпляра класса как если бы это была обычная функция.

Когда происходит «вызов», то в большинстве случаев, генерируется опкод `CALL_FUNCTION` (вызов callable-объекта):

```python
>>> import dis
>>> dis.dis("add(1,2)")
  1           0 LOAD_NAME                0 (add)
              2 LOAD_CONST               0 (1)
              4 LOAD_CONST               1 (2)
              6 CALL_FUNCTION            2
              8 RETURN_VALUE
```

>`CALL_FUNCTION(argc)`
><br>Calls a callable object with positional arguments. `argc` indicates the number of positional arguments. The top of the stack contains positional arguments, with the right-most argument on top. Below the arguments is a callable object to call. `CALL_FUNCTION` pops all arguments and the callable object off the stack, calls the callable object with those arguments, and pushes the return value returned by the callable object.

Давайте кратко рассмотрим обработчик опкода [CALL_FUNCTION](https://github.com/python/cpython/blob/3.8/Python/ceval.c#L3496):
```c
case TARGET(CALL_FUNCTION): {
    PREDICTED(CALL_FUNCTION);
    PyObject **sp, *res;
    sp = stack_pointer;
    res = call_function(tstate, &sp, oparg, NULL);
    stack_pointer = sp;
    PUSH(res);
    if (res == NULL) {
        goto error;
    }
    DISPATCH();
}
```
Фактически происходит вызов функции [call_function](https://github.com/python/cpython/blob/3.8/Python/ceval.c#L3496), куда передается адрес вершины стека `sp` и число позиционных аргументов `oparg`:
```python
(gdb) p *(sp-1)
$1 = 2
(gdb) p *(sp-2)
$2 = 1
(gdb) p *(sp-3)
$3 = <function at remote 0x1014597d0>
(gdb) p ((PyFunctionObject*)(*(sp-3)))->func_name
$4 = 'add'
(gdb) p oparg
$5 = 2
```
`call_function` является общей для вызова функций, методов, классов и других объектов:

```c 
Py_LOCAL_INLINE(PyObject *) _Py_HOT_FUNCTION
call_function(PyThreadState *tstate, PyObject ***pp_stack, Py_ssize_t oparg, PyObject *kwnames)
{
    PyObject **pfunc = (*pp_stack) - oparg - 1;
    PyObject *func = *pfunc;
    PyObject *x, *w;
    Py_ssize_t nkwargs = (kwnames == NULL) ? 0 : PyTuple_GET_SIZE(kwnames);
    Py_ssize_t nargs = oparg - nkwargs;
    PyObject **stack = (*pp_stack) - nargs - nkwargs;

    if (tstate->use_tracing) {
        x = trace_call_function(tstate, func, stack, nargs, kwnames);
    }
    else {
        x = _PyObject_Vectorcall(func, stack, nargs | PY_VECTORCALL_ARGUMENTS_OFFSET, kwnames);
    }

    // ...

    return x;
}
```
Происходит подготовка аргументов для вызова функции [`_PyObject_Vectorcall`](https://github.com/python/cpython/blob/3.8/Include/cpython/abstract.h#L114), где `nargs` и `nkwargs` указывает на число позиционных и именованных аргументов, соответственно, `nkwargs` представляет собой кортеж с именами ключевых аргументов (опкод `CALL_FUNCTION_KW`), `stack` указывает на первый аргумент функции, а `func` указывает на объект `PyFunctionObject` (нашу функцию `add`):
```python 
(gdb) p nargs
$6 = 2
(gdb) p nkwargs
$7 = 0
(gdb) p kwnames
$8 = 0x0
(gdb) p *stack
$9 = 1
(gdb) p *(stack+1)
$10 = 2
(gdb) p *(stack-1)
$11 = <function at remote 0x1014597d0>
(gdb) p func
$12 = <function at remote 0x1014597d0>
(gdb) p ((PyFunctionObject*)0x1014597d0)->func_name
$13 = 'add'
```
```c
static inline PyObject *
_PyObject_Vectorcall(PyObject *callable, PyObject *const *args,
                     size_t nargsf, PyObject *kwnames)
{
    PyObject *res;
    vectorcallfunc func;
    // ...
    func = _PyVectorcall_Function(callable);
    if (func == NULL) {
        Py_ssize_t nargs = PyVectorcall_NARGS(nargsf);
        return _PyObject_MakeTpCall(callable, args, nargs, kwnames);
    }
    res = func(callable, args, nargsf, kwnames);
    return _Py_CheckFunctionResult(callable, res, NULL);
}
```
В функции `_PyObject_Vectorcall` проверяется поддерживает ли callable-объект новый протокол Vectorcall, который был введен в [PEP 590](https://www.python.org/dev/peps/pep-0590/) с целью оптимизации вызова callable-объектов:

>The poor performance is largely a result of having to create intermediate tuples, and possibly intermediate dicts, during the call. This is mitigated in CPython by including special-case code to speed up calls to Python and builtin functions. Unfortunately, this means that other callables such as classes and third party extension objects are called using the slower, more general tp_call calling convention.
>
> This PEP proposes that the calling convention used internally for Python and builtin functions is generalized and published so that all calls can benefit from better performance...

Отметим, что все пользовательские функции, начиная с Python 3.8, поддерживают протокол `Vectorcall`. 
Возможно, вы обратили внимание, что последнем полем структуры `PyFunctionObject` является vectorcall типа [`vectorcallfunc`](https://github.com/python/cpython/blob/3.8/Include/cpython/object.h#L58):
```c 
typedef PyObject *(*vectorcallfunc)(PyObject *callable, PyObject *const *args,
                                    size_t nargsf, PyObject *kwnames);
```
Это поле инициализируется при создании новой функции (см. опкод `MAKE_FUNCTION`):

```c 
PyObject *
PyFunction_NewWithQualName(PyObject *code, PyObject *globals, PyObject *qualname)
{
    PyFunctionObject *op;
    // ...
    op = PyObject_GC_New(PyFunctionObject, &PyFunction_Type);
    // ...
    op->vectorcall = _PyFunction_Vectorcall;
    // ...
    return (PyObject *)op;
}
```
Таким образом, вызов:

```python
res = func(callable, args, nargsf, kwnames);
```
эквивалентен вызову:
```python
res = _PyFunction_Vectorcall(callable, args, nargsf, kwnames);
```
Наконец перейдем к [`_PyFunction_Vectorcall`](https://github.com/python/cpython/blob/3.8/Objects/call.c#L386):

```c 
PyObject *
_PyFunction_Vectorcall(PyObject *func, PyObject* const* stack,
                       size_t nargsf, PyObject *kwnames)
{
    PyCodeObject *co = (PyCodeObject *)PyFunction_GET_CODE(func);

    // ...

    return _PyEval_EvalCodeWithName((PyObject*)co, globals, (PyObject *)NULL,
                                    stack, nargs,
                                    nkwargs ? _PyTuple_ITEMS(kwnames) : NULL,
                                    stack + nargs,
                                    nkwargs, 1,
                                    d, (int)nd, kwdefs,
                                    closure, name, qualname);
}
```
Отметим лишь два момента, первый, это получение объекта кода, о котором мы говорили ранее, и второе, создание и исполнение (evaluation) нового фрейма с телом нашей функции.



### Аргументы _vs_ параметры

**Параметром** функции называется переменная, которая будет связана с переданным в функцию значением. **Аргументом** функции называется переменная (или выражение), значение которой используется при вызове функции:
```python
def minimum(a, b)
            ^  ^
       параметры функции

a, b = 1, 2
minimum(a, b)
        ^  ^
   аргументы функции
```
Обычно параметры называют просто аргументами.

### Виды аргументов

При вызове функции мы можем передать аргументы как позиционные, в таком случае важен порядок следования аргументов:
```python
>>> minimum(4, 5)
4
>>> dis.dis("minimum(4, 5)")
  1           0 LOAD_NAME                0 (minimum)
              2 LOAD_CONST               0 (4)
              4 LOAD_CONST               1 (5)
              6 CALL_FUNCTION            2
              8 RETURN_VALUE
```
Также мы можем передать аргументы как именованные, в этом случае не имеет значения в каком порядке мы их указываем:

```python
>>> minimum(b=4, a=5)
4
>>> dis.dis("minimum(b=4, a=5)")
  1           0 LOAD_NAME                0 (minimum)
              2 LOAD_CONST               0 (4)
              4 LOAD_CONST               1 (5)
              6 LOAD_CONST               2 (('b', 'a'))
              8 CALL_FUNCTION_KW         2
             10 RETURN_VALUE
```
И, наконец, мы можем использовать смешанный вариант передачи аргументов:

```python
>>> minimum(5, b=4)
4
>>> dis.dis("minimum(2, b=1)")
  1           0 LOAD_NAME                0 (minimum)
              2 LOAD_CONST               0 (5)
              4 LOAD_CONST               1 (4)
              6 LOAD_CONST               2 (('b',))
              8 CALL_FUNCTION_KW         2
             10 RETURN_VALUE
```

Чтобы определить функцию, которая будет принимать любое количество позиционных аргументов, нужно использовать аргумент со звёздочкой (*argument):

```python
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))
```
`rest` - это кортеж всех дополнительных позиционных аргументов.

><span style='font-size:20px;color:lawngreen;'> 📝Примечание:</span>
>
> Аргумент со * может быть только последним в списке позиционных аргументов в определении функции.
> Аргумент с ** может идти только в последним.
><br> Тонкость в том, что аргумент без звёздочки может идти и после аргумента со звёздочкой
>```python
>def test(x, *args, y, **kwargs):
>    pass
>```
> Такие аргументы известны, как «обязательные именованные аргументы»


[**PEP 3102** — Keyword-Only Arguments](https://www.python.org/dev/peps/pep-3102/)
<br>Мы можем обязать передавать только именованные аргументы, указав после звёздочки нужные обязательные именованные аргументы:
```python
def recv(maxsize, *, block):
    """Receive a message"""
    pass
recv(1024, True)       # TypeError
recv(1024, block=True) # Ok
```
