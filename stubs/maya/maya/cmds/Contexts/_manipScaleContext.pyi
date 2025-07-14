"""Stub files for Contexts category in Maya commands, command: manipScaleContext."""

from typing import Any, overload

@overload #Overload for manipScaleContext in ['create']
def manipScaleContext([object]: [object], activeHandle: int = ..., alignAlong: [float, float, float] = ..., bakePivotOri: bool = ..., constrainAlongNormal: bool = ..., currentActiveHandle: int = ..., exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., mode: int = ..., orientAxes: [float, float, float] = ..., orientObject: str = ..., orientTowards: [float, float, float] = ..., pinPivot: bool = ..., pivotOriHandle: bool = ..., postCommand: script = ..., postDragCommand: [script, string] = ..., preCommand: script = ..., preDragCommand: [script, string] = ..., preserveChildPosition: bool = ..., preserveUV: bool = ..., resetPivotMode: int = ..., scale: [float, float, float] = ..., snap: bool = ..., snapPivotOri: bool = ..., snapPivotPos: bool = ..., snapRelative: bool = ..., snapValue: float = ..., tweakMode: bool = ..., useManipPivot: bool = ..., useObjectPivot: bool = ..., xformConstraint: str = ...) -> str:
    """manipScaleContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a scale manip context.

    ---
    - Args:
        - [object]: Input item(s).
        - activeHandle (ah): Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
            (all axes) is active (default)
        - alignAlong (aa): Aligns active handle along vector.
        - bakePivotOri (bpo): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - currentActiveHandle (cah): Sets the active handle for the manip. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle (all axes) is active4 - XY plane handle is active5 - YZ plane handle is active6 - XZ
            plane handle is active
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Scale mode:0 - Object Space1 - Local Space2 - World Space (default)3 - Scale Along Vertex Normal4 - Scale Along Rotation Axis5 - Scale Along Live Object Axis6 - Custom Axis Orientation10 - Component Space
        - orientAxes (oa): Orients manipulator rotating around axes by specified angles
        - orientObject (oo): Orients manipulator to the passed in object/component
        - orientTowards (ot): Orients active handle towards world point
        - pinPivot (pin): Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        - pivotOriHandle (poh): When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        - postCommand (psc): Specifies a command to be executed when the tool is exited.
        - postDragCommand (pod): Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        - preCommand (prc): Specifies a command to be executed when the tool is entered.
        - preDragCommand (prd): Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        - preserveChildPosition (pcp): When false, the children objects move when their parent is rotated. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        - preserveUV (puv): When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        - resetPivotMode (rpm): Specifies the mode used when resetting the pivot position. Available modes are:0: Center pivot (on bounding box)1: Zero pivot (object-space origin)
        - scale (sc): Returns the scale of the manipulator for its current orientation/mode.
        - snap (s): Specify that the manipulation is to use absolute snap
        - snapPivotOri (spo): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        - snapPivotPos (spp): Snap pivot position. Modify pivot position when snapping the pivot to a component.
        - snapRelative (sr): Specify that the manipulation is to use relative snap
        - snapValue (sv): Specify the snapping value
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and scaled in one step using a click-drag interaction.
        - useManipPivot (ump): Specify whether to pivot on the manip
        - useObjectPivot (uop): Specify whether to pivot on the object
        - xformConstraint (xc): none - no transform constraintedge - edge transform constraintsurface - surface transform constraint
    """
