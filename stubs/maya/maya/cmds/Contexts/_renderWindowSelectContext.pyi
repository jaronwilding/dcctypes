"""Stub files for Contexts category in Maya commands, command: renderWindowSelectContext."""

from typing import Any, overload

@overload #Overload for renderWindowSelectContext in ['create']
def renderWindowSelectContext(exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ...) -> str:
    """renderWindowSelectContext is undoable, queryable, and editable.
    
    Set the selection context for the render view panel.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for renderWindowSelectContext in ['create']
def renderWindowSelectContext(ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ...) -> str:
    """renderWindowSelectContext is undoable, queryable, and editable.
    
    Set the selection context for the render view panel.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for renderWindowSelectContext in ['create']
def renderWindowSelectContext(exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ...) -> str:
    """renderWindowSelectContext is undoable, queryable, and editable.
    
    Set the selection context for the render view panel.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for renderWindowSelectContext in ['query']
def renderWindowSelectContext(image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> str:
    """renderWindowSelectContext is undoable, queryable, and editable.
    
    Set the selection context for the render view panel.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for renderWindowSelectContext in ['query']
def renderWindowSelectContext(i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> str:
    """renderWindowSelectContext is undoable, queryable, and editable.
    
    Set the selection context for the render view panel.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for renderWindowSelectContext in ['query']
def renderWindowSelectContext(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> str:
    """renderWindowSelectContext is undoable, queryable, and editable.
    
    Set the selection context for the render view panel.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for renderWindowSelectContext in ['edit']
def renderWindowSelectContext(image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> str:
    """renderWindowSelectContext is undoable, queryable, and editable.
    
    Set the selection context for the render view panel.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for renderWindowSelectContext in ['edit']
def renderWindowSelectContext(i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> str:
    """renderWindowSelectContext is undoable, queryable, and editable.
    
    Set the selection context for the render view panel.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for renderWindowSelectContext in ['edit']
def renderWindowSelectContext(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """renderWindowSelectContext is undoable, queryable, and editable.
    
    Set the selection context for the render view panel.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
