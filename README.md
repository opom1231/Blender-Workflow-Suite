# Blender-Workflow-Suite

A collection of scripts to fix specific friction points in my Linux 3D workflow.

## 1. Logitech Gesture Bridge

Maps MX Master 3S side-button gestures to Blender pivot point modes (Median, Individual Origins, 3D Cursor).

**How it works:**
  - Hardware: Solaar detects mouse gestures and sends a keyboard shortcut.
  - Systems: Linux uinput and udev rules allow the virtual shortcut to reach Blender.
  - Blender: A Python addon registers operators and listens for the shortcuts.

**Current Setup:**
  - Requires Solaar for hardware-to-shortcut translation.

**Planned:**
  - Replace Solaar with a direct Python hidraw listener to reduce dependencies.
