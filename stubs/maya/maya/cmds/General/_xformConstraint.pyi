"""Stub files for General category in Maya commands, command: xformConstraint."""

from typing import Any, overload

@overload #Overload for xformConstraint in ['create']
def xformConstraint(alongNormal: int = ..., type: str = ...) -> None:
    """xformConstraint is undoable, queryable, and editable.
    
    This command allows you to change the transform constraint used by the
    transform tools during component transforms.

    ---
    - Args:
        - alongNormal (n): When set the transform constraint will first be applied along the vertex normals of the components being transformed. When queried, returns the current state of this option.
        - type (t): Set the type of transform constraint to use. When queried, returns the current transform constraint as a string.none - no constraintsurface - constrain components to their surfaceedge - constrain components to surface edges
    """
@overload #Overload for xformConstraint in ['create']
def xformConstraint(n: int = ..., t: str = ...) -> None:
    """xformConstraint is undoable, queryable, and editable.
    
    This command allows you to change the transform constraint used by the
    transform tools during component transforms.

    ---
    - Args:
        - alongNormal (n): When set the transform constraint will first be applied along the vertex normals of the components being transformed. When queried, returns the current state of this option.
        - type (t): Set the type of transform constraint to use. When queried, returns the current transform constraint as a string.none - no constraintsurface - constrain components to their surfaceedge - constrain components to surface edges
    """
@overload #Overload for xformConstraint in ['create']
def xformConstraint(alongNormal: int = ..., n: int = ..., type: str = ..., t: str = ...) -> None:
    """xformConstraint is undoable, queryable, and editable.
    
    This command allows you to change the transform constraint used by the
    transform tools during component transforms.

    ---
    - Args:
        - alongNormal (n): When set the transform constraint will first be applied along the vertex normals of the components being transformed. When queried, returns the current state of this option.
        - type (t): Set the type of transform constraint to use. When queried, returns the current transform constraint as a string.none - no constraintsurface - constrain components to their surfaceedge - constrain components to surface edges
    """
@overload #Overload for xformConstraint in ['query']
def xformConstraint(alongNormal: int = ..., live: bool = ..., type: str = ..., query: bool = ...) -> None:
    """xformConstraint is undoable, queryable, and editable.
    
    This command allows you to change the transform constraint used by the
    transform tools during component transforms.

    ---
    - Args:
        - alongNormal (n): When set the transform constraint will first be applied along the vertex normals of the components being transformed. When queried, returns the current state of this option.
        - live (l): Query-only flag that can be used to check whether the current live surface will be used as a transform constraint.
        - type (t): Set the type of transform constraint to use. When queried, returns the current transform constraint as a string.none - no constraintsurface - constrain components to their surfaceedge - constrain components to surface edges
        - query (q): Query mode flag
    """
@overload #Overload for xformConstraint in ['query']
def xformConstraint(n: int = ..., l: bool = ..., t: str = ..., q: bool = ...) -> None:
    """xformConstraint is undoable, queryable, and editable.
    
    This command allows you to change the transform constraint used by the
    transform tools during component transforms.

    ---
    - Args:
        - alongNormal (n): When set the transform constraint will first be applied along the vertex normals of the components being transformed. When queried, returns the current state of this option.
        - live (l): Query-only flag that can be used to check whether the current live surface will be used as a transform constraint.
        - type (t): Set the type of transform constraint to use. When queried, returns the current transform constraint as a string.none - no constraintsurface - constrain components to their surfaceedge - constrain components to surface edges
        - query (q): Query mode flag
    """
@overload #Overload for xformConstraint in ['query']
def xformConstraint(alongNormal: int = ..., n: int = ..., live: bool = ..., l: bool = ..., type: str = ..., t: str = ..., query: bool = ..., q: bool = ...) -> None:
    """xformConstraint is undoable, queryable, and editable.
    
    This command allows you to change the transform constraint used by the
    transform tools during component transforms.

    ---
    - Args:
        - alongNormal (n): When set the transform constraint will first be applied along the vertex normals of the components being transformed. When queried, returns the current state of this option.
        - live (l): Query-only flag that can be used to check whether the current live surface will be used as a transform constraint.
        - type (t): Set the type of transform constraint to use. When queried, returns the current transform constraint as a string.none - no constraintsurface - constrain components to their surfaceedge - constrain components to surface edges
        - query (q): Query mode flag
    """
@overload #Overload for xformConstraint in ['edit']
def xformConstraint(alongNormal: int = ..., type: str = ..., edit: bool = ...) -> None:
    """xformConstraint is undoable, queryable, and editable.
    
    This command allows you to change the transform constraint used by the
    transform tools during component transforms.

    ---
    - Args:
        - alongNormal (n): When set the transform constraint will first be applied along the vertex normals of the components being transformed. When queried, returns the current state of this option.
        - type (t): Set the type of transform constraint to use. When queried, returns the current transform constraint as a string.none - no constraintsurface - constrain components to their surfaceedge - constrain components to surface edges
        - edit (e): Edit mode flag
    """
@overload #Overload for xformConstraint in ['edit']
def xformConstraint(n: int = ..., t: str = ..., e: bool = ...) -> None:
    """xformConstraint is undoable, queryable, and editable.
    
    This command allows you to change the transform constraint used by the
    transform tools during component transforms.

    ---
    - Args:
        - alongNormal (n): When set the transform constraint will first be applied along the vertex normals of the components being transformed. When queried, returns the current state of this option.
        - type (t): Set the type of transform constraint to use. When queried, returns the current transform constraint as a string.none - no constraintsurface - constrain components to their surfaceedge - constrain components to surface edges
        - edit (e): Edit mode flag
    """
@overload #Overload for xformConstraint in ['edit']
def xformConstraint(alongNormal: int = ..., n: int = ..., type: str = ..., t: str = ..., edit: bool = ..., e: bool = ...) -> None:
    """xformConstraint is undoable, queryable, and editable.
    
    This command allows you to change the transform constraint used by the
    transform tools during component transforms.

    ---
    - Args:
        - alongNormal (n): When set the transform constraint will first be applied along the vertex normals of the components being transformed. When queried, returns the current state of this option.
        - type (t): Set the type of transform constraint to use. When queried, returns the current transform constraint as a string.none - no constraintsurface - constrain components to their surfaceedge - constrain components to surface edges
        - edit (e): Edit mode flag
    """
