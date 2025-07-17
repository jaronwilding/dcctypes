"""Stub files for Contexts category in Maya commands, command: lassoContext."""

from typing import Any, overload

@overload #Overload for lassoContext in ['create']
def lassoContext(string: str, drawClosed: bool = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ...) -> str:
    """lassoContext is undoable, queryable, and editable.
    
    Creates a context to perform selection via a "lasso". Use for irregular
    selection regions, where the "marquee-style" select of the "selectContext" is
    inappropriate.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new lasso context, then switch to it
        cmds.lassoContext('lassoContext1')
        cmds.setToolTo('lassoContext1')
    ```

    ---
    - Args:
        - string: Input item(s).
        - drawClosed (dc): Turns the closed display of the lasso on/off.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for lassoContext in ['create']
def lassoContext(string: str, dc: bool = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ...) -> str:
    """lassoContext is undoable, queryable, and editable.
    
    Creates a context to perform selection via a "lasso". Use for irregular
    selection regions, where the "marquee-style" select of the "selectContext" is
    inappropriate.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new lasso context, then switch to it
        cmds.lassoContext('lassoContext1')
        cmds.setToolTo('lassoContext1')
    ```

    ---
    - Args:
        - string: Input item(s).
        - drawClosed (dc): Turns the closed display of the lasso on/off.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for lassoContext in ['create']
def lassoContext(string: str, drawClosed: bool = ..., dc: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ...) -> str:
    """lassoContext is undoable, queryable, and editable.
    
    Creates a context to perform selection via a "lasso". Use for irregular
    selection regions, where the "marquee-style" select of the "selectContext" is
    inappropriate.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new lasso context, then switch to it
        cmds.lassoContext('lassoContext1')
        cmds.setToolTo('lassoContext1')
    ```

    ---
    - Args:
        - string: Input item(s).
        - drawClosed (dc): Turns the closed display of the lasso on/off.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for lassoContext in ['query']
def lassoContext(string: str, drawClosed: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> str:
    """lassoContext is undoable, queryable, and editable.
    
    Creates a context to perform selection via a "lasso". Use for irregular
    selection regions, where the "marquee-style" select of the "selectContext" is
    inappropriate.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new lasso context, then switch to it
        cmds.lassoContext('lassoContext1')
        cmds.setToolTo('lassoContext1')
    ```

    ---
    - Args:
        - string: Input item(s).
        - drawClosed (dc): Turns the closed display of the lasso on/off.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for lassoContext in ['query']
def lassoContext(string: str, dc: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> str:
    """lassoContext is undoable, queryable, and editable.
    
    Creates a context to perform selection via a "lasso". Use for irregular
    selection regions, where the "marquee-style" select of the "selectContext" is
    inappropriate.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new lasso context, then switch to it
        cmds.lassoContext('lassoContext1')
        cmds.setToolTo('lassoContext1')
    ```

    ---
    - Args:
        - string: Input item(s).
        - drawClosed (dc): Turns the closed display of the lasso on/off.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for lassoContext in ['query']
def lassoContext(string: str, drawClosed: bool = ..., dc: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> str:
    """lassoContext is undoable, queryable, and editable.
    
    Creates a context to perform selection via a "lasso". Use for irregular
    selection regions, where the "marquee-style" select of the "selectContext" is
    inappropriate.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new lasso context, then switch to it
        cmds.lassoContext('lassoContext1')
        cmds.setToolTo('lassoContext1')
    ```

    ---
    - Args:
        - string: Input item(s).
        - drawClosed (dc): Turns the closed display of the lasso on/off.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for lassoContext in ['edit']
def lassoContext(string: str, drawClosed: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> str:
    """lassoContext is undoable, queryable, and editable.
    
    Creates a context to perform selection via a "lasso". Use for irregular
    selection regions, where the "marquee-style" select of the "selectContext" is
    inappropriate.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new lasso context, then switch to it
        cmds.lassoContext('lassoContext1')
        cmds.setToolTo('lassoContext1')
    ```

    ---
    - Args:
        - string: Input item(s).
        - drawClosed (dc): Turns the closed display of the lasso on/off.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for lassoContext in ['edit']
def lassoContext(string: str, dc: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> str:
    """lassoContext is undoable, queryable, and editable.
    
    Creates a context to perform selection via a "lasso". Use for irregular
    selection regions, where the "marquee-style" select of the "selectContext" is
    inappropriate.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new lasso context, then switch to it
        cmds.lassoContext('lassoContext1')
        cmds.setToolTo('lassoContext1')
    ```

    ---
    - Args:
        - string: Input item(s).
        - drawClosed (dc): Turns the closed display of the lasso on/off.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for lassoContext in ['edit']
def lassoContext(string: str, drawClosed: bool = ..., dc: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """lassoContext is undoable, queryable, and editable.
    
    Creates a context to perform selection via a "lasso". Use for irregular
    selection regions, where the "marquee-style" select of the "selectContext" is
    inappropriate.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new lasso context, then switch to it
        cmds.lassoContext('lassoContext1')
        cmds.setToolTo('lassoContext1')
    ```

    ---
    - Args:
        - string: Input item(s).
        - drawClosed (dc): Turns the closed display of the lasso on/off.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
