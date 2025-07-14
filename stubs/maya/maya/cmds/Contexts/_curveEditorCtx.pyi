"""Stub files for Contexts category in Maya commands, command: curveEditorCtx."""

from typing import Any, overload

@overload #Overload for curveEditorCtx in ['create']
def curveEditorCtx(exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., relativeTangentSize: float = ..., title: str = ...) -> str:
    """curveEditorCtx is undoable, queryable, and editable.
    
    The curveEditorCtx command creates a new NURBS editor context, which is used
    to edit a NURBS curve or surface.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - relativeTangentSize (rts): Relative size of the tangent manipulator handle.  Helps to adjust as the surface parameterization controls the size of the tangent, even if the shape of the surface remains the same. The default is 4.
        - title (t): The title for the tool.
    """
@overload #Overload for curveEditorCtx in ['create']
def curveEditorCtx(ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., rts: float = ..., t: str = ...) -> str:
    """curveEditorCtx is undoable, queryable, and editable.
    
    The curveEditorCtx command creates a new NURBS editor context, which is used
    to edit a NURBS curve or surface.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - relativeTangentSize (rts): Relative size of the tangent manipulator handle.  Helps to adjust as the surface parameterization controls the size of the tangent, even if the shape of the surface remains the same. The default is 4.
        - title (t): The title for the tool.
    """
@overload #Overload for curveEditorCtx in ['create']
def curveEditorCtx(exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., relativeTangentSize: float = ..., rts: float = ..., title: str = ..., t: str = ...) -> str:
    """curveEditorCtx is undoable, queryable, and editable.
    
    The curveEditorCtx command creates a new NURBS editor context, which is used
    to edit a NURBS curve or surface.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - relativeTangentSize (rts): Relative size of the tangent manipulator handle.  Helps to adjust as the surface parameterization controls the size of the tangent, even if the shape of the surface remains the same. The default is 4.
        - title (t): The title for the tool.
    """
@overload #Overload for curveEditorCtx in ['query']
def curveEditorCtx(direction: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., relativeTangentSize: float = ..., title: str = ..., query: bool = ...) -> str:
    """curveEditorCtx is undoable, queryable, and editable.
    
    The curveEditorCtx command creates a new NURBS editor context, which is used
    to edit a NURBS curve or surface.

    ---
    - Args:
        - direction (dir): Query the current direction of the tangent control.  Always zero for the curve case.  In the surface case, its 0 for the normal direction, 1 for U direction and 2 for V direction.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - relativeTangentSize (rts): Relative size of the tangent manipulator handle.  Helps to adjust as the surface parameterization controls the size of the tangent, even if the shape of the surface remains the same. The default is 4.
        - title (t): The title for the tool.
        - query (q): Query mode flag
    """
@overload #Overload for curveEditorCtx in ['query']
def curveEditorCtx(dir: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., rts: float = ..., t: str = ..., q: bool = ...) -> str:
    """curveEditorCtx is undoable, queryable, and editable.
    
    The curveEditorCtx command creates a new NURBS editor context, which is used
    to edit a NURBS curve or surface.

    ---
    - Args:
        - direction (dir): Query the current direction of the tangent control.  Always zero for the curve case.  In the surface case, its 0 for the normal direction, 1 for U direction and 2 for V direction.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - relativeTangentSize (rts): Relative size of the tangent manipulator handle.  Helps to adjust as the surface parameterization controls the size of the tangent, even if the shape of the surface remains the same. The default is 4.
        - title (t): The title for the tool.
        - query (q): Query mode flag
    """
@overload #Overload for curveEditorCtx in ['query']
def curveEditorCtx(direction: int = ..., dir: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., relativeTangentSize: float = ..., rts: float = ..., title: str = ..., t: str = ..., query: bool = ..., q: bool = ...) -> str:
    """curveEditorCtx is undoable, queryable, and editable.
    
    The curveEditorCtx command creates a new NURBS editor context, which is used
    to edit a NURBS curve or surface.

    ---
    - Args:
        - direction (dir): Query the current direction of the tangent control.  Always zero for the curve case.  In the surface case, its 0 for the normal direction, 1 for U direction and 2 for V direction.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - relativeTangentSize (rts): Relative size of the tangent manipulator handle.  Helps to adjust as the surface parameterization controls the size of the tangent, even if the shape of the surface remains the same. The default is 4.
        - title (t): The title for the tool.
        - query (q): Query mode flag
    """
@overload #Overload for curveEditorCtx in ['edit']
def curveEditorCtx(image1: str = ..., image2: str = ..., image3: str = ..., relativeTangentSize: float = ..., title: str = ..., edit: bool = ...) -> str:
    """curveEditorCtx is undoable, queryable, and editable.
    
    The curveEditorCtx command creates a new NURBS editor context, which is used
    to edit a NURBS curve or surface.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - relativeTangentSize (rts): Relative size of the tangent manipulator handle.  Helps to adjust as the surface parameterization controls the size of the tangent, even if the shape of the surface remains the same. The default is 4.
        - title (t): The title for the tool.
        - edit (e): Edit mode flag
    """
@overload #Overload for curveEditorCtx in ['edit']
def curveEditorCtx(i1: str = ..., i2: str = ..., i3: str = ..., rts: float = ..., t: str = ..., e: bool = ...) -> str:
    """curveEditorCtx is undoable, queryable, and editable.
    
    The curveEditorCtx command creates a new NURBS editor context, which is used
    to edit a NURBS curve or surface.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - relativeTangentSize (rts): Relative size of the tangent manipulator handle.  Helps to adjust as the surface parameterization controls the size of the tangent, even if the shape of the surface remains the same. The default is 4.
        - title (t): The title for the tool.
        - edit (e): Edit mode flag
    """
@overload #Overload for curveEditorCtx in ['edit']
def curveEditorCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., relativeTangentSize: float = ..., rts: float = ..., title: str = ..., t: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """curveEditorCtx is undoable, queryable, and editable.
    
    The curveEditorCtx command creates a new NURBS editor context, which is used
    to edit a NURBS curve or surface.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - relativeTangentSize (rts): Relative size of the tangent manipulator handle.  Helps to adjust as the surface parameterization controls the size of the tangent, even if the shape of the surface remains the same. The default is 4.
        - title (t): The title for the tool.
        - edit (e): Edit mode flag
    """
