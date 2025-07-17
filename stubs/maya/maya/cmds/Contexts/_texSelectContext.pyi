"""Stub files for Contexts category in Maya commands, command: texSelectContext."""

from typing import Any, overload

@overload #Overload for texSelectContext in ['create']
def texSelectContext(exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ...) -> str:
    """texSelectContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.texSelectContext()
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for texSelectContext in ['create']
def texSelectContext(ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ...) -> str:
    """texSelectContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.texSelectContext()
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for texSelectContext in ['create']
def texSelectContext(exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ...) -> str:
    """texSelectContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.texSelectContext()
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for texSelectContext in ['query']
def texSelectContext(image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> str:
    """texSelectContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.texSelectContext()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for texSelectContext in ['query']
def texSelectContext(i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> str:
    """texSelectContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.texSelectContext()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for texSelectContext in ['query']
def texSelectContext(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> str:
    """texSelectContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.texSelectContext()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for texSelectContext in ['edit']
def texSelectContext(image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> str:
    """texSelectContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.texSelectContext()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for texSelectContext in ['edit']
def texSelectContext(i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> str:
    """texSelectContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.texSelectContext()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for texSelectContext in ['edit']
def texSelectContext(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """texSelectContext is undoable, queryable, and editable.
    
    Command used to register the texSelectCtx tool.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.texSelectContext()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
