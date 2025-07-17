"""Stub files for Contexts category in Maya commands, command: filterButterworthCtx."""

from typing import Any, overload

@overload #Overload for filterButterworthCtx in ['create']
def filterButterworthCtx(contextName: contextName, exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ...) -> str:
    """filterButterworthCtx is undoable, queryable, and editable.
    
    Creates/edits a Butterworth filter context. This context can be used to
    interactively preview/edit the Butterworth filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterButterworthCtx()
        # Activate the tool context
        cmds.setToolTo( ctx )
        # Adjust the Butterworth cutoff frequency to selected keys.
        cmds.filterButterworthCtx( ctx, e=True, sk=True, cof=3.0 )
        # Apply the current settings to the selected curves.
        cmds.filterButterworthCtx( ctx, e=True, apply=True )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for filterButterworthCtx in ['create']
def filterButterworthCtx(contextName: contextName, ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ...) -> str:
    """filterButterworthCtx is undoable, queryable, and editable.
    
    Creates/edits a Butterworth filter context. This context can be used to
    interactively preview/edit the Butterworth filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterButterworthCtx()
        # Activate the tool context
        cmds.setToolTo( ctx )
        # Adjust the Butterworth cutoff frequency to selected keys.
        cmds.filterButterworthCtx( ctx, e=True, sk=True, cof=3.0 )
        # Apply the current settings to the selected curves.
        cmds.filterButterworthCtx( ctx, e=True, apply=True )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for filterButterworthCtx in ['create']