@overload #Overload for manipScaleContext in ['create']
def manipScaleContext([object]: [object], ah: int = ..., aa: [float, float, float] = ..., bpo: bool = ..., xn: bool = ..., cah: int = ..., ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., m: int = ..., oa: [float, float, float] = ..., oo: str = ..., ot: [float, float, float] = ..., pin: bool = ..., poh: bool = ..., psc: script = ..., pod: [script, string] = ..., prc: script = ..., prd: [script, string] = ..., pcp: bool = ..., puv: bool = ..., rpm: int = ..., sc: [float, float, float] = ..., s: bool = ..., spo: bool = ..., spp: bool = ..., sr: bool = ..., sv: float = ..., twk: bool = ..., ump: bool = ..., uop: bool = ..., xc: str = ...) -> str:
    """manipScaleContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a scale manip context.

    ---
    - Args:
        - [object]: Input item(s).
        - activeHandle (ah): Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
            (all axes) is active (default)
        - alignAlong (aa): Aligns active handle along vector.
        - bakePivotOri (bpo): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - currentActiveHandle (cah): Sets the active handle for the manip. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle (all axes) is active4 - XY plane handle is active5 - YZ plane handle is active6 - XZ
            plane handle is active
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Scale mode:0 - Object Space1 - Local Space2 - World Space (default)3 - Scale Along Vertex Normal4 - Scale Along Rotation Axis5 - Scale Along Live Object Axis6 - Custom Axis Orientation10 - Component Space
        - orientAxes (oa): Orients manipulator rotating around axes by specified angles
        - orientObject (oo): Orients manipulator to the passed in object/component
        - orientTowards (ot): Orients active handle towards world point
        - pinPivot (pin): Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        - pivotOriHandle (poh): When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        - postCommand (psc): Specifies a command to be executed when the tool is exited.
        - postDragCommand (pod): Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        - preCommand (prc): Specifies a command to be executed when the tool is entered.
        - preDragCommand (prd): Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        - preserveChildPosition (pcp): When false, the children objects move when their parent is rotated. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        - preserveUV (puv): When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        - resetPivotMode (rpm): Specifies the mode used when resetting the pivot position. Available modes are:0: Center pivot (on bounding box)1: Zero pivot (object-space origin)
        - scale (sc): Returns the scale of the manipulator for its current orientation/mode.
        - snap (s): Specify that the manipulation is to use absolute snap
        - snapPivotOri (spo): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        - snapPivotPos (spp): Snap pivot position. Modify pivot position when snapping the pivot to a component.
        - snapRelative (sr): Specify that the manipulation is to use relative snap
        - snapValue (sv): Specify the snapping value
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and scaled in one step using a click-drag interaction.
        - useManipPivot (ump): Specify whether to pivot on the manip
        - useObjectPivot (uop): Specify whether to pivot on the object
        - xformConstraint (xc): none - no transform constraintedge - edge transform constraintsurface - surface transform constraint
    """
