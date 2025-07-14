"""Stub files for Display category in Maya commands, command: hide."""

from typing import Any, overload

@overload #Overload for hide in ['create']
def hide([objects]: [objects], allObjects: bool = ..., clearLastHidden: bool = ..., clearSelection: bool = ..., invertComponents: bool = ..., returnHidden: bool = ..., testVisibility: bool = ...) -> None:
    """hide is undoable, NOT queryable, and NOT editable.
    
    The hide command is used to make objects invisible. If no flags are used, the
    objects specified, or the active objects if none are specified, will be made
    invisible.

    ---
    - Args:
        - [objects]: Input item(s).
        - allObjects (all): Make everything invisible (top level objects).
        - clearLastHidden (clh): Clear the last hidden list.
        - clearSelection (cs): Clear selection after the operation.
        - invertComponents (ic): Hide components that are not specified.
        - returnHidden (rh): Hide objects, but also return list of hidden objects.
        - testVisibility (tv): Do not change visibility, just test it (returns 1 is invisible, 2 if visible, 3 if partially visible).
    """
@overload #Overload for hide in ['create']
def hide([objects]: [objects], all: bool = ..., clh: bool = ..., cs: bool = ..., ic: bool = ..., rh: bool = ..., tv: bool = ...) -> None:
    """hide is undoable, NOT queryable, and NOT editable.
    
    The hide command is used to make objects invisible. If no flags are used, the
    objects specified, or the active objects if none are specified, will be made
    invisible.

    ---
    - Args:
        - [objects]: Input item(s).
        - allObjects (all): Make everything invisible (top level objects).
        - clearLastHidden (clh): Clear the last hidden list.
        - clearSelection (cs): Clear selection after the operation.
        - invertComponents (ic): Hide components that are not specified.
        - returnHidden (rh): Hide objects, but also return list of hidden objects.
        - testVisibility (tv): Do not change visibility, just test it (returns 1 is invisible, 2 if visible, 3 if partially visible).
    """
@overload #Overload for hide in ['create']
def hide([objects]: [objects], allObjects: bool = ..., all: bool = ..., clearLastHidden: bool = ..., clh: bool = ..., clearSelection: bool = ..., cs: bool = ..., invertComponents: bool = ..., ic: bool = ..., returnHidden: bool = ..., rh: bool = ..., testVisibility: bool = ..., tv: bool = ...) -> None:
    """hide is undoable, NOT queryable, and NOT editable.
    
    The hide command is used to make objects invisible. If no flags are used, the
    objects specified, or the active objects if none are specified, will be made
    invisible.

    ---
    - Args:
        - [objects]: Input item(s).
        - allObjects (all): Make everything invisible (top level objects).
        - clearLastHidden (clh): Clear the last hidden list.
        - clearSelection (cs): Clear selection after the operation.
        - invertComponents (ic): Hide components that are not specified.
        - returnHidden (rh): Hide objects, but also return list of hidden objects.
        - testVisibility (tv): Do not change visibility, just test it (returns 1 is invisible, 2 if visible, 3 if partially visible).
    """
