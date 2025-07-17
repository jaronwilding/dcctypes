"""Stub files for Contexts category in Maya commands, command: manipMoveLimitsCtx."""

from typing import Any, overload

@overload #Overload for manipMoveLimitsCtx in ['create']
def manipMoveLimitsCtx(exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ...) -> str:
    """manipMoveLimitsCtx is undoable, queryable, and editable.
    
    Create a context for the translate limits manipulator.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.manipMoveLimitsCtx()
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for manipMoveLimitsCtx in ['create']
def manipMoveLimitsCtx(ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ...) -> str:
    """manipMoveLimitsCtx is undoable, queryable, and editable.
    
    Create a context for the translate limits manipulator.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.manipMoveLimitsCtx()
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for manipMoveLimitsCtx in ['create']
def manipMoveLimitsCtx(exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ...) -> str:
    """manipMoveLimitsCtx is undoable, queryable, and editable.
    
    Create a context for the translate limits manipulator.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.manipMoveLimitsCtx()
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for manipMoveLimitsCtx in ['query']
def manipMoveLimitsCtx(image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> str:
    """manipMoveLimitsCtx is undoable, queryable, and editable.
    
    Create a context for the translate limits manipulator.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.manipMoveLimitsCtx()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for manipMoveLimitsCtx in ['query']
def manipMoveLimitsCtx(i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> str:
    """manipMoveLimitsCtx is undoable, queryable, and editable.
    
    Create a context for the translate limits manipulator.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.manipMoveLimitsCtx()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for manipMoveLimitsCtx in ['query']
def manipMoveLimitsCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> str:
    """manipMoveLimitsCtx is undoable, queryable, and editable.
    
    Create a context for the translate limits manipulator.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.manipMoveLimitsCtx()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for manipMoveLimitsCtx in ['edit']
def manipMoveLimitsCtx(image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> str:
    """manipMoveLimitsCtx is undoable, queryable, and editable.
    
    Create a context for the translate limits manipulator.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.manipMoveLimitsCtx()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for manipMoveLimitsCtx in ['edit']
def manipMoveLimitsCtx(i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> str:
    """manipMoveLimitsCtx is undoable, queryable, and editable.
    
    Create a context for the translate limits manipulator.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.manipMoveLimitsCtx()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for manipMoveLimitsCtx in ['edit']
def manipMoveLimitsCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """manipMoveLimitsCtx is undoable, queryable, and editable.
    
    Create a context for the translate limits manipulator.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.manipMoveLimitsCtx()
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
