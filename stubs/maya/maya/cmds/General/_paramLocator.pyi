"""Stub files for General category in Maya commands, command: paramLocator."""

from typing import Any, overload

@overload #Overload for paramLocator in ['create']
def paramLocator([object]: [object], position: bool = ...) -> str:
    """paramLocator is undoable, queryable, and editable.
    
    The command creates a locator in the underworld of a NURBS curve or NURBS
    surface at the specified parameter value. If no object is specified, then a
    locator will be created on the first valid selected item (either a curve point
    or a surface point).

    ---
    - Args:
        - [object]: Input item(s).
        - position (p): Whether to set the locator position in normalized space.
    """
@overload #Overload for paramLocator in ['create']
def paramLocator([object]: [object], p: bool = ...) -> str:
    """paramLocator is undoable, queryable, and editable.
    
    The command creates a locator in the underworld of a NURBS curve or NURBS
    surface at the specified parameter value. If no object is specified, then a
    locator will be created on the first valid selected item (either a curve point
    or a surface point).

    ---
    - Args:
        - [object]: Input item(s).
        - position (p): Whether to set the locator position in normalized space.
    """
@overload #Overload for paramLocator in ['create']
def paramLocator([object]: [object], position: bool = ..., p: bool = ...) -> str:
    """paramLocator is undoable, queryable, and editable.
    
    The command creates a locator in the underworld of a NURBS curve or NURBS
    surface at the specified parameter value. If no object is specified, then a
    locator will be created on the first valid selected item (either a curve point
    or a surface point).

    ---
    - Args:
        - [object]: Input item(s).
        - position (p): Whether to set the locator position in normalized space.
    """
