"""Stub files for Contexts category in Maya commands, command: filterGaussianCtx."""

from typing import Any, overload

@overload #Overload for filterGaussianCtx in ['create']
def filterGaussianCtx(contextName: contextName, exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ...) -> str:
    """filterGaussianCtx is undoable, queryable, and editable.
    
    Creates a smooth (gaussian) filter context. This context can ben used to
    interactively preview/edit the smooth (gaussian) filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterGaussianCtx()
        # Set the context to the new context just created
        cmds.setToolTo(ctx)
        # Adjust the width and sample count to selected curves.
        cmds.filterGaussianCtx(ctx, e=True, width=3, sampleCount=8)
        # Apply current settings to the real curves.
        cmds.filterGaussianCtx(ctx, e=True, a=True)
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
@overload #Overload for filterGaussianCtx in ['create']
def filterGaussianCtx(contextName: contextName, ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ...) -> str:
    """filterGaussianCtx is undoable, queryable, and editable.
    
    Creates a smooth (gaussian) filter context. This context can ben used to
    interactively preview/edit the smooth (gaussian) filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterGaussianCtx()
        # Set the context to the new context just created
        cmds.setToolTo(ctx)
        # Adjust the width and sample count to selected curves.
        cmds.filterGaussianCtx(ctx, e=True, width=3, sampleCount=8)
        # Apply current settings to the real curves.
        cmds.filterGaussianCtx(ctx, e=True, a=True)
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
@overload #Overload for filterGaussianCtx in ['create']
def filterGaussianCtx(contextName: contextName, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ...) -> str:
    """filterGaussianCtx is undoable, queryable, and editable.
    
    Creates a smooth (gaussian) filter context. This context can ben used to
    interactively preview/edit the smooth (gaussian) filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterGaussianCtx()
        # Set the context to the new context just created
        cmds.setToolTo(ctx)
        # Adjust the width and sample count to selected curves.
        cmds.filterGaussianCtx(ctx, e=True, width=3, sampleCount=8)
        # Apply current settings to the real curves.
        cmds.filterGaussianCtx(ctx, e=True, a=True)
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
@overload #Overload for filterGaussianCtx in ['query']
def filterGaussianCtx(contextName: contextName, endTime: time = ..., image1: str = ..., image2: str = ..., image3: str = ..., sampleCount: int = ..., selectedKeys: bool = ..., startTime: time = ..., useQuaternion: bool = ..., width: time = ..., query: bool = ...) -> str:
    """filterGaussianCtx is undoable, queryable, and editable.
    
    Creates a smooth (gaussian) filter context. This context can ben used to
    interactively preview/edit the smooth (gaussian) filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterGaussianCtx()
        # Set the context to the new context just created
        cmds.setToolTo(ctx)
        # Adjust the width and sample count to selected curves.
        cmds.filterGaussianCtx(ctx, e=True, width=3, sampleCount=8)
        # Apply current settings to the real curves.
        cmds.filterGaussianCtx(ctx, e=True, a=True)
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - sampleCount (sc): This parameter specifies the number of neighbor will be sampled.
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - useQuaternion (uq): When this is enabled, the filter will first convert the curves (rotation channel curves, 3 sibling requires at the same time) from Euler space to quaternions. Then apply the gaussian filter on it. Convert it back from Quaternions back to
            Euler space eventually.
        - width (w): This parameter specifies the width of the gaussian kernel shape. Wider width will
        - query (q): Query mode flag
    """
@overload #Overload for filterGaussianCtx in ['query']
def filterGaussianCtx(contextName: contextName, e: time = ..., i1: str = ..., i2: str = ..., i3: str = ..., sc: int = ..., sk: bool = ..., s: time = ..., uq: bool = ..., w: time = ..., q: bool = ...) -> str:
    """filterGaussianCtx is undoable, queryable, and editable.
    
    Creates a smooth (gaussian) filter context. This context can ben used to
    interactively preview/edit the smooth (gaussian) filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterGaussianCtx()
        # Set the context to the new context just created
        cmds.setToolTo(ctx)
        # Adjust the width and sample count to selected curves.
        cmds.filterGaussianCtx(ctx, e=True, width=3, sampleCount=8)
        # Apply current settings to the real curves.
        cmds.filterGaussianCtx(ctx, e=True, a=True)
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - sampleCount (sc): This parameter specifies the number of neighbor will be sampled.
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - useQuaternion (uq): When this is enabled, the filter will first convert the curves (rotation channel curves, 3 sibling requires at the same time) from Euler space to quaternions. Then apply the gaussian filter on it. Convert it back from Quaternions back to
            Euler space eventually.
        - width (w): This parameter specifies the width of the gaussian kernel shape. Wider width will
        - query (q): Query mode flag
    """
@overload #Overload for filterGaussianCtx in ['query']
def filterGaussianCtx(contextName: contextName, endTime: time = ..., e: time = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., sampleCount: int = ..., sc: int = ..., selectedKeys: bool = ..., sk: bool = ..., startTime: time = ..., s: time = ..., useQuaternion: bool = ..., uq: bool = ..., width: time = ..., w: time = ..., query: bool = ..., q: bool = ...) -> str:
    """filterGaussianCtx is undoable, queryable, and editable.
    
    Creates a smooth (gaussian) filter context. This context can ben used to
    interactively preview/edit the smooth (gaussian) filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterGaussianCtx()
        # Set the context to the new context just created
        cmds.setToolTo(ctx)
        # Adjust the width and sample count to selected curves.
        cmds.filterGaussianCtx(ctx, e=True, width=3, sampleCount=8)
        # Apply current settings to the real curves.
        cmds.filterGaussianCtx(ctx, e=True, a=True)
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - sampleCount (sc): This parameter specifies the number of neighbor will be sampled.
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - useQuaternion (uq): When this is enabled, the filter will first convert the curves (rotation channel curves, 3 sibling requires at the same time) from Euler space to quaternions. Then apply the gaussian filter on it. Convert it back from Quaternions back to
            Euler space eventually.
        - width (w): This parameter specifies the width of the gaussian kernel shape. Wider width will
        - query (q): Query mode flag
    """
@overload #Overload for filterGaussianCtx in ['edit']
def filterGaussianCtx(contextName: contextName, apply: bool = ..., endTime: time = ..., image1: str = ..., image2: str = ..., image3: str = ..., sampleCount: int = ..., selectedKeys: bool = ..., startTime: time = ..., useQuaternion: bool = ..., width: time = ..., edit: bool = ...) -> str:
    """filterGaussianCtx is undoable, queryable, and editable.
    
    Creates a smooth (gaussian) filter context. This context can ben used to
    interactively preview/edit the smooth (gaussian) filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterGaussianCtx()
        # Set the context to the new context just created
        cmds.setToolTo(ctx)
        # Adjust the width and sample count to selected curves.
        cmds.filterGaussianCtx(ctx, e=True, width=3, sampleCount=8)
        # Apply current settings to the real curves.
        cmds.filterGaussianCtx(ctx, e=True, a=True)
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - apply (a): When specified, finalizes the current context state and records the command for the operation. This is equivalent to completing the tool action without exiting the current tool context.
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - sampleCount (sc): This parameter specifies the number of neighbor will be sampled.
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - useQuaternion (uq): When this is enabled, the filter will first convert the curves (rotation channel curves, 3 sibling requires at the same time) from Euler space to quaternions. Then apply the gaussian filter on it. Convert it back from Quaternions back to
            Euler space eventually.
        - width (w): This parameter specifies the width of the gaussian kernel shape. Wider width will
        - edit (e): Edit mode flag
    """
@overload #Overload for filterGaussianCtx in ['edit']
def filterGaussianCtx(contextName: contextName, a: bool = ..., e: time = ..., i1: str = ..., i2: str = ..., i3: str = ..., sc: int = ..., sk: bool = ..., s: time = ..., uq: bool = ..., w: time = ..., e: bool = ...) -> str:
    """filterGaussianCtx is undoable, queryable, and editable.
    
    Creates a smooth (gaussian) filter context. This context can ben used to
    interactively preview/edit the smooth (gaussian) filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterGaussianCtx()
        # Set the context to the new context just created
        cmds.setToolTo(ctx)
        # Adjust the width and sample count to selected curves.
        cmds.filterGaussianCtx(ctx, e=True, width=3, sampleCount=8)
        # Apply current settings to the real curves.
        cmds.filterGaussianCtx(ctx, e=True, a=True)
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - apply (a): When specified, finalizes the current context state and records the command for the operation. This is equivalent to completing the tool action without exiting the current tool context.
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - sampleCount (sc): This parameter specifies the number of neighbor will be sampled.
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - useQuaternion (uq): When this is enabled, the filter will first convert the curves (rotation channel curves, 3 sibling requires at the same time) from Euler space to quaternions. Then apply the gaussian filter on it. Convert it back from Quaternions back to
            Euler space eventually.
        - width (w): This parameter specifies the width of the gaussian kernel shape. Wider width will
        - edit (e): Edit mode flag
    """
@overload #Overload for filterGaussianCtx in ['edit']
def filterGaussianCtx(contextName: contextName, apply: bool = ..., a: bool = ..., endTime: time = ..., e: time = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., sampleCount: int = ..., sc: int = ..., selectedKeys: bool = ..., sk: bool = ..., startTime: time = ..., s: time = ..., useQuaternion: bool = ..., uq: bool = ..., width: time = ..., w: time = ..., edit: bool = ..., e: bool = ...) -> str:
    """filterGaussianCtx is undoable, queryable, and editable.
    
    Creates a smooth (gaussian) filter context. This context can ben used to
    interactively preview/edit the smooth (gaussian) filter on a set of animation
    curves.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Create a context
        ctx = cmds.filterGaussianCtx()
        # Set the context to the new context just created
        cmds.setToolTo(ctx)
        # Adjust the width and sample count to selected curves.
        cmds.filterGaussianCtx(ctx, e=True, width=3, sampleCount=8)
        # Apply current settings to the real curves.
        cmds.filterGaussianCtx(ctx, e=True, a=True)
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - apply (a): When specified, finalizes the current context state and records the command for the operation. This is equivalent to completing the tool action without exiting the current tool context.
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - sampleCount (sc): This parameter specifies the number of neighbor will be sampled.
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - useQuaternion (uq): When this is enabled, the filter will first convert the curves (rotation channel curves, 3 sibling requires at the same time) from Euler space to quaternions. Then apply the gaussian filter on it. Convert it back from Quaternions back to
            Euler space eventually.
        - width (w): This parameter specifies the width of the gaussian kernel shape. Wider width will
        - edit (e): Edit mode flag
    """
