"""Stub files for Contexts category in Maya commands, command: rollCtx."""

from typing import Any, overload

@overload #Overload for rollCtx in ['create']
def rollCtx([context]: [context], alternateContext: bool = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., rollScale: float = ..., toolName: str = ...) -> str:
    """rollCtx is undoable, queryable, and editable.
    
    Create, edit, or query a roll context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.rollCtx( 'rollContext', rs=30.0 )
    ```

    ---
    - Args:
        - [context]: Input item(s).
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - rollScale (rs): In degrees of rotation per 100 pixels of cursor drag.
        - toolName (tn): Name of the specific tool to which this command refers.
    """
@overload #Overload for rollCtx in ['create']
def rollCtx([context]: [context], ac: bool = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., rs: float = ..., tn: str = ...) -> str:
    """rollCtx is undoable, queryable, and editable.
    
    Create, edit, or query a roll context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.rollCtx( 'rollContext', rs=30.0 )
    ```

    ---
    - Args:
        - [context]: Input item(s).
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - rollScale (rs): In degrees of rotation per 100 pixels of cursor drag.
        - toolName (tn): Name of the specific tool to which this command refers.
    """
@overload #Overload for rollCtx in ['create']
def rollCtx([context]: [context], alternateContext: bool = ..., ac: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., rollScale: float = ..., rs: float = ..., toolName: str = ..., tn: str = ...) -> str:
    """rollCtx is undoable, queryable, and editable.
    
    Create, edit, or query a roll context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.rollCtx( 'rollContext', rs=30.0 )
    ```

    ---
    - Args:
        - [context]: Input item(s).
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - rollScale (rs): In degrees of rotation per 100 pixels of cursor drag.
        - toolName (tn): Name of the specific tool to which this command refers.
    """
@overload #Overload for rollCtx in ['query']
def rollCtx([context]: [context], alternateContext: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., rollScale: float = ..., toolName: str = ..., query: bool = ...) -> str:
    """rollCtx is undoable, queryable, and editable.
    
    Create, edit, or query a roll context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.rollCtx( 'rollContext', rs=30.0 )
    ```

    ---
    - Args:
        - [context]: Input item(s).
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - rollScale (rs): In degrees of rotation per 100 pixels of cursor drag.
        - toolName (tn): Name of the specific tool to which this command refers.
        - query (q): Query mode flag
    """
@overload #Overload for rollCtx in ['query']
def rollCtx([context]: [context], ac: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., rs: float = ..., tn: str = ..., q: bool = ...) -> str:
    """rollCtx is undoable, queryable, and editable.
    
    Create, edit, or query a roll context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.rollCtx( 'rollContext', rs=30.0 )
    ```

    ---
    - Args:
        - [context]: Input item(s).
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - rollScale (rs): In degrees of rotation per 100 pixels of cursor drag.
        - toolName (tn): Name of the specific tool to which this command refers.
        - query (q): Query mode flag
    """
@overload #Overload for rollCtx in ['query']
def rollCtx([context]: [context], alternateContext: bool = ..., ac: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., rollScale: float = ..., rs: float = ..., toolName: str = ..., tn: str = ..., query: bool = ..., q: bool = ...) -> str:
    """rollCtx is undoable, queryable, and editable.
    
    Create, edit, or query a roll context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.rollCtx( 'rollContext', rs=30.0 )
    ```

    ---
    - Args:
        - [context]: Input item(s).
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - rollScale (rs): In degrees of rotation per 100 pixels of cursor drag.
        - toolName (tn): Name of the specific tool to which this command refers.
        - query (q): Query mode flag
    """
@overload #Overload for rollCtx in ['edit']
def rollCtx([context]: [context], image1: str = ..., image2: str = ..., image3: str = ..., rollScale: float = ..., edit: bool = ...) -> str:
    """rollCtx is undoable, queryable, and editable.
    
    Create, edit, or query a roll context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.rollCtx( 'rollContext', rs=30.0 )
    ```

    ---
    - Args:
        - [context]: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - rollScale (rs): In degrees of rotation per 100 pixels of cursor drag.
        - edit (e): Edit mode flag
    """
@overload #Overload for rollCtx in ['edit']
def rollCtx([context]: [context], i1: str = ..., i2: str = ..., i3: str = ..., rs: float = ..., e: bool = ...) -> str:
    """rollCtx is undoable, queryable, and editable.
    
    Create, edit, or query a roll context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.rollCtx( 'rollContext', rs=30.0 )
    ```

    ---
    - Args:
        - [context]: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - rollScale (rs): In degrees of rotation per 100 pixels of cursor drag.
        - edit (e): Edit mode flag
    """
@overload #Overload for rollCtx in ['edit']
def rollCtx([context]: [context], image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., rollScale: float = ..., rs: float = ..., edit: bool = ..., e: bool = ...) -> str:
    """rollCtx is undoable, queryable, and editable.
    
    Create, edit, or query a roll context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.rollCtx( 'rollContext', rs=30.0 )
    ```

    ---
    - Args:
        - [context]: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - rollScale (rs): In degrees of rotation per 100 pixels of cursor drag.
        - edit (e): Edit mode flag
    """
