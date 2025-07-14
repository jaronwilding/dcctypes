"""Stub files for Contexts category in Maya commands, command: polyShortestPathCtx."""

from typing import Any, overload

@overload #Overload for polyShortestPathCtx in ['create']
def polyShortestPathCtx(exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ...) -> None:
    """polyShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the 3d viewport.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for polyShortestPathCtx in ['create']
def polyShortestPathCtx(ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ...) -> None:
    """polyShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the 3d viewport.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for polyShortestPathCtx in ['create']
def polyShortestPathCtx(exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ...) -> None:
    """polyShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the 3d viewport.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for polyShortestPathCtx in ['query']
def polyShortestPathCtx(image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> None:
    """polyShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the 3d viewport.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for polyShortestPathCtx in ['query']
def polyShortestPathCtx(i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> None:
    """polyShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the 3d viewport.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for polyShortestPathCtx in ['query']
def polyShortestPathCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> None:
    """polyShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the 3d viewport.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for polyShortestPathCtx in ['edit']
def polyShortestPathCtx(image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> None:
    """polyShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the 3d viewport.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for polyShortestPathCtx in ['edit']
def polyShortestPathCtx(i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> None:
    """polyShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the 3d viewport.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for polyShortestPathCtx in ['edit']
def polyShortestPathCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> None:
    """polyShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the 3d viewport.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
