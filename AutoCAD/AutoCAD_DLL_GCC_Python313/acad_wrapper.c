#include <Python.h>
#include <windows.h>
#include <stdio.h>

//static int is_initialized = 0;

void write_object_to_file(PyObject *obj, const char *filename) {
    FILE *fp = fopen(filename, "w");
    if (fp == NULL) {
        printf("🚫 파일 열기 실패: %s\n", filename);
        return;
    }

    if (obj == NULL) {
        fprintf(fp, "❌ PyObject == NULL\n");
    } else {
        PyObject_Print(obj, fp, 0);  // Python 객체의 문자열 표현 출력
        fprintf(fp, "\n");

        // UTF-8 문자열로 출력 (문자열 객체인 경우)
        if (PyUnicode_Check(obj)) {
            const char *utf8 = PyUnicode_AsUTF8(obj);
            if (utf8 != NULL) {
                fprintf(fp, "UTF-8 값: %s\n", utf8);
            } else {
                fprintf(fp, "❌ PyUnicode_AsUTF8 실패\n");
                PyErr_Print();  // 에러 추적
            }
        }
    }

    fclose(fp);
}

__declspec(dllexport)
int __stdcall DrawAutoCAD()
{    
    // 메인 인터프리터를 사용하지 않고, 서브 인터프리터 생성
    Py_Initialize();
    PyThreadState *mainThreadState = PyThreadState_Get();
    PyThreadState *subThreadState = Py_NewInterpreter();

    if (subThreadState == NULL) {
        Py_Finalize();
        return -9999;  // 서브 인터프리터 생성 실패
    }

    // 해당 서브 인터프리터에서 sys.path 설정
    //PyRun_SimpleString("import sys");
    //PyRun_SimpleString("sys.path.append('.')");

    //PyObject *pName = PyUnicode_FromString("acad_control");
    //PyObject *pModule = PyImport_Import(pName);
    //Py_DECREF(pName);

    int result = -11111;

    //Py_Initialize();
    //if (!is_initialized) {
    //    Py_Initialize();
    //    is_initialized = 1;
    //}

    PyRun_SimpleString("import sys");
    //PyRun_SimpleString("sys.path.append('.')");
    //PyRun_SimpleString("sys.path.append('D://work//test_Python//AutoCAD//AutoCAD_DLL_GCC_Python313')");
    PyRun_SimpleString("sys.path.append('D://work//test_Python//AutoCAD//AutoCAD_DLL_GCC_Python313//__pycache__')");
    PyObject *pName = PyUnicode_FromString("acad_control");
    PyObject *pModule = PyImport_Import(pName);
    Py_DECREF(pName);    
    if (pModule != NULL) {
        PyObject *pFunc = PyObject_GetAttrString(pModule, "run_draw_and_zoom");
        if (pFunc && PyCallable_Check(pFunc)) {
            PyObject *pResult = PyObject_CallObject(pFunc, NULL);
            if (pResult != NULL) {
                //int result = (int)PyLong_AsLong(pResult);
                result = (int)PyLong_AsLong(pResult);
                Py_DECREF(pResult);
                //Py_Finalize();
                //return result;
                //return 222222;
            }
            Py_XDECREF(pFunc);
        }
        Py_DECREF(pModule);
    }
    else
    {
        //PyObject_Print(pName, stdout, 0);
        //printf("\n");
        //printf("🚫 PyImport_Import 실패: acad_control 모듈 로드 실패\n");
        //PyErr_Print();  // 반드시 출력해야 원인 확인 가능                 
        //write_object_to_file(PyRun_SimpleString("sys.path.append('.')"), "D:/work/test_Python/AutoCAD/AutoCAD_DLL_GCC_Python313/pname_debug.txt");
        write_object_to_file(pName, "D://work//test_Python//AutoCAD//AutoCAD_DLL_GCC_Python313//pname_debug.txt");
        //return -55555555;    
        result =-55555555;    
    }    

    Py_EndInterpreter(subThreadState);
    PyThreadState_Swap(mainThreadState);    
    Py_Finalize();
    //return -1111;    
    return result;    
}