"""Stub files for Contexts category in Maya commands, command: boxDollyCtx."""

from typing import Any, overload

@overload #Overload for boxDollyCtx in ['create']
def boxDollyCtx(alternateContext: bool = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., toolName: str = ...) -> str:
    """boxDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.boxDollyCtx( 'boxDollyContext', ac=False )
    ```

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
    """
@overload #Overload for boxDollyCtx in ['create']
def boxDollyCtx(ac: bool = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., tn: str = ...) -> str:
    """boxDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.boxDollyCtx( 'boxDollyContext', ac=False )
    ```

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
    """
@overload #Overload for boxDollyCtx in ['create']
def boxDollyCtx(alternateContext: bool = ..., ac: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., toolName: str = ..., tn: str = ...) -> str:
    """boxDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.boxDollyCtx( 'boxDollyContext', ac=False )
    ```

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
    """
@overload #Overload for boxDollyCtx in ['query']
def boxDollyCtx(alternateContext: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., toolName: str = ..., query: bool = ...) -> str:
    """boxDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.boxDollyCtx( 'boxDollyContext', ac=False )
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - query (q): Query mode flag
    """
@overload #Overload for boxDollyCtx in ['query']
def boxDollyCtx(ac: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., tn: str = ..., q: bool = ...) -> str:
    """boxDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.boxDollyCtx( 'boxDollyContext', ac=False )
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - query (q): Query mode flag
    """
@overload #Overload for boxDollyCtx in ['query']
def boxDollyCtx(alternateContext: bool = ..., ac: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., toolName: str = ..., tn: str = ..., query: bool = ..., q: bool = ...) -> str:
    """boxDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.boxDollyCtx( 'boxDollyContext', ac=False )
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - query (q): Query mode flag
    """
@overload #Overload for boxDollyCtx in ['edit']
def boxDollyCtx(image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> str:
    """boxDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.boxDollyCtx( 'boxDollyContext', ac=False )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for boxDollyCtx in ['edit']
def boxDollyCtx(i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> str:
    """boxDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.boxDollyCtx( 'boxDollyContext', ac=False )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for boxDollyCtx in ['edit']
def boxDollyCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """boxDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a dolly context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.boxDollyCtx( 'boxDollyContext', ac=False )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
