"""Stub files for Contexts category in Maya commands, command: manipMoveContext."""

from typing import Any, overload

@overload #Overload for manipMoveContext in ['create']
def manipMoveContext([object]: [object], alignAlong: [float, float, float] = ..., exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., orientObject: str = ..., orientTowards: [float, float, float] = ..., postCommand: script = ..., postDragCommand: [script, string] = ..., preCommand: script = ..., preDragCommand: [script, string] = ...) -> str:
    """manipMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a move manip context. Note
    that the flags -s, -sv, -sr, -scr, -slp, -slf control the global behaviour of
    all move manip context. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    move manip context.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.manipMoveContext()
        # To query the mode of an existing context:
        cmds.manipMoveContext( 'manipMoveContext1', q=True, mode=True )
        # To edit an existing context to come up with the X axis handle
        # active by default:
        cmds.manipMoveContext( 'manipMoveContext1', e=True, ah=0 )
        cmds.spaceLocator( p=(0, 0, 0), name='locatorA' )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, m=2 ) # WorldSpace
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=0.4 )
        # Now, dragging any of the move handles will
        # move the object in steps of 0.4 units.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=False )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (0,0,0) (2,0,0) (4,0,0) ...etc
        # NOTE: If in objectSpace Mode, the snapRelative should be ON.
        # Absolute discrete move is not supported in objectSpace mode.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=True )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (2.8,0,0) (4.8,0,0) (6.8,0,0) ...etc
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - alignAlong (aa): Aligns active handle along vector.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - orientObject (oo): Orients manipulator to the passed in object/component
        - orientTowards (ot): Orients active handle towards world point
        - postCommand (psc): Specifies a command to be executed when the tool is exited.
        - postDragCommand (pod): Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        - preCommand (prc): Specifies a command to be executed when the tool is entered.
        - preDragCommand (prd): Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
    """
@overload #Overload for manipMoveContext in ['create']
def manipMoveContext([object]: [object], aa: [float, float, float] = ..., ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., oo: str = ..., ot: [float, float, float] = ..., psc: script = ..., pod: [script, string] = ..., prc: script = ..., prd: [script, string] = ...) -> str:
    """manipMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a move manip context. Note
    that the flags -s, -sv, -sr, -scr, -slp, -slf control the global behaviour of
    all move manip context. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    move manip context.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.manipMoveContext()
        # To query the mode of an existing context:
        cmds.manipMoveContext( 'manipMoveContext1', q=True, mode=True )
        # To edit an existing context to come up with the X axis handle
        # active by default:
        cmds.manipMoveContext( 'manipMoveContext1', e=True, ah=0 )
        cmds.spaceLocator( p=(0, 0, 0), name='locatorA' )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, m=2 ) # WorldSpace
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=0.4 )
        # Now, dragging any of the move handles will
        # move the object in steps of 0.4 units.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=False )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (0,0,0) (2,0,0) (4,0,0) ...etc
        # NOTE: If in objectSpace Mode, the snapRelative should be ON.
        # Absolute discrete move is not supported in objectSpace mode.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=True )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (2.8,0,0) (4.8,0,0) (6.8,0,0) ...etc
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - alignAlong (aa): Aligns active handle along vector.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - orientObject (oo): Orients manipulator to the passed in object/component
        - orientTowards (ot): Orients active handle towards world point
        - postCommand (psc): Specifies a command to be executed when the tool is exited.
        - postDragCommand (pod): Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        - preCommand (prc): Specifies a command to be executed when the tool is entered.
        - preDragCommand (prd): Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
    """
@overload #Overload for manipMoveContext in ['create']
def manipMoveContext([object]: [object], alignAlong: [float, float, float] = ..., aa: [float, float, float] = ..., exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., orientObject: str = ..., oo: str = ..., orientTowards: [float, float, float] = ..., ot: [float, float, float] = ..., postCommand: script = ..., psc: script = ..., postDragCommand: [script, string] = ..., pod: [script, string] = ..., preCommand: script = ..., prc: script = ..., preDragCommand: [script, string] = ..., prd: [script, string] = ...) -> str:
    """manipMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a move manip context. Note
    that the flags -s, -sv, -sr, -scr, -slp, -slf control the global behaviour of
    all move manip context. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    move manip context.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.manipMoveContext()
        # To query the mode of an existing context:
        cmds.manipMoveContext( 'manipMoveContext1', q=True, mode=True )
        # To edit an existing context to come up with the X axis handle
        # active by default:
        cmds.manipMoveContext( 'manipMoveContext1', e=True, ah=0 )
        cmds.spaceLocator( p=(0, 0, 0), name='locatorA' )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, m=2 ) # WorldSpace
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=0.4 )
        # Now, dragging any of the move handles will
        # move the object in steps of 0.4 units.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=False )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (0,0,0) (2,0,0) (4,0,0) ...etc
        # NOTE: If in objectSpace Mode, the snapRelative should be ON.
        # Absolute discrete move is not supported in objectSpace mode.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=True )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (2.8,0,0) (4.8,0,0) (6.8,0,0) ...etc
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - alignAlong (aa): Aligns active handle along vector.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - orientObject (oo): Orients manipulator to the passed in object/component
        - orientTowards (ot): Orients active handle towards world point
        - postCommand (psc): Specifies a command to be executed when the tool is exited.
        - postDragCommand (pod): Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        - preCommand (prc): Specifies a command to be executed when the tool is entered.
        - preDragCommand (prd): Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
    """
