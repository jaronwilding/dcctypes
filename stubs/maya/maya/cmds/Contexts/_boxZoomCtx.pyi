"""Stub files for Contexts category in Maya commands, command: boxZoomCtx."""

from typing import Any, overload

@overload #Overload for boxZoomCtx in ['create']
def boxZoomCtx(object: object, exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., zoomScale: float = ...) -> str:
    """boxZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a box zoom context. If this
    context is used on a perspective camera, the field of view and view direction
    are changed. If the camera is orthographic, the orthographic width and eye
    point are changed. The left and middle mouse interactively zoom the view. The
    control key can be used to enable box zoom. A box starting from left to right
    will zoom in, and a box starting from right to left will zoom out.

    ---
    - Args:
        - object: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - zoomScale (zs): Scale the zoom.
    """
@overload #Overload for boxZoomCtx in ['create']
def boxZoomCtx(object: object, ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., zs: float = ...) -> str:
    """boxZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a box zoom context. If this
    context is used on a perspective camera, the field of view and view direction
    are changed. If the camera is orthographic, the orthographic width and eye
    point are changed. The left and middle mouse interactively zoom the view. The
    control key can be used to enable box zoom. A box starting from left to right
    will zoom in, and a box starting from right to left will zoom out.

    ---
    - Args:
        - object: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - zoomScale (zs): Scale the zoom.
    """
@overload #Overload for boxZoomCtx in ['create']
def boxZoomCtx(object: object, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., zoomScale: float = ..., zs: float = ...) -> str:
    """boxZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a box zoom context. If this
    context is used on a perspective camera, the field of view and view direction
    are changed. If the camera is orthographic, the orthographic width and eye
    point are changed. The left and middle mouse interactively zoom the view. The
    control key can be used to enable box zoom. A box starting from left to right
    will zoom in, and a box starting from right to left will zoom out.

    ---
    - Args:
        - object: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - zoomScale (zs): Scale the zoom.
    """
@overload #Overload for boxZoomCtx in ['query']
def boxZoomCtx(object: object, image1: str = ..., image2: str = ..., image3: str = ..., zoomScale: float = ..., query: bool = ...) -> str:
    """boxZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a box zoom context. If this
    context is used on a perspective camera, the field of view and view direction
    are changed. If the camera is orthographic, the orthographic width and eye
    point are changed. The left and middle mouse interactively zoom the view. The
    control key can be used to enable box zoom. A box starting from left to right
    will zoom in, and a box starting from right to left will zoom out.

    ---
    - Args:
        - object: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - zoomScale (zs): Scale the zoom.
        - query (q): Query mode flag
    """
@overload #Overload for boxZoomCtx in ['query']
def boxZoomCtx(object: object, i1: str = ..., i2: str = ..., i3: str = ..., zs: float = ..., q: bool = ...) -> str:
    """boxZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a box zoom context. If this
    context is used on a perspective camera, the field of view and view direction
    are changed. If the camera is orthographic, the orthographic width and eye
    point are changed. The left and middle mouse interactively zoom the view. The
    control key can be used to enable box zoom. A box starting from left to right
    will zoom in, and a box starting from right to left will zoom out.

    ---
    - Args:
        - object: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - zoomScale (zs): Scale the zoom.
        - query (q): Query mode flag
    """
@overload #Overload for boxZoomCtx in ['query']
def boxZoomCtx(object: object, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., zoomScale: float = ..., zs: float = ..., query: bool = ..., q: bool = ...) -> str:
    """boxZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a box zoom context. If this
    context is used on a perspective camera, the field of view and view direction
    are changed. If the camera is orthographic, the orthographic width and eye
    point are changed. The left and middle mouse interactively zoom the view. The
    control key can be used to enable box zoom. A box starting from left to right
    will zoom in, and a box starting from right to left will zoom out.

    ---
    - Args:
        - object: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - zoomScale (zs): Scale the zoom.
        - query (q): Query mode flag
    """
@overload #Overload for boxZoomCtx in ['edit']
def boxZoomCtx(object: object, image1: str = ..., image2: str = ..., image3: str = ..., zoomScale: float = ..., edit: bool = ...) -> str:
    """boxZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a box zoom context. If this
    context is used on a perspective camera, the field of view and view direction
    are changed. If the camera is orthographic, the orthographic width and eye
    point are changed. The left and middle mouse interactively zoom the view. The
    control key can be used to enable box zoom. A box starting from left to right
    will zoom in, and a box starting from right to left will zoom out.

    ---
    - Args:
        - object: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - zoomScale (zs): Scale the zoom.
        - edit (e): Edit mode flag
    """
@overload #Overload for boxZoomCtx in ['edit']
def boxZoomCtx(object: object, i1: str = ..., i2: str = ..., i3: str = ..., zs: float = ..., e: bool = ...) -> str:
    """boxZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a box zoom context. If this
    context is used on a perspective camera, the field of view and view direction
    are changed. If the camera is orthographic, the orthographic width and eye
    point are changed. The left and middle mouse interactively zoom the view. The
    control key can be used to enable box zoom. A box starting from left to right
    will zoom in, and a box starting from right to left will zoom out.

    ---
    - Args:
        - object: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - zoomScale (zs): Scale the zoom.
        - edit (e): Edit mode flag
    """
@overload #Overload for boxZoomCtx in ['edit']
def boxZoomCtx(object: object, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., zoomScale: float = ..., zs: float = ..., edit: bool = ..., e: bool = ...) -> str:
    """boxZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a box zoom context. If this
    context is used on a perspective camera, the field of view and view direction
    are changed. If the camera is orthographic, the orthographic width and eye
    point are changed. The left and middle mouse interactively zoom the view. The
    control key can be used to enable box zoom. A box starting from left to right
    will zoom in, and a box starting from right to left will zoom out.

    ---
    - Args:
        - object: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - zoomScale (zs): Scale the zoom.
        - edit (e): Edit mode flag
    """
