"""Stub files for Contexts category in Maya commands, command: curveEPCtx."""

from typing import Any, overload

@overload #Overload for curveEPCtx in ['create']
def curveEPCtx(bezier: bool = ..., degree: int = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., preserveShape: bool = ..., preserveShapeFraction: float = ..., refit: bool = ..., uniform: bool = ...) -> str:
    """curveEPCtx is undoable, queryable, and editable.
    
    The curveEPCtx command creates a new context for creating curves by placing
    edit points.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 5:
        cmds.curveEPCtx( degree=5 )
        # To query the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', e=True, degree=7 )
    ```

    ---
    - Args:
        - bezier (bez): Use bezier curves
        - degree (d): Curve degree
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - preserveShapeFraction (pf): Fraction value used when preserving the shape
        - refit (rf): Set this flag to refit the curve
        - uniform (un): Should the curve use uniform parameterization?
    """
@overload #Overload for curveEPCtx in ['create']
def curveEPCtx(bez: bool = ..., d: int = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., ps: bool = ..., pf: float = ..., rf: bool = ..., un: bool = ...) -> str:
    """curveEPCtx is undoable, queryable, and editable.
    
    The curveEPCtx command creates a new context for creating curves by placing
    edit points.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 5:
        cmds.curveEPCtx( degree=5 )
        # To query the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', e=True, degree=7 )
    ```

    ---
    - Args:
        - bezier (bez): Use bezier curves
        - degree (d): Curve degree
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - preserveShapeFraction (pf): Fraction value used when preserving the shape
        - refit (rf): Set this flag to refit the curve
        - uniform (un): Should the curve use uniform parameterization?
    """
@overload #Overload for curveEPCtx in ['create']
def curveEPCtx(bezier: bool = ..., bez: bool = ..., degree: int = ..., d: int = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., preserveShape: bool = ..., ps: bool = ..., preserveShapeFraction: float = ..., pf: float = ..., refit: bool = ..., rf: bool = ..., uniform: bool = ..., un: bool = ...) -> str:
    """curveEPCtx is undoable, queryable, and editable.
    
    The curveEPCtx command creates a new context for creating curves by placing
    edit points.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 5:
        cmds.curveEPCtx( degree=5 )
        # To query the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', e=True, degree=7 )
    ```

    ---
    - Args:
        - bezier (bez): Use bezier curves
        - degree (d): Curve degree
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - preserveShapeFraction (pf): Fraction value used when preserving the shape
        - refit (rf): Set this flag to refit the curve
        - uniform (un): Should the curve use uniform parameterization?
    """
@overload #Overload for curveEPCtx in ['query']
def curveEPCtx(bezier: bool = ..., degree: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., preserveShape: bool = ..., preserveShapeFraction: float = ..., refit: bool = ..., uniform: bool = ..., query: bool = ...) -> str:
    """curveEPCtx is undoable, queryable, and editable.
    
    The curveEPCtx command creates a new context for creating curves by placing
    edit points.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 5:
        cmds.curveEPCtx( degree=5 )
        # To query the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', e=True, degree=7 )
    ```

    ---
    - Args:
        - bezier (bez): Use bezier curves
        - degree (d): Curve degree
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - preserveShapeFraction (pf): Fraction value used when preserving the shape
        - refit (rf): Set this flag to refit the curve
        - uniform (un): Should the curve use uniform parameterization?
        - query (q): Query mode flag
    """
@overload #Overload for curveEPCtx in ['query']
def curveEPCtx(bez: bool = ..., d: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., ps: bool = ..., pf: float = ..., rf: bool = ..., un: bool = ..., q: bool = ...) -> str:
    """curveEPCtx is undoable, queryable, and editable.
    
    The curveEPCtx command creates a new context for creating curves by placing
    edit points.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 5:
        cmds.curveEPCtx( degree=5 )
        # To query the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', e=True, degree=7 )
    ```

    ---
    - Args:
        - bezier (bez): Use bezier curves
        - degree (d): Curve degree
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - preserveShapeFraction (pf): Fraction value used when preserving the shape
        - refit (rf): Set this flag to refit the curve
        - uniform (un): Should the curve use uniform parameterization?
        - query (q): Query mode flag
    """
