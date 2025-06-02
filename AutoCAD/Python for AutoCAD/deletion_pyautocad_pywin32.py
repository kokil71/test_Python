# https://www.supplychaindataanalytics.com/deleting-objects-in-a-autocad-template-with-pyautocad-pywin32-python/
# pyautocad/pywin32 AutoCAD object deletion

"""

# Deleting objects using pyautocad
# Setting up environment for pyautocad
# As usual, we will set up our environment for integrating python with AutoCAD.
from pyautocad import Autocad

acad = Autocad(create_if_not_exists=True)

# Using delete method provided by pyautocad
# Now we will use a very simple utility of pyautocad called iter_objects(), to loop through every object from the template.
#for object in acad.iter.objects()
#      object.Delete()
# Filtering out objects for deletion using pyautocad
# Sometimes we need to filter our objects before deleting i.e. suppose if we want to delete only the circle from the template as shown in Figure 1, then we can use the following methodology.
#for object in acad.iter_objects(object_name_or_list="AcDbCircle"):
for i in acad.iter_objects_fast(object_name_or_list="AcDbCircle"):
    object.Delete()

#for i in acad.iter_objects_fast(object_name_or_list="AcDbPolyline"):

"""

# Deleting objects using pywin32 (win32com.client)
# Setting up environment for pywin32
# As we have discussed initiating an AutoCAD template using pywin32 in our previous blog, we will set up our work environment to integrate python and AutoCAD.
import win32com.client

acad = win32com.client.Dispatch("AutoCAD.Application")

acad.Visible = True
acadModel = acad.ActiveDocument.ModelSpace  

#Deleting objects from AutoCAD template using pywin32
# While using pywin32, we have a very direct approach to code for iterating through objects from the AutoCAD template.
#for object in acadModel:
#      object.Delete()

#Filtering objects for deletion while working with pywin32
#Filtering out objects while using pywin32 takes just an “if statement”. Let’s look at the same.
for object in acadModel:
    if object.ObjectName == "AcDbCircle":
        object.Delete()