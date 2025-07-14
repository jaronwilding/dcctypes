"""Stub files for Display category in Maya commands, command: showHidden."""

from typing import Any, overload

@overload #Overload for showHidden in ['create']
def showHidden([objects...]: [objects...], above: bool = ..., allObjects: bool = ..., below: bool = ..., lastHidden: bool = ...) -> None:
    """showHidden is undoable, NOT queryable, and NOT editable.
    
    The showHidden command is used to make invisible objects visible. If no flags
    are specified, only the objects given to the command will be made visible. If
    a parent of an object is invisible, the object will still be invisible.
    Invisibility is inherited. To ensure the object becomes visible, use the
    -a/above flag. This forces all invisible ancestors of the object(s) to be
    visible. If the -b/below flag is used, any invisible objects below the object
    will be made visible. To make all objects visible, use the -all/allObjects
    flag.
    
    See also: hide

    ---
    - Args:
        - [objects...]: Input item(s).
        - above (a): Make objects and all their invisible ancestors visible.
        - allObjects (all): Make all invisible objects visible.
        - below (b): Make objects and all their invisible descendants visible.
        - lastHidden (lh): Show everything that was hidden with the last hide command.
    """
@overload #Overload for showHidden in ['create']
def showHidden([objects...]: [objects...], a: bool = ..., all: bool = ..., b: bool = ..., lh: bool = ...) -> None:
    """showHidden is undoable, NOT queryable, and NOT editable.
    
    The showHidden command is used to make invisible objects visible. If no flags
    are specified, only the objects given to the command will be made visible. If
    a parent of an object is invisible, the object will still be invisible.
    Invisibility is inherited. To ensure the object becomes visible, use the
    -a/above flag. This forces all invisible ancestors of the object(s) to be
    visible. If the -b/below flag is used, any invisible objects below the object
    will be made visible. To make all objects visible, use the -all/allObjects
    flag.
    
    See also: hide

    ---
    - Args:
        - [objects...]: Input item(s).
        - above (a): Make objects and all their invisible ancestors visible.
        - allObjects (all): Make all invisible objects visible.
        - below (b): Make objects and all their invisible descendants visible.
        - lastHidden (lh): Show everything that was hidden with the last hide command.
    """
@overload #Overload for showHidden in ['create']
def showHidden([objects...]: [objects...], above: bool = ..., a: bool = ..., allObjects: bool = ..., all: bool = ..., below: bool = ..., b: bool = ..., lastHidden: bool = ..., lh: bool = ...) -> None:
    """showHidden is undoable, NOT queryable, and NOT editable.
    
    The showHidden command is used to make invisible objects visible. If no flags
    are specified, only the objects given to the command will be made visible. If
    a parent of an object is invisible, the object will still be invisible.
    Invisibility is inherited. To ensure the object becomes visible, use the
    -a/above flag. This forces all invisible ancestors of the object(s) to be
    visible. If the -b/below flag is used, any invisible objects below the object
    will be made visible. To make all objects visible, use the -all/allObjects
    flag.
    
    See also: hide

    ---
    - Args:
        - [objects...]: Input item(s).
        - above (a): Make objects and all their invisible ancestors visible.
        - allObjects (all): Make all invisible objects visible.
        - below (b): Make objects and all their invisible descendants visible.
        - lastHidden (lh): Show everything that was hidden with the last hide command.
    """