@overload #Overload for manipScaleContext in ['create']
def manipScaleContext([object]: [object], activeHandle: int = ..., ah: int = ..., alignAlong: [float, float, float] = ..., aa: [float, float, float] = ..., bakePivotOri: bool = ..., bpo: bool = ..., constrainAlongNormal: bool = ..., xn: bool = ..., currentActiveHandle: int = ..., cah: int = ..., exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., mode: int = ..., m: int = ..., orientAxes: [float, float, float] = ..., oa: [float, float, float] = ..., orientObject: str = ..., oo: str = ..., orientTowards: [float, float, float] = ..., ot: [float, float, float] = ..., pinPivot: bool = ..., pin: bool = ..., pivotOriHandle: bool = ..., poh: bool = ..., postCommand: script = ..., psc: script = ..., postDragCommand: [script, string] = ..., pod: [script, string] = ..., preCommand: script = ..., prc: script = ..., preDragCommand: [script, string] = ..., prd: [script, string] = ..., preserveChildPosition: bool = ..., pcp: bool = ..., preserveUV: bool = ..., puv: bool = ..., resetPivotMode: int = ..., rpm: int = ..., scale: [float, float, float] = ..., sc: [float, float, float] = ..., snap: bool = ..., s: bool = ..., snapPivotOri: bool = ..., spo: bool = ..., snapPivotPos: bool = ..., spp: bool = ..., snapRelative: bool = ..., sr: bool = ..., snapValue: float = ..., sv: float = ..., tweakMode: bool = ..., twk: bool = ..., useManipPivot: bool = ..., ump: bool = ..., useObjectPivot: bool = ..., uop: bool = ..., xformConstraint: str = ..., xc: str = ...) -> str:
    """manipScaleContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a scale manip context.

    ---
    - Args:
        - [object]: Input item(s).
        - activeHandle (ah): Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
            (all axes) is active (default)
        - alignAlong (aa): Aligns active handle along vector.
        - bakePivotOri (bpo): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - currentActiveHandle (cah): Sets the active handle for the manip. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle (all axes) is active4 - XY plane handle is active5 - YZ plane handle is active6 - XZ
            plane handle is active
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Scale mode:0 - Object Space1 - Local Space2 - World Space (default)3 - Scale Along Vertex Normal4 - Scale Along Rotation Axis5 - Scale Along Live Object Axis6 - Custom Axis Orientation10 - Component Space
        - orientAxes (oa): Orients manipulator rotating around axes by specified angles
        - orientObject (oo): Orients manipulator to the passed in object/component
        - orientTowards (ot): Orients active handle towards world point
        - pinPivot (pin): Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        - pivotOriHandle (poh): When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        - postCommand (psc): Specifies a command to be executed when the tool is exited.
        - postDragCommand (pod): Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        - preCommand (prc): Specifies a command to be executed when the tool is entered.
        - preDragCommand (prd): Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        - preserveChildPosition (pcp): When false, the children objects move when their parent is rotated. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        - preserveUV (puv): When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        - resetPivotMode (rpm): Specifies the mode used when resetting the pivot position. Available modes are:0: Center pivot (on bounding box)1: Zero pivot (object-space origin)
        - scale (sc): Returns the scale of the manipulator for its current orientation/mode.
        - snap (s): Specify that the manipulation is to use absolute snap
        - snapPivotOri (spo): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        - snapPivotPos (spp): Snap pivot position. Modify pivot position when snapping the pivot to a component.
        - snapRelative (sr): Specify that the manipulation is to use relative snap
        - snapValue (sv): Specify the snapping value
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and scaled in one step using a click-drag interaction.
        - useManipPivot (ump): Specify whether to pivot on the manip
        - useObjectPivot (uop): Specify whether to pivot on the object
        - xformConstraint (xc): none - no transform constraintedge - edge transform constraintsurface - surface transform constraint
    """
