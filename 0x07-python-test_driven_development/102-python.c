#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - prints Python strings
 * @p: Python Object
 * Return: no return
 */
void print_python_string(PyObject *p)
{
    PyObject *str, *repr;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }
    if (PyUnicode_IS_COMPACT_ASCII(p))
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");
    printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
    repr = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
    if (repr != NULL)
    {
        printf("  value: %s\n", PyBytes_AsString(repr));
        Py_DECREF(repr);
    }
    else
    {
        printf("  [ERROR] Unable to encode string\n");
    }
}
