"""Stub files for Contexts category in Maya commands, command: graphSelectContext."""

from typing import Any, overload

@overload #Overload for graphSelectContext in ['create']
def graphSelectContext(exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ...) -> str:
    """graphSelectContext is undoable, queryable, and editable.
    
    This command can be used to create a selection context for the hypergraph
    editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a selection context for the hypergraph editor.
        #
        cmds.graphSelectContext( 'hyperGraphSelectContext' )
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for graphSelectContext in ['create']
def graphSelectContext(ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ...) -> str:
    """graphSelectContext is undoable, queryable, and editable.
    
    This command can be used to create a selection context for the hypergraph
    editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a selection context for the hypergraph editor.
        #
        cmds.graphSelectContext( 'hyperGraphSelectContext' )
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for graphSelectContext in ['create']
def graphSelectContext(exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ...) -> str:
    """graphSelectContext is undoable, queryable, and editable.
    
    This command can be used to create a selection context for the hypergraph
    editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a selection context for the hypergraph editor.
        #
        cmds.graphSelectContext( 'hyperGraphSelectContext' )
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for graphSelectContext in ['query']
def graphSelectContext(image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> str:
    """graphSelectContext is undoable, queryable, and editable.
    
    This command can be used to create a selection context for the hypergraph
    editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a selection context for the hypergraph editor.
        #
        cmds.graphSelectContext( 'hyperGraphSelectContext' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for graphSelectContext in ['query']
def graphSelectContext(i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> str:
    """graphSelectContext is undoable, queryable, and editable.
    
    This command can be used to create a selection context for the hypergraph
    editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a selection context for the hypergraph editor.
        #
        cmds.graphSelectContext( 'hyperGraphSelectContext' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for graphSelectContext in ['query']
def graphSelectContext(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> str:
    """graphSelectContext is undoable, queryable, and editable.
    
    This command can be used to create a selection context for the hypergraph
    editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a selection context for the hypergraph editor.
        #
        cmds.graphSelectContext( 'hyperGraphSelectContext' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for graphSelectContext in ['edit']
def graphSelectContext(image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> str:
    """graphSelectContext is undoable, queryable, and editable.
    
    This command can be used to create a selection context for the hypergraph
    editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a selection context for the hypergraph editor.
        #
        cmds.graphSelectContext( 'hyperGraphSelectContext' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for graphSelectContext in ['edit']
def graphSelectContext(i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> str:
    """graphSelectContext is undoable, queryable, and editable.
    
    This command can be used to create a selection context for the hypergraph
    editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a selection context for the hypergraph editor.
        #
        cmds.graphSelectContext( 'hyperGraphSelectContext' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for graphSelectContext in ['edit']
def graphSelectContext(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """graphSelectContext is undoable, queryable, and editable.
    
    This command can be used to create a selection context for the hypergraph
    editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a selection context for the hypergraph editor.
        #
        cmds.graphSelectContext( 'hyperGraphSelectContext' )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
