"""Stub files for Contexts category in Maya commands, command: keyframeRegionDollyCtx."""

from typing import Any, overload

@overload #Overload for keyframeRegionDollyCtx in ['create']
def keyframeRegionDollyCtx(exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ...) -> str:
    """keyframeRegionDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create a dolly context for the dope sheet editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a dolly view context for the dope sheet editor
        #
        cmds.keyframeRegionDollyCtx( 'keyframeRegionDollyContext' )
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
@overload #Overload for keyframeRegionDollyCtx in ['create']
def keyframeRegionDollyCtx(ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ...) -> str:
    """keyframeRegionDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create a dolly context for the dope sheet editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a dolly view context for the dope sheet editor
        #
        cmds.keyframeRegionDollyCtx( 'keyframeRegionDollyContext' )
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
@overload #Overload for keyframeRegionDollyCtx in ['create']
def keyframeRegionDollyCtx(exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ...) -> str:
    """keyframeRegionDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create a dolly context for the dope sheet editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a dolly view context for the dope sheet editor
        #
        cmds.keyframeRegionDollyCtx( 'keyframeRegionDollyContext' )
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
@overload #Overload for keyframeRegionDollyCtx in ['query']
def keyframeRegionDollyCtx(image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> str:
    """keyframeRegionDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create a dolly context for the dope sheet editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a dolly view context for the dope sheet editor
        #
        cmds.keyframeRegionDollyCtx( 'keyframeRegionDollyContext' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for keyframeRegionDollyCtx in ['query']
def keyframeRegionDollyCtx(i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> str:
    """keyframeRegionDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create a dolly context for the dope sheet editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a dolly view context for the dope sheet editor
        #
        cmds.keyframeRegionDollyCtx( 'keyframeRegionDollyContext' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for keyframeRegionDollyCtx in ['query']
def keyframeRegionDollyCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> str:
    """keyframeRegionDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create a dolly context for the dope sheet editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a dolly view context for the dope sheet editor
        #
        cmds.keyframeRegionDollyCtx( 'keyframeRegionDollyContext' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for keyframeRegionDollyCtx in ['edit']
def keyframeRegionDollyCtx(image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> str:
    """keyframeRegionDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create a dolly context for the dope sheet editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a dolly view context for the dope sheet editor
        #
        cmds.keyframeRegionDollyCtx( 'keyframeRegionDollyContext' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for keyframeRegionDollyCtx in ['edit']
def keyframeRegionDollyCtx(i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> str:
    """keyframeRegionDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create a dolly context for the dope sheet editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a dolly view context for the dope sheet editor
        #
        cmds.keyframeRegionDollyCtx( 'keyframeRegionDollyContext' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for keyframeRegionDollyCtx in ['edit']
def keyframeRegionDollyCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """keyframeRegionDollyCtx is undoable, queryable, and editable.
    
    This command can be used to create a dolly context for the dope sheet editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a dolly view context for the dope sheet editor
        #
        cmds.keyframeRegionDollyCtx( 'keyframeRegionDollyContext' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