@overload #Overload for manipScaleContext in ['query']
def manipScaleContext([object]: [object], activeHandle: int = ..., alignAlong: [float, float, float] = ..., bakePivotOri: bool = ..., constrainAlongNormal: bool = ..., currentActiveHandle: int = ..., editPivotMode: bool = ..., editPivotPosition: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., lastMode: int = ..., manipVisible: bool = ..., mode: int = ..., orientAxes: [float, float, float] = ..., orientObject: str = ..., orientTowards: [float, float, float] = ..., pinPivot: bool = ..., pivotOriHandle: bool = ..., position: bool = ..., postCommand: script = ..., postDragCommand: [script, string] = ..., preCommand: script = ..., preDragCommand: [script, string] = ..., preserveChildPosition: bool = ..., preserveUV: bool = ..., preventNegativeScale: bool = ..., resetPivotMode: int = ..., scale: [float, float, float] = ..., snap: bool = ..., snapPivotOri: bool = ..., snapPivotPos: bool = ..., snapRelative: bool = ..., snapValue: float = ..., tweakMode: bool = ..., useManipPivot: bool = ..., useObjectPivot: bool = ..., xformConstraint: str = ..., query: bool = ...) -> str:
    """manipScaleContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a scale manip context.

    ---
    - Args:
        - [object]: Input item(s).
        - activeHandle (ah): Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
            (all axes) is active (default)
        - alignAlong (aa): Aligns active handle along vector.
        - bakePivotOri (bpo): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - currentActiveHandle (cah): Sets the active handle for the manip. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle (all axes) is active4 - XY plane handle is active5 - YZ plane handle is active6 - XZ
            plane handle is active
        - editPivotMode (epm): Returns true manipulator is in edit pivot mode
        - editPivotPosition (epp): Returns the current position of the edit pivot manipulator.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - lastMode (lm): Returns the previous scaling mode.
        - manipVisible (vis): Returns true if the scale manipulator is visible.
        - mode (m): Scale mode:0 - Object Space1 - Local Space2 - World Space (default)3 - Scale Along Vertex Normal4 - Scale Along Rotation Axis5 - Scale Along Live Object Axis6 - Custom Axis Orientation10 - Component Space
        - orientAxes (oa): Orients manipulator rotating around axes by specified angles
        - orientObject (oo): Orients manipulator to the passed in object/component
        - orientTowards (ot): Orients active handle towards world point
        - pinPivot (pin): Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        - pivotOriHandle (poh): When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        - position (p): Returns the current position of the manipulator.
        - postCommand (psc): Specifies a command to be executed when the tool is exited.
        - postDragCommand (pod): Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        - preCommand (prc): Specifies a command to be executed when the tool is entered.
        - preDragCommand (prd): Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        - preserveChildPosition (pcp): When false, the children objects move when their parent is rotated. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        - preserveUV (puv): When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        - preventNegativeScale (pns): When this is true, negative scale is not allowed.
        - resetPivotMode (rpm): Specifies the mode used when resetting the pivot position. Available modes are:0: Center pivot (on bounding box)1: Zero pivot (object-space origin)
        - scale (sc): Returns the scale of the manipulator for its current orientation/mode.
        - snap (s): Specify that the manipulation is to use absolute snap
        - snapPivotOri (spo): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        - snapPivotPos (spp): Snap pivot position. Modify pivot position when snapping the pivot to a component.
        - snapRelative (sr): Specify that the manipulation is to use relative snap
        - snapValue (sv): Specify the snapping value
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and scaled in one step using a click-drag interaction.
        - useManipPivot (ump): Specify whether to pivot on the manip
        - useObjectPivot (uop): Specify whether to pivot on the object
        - xformConstraint (xc): none - no transform constraintedge - edge transform constraintsurface - surface transform constraint
        - query (q): Query mode flag
    """
@overload #Overload for manipScaleContext in ['query']
def manipScaleContext([object]: [object], ah: int = ..., aa: [float, float, float] = ..., bpo: bool = ..., xn: bool = ..., cah: int = ..., epm: bool = ..., epp: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., lm: int = ..., vis: bool = ..., m: int = ..., oa: [float, float, float] = ..., oo: str = ..., ot: [float, float, float] = ..., pin: bool = ..., poh: bool = ..., p: bool = ..., psc: script = ..., pod: [script, string] = ..., prc: script = ..., prd: [script, string] = ..., pcp: bool = ..., puv: bool = ..., pns: bool = ..., rpm: int = ..., sc: [float, float, float] = ..., s: bool = ..., spo: bool = ..., spp: bool = ..., sr: bool = ..., sv: float = ..., twk: bool = ..., ump: bool = ..., uop: bool = ..., xc: str = ..., q: bool = ...) -> str:
    """manipScaleContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a scale manip context.

    ---
    - Args:
        - [object]: Input item(s).
        - activeHandle (ah): Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
            (all axes) is active (default)
        - alignAlong (aa): Aligns active handle along vector.
        - bakePivotOri (bpo): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - currentActiveHandle (cah): Sets the active handle for the manip. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle (all axes) is active4 - XY plane handle is active5 - YZ plane handle is active6 - XZ
            plane handle is active
        - editPivotMode (epm): Returns true manipulator is in edit pivot mode
        - editPivotPosition (epp): Returns the current position of the edit pivot manipulator.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - lastMode (lm): Returns the previous scaling mode.
        - manipVisible (vis): Returns true if the scale manipulator is visible.
        - mode (m): Scale mode:0 - Object Space1 - Local Space2 - World Space (default)3 - Scale Along Vertex Normal4 - Scale Along Rotation Axis5 - Scale Along Live Object Axis6 - Custom Axis Orientation10 - Component Space
        - orientAxes (oa): Orients manipulator rotating around axes by specified angles
        - orientObject (oo): Orients manipulator to the passed in object/component
        - orientTowards (ot): Orients active handle towards world point
        - pinPivot (pin): Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        - pivotOriHandle (poh): When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        - position (p): Returns the current position of the manipulator.
        - postCommand (psc): Specifies a command to be executed when the tool is exited.
        - postDragCommand (pod): Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        - preCommand (prc): Specifies a command to be executed when the tool is entered.
        - preDragCommand (prd): Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        - preserveChildPosition (pcp): When false, the children objects move when their parent is rotated. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        - preserveUV (puv): When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        - preventNegativeScale (pns): When this is true, negative scale is not allowed.
        - resetPivotMode (rpm): Specifies the mode used when resetting the pivot position. Available modes are:0: Center pivot (on bounding box)1: Zero pivot (object-space origin)
        - scale (sc): Returns the scale of the manipulator for its current orientation/mode.
        - snap (s): Specify that the manipulation is to use absolute snap
        - snapPivotOri (spo): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        - snapPivotPos (spp): Snap pivot position. Modify pivot position when snapping the pivot to a component.
        - snapRelative (sr): Specify that the manipulation is to use relative snap
        - snapValue (sv): Specify the snapping value
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and scaled in one step using a click-drag interaction.
        - useManipPivot (ump): Specify whether to pivot on the manip
        - useObjectPivot (uop): Specify whether to pivot on the object
        - xformConstraint (xc): none - no transform constraintedge - edge transform constraintsurface - surface transform constraint
        - query (q): Query mode flag
    """