@overload #Overload for manipMoveContext in ['query']
def manipMoveContext([object]: [object], activeHandle: int = ..., activeHandleNormal: int = ..., autoOrientSecondaryAxis: bool = ..., bakePivotOri: bool = ..., constrainAlongNormal: bool = ..., currentActiveHandle: int = ..., editPivotMode: bool = ..., editPivotPosition: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., interactiveUpdate: bool = ..., lastMode: int = ..., manipVisible: bool = ..., mode: int = ..., orientAxes: [float, float, float] = ..., orientJoint: str = ..., orientJointEnabled: bool = ..., pinPivot: bool = ..., pivotOriHandle: bool = ..., position: bool = ..., preserveChildPosition: bool = ..., preserveUV: bool = ..., resetPivotMode: int = ..., secondaryAxisOrient: str = ..., snap: bool = ..., snapComponentsRelative: bool = ..., snapLiveFaceCenter: bool = ..., snapLivePoint: bool = ..., snapPivotOri: bool = ..., snapPivotPos: bool = ..., snapRelative: bool = ..., snapValue: float = ..., translate: [float, float, float] = ..., tweakMode: bool = ..., xformConstraint: str = ..., query: bool = ...) -> str:
    """manipMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a move manip context. Note
    that the flags -s, -sv, -sr, -scr, -slp, -slf control the global behaviour of
    all move manip context. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    move manip context.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.manipMoveContext()
        # To query the mode of an existing context:
        cmds.manipMoveContext( 'manipMoveContext1', q=True, mode=True )
        # To edit an existing context to come up with the X axis handle
        # active by default:
        cmds.manipMoveContext( 'manipMoveContext1', e=True, ah=0 )
        cmds.spaceLocator( p=(0, 0, 0), name='locatorA' )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, m=2 ) # WorldSpace
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=0.4 )
        # Now, dragging any of the move handles will
        # move the object in steps of 0.4 units.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=False )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (0,0,0) (2,0,0) (4,0,0) ...etc
        # NOTE: If in objectSpace Mode, the snapRelative should be ON.
        # Absolute discrete move is not supported in objectSpace mode.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=True )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (2.8,0,0) (4.8,0,0) (6.8,0,0) ...etc
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - activeHandle (ah): Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
            (all 3 axes) is active (default)
        - activeHandleNormal (ahn): 0 - U axis handle is active1 - V axis handle is active2 - N axis handle is active ( default )3 - Center handle (all 3 axes) is activeapplicable only when the manip mode is 3.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - bakePivotOri (bpo): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - currentActiveHandle (cah): Sets the active handle for the manip. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle (all 3 axes) is active4 - XY plane handle is active5 - YZ plane handle is active6 - XZ
            plane handle is active
        - editPivotMode (epm): Returns true manipulator is in edit pivot mode
        - editPivotPosition (epp): Returns the current position of the edit pivot manipulator.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - interactiveUpdate (iu): Value can be : true or false. This flag value is valid only if the mode is 3 i.e. move vertex normal.
        - lastMode (lm): Returns the previous translation mode.
        - manipVisible (vis): Returns true if the main translate manipulator is visible.
        - mode (m): Translate mode:0 - Object Space1 - Local Space2 - World Space (default)3 - Move Along Vertex Normal4 - Move Along Rotation Axis5 - Move Along Live Object Axis6 - Custom Axis Orientation10 - Component Space
        - orientAxes (oa): Orients manipulator rotating around axes by specified angles
        - orientJoint (oj): Specifies the type of orientation for joint orientation. Valid options are: none, xyz, xzy, yxz, yzx, zxy, zyx.
        - orientJointEnabled (oje): Specifies if joints should be reoriented when moved.
        - pinPivot (pin): Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        - pivotOriHandle (poh): When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        - position (p): Returns the current position of the manipulator
        - preserveChildPosition (pcp): When false, the children objects move when their parent is moved. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        - preserveUV (puv): When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        - resetPivotMode (rpm): Specifies the mode used when resetting the pivot position. Available modes are:0: Center pivot (on bounding box)1: Zero pivot (object-space origin)
        - secondaryAxisOrient (sao): Specifies the global axis (in world coordinates) that should be used to should be used to align the second axis of the orientJointType triple. Valid options are xup, yup, zup, xdown, ydown, zdown, none.
        - snap (s): Value can be : true or false. Enable/Disable the discrete move. If set to true, the move manipulator of all the move contexts would snap at discrete points along the active handle during mouse drag.  The interval between the points can be
            controlled using the 'snapValue' flag.
        - snapComponentsRelative (scr): Value can be : true or false. If true, while snapping a group of CVs/Vertices, the relative spacing between them will be preserved. If false, all the CVs/Vertices will be snapped to the target point (is used during grid snap(hotkey 'x'),
            and point snap(hotkey 'v')) Depress the 'x' key before click-dragging the manip handle and check to see the behaviour of moving a bunch of CVs, with this flag ON and OFF.
        - snapLiveFaceCenter (slf): Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the face centers of the object.
        - snapLivePoint (slp): Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the vertices of the object.
        - snapPivotOri (spo): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        - snapPivotPos (spp): Snap pivot position. Modify pivot position when snapping the pivot to a component.
        - snapRelative (sr): Value can be : true or false. Applicable only when the snap is enabled. If true, the snapValue is treated relative to the original position before moving. If false, the snapValue is treated relative to the world origin. NOTE:    If in
            local/object Space Mode, the snapRelative should be ON. Absolute discrete move is not supported in local/object mode.
        - snapValue (sv): Applicable only when the snap is enabled. The manipulator of all move contexts would move in steps of 'snapValue'
        - translate (tr): Returns the translation of the manipulator for its current orientation/mode.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.
        - xformConstraint (xc): none - no transform constraintedge - edge transform constraintsurface - surface transform constraint
        - query (q): Query mode flag
    """
