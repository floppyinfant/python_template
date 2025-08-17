import bpy
from . import hello_operator


# defined classes must be registered
classes = (
    hello_operator.SimpleOperator
)


def register():
    """Register and add to the "object" menu. 
        (required to also use F3 search "Simple Object Operator" for quick access)."""
    
    for cls in classes:
        bpy.utils.register_class(cls)
    
    # TODO is this the correct place to call menu_func?
    bpy.types.VIEW3D_MT_object.append(hello_operator.menu_func)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
