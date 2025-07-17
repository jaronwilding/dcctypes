"""Stub files for Contexts category in Maya commands, command: insertJointCtx."""

from typing import Any, overload

@overload #Overload for insertJointCtx in ['create']
def insertJointCtx(exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ...) -> str:
    """insertJointCtx is undoable, queryable, and editable.
    
    The command will create an insert joint context. The insert joint tool inserts
    joints into an existing chain of joints.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.insertJointCtx()
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for insertJointCtx in ['create']
def insertJointCtx(ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ...) -> str:
    """insertJointCtx is undoable, queryable, and editable.
    
    The command will create an insert joint context. The insert joint tool inserts
    joints into an existing chain of joints.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.insertJointCtx()
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for insertJointCtx in ['create']
def insertJointCtx(exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ...) -> str:
    """insertJointCtx is undoable, queryable, and editable.
    
    The command will create an insert joint context. The insert joint tool inserts
    joints into an existing chain of joints.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.insertJointCtx()
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for insertJointCtx in ['query']
def insertJointCtx(image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> str:
    """insertJointCtx is undoable, queryable, and editable.
    
    The command will create an insert joint context. The insert joint tool inserts
    joints into an existing chain of joints.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.insertJointCtx()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for insertJointCtx in ['query']
def insertJointCtx(i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> str:
    """insertJointCtx is undoable, queryable, and editable.
    
    The command will create an insert joint context. The insert joint tool inserts
    joints into an existing chain of joints.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.insertJointCtx()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for insertJointCtx in ['query']
def insertJointCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> str:
    """insertJointCtx is undoable, queryable, and editable.
    
    The command will create an insert joint context. The insert joint tool inserts
    joints into an existing chain of joints.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.insertJointCtx()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for insertJointCtx in ['edit']
def insertJointCtx(image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> str:
    """insertJointCtx is undoable, queryable, and editable.
    
    The command will create an insert joint context. The insert joint tool inserts
    joints into an existing chain of joints.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.insertJointCtx()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for insertJointCtx in ['edit']
def insertJointCtx(i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> str:
    """insertJointCtx is undoable, queryable, and editable.
    
    The command will create an insert joint context. The insert joint tool inserts
    joints into an existing chain of joints.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.insertJointCtx()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for insertJointCtx in ['edit']
def insertJointCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """insertJointCtx is undoable, queryable, and editable.
    
    The command will create an insert joint context. The insert joint tool inserts
    joints into an existing chain of joints.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.insertJointCtx()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