@overload #Overload for manipScaleContext in ['query']
def manipScaleContext([object]: [object], activeHandle: int = ..., ah: int = ..., alignAlong: [float, float, float] = ..., aa: [float, float, float] = ..., bakePivotOri: bool = ..., bpo: bool = ..., constrainAlongNormal: bool = ..., xn: bool = ..., currentActiveHandle: int = ..., cah: int = ..., editPivotMode: bool = ..., epm: bool = ..., editPivotPosition: bool = ..., epp: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., lastMode: int = ..., lm: int = ..., manipVisible: bool = ..., vis: bool = ..., mode: int = ..., m: int = ..., orientAxes: [float, float, float] = ..., oa: [float, float, float] = ..., orientObject: str = ..., oo: str = ..., orientTowards: [float, float, float] = ..., ot: [float, float, float] = ..., pinPivot: bool = ..., pin: bool = ..., pivotOriHandle: bool = ..., poh: bool = ..., position: bool = ..., p: bool = ..., postCommand: script = ..., psc: script = ..., postDragCommand: [script, string] = ..., pod: [script, string] = ..., preCommand: script = ..., prc: script = ..., preDragCommand: [script, string] = ..., prd: [script, string] = ..., preserveChildPosition: bool = ..., pcp: bool = ..., preserveUV: bool = ..., puv: bool = ..., preventNegativeScale: bool = ..., pns: bool = ..., resetPivotMode: int = ..., rpm: int = ..., scale: [float, float, float] = ..., sc: [float, float, float] = ..., snap: bool = ..., s: bool = ..., snapPivotOri: bool = ..., spo: bool = ..., snapPivotPos: bool = ..., spp: bool = ..., snapRelative: bool = ..., sr: bool = ..., snapValue: float = ..., sv: float = ..., tweakMode: bool = ..., twk: bool = ..., useManipPivot: bool = ..., ump: bool = ..., useObjectPivot: bool = ..., uop: bool = ..., xformConstraint: str = ..., xc: str = ..., query: bool = ..., q: bool = ...) -> str:
    """manipScaleContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a scale manip context.

    ---
    - Args:
        - [object]: Input item(s).
        - activeHandle (ah): Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
            (all axes) is active (default)
        - alignAlong (aa): Aligns active handle along vector.
        - bakePivotOri (bpo): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - currentActiveHandle (cah): Sets the active handle for the manip. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle (all axes) is active4 - XY plane handle is active5 - YZ plane handle is active6 - XZ
            plane handle is active
        - editPivotMode (epm): Returns true manipulator is in edit pivot mode
        - editPivotPosition (epp): Returns the current position of the edit pivot manipulator.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - lastMode (lm): Returns the previous scaling mode.
        - manipVisible (vis): Returns true if the scale manipulator is visible.
        - mode (m): Scale mode:0 - Object Space1 - Local Space2 - World Space (default)3 - Scale Along Vertex Normal4 - Scale Along Rotation Axis5 - Scale Along Live Object Axis6 - Custom Axis Orientation10 - Component Space
        - orientAxes (oa): Orients manipulator rotating around axes by specified angles
        - orientObject (oo): Orients manipulator to the passed in object/component
        - orientTowards (ot): Orients active handle towards world point
        - pinPivot (pin): Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        - pivotOriHandle (poh): When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        - position (p): Returns the current position of the manipulator.
        - postCommand (psc): Specifies a command to be executed when the tool is exited.
        - postDragCommand (pod): Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        - preCommand (prc): Specifies a command to be executed when the tool is entered.
        - preDragCommand (prd): Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        - preserveChildPosition (pcp): When false, the children objects move when their parent is rotated. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        - preserveUV (puv): When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        - preventNegativeScale (pns): When this is true, negative scale is not allowed.
        - resetPivotMode (rpm): Specifies the mode used when resetting the pivot position. Available modes are:0: Center pivot (on bounding box)1: Zero pivot (object-space origin)
        - scale (sc): Returns the scale of the manipulator for its current orientation/mode.
        - snap (s): Specify that the manipulation is to use absolute snap
        - snapPivotOri (spo): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        - snapPivotPos (spp): Snap pivot position. Modify pivot position when snapping the pivot to a component.
        - snapRelative (sr): Specify that the manipulation is to use relative snap
        - snapValue (sv): Specify the snapping value
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and scaled in one step using a click-drag interaction.
        - useManipPivot (ump): Specify whether to pivot on the manip
        - useObjectPivot (uop): Specify whether to pivot on the object
        - xformConstraint (xc): none - no transform constraintedge - edge transform constraintsurface - surface transform constraint
        - query (q): Query mode flag
    """