@overload #Overload for curveEPCtx in ['query']
def curveEPCtx(bezier: bool = ..., bez: bool = ..., degree: int = ..., d: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., preserveShape: bool = ..., ps: bool = ..., preserveShapeFraction: float = ..., pf: float = ..., refit: bool = ..., rf: bool = ..., uniform: bool = ..., un: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """curveEPCtx is undoable, queryable, and editable.
    
    The curveEPCtx command creates a new context for creating curves by placing
    edit points.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 5:
        cmds.curveEPCtx( degree=5 )
        # To query the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', e=True, degree=7 )
    ```

    ---
    - Args:
        - bezier (bez): Use bezier curves
        - degree (d): Curve degree
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - preserveShapeFraction (pf): Fraction value used when preserving the shape
        - refit (rf): Set this flag to refit the curve
        - uniform (un): Should the curve use uniform parameterization?
        - query (q): Query mode flag
    """
@overload #Overload for curveEPCtx in ['edit']
def curveEPCtx(bezier: bool = ..., degree: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., preserveShape: bool = ..., preserveShapeFraction: float = ..., refit: bool = ..., uniform: bool = ..., edit: bool = ...) -> str:
    """curveEPCtx is undoable, queryable, and editable.
    
    The curveEPCtx command creates a new context for creating curves by placing
    edit points.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 5:
        cmds.curveEPCtx( degree=5 )
        # To query the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', e=True, degree=7 )
    ```

    ---
    - Args:
        - bezier (bez): Use bezier curves
        - degree (d): Curve degree
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - preserveShapeFraction (pf): Fraction value used when preserving the shape
        - refit (rf): Set this flag to refit the curve
        - uniform (un): Should the curve use uniform parameterization?
        - edit (e): Edit mode flag
    """
@overload #Overload for curveEPCtx in ['edit']
def curveEPCtx(bez: bool = ..., d: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., ps: bool = ..., pf: float = ..., rf: bool = ..., un: bool = ..., e: bool = ...) -> str:
    """curveEPCtx is undoable, queryable, and editable.
    
    The curveEPCtx command creates a new context for creating curves by placing
    edit points.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 5:
        cmds.curveEPCtx( degree=5 )
        # To query the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', e=True, degree=7 )
    ```

    ---
    - Args:
        - bezier (bez): Use bezier curves
        - degree (d): Curve degree
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - preserveShapeFraction (pf): Fraction value used when preserving the shape
        - refit (rf): Set this flag to refit the curve
        - uniform (un): Should the curve use uniform parameterization?
        - edit (e): Edit mode flag
    """
@overload #Overload for curveEPCtx in ['edit']
def curveEPCtx(bezier: bool = ..., bez: bool = ..., degree: int = ..., d: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., preserveShape: bool = ..., ps: bool = ..., preserveShapeFraction: float = ..., pf: float = ..., refit: bool = ..., rf: bool = ..., uniform: bool = ..., un: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """curveEPCtx is undoable, queryable, and editable.
    
    The curveEPCtx command creates a new context for creating curves by placing
    edit points.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new context that will create curves of degree 5:
        cmds.curveEPCtx( degree=5 )
        # To query the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', q=True, degree=True )
        # To edit the degree of an existing context:
        cmds.curveEPCtx( 'curveEPCtx1', e=True, degree=7 )
    ```

    ---
    - Args:
        - bezier (bez): Use bezier curves
        - degree (d): Curve degree
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - preserveShapeFraction (pf): Fraction value used when preserving the shape
        - refit (rf): Set this flag to refit the curve
        - uniform (un): Should the curve use uniform parameterization?
        - edit (e): Edit mode flag
    """
