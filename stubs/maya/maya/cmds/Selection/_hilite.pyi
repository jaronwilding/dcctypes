"""Stub files for Selection category in Maya commands, command: hilite."""

from typing import Any, overload

@overload #Overload for hilite in ['create']
def hilite([objects]: [objects], replace: bool = ..., toggle: bool = ..., unHilite: bool = ...) -> None:
    """hilite is undoable, NOT queryable, and NOT editable.
    
    Hilites/Unhilites the specified object(s). Hiliting an object makes it
    possible to select the components of the object. If no objects are specified
    then the selection list is used.

    ---
    - Args:
        - [objects]: Input item(s).
        - replace (r): Hilite the specified objects.  Any objects previously hilited will no longer be hilited.
        - toggle (tgl): Toggle the hilite state of the specified objects.
        - unHilite (u): Remove the specified objects from the hilite list.
    """
@overload #Overload for hilite in ['create']
def hilite([objects]: [objects], r: bool = ..., tgl: bool = ..., u: bool = ...) -> None:
    """hilite is undoable, NOT queryable, and NOT editable.
    
    Hilites/Unhilites the specified object(s). Hiliting an object makes it
    possible to select the components of the object. If no objects are specified
    then the selection list is used.

    ---
    - Args:
        - [objects]: Input item(s).
        - replace (r): Hilite the specified objects.  Any objects previously hilited will no longer be hilited.
        - toggle (tgl): Toggle the hilite state of the specified objects.
        - unHilite (u): Remove the specified objects from the hilite list.
    """
@overload #Overload for hilite in ['create']
def hilite([objects]: [objects], replace: bool = ..., r: bool = ..., toggle: bool = ..., tgl: bool = ..., unHilite: bool = ..., u: bool = ...) -> None:
    """hilite is undoable, NOT queryable, and NOT editable.
    
    Hilites/Unhilites the specified object(s). Hiliting an object makes it
    possible to select the components of the object. If no objects are specified
    then the selection list is used.

    ---
    - Args:
        - [objects]: Input item(s).
        - replace (r): Hilite the specified objects.  Any objects previously hilited will no longer be hilited.
        - toggle (tgl): Toggle the hilite state of the specified objects.
        - unHilite (u): Remove the specified objects from the hilite list.
    """
