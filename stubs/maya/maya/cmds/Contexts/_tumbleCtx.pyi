"""Stub files for Contexts category in Maya commands, command: tumbleCtx."""

from typing import Any, overload

@overload #Overload for tumbleCtx in ['create']
def tumbleCtx(alternateContext: bool = ..., autoOrthoConstrain: bool = ..., autoSetPivot: bool = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., localTumble: int = ..., name: str = ..., objectTumble: bool = ..., orthoLock: bool = ..., orthoStep: angle = ..., toolName: str = ..., tumbleScale: float = ...) -> str:
    """tumbleCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a tumble context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - autoOrthoConstrain (aoc): Automatically constrain horizontal and vertical rotations when the camera is orthographic. The shift key can be used to unconstrain the rotation.
        - autoSetPivot (asp): Automatically set the camera pivot to the selection or tool effect region
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localTumble (lt): Describes what point the camera will tumble around:0 for the camera's tumble pivot1 for the camera's center of interest2 for the camera's local axis, offset by its tumble pivot
        - name (n): If this is a tool command, name the tool appropriately.
        - objectTumble (ot): Make the camera tumble around the selected object, if true.
        - orthoLock (ol): Orthographic cameras cannot be tumbled while orthoLock is on.
        - orthoStep (os): Specify the angular step in degrees for orthographic rotation. If camera is orthographic and autoOrthoConstrain is toggled on the rotation will be stepped by this amount.
        - toolName (tn): Name of the specific tool to which this command refers.
        - tumbleScale (ts): Set the rotation speed. A tumble scale of 1.0 will result in in 40 degrees of rotation per 100 pixels of cursor drag.
    """
@overload #Overload for tumbleCtx in ['create']
def tumbleCtx(ac: bool = ..., aoc: bool = ..., asp: bool = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., lt: int = ..., n: str = ..., ot: bool = ..., ol: bool = ..., os: angle = ..., tn: str = ..., ts: float = ...) -> str:
    """tumbleCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a tumble context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - autoOrthoConstrain (aoc): Automatically constrain horizontal and vertical rotations when the camera is orthographic. The shift key can be used to unconstrain the rotation.
        - autoSetPivot (asp): Automatically set the camera pivot to the selection or tool effect region
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localTumble (lt): Describes what point the camera will tumble around:0 for the camera's tumble pivot1 for the camera's center of interest2 for the camera's local axis, offset by its tumble pivot
        - name (n): If this is a tool command, name the tool appropriately.
        - objectTumble (ot): Make the camera tumble around the selected object, if true.
        - orthoLock (ol): Orthographic cameras cannot be tumbled while orthoLock is on.
        - orthoStep (os): Specify the angular step in degrees for orthographic rotation. If camera is orthographic and autoOrthoConstrain is toggled on the rotation will be stepped by this amount.
        - toolName (tn): Name of the specific tool to which this command refers.
        - tumbleScale (ts): Set the rotation speed. A tumble scale of 1.0 will result in in 40 degrees of rotation per 100 pixels of cursor drag.
    """
@overload #Overload for tumbleCtx in ['create']
def tumbleCtx(alternateContext: bool = ..., ac: bool = ..., autoOrthoConstrain: bool = ..., aoc: bool = ..., autoSetPivot: bool = ..., asp: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., localTumble: int = ..., lt: int = ..., name: str = ..., n: str = ..., objectTumble: bool = ..., ot: bool = ..., orthoLock: bool = ..., ol: bool = ..., orthoStep: angle = ..., os: angle = ..., toolName: str = ..., tn: str = ..., tumbleScale: float = ..., ts: float = ...) -> str:
    """tumbleCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a tumble context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - autoOrthoConstrain (aoc): Automatically constrain horizontal and vertical rotations when the camera is orthographic. The shift key can be used to unconstrain the rotation.
        - autoSetPivot (asp): Automatically set the camera pivot to the selection or tool effect region
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localTumble (lt): Describes what point the camera will tumble around:0 for the camera's tumble pivot1 for the camera's center of interest2 for the camera's local axis, offset by its tumble pivot
        - name (n): If this is a tool command, name the tool appropriately.
        - objectTumble (ot): Make the camera tumble around the selected object, if true.
        - orthoLock (ol): Orthographic cameras cannot be tumbled while orthoLock is on.
        - orthoStep (os): Specify the angular step in degrees for orthographic rotation. If camera is orthographic and autoOrthoConstrain is toggled on the rotation will be stepped by this amount.
        - toolName (tn): Name of the specific tool to which this command refers.
        - tumbleScale (ts): Set the rotation speed. A tumble scale of 1.0 will result in in 40 degrees of rotation per 100 pixels of cursor drag.
    """
