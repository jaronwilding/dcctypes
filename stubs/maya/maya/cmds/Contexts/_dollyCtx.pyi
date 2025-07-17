"""Stub files for Contexts category in Maya commands, command: dollyCtx."""

from typing import Any, overload

@overload #Overload for dollyCtx in ['create']
def dollyCtx(object: object, alternateContext: bool = ..., boxDollyType: str = ..., centerOfInterestDolly: bool = ..., dollyTowardsCenter: bool = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., localDolly: bool = ..., name: str = ..., orthoZoom: bool = ..., scale: float = ..., toolName: str = ...) -> str:
    """dollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.dollyCtx( 'dollyContext', s=1.0, ac=False, ld=False, cd=False )
        cmds.dollyCtx( 'dollyContext', e=True, bdt='surface' )
    ```

    ---
    - Args:
        - object: Input item(s).
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - boxDollyType (bdt): Set the behavior of where the camera's center of interest is set to after the box dolly. Insurfacemode, the center of interest will be snapped to the surface point at the center of the marquee. Inbboxmode, the closest bounding box to the
            camera will be used. Bounding box mode will use the selection mask to determine which objects to include into the calculation.
        - centerOfInterestDolly (cd): Set the translate the camera's center of interest. Left and right drag movements with the mouse will translate the center of interest towards or away respectively from the camera. The center of interest can be snapped to objects by using
            the left mouse button for selection. The default select mask will be used.
        - dollyTowardsCenter (dtc): Dolly towards center (if true), else dolly towards point where user clicks in the view.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localDolly (ld): Dolly with respect to the camera's center of interest. The camera will not pass through the center of interest. Local dolly only applies to perspective cameras.
        - name (n): If this is a tool command, name the tool appropriately.
        - orthoZoom (oz): Zoom orthographic view (if true), else dolly orthographic camera. Default value is true.
        - scale (s): The sensitivity for dollying the camera.
        - toolName (tn): Name of the specific tool to which this command refers.
    """
@overload #Overload for dollyCtx in ['create']
def dollyCtx(object: object, ac: bool = ..., bdt: str = ..., cd: bool = ..., dtc: bool = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ld: bool = ..., n: str = ..., oz: bool = ..., s: float = ..., tn: str = ...) -> str:
    """dollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.dollyCtx( 'dollyContext', s=1.0, ac=False, ld=False, cd=False )
        cmds.dollyCtx( 'dollyContext', e=True, bdt='surface' )
    ```

    ---
    - Args:
        - object: Input item(s).
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - boxDollyType (bdt): Set the behavior of where the camera's center of interest is set to after the box dolly. Insurfacemode, the center of interest will be snapped to the surface point at the center of the marquee. Inbboxmode, the closest bounding box to the
            camera will be used. Bounding box mode will use the selection mask to determine which objects to include into the calculation.
        - centerOfInterestDolly (cd): Set the translate the camera's center of interest. Left and right drag movements with the mouse will translate the center of interest towards or away respectively from the camera. The center of interest can be snapped to objects by using
            the left mouse button for selection. The default select mask will be used.
        - dollyTowardsCenter (dtc): Dolly towards center (if true), else dolly towards point where user clicks in the view.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localDolly (ld): Dolly with respect to the camera's center of interest. The camera will not pass through the center of interest. Local dolly only applies to perspective cameras.
        - name (n): If this is a tool command, name the tool appropriately.
        - orthoZoom (oz): Zoom orthographic view (if true), else dolly orthographic camera. Default value is true.
        - scale (s): The sensitivity for dollying the camera.
        - toolName (tn): Name of the specific tool to which this command refers.
    """
