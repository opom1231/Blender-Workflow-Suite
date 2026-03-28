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

class set_pivot_individual(bpy.types.Operator):
    """Set Pivot to Individual Origin"""
    bl_idname = "view3d.pivot_individual"
    bl_label = "Set Pivot to Individual Origin"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
        return {'FINISHED'}
class set_pivot_cursor(bpy.types.Operator):
    """Set Pivot to 3D Cursor"""
    bl_idname = "view3d.pivot_cursor"
    bl_label = "Set Pivot to 3D Cursor"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        context.scene.tool_settings.transform_pivot_point = 'CURSOR'
        return {'FINISHED'}

# Keymap storage

addon_keymaps = []

# Registering

classes = (
    set_pivot_median,
    set_pivot_individual,
    set_pivot_cursor
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    # Accessing Window Manager to setup keybinds through Keyboard Configuration
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc:
        # New keymap group for the 3D View
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')

        # KEYMAP 1: Median (Ctrl + Shift + Up)
        kmi_up = km.keymap_items.new(set_pivot_median.bl_idname, 'UP_ARROW', 'PRESS', ctrl=True, shift=True)
        addon_keymaps.append((km, kmi_up))

        # KEYMAP 2: Individual (Ctrl + Shift + Left)
        kmi_left = km.keymap_items.new(set_pivot_individual.bl_idname, 'LEFT_ARROW', 'PRESS', shift=True, ctrl=True)
        addon_keymaps.append((km, kmi_left))

        # KEYMAP 3: Cursor (Ctrl + Shift + Right)
        kmi_right = km.keymap_items.new(set_pivot_cursor.bl_idname, 'RIGHT_ARROW', 'PRESS', shift=True, ctrl=True)
        addon_keymaps.append((km, kmi_right))

def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
        
if __name__ == "__main__":
    register()

