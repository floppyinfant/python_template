# __init__.py

# ##### BEGIN GPL LICENSE BLOCK #####
#
#    Copyright (c) 2020 Elie Michel
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


"""
Blender Add-on Tutorial
https://docs.blender.org/manual/en/3.6/advanced/scripting/addon_tutorial.html
https://docs.blender.org/api/current/info_quickstart.html
https://docs.blender.org/api/current/info_tips_and_tricks.html#use-the-terminal

Blender Tools for Development:
Window > System Console                 # Python print() and error traceback output
Preferences > Interface > Developer Extras
https://docs.blender.org/manual/en/3.6/editors/preferences/interface.html#prefs-interface-dev-extras
--> Topbar Edit Menu > Operator Search  # bpy.ops.<bl_idname>
--> Button Context Menu > Online Python Reference
--> Preferences Experimental Tab
Preferences > Interface > Python Tooltips
Preferences > Add-ons > 'Development: Is Key Free' 
--> Text Editor > Sidebar (N) > Dev
Menu Help > Operator Cheat Sheet 
--> Text Editor > OperatorList.txt
Text Editor > Menu Templates            # Examples

Blender Python API
https://docs.blender.org/api/current/info_overview.html

Blender Developers
https://wiki.blender.org/wiki/Main_Page

UPBGE Python API
https://upbge.org/docs/latest/api//index.html

BGE (v2.79)
https://docs.blender.org/manual/en/2.79/game_engine/index.html

- - -

Setup Dev-Env Tutorial
https://youtu.be/YUytEtaVrrc (Setup VSCode on Windows, Victor Stapanovic / CG Python)

Install:
VSCode
https://code.visualstudio.com/
https://vscode.dev/ (Online Editor)
VSCode Extensions:
    Python Extension
    Blender Development Extension

Python
https://www.python.org/

Terminal:
pip install fake-bpy-module-latest
https://github.com/nutti/fake-bpy-module 

- - -

Alternatives:
Serpens (Node-based Development)
https://joshuaknauber.gumroad.com/l/serpens-b3d 
https://joshuaknauber.notion.site/Serpens-Documentation-d44c98df6af64d7c9a7925020af11233 (Serpens Documentation)

EasyBPY (by Curtis Holt)
https://curtisholt.online/easybpy
https://github.com/curtisjamesholt/EasyBPY/blob/master/easybpy.py

- - -

Usage:
Blender Development Extension:
https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development 
Ctrl + Shift + P		>Blender: Start (Choose Blender Executable…)
Give Write-Permissions to “Program Folder/<version>/Python” in Windows Explorer
Ctrl + Shift + P		>Blender: Run Script
"""


bl_info = {
    "name": "Blender Addon Template",
    "author": "floppy infant <make@floppyinfant.com>",
    "version": (0, 0, 1),
    "blender": (3, 50, 0),
    "location": "Properties > Scene",
    "description": "An example of add-on for Blender",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "TODO: https://github.com/",
    "support": "COMMUNITY",
    "category": "3D view",
}


import bpy
import mathutils

# Modules API Docs: https://docs.blender.org/api/current/index.html 
# bpy.context	// Pointers
# bpy.ops		// Operators
# bpy.props		// Operator Property types: int, float, vector, color, boolean, string
#                  These properties from bpy.props are handled specially by Blender 
#                  when the class is registered so they display as buttons in the user interface. 
#                  There are many arguments you can pass to properties to set limits, 
#                  change the default and display a tooltip.
# bpy.types
# bpy.data		// Collections
# bpy.msgbus	// Message Bus
# bpy.utils
# bpy.path
# bpy.app		// readonly constants
#
# aud			// Audio
# bgl			// OpenGL Wrapper
# blf			// Font
# bmesh
# bpy_extras
# freestyle
# gpu
# imbuf
# mathutils
# https://docs.blender.org/api/3.6/mathutils.html#mathutils.Vector
# https://docs.blender.org/api/3.6/mathutils.geometry.html


from math import radians
import random
import time

# TODO: delete; from 'AdvancedBlenderAddon'
from . import preferences
from . import properties
from . import operators
from . import panels
from . import overlays
from . import tools
from . import handlers

import os
# https://docs.blender.org/api/current/info_tips_and_tricks.html#executing-external-scripts
filename = os.path.join(os.path.dirname(bpy.data.filepath), "myscript.py")
exec(compile(open(filename).read(), filename, 'exec'))


# TODO: move any code to Operators class execute function
scene = bpy.context.scene
cursor = bpy.context.scene.cursor.location
obj = bpy.context.active_object

