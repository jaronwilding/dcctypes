"""Stub files for Contexts category in Maya commands, command: panZoomCtx."""

from typing import Any, overload

@overload #Overload for panZoomCtx in ['create']
def panZoomCtx(alternateContext: bool = ..., buttonDown: bool = ..., buttonUp: bool = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., panMode: bool = ..., toolName: str = ..., zoomMode: bool = ..., zoomScale: float = ...) -> str:
    """panZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create camera 2D pan/zoom context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - buttonDown (btd): Perform the button down operation
        - buttonUp (btu): Perform the button up operation
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - panMode (pm): Specify to create a camera 2D pan context, which is the default.
        - toolName (tn): Name of the specific tool to which this command refers.
        - zoomMode (zm): Specify to create a camera 2D zoom context.
        - zoomScale (zs): Scale the zoom. The smaller the scale the slower the drag.
    """
@overload #Overload for panZoomCtx in ['create']
def panZoomCtx(ac: bool = ..., btd: bool = ..., btu: bool = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., pm: bool = ..., tn: str = ..., zm: bool = ..., zs: float = ...) -> str:
    """panZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create camera 2D pan/zoom context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - buttonDown (btd): Perform the button down operation
        - buttonUp (btu): Perform the button up operation
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - panMode (pm): Specify to create a camera 2D pan context, which is the default.
        - toolName (tn): Name of the specific tool to which this command refers.
        - zoomMode (zm): Specify to create a camera 2D zoom context.
        - zoomScale (zs): Scale the zoom. The smaller the scale the slower the drag.
    """
@overload #Overload for panZoomCtx in ['create']
def panZoomCtx(alternateContext: bool = ..., ac: bool = ..., buttonDown: bool = ..., btd: bool = ..., buttonUp: bool = ..., btu: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., panMode: bool = ..., pm: bool = ..., toolName: str = ..., tn: str = ..., zoomMode: bool = ..., zm: bool = ..., zoomScale: float = ..., zs: float = ...) -> str:
    """panZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create camera 2D pan/zoom context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - buttonDown (btd): Perform the button down operation
        - buttonUp (btu): Perform the button up operation
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - panMode (pm): Specify to create a camera 2D pan context, which is the default.
        - toolName (tn): Name of the specific tool to which this command refers.
        - zoomMode (zm): Specify to create a camera 2D zoom context.
        - zoomScale (zs): Scale the zoom. The smaller the scale the slower the drag.
    """
@overload #Overload for panZoomCtx in ['query']
def panZoomCtx(alternateContext: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., toolName: str = ..., zoomScale: float = ..., query: bool = ...) -> str:
    """panZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create camera 2D pan/zoom context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - zoomScale (zs): Scale the zoom. The smaller the scale the slower the drag.
        - query (q): Query mode flag
    """
@overload #Overload for panZoomCtx in ['query']
def panZoomCtx(ac: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., tn: str = ..., zs: float = ..., q: bool = ...) -> str:
    """panZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create camera 2D pan/zoom context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - zoomScale (zs): Scale the zoom. The smaller the scale the slower the drag.
        - query (q): Query mode flag
    """
@overload #Overload for panZoomCtx in ['query']
def panZoomCtx(alternateContext: bool = ..., ac: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., toolName: str = ..., tn: str = ..., zoomScale: float = ..., zs: float = ..., query: bool = ..., q: bool = ...) -> str:
    """panZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create camera 2D pan/zoom context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - zoomScale (zs): Scale the zoom. The smaller the scale the slower the drag.
        - query (q): Query mode flag
    """
@overload #Overload for panZoomCtx in ['edit']
def panZoomCtx(alternateContext: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., toolName: str = ..., zoomScale: float = ..., edit: bool = ...) -> str:
    """panZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create camera 2D pan/zoom context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - zoomScale (zs): Scale the zoom. The smaller the scale the slower the drag.
        - edit (e): Edit mode flag
    """
@overload #Overload for panZoomCtx in ['edit']
def panZoomCtx(ac: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., tn: str = ..., zs: float = ..., e: bool = ...) -> str:
    """panZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create camera 2D pan/zoom context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - zoomScale (zs): Scale the zoom. The smaller the scale the slower the drag.
        - edit (e): Edit mode flag
    """
@overload #Overload for panZoomCtx in ['edit']
def panZoomCtx(alternateContext: bool = ..., ac: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., toolName: str = ..., tn: str = ..., zoomScale: float = ..., zs: float = ..., edit: bool = ..., e: bool = ...) -> str:
    """panZoomCtx is undoable, queryable, and editable.
    
    This command can be used to create camera 2D pan/zoom context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - zoomScale (zs): Scale the zoom. The smaller the scale the slower the drag.
        - edit (e): Edit mode flag
    """
