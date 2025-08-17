import bpy
from .... import __package__ as base_package

# file == module
from . import hello_panel
#from .hello_panel import HelloWorldPanel


# defined classes must be registered
classes = (
    hello_panel.HelloWorldPanel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
