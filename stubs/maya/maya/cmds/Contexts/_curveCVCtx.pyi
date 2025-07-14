"""Stub files for Contexts category in Maya commands, command: curveCVCtx."""

from typing import Any, overload

@overload #Overload for curveCVCtx in ['create']
def curveCVCtx(bezier: bool = ..., degree: int = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., multEndKnots: bool = ..., name: str = ..., preserveShape: bool = ..., rational: bool = ..., refit: bool = ..., symmetry: bool = ..., uniform: bool = ...) -> str:
    """curveCVCtx is undoable, queryable, and editable.
    
    The curveCVCtx command creates a new context for creating curves by placing
    control vertices (CVs).

    ---
    - Args:
        - degree (d): Curve degree
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - multEndKnots (me): Specify if multiple end knots are to be created.
        - name (n): If this is a tool command, name the tool appropriately.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - rational (rl): Should the curve be rational?
        - refit (rf): Set this flag to refit the curve
        - symmetry (sm): Specify if symmetry is to be used
        - uniform (un): Should the curve use uniform parameterization?
    """
@overload #Overload for curveCVCtx in ['create']
def curveCVCtx(bez: bool = ..., d: int = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., me: bool = ..., n: str = ..., ps: bool = ..., rl: bool = ..., rf: bool = ..., sm: bool = ..., un: bool = ...) -> str:
    """curveCVCtx is undoable, queryable, and editable.
    
    The curveCVCtx command creates a new context for creating curves by placing
    control vertices (CVs).

    ---
    - Args:
        - degree (d): Curve degree
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - multEndKnots (me): Specify if multiple end knots are to be created.
        - name (n): If this is a tool command, name the tool appropriately.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - rational (rl): Should the curve be rational?
        - refit (rf): Set this flag to refit the curve
        - symmetry (sm): Specify if symmetry is to be used
        - uniform (un): Should the curve use uniform parameterization?
    """
@overload #Overload for curveCVCtx in ['create']
def curveCVCtx(bezier: bool = ..., bez: bool = ..., degree: int = ..., d: int = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., multEndKnots: bool = ..., me: bool = ..., name: str = ..., n: str = ..., preserveShape: bool = ..., ps: bool = ..., rational: bool = ..., rl: bool = ..., refit: bool = ..., rf: bool = ..., symmetry: bool = ..., sm: bool = ..., uniform: bool = ..., un: bool = ...) -> str:
    """curveCVCtx is undoable, queryable, and editable.
    
    The curveCVCtx command creates a new context for creating curves by placing
    control vertices (CVs).

    ---
    - Args:
        - degree (d): Curve degree
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - multEndKnots (me): Specify if multiple end knots are to be created.
        - name (n): If this is a tool command, name the tool appropriately.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - rational (rl): Should the curve be rational?
        - refit (rf): Set this flag to refit the curve
        - symmetry (sm): Specify if symmetry is to be used
        - uniform (un): Should the curve use uniform parameterization?
    """
@overload #Overload for curveCVCtx in ['query']
def curveCVCtx(bezier: bool = ..., degree: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., multEndKnots: bool = ..., preserveShape: bool = ..., rational: bool = ..., refit: bool = ..., symmetry: bool = ..., uniform: bool = ..., query: bool = ...) -> str:
    """curveCVCtx is undoable, queryable, and editable.
    
    The curveCVCtx command creates a new context for creating curves by placing
    control vertices (CVs).

    ---
    - Args:
        - degree (d): Curve degree
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - multEndKnots (me): Specify if multiple end knots are to be created.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - rational (rl): Should the curve be rational?
        - refit (rf): Set this flag to refit the curve
        - symmetry (sm): Specify if symmetry is to be used
        - uniform (un): Should the curve use uniform parameterization?
        - query (q): Query mode flag
    """
