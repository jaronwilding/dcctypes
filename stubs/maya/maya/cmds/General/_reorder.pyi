"""Stub files for General category in Maya commands, command: reorder."""

from typing import Any, overload

@overload #Overload for reorder in ['create']
def reorder([objects...]: [objects...], back: bool = ..., front: bool = ..., relative: int = ...) -> None:
    """reorder is undoable, NOT queryable, and NOT editable.
    
    This command reorders (moves) objects relative to their siblings.
    
    For relative moves, both positive and negative numbers may be specified.
    Positive numbers move the object forward and negative numbers move the object
    backward amoung its siblings. When an object is at the end (beginning) of the
    list of siblings, a relative move of 1 (-1) will put the object at the
    beginning (end) of the list of siblings. That is, relative moves will wrap if
    necessary.
    
    If a shape is specified and it is the only child then its parent will be
    reordered.

    ---
    - Args:
        - [objects...]: Input item(s).
        - back (b): Move object(s) to back of sibling list.
        - front (f): Move object(s) to front of sibling list.
        - relative (r): Move object(s) relative to other siblings.
    """
@overload #Overload for reorder in ['create']
def reorder([objects...]: [objects...], b: bool = ..., f: bool = ..., r: int = ...) -> None:
    """reorder is undoable, NOT queryable, and NOT editable.
    
    This command reorders (moves) objects relative to their siblings.
    
    For relative moves, both positive and negative numbers may be specified.
    Positive numbers move the object forward and negative numbers move the object
    backward amoung its siblings. When an object is at the end (beginning) of the
    list of siblings, a relative move of 1 (-1) will put the object at the
    beginning (end) of the list of siblings. That is, relative moves will wrap if
    necessary.
    
    If a shape is specified and it is the only child then its parent will be
    reordered.

    ---
    - Args:
        - [objects...]: Input item(s).
        - back (b): Move object(s) to back of sibling list.
        - front (f): Move object(s) to front of sibling list.
        - relative (r): Move object(s) relative to other siblings.
    """
@overload #Overload for reorder in ['create']
def reorder([objects...]: [objects...], back: bool = ..., b: bool = ..., front: bool = ..., f: bool = ..., relative: int = ..., r: int = ...) -> None:
    """reorder is undoable, NOT queryable, and NOT editable.
    
    This command reorders (moves) objects relative to their siblings.
    
    For relative moves, both positive and negative numbers may be specified.
    Positive numbers move the object forward and negative numbers move the object
    backward amoung its siblings. When an object is at the end (beginning) of the
    list of siblings, a relative move of 1 (-1) will put the object at the
    beginning (end) of the list of siblings. That is, relative moves will wrap if
    necessary.
    
    If a shape is specified and it is the only child then its parent will be
    reordered.

    ---
    - Args:
        - [objects...]: Input item(s).
        - back (b): Move object(s) to back of sibling list.
        - front (f): Move object(s) to front of sibling list.
        - relative (r): Move object(s) relative to other siblings.
    """
