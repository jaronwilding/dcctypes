"""Stub files for Attributes category in Maya commands, command: isDirty."""

from typing import Any, overload

@overload #Overload for isDirty in ['create']
def isDirty(string...: string..., connection: bool = ..., datablock: bool = ...) -> bool:
    """isDirty is undoable, NOT queryable, and NOT editable.
    
    The isDirty command is used to check if a plug is dirty. The return value is 0
    if it is not and 1 if it is. If more than one plug is specified then the
    result is the logical "or" of all objects (ie. returns 1 if *any* of the plugs
    are dirty).

    ---
    - Args:
        - string...: Input item(s).
        - connection (c): Check the connection of the plug (default).
        - datablock (d): Check the datablock entry for the plug.
    """
@overload #Overload for isDirty in ['create']
def isDirty(string...: string..., c: bool = ..., d: bool = ...) -> bool:
    """isDirty is undoable, NOT queryable, and NOT editable.
    
    The isDirty command is used to check if a plug is dirty. The return value is 0
    if it is not and 1 if it is. If more than one plug is specified then the
    result is the logical "or" of all objects (ie. returns 1 if *any* of the plugs
    are dirty).

    ---
    - Args:
        - string...: Input item(s).
        - connection (c): Check the connection of the plug (default).
        - datablock (d): Check the datablock entry for the plug.
    """
@overload #Overload for isDirty in ['create']
def isDirty(string...: string..., connection: bool = ..., c: bool = ..., datablock: bool = ..., d: bool = ...) -> bool:
    """isDirty is undoable, NOT queryable, and NOT editable.
    
    The isDirty command is used to check if a plug is dirty. The return value is 0
    if it is not and 1 if it is. If more than one plug is specified then the
    result is the logical "or" of all objects (ie. returns 1 if *any* of the plugs
    are dirty).

    ---
    - Args:
        - string...: Input item(s).
        - connection (c): Check the connection of the plug (default).
        - datablock (d): Check the datablock entry for the plug.
    """
