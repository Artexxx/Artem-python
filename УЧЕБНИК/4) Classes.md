### Создание экземпляра класса

Давайте немного остановимся на том как создаются новые экземпляры класса:

```python
class TestClass(object):
    def f1(self, val):
        return val
    
>>> dis.dis("temp = C()")
  1           0 LOAD_NAME                0 (C)
              2 CALL_FUNCTION            0
              4 STORE_NAME               1 (temp)
              6 LOAD_CONST               0 (None)
              8 RETURN_VALUE
```

Итак, на стек помещается класс `TestClass`, и затем выполняется инструкция `CALL_FUNCTION`:

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

    assert((x != NULL) ^ (_PyErr_Occurred(tstate) != NULL));

    /* Clear the stack of the function object. */
    while ((*pp_stack) > pfunc) {
        w = EXT_POP(*pp_stack);
        Py_DECREF(w);
    }

    return x;
}
```
Произойдёт вызов функции `_PyObject_Vectorcall` ([PEP 590](https://www.python.org/dev/peps/pep-0590/)):
```c
static inline PyObject *
_PyObject_Vectorcall(PyObject *callable, PyObject *const *args,
                     size_t nargsf, PyObject *kwnames)
{
    assert(kwnames == NULL || PyTuple_Check(kwnames));
    assert(args != NULL || PyVectorcall_NARGS(nargsf) == 0);
    vectorcallfunc func = _PyVectorcall_Function(callable);
    if (func == NULL) {
        Py_ssize_t nargs = PyVectorcall_NARGS(nargsf);
        return _PyObject_MakeTpCall(callable, args, nargs, kwnames);
    }
    PyObject *res = func(callable, args, nargsf, kwnames);
    return _Py_CheckFunctionResult(callable, res, NULL);
}
```
```c
PyObject *
_PyObject_MakeTpCall(PyObject *callable, PyObject *const *args, Py_ssize_t nargs, PyObject *keywords)
{
    /* Slow path: build a temporary tuple for positional arguments and a
     * temporary dictionary for keyword arguments (if any) */
    ternaryfunc call = Py_TYPE(callable)->tp_call;

    // ...

    PyObject *result = NULL;
    if (Py_EnterRecursiveCall(" while calling a Python object") == 0)
    {
        result = call(callable, argstuple, kwdict);
        Py_LeaveRecursiveCall();
    }

    // ...

    result = _Py_CheckFunctionResult(callable, result, NULL);
    return result;
}
```
Макрос `PY_TYPE` возвращает тип объекта.
Уже упоминалось, что классы также являются объектами, а следовательно и у них есть тип, другими словами, есть классы, которые порождают другие классы и называются они метаклассами (иногда встречается термин «метатип»):

```c 
>>> type(User)
<class 'type'>
```
По умолчанию метаклассом для всех классов является класс [`type`](https://github.com/python/cpython/blob/3.8/Objects/typeobject.c#L3607), только если мы явно не указали другой метакласс.
Также отметим, что все типы в виртуальной машине CPython представлены структурой [`PyTypeObject`](https://docs.python.org/3/c-api/typeobj.html), содержащей по большей части указатели на функции (слоты), которые определяют поведение объекта.
Таким образом, в листинге выше происходит обращение к слоту `tp_call`, который по умолчанию содержит указатель на функцию `type_call`:

```c hl_lines="2 3"
static PyObject *
type_call(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    PyObject *obj;

    // ...
    obj = type->tp_new(type, args, kwds);
    obj = _Py_CheckFunctionResult((PyObject*)type, obj, NULL);
    if (obj == NULL)
        return NULL;

    // ...
    /* If the returned object is not an instance of type,
       it won't be initialized. */
    if (!PyType_IsSubtype(Py_TYPE(obj), type))
        return obj;

    type = Py_TYPE(obj);
    if (type->tp_init != NULL) {
        int res = type->tp_init(obj, args, kwds);
        // ...
    }
    return obj;
}
```

```python hl_lines="5 6 7 8 9 10 16 23 24 25"
import os, sys, re

REGEX_HL_LINE = re.compile(r".*?hl_lines=\"(?P<hl_lines>.*?)\"")
HL_LINE_SPACES = 2


def format_directory(dir_path):
    for file_path in [os.path.join(dp, f) for dp, dn, filenames in os.walk(dir_path) for f in filenames if os.path.splitext(f)[1] == '.md']: format_file(file_path)


def format_file(file_path):
    has_changed = False
    with open(file_path, "r") as stream:
        md_lines = stream.readlines()        
    for index, line in enumerate(md_lines):
        hl_lines = get_hl_lines(line)
        if not hl_lines:
            continue
        hl_lines_numbers = parse_hl_lines(hl_lines)
        formated_hl_lines_numbers = format_hl_lines(hl_lines_numbers)
        new_line = replace_hl_lines(line, formated_hl_lines_numbers)
        md_lines[index] = new_line
        has_changed = True
    if has_changed:
        with open(file_path, "w+") as stream:
            md_lines = stream.writelines(md_lines)


def get_hl_lines(line):
    match = REGEX_HL_LINE.match(line)
    return match.group("hl_lines") if match else ""


def parse_hl_lines(hl_lines):
    result = []
    for item in hl_lines.split(" "):
        if not item:  # handle empty string from split
            continue
        if "-" in item:  # handle range
            range_item_min, range_item_max = item.split("-")
            if int(range_item_min) >= int(range_item_max):
                raise ValueError
            items = [i for i in range(int(range_item_min), int(range_item_max)+1)]
            result += items
            continue
        result.append(int(item))  # handle simple number
    result.sort()
    return result

```
