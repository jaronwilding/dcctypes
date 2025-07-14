"""Stub files for Selection category in Maya commands, command: isolateSelect."""

from typing import Any, overload

@overload #Overload for isolateSelect in ['query']
def isolateSelect(string: str, state: bool = ..., viewObjects: bool = ..., query: bool = ...) -> bool:
    """isolateSelect is undoable, queryable, and NOT editable.
    
    This command turns on/off isolate select mode in a specified modeling view,
    specified as the argument. Isolate select mode is a display mode where the
    currently selected objects are added to a list and only those objects are
    displayed in the view. It allows for selective viewing of specific objects and
    object components.

    ---
    - Args:
        - string: Input item(s).
        - state (s): Turns isolate select mode on/off.
        - viewObjects (vo): Returns the name (if any) of the objectSet which contains the list of objects visible in the view if isolate select mode is on. If isolate select mode is off, an empty string is returned.
        - query (q): Query mode flag
    """
@overload #Overload for isolateSelect in ['query']
def isolateSelect(string: str, s: bool = ..., vo: bool = ..., q: bool = ...) -> bool:
    """isolateSelect is undoable, queryable, and NOT editable.
    
    This command turns on/off isolate select mode in a specified modeling view,
    specified as the argument. Isolate select mode is a display mode where the
    currently selected objects are added to a list and only those objects are
    displayed in the view. It allows for selective viewing of specific objects and
    object components.

    ---
    - Args:
        - string: Input item(s).
        - state (s): Turns isolate select mode on/off.
        - viewObjects (vo): Returns the name (if any) of the objectSet which contains the list of objects visible in the view if isolate select mode is on. If isolate select mode is off, an empty string is returned.
        - query (q): Query mode flag
    """
@overload #Overload for isolateSelect in ['query']
def isolateSelect(string: str, state: bool = ..., s: bool = ..., viewObjects: bool = ..., vo: bool = ..., query: bool = ..., q: bool = ...) -> bool:
    """isolateSelect is undoable, queryable, and NOT editable.
    
    This command turns on/off isolate select mode in a specified modeling view,
    specified as the argument. Isolate select mode is a display mode where the
    currently selected objects are added to a list and only those objects are
    displayed in the view. It allows for selective viewing of specific objects and
    object components.

    ---
    - Args:
        - string: Input item(s).
        - state (s): Turns isolate select mode on/off.
        - viewObjects (vo): Returns the name (if any) of the objectSet which contains the list of objects visible in the view if isolate select mode is on. If isolate select mode is off, an empty string is returned.
        - query (q): Query mode flag
    """