@overload #Overload for manipScaleContext in ['edit']
def manipScaleContext([object]: [object], activeHandle: int = ..., alignAlong: [float, float, float] = ..., bakePivotOri: bool = ..., constrainAlongNormal: bool = ..., currentActiveHandle: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., mode: int = ..., orientAxes: [float, float, float] = ..., orientObject: str = ..., orientTowards: [float, float, float] = ..., pinPivot: bool = ..., pivotOriHandle: bool = ..., postCommand: script = ..., postDragCommand: [script, string] = ..., preCommand: script = ..., preDragCommand: [script, string] = ..., preserveChildPosition: bool = ..., preserveUV: bool = ..., resetPivotMode: int = ..., scale: [float, float, float] = ..., snap: bool = ..., snapPivotOri: bool = ..., snapPivotPos: bool = ..., snapRelative: bool = ..., snapValue: float = ..., tweakMode: bool = ..., useManipPivot: bool = ..., useObjectPivot: bool = ..., xformConstraint: str = ..., edit: bool = ...) -> str:
    """manipScaleContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a scale manip context.

    ---
    - Args:
        - [object]: Input item(s).
        - activeHandle (ah): Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
            (all axes) is active (default)
        - alignAlong (aa): Aligns active handle along vector.
        - bakePivotOri (bpo): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - currentActiveHandle (cah): Sets the active handle for the manip. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle (all axes) is active4 - XY plane handle is active5 - YZ plane handle is active6 - XZ
            plane handle is active
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Scale mode:0 - Object Space1 - Local Space2 - World Space (default)3 - Scale Along Vertex Normal4 - Scale Along Rotation Axis5 - Scale Along Live Object Axis6 - Custom Axis Orientation10 - Component Space
        - orientAxes (oa): Orients manipulator rotating around axes by specified angles
        - orientObject (oo): Orients manipulator to the passed in object/component
        - orientTowards (ot): Orients active handle towards world point
        - pinPivot (pin): Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        - pivotOriHandle (poh): When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        - postCommand (psc): Specifies a command to be executed when the tool is exited.
        - postDragCommand (pod): Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        - preCommand (prc): Specifies a command to be executed when the tool is entered.
        - preDragCommand (prd): Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        - preserveChildPosition (pcp): When false, the children objects move when their parent is rotated. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        - preserveUV (puv): When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        - resetPivotMode (rpm): Specifies the mode used when resetting the pivot position. Available modes are:0: Center pivot (on bounding box)1: Zero pivot (object-space origin)
        - scale (sc): Returns the scale of the manipulator for its current orientation/mode.
        - snap (s): Specify that the manipulation is to use absolute snap
        - snapPivotOri (spo): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        - snapPivotPos (spp): Snap pivot position. Modify pivot position when snapping the pivot to a component.
        - snapRelative (sr): Specify that the manipulation is to use relative snap
        - snapValue (sv): Specify the snapping value
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and scaled in one step using a click-drag interaction.
        - useManipPivot (ump): Specify whether to pivot on the manip
        - useObjectPivot (uop): Specify whether to pivot on the object
        - xformConstraint (xc): none - no transform constraintedge - edge transform constraintsurface - surface transform constraint
        - edit (e): Edit mode flag
    """
