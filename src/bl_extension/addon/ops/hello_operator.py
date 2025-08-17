import bpy

class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_label = "Simple Object Operator"
    bl_idname = "object.simple_operator"
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        f(context)
        return {'FINISHED'}


def f(context):
    for ob in context.scene.objects:
        print(ob)


def menu_func(self, context):
    self.layout.operator(SimpleOperator.bl_idname, text=SimpleOperator.bl_label)

