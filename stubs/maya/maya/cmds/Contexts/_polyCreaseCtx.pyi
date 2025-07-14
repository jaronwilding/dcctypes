"""Stub files for Contexts category in Maya commands, command: polyCreaseCtx."""

from typing import Any, overload

@overload #Overload for polyCreaseCtx in ['create']
def polyCreaseCtx(exists: bool = ..., extendSelection: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., relative: bool = ...) -> None:
    """polyCreaseCtx is undoable, queryable, and editable.
    
    Create a new context to crease components on polygonal objects

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - extendSelection (es): Enable/disable extending selection to all connected creased components.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - relative (r): Enable/disable applying value relative to existing crease value. If disabled, absolute value is applied.
    """
@overload #Overload for polyCreaseCtx in ['create']
def polyCreaseCtx(ex: bool = ..., es: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., r: bool = ...) -> None:
    """polyCreaseCtx is undoable, queryable, and editable.
    
    Create a new context to crease components on polygonal objects

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - extendSelection (es): Enable/disable extending selection to all connected creased components.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - relative (r): Enable/disable applying value relative to existing crease value. If disabled, absolute value is applied.
    """
@overload #Overload for polyCreaseCtx in ['create']
def polyCreaseCtx(exists: bool = ..., ex: bool = ..., extendSelection: bool = ..., es: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., relative: bool = ..., r: bool = ...) -> None:
    """polyCreaseCtx is undoable, queryable, and editable.
    
    Create a new context to crease components on polygonal objects

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - extendSelection (es): Enable/disable extending selection to all connected creased components.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - relative (r): Enable/disable applying value relative to existing crease value. If disabled, absolute value is applied.
    """
@overload #Overload for polyCreaseCtx in ['query']
def polyCreaseCtx(extendSelection: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., relative: bool = ..., query: bool = ...) -> None:
    """polyCreaseCtx is undoable, queryable, and editable.
    
    Create a new context to crease components on polygonal objects

    ---
    - Args:
        - extendSelection (es): Enable/disable extending selection to all connected creased components.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - relative (r): Enable/disable applying value relative to existing crease value. If disabled, absolute value is applied.
        - query (q): Query mode flag
    """
@overload #Overload for polyCreaseCtx in ['query']
def polyCreaseCtx(es: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., r: bool = ..., q: bool = ...) -> None:
    """polyCreaseCtx is undoable, queryable, and editable.
    
    Create a new context to crease components on polygonal objects

    ---
    - Args:
        - extendSelection (es): Enable/disable extending selection to all connected creased components.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - relative (r): Enable/disable applying value relative to existing crease value. If disabled, absolute value is applied.
        - query (q): Query mode flag
    """
@overload #Overload for polyCreaseCtx in ['query']
def polyCreaseCtx(extendSelection: bool = ..., es: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., relative: bool = ..., r: bool = ..., query: bool = ..., q: bool = ...) -> None:
    """polyCreaseCtx is undoable, queryable, and editable.
    
    Create a new context to crease components on polygonal objects

    ---
    - Args:
        - extendSelection (es): Enable/disable extending selection to all connected creased components.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - relative (r): Enable/disable applying value relative to existing crease value. If disabled, absolute value is applied.
        - query (q): Query mode flag
    """
@overload #Overload for polyCreaseCtx in ['edit']
def polyCreaseCtx(createSet: str = ..., extendSelection: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., relative: bool = ..., edit: bool = ...) -> None:
    """polyCreaseCtx is undoable, queryable, and editable.
    
    Create a new context to crease components on polygonal objects

    ---
    - Args:
        - createSet (cs): Creates a set for the selected components.
        - extendSelection (es): Enable/disable extending selection to all connected creased components.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - relative (r): Enable/disable applying value relative to existing crease value. If disabled, absolute value is applied.
        - edit (e): Edit mode flag
    """
@overload #Overload for polyCreaseCtx in ['edit']
def polyCreaseCtx(cs: str = ..., es: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., r: bool = ..., e: bool = ...) -> None:
    """polyCreaseCtx is undoable, queryable, and editable.
    
    Create a new context to crease components on polygonal objects

    ---
    - Args:
        - createSet (cs): Creates a set for the selected components.
        - extendSelection (es): Enable/disable extending selection to all connected creased components.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - relative (r): Enable/disable applying value relative to existing crease value. If disabled, absolute value is applied.
        - edit (e): Edit mode flag
    """
@overload #Overload for polyCreaseCtx in ['edit']
def polyCreaseCtx(createSet: str = ..., cs: str = ..., extendSelection: bool = ..., es: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., relative: bool = ..., r: bool = ..., edit: bool = ..., e: bool = ...) -> None:
    """polyCreaseCtx is undoable, queryable, and editable.
    
    Create a new context to crease components on polygonal objects

    ---
    - Args:
        - createSet (cs): Creates a set for the selected components.
        - extendSelection (es): Enable/disable extending selection to all connected creased components.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - relative (r): Enable/disable applying value relative to existing crease value. If disabled, absolute value is applied.
        - edit (e): Edit mode flag
    """
