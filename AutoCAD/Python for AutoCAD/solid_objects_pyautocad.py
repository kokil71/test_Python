# https://www.supplychaindataanalytics.com/solid-objects-in-autocad-using-pyautocad-python/
# Solid AutoCAD objects in pyautocad (Python)

import pythoncom
import win32gui
import win32com.client
import time
from pyautocad import Autocad, APoint, aDouble
#from math import pi

def connect_autocad():
    try:
        # 실행 중인 AutoCAD 인스턴스에 연결
        acad_app = win32com.client.GetActiveObject("AutoCAD.Application")        
        #print("✅ AutoCAD 실행 중입니다.")
        return Autocad(create_if_not_exists=False)          # pyautocad 연결
    except Exception:
        #print("❌ 실행 중인 AutoCAD 없음. 새 인스턴스를 시작합니다.")
        try:
            acad_app = win32com.client.Dispatch("AutoCAD.Application")
            #acad_app.Visible = True
            time.sleep(3)  # 로딩 대기
            #print("✅ 새 AutoCAD 인스턴스 시작 완료.")
            return Autocad(create_if_not_exists=False)      # pyautocad 연결
        except Exception as e:
            print("🚫 AutoCAD 연결 실패:", e)
            return None
    finally:
        hwnd = win32gui.FindWindow(None, acad_app.Caption)
        bring_autocad_to_front(hwnd)      

def bring_autocad_to_front(hwnd):
    try:
        #acad = win32com.client.GetActiveObject("AutoCAD.Application")
        #hwnd = win32gui.FindWindow(None, acad.Caption)
        if hwnd:
            win32gui.ShowWindow(hwnd, 5)  # SW_SHOW
            win32gui.SetForegroundWindow(hwnd)
            #print("✅ AutoCAD 창을 전면으로 전환 완료.")
        else:
            print("❌ AutoCAD 창을 찾을 수 없습니다.")
    except Exception as e:
        print("🚫 오류:", e)

def draw_and_zoom(acad):    
    if acad is None:
        print("AutoCAD 연결이 안 되어 종료합니다.")
        return

    # Understanding the basics of solid AutoCAD objects
    # In AutoCAD, we have different solid objects, e.g. box, cone, cylinder, sphere, etc. and each one of them has object-specific methods to create those individual objects.
    # But unlike the basic geometrical objects such as lines, polylines, circles, arcs, etc., to find the properties of the objects, we have a common set of methods that shall be used for all sorts of solid objects.
    # To make this clearer, we will start exploring solid objects.

    # Writing Python code for solid AutoCAD objects using pyautocad
    # In this blog post I will talk about some basic solid objects i.e. box, cone, cylinder, elliptical cone, elliptical cylinder, sphere, torus and wedge.
    # Each individual of the above-mentioned objects has its own methods to create those objects according to their respective geometrical properties.
    # I will mention the parameters to be passed with each of the commands that we will use for respective objects:
    # Box: (Origin/Center, Length, Width, Height)
    box = acad.model.AddBox(APoint(0, 0, 0), 1000, 1200, 750)
    # Cone: (Center, Base radius, Height)
    cone = acad.model.AddCone(APoint(2000, 0, 0), 750, 800)
    # Cylinder: (Center, Radius, Height)
    cyl =  acad.model.AddCylinder(APoint(3200, 0, 0), 350, 1250)
    # Elliptical Cone: (Center, MajorRadius, MinorRadius, Height)
    econe =  acad.model.AddEllipticalCone(APoint(4000, 500 , 0), 450, 225, 1275.62)
    # EllipticalCylinder: (Center, MajorRadius, MinorRadius, Height)
    ecyl =  acad.model.AddEllipticalCylinder(APoint(1500, 2000 , 0), 750, 400, 950)
    # Sphere: (Center, Radius)
    sph = acad.model.AddSphere(APoint(2500, 3500, 0), 250)
    # Torus: (Center, TorusRadius, TubeRadius)
    tor = acad.model.AddTorus(APoint(1000, 4000, 0), 500, 100)
    # Wedge: (Center, Length, Width, Height)
    wed = acad.model.AddWedge(APoint(2000, 5000, 0), 1000, 1200, 750)  

    # Properties of solid objects
    # It is because the solid objects are a collection of polylines resulting in a solid object, the solid object has a similar set of properties that can be fetched using similar methods.
    # For example, we have methods to find the radius of gyration, the moment of inertia, volume, etc. and each object type possesses these properties.
    # Let us implement these methods against the box we have created and fetch the properties.
    print("Volume of box: " + str(box.Volume))
    print("Centroid of box: " + str(box.Centroid))
    print("Moment of Inertia of box: " + str(box.MomentOfInertia))
    print("Product of inertia of box: " + str(box.ProductOfInertia))
    print("Principal directions of box: " + str(box.PrincipalDirections))
    print("Principal moments of box: " + str(box.PrincipalMoments))
    print("Radius of giration of box: " + str(box.RadiiOfGyration))

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()