@overload #Overload for manipMoveContext in ['query']
def manipMoveContext([object]: [object], ah: int = ..., ahn: int = ..., aos: bool = ..., bpo: bool = ..., xn: bool = ..., cah: int = ..., epm: bool = ..., epp: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., iu: bool = ..., lm: int = ..., vis: bool = ..., m: int = ..., oa: [float, float, float] = ..., oj: str = ..., oje: bool = ..., pin: bool = ..., poh: bool = ..., p: bool = ..., pcp: bool = ..., puv: bool = ..., rpm: int = ..., sao: str = ..., s: bool = ..., scr: bool = ..., slf: bool = ..., slp: bool = ..., spo: bool = ..., spp: bool = ..., sr: bool = ..., sv: float = ..., tr: [float, float, float] = ..., twk: bool = ..., xc: str = ..., q: bool = ...) -> str:
    """manipMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a move manip context. Note
    that the flags -s, -sv, -sr, -scr, -slp, -slf control the global behaviour of
    all move manip context. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    move manip context.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.manipMoveContext()
        # To query the mode of an existing context:
        cmds.manipMoveContext( 'manipMoveContext1', q=True, mode=True )
        # To edit an existing context to come up with the X axis handle
        # active by default:
        cmds.manipMoveContext( 'manipMoveContext1', e=True, ah=0 )
        cmds.spaceLocator( p=(0, 0, 0), name='locatorA' )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, m=2 ) # WorldSpace
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=0.4 )
        # Now, dragging any of the move handles will
        # move the object in steps of 0.4 units.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=False )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (0,0,0) (2,0,0) (4,0,0) ...etc
        # NOTE: If in objectSpace Mode, the snapRelative should be ON.
        # Absolute discrete move is not supported in objectSpace mode.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=True )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (2.8,0,0) (4.8,0,0) (6.8,0,0) ...etc
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - activeHandle (ah): Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
            (all 3 axes) is active (default)
        - activeHandleNormal (ahn): 0 - U axis handle is active1 - V axis handle is active2 - N axis handle is active ( default )3 - Center handle (all 3 axes) is activeapplicable only when the manip mode is 3.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - bakePivotOri (bpo): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - currentActiveHandle (cah): Sets the active handle for the manip. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle (all 3 axes) is active4 - XY plane handle is active5 - YZ plane handle is active6 - XZ
            plane handle is active
        - editPivotMode (epm): Returns true manipulator is in edit pivot mode
        - editPivotPosition (epp): Returns the current position of the edit pivot manipulator.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - interactiveUpdate (iu): Value can be : true or false. This flag value is valid only if the mode is 3 i.e. move vertex normal.
        - lastMode (lm): Returns the previous translation mode.
        - manipVisible (vis): Returns true if the main translate manipulator is visible.
        - mode (m): Translate mode:0 - Object Space1 - Local Space2 - World Space (default)3 - Move Along Vertex Normal4 - Move Along Rotation Axis5 - Move Along Live Object Axis6 - Custom Axis Orientation10 - Component Space
        - orientAxes (oa): Orients manipulator rotating around axes by specified angles
        - orientJoint (oj): Specifies the type of orientation for joint orientation. Valid options are: none, xyz, xzy, yxz, yzx, zxy, zyx.
        - orientJointEnabled (oje): Specifies if joints should be reoriented when moved.
        - pinPivot (pin): Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        - pivotOriHandle (poh): When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        - position (p): Returns the current position of the manipulator
        - preserveChildPosition (pcp): When false, the children objects move when their parent is moved. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        - preserveUV (puv): When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        - resetPivotMode (rpm): Specifies the mode used when resetting the pivot position. Available modes are:0: Center pivot (on bounding box)1: Zero pivot (object-space origin)
        - secondaryAxisOrient (sao): Specifies the global axis (in world coordinates) that should be used to should be used to align the second axis of the orientJointType triple. Valid options are xup, yup, zup, xdown, ydown, zdown, none.
        - snap (s): Value can be : true or false. Enable/Disable the discrete move. If set to true, the move manipulator of all the move contexts would snap at discrete points along the active handle during mouse drag.  The interval between the points can be
            controlled using the 'snapValue' flag.
        - snapComponentsRelative (scr): Value can be : true or false. If true, while snapping a group of CVs/Vertices, the relative spacing between them will be preserved. If false, all the CVs/Vertices will be snapped to the target point (is used during grid snap(hotkey 'x'),
            and point snap(hotkey 'v')) Depress the 'x' key before click-dragging the manip handle and check to see the behaviour of moving a bunch of CVs, with this flag ON and OFF.
        - snapLiveFaceCenter (slf): Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the face centers of the object.
        - snapLivePoint (slp): Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the vertices of the object.
        - snapPivotOri (spo): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        - snapPivotPos (spp): Snap pivot position. Modify pivot position when snapping the pivot to a component.
        - snapRelative (sr): Value can be : true or false. Applicable only when the snap is enabled. If true, the snapValue is treated relative to the original position before moving. If false, the snapValue is treated relative to the world origin. NOTE:    If in
            local/object Space Mode, the snapRelative should be ON. Absolute discrete move is not supported in local/object mode.
        - snapValue (sv): Applicable only when the snap is enabled. The manipulator of all move contexts would move in steps of 'snapValue'
        - translate (tr): Returns the translation of the manipulator for its current orientation/mode.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.
        - xformConstraint (xc): none - no transform constraintedge - edge transform constraintsurface - surface transform constraint
        - query (q): Query mode flag
    """
