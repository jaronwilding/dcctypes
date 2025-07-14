"""Stub files for General category in Maya commands, command: scaleComponents."""

from typing import Any, overload

@overload #Overload for scaleComponents in ['create']
def scaleComponents(float float float [objects]: float float float [objects], pivot: [linear, linear, linear] = ..., rotation: [angle, angle, angle] = ...) -> None:
    """scaleComponents is undoable, NOT queryable, and NOT editable.
    
    This is a limited version of the scale command. First, it only works on
    selected components. You provide a pivot in world space, and you can provide a
    rotation. This rotation affects the scaling, so that rather than scaling in X,
    Y, Z, this is scaling in X, Y, and Z after they have been rotated by the given
    rotation.
    
    This allows selected components to be scaled in any arbitrary space, not just
    object or world space as the regular scale allows.
    
    Scale values are always relative, not absolute.

    ---
    - Args:
        - float float float [objects]: Input item(s).
        - pivot (p): The pivot position in world space (default is origin)
        - rotation (ro): The rotational offset for the scaling (default is none)
    """
@overload #Overload for scaleComponents in ['create']
def scaleComponents(float float float [objects]: float float float [objects], p: [linear, linear, linear] = ..., ro: [angle, angle, angle] = ...) -> None:
    """scaleComponents is undoable, NOT queryable, and NOT editable.
    
    This is a limited version of the scale command. First, it only works on
    selected components. You provide a pivot in world space, and you can provide a
    rotation. This rotation affects the scaling, so that rather than scaling in X,
    Y, Z, this is scaling in X, Y, and Z after they have been rotated by the given
    rotation.
    
    This allows selected components to be scaled in any arbitrary space, not just
    object or world space as the regular scale allows.
    
    Scale values are always relative, not absolute.

    ---
    - Args:
        - float float float [objects]: Input item(s).
        - pivot (p): The pivot position in world space (default is origin)
        - rotation (ro): The rotational offset for the scaling (default is none)
    """
@overload #Overload for scaleComponents in ['create']
def scaleComponents(float float float [objects]: float float float [objects], pivot: [linear, linear, linear] = ..., p: [linear, linear, linear] = ..., rotation: [angle, angle, angle] = ..., ro: [angle, angle, angle] = ...) -> None:
    """scaleComponents is undoable, NOT queryable, and NOT editable.
    
    This is a limited version of the scale command. First, it only works on
    selected components. You provide a pivot in world space, and you can provide a
    rotation. This rotation affects the scaling, so that rather than scaling in X,
    Y, Z, this is scaling in X, Y, and Z after they have been rotated by the given
    rotation.
    
    This allows selected components to be scaled in any arbitrary space, not just
    object or world space as the regular scale allows.
    
    Scale values are always relative, not absolute.

    ---
    - Args:
        - float float float [objects]: Input item(s).
        - pivot (p): The pivot position in world space (default is origin)
        - rotation (ro): The rotational offset for the scaling (default is none)
    """
