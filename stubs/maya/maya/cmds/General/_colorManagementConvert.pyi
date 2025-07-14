"""Stub files for General category in Maya commands, command: colorManagementConvert."""

from typing import Any, overload

@overload #Overload for colorManagementConvert in ['create']
def colorManagementConvert(toDisplaySpace: [float, float, float] = ...) -> None:
    """colorManagementConvert is NOT undoable, NOT queryable, and NOT editable.
    
    This command can be used to convert rendering (a.k.a. working) space color
    values to display space color values. This is useful if you create custom UI
    with colors painted to screen, where you need to handle color management
    yourself. The current view transform set in the Color Management user
    preferences will be used.

    ---
    - Args:
        - toDisplaySpace (tds): Converts the given RGB value to display space.
    """
@overload #Overload for colorManagementConvert in ['create']
def colorManagementConvert(tds: [float, float, float] = ...) -> None:
    """colorManagementConvert is NOT undoable, NOT queryable, and NOT editable.
    
    This command can be used to convert rendering (a.k.a. working) space color
    values to display space color values. This is useful if you create custom UI
    with colors painted to screen, where you need to handle color management
    yourself. The current view transform set in the Color Management user
    preferences will be used.

    ---
    - Args:
        - toDisplaySpace (tds): Converts the given RGB value to display space.
    """
@overload #Overload for colorManagementConvert in ['create']
def colorManagementConvert(toDisplaySpace: [float, float, float] = ..., tds: [float, float, float] = ...) -> None:
    """colorManagementConvert is NOT undoable, NOT queryable, and NOT editable.
    
    This command can be used to convert rendering (a.k.a. working) space color
    values to display space color values. This is useful if you create custom UI
    with colors painted to screen, where you need to handle color management
    yourself. The current view transform set in the Color Management user
    preferences will be used.

    ---
    - Args:
        - toDisplaySpace (tds): Converts the given RGB value to display space.
    """
