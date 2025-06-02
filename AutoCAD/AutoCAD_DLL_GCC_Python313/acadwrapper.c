#include <windows.h>
#include <stdio.h>

__declspec(dllexport)
int __stdcall DrawAutoCAD()
{
    STARTUPINFO si = { sizeof(STARTUPINFO) };
    PROCESS_INFORMATION pi;
    DWORD exitCode = 0;

    // 명령줄: python 실행 (절대경로 사용 권장)
    const char *cmd = "python D:/work/test_Python/AutoCAD/AutoCAD_DLL_GCC_Python313/run_autocad.py";

    if (!CreateProcessA(
        NULL,
        (LPSTR)cmd,
        NULL, NULL, FALSE,
        CREATE_NO_WINDOW, NULL, NULL,
        &si, &pi))
    {
        return -9999;
    }

    // 실행 대기
    WaitForSingleObject(pi.hProcess, INFINITE);
    GetExitCodeProcess(pi.hProcess, &exitCode);
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);
/*
    // 결과 파일 읽기
    FILE *f = fopen("D://work//test_Python//AutoCAD//AutoCAD_DLL_GCC_Python313//acad_result.txt", "r");
    if (!f) return -8888;
*/
    //int result = -7777;
    int result = 1;
/*    
    fscanf(f, "%d", &result);
    fclose(f);
*/
    return result;
}