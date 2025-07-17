"""Stub files for Contexts category in Maya commands, command: threePointArcCtx."""

from typing import Any, overload

@overload #Overload for threePointArcCtx in ['create']
def threePointArcCtx(degree: int = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., spans: int = ...) -> str:
    """threePointArcCtx is undoable, queryable, and editable.
    
    The threePointArcCtx command creates a new context for creating 3 point arcs

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 1:
        cmds.threePointArcCtx( "arcContext", degree=1 )
        cmds.setToolTo("arcContext")
        # To query the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", e=True, degree=3 )
    ```

    ---
    - Args:
        - degree (d): VAlid values are 1 or 3. Default degree 3.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - spans (s): Default is 8.
    """
@overload #Overload for threePointArcCtx in ['create']
def threePointArcCtx(d: int = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., s: int = ...) -> str:
    """threePointArcCtx is undoable, queryable, and editable.
    
    The threePointArcCtx command creates a new context for creating 3 point arcs

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 1:
        cmds.threePointArcCtx( "arcContext", degree=1 )
        cmds.setToolTo("arcContext")
        # To query the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", e=True, degree=3 )
    ```

    ---
    - Args:
        - degree (d): VAlid values are 1 or 3. Default degree 3.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - spans (s): Default is 8.
    """
@overload #Overload for threePointArcCtx in ['create']
def threePointArcCtx(degree: int = ..., d: int = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., spans: int = ..., s: int = ...) -> str:
    """threePointArcCtx is undoable, queryable, and editable.
    
    The threePointArcCtx command creates a new context for creating 3 point arcs

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 1:
        cmds.threePointArcCtx( "arcContext", degree=1 )
        cmds.setToolTo("arcContext")
        # To query the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", e=True, degree=3 )
    ```

    ---
    - Args:
        - degree (d): VAlid values are 1 or 3. Default degree 3.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - spans (s): Default is 8.
    """
@overload #Overload for threePointArcCtx in ['query']
def threePointArcCtx(degree: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., spans: int = ..., query: bool = ...) -> str:
    """threePointArcCtx is undoable, queryable, and editable.
    
    The threePointArcCtx command creates a new context for creating 3 point arcs

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 1:
        cmds.threePointArcCtx( "arcContext", degree=1 )
        cmds.setToolTo("arcContext")
        # To query the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", e=True, degree=3 )
    ```

    ---
    - Args:
        - degree (d): VAlid values are 1 or 3. Default degree 3.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - spans (s): Default is 8.
        - query (q): Query mode flag
    """
@overload #Overload for threePointArcCtx in ['query']
def threePointArcCtx(d: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., s: int = ..., q: bool = ...) -> str:
    """threePointArcCtx is undoable, queryable, and editable.
    
    The threePointArcCtx command creates a new context for creating 3 point arcs

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 1:
        cmds.threePointArcCtx( "arcContext", degree=1 )
        cmds.setToolTo("arcContext")
        # To query the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", e=True, degree=3 )
    ```

    ---
    - Args:
        - degree (d): VAlid values are 1 or 3. Default degree 3.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - spans (s): Default is 8.
        - query (q): Query mode flag
    """
@overload #Overload for threePointArcCtx in ['query']
def threePointArcCtx(degree: int = ..., d: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., spans: int = ..., s: int = ..., query: bool = ..., q: bool = ...) -> str:
    """threePointArcCtx is undoable, queryable, and editable.
    
    The threePointArcCtx command creates a new context for creating 3 point arcs

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 1:
        cmds.threePointArcCtx( "arcContext", degree=1 )
        cmds.setToolTo("arcContext")
        # To query the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", e=True, degree=3 )
    ```

    ---
    - Args:
        - degree (d): VAlid values are 1 or 3. Default degree 3.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - spans (s): Default is 8.
        - query (q): Query mode flag
    """
@overload #Overload for threePointArcCtx in ['edit']
def threePointArcCtx(degree: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., spans: int = ..., edit: bool = ...) -> str:
    """threePointArcCtx is undoable, queryable, and editable.
    
    The threePointArcCtx command creates a new context for creating 3 point arcs

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 1:
        cmds.threePointArcCtx( "arcContext", degree=1 )
        cmds.setToolTo("arcContext")
        # To query the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", e=True, degree=3 )
    ```

    ---
    - Args:
        - degree (d): VAlid values are 1 or 3. Default degree 3.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - spans (s): Default is 8.
        - edit (e): Edit mode flag
    """
@overload #Overload for threePointArcCtx in ['edit']
def threePointArcCtx(d: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., s: int = ..., e: bool = ...) -> str:
    """threePointArcCtx is undoable, queryable, and editable.
    
    The threePointArcCtx command creates a new context for creating 3 point arcs

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 1:
        cmds.threePointArcCtx( "arcContext", degree=1 )
        cmds.setToolTo("arcContext")
        # To query the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", e=True, degree=3 )
    ```

    ---
    - Args:
        - degree (d): VAlid values are 1 or 3. Default degree 3.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - spans (s): Default is 8.
        - edit (e): Edit mode flag
    """
@overload #Overload for threePointArcCtx in ['edit']
def threePointArcCtx(degree: int = ..., d: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., spans: int = ..., s: int = ..., edit: bool = ..., e: bool = ...) -> str:
    """threePointArcCtx is undoable, queryable, and editable.
    
    The threePointArcCtx command creates a new context for creating 3 point arcs

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 1:
        cmds.threePointArcCtx( "arcContext", degree=1 )
        cmds.setToolTo("arcContext")
        # To query the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.threePointArcCtx( "arcContext", e=True, degree=3 )
    ```

    ---
    - Args:
        - degree (d): VAlid values are 1 or 3. Default degree 3.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - spans (s): Default is 8.
        - edit (e): Edit mode flag
    """
