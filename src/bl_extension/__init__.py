# region INFO
# blender extensions @since 4.2
# https://docs.blender.org/api/current/info_quickstart.html
# https://docs.blender.org/manual/en/latest/advanced/extensions/index.html
# https://developer.blender.org/docs/handbook/extensions/addon_guidelines/
# https://extensions.blender.org/
# endregion

import bpy

# region DELETE_ME
"""
# old for addons; now moved to blender_manifest.toml for extensions
bl_info = {
    'name': '',
    'author': '',
    'description': '',
    'blender': (2, 93, 0),
    'version': (2, 0, 5),
    "doc_url": "https://",
    'location': 'View3D',
    'category': '3D View',
}
"""

from mathutils import *

# builtin modules
c = bpy.context
d = bpy.data

b_t = bpy.types
b_p = bpy.props
b_o = bpy.ops
b_u = bpy.utils
b_a = bpy.app
# bgl, gpu, blf, mathutils
# endregion

# region MAIN
# ----------------------------------------------------------------------------
# __init__.py: package == extension -> addon -> modules -> sub~ -> files == modules -> classes
# ----------------------------------------------------------------------------
# file structure:
# package/module.py (defines Classes)
# package/__init__.py
# use relative imports in __init__.py:
#from .module import Class
# vs. main.py
#from package import Class

from . import addon

def register():
    addon.register()


def unregister():
    """Unregister in reverse order and remove from the "object" menu."""
    addon.unregister()


if __name__ == "__main__":
    register()

# endregion
