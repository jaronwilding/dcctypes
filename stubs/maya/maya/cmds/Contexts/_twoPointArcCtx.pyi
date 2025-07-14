"""Stub files for Contexts category in Maya commands, command: twoPointArcCtx."""

from typing import Any, overload

@overload #Overload for twoPointArcCtx in ['create']
def twoPointArcCtx(degree: int = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., spans: int = ...) -> str:
    """twoPointArcCtx is undoable, queryable, and editable.
    
    The twoPointArcCtx command creates a new context for creating two point
    circular arcs

    ---
    - Args:
        - degree (d): Valid values are 1 or 3. Default degree 3.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - spans (s): Default is 4.
    """
@overload #Overload for twoPointArcCtx in ['create']
def twoPointArcCtx(d: int = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., s: int = ...) -> str:
    """twoPointArcCtx is undoable, queryable, and editable.
    
    The twoPointArcCtx command creates a new context for creating two point
    circular arcs

    ---
    - Args:
        - degree (d): Valid values are 1 or 3. Default degree 3.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - spans (s): Default is 4.
    """
@overload #Overload for twoPointArcCtx in ['create']
def twoPointArcCtx(degree: int = ..., d: int = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., spans: int = ..., s: int = ...) -> str:
    """twoPointArcCtx is undoable, queryable, and editable.
    
    The twoPointArcCtx command creates a new context for creating two point
    circular arcs

    ---
    - Args:
        - degree (d): Valid values are 1 or 3. Default degree 3.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - spans (s): Default is 4.
    """
@overload #Overload for twoPointArcCtx in ['query']
def twoPointArcCtx(degree: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., spans: int = ..., query: bool = ...) -> str:
    """twoPointArcCtx is undoable, queryable, and editable.
    
    The twoPointArcCtx command creates a new context for creating two point
    circular arcs

    ---
    - Args:
        - degree (d): Valid values are 1 or 3. Default degree 3.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - spans (s): Default is 4.
        - query (q): Query mode flag
    """
@overload #Overload for twoPointArcCtx in ['query']
def twoPointArcCtx(d: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., s: int = ..., q: bool = ...) -> str:
    """twoPointArcCtx is undoable, queryable, and editable.
    
    The twoPointArcCtx command creates a new context for creating two point
    circular arcs

    ---
    - Args:
        - degree (d): Valid values are 1 or 3. Default degree 3.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - spans (s): Default is 4.
        - query (q): Query mode flag
    """
@overload #Overload for twoPointArcCtx in ['query']
def twoPointArcCtx(degree: int = ..., d: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., spans: int = ..., s: int = ..., query: bool = ..., q: bool = ...) -> str:
    """twoPointArcCtx is undoable, queryable, and editable.
    
    The twoPointArcCtx command creates a new context for creating two point
    circular arcs

    ---
    - Args:
        - degree (d): Valid values are 1 or 3. Default degree 3.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - spans (s): Default is 4.
        - query (q): Query mode flag
    """
@overload #Overload for twoPointArcCtx in ['edit']
def twoPointArcCtx(degree: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., spans: int = ..., edit: bool = ...) -> str:
    """twoPointArcCtx is undoable, queryable, and editable.
    
    The twoPointArcCtx command creates a new context for creating two point
    circular arcs

    ---
    - Args:
        - degree (d): Valid values are 1 or 3. Default degree 3.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - spans (s): Default is 4.
        - edit (e): Edit mode flag
    """
@overload #Overload for twoPointArcCtx in ['edit']
def twoPointArcCtx(d: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., s: int = ..., e: bool = ...) -> str:
    """twoPointArcCtx is undoable, queryable, and editable.
    
    The twoPointArcCtx command creates a new context for creating two point
    circular arcs

    ---
    - Args:
        - degree (d): Valid values are 1 or 3. Default degree 3.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - spans (s): Default is 4.
        - edit (e): Edit mode flag
    """
@overload #Overload for twoPointArcCtx in ['edit']
def twoPointArcCtx(degree: int = ..., d: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., spans: int = ..., s: int = ..., edit: bool = ..., e: bool = ...) -> str:
    """twoPointArcCtx is undoable, queryable, and editable.
    
    The twoPointArcCtx command creates a new context for creating two point
    circular arcs

    ---
    - Args:
        - degree (d): Valid values are 1 or 3. Default degree 3.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - spans (s): Default is 4.
        - edit (e): Edit mode flag
    """
