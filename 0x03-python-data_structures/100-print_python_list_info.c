#include <Python.h>
#include <listobject.h>

void print_python_list_info(PyObject *p) 
{
    if (!PyList_Check(p)) {
        PyErr_SetString(PyExc_TypeError, "Expected a list!");
        return;
    }
    
    long int size = PyList_Size(p);
    
    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);
    
    for (int j = 0; j < size; j++) {
        printf("Element %i: %s\n", j, PyList_GetItem(p, j)->ob_type->tp_name);
    }
}