@overload #Overload for dollyCtx in ['create']
def dollyCtx(object: object, alternateContext: bool = ..., ac: bool = ..., boxDollyType: str = ..., bdt: str = ..., centerOfInterestDolly: bool = ..., cd: bool = ..., dollyTowardsCenter: bool = ..., dtc: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., localDolly: bool = ..., ld: bool = ..., name: str = ..., n: str = ..., orthoZoom: bool = ..., oz: bool = ..., scale: float = ..., s: float = ..., toolName: str = ..., tn: str = ...) -> str:
    """dollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.dollyCtx( 'dollyContext', s=1.0, ac=False, ld=False, cd=False )
        cmds.dollyCtx( 'dollyContext', e=True, bdt='surface' )
    ```

    ---
    - Args:
        - object: Input item(s).
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - boxDollyType (bdt): Set the behavior of where the camera's center of interest is set to after the box dolly. Insurfacemode, the center of interest will be snapped to the surface point at the center of the marquee. Inbboxmode, the closest bounding box to the
            camera will be used. Bounding box mode will use the selection mask to determine which objects to include into the calculation.
        - centerOfInterestDolly (cd): Set the translate the camera's center of interest. Left and right drag movements with the mouse will translate the center of interest towards or away respectively from the camera. The center of interest can be snapped to objects by using
            the left mouse button for selection. The default select mask will be used.
        - dollyTowardsCenter (dtc): Dolly towards center (if true), else dolly towards point where user clicks in the view.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localDolly (ld): Dolly with respect to the camera's center of interest. The camera will not pass through the center of interest. Local dolly only applies to perspective cameras.
        - name (n): If this is a tool command, name the tool appropriately.
        - orthoZoom (oz): Zoom orthographic view (if true), else dolly orthographic camera. Default value is true.
        - scale (s): The sensitivity for dollying the camera.
        - toolName (tn): Name of the specific tool to which this command refers.
    """
@overload #Overload for dollyCtx in ['query']
def dollyCtx(object: object, alternateContext: bool = ..., boxDollyType: str = ..., centerOfInterestDolly: bool = ..., dollyTowardsCenter: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., localDolly: bool = ..., orthoZoom: bool = ..., scale: float = ..., toolName: str = ..., query: bool = ...) -> str:
    """dollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.dollyCtx( 'dollyContext', s=1.0, ac=False, ld=False, cd=False )
        cmds.dollyCtx( 'dollyContext', e=True, bdt='surface' )
    ```

    ---
    - Args:
        - object: Input item(s).
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - boxDollyType (bdt): Set the behavior of where the camera's center of interest is set to after the box dolly. Insurfacemode, the center of interest will be snapped to the surface point at the center of the marquee. Inbboxmode, the closest bounding box to the
            camera will be used. Bounding box mode will use the selection mask to determine which objects to include into the calculation.
        - centerOfInterestDolly (cd): Set the translate the camera's center of interest. Left and right drag movements with the mouse will translate the center of interest towards or away respectively from the camera. The center of interest can be snapped to objects by using
            the left mouse button for selection. The default select mask will be used.
        - dollyTowardsCenter (dtc): Dolly towards center (if true), else dolly towards point where user clicks in the view.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localDolly (ld): Dolly with respect to the camera's center of interest. The camera will not pass through the center of interest. Local dolly only applies to perspective cameras.
        - orthoZoom (oz): Zoom orthographic view (if true), else dolly orthographic camera. Default value is true.
        - scale (s): The sensitivity for dollying the camera.
        - toolName (tn): Name of the specific tool to which this command refers.
        - query (q): Query mode flag
    """
