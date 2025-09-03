# Blender Python API

https://docs.blender.org/api/current/index.html  

Extensions Tutorial  
https://docs.blender.org/manual/en/latest/advanced/extensions/getting_started.html  

Addon Tutorial  
https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html  

---

YouTube Tutorial  
https://youtu.be/wWTAQP7-ZUQ (Blender)  

https://www.youtube.com/@CGPython  
https://youtu.be/YUytEtaVrrc (VScode Setup)  
https://youtu.be/0_QskeU8CPo (Panel Demo)  

https://youtube.com/playlist?list=PLRKZHg6r5mu42davqG2wUl_P-JDgJTaus (Curtis Holt)  

https://www.youtube.com/@DarkfallBlender  

---

## Blender Scripting Workspace

In Preferences > Interface > Python Tooltips enable  
In Preferences > Interface > Developer Extras enable  

## Installing Modules
https://youtu.be/k1gCIezKA8E?t=121  
inside Blenders Scripting Workspace (interactive console):  
```
bpy.utils.user_resource("SCRIPTS", path="modules")
```
```Bash
pip install <library> --target=""  
```

## Development Tools  

https://developer.blender.org/docs/handbook/extensions/addon_dev_setup/  

### IDE VScode  

https://developer.blender.org/docs/handbook/development_environments/vscode/  

Blender Development Extension  
https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development  
Installs modules in Blender for Debugging;  
N-Panel > Dev:  
- Blender at Port 7993
- debugpy at Port 5428
- Editor at http://localhost:61762  

Setup  
Give write Permissions to Python Directory inside Blender Installation Path.  
https://youtu.be/YUytEtaVrrc?t=501  
Ctrl + Shift + P (Command Palette) > Blender: Start (Choose Blender.exe)  

Usage  
Ctrl + Shift + P (Command Palette) > Blender: Run Script  

Fake-bpy Module  
https://github.com/nutti/fake-bpy-module  
https://pypi.org/project/fake-bpy-module/  
```Bash
.venv/Scripts/activate
pip install fake-bpy-module
```
```Python
import bpy
"""automatically uses fake-bpy in VScode and works in Blender"""
```

### Numpy-STL
https://numpy-stl.readthedocs.io/en/latest/

---

## bpy.types.Panel
https://docs.blender.org/api/current/bpy.types.Panel.html

bl_space_type = "VIEW_3D"  
https://docs.blender.org/api/current/bpy_types_enum_items/space_type_items.html#rna-enum-space-type-items

bl_region_type = "UI"  
https://docs.blender.org/api/current/bpy_types_enum_items/region_type_items.html#rna-enum-region-type-items

```python
class VIEW3D_PT_my_custom_panel(bpy.types.Panel):  # class naming convention ‘CATEGORY_PT_name’

    # where to add the panel in the UI
    bl_space_type = "VIEW_3D"  # 3D Viewport area (find list of values here https://docs.blender.org/api/current/bpy_types_enum_items/space_type_items.html#rna-enum-space-type-items)
    bl_region_type = "UI"  # Sidebar region (find list of values here https://docs.blender.org/api/current/bpy_types_enum_items/region_type_items.html#rna-enum-region-type-items)

    # add labels
    bl_category = "My Custom Panel category"  # found in the Sidebar
    bl_label = "My Custom Panel label"  # found at the top of the Panel

    def draw(self, context):
        """define the layout of the panel"""
        row = self.layout.row()
        row.operator("mesh.primitive_cube_add", text="Add Cube")
        row = self.layout.row()
        row.operator("mesh.primitive_ico_sphere_add", text="Add Ico Sphere")
        row = self.layout.row()
        row.operator("object.shade_smooth", text="Shade Smooth")

        self.layout.separator()

        row = self.layout.row()
        row.operator("mesh.add_subdiv_monkey", text="Add Subdivided Monkey")
```

---

## bpy.types.Operator
https://docs.blender.org/api/current/bpy.types.Operator.html

```python
class MESH_OT_add_subdiv_monkey(bpy.types.Operator):
    """Create a new monkey mesh object with a subdivision surf modifier and shaded smooth"""

    bl_idname = "mesh.add_subdiv_monkey"
    bl_label = "Add Subdivided Monkey Mesh Object"
    bl_options = {"REGISTER", "UNDO"}

    mesh_size: bpy.props.FloatProperty(
        name="Size",
        default=4.0,
        description="The size of the monkey",
    )

    def execute(self, context):

        add_subdiv_monkey_obj(self.mesh_size, self.subdiv_viewport_lvl, self.subdiv_render_lvl, self.shade_smooth)

        return {"FINISHED"}
```

---

