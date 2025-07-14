"""Stub files for Contexts category in Maya commands, command: texManipContext."""

from typing import Any, overload

@overload #Overload for texManipContext in ['create']
def texManipContext(exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ...) -> str | str:
    """texManipContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool. Command used to register the
    texManipCtx tool.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for texManipContext in ['create']
def texManipContext(ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ...) -> str | str:
    """texManipContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool. Command used to register the
    texManipCtx tool.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for texManipContext in ['create']
def texManipContext(exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ...) -> str | str:
    """texManipContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool. Command used to register the
    texManipCtx tool.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for texManipContext in ['query']
def texManipContext(image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> str | str:
    """texManipContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool. Command used to register the
    texManipCtx tool.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for texManipContext in ['query']
def texManipContext(i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> str | str:
    """texManipContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool. Command used to register the
    texManipCtx tool.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for texManipContext in ['query']
def texManipContext(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> str | str:
    """texManipContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool. Command used to register the
    texManipCtx tool.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for texManipContext in ['edit']
def texManipContext(image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> str | str:
    """texManipContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool. Command used to register the
    texManipCtx tool.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for texManipContext in ['edit']
def texManipContext(i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> str | str:
    """texManipContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool. Command used to register the
    texManipCtx tool.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for texManipContext in ['edit']
def texManipContext(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> str | str:
    """texManipContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool. Command used to register the
    texManipCtx tool.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