@overload #Overload for tumbleCtx in ['query']
def tumbleCtx(alternateContext: bool = ..., autoOrthoConstrain: bool = ..., autoSetPivot: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., localTumble: int = ..., objectTumble: bool = ..., orthoLock: bool = ..., orthoStep: angle = ..., toolName: str = ..., tumbleScale: float = ..., query: bool = ...) -> str:
    """tumbleCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a tumble context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - autoOrthoConstrain (aoc): Automatically constrain horizontal and vertical rotations when the camera is orthographic. The shift key can be used to unconstrain the rotation.
        - autoSetPivot (asp): Automatically set the camera pivot to the selection or tool effect region
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localTumble (lt): Describes what point the camera will tumble around:0 for the camera's tumble pivot1 for the camera's center of interest2 for the camera's local axis, offset by its tumble pivot
        - objectTumble (ot): Make the camera tumble around the selected object, if true.
        - orthoLock (ol): Orthographic cameras cannot be tumbled while orthoLock is on.
        - orthoStep (os): Specify the angular step in degrees for orthographic rotation. If camera is orthographic and autoOrthoConstrain is toggled on the rotation will be stepped by this amount.
        - toolName (tn): Name of the specific tool to which this command refers.
        - tumbleScale (ts): Set the rotation speed. A tumble scale of 1.0 will result in in 40 degrees of rotation per 100 pixels of cursor drag.
        - query (q): Query mode flag
    """
@overload #Overload for tumbleCtx in ['query']
def tumbleCtx(ac: bool = ..., aoc: bool = ..., asp: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., lt: int = ..., ot: bool = ..., ol: bool = ..., os: angle = ..., tn: str = ..., ts: float = ..., q: bool = ...) -> str:
    """tumbleCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a tumble context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - autoOrthoConstrain (aoc): Automatically constrain horizontal and vertical rotations when the camera is orthographic. The shift key can be used to unconstrain the rotation.
        - autoSetPivot (asp): Automatically set the camera pivot to the selection or tool effect region
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localTumble (lt): Describes what point the camera will tumble around:0 for the camera's tumble pivot1 for the camera's center of interest2 for the camera's local axis, offset by its tumble pivot
        - objectTumble (ot): Make the camera tumble around the selected object, if true.
        - orthoLock (ol): Orthographic cameras cannot be tumbled while orthoLock is on.
        - orthoStep (os): Specify the angular step in degrees for orthographic rotation. If camera is orthographic and autoOrthoConstrain is toggled on the rotation will be stepped by this amount.
        - toolName (tn): Name of the specific tool to which this command refers.
        - tumbleScale (ts): Set the rotation speed. A tumble scale of 1.0 will result in in 40 degrees of rotation per 100 pixels of cursor drag.
        - query (q): Query mode flag
    """
@overload #Overload for tumbleCtx in ['query']
def tumbleCtx(alternateContext: bool = ..., ac: bool = ..., autoOrthoConstrain: bool = ..., aoc: bool = ..., autoSetPivot: bool = ..., asp: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., localTumble: int = ..., lt: int = ..., objectTumble: bool = ..., ot: bool = ..., orthoLock: bool = ..., ol: bool = ..., orthoStep: angle = ..., os: angle = ..., toolName: str = ..., tn: str = ..., tumbleScale: float = ..., ts: float = ..., query: bool = ..., q: bool = ...) -> str:
    """tumbleCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a tumble context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - autoOrthoConstrain (aoc): Automatically constrain horizontal and vertical rotations when the camera is orthographic. The shift key can be used to unconstrain the rotation.
        - autoSetPivot (asp): Automatically set the camera pivot to the selection or tool effect region
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localTumble (lt): Describes what point the camera will tumble around:0 for the camera's tumble pivot1 for the camera's center of interest2 for the camera's local axis, offset by its tumble pivot
        - objectTumble (ot): Make the camera tumble around the selected object, if true.
        - orthoLock (ol): Orthographic cameras cannot be tumbled while orthoLock is on.
        - orthoStep (os): Specify the angular step in degrees for orthographic rotation. If camera is orthographic and autoOrthoConstrain is toggled on the rotation will be stepped by this amount.
        - toolName (tn): Name of the specific tool to which this command refers.
        - tumbleScale (ts): Set the rotation speed. A tumble scale of 1.0 will result in in 40 degrees of rotation per 100 pixels of cursor drag.
        - query (q): Query mode flag
    """
