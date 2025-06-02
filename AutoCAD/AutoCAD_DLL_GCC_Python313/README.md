# AutoCAD DLL with Python 3.13 and GCC (MinGW)

## 구성 파일
- `acad_control.py`: AutoCAD 객체를 제어하는 Python 스크립트
- `acad_wrapper.c`: Python 스크립트를 호출하는 DLL C 코드
- `compile.bat`: MinGW로 DLL 빌드
- `vba_example.bas`: DLL을 호출하는 Excel VBA 예제

## 빌드 방법
1. Python 3.13 설치
2. `pip install pyautocad pywin32`
3. `compile.bat` 실행

## VBA 호출
VBA 편집기에서 `vba_example.bas` 내용 복사 → DLL 경로 수정 후 실행