@overload #Overload for curveCVCtx in ['query']
def curveCVCtx(bez: bool = ..., d: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., me: bool = ..., ps: bool = ..., rl: bool = ..., rf: bool = ..., sm: bool = ..., un: bool = ..., q: bool = ...) -> str:
    """curveCVCtx is undoable, queryable, and editable.
    
    The curveCVCtx command creates a new context for creating curves by placing
    control vertices (CVs).

    ---
    - Args:
        - degree (d): Curve degree
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - multEndKnots (me): Specify if multiple end knots are to be created.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - rational (rl): Should the curve be rational?
        - refit (rf): Set this flag to refit the curve
        - symmetry (sm): Specify if symmetry is to be used
        - uniform (un): Should the curve use uniform parameterization?
        - query (q): Query mode flag
    """
@overload #Overload for curveCVCtx in ['query']
def curveCVCtx(bezier: bool = ..., bez: bool = ..., degree: int = ..., d: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., multEndKnots: bool = ..., me: bool = ..., preserveShape: bool = ..., ps: bool = ..., rational: bool = ..., rl: bool = ..., refit: bool = ..., rf: bool = ..., symmetry: bool = ..., sm: bool = ..., uniform: bool = ..., un: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """curveCVCtx is undoable, queryable, and editable.
    
    The curveCVCtx command creates a new context for creating curves by placing
    control vertices (CVs).

    ---
    - Args:
        - degree (d): Curve degree
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - multEndKnots (me): Specify if multiple end knots are to be created.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - rational (rl): Should the curve be rational?
        - refit (rf): Set this flag to refit the curve
        - symmetry (sm): Specify if symmetry is to be used
        - uniform (un): Should the curve use uniform parameterization?
        - query (q): Query mode flag
    """
@overload #Overload for curveCVCtx in ['edit']
def curveCVCtx(bezier: bool = ..., degree: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., multEndKnots: bool = ..., preserveShape: bool = ..., rational: bool = ..., refit: bool = ..., symmetry: bool = ..., uniform: bool = ..., edit: bool = ...) -> str:
    """curveCVCtx is undoable, queryable, and editable.
    
    The curveCVCtx command creates a new context for creating curves by placing
    control vertices (CVs).

    ---
    - Args:
        - degree (d): Curve degree
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - multEndKnots (me): Specify if multiple end knots are to be created.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - rational (rl): Should the curve be rational?
        - refit (rf): Set this flag to refit the curve
        - symmetry (sm): Specify if symmetry is to be used
        - uniform (un): Should the curve use uniform parameterization?
        - edit (e): Edit mode flag
    """
@overload #Overload for curveCVCtx in ['edit']
def curveCVCtx(bez: bool = ..., d: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., me: bool = ..., ps: bool = ..., rl: bool = ..., rf: bool = ..., sm: bool = ..., un: bool = ..., e: bool = ...) -> str:
    """curveCVCtx is undoable, queryable, and editable.
    
    The curveCVCtx command creates a new context for creating curves by placing
    control vertices (CVs).

    ---
    - Args:
        - degree (d): Curve degree
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - multEndKnots (me): Specify if multiple end knots are to be created.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - rational (rl): Should the curve be rational?
        - refit (rf): Set this flag to refit the curve
        - symmetry (sm): Specify if symmetry is to be used
        - uniform (un): Should the curve use uniform parameterization?
        - edit (e): Edit mode flag
    """
@overload #Overload for curveCVCtx in ['edit']
def curveCVCtx(bezier: bool = ..., bez: bool = ..., degree: int = ..., d: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., multEndKnots: bool = ..., me: bool = ..., preserveShape: bool = ..., ps: bool = ..., rational: bool = ..., rl: bool = ..., refit: bool = ..., rf: bool = ..., symmetry: bool = ..., sm: bool = ..., uniform: bool = ..., un: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """curveCVCtx is undoable, queryable, and editable.
    
    The curveCVCtx command creates a new context for creating curves by placing
    control vertices (CVs).

    ---
    - Args:
        - degree (d): Curve degree
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - multEndKnots (me): Specify if multiple end knots are to be created.
        - preserveShape (ps): Set this flag to make the operation preserve the shape
        - rational (rl): Should the curve be rational?
        - refit (rf): Set this flag to refit the curve
        - symmetry (sm): Specify if symmetry is to be used
        - uniform (un): Should the curve use uniform parameterization?
        - edit (e): Edit mode flag
    """
