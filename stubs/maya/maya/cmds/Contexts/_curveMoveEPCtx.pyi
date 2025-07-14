"""Stub files for Contexts category in Maya commands, command: curveMoveEPCtx."""

from typing import Any, overload

@overload #Overload for curveMoveEPCtx in ['create']
def curveMoveEPCtx(exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ...) -> str:
    """curveMoveEPCtx is undoable, queryable, and editable.
    
    The curveMoveEPCtx command creates a new context for moving curve edit points
    using a manipulator. Edit points can only be moved one at a time.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for curveMoveEPCtx in ['create']
def curveMoveEPCtx(ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ...) -> str:
    """curveMoveEPCtx is undoable, queryable, and editable.
    
    The curveMoveEPCtx command creates a new context for moving curve edit points
    using a manipulator. Edit points can only be moved one at a time.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for curveMoveEPCtx in ['create']
def curveMoveEPCtx(exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ...) -> str:
    """curveMoveEPCtx is undoable, queryable, and editable.
    
    The curveMoveEPCtx command creates a new context for moving curve edit points
    using a manipulator. Edit points can only be moved one at a time.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for curveMoveEPCtx in ['query']
def curveMoveEPCtx(image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> str:
    """curveMoveEPCtx is undoable, queryable, and editable.
    
    The curveMoveEPCtx command creates a new context for moving curve edit points
    using a manipulator. Edit points can only be moved one at a time.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for curveMoveEPCtx in ['query']
def curveMoveEPCtx(i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> str:
    """curveMoveEPCtx is undoable, queryable, and editable.
    
    The curveMoveEPCtx command creates a new context for moving curve edit points
    using a manipulator. Edit points can only be moved one at a time.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for curveMoveEPCtx in ['query']
def curveMoveEPCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> str:
    """curveMoveEPCtx is undoable, queryable, and editable.
    
    The curveMoveEPCtx command creates a new context for moving curve edit points
    using a manipulator. Edit points can only be moved one at a time.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for curveMoveEPCtx in ['edit']
def curveMoveEPCtx(image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> str:
    """curveMoveEPCtx is undoable, queryable, and editable.
    
    The curveMoveEPCtx command creates a new context for moving curve edit points
    using a manipulator. Edit points can only be moved one at a time.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for curveMoveEPCtx in ['edit']
def curveMoveEPCtx(i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> str:
    """curveMoveEPCtx is undoable, queryable, and editable.
    
    The curveMoveEPCtx command creates a new context for moving curve edit points
    using a manipulator. Edit points can only be moved one at a time.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for curveMoveEPCtx in ['edit']
def curveMoveEPCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """curveMoveEPCtx is undoable, queryable, and editable.
    
    The curveMoveEPCtx command creates a new context for moving curve edit points
    using a manipulator. Edit points can only be moved one at a time.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
