"""Stub files for General category in Maya commands, command: matchTransform."""

from typing import Any, overload

@overload #Overload for matchTransform in ['create']
def matchTransform([objects...]: [objects...], pivots: bool = ..., position: bool = ..., positionX: bool = ..., positionY: bool = ..., positionZ: bool = ..., rotatePivot: bool = ..., rotation: bool = ..., rotationX: bool = ..., rotationY: bool = ..., rotationZ: bool = ..., scale: bool = ..., scaleBox: bool = ..., scalePivot: bool = ..., scaleX: bool = ..., scaleY: bool = ..., scaleZ: bool = ...) -> None:
    """matchTransform is undoable, NOT queryable, and NOT editable.
    
    This command modifies the source object's transform to match the target
    object's transform.
    
    If no flags are specified then the command will match position, rotation and
    scaling.

    Example:
    ```python
        import maya.cmds as cmds
        # create a cone and randomly transform it
        cmds.polyCone(n='cone1')
        cmds.scale(0.2, 2.0, 0.2);
        cmds.rotate(20, 45, 70)
        cmds.move(-2, 0, 2)
        # create a cylinder
        cmds.polyCylinder(n='cylinder1')
        # modify the cylinder's transform to match the cone
        cmds.matchTransform('cylinder1','cone1')
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - pivots (piv): Match the source object(s) scale/rotate pivot positions to the target transform's pivot.
        - position (pos): Match the source object(s) position to the target object.
        - positionX (px): Match the source object(s) X position to the target object.
        - positionY (py): Match the source object(s) Y position to the target object.
        - positionZ (pz): Match the source object(s) Z position to the target object.
        - rotatePivot (rp): Match the source object(s) rotate pivot position to the target transform's pivot.
        - rotation (rot): Match the source object(s) rotation to the target object.
        - rotationX (rx): Match the source object(s) X rotation to the target object.
        - rotationY (ry): Match the source object(s) Y rotation to the target object.
        - rotationZ (rz): Match the source object(s) Z rotation to the target object.
        - scale (scl): Match the source object(s) scale to the target transform.
        - scaleBox (box): Use the source/target object's child bounding box size when matching scaling.
        - scalePivot (sp): Match the source object(s) scale pivot position to the target transform's pivot.
        - scaleX (sx): Match the source object(s) X scale to the target object.
        - scaleY (sy): Match the source object(s) Y scale to the target object.
        - scaleZ (sz): Match the source object(s) Z scale to the target object.
    """
@overload #Overload for matchTransform in ['create']
def matchTransform([objects...]: [objects...], piv: bool = ..., pos: bool = ..., px: bool = ..., py: bool = ..., pz: bool = ..., rp: bool = ..., rot: bool = ..., rx: bool = ..., ry: bool = ..., rz: bool = ..., scl: bool = ..., box: bool = ..., sp: bool = ..., sx: bool = ..., sy: bool = ..., sz: bool = ...) -> None:
    """matchTransform is undoable, NOT queryable, and NOT editable.
    
    This command modifies the source object's transform to match the target
    object's transform.
    
    If no flags are specified then the command will match position, rotation and
    scaling.

    Example:
    ```python
        import maya.cmds as cmds
        # create a cone and randomly transform it
        cmds.polyCone(n='cone1')
        cmds.scale(0.2, 2.0, 0.2);
        cmds.rotate(20, 45, 70)
        cmds.move(-2, 0, 2)
        # create a cylinder
        cmds.polyCylinder(n='cylinder1')
        # modify the cylinder's transform to match the cone
        cmds.matchTransform('cylinder1','cone1')
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - pivots (piv): Match the source object(s) scale/rotate pivot positions to the target transform's pivot.
        - position (pos): Match the source object(s) position to the target object.
        - positionX (px): Match the source object(s) X position to the target object.
        - positionY (py): Match the source object(s) Y position to the target object.
        - positionZ (pz): Match the source object(s) Z position to the target object.
        - rotatePivot (rp): Match the source object(s) rotate pivot position to the target transform's pivot.
        - rotation (rot): Match the source object(s) rotation to the target object.
        - rotationX (rx): Match the source object(s) X rotation to the target object.
        - rotationY (ry): Match the source object(s) Y rotation to the target object.
        - rotationZ (rz): Match the source object(s) Z rotation to the target object.
        - scale (scl): Match the source object(s) scale to the target transform.
        - scaleBox (box): Use the source/target object's child bounding box size when matching scaling.
        - scalePivot (sp): Match the source object(s) scale pivot position to the target transform's pivot.
        - scaleX (sx): Match the source object(s) X scale to the target object.
        - scaleY (sy): Match the source object(s) Y scale to the target object.
        - scaleZ (sz): Match the source object(s) Z scale to the target object.
    """
@overload #Overload for matchTransform in ['create']
def matchTransform([objects...]: [objects...], pivots: bool = ..., piv: bool = ..., position: bool = ..., pos: bool = ..., positionX: bool = ..., px: bool = ..., positionY: bool = ..., py: bool = ..., positionZ: bool = ..., pz: bool = ..., rotatePivot: bool = ..., rp: bool = ..., rotation: bool = ..., rot: bool = ..., rotationX: bool = ..., rx: bool = ..., rotationY: bool = ..., ry: bool = ..., rotationZ: bool = ..., rz: bool = ..., scale: bool = ..., scl: bool = ..., scaleBox: bool = ..., box: bool = ..., scalePivot: bool = ..., sp: bool = ..., scaleX: bool = ..., sx: bool = ..., scaleY: bool = ..., sy: bool = ..., scaleZ: bool = ..., sz: bool = ...) -> None:
    """matchTransform is undoable, NOT queryable, and NOT editable.
    
    This command modifies the source object's transform to match the target
    object's transform.
    
    If no flags are specified then the command will match position, rotation and
    scaling.

    Example:
    ```python
        import maya.cmds as cmds
        # create a cone and randomly transform it
        cmds.polyCone(n='cone1')
        cmds.scale(0.2, 2.0, 0.2);
        cmds.rotate(20, 45, 70)
        cmds.move(-2, 0, 2)
        # create a cylinder
        cmds.polyCylinder(n='cylinder1')
        # modify the cylinder's transform to match the cone
        cmds.matchTransform('cylinder1','cone1')
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - pivots (piv): Match the source object(s) scale/rotate pivot positions to the target transform's pivot.
        - position (pos): Match the source object(s) position to the target object.
        - positionX (px): Match the source object(s) X position to the target object.
        - positionY (py): Match the source object(s) Y position to the target object.
        - positionZ (pz): Match the source object(s) Z position to the target object.
        - rotatePivot (rp): Match the source object(s) rotate pivot position to the target transform's pivot.
        - rotation (rot): Match the source object(s) rotation to the target object.
        - rotationX (rx): Match the source object(s) X rotation to the target object.
        - rotationY (ry): Match the source object(s) Y rotation to the target object.
        - rotationZ (rz): Match the source object(s) Z rotation to the target object.
        - scale (scl): Match the source object(s) scale to the target transform.
        - scaleBox (box): Use the source/target object's child bounding box size when matching scaling.
        - scalePivot (sp): Match the source object(s) scale pivot position to the target transform's pivot.
        - scaleX (sx): Match the source object(s) X scale to the target object.
        - scaleY (sy): Match the source object(s) Y scale to the target object.
        - scaleZ (sz): Match the source object(s) Z scale to the target object.
    """