@overload #Overload for manipScaleContext in ['edit']
def manipScaleContext([object]: [object], ah: int = ..., aa: [float, float, float] = ..., bpo: bool = ..., xn: bool = ..., cah: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., m: int = ..., oa: [float, float, float] = ..., oo: str = ..., ot: [float, float, float] = ..., pin: bool = ..., poh: bool = ..., psc: script = ..., pod: [script, string] = ..., prc: script = ..., prd: [script, string] = ..., pcp: bool = ..., puv: bool = ..., rpm: int = ..., sc: [float, float, float] = ..., s: bool = ..., spo: bool = ..., spp: bool = ..., sr: bool = ..., sv: float = ..., twk: bool = ..., ump: bool = ..., uop: bool = ..., xc: str = ..., e: bool = ...) -> str:
    """manipScaleContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a scale manip context.

    ---
    - Args:
        - [object]: Input item(s).
        - activeHandle (ah): Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
            (all axes) is active (default)
        - alignAlong (aa): Aligns active handle along vector.
        - bakePivotOri (bpo): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - currentActiveHandle (cah): Sets the active handle for the manip. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle (all axes) is active4 - XY plane handle is active5 - YZ plane handle is active6 - XZ
            plane handle is active
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Scale mode:0 - Object Space1 - Local Space2 - World Space (default)3 - Scale Along Vertex Normal4 - Scale Along Rotation Axis5 - Scale Along Live Object Axis6 - Custom Axis Orientation10 - Component Space
        - orientAxes (oa): Orients manipulator rotating around axes by specified angles
        - orientObject (oo): Orients manipulator to the passed in object/component
        - orientTowards (ot): Orients active handle towards world point
        - pinPivot (pin): Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        - pivotOriHandle (poh): When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        - postCommand (psc): Specifies a command to be executed when the tool is exited.
        - postDragCommand (pod): Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        - preCommand (prc): Specifies a command to be executed when the tool is entered.
        - preDragCommand (prd): Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        - preserveChildPosition (pcp): When false, the children objects move when their parent is rotated. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        - preserveUV (puv): When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        - resetPivotMode (rpm): Specifies the mode used when resetting the pivot position. Available modes are:0: Center pivot (on bounding box)1: Zero pivot (object-space origin)
        - scale (sc): Returns the scale of the manipulator for its current orientation/mode.
        - snap (s): Specify that the manipulation is to use absolute snap
        - snapPivotOri (spo): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        - snapPivotPos (spp): Snap pivot position. Modify pivot position when snapping the pivot to a component.
        - snapRelative (sr): Specify that the manipulation is to use relative snap
        - snapValue (sv): Specify the snapping value
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and scaled in one step using a click-drag interaction.
        - useManipPivot (ump): Specify whether to pivot on the manip
        - useObjectPivot (uop): Specify whether to pivot on the object
        - xformConstraint (xc): none - no transform constraintedge - edge transform constraintsurface - surface transform constraint
        - edit (e): Edit mode flag
    """
