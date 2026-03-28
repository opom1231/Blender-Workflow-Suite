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

# Keymap storage

addon_keymaps = []

# Registering

def register():
    bpy.utils.register_class(set_pivot_median)

    # Accessing Window Manager to setup keybinds through Keyboard Configuration
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc:
        # New keymap group for the 3D View
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        # Key map input
        kmi = km.keymap_items.new(set_pivot_median.bl_idname, 'UP_ARROW', 'PRESS', ctrl=True, shift=True)

        addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(set_pivot_median)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()

