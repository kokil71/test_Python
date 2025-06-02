import sys
sys.path.append("D:\\work\\testPythonToAutoCAD")  # 경로는 본인의 폴더에 맞게 수정

#from mymodule import MyClass  # mymodule.py 안의 MyClass
from AutoCAD import *  # mymodule.py 안의 MyClass

# Create the AutoCAD object
acad = AutoCAD()

# Draw a Line
# Define start and end points using APoint
start_point = APoint(0, 0, 0)
end_point = APoint(100, 100, 0)

# Draw the line
acad.add_line(start_point, end_point)

# Draw a Circle
# Define the center point and radius
center = APoint(50, 50, 0)
radius = 25

# Draw the circle
acad.add_circle(center, radius)

# Draw an Ellipse
# Define the center point and major axis
center = APoint(75, 75, 0)
major_axis = APoint(50, 0, 0)
ratio = 0.5  # Minor axis ratio

# Draw the ellipse
acad.add_ellipse(center, major_axis, ratio)

# Draw a Rectangle
# Define lower left and upper right corners
lower_left = APoint(10, 10, 0)
upper_right = APoint(60, 40, 0)

# Draw the rectangle
acad.add_rectangle(lower_left, upper_right)

# Add Text
# Define the text content, insertion point, and height
text_content = "Hello AutoCAD"
insertion_point = APoint(20, 20, 0)
text_height = 5

# Create and add the text
text = Text(text_content, insertion_point, text_height)
acad.add_text(text)

# Repeat block horizontally
# Repeat the "blockname" block horizontally
total_length = 100  # Total length X
block_length = 10  # Length of the block "blockname"
insertion_point = APoint(0, 0, 0)  # Initial insertion point

# Execute the block repetition
#acad.repeat_block_horizontally("blockname", total_length, block_length, insertion_point)

# Set the visibility of a layer
#acad.set_layer_visibility("Linea di mezzeria", visible=False)

# Lock a layer
#acad.lock_layer("Quote", lock=True)

# Delete a layer
#acad.delete_layer("Simboli")

# Change the color of a layer
#acad.change_layer_color("Contorni", Color.YELLOW)

# Set the linetype of a layer
#acad.set_layer_linetype("Assi", "DASHED")

# Select objects
#selected_objects = acad.select_objects(object_type="AcDbLine", layer_name="Contorni")
#print(f"Selected objects: {len(selected_objects)}")

# Move, scale, and rotate objects
#for obj in selected_objects:
#    acad.move_object(obj, APoint(10, 10, 0))
#    acad.scale_object(obj, APoint(0, 0, 0), 2)
#    acad.rotate_object(obj, APoint(0, 0, 0), 45)

# Align and distribute objects
#acad.align_objects(selected_objects, alignment="left")
#acad.distribute_objects(selected_objects, spacing=5)

# Insert a block from a file
#acad.insert_block_from_file("path_to_file.dwg", APoint(0, 0, 0))

# Export a block to a file
#acad.export_block_to_file("piatto", "path_to_export.dwg")

# Modify block attributes
block_references = acad.get_block_coordinates("piatto")
if block_references:
    block_ref = block_references[0]  # Get the first found block
    acad.modify_block_attribute(block_ref, "Tag", "NewValue")

# Delete block attributes
#acad.delete_block_attribute(block_ref, "Tag")

# Request user input
#point = acad.get_user_input_point("Select a point")
text = acad.get_user_input_string("Enter a string")
integer = acad.get_user_input_integer("Enter an integer")

# Display a message to the user
acad.show_message("Operation completed")

# Create a group of objects
#group = acad.create_group("MyGroup", selected_objects)

# Add objects to a group
#acad.add_to_group("MyGroup", selected_objects)

# Remove objects from a group
#acad.remove_from_group("MyGroup", selected_objects)

# Select a group of objects
#group_items = acad.select_group("MyGroup")
#print(f"Objects in group 'MyGroup': {len(group_items)}")