@overload #Overload for manipMoveContext in ['query']
def manipMoveContext([object]: [object], activeHandle: int = ..., ah: int = ..., activeHandleNormal: int = ..., ahn: int = ..., autoOrientSecondaryAxis: bool = ..., aos: bool = ..., bakePivotOri: bool = ..., bpo: bool = ..., constrainAlongNormal: bool = ..., xn: bool = ..., currentActiveHandle: int = ..., cah: int = ..., editPivotMode: bool = ..., epm: bool = ..., editPivotPosition: bool = ..., epp: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., interactiveUpdate: bool = ..., iu: bool = ..., lastMode: int = ..., lm: int = ..., manipVisible: bool = ..., vis: bool = ..., mode: int = ..., m: int = ..., orientAxes: [float, float, float] = ..., oa: [float, float, float] = ..., orientJoint: str = ..., oj: str = ..., orientJointEnabled: bool = ..., oje: bool = ..., pinPivot: bool = ..., pin: bool = ..., pivotOriHandle: bool = ..., poh: bool = ..., position: bool = ..., p: bool = ..., preserveChildPosition: bool = ..., pcp: bool = ..., preserveUV: bool = ..., puv: bool = ..., resetPivotMode: int = ..., rpm: int = ..., secondaryAxisOrient: str = ..., sao: str = ..., snap: bool = ..., s: bool = ..., snapComponentsRelative: bool = ..., scr: bool = ..., snapLiveFaceCenter: bool = ..., slf: bool = ..., snapLivePoint: bool = ..., slp: bool = ..., snapPivotOri: bool = ..., spo: bool = ..., snapPivotPos: bool = ..., spp: bool = ..., snapRelative: bool = ..., sr: bool = ..., snapValue: float = ..., sv: float = ..., translate: [float, float, float] = ..., tr: [float, float, float] = ..., tweakMode: bool = ..., twk: bool = ..., xformConstraint: str = ..., xc: str = ..., query: bool = ..., q: bool = ...) -> str:
    """manipMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a move manip context. Note
    that the flags -s, -sv, -sr, -scr, -slp, -slf control the global behaviour of
    all move manip context. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    move manip context.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.manipMoveContext()
        # To query the mode of an existing context:
        cmds.manipMoveContext( 'manipMoveContext1', q=True, mode=True )
        # To edit an existing context to come up with the X axis handle
        # active by default:
        cmds.manipMoveContext( 'manipMoveContext1', e=True, ah=0 )
        cmds.spaceLocator( p=(0, 0, 0), name='locatorA' )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, m=2 ) # WorldSpace
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=0.4 )
        # Now, dragging any of the move handles will
        # move the object in steps of 0.4 units.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=False )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (0,0,0) (2,0,0) (4,0,0) ...etc
        # NOTE: If in objectSpace Mode, the snapRelative should be ON.
        # Absolute discrete move is not supported in objectSpace mode.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=True )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (2.8,0,0) (4.8,0,0) (6.8,0,0) ...etc
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - activeHandle (ah): Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
            (all 3 axes) is active (default)
        - activeHandleNormal (ahn): 0 - U axis handle is active1 - V axis handle is active2 - N axis handle is active ( default )3 - Center handle (all 3 axes) is activeapplicable only when the manip mode is 3.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - bakePivotOri (bpo): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - currentActiveHandle (cah): Sets the active handle for the manip. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle (all 3 axes) is active4 - XY plane handle is active5 - YZ plane handle is active6 - XZ
            plane handle is active
        - editPivotMode (epm): Returns true manipulator is in edit pivot mode
        - editPivotPosition (epp): Returns the current position of the edit pivot manipulator.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - interactiveUpdate (iu): Value can be : true or false. This flag value is valid only if the mode is 3 i.e. move vertex normal.
        - lastMode (lm): Returns the previous translation mode.
        - manipVisible (vis): Returns true if the main translate manipulator is visible.
        - mode (m): Translate mode:0 - Object Space1 - Local Space2 - World Space (default)3 - Move Along Vertex Normal4 - Move Along Rotation Axis5 - Move Along Live Object Axis6 - Custom Axis Orientation10 - Component Space
        - orientAxes (oa): Orients manipulator rotating around axes by specified angles
        - orientJoint (oj): Specifies the type of orientation for joint orientation. Valid options are: none, xyz, xzy, yxz, yzx, zxy, zyx.
        - orientJointEnabled (oje): Specifies if joints should be reoriented when moved.
        - pinPivot (pin): Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        - pivotOriHandle (poh): When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        - position (p): Returns the current position of the manipulator
        - preserveChildPosition (pcp): When false, the children objects move when their parent is moved. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        - preserveUV (puv): When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        - resetPivotMode (rpm): Specifies the mode used when resetting the pivot position. Available modes are:0: Center pivot (on bounding box)1: Zero pivot (object-space origin)
        - secondaryAxisOrient (sao): Specifies the global axis (in world coordinates) that should be used to should be used to align the second axis of the orientJointType triple. Valid options are xup, yup, zup, xdown, ydown, zdown, none.
        - snap (s): Value can be : true or false. Enable/Disable the discrete move. If set to true, the move manipulator of all the move contexts would snap at discrete points along the active handle during mouse drag.  The interval between the points can be
            controlled using the 'snapValue' flag.
        - snapComponentsRelative (scr): Value can be : true or false. If true, while snapping a group of CVs/Vertices, the relative spacing between them will be preserved. If false, all the CVs/Vertices will be snapped to the target point (is used during grid snap(hotkey 'x'),
            and point snap(hotkey 'v')) Depress the 'x' key before click-dragging the manip handle and check to see the behaviour of moving a bunch of CVs, with this flag ON and OFF.
        - snapLiveFaceCenter (slf): Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the face centers of the object.
        - snapLivePoint (slp): Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the vertices of the object.
        - snapPivotOri (spo): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        - snapPivotPos (spp): Snap pivot position. Modify pivot position when snapping the pivot to a component.
        - snapRelative (sr): Value can be : true or false. Applicable only when the snap is enabled. If true, the snapValue is treated relative to the original position before moving. If false, the snapValue is treated relative to the world origin. NOTE:    If in
            local/object Space Mode, the snapRelative should be ON. Absolute discrete move is not supported in local/object mode.
        - snapValue (sv): Applicable only when the snap is enabled. The manipulator of all move contexts would move in steps of 'snapValue'
        - translate (tr): Returns the translation of the manipulator for its current orientation/mode.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.
        - xformConstraint (xc): none - no transform constraintedge - edge transform constraintsurface - surface transform constraint
        - query (q): Query mode flag
    """
