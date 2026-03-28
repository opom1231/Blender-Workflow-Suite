bl_info = {
    "name": "Custom Pivot Point Operators",
    "author": "Yoseph Amare",
    "version": (1, 0),
    "blender": (4, 5, 0),
    "location": "3D View > Pivot Shortcuts",
    "description": "Adds visible custom operators to set pivot point modes",
    "category": "3D View",
}

# Custom Operators

import bpy
class set_pivot_median(bpy.types.Operator):
    """Set Pivot to Median Point"""
    bl_idname = "view3d.pivot_median"
    bl_label = "Set Pivot to Median Point"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        context.scene.tool_settings.transform_pivot_point = 'MEDIAN_POINT'
        return {'FINISHED'}

# Registering

def register():
    bpy.utils.register_class(set_pivot_median)

def unregister():
    bpy.utils.unregister_class(set_pivot_median)

if __name__ == "__main__":
    register()