for obj in scene.objects:
    obj.location.x += 1.0


### operators ################################################################
# https://docs.blender.org/api/3.6/bpy.types.Operator.html
# https://docs.blender.org/api/3.6/bpy.ops.html
# Menu Help > Operator Cheat Sheet --> see Text Editor > OperatorList.txt

def render_settings(context):
    # TODO: code to be executed by the operator, e.g.:
    bpy.data.scenes['Scene'].render.engine = 'BLENDER_EEVEE'


class FI_OT_render_settings(bpy.types.Operator):
    """This string is used for the tooltip and API docs."""

    bl_idname = "render.render_settings"    # bpy.ops.render.render_settings('INVOKE_DEFAULT')
                                            # for direct invocation
    bl_label = "Render Settings"            # search for it in Operator Search Menu
    bl_options = {'REGISTER', 'UNDO'}


    # Blender Properties
    x: bpy.props.IntProperty()
    y: bpy.props.IntProperty()
    noise_scale : bpy.props.FloatProperty(
        name = "Noise Scale",
        description = "The scale of the noise",
        default = 1.0,
        min = 0.0,
        max = 2.0
    )


    def execute(self, context):
        """test call: bpy.ops.<bl_idname>('EXEC_DEFAULT', x=2, y=5)"""
        render_settings(context)
        # the report message appears in the header:
        self.report({'INFO'}, "Mouse coords are %d %d" % (self.x, self.y))
        return {'FINISHED'}
    

    def invoke(self, context, event):
        """https://docs.blender.org/api/3.6/bpy.types.Operator.html"""
        self.x = event.mouse_x
        self.y = event.mouse_y
        return self.execute(context)
    

    @classmethod
    def poll(cls, context):
        return context.object is not None


### UI panels ################################################################
# https://docs.blender.org/api/3.6/bpy.types.Menu.html
# https://docs.blender.org/api/3.6/bpy.types.Panel.html

# add to Menu:
# Topbar Editor Menus: TOPBAR_MT...
# View3D Editor Menus: VIEW3D_MT...
# Side (N)-Panel
# Object Context Menu (Viewport)
# Pie-Menu
# Quick-Menu
#
# add to Header:
# Topbar Ht Upper Bar
# View3D Ht Header [or any other View Header]
# View3D Ht Tool Header: VIEW3D_PT_tools...
# Statusbar Ht Header
# 
# add to Panel:
# Properties Navigation Bar
# Properties Window, Properties Window Object (e.g. Object Transforms)
# Toolbar (T): View3D Tools Active

class FI_PT_pixel_render_panel(bpy.types.Panel):
    """Creates a Panel for Pixel Rendering in the UI Panels"""

    bl_label = "Pixel Render"
    bl_idname = "PIXEL_RENDER_PT_pixel_render_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Pixel Render"


    def draw(self, context):
        layout = self.layout
        scene = context.scene     
        
        box = layout.box()
        row = box.row()
        row.alignment = 'CENTER'          
        row.label(text="Render Settings for Pixel Art", icon = "RESTRICT_RENDER_OFF")
        row = box.row()
        row = box.row()
        row.scale_y = 1.5
        row.operator("render.render_settings")


### register classes by factory ##############################################

classes = (
    FI_PT_pixel_render_panel,
)
# register, unregister = bpy.utils.register_classes_factory(classes)


### register classes one-by-one ##############################################

# Keymaps (Shortcuts)
# https://docs.blender.org/manual/en/3.6/advanced/scripting/addon_tutorial.html#keymap
# add-on "Development: Is Key Free": Text Editor > Sidebar (N) > Dev
# https://docs.blender.org/manual/en/3.6/addons/development/is_key_free.html
addon_keymaps = []

def menu_func(self, context):
    self.layout.operator(FI_OT_render_settings.bl_idname)

    # https://docs.blender.org/api/3.6/bpy.types.Operator.html
    # self.layout.operator_context = 'INVOKE_DEFAULT'
    # self.layout.operator(FI_OT_render_settings.bl_idname, text="Text Export Operator")

def register():
    bpy.utils.register_class(FI_OT_render_settings)
    bpy.types.VIEW3D_MT_object.append(menu_func)  # Adds the new operator to an existing menu.

    # handle the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(FI_OT_render_settings.bl_idname, 'S', 'PRESS', ctrl=True, shift=True)
    kmi.properties.total = 4
    addon_keymaps.append((km, kmi))

def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    bpy.utils.unregister_class(FI_OT_render_settings)

    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
