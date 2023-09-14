#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
	long int s;
	int i;
	char *str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &str, &s);

	printf("  size: %li\n", s);
	printf("  trying string: %s\n", str);
	if (s < 10)
		printf("  first %li bytes:", s + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= s && i < 10; i++)
		printf(" %02hhx", str[i]);
	printf("\n");
}

void print_python_list(PyObject *p)
{
        long int s = PyList_Size(p);
        int i;
        PyListObject *l = (PyListObject *)p;
        const char *t;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", s);
        printf("[*] Allocated = %li\n", l->allocated);
        for (i = 0; i < s; i++)
        {
                t = (l->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, t);
                if (!strcmp(t, "bytes"))
                        print_python_bytes(l->ob_item[i]);
        }
}