@overload #Overload for dollyCtx in ['query']
def dollyCtx(object: object, ac: bool = ..., bdt: str = ..., cd: bool = ..., dtc: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ld: bool = ..., oz: bool = ..., s: float = ..., tn: str = ..., q: bool = ...) -> str:
    """dollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.dollyCtx( 'dollyContext', s=1.0, ac=False, ld=False, cd=False )
        cmds.dollyCtx( 'dollyContext', e=True, bdt='surface' )
    ```

    ---
    - Args:
        - object: Input item(s).
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - boxDollyType (bdt): Set the behavior of where the camera's center of interest is set to after the box dolly. Insurfacemode, the center of interest will be snapped to the surface point at the center of the marquee. Inbboxmode, the closest bounding box to the
            camera will be used. Bounding box mode will use the selection mask to determine which objects to include into the calculation.
        - centerOfInterestDolly (cd): Set the translate the camera's center of interest. Left and right drag movements with the mouse will translate the center of interest towards or away respectively from the camera. The center of interest can be snapped to objects by using
            the left mouse button for selection. The default select mask will be used.
        - dollyTowardsCenter (dtc): Dolly towards center (if true), else dolly towards point where user clicks in the view.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localDolly (ld): Dolly with respect to the camera's center of interest. The camera will not pass through the center of interest. Local dolly only applies to perspective cameras.
        - orthoZoom (oz): Zoom orthographic view (if true), else dolly orthographic camera. Default value is true.
        - scale (s): The sensitivity for dollying the camera.
        - toolName (tn): Name of the specific tool to which this command refers.
        - query (q): Query mode flag
    """
@overload #Overload for dollyCtx in ['query']
def dollyCtx(object: object, alternateContext: bool = ..., ac: bool = ..., boxDollyType: str = ..., bdt: str = ..., centerOfInterestDolly: bool = ..., cd: bool = ..., dollyTowardsCenter: bool = ..., dtc: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., localDolly: bool = ..., ld: bool = ..., orthoZoom: bool = ..., oz: bool = ..., scale: float = ..., s: float = ..., toolName: str = ..., tn: str = ..., query: bool = ..., q: bool = ...) -> str:
    """dollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.dollyCtx( 'dollyContext', s=1.0, ac=False, ld=False, cd=False )
        cmds.dollyCtx( 'dollyContext', e=True, bdt='surface' )
    ```

    ---
    - Args:
        - object: Input item(s).
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - boxDollyType (bdt): Set the behavior of where the camera's center of interest is set to after the box dolly. Insurfacemode, the center of interest will be snapped to the surface point at the center of the marquee. Inbboxmode, the closest bounding box to the
            camera will be used. Bounding box mode will use the selection mask to determine which objects to include into the calculation.
        - centerOfInterestDolly (cd): Set the translate the camera's center of interest. Left and right drag movements with the mouse will translate the center of interest towards or away respectively from the camera. The center of interest can be snapped to objects by using
            the left mouse button for selection. The default select mask will be used.
        - dollyTowardsCenter (dtc): Dolly towards center (if true), else dolly towards point where user clicks in the view.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localDolly (ld): Dolly with respect to the camera's center of interest. The camera will not pass through the center of interest. Local dolly only applies to perspective cameras.
        - orthoZoom (oz): Zoom orthographic view (if true), else dolly orthographic camera. Default value is true.
        - scale (s): The sensitivity for dollying the camera.
        - toolName (tn): Name of the specific tool to which this command refers.
        - query (q): Query mode flag
    """
@overload #Overload for dollyCtx in ['edit']
def dollyCtx(object: object, boxDollyType: str = ..., centerOfInterestDolly: bool = ..., dollyTowardsCenter: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., localDolly: bool = ..., orthoZoom: bool = ..., scale: float = ..., edit: bool = ...) -> str:
    """dollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.dollyCtx( 'dollyContext', s=1.0, ac=False, ld=False, cd=False )
        cmds.dollyCtx( 'dollyContext', e=True, bdt='surface' )
    ```

    ---
    - Args:
        - object: Input item(s).
        - boxDollyType (bdt): Set the behavior of where the camera's center of interest is set to after the box dolly. Insurfacemode, the center of interest will be snapped to the surface point at the center of the marquee. Inbboxmode, the closest bounding box to the
            camera will be used. Bounding box mode will use the selection mask to determine which objects to include into the calculation.
        - centerOfInterestDolly (cd): Set the translate the camera's center of interest. Left and right drag movements with the mouse will translate the center of interest towards or away respectively from the camera. The center of interest can be snapped to objects by using
            the left mouse button for selection. The default select mask will be used.
        - dollyTowardsCenter (dtc): Dolly towards center (if true), else dolly towards point where user clicks in the view.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localDolly (ld): Dolly with respect to the camera's center of interest. The camera will not pass through the center of interest. Local dolly only applies to perspective cameras.
        - orthoZoom (oz): Zoom orthographic view (if true), else dolly orthographic camera. Default value is true.
        - scale (s): The sensitivity for dollying the camera.
        - edit (e): Edit mode flag
    """
