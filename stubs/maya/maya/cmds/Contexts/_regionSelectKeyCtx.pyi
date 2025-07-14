"""Stub files for Contexts category in Maya commands, command: regionSelectKeyCtx."""

from typing import Any, overload

@overload #Overload for regionSelectKeyCtx in ['create']
def regionSelectKeyCtx(contextName: contextName, exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ...) -> float:
    """regionSelectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the region select tool.

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for regionSelectKeyCtx in ['create']
def regionSelectKeyCtx(contextName: contextName, ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ...) -> float:
    """regionSelectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the region select tool.

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for regionSelectKeyCtx in ['create']
def regionSelectKeyCtx(contextName: contextName, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ...) -> float:
    """regionSelectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the region select tool.

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for regionSelectKeyCtx in ['query']
def regionSelectKeyCtx(contextName: contextName, bottomManip: float = ..., image1: str = ..., image2: str = ..., image3: str = ..., leftManip: float = ..., rightManip: float = ..., topManip: float = ..., query: bool = ...) -> float:
    """regionSelectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the region select tool.

    ---
    - Args:
        - contextName: Input item(s).
        - bottomManip (bot): Get a point located inside the bottom manipulator of the region box, in screen space.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - leftManip (lft): Get a point located inside the left manipulator of the region box, in screen space.
        - rightManip (rgt): Get a point located inside the right manipulator of the region box, in screen space.
        - topManip (top): Get a point located inside the top manipulator of the region box, in screen space.
        - query (q): Query mode flag
    """
@overload #Overload for regionSelectKeyCtx in ['query']
def regionSelectKeyCtx(contextName: contextName, bot: float = ..., i1: str = ..., i2: str = ..., i3: str = ..., lft: float = ..., rgt: float = ..., top: float = ..., q: bool = ...) -> float:
    """regionSelectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the region select tool.

    ---
    - Args:
        - contextName: Input item(s).
        - bottomManip (bot): Get a point located inside the bottom manipulator of the region box, in screen space.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - leftManip (lft): Get a point located inside the left manipulator of the region box, in screen space.
        - rightManip (rgt): Get a point located inside the right manipulator of the region box, in screen space.
        - topManip (top): Get a point located inside the top manipulator of the region box, in screen space.
        - query (q): Query mode flag
    """
@overload #Overload for regionSelectKeyCtx in ['query']
def regionSelectKeyCtx(contextName: contextName, bottomManip: float = ..., bot: float = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., leftManip: float = ..., lft: float = ..., rightManip: float = ..., rgt: float = ..., topManip: float = ..., top: float = ..., query: bool = ..., q: bool = ...) -> float:
    """regionSelectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the region select tool.

    ---
    - Args:
        - contextName: Input item(s).
        - bottomManip (bot): Get a point located inside the bottom manipulator of the region box, in screen space.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - leftManip (lft): Get a point located inside the left manipulator of the region box, in screen space.
        - rightManip (rgt): Get a point located inside the right manipulator of the region box, in screen space.
        - topManip (top): Get a point located inside the top manipulator of the region box, in screen space.
        - query (q): Query mode flag
    """
@overload #Overload for regionSelectKeyCtx in ['edit']
def regionSelectKeyCtx(contextName: contextName, image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> float:
    """regionSelectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the region select tool.

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for regionSelectKeyCtx in ['edit']
def regionSelectKeyCtx(contextName: contextName, i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> float:
    """regionSelectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the region select tool.

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for regionSelectKeyCtx in ['edit']
def regionSelectKeyCtx(contextName: contextName, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> float:
    """regionSelectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the region select tool.

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
