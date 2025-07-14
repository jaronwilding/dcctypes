"""Stub files for General category in Maya commands, command: transformCompare."""

from typing import Any, overload

@overload #Overload for transformCompare in ['create']
def transformCompare([dagObject dagObject]: [dagObject dagObject], root: bool = ...) -> int:
    """transformCompare is undoable, NOT queryable, and NOT editable.
    
    Compares two transforms passed as arguments. If they are the same, returns 0.
    If they are different, returns 1. If no transforms are specified in the
    command line, then the transforms from the active list are used.

    ---
    - Args:
        - [dagObject dagObject]: Input item(s).
        - root (r): Compare the root only, rather than the entire hierarchy below the roots.
    """
@overload #Overload for transformCompare in ['create']
def transformCompare([dagObject dagObject]: [dagObject dagObject], r: bool = ...) -> int:
    """transformCompare is undoable, NOT queryable, and NOT editable.
    
    Compares two transforms passed as arguments. If they are the same, returns 0.
    If they are different, returns 1. If no transforms are specified in the
    command line, then the transforms from the active list are used.

    ---
    - Args:
        - [dagObject dagObject]: Input item(s).
        - root (r): Compare the root only, rather than the entire hierarchy below the roots.
    """
@overload #Overload for transformCompare in ['create']
def transformCompare([dagObject dagObject]: [dagObject dagObject], root: bool = ..., r: bool = ...) -> int:
    """transformCompare is undoable, NOT queryable, and NOT editable.
    
    Compares two transforms passed as arguments. If they are the same, returns 0.
    If they are different, returns 1. If no transforms are specified in the
    command line, then the transforms from the active list are used.

    ---
    - Args:
        - [dagObject dagObject]: Input item(s).
        - root (r): Compare the root only, rather than the entire hierarchy below the roots.
    """
