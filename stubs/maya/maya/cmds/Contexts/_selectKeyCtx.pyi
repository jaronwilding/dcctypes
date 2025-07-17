"""Stub files for Contexts category in Maya commands, command: selectKeyCtx."""

from typing import Any, overload

@overload #Overload for selectKeyCtx in ['create']
def selectKeyCtx(contextName: contextName, exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ...) -> None:
    """selectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to select keyframes within
    the graph editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a select key context for the graph editor
        #
        cmds.selectKeyCtx( 'selectKeyContext' )
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
@overload #Overload for selectKeyCtx in ['create']
def selectKeyCtx(contextName: contextName, ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ...) -> None:
    """selectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to select keyframes within
    the graph editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a select key context for the graph editor
        #
        cmds.selectKeyCtx( 'selectKeyContext' )
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
@overload #Overload for selectKeyCtx in ['create']
def selectKeyCtx(contextName: contextName, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ...) -> None:
    """selectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to select keyframes within
    the graph editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a select key context for the graph editor
        #
        cmds.selectKeyCtx( 'selectKeyContext' )
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
@overload #Overload for selectKeyCtx in ['query']
def selectKeyCtx(contextName: contextName, image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> None:
    """selectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to select keyframes within
    the graph editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a select key context for the graph editor
        #
        cmds.selectKeyCtx( 'selectKeyContext' )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for selectKeyCtx in ['query']
def selectKeyCtx(contextName: contextName, i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> None:
    """selectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to select keyframes within
    the graph editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a select key context for the graph editor
        #
        cmds.selectKeyCtx( 'selectKeyContext' )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for selectKeyCtx in ['query']
def selectKeyCtx(contextName: contextName, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> None:
    """selectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to select keyframes within
    the graph editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a select key context for the graph editor
        #
        cmds.selectKeyCtx( 'selectKeyContext' )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for selectKeyCtx in ['edit']
def selectKeyCtx(contextName: contextName, image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> None:
    """selectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to select keyframes within
    the graph editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a select key context for the graph editor
        #
        cmds.selectKeyCtx( 'selectKeyContext' )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for selectKeyCtx in ['edit']
def selectKeyCtx(contextName: contextName, i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> None:
    """selectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to select keyframes within
    the graph editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a select key context for the graph editor
        #
        cmds.selectKeyCtx( 'selectKeyContext' )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for selectKeyCtx in ['edit']
def selectKeyCtx(contextName: contextName, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> None:
    """selectKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to select keyframes within
    the graph editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a select key context for the graph editor
        #
        cmds.selectKeyCtx( 'selectKeyContext' )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
