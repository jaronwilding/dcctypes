"""Stub files for Contexts category in Maya commands, command: trackCtx."""

from typing import Any, overload

@overload #Overload for trackCtx in ['create']
def trackCtx(alternateContext: bool = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., toolName: str = ..., trackGeometry: bool = ..., trackScale: float = ...) -> str:
    """trackCtx is undoable, queryable, and editable.
    
    This command can be used to create a track context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - toolName (tn): Name of the specific tool to which this command refers.
        - trackGeometry (tg): Toggle whether the drag should try to track geometry. The context will compute a track plane by intersecting the initial press with geometry or the live object.
        - trackScale (ts): Specify the distance to the track plane from the camera. The smaller the scale the slower the drag.
    """
@overload #Overload for trackCtx in ['create']
def trackCtx(ac: bool = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., tn: str = ..., tg: bool = ..., ts: float = ...) -> str:
    """trackCtx is undoable, queryable, and editable.
    
    This command can be used to create a track context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - toolName (tn): Name of the specific tool to which this command refers.
        - trackGeometry (tg): Toggle whether the drag should try to track geometry. The context will compute a track plane by intersecting the initial press with geometry or the live object.
        - trackScale (ts): Specify the distance to the track plane from the camera. The smaller the scale the slower the drag.
    """
@overload #Overload for trackCtx in ['create']
def trackCtx(alternateContext: bool = ..., ac: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., toolName: str = ..., tn: str = ..., trackGeometry: bool = ..., tg: bool = ..., trackScale: float = ..., ts: float = ...) -> str:
    """trackCtx is undoable, queryable, and editable.
    
    This command can be used to create a track context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - toolName (tn): Name of the specific tool to which this command refers.
        - trackGeometry (tg): Toggle whether the drag should try to track geometry. The context will compute a track plane by intersecting the initial press with geometry or the live object.
        - trackScale (ts): Specify the distance to the track plane from the camera. The smaller the scale the slower the drag.
    """
@overload #Overload for trackCtx in ['query']
def trackCtx(alternateContext: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., toolName: str = ..., trackGeometry: bool = ..., trackScale: float = ..., query: bool = ...) -> str:
    """trackCtx is undoable, queryable, and editable.
    
    This command can be used to create a track context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - trackGeometry (tg): Toggle whether the drag should try to track geometry. The context will compute a track plane by intersecting the initial press with geometry or the live object.
        - trackScale (ts): Specify the distance to the track plane from the camera. The smaller the scale the slower the drag.
        - query (q): Query mode flag
    """
@overload #Overload for trackCtx in ['query']
def trackCtx(ac: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., tn: str = ..., tg: bool = ..., ts: float = ..., q: bool = ...) -> str:
    """trackCtx is undoable, queryable, and editable.
    
    This command can be used to create a track context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - trackGeometry (tg): Toggle whether the drag should try to track geometry. The context will compute a track plane by intersecting the initial press with geometry or the live object.
        - trackScale (ts): Specify the distance to the track plane from the camera. The smaller the scale the slower the drag.
        - query (q): Query mode flag
    """
@overload #Overload for trackCtx in ['query']
def trackCtx(alternateContext: bool = ..., ac: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., toolName: str = ..., tn: str = ..., trackGeometry: bool = ..., tg: bool = ..., trackScale: float = ..., ts: float = ..., query: bool = ..., q: bool = ...) -> str:
    """trackCtx is undoable, queryable, and editable.
    
    This command can be used to create a track context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - trackGeometry (tg): Toggle whether the drag should try to track geometry. The context will compute a track plane by intersecting the initial press with geometry or the live object.
        - trackScale (ts): Specify the distance to the track plane from the camera. The smaller the scale the slower the drag.
        - query (q): Query mode flag
    """
@overload #Overload for trackCtx in ['edit']
def trackCtx(alternateContext: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., toolName: str = ..., trackGeometry: bool = ..., trackScale: float = ..., edit: bool = ...) -> str:
    """trackCtx is undoable, queryable, and editable.
    
    This command can be used to create a track context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - trackGeometry (tg): Toggle whether the drag should try to track geometry. The context will compute a track plane by intersecting the initial press with geometry or the live object.
        - trackScale (ts): Specify the distance to the track plane from the camera. The smaller the scale the slower the drag.
        - edit (e): Edit mode flag
    """
@overload #Overload for trackCtx in ['edit']
def trackCtx(ac: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., tn: str = ..., tg: bool = ..., ts: float = ..., e: bool = ...) -> str:
    """trackCtx is undoable, queryable, and editable.
    
    This command can be used to create a track context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - trackGeometry (tg): Toggle whether the drag should try to track geometry. The context will compute a track plane by intersecting the initial press with geometry or the live object.
        - trackScale (ts): Specify the distance to the track plane from the camera. The smaller the scale the slower the drag.
        - edit (e): Edit mode flag
    """
@overload #Overload for trackCtx in ['edit']
def trackCtx(alternateContext: bool = ..., ac: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., toolName: str = ..., tn: str = ..., trackGeometry: bool = ..., tg: bool = ..., trackScale: float = ..., ts: float = ..., edit: bool = ..., e: bool = ...) -> str:
    """trackCtx is undoable, queryable, and editable.
    
    This command can be used to create a track context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - trackGeometry (tg): Toggle whether the drag should try to track geometry. The context will compute a track plane by intersecting the initial press with geometry or the live object.
        - trackScale (ts): Specify the distance to the track plane from the camera. The smaller the scale the slower the drag.
        - edit (e): Edit mode flag
    """
