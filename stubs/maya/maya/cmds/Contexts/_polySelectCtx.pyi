"""Stub files for Contexts category in Maya commands, command: polySelectCtx."""

from typing import Any, overload

@overload #Overload for polySelectCtx in ['create']
def polySelectCtx(exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., mode: int = ...) -> None:
    """polySelectCtx is undoable, queryable, and editable.
    
    Create a new context to select polygon components

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Edge loop or Edge ring or Border edge mode
    """
@overload #Overload for polySelectCtx in ['create']
def polySelectCtx(ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., m: int = ...) -> None:
    """polySelectCtx is undoable, queryable, and editable.
    
    Create a new context to select polygon components

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Edge loop or Edge ring or Border edge mode
    """
@overload #Overload for polySelectCtx in ['create']
def polySelectCtx(exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., mode: int = ..., m: int = ...) -> None:
    """polySelectCtx is undoable, queryable, and editable.
    
    Create a new context to select polygon components

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Edge loop or Edge ring or Border edge mode
    """
@overload #Overload for polySelectCtx in ['query']
def polySelectCtx(image1: str = ..., image2: str = ..., image3: str = ..., mode: int = ..., query: bool = ...) -> None:
    """polySelectCtx is undoable, queryable, and editable.
    
    Create a new context to select polygon components

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Edge loop or Edge ring or Border edge mode
        - query (q): Query mode flag
    """
@overload #Overload for polySelectCtx in ['query']
def polySelectCtx(i1: str = ..., i2: str = ..., i3: str = ..., m: int = ..., q: bool = ...) -> None:
    """polySelectCtx is undoable, queryable, and editable.
    
    Create a new context to select polygon components

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Edge loop or Edge ring or Border edge mode
        - query (q): Query mode flag
    """
@overload #Overload for polySelectCtx in ['query']
def polySelectCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., mode: int = ..., m: int = ..., query: bool = ..., q: bool = ...) -> None:
    """polySelectCtx is undoable, queryable, and editable.
    
    Create a new context to select polygon components

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Edge loop or Edge ring or Border edge mode
        - query (q): Query mode flag
    """
@overload #Overload for polySelectCtx in ['edit']
def polySelectCtx(image1: str = ..., image2: str = ..., image3: str = ..., mode: int = ..., edit: bool = ...) -> None:
    """polySelectCtx is undoable, queryable, and editable.
    
    Create a new context to select polygon components

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Edge loop or Edge ring or Border edge mode
        - edit (e): Edit mode flag
    """
@overload #Overload for polySelectCtx in ['edit']
def polySelectCtx(i1: str = ..., i2: str = ..., i3: str = ..., m: int = ..., e: bool = ...) -> None:
    """polySelectCtx is undoable, queryable, and editable.
    
    Create a new context to select polygon components

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Edge loop or Edge ring or Border edge mode
        - edit (e): Edit mode flag
    """
@overload #Overload for polySelectCtx in ['edit']
def polySelectCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., mode: int = ..., m: int = ..., edit: bool = ..., e: bool = ...) -> None:
    """polySelectCtx is undoable, queryable, and editable.
    
    Create a new context to select polygon components

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Edge loop or Edge ring or Border edge mode
        - edit (e): Edit mode flag
    """
