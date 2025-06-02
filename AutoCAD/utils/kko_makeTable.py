# 엑셀에서 Data 읽어와서 캐드 표 만드는 코드

import win32com.client
import pythoncom
import openpyxl
import os
import sys
import time

# AutoCAD 포인트 및 배열 생성 헬퍼
def APoint(x, y, z=0):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (x, y, z))

def aDouble(*xyz):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, xyz)

# 배경색 설정 함수 (RGB -> BGR 정수 변환)
def rgb_to_bgr_int(r, g, b):
    return b * 65536 + g * 256 + r

# 문자열의 좌측에서 n개 문자만 가져오는 함수는 아래와 같이 작성할 수 있습니다:
def left(s: str, n: int) -> str:
    return s[:n]

def create_acad_color(acad_app, r, g, b):
    """AutoCAD 색상 객체 (IAcadAcCmColor)를 생성하여 반환"""
    color = acad_app.ActiveDocument.Application.GetInterfaceObject("AutoCAD.AcCmColor.", left(acad_app.ActiveDocument.Application.Version, 2))
    #color = acad_app.ActiveDocument.Application.GetInterfaceObject("AutoCAD.AcCmColor.20")
    color.SetRGB(r, g, b)
    return color

# 엑셀 파일 읽기
def read_excel_data(file_path: str, sheet_name: str = None) -> list:
    if not os.path.exists(file_path):
        print(f"❌ 엑셀 파일 없음: {file_path}")
        sys.exit(1)
    try:
        wb = openpyxl.load_workbook(file_path, data_only=True)
        sheet = wb[sheet_name] if sheet_name else wb.active
        data = []
        for row in sheet.iter_rows(values_only=True):
            if any(cell is not None for cell in row):
                data.append(list(row))
        return data
    except Exception as e:
        print(f"🚫 엑셀 읽기 오류: {e}")
        sys.exit(1)

# AutoCAD 연결
def connect_autocad():
    try:
        acad = win32com.client.GetActiveObject("AutoCAD.Application")
    except:
        acad = win32com.client.Dispatch("AutoCAD.Application")
        acad.Visible = True
        time.sleep(3)
    return acad

# 테이블 그리기
def draw_table(acad_app, data: list, insert_point=(0, 0, 0), row_height=5, column_width=30):
    if not data or not data[0]:
        print("❌ 유효한 데이터 없음.")
        return

    doc = acad_app.ActiveDocument
    ms = doc.ModelSpace

    insert_point = APoint(*insert_point)
    rows = len(data)
    cols = max(len(row) for row in data)

    try:
        table = ms.AddTable(insert_point, rows+2, cols, row_height, column_width)
        table.StyleName = "Standard"
        #table.StyleName = "acDataRow"
        
        # 👉 타이틀, 헤더 숨기기 (acDataRow 형태)
        #table.HasTitle = False
        #table.HasHeader = False
        #table.TitleSuppressed = True       # 타이틀 숨기기 (AutoCAD 2022 이상)
        #table.HeaderSuppressed = True     # 헤더 숨기기 (AutoCAD 2022 이상)
        #table.SetRowHeight(0, 0.001)
        #table.SetRowHeight(1, 0.001)
        #table.SetText(0, 0, "")
        #table.SetText(1, 0, "")
        
        # Title/Header 제거 (AutoCAD 2021 이상에서 가능)
        try:
            table.DeleteRows(0, 2)
        except:
            print("⚠️ Title/Header 행 제거 실패 (버전 또는 라이선스 제한)")

        table.Direction = aDouble(1, 0, 0)  # 방향: 오른쪽으로

        for r in range(rows):
            for c in range(cols):
                value = data[r][c] if c < len(data[r]) else ""
                #table.SetCellStyle(r, c, 1)
                table.SetText(r+2-2, c, str(value))

                # 정렬 설정 : 1/2/3/4/5/6/7/8/9 = acTopLeft / acTopCenter / acTopRight / acMiddleLeft / acMiddleCenter / acMiddleRight / acBottomLeft / acBottomCenter / acBottomRight
                table.SetCellAlignment(r+2-2, c, 5)
                ##table.SetTextHeight(r, c, 3.0)      # 텍스트 높이
                ##lngContent = table.CreateContent(r, c, r * 10000 + c)
                ##table.SetTextHeight2(r, c, lngContent, 1000.0)      # 텍스트 높이
                table.SetCellTextHeight(r+2-2, c, 2)
                

                # 헤더 배경색 설정 (첫 행)
                if r == 0:
                    ##yellow_bgr = rgb_to_bgr_int(255, 255, 200)                
                    ##yellow_bgr = create_acad_color(acad, 255, 255, 200)                
                    color = table.GetCellBackgroundColor(r+2-2, c)
                    color.SetRGB(255, 255, 200)
                    #table.SetCellBackgroundColor(r, c, color)  # 밝은 노랑 (RGB 255, 255, 200)

        print("✅ AutoCAD 테이블 생성 완료")

    except Exception as e:
        print(f"🚫 테이블 생성 오류: {e}")

"""
# 메인 실행부
if __name__ == "__main__":
    pythoncom.CoInitialize()

    excel_file = r"D:\work\makeTable.xlsx"
    print(f"📄 엑셀 파일 확인 중: {excel_file}")

    data = read_excel_data(excel_file)
    acad = connect_autocad()
    draw_table(acad, data)

    pythoncom.CoUninitialize()
"""