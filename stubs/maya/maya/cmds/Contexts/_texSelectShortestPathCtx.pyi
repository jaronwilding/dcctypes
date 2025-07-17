"""Stub files for Contexts category in Maya commands, command: texSelectShortestPathCtx."""

from typing import Any, overload

@overload #Overload for texSelectShortestPathCtx in ['create']
def texSelectShortestPathCtx(exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ...) -> None:
    """texSelectShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the texture editor window.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new poly shortest edge path context:
        #
        cmds.texSelectShortestPathCtx( 'PolyTexShortestPath' )
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for texSelectShortestPathCtx in ['create']
def texSelectShortestPathCtx(ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ...) -> None:
    """texSelectShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the texture editor window.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new poly shortest edge path context:
        #
        cmds.texSelectShortestPathCtx( 'PolyTexShortestPath' )
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for texSelectShortestPathCtx in ['create']
def texSelectShortestPathCtx(exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ...) -> None:
    """texSelectShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the texture editor window.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new poly shortest edge path context:
        #
        cmds.texSelectShortestPathCtx( 'PolyTexShortestPath' )
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for texSelectShortestPathCtx in ['query']
def texSelectShortestPathCtx(image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> None:
    """texSelectShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the texture editor window.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new poly shortest edge path context:
        #
        cmds.texSelectShortestPathCtx( 'PolyTexShortestPath' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for texSelectShortestPathCtx in ['query']
def texSelectShortestPathCtx(i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> None:
    """texSelectShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the texture editor window.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new poly shortest edge path context:
        #
        cmds.texSelectShortestPathCtx( 'PolyTexShortestPath' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for texSelectShortestPathCtx in ['query']
def texSelectShortestPathCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> None:
    """texSelectShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the texture editor window.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new poly shortest edge path context:
        #
        cmds.texSelectShortestPathCtx( 'PolyTexShortestPath' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for texSelectShortestPathCtx in ['edit']
def texSelectShortestPathCtx(image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> None:
    """texSelectShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the texture editor window.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new poly shortest edge path context:
        #
        cmds.texSelectShortestPathCtx( 'PolyTexShortestPath' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for texSelectShortestPathCtx in ['edit']
def texSelectShortestPathCtx(i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> None:
    """texSelectShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the texture editor window.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new poly shortest edge path context:
        #
        cmds.texSelectShortestPathCtx( 'PolyTexShortestPath' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for texSelectShortestPathCtx in ['edit']
def texSelectShortestPathCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> None:
    """texSelectShortestPathCtx is undoable, queryable, and editable.
    
    Creates a new context to select shortest edge path between two vertices or UVs
    in the texture editor window.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new poly shortest edge path context:
        #
        cmds.texSelectShortestPathCtx( 'PolyTexShortestPath' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