@overload #Overload for manipMoveContext in ['edit']
def manipMoveContext([object]: [object], activeHandle: int = ..., activeHandleNormal: int = ..., alignAlong: [float, float, float] = ..., autoOrientSecondaryAxis: bool = ..., bakePivotOri: bool = ..., constrainAlongNormal: bool = ..., currentActiveHandle: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., interactiveUpdate: bool = ..., mode: int = ..., orientAxes: [float, float, float] = ..., orientJoint: str = ..., orientJointEnabled: bool = ..., orientObject: str = ..., orientTowards: [float, float, float] = ..., pinPivot: bool = ..., pivotOriHandle: bool = ..., postCommand: script = ..., postDragCommand: [script, string] = ..., preCommand: script = ..., preDragCommand: [script, string] = ..., preserveChildPosition: bool = ..., preserveUV: bool = ..., resetPivotMode: int = ..., secondaryAxisOrient: str = ..., snap: bool = ..., snapComponentsRelative: bool = ..., snapLiveFaceCenter: bool = ..., snapLivePoint: bool = ..., snapPivotOri: bool = ..., snapPivotPos: bool = ..., snapRelative: bool = ..., snapValue: float = ..., translate: [float, float, float] = ..., tweakMode: bool = ..., xformConstraint: str = ..., edit: bool = ...) -> str:
    """manipMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a move manip context. Note
    that the flags -s, -sv, -sr, -scr, -slp, -slf control the global behaviour of
    all move manip context. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    move manip context.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.manipMoveContext()
        # To query the mode of an existing context:
        cmds.manipMoveContext( 'manipMoveContext1', q=True, mode=True )
        # To edit an existing context to come up with the X axis handle
        # active by default:
        cmds.manipMoveContext( 'manipMoveContext1', e=True, ah=0 )
        cmds.spaceLocator( p=(0, 0, 0), name='locatorA' )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, m=2 ) # WorldSpace
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=0.4 )
        # Now, dragging any of the move handles will
        # move the object in steps of 0.4 units.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=False )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (0,0,0) (2,0,0) (4,0,0) ...etc
        # NOTE: If in objectSpace Mode, the snapRelative should be ON.
        # Absolute discrete move is not supported in objectSpace mode.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=True )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (2.8,0,0) (4.8,0,0) (6.8,0,0) ...etc
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - activeHandle (ah): Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
            (all 3 axes) is active (default)
        - activeHandleNormal (ahn): 0 - U axis handle is active1 - V axis handle is active2 - N axis handle is active ( default )3 - Center handle (all 3 axes) is activeapplicable only when the manip mode is 3.
        - alignAlong (aa): Aligns active handle along vector.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - bakePivotOri (bpo): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - currentActiveHandle (cah): Sets the active handle for the manip. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle (all 3 axes) is active4 - XY plane handle is active5 - YZ plane handle is active6 - XZ
            plane handle is active
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - interactiveUpdate (iu): Value can be : true or false. This flag value is valid only if the mode is 3 i.e. move vertex normal.
        - mode (m): Translate mode:0 - Object Space1 - Local Space2 - World Space (default)3 - Move Along Vertex Normal4 - Move Along Rotation Axis5 - Move Along Live Object Axis6 - Custom Axis Orientation10 - Component Space
        - orientAxes (oa): Orients manipulator rotating around axes by specified angles
        - orientJoint (oj): Specifies the type of orientation for joint orientation. Valid options are: none, xyz, xzy, yxz, yzx, zxy, zyx.
        - orientJointEnabled (oje): Specifies if joints should be reoriented when moved.
        - orientObject (oo): Orients manipulator to the passed in object/component
        - orientTowards (ot): Orients active handle towards world point
        - pinPivot (pin): Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        - pivotOriHandle (poh): When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        - postCommand (psc): Specifies a command to be executed when the tool is exited.
        - postDragCommand (pod): Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        - preCommand (prc): Specifies a command to be executed when the tool is entered.
        - preDragCommand (prd): Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        - preserveChildPosition (pcp): When false, the children objects move when their parent is moved. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        - preserveUV (puv): When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        - resetPivotMode (rpm): Specifies the mode used when resetting the pivot position. Available modes are:0: Center pivot (on bounding box)1: Zero pivot (object-space origin)
        - secondaryAxisOrient (sao): Specifies the global axis (in world coordinates) that should be used to should be used to align the second axis of the orientJointType triple. Valid options are xup, yup, zup, xdown, ydown, zdown, none.
        - snap (s): Value can be : true or false. Enable/Disable the discrete move. If set to true, the move manipulator of all the move contexts would snap at discrete points along the active handle during mouse drag.  The interval between the points can be
            controlled using the 'snapValue' flag.
        - snapComponentsRelative (scr): Value can be : true or false. If true, while snapping a group of CVs/Vertices, the relative spacing between them will be preserved. If false, all the CVs/Vertices will be snapped to the target point (is used during grid snap(hotkey 'x'),
            and point snap(hotkey 'v')) Depress the 'x' key before click-dragging the manip handle and check to see the behaviour of moving a bunch of CVs, with this flag ON and OFF.
        - snapLiveFaceCenter (slf): Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the face centers of the object.
        - snapLivePoint (slp): Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the vertices of the object.
        - snapPivotOri (spo): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        - snapPivotPos (spp): Snap pivot position. Modify pivot position when snapping the pivot to a component.
        - snapRelative (sr): Value can be : true or false. Applicable only when the snap is enabled. If true, the snapValue is treated relative to the original position before moving. If false, the snapValue is treated relative to the world origin. NOTE:    If in
            local/object Space Mode, the snapRelative should be ON. Absolute discrete move is not supported in local/object mode.
        - snapValue (sv): Applicable only when the snap is enabled. The manipulator of all move contexts would move in steps of 'snapValue'
        - translate (tr): Returns the translation of the manipulator for its current orientation/mode.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.
        - xformConstraint (xc): none - no transform constraintedge - edge transform constraintsurface - surface transform constraint
        - edit (e): Edit mode flag
    """