@overload #Overload for tumbleCtx in ['edit']
def tumbleCtx(alternateContext: bool = ..., autoOrthoConstrain: bool = ..., autoSetPivot: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., localTumble: int = ..., objectTumble: bool = ..., orthoLock: bool = ..., orthoStep: angle = ..., toolName: str = ..., tumbleScale: float = ..., edit: bool = ...) -> str:
    """tumbleCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a tumble context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - autoOrthoConstrain (aoc): Automatically constrain horizontal and vertical rotations when the camera is orthographic. The shift key can be used to unconstrain the rotation.
        - autoSetPivot (asp): Automatically set the camera pivot to the selection or tool effect region
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localTumble (lt): Describes what point the camera will tumble around:0 for the camera's tumble pivot1 for the camera's center of interest2 for the camera's local axis, offset by its tumble pivot
        - objectTumble (ot): Make the camera tumble around the selected object, if true.
        - orthoLock (ol): Orthographic cameras cannot be tumbled while orthoLock is on.
        - orthoStep (os): Specify the angular step in degrees for orthographic rotation. If camera is orthographic and autoOrthoConstrain is toggled on the rotation will be stepped by this amount.
        - toolName (tn): Name of the specific tool to which this command refers.
        - tumbleScale (ts): Set the rotation speed. A tumble scale of 1.0 will result in in 40 degrees of rotation per 100 pixels of cursor drag.
        - edit (e): Edit mode flag
    """
@overload #Overload for tumbleCtx in ['edit']
def tumbleCtx(ac: bool = ..., aoc: bool = ..., asp: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., lt: int = ..., ot: bool = ..., ol: bool = ..., os: angle = ..., tn: str = ..., ts: float = ..., e: bool = ...) -> str:
    """tumbleCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a tumble context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - autoOrthoConstrain (aoc): Automatically constrain horizontal and vertical rotations when the camera is orthographic. The shift key can be used to unconstrain the rotation.
        - autoSetPivot (asp): Automatically set the camera pivot to the selection or tool effect region
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localTumble (lt): Describes what point the camera will tumble around:0 for the camera's tumble pivot1 for the camera's center of interest2 for the camera's local axis, offset by its tumble pivot
        - objectTumble (ot): Make the camera tumble around the selected object, if true.
        - orthoLock (ol): Orthographic cameras cannot be tumbled while orthoLock is on.
        - orthoStep (os): Specify the angular step in degrees for orthographic rotation. If camera is orthographic and autoOrthoConstrain is toggled on the rotation will be stepped by this amount.
        - toolName (tn): Name of the specific tool to which this command refers.
        - tumbleScale (ts): Set the rotation speed. A tumble scale of 1.0 will result in in 40 degrees of rotation per 100 pixels of cursor drag.
        - edit (e): Edit mode flag
    """
@overload #Overload for tumbleCtx in ['edit']
def tumbleCtx(alternateContext: bool = ..., ac: bool = ..., autoOrthoConstrain: bool = ..., aoc: bool = ..., autoSetPivot: bool = ..., asp: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., localTumble: int = ..., lt: int = ..., objectTumble: bool = ..., ot: bool = ..., orthoLock: bool = ..., ol: bool = ..., orthoStep: angle = ..., os: angle = ..., toolName: str = ..., tn: str = ..., tumbleScale: float = ..., ts: float = ..., edit: bool = ..., e: bool = ...) -> str:
    """tumbleCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a tumble context.

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - autoOrthoConstrain (aoc): Automatically constrain horizontal and vertical rotations when the camera is orthographic. The shift key can be used to unconstrain the rotation.
        - autoSetPivot (asp): Automatically set the camera pivot to the selection or tool effect region
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localTumble (lt): Describes what point the camera will tumble around:0 for the camera's tumble pivot1 for the camera's center of interest2 for the camera's local axis, offset by its tumble pivot
        - objectTumble (ot): Make the camera tumble around the selected object, if true.
        - orthoLock (ol): Orthographic cameras cannot be tumbled while orthoLock is on.
        - orthoStep (os): Specify the angular step in degrees for orthographic rotation. If camera is orthographic and autoOrthoConstrain is toggled on the rotation will be stepped by this amount.
        - toolName (tn): Name of the specific tool to which this command refers.
        - tumbleScale (ts): Set the rotation speed. A tumble scale of 1.0 will result in in 40 degrees of rotation per 100 pixels of cursor drag.
        - edit (e): Edit mode flag
    """