@overload #Overload for dollyCtx in ['edit']
def dollyCtx(object: object, bdt: str = ..., cd: bool = ..., dtc: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ld: bool = ..., oz: bool = ..., s: float = ..., e: bool = ...) -> str:
    """dollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.dollyCtx( 'dollyContext', s=1.0, ac=False, ld=False, cd=False )
        cmds.dollyCtx( 'dollyContext', e=True, bdt='surface' )
    ```

    ---
    - Args:
        - object: Input item(s).
        - boxDollyType (bdt): Set the behavior of where the camera's center of interest is set to after the box dolly. Insurfacemode, the center of interest will be snapped to the surface point at the center of the marquee. Inbboxmode, the closest bounding box to the
            camera will be used. Bounding box mode will use the selection mask to determine which objects to include into the calculation.
        - centerOfInterestDolly (cd): Set the translate the camera's center of interest. Left and right drag movements with the mouse will translate the center of interest towards or away respectively from the camera. The center of interest can be snapped to objects by using
            the left mouse button for selection. The default select mask will be used.
        - dollyTowardsCenter (dtc): Dolly towards center (if true), else dolly towards point where user clicks in the view.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localDolly (ld): Dolly with respect to the camera's center of interest. The camera will not pass through the center of interest. Local dolly only applies to perspective cameras.
        - orthoZoom (oz): Zoom orthographic view (if true), else dolly orthographic camera. Default value is true.
        - scale (s): The sensitivity for dollying the camera.
        - edit (e): Edit mode flag
    """
@overload #Overload for dollyCtx in ['edit']
def dollyCtx(object: object, boxDollyType: str = ..., bdt: str = ..., centerOfInterestDolly: bool = ..., cd: bool = ..., dollyTowardsCenter: bool = ..., dtc: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., localDolly: bool = ..., ld: bool = ..., orthoZoom: bool = ..., oz: bool = ..., scale: float = ..., s: float = ..., edit: bool = ..., e: bool = ...) -> str:
    """dollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.dollyCtx( 'dollyContext', s=1.0, ac=False, ld=False, cd=False )
        cmds.dollyCtx( 'dollyContext', e=True, bdt='surface' )
    ```

    ---
    - Args:
        - object: Input item(s).
        - boxDollyType (bdt): Set the behavior of where the camera's center of interest is set to after the box dolly. Insurfacemode, the center of interest will be snapped to the surface point at the center of the marquee. Inbboxmode, the closest bounding box to the
            camera will be used. Bounding box mode will use the selection mask to determine which objects to include into the calculation.
        - centerOfInterestDolly (cd): Set the translate the camera's center of interest. Left and right drag movements with the mouse will translate the center of interest towards or away respectively from the camera. The center of interest can be snapped to objects by using
            the left mouse button for selection. The default select mask will be used.
        - dollyTowardsCenter (dtc): Dolly towards center (if true), else dolly towards point where user clicks in the view.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localDolly (ld): Dolly with respect to the camera's center of interest. The camera will not pass through the center of interest. Local dolly only applies to perspective cameras.
        - orthoZoom (oz): Zoom orthographic view (if true), else dolly orthographic camera. Default value is true.
        - scale (s): The sensitivity for dollying the camera.
        - edit (e): Edit mode flag
    """