@overload #Overload for manipScaleContext in ['edit']
def manipScaleContext([object]: [object], activeHandle: int = ..., ah: int = ..., alignAlong: [float, float, float] = ..., aa: [float, float, float] = ..., bakePivotOri: bool = ..., bpo: bool = ..., constrainAlongNormal: bool = ..., xn: bool = ..., currentActiveHandle: int = ..., cah: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., mode: int = ..., m: int = ..., orientAxes: [float, float, float] = ..., oa: [float, float, float] = ..., orientObject: str = ..., oo: str = ..., orientTowards: [float, float, float] = ..., ot: [float, float, float] = ..., pinPivot: bool = ..., pin: bool = ..., pivotOriHandle: bool = ..., poh: bool = ..., postCommand: script = ..., psc: script = ..., postDragCommand: [script, string] = ..., pod: [script, string] = ..., preCommand: script = ..., prc: script = ..., preDragCommand: [script, string] = ..., prd: [script, string] = ..., preserveChildPosition: bool = ..., pcp: bool = ..., preserveUV: bool = ..., puv: bool = ..., resetPivotMode: int = ..., rpm: int = ..., scale: [float, float, float] = ..., sc: [float, float, float] = ..., snap: bool = ..., s: bool = ..., snapPivotOri: bool = ..., spo: bool = ..., snapPivotPos: bool = ..., spp: bool = ..., snapRelative: bool = ..., sr: bool = ..., snapValue: float = ..., sv: float = ..., tweakMode: bool = ..., twk: bool = ..., useManipPivot: bool = ..., ump: bool = ..., useObjectPivot: bool = ..., uop: bool = ..., xformConstraint: str = ..., xc: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """manipScaleContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a scale manip context.

    ---
    - Args:
        - [object]: Input item(s).
        - activeHandle (ah): Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
            (all axes) is active (default)
        - alignAlong (aa): Aligns active handle along vector.
        - bakePivotOri (bpo): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - currentActiveHandle (cah): Sets the active handle for the manip. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle (all axes) is active4 - XY plane handle is active5 - YZ plane handle is active6 - XZ
            plane handle is active
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Scale mode:0 - Object Space1 - Local Space2 - World Space (default)3 - Scale Along Vertex Normal4 - Scale Along Rotation Axis5 - Scale Along Live Object Axis6 - Custom Axis Orientation10 - Component Space
        - orientAxes (oa): Orients manipulator rotating around axes by specified angles
        - orientObject (oo): Orients manipulator to the passed in object/component
        - orientTowards (ot): Orients active handle towards world point
        - pinPivot (pin): Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        - pivotOriHandle (poh): When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        - postCommand (psc): Specifies a command to be executed when the tool is exited.
        - postDragCommand (pod): Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        - preCommand (prc): Specifies a command to be executed when the tool is entered.
        - preDragCommand (prd): Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        - preserveChildPosition (pcp): When false, the children objects move when their parent is rotated. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        - preserveUV (puv): When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        - resetPivotMode (rpm): Specifies the mode used when resetting the pivot position. Available modes are:0: Center pivot (on bounding box)1: Zero pivot (object-space origin)
        - scale (sc): Returns the scale of the manipulator for its current orientation/mode.
        - snap (s): Specify that the manipulation is to use absolute snap
        - snapPivotOri (spo): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        - snapPivotPos (spp): Snap pivot position. Modify pivot position when snapping the pivot to a component.
        - snapRelative (sr): Specify that the manipulation is to use relative snap
        - snapValue (sv): Specify the snapping value
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and scaled in one step using a click-drag interaction.
        - useManipPivot (ump): Specify whether to pivot on the manip
        - useObjectPivot (uop): Specify whether to pivot on the object
        - xformConstraint (xc): none - no transform constraintedge - edge transform constraintsurface - surface transform constraint
        - edit (e): Edit mode flag
    """