def filterButterworthCtx(contextName: contextName, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ...) -> str:
    """filterButterworthCtx is undoable, queryable, and editable.
    
    Creates/edits a Butterworth filter context. This context can be used to
    interactively preview/edit the Butterworth filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterButterworthCtx()
        # Activate the tool context
        cmds.setToolTo( ctx )
        # Adjust the Butterworth cutoff frequency to selected keys.
        cmds.filterButterworthCtx( ctx, e=True, sk=True, cof=3.0 )
        # Apply the current settings to the selected curves.
        cmds.filterButterworthCtx( ctx, e=True, apply=True )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for filterButterworthCtx in ['query']
def filterButterworthCtx(contextName: contextName, cutoffFrequency: float = ..., endTime: time = ..., image1: str = ..., image2: str = ..., image3: str = ..., keepKeysOnFrame: bool = ..., samplingRate: float = ..., selectedKeys: bool = ..., startTime: time = ..., query: bool = ...) -> str:
    """filterButterworthCtx is undoable, queryable, and editable.
    
    Creates/edits a Butterworth filter context. This context can be used to
    interactively preview/edit the Butterworth filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterButterworthCtx()
        # Activate the tool context
        cmds.setToolTo( ctx )
        # Adjust the Butterworth cutoff frequency to selected keys.
        cmds.filterButterworthCtx( ctx, e=True, sk=True, cof=3.0 )
        # Apply the current settings to the selected curves.
        cmds.filterButterworthCtx( ctx, e=True, apply=True )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - cutoffFrequency (cof): Specifies the cutoff frequency setting of the Butterworth filter. Default is 7.0.
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keepKeysOnFrame (kof): When true, the Butterworth filter will reposition output keys to whole frames for the specified sampling rate.
        - samplingRate (sr): Specifies the sampling rate setting of the Butterworth filter. Default is 30.0.
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - query (q): Query mode flag
    """
@overload #Overload for filterButterworthCtx in ['query']
def filterButterworthCtx(contextName: contextName, cof: float = ..., e: time = ..., i1: str = ..., i2: str = ..., i3: str = ..., kof: bool = ..., sr: float = ..., sk: bool = ..., s: time = ..., q: bool = ...) -> str:
    """filterButterworthCtx is undoable, queryable, and editable.
    
    Creates/edits a Butterworth filter context. This context can be used to
    interactively preview/edit the Butterworth filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterButterworthCtx()
        # Activate the tool context
        cmds.setToolTo( ctx )
        # Adjust the Butterworth cutoff frequency to selected keys.
        cmds.filterButterworthCtx( ctx, e=True, sk=True, cof=3.0 )
        # Apply the current settings to the selected curves.
        cmds.filterButterworthCtx( ctx, e=True, apply=True )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - cutoffFrequency (cof): Specifies the cutoff frequency setting of the Butterworth filter. Default is 7.0.
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keepKeysOnFrame (kof): When true, the Butterworth filter will reposition output keys to whole frames for the specified sampling rate.
        - samplingRate (sr): Specifies the sampling rate setting of the Butterworth filter. Default is 30.0.
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - query (q): Query mode flag
    """
@overload #Overload for filterButterworthCtx in ['query']
def filterButterworthCtx(contextName: contextName, cutoffFrequency: float = ..., cof: float = ..., endTime: time = ..., e: time = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., keepKeysOnFrame: bool = ..., kof: bool = ..., samplingRate: float = ..., sr: float = ..., selectedKeys: bool = ..., sk: bool = ..., startTime: time = ..., s: time = ..., query: bool = ..., q: bool = ...) -> str:
    """filterButterworthCtx is undoable, queryable, and editable.
    
    Creates/edits a Butterworth filter context. This context can be used to
    interactively preview/edit the Butterworth filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterButterworthCtx()
        # Activate the tool context
        cmds.setToolTo( ctx )
        # Adjust the Butterworth cutoff frequency to selected keys.
        cmds.filterButterworthCtx( ctx, e=True, sk=True, cof=3.0 )
        # Apply the current settings to the selected curves.
        cmds.filterButterworthCtx( ctx, e=True, apply=True )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - cutoffFrequency (cof): Specifies the cutoff frequency setting of the Butterworth filter. Default is 7.0.
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keepKeysOnFrame (kof): When true, the Butterworth filter will reposition output keys to whole frames for the specified sampling rate.
        - samplingRate (sr): Specifies the sampling rate setting of the Butterworth filter. Default is 30.0.
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - query (q): Query mode flag
    """
@overload #Overload for filterButterworthCtx in ['edit']
def filterButterworthCtx(contextName: contextName, apply: bool = ..., cutoffFrequency: float = ..., endTime: time = ..., image1: str = ..., image2: str = ..., image3: str = ..., keepKeysOnFrame: bool = ..., samplingRate: float = ..., selectedKeys: bool = ..., startTime: time = ..., edit: bool = ...) -> str:
    """filterButterworthCtx is undoable, queryable, and editable.
    
    Creates/edits a Butterworth filter context. This context can be used to
    interactively preview/edit the Butterworth filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterButterworthCtx()
        # Activate the tool context
        cmds.setToolTo( ctx )
        # Adjust the Butterworth cutoff frequency to selected keys.
        cmds.filterButterworthCtx( ctx, e=True, sk=True, cof=3.0 )
        # Apply the current settings to the selected curves.
        cmds.filterButterworthCtx( ctx, e=True, apply=True )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - apply (a): When specified, finalizes the current context state and records the command for the operation. This is equivalent to completing the tool action without exiting the current tool context.
        - cutoffFrequency (cof): Specifies the cutoff frequency setting of the Butterworth filter. Default is 7.0.
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keepKeysOnFrame (kof): When true, the Butterworth filter will reposition output keys to whole frames for the specified sampling rate.
        - samplingRate (sr): Specifies the sampling rate setting of the Butterworth filter. Default is 30.0.
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - edit (e): Edit mode flag
    """
@overload #Overload for filterButterworthCtx in ['edit']
def filterButterworthCtx(contextName: contextName, a: bool = ..., cof: float = ..., e: time = ..., i1: str = ..., i2: str = ..., i3: str = ..., kof: bool = ..., sr: float = ..., sk: bool = ..., s: time = ..., e: bool = ...) -> str:
    """filterButterworthCtx is undoable, queryable, and editable.
    
    Creates/edits a Butterworth filter context. This context can be used to
    interactively preview/edit the Butterworth filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterButterworthCtx()
        # Activate the tool context
        cmds.setToolTo( ctx )
        # Adjust the Butterworth cutoff frequency to selected keys.
        cmds.filterButterworthCtx( ctx, e=True, sk=True, cof=3.0 )
        # Apply the current settings to the selected curves.
        cmds.filterButterworthCtx( ctx, e=True, apply=True )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - apply (a): When specified, finalizes the current context state and records the command for the operation. This is equivalent to completing the tool action without exiting the current tool context.
        - cutoffFrequency (cof): Specifies the cutoff frequency setting of the Butterworth filter. Default is 7.0.
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keepKeysOnFrame (kof): When true, the Butterworth filter will reposition output keys to whole frames for the specified sampling rate.
        - samplingRate (sr): Specifies the sampling rate setting of the Butterworth filter. Default is 30.0.
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - edit (e): Edit mode flag
    """
@overload #Overload for filterButterworthCtx in ['edit']
def filterButterworthCtx(contextName: contextName, apply: bool = ..., a: bool = ..., cutoffFrequency: float = ..., cof: float = ..., endTime: time = ..., e: time = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., keepKeysOnFrame: bool = ..., kof: bool = ..., samplingRate: float = ..., sr: float = ..., selectedKeys: bool = ..., sk: bool = ..., startTime: time = ..., s: time = ..., edit: bool = ..., e: bool = ...) -> str:
    """filterButterworthCtx is undoable, queryable, and editable.
    
    Creates/edits a Butterworth filter context. This context can be used to
    interactively preview/edit the Butterworth filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterButterworthCtx()
        # Activate the tool context
        cmds.setToolTo( ctx )
        # Adjust the Butterworth cutoff frequency to selected keys.
        cmds.filterButterworthCtx( ctx, e=True, sk=True, cof=3.0 )
        # Apply the current settings to the selected curves.
        cmds.filterButterworthCtx( ctx, e=True, apply=True )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - apply (a): When specified, finalizes the current context state and records the command for the operation. This is equivalent to completing the tool action without exiting the current tool context.
        - cutoffFrequency (cof): Specifies the cutoff frequency setting of the Butterworth filter. Default is 7.0.
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keepKeysOnFrame (kof): When true, the Butterworth filter will reposition output keys to whole frames for the specified sampling rate.
        - samplingRate (sr): Specifies the sampling rate setting of the Butterworth filter. Default is 30.0.
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - edit (e): Edit mode flag
    """
