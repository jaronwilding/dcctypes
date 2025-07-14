"""Stub files for General category in Maya commands, command: align."""

from typing import Any, overload

@overload #Overload for align in ['create']
def align(alignToLead: bool = ..., coordinateSystem: name = ..., xAxis: str = ..., yAxis: str = ..., zAxis: str = ...) -> bool:
    """align is undoable, NOT queryable, and NOT editable.
    
    Align or spread objects along X Y and Z axis.

    ---
    - Args:
        - alignToLead (atl): When set, the min, center or max values are computed from the lead object. Otherwise, the values are averaged for all objects.Default is false
        - coordinateSystem (cs): Defines the X, Y, and Z coordinates. Default is the world coordinates
        - xAxis (x): Any of none, min, mid, max, dist, stack.This defines the kind of alignment to perfom, default is none.
        - yAxis (y): Any of none, min, mid, max, dist, stack.This defines the kind of alignment to perfom, default is none.
        - zAxis (z): Any of none, min, mid, max, dist, stack.This defines the kind of alignment to perfom, default is none.
    """
@overload #Overload for align in ['create']
def align(atl: bool = ..., cs: name = ..., x: str = ..., y: str = ..., z: str = ...) -> bool:
    """align is undoable, NOT queryable, and NOT editable.
    
    Align or spread objects along X Y and Z axis.

    ---
    - Args:
        - alignToLead (atl): When set, the min, center or max values are computed from the lead object. Otherwise, the values are averaged for all objects.Default is false
        - coordinateSystem (cs): Defines the X, Y, and Z coordinates. Default is the world coordinates
        - xAxis (x): Any of none, min, mid, max, dist, stack.This defines the kind of alignment to perfom, default is none.
        - yAxis (y): Any of none, min, mid, max, dist, stack.This defines the kind of alignment to perfom, default is none.
        - zAxis (z): Any of none, min, mid, max, dist, stack.This defines the kind of alignment to perfom, default is none.
    """
@overload #Overload for align in ['create']
def align(alignToLead: bool = ..., atl: bool = ..., coordinateSystem: name = ..., cs: name = ..., xAxis: str = ..., x: str = ..., yAxis: str = ..., y: str = ..., zAxis: str = ..., z: str = ...) -> bool:
    """align is undoable, NOT queryable, and NOT editable.
    
    Align or spread objects along X Y and Z axis.

    ---
    - Args:
        - alignToLead (atl): When set, the min, center or max values are computed from the lead object. Otherwise, the values are averaged for all objects.Default is false
        - coordinateSystem (cs): Defines the X, Y, and Z coordinates. Default is the world coordinates
        - xAxis (x): Any of none, min, mid, max, dist, stack.This defines the kind of alignment to perfom, default is none.
        - yAxis (y): Any of none, min, mid, max, dist, stack.This defines the kind of alignment to perfom, default is none.
        - zAxis (z): Any of none, min, mid, max, dist, stack.This defines the kind of alignment to perfom, default is none.
    """