@overload #Overload for manipMoveContext in ['edit']
def manipMoveContext([object]: [object], ah: int = ..., ahn: int = ..., aa: [float, float, float] = ..., aos: bool = ..., bpo: bool = ..., xn: bool = ..., cah: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., iu: bool = ..., m: int = ..., oa: [float, float, float] = ..., oj: str = ..., oje: bool = ..., oo: str = ..., ot: [float, float, float] = ..., pin: bool = ..., poh: bool = ..., psc: script = ..., pod: [script, string] = ..., prc: script = ..., prd: [script, string] = ..., pcp: bool = ..., puv: bool = ..., rpm: int = ..., sao: str = ..., s: bool = ..., scr: bool = ..., slf: bool = ..., slp: bool = ..., spo: bool = ..., spp: bool = ..., sr: bool = ..., sv: float = ..., tr: [float, float, float] = ..., twk: bool = ..., xc: str = ..., e: bool = ...) -> str:
    """manipMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a move manip context. Note
    that the flags -s, -sv, -sr, -scr, -slp, -slf control the global behaviour of
    all move manip context. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    move manip context.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.manipMoveContext()
        # To query the mode of an existing context:
        cmds.manipMoveContext( 'manipMoveContext1', q=True, mode=True )
        # To edit an existing context to come up with the X axis handle
        # active by default:
        cmds.manipMoveContext( 'manipMoveContext1', e=True, ah=0 )
        cmds.spaceLocator( p=(0, 0, 0), name='locatorA' )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, m=2 ) # WorldSpace
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=0.4 )
        # Now, dragging any of the move handles will
        # move the object in steps of 0.4 units.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=False )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (0,0,0) (2,0,0) (4,0,0) ...etc
        # NOTE: If in objectSpace Mode, the snapRelative should be ON.
        # Absolute discrete move is not supported in objectSpace mode.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=True )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (2.8,0,0) (4.8,0,0) (6.8,0,0) ...etc
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - activeHandle (ah): Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
            (all 3 axes) is active (default)
        - activeHandleNormal (ahn): 0 - U axis handle is active1 - V axis handle is active2 - N axis handle is active ( default )3 - Center handle (all 3 axes) is activeapplicable only when the manip mode is 3.
        - alignAlong (aa): Aligns active handle along vector.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - bakePivotOri (bpo): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - currentActiveHandle (cah): Sets the active handle for the manip. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle (all 3 axes) is active4 - XY plane handle is active5 - YZ plane handle is active6 - XZ
            plane handle is active
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - interactiveUpdate (iu): Value can be : true or false. This flag value is valid only if the mode is 3 i.e. move vertex normal.
        - mode (m): Translate mode:0 - Object Space1 - Local Space2 - World Space (default)3 - Move Along Vertex Normal4 - Move Along Rotation Axis5 - Move Along Live Object Axis6 - Custom Axis Orientation10 - Component Space
        - orientAxes (oa): Orients manipulator rotating around axes by specified angles
        - orientJoint (oj): Specifies the type of orientation for joint orientation. Valid options are: none, xyz, xzy, yxz, yzx, zxy, zyx.
        - orientJointEnabled (oje): Specifies if joints should be reoriented when moved.
        - orientObject (oo): Orients manipulator to the passed in object/component
        - orientTowards (ot): Orients active handle towards world point
        - pinPivot (pin): Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        - pivotOriHandle (poh): When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        - postCommand (psc): Specifies a command to be executed when the tool is exited.
        - postDragCommand (pod): Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        - preCommand (prc): Specifies a command to be executed when the tool is entered.
        - preDragCommand (prd): Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        - preserveChildPosition (pcp): When false, the children objects move when their parent is moved. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        - preserveUV (puv): When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        - resetPivotMode (rpm): Specifies the mode used when resetting the pivot position. Available modes are:0: Center pivot (on bounding box)1: Zero pivot (object-space origin)
        - secondaryAxisOrient (sao): Specifies the global axis (in world coordinates) that should be used to should be used to align the second axis of the orientJointType triple. Valid options are xup, yup, zup, xdown, ydown, zdown, none.
        - snap (s): Value can be : true or false. Enable/Disable the discrete move. If set to true, the move manipulator of all the move contexts would snap at discrete points along the active handle during mouse drag.  The interval between the points can be
            controlled using the 'snapValue' flag.
        - snapComponentsRelative (scr): Value can be : true or false. If true, while snapping a group of CVs/Vertices, the relative spacing between them will be preserved. If false, all the CVs/Vertices will be snapped to the target point (is used during grid snap(hotkey 'x'),
            and point snap(hotkey 'v')) Depress the 'x' key before click-dragging the manip handle and check to see the behaviour of moving a bunch of CVs, with this flag ON and OFF.
        - snapLiveFaceCenter (slf): Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the face centers of the object.
        - snapLivePoint (slp): Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the vertices of the object.
        - snapPivotOri (spo): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        - snapPivotPos (spp): Snap pivot position. Modify pivot position when snapping the pivot to a component.
        - snapRelative (sr): Value can be : true or false. Applicable only when the snap is enabled. If true, the snapValue is treated relative to the original position before moving. If false, the snapValue is treated relative to the world origin. NOTE:    If in
            local/object Space Mode, the snapRelative should be ON. Absolute discrete move is not supported in local/object mode.
        - snapValue (sv): Applicable only when the snap is enabled. The manipulator of all move contexts would move in steps of 'snapValue'
        - translate (tr): Returns the translation of the manipulator for its current orientation/mode.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.
        - xformConstraint (xc): none - no transform constraintedge - edge transform constraintsurface - surface transform constraint
        - edit (e): Edit mode flag
    """
