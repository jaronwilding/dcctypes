"""Stub files for Contexts category in Maya commands, command: curveSketchCtx."""

from typing import Any, overload

@overload #Overload for curveSketchCtx in ['create']
def curveSketchCtx([object]: [object], degree: int = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ...) -> str:
    """curveSketchCtx is undoable, queryable, and editable.
    
    The curveSketchCtx command creates a new curve sketch context, also known as
    the "pencil context".

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new sketch context, which creates degree 3 curves:
        cmds.curveSketchCtx( "pencilContext", degree=3 )
        cmds.setToolTo("pencilContext")
        # To query the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext",q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext", e=True, degree=1 )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - degree (d): Valid values are 1 or 3
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for curveSketchCtx in ['create']
def curveSketchCtx([object]: [object], d: int = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ...) -> str:
    """curveSketchCtx is undoable, queryable, and editable.
    
    The curveSketchCtx command creates a new curve sketch context, also known as
    the "pencil context".

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new sketch context, which creates degree 3 curves:
        cmds.curveSketchCtx( "pencilContext", degree=3 )
        cmds.setToolTo("pencilContext")
        # To query the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext",q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext", e=True, degree=1 )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - degree (d): Valid values are 1 or 3
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for curveSketchCtx in ['create']
def curveSketchCtx([object]: [object], degree: int = ..., d: int = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ...) -> str:
    """curveSketchCtx is undoable, queryable, and editable.
    
    The curveSketchCtx command creates a new curve sketch context, also known as
    the "pencil context".

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new sketch context, which creates degree 3 curves:
        cmds.curveSketchCtx( "pencilContext", degree=3 )
        cmds.setToolTo("pencilContext")
        # To query the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext",q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext", e=True, degree=1 )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - degree (d): Valid values are 1 or 3
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for curveSketchCtx in ['query']
def curveSketchCtx([object]: [object], degree: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> str:
    """curveSketchCtx is undoable, queryable, and editable.
    
    The curveSketchCtx command creates a new curve sketch context, also known as
    the "pencil context".

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new sketch context, which creates degree 3 curves:
        cmds.curveSketchCtx( "pencilContext", degree=3 )
        cmds.setToolTo("pencilContext")
        # To query the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext",q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext", e=True, degree=1 )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - degree (d): Valid values are 1 or 3
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for curveSketchCtx in ['query']
def curveSketchCtx([object]: [object], d: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> str:
    """curveSketchCtx is undoable, queryable, and editable.
    
    The curveSketchCtx command creates a new curve sketch context, also known as
    the "pencil context".

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new sketch context, which creates degree 3 curves:
        cmds.curveSketchCtx( "pencilContext", degree=3 )
        cmds.setToolTo("pencilContext")
        # To query the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext",q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext", e=True, degree=1 )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - degree (d): Valid values are 1 or 3
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for curveSketchCtx in ['query']
def curveSketchCtx([object]: [object], degree: int = ..., d: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> str:
    """curveSketchCtx is undoable, queryable, and editable.
    
    The curveSketchCtx command creates a new curve sketch context, also known as
    the "pencil context".

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new sketch context, which creates degree 3 curves:
        cmds.curveSketchCtx( "pencilContext", degree=3 )
        cmds.setToolTo("pencilContext")
        # To query the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext",q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext", e=True, degree=1 )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - degree (d): Valid values are 1 or 3
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for curveSketchCtx in ['edit']
def curveSketchCtx([object]: [object], degree: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> str:
    """curveSketchCtx is undoable, queryable, and editable.
    
    The curveSketchCtx command creates a new curve sketch context, also known as
    the "pencil context".

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new sketch context, which creates degree 3 curves:
        cmds.curveSketchCtx( "pencilContext", degree=3 )
        cmds.setToolTo("pencilContext")
        # To query the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext",q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext", e=True, degree=1 )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - degree (d): Valid values are 1 or 3
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for curveSketchCtx in ['edit']
def curveSketchCtx([object]: [object], d: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> str:
    """curveSketchCtx is undoable, queryable, and editable.
    
    The curveSketchCtx command creates a new curve sketch context, also known as
    the "pencil context".

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new sketch context, which creates degree 3 curves:
        cmds.curveSketchCtx( "pencilContext", degree=3 )
        cmds.setToolTo("pencilContext")
        # To query the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext",q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext", e=True, degree=1 )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - degree (d): Valid values are 1 or 3
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for curveSketchCtx in ['edit']
def curveSketchCtx([object]: [object], degree: int = ..., d: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """curveSketchCtx is undoable, queryable, and editable.
    
    The curveSketchCtx command creates a new curve sketch context, also known as
    the "pencil context".

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new sketch context, which creates degree 3 curves:
        cmds.curveSketchCtx( "pencilContext", degree=3 )
        cmds.setToolTo("pencilContext")
        # To query the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext",q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveSketchCtx( "pencilContext", e=True, degree=1 )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - degree (d): Valid values are 1 or 3
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