@overload #Overload for manipMoveContext in ['edit']
def manipMoveContext([object]: [object], activeHandle: int = ..., ah: int = ..., activeHandleNormal: int = ..., ahn: int = ..., alignAlong: [float, float, float] = ..., aa: [float, float, float] = ..., autoOrientSecondaryAxis: bool = ..., aos: bool = ..., bakePivotOri: bool = ..., bpo: bool = ..., constrainAlongNormal: bool = ..., xn: bool = ..., currentActiveHandle: int = ..., cah: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., interactiveUpdate: bool = ..., iu: bool = ..., mode: int = ..., m: int = ..., orientAxes: [float, float, float] = ..., oa: [float, float, float] = ..., orientJoint: str = ..., oj: str = ..., orientJointEnabled: bool = ..., oje: bool = ..., orientObject: str = ..., oo: str = ..., orientTowards: [float, float, float] = ..., ot: [float, float, float] = ..., pinPivot: bool = ..., pin: bool = ..., pivotOriHandle: bool = ..., poh: bool = ..., postCommand: script = ..., psc: script = ..., postDragCommand: [script, string] = ..., pod: [script, string] = ..., preCommand: script = ..., prc: script = ..., preDragCommand: [script, string] = ..., prd: [script, string] = ..., preserveChildPosition: bool = ..., pcp: bool = ..., preserveUV: bool = ..., puv: bool = ..., resetPivotMode: int = ..., rpm: int = ..., secondaryAxisOrient: str = ..., sao: str = ..., snap: bool = ..., s: bool = ..., snapComponentsRelative: bool = ..., scr: bool = ..., snapLiveFaceCenter: bool = ..., slf: bool = ..., snapLivePoint: bool = ..., slp: bool = ..., snapPivotOri: bool = ..., spo: bool = ..., snapPivotPos: bool = ..., spp: bool = ..., snapRelative: bool = ..., sr: bool = ..., snapValue: float = ..., sv: float = ..., translate: [float, float, float] = ..., tr: [float, float, float] = ..., tweakMode: bool = ..., twk: bool = ..., xformConstraint: str = ..., xc: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """manipMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a move manip context. Note
    that the flags -s, -sv, -sr, -scr, -slp, -slf control the global behaviour of
    all move manip context. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    move manip context.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.manipMoveContext()
        # To query the mode of an existing context:
        cmds.manipMoveContext( 'manipMoveContext1', q=True, mode=True )
        # To edit an existing context to come up with the X axis handle
        # active by default:
        cmds.manipMoveContext( 'manipMoveContext1', e=True, ah=0 )
        cmds.spaceLocator( p=(0, 0, 0), name='locatorA' )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, m=2 ) # WorldSpace
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=0.4 )
        # Now, dragging any of the move handles will
        # move the object in steps of 0.4 units.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=False )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (0,0,0) (2,0,0) (4,0,0) ...etc
        # NOTE: If in objectSpace Mode, the snapRelative should be ON.
        # Absolute discrete move is not supported in objectSpace mode.
        cmds.move( 0.8, 0, 0, 'locatorA', a=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
        cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=True )
        # Now, dragging X-axis handle will
        # move the object in steps of 2 units, and will
        # place the object anywhere in (2.8,0,0) (4.8,0,0) (6.8,0,0) ...etc
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - activeHandle (ah): Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
            (all 3 axes) is active (default)
        - activeHandleNormal (ahn): 0 - U axis handle is active1 - V axis handle is active2 - N axis handle is active ( default )3 - Center handle (all 3 axes) is activeapplicable only when the manip mode is 3.
        - alignAlong (aa): Aligns active handle along vector.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - bakePivotOri (bpo): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - currentActiveHandle (cah): Sets the active handle for the manip. Values can be:0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle (all 3 axes) is active4 - XY plane handle is active5 - YZ plane handle is active6 - XZ
            plane handle is active
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - interactiveUpdate (iu): Value can be : true or false. This flag value is valid only if the mode is 3 i.e. move vertex normal.
        - mode (m): Translate mode:0 - Object Space1 - Local Space2 - World Space (default)3 - Move Along Vertex Normal4 - Move Along Rotation Axis5 - Move Along Live Object Axis6 - Custom Axis Orientation10 - Component Space
        - orientAxes (oa): Orients manipulator rotating around axes by specified angles
        - orientJoint (oj): Specifies the type of orientation for joint orientation. Valid options are: none, xyz, xzy, yxz, yzx, zxy, zyx.
        - orientJointEnabled (oje): Specifies if joints should be reoriented when moved.
        - orientObject (oo): Orients manipulator to the passed in object/component
        - orientTowards (ot): Orients active handle towards world point
        - pinPivot (pin): Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        - pivotOriHandle (poh): When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        - postCommand (psc): Specifies a command to be executed when the tool is exited.
        - postDragCommand (pod): Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        - preCommand (prc): Specifies a command to be executed when the tool is entered.
        - preDragCommand (prd): Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        - preserveChildPosition (pcp): When false, the children objects move when their parent is moved. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        - preserveUV (puv): When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        - resetPivotMode (rpm): Specifies the mode used when resetting the pivot position. Available modes are:0: Center pivot (on bounding box)1: Zero pivot (object-space origin)
        - secondaryAxisOrient (sao): Specifies the global axis (in world coordinates) that should be used to should be used to align the second axis of the orientJointType triple. Valid options are xup, yup, zup, xdown, ydown, zdown, none.
        - snap (s): Value can be : true or false. Enable/Disable the discrete move. If set to true, the move manipulator of all the move contexts would snap at discrete points along the active handle during mouse drag.  The interval between the points can be
            controlled using the 'snapValue' flag.
        - snapComponentsRelative (scr): Value can be : true or false. If true, while snapping a group of CVs/Vertices, the relative spacing between them will be preserved. If false, all the CVs/Vertices will be snapped to the target point (is used during grid snap(hotkey 'x'),
            and point snap(hotkey 'v')) Depress the 'x' key before click-dragging the manip handle and check to see the behaviour of moving a bunch of CVs, with this flag ON and OFF.
        - snapLiveFaceCenter (slf): Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the face centers of the object.
        - snapLivePoint (slp): Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the vertices of the object.
        - snapPivotOri (spo): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        - snapPivotPos (spp): Snap pivot position. Modify pivot position when snapping the pivot to a component.
        - snapRelative (sr): Value can be : true or false. Applicable only when the snap is enabled. If true, the snapValue is treated relative to the original position before moving. If false, the snapValue is treated relative to the world origin. NOTE:    If in
            local/object Space Mode, the snapRelative should be ON. Absolute discrete move is not supported in local/object mode.
        - snapValue (sv): Applicable only when the snap is enabled. The manipulator of all move contexts would move in steps of 'snapValue'
        - translate (tr): Returns the translation of the manipulator for its current orientation/mode.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.
        - xformConstraint (xc): none - no transform constraintedge - edge transform constraintsurface - surface transform constraint
        - edit (e): Edit mode flag
    """
