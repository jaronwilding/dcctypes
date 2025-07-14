"""Stub files for Contexts category in Maya commands, command: curveAddPtCtx."""

from typing import Any, overload

@overload #Overload for curveAddPtCtx in ['create']
def curveAddPtCtx(exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ...) -> str:
    """curveAddPtCtx is undoable, queryable, and editable.
    
    The curveAddPtCtx command creates a new curve add points context, which adds
    either control vertices (CVs) or edit points to an existing curve.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for curveAddPtCtx in ['create']
def curveAddPtCtx(ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ...) -> str:
    """curveAddPtCtx is undoable, queryable, and editable.
    
    The curveAddPtCtx command creates a new curve add points context, which adds
    either control vertices (CVs) or edit points to an existing curve.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for curveAddPtCtx in ['create']
def curveAddPtCtx(exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ...) -> str:
    """curveAddPtCtx is undoable, queryable, and editable.
    
    The curveAddPtCtx command creates a new curve add points context, which adds
    either control vertices (CVs) or edit points to an existing curve.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for curveAddPtCtx in ['query']
def curveAddPtCtx(image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> str:
    """curveAddPtCtx is undoable, queryable, and editable.
    
    The curveAddPtCtx command creates a new curve add points context, which adds
    either control vertices (CVs) or edit points to an existing curve.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for curveAddPtCtx in ['query']
def curveAddPtCtx(i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> str:
    """curveAddPtCtx is undoable, queryable, and editable.
    
    The curveAddPtCtx command creates a new curve add points context, which adds
    either control vertices (CVs) or edit points to an existing curve.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for curveAddPtCtx in ['query']
def curveAddPtCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> str:
    """curveAddPtCtx is undoable, queryable, and editable.
    
    The curveAddPtCtx command creates a new curve add points context, which adds
    either control vertices (CVs) or edit points to an existing curve.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for curveAddPtCtx in ['edit']
def curveAddPtCtx(image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> str:
    """curveAddPtCtx is undoable, queryable, and editable.
    
    The curveAddPtCtx command creates a new curve add points context, which adds
    either control vertices (CVs) or edit points to an existing curve.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for curveAddPtCtx in ['edit']
def curveAddPtCtx(i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> str:
    """curveAddPtCtx is undoable, queryable, and editable.
    
    The curveAddPtCtx command creates a new curve add points context, which adds
    either control vertices (CVs) or edit points to an existing curve.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for curveAddPtCtx in ['edit']
def curveAddPtCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """curveAddPtCtx is undoable, queryable, and editable.
    
    The curveAddPtCtx command creates a new curve add points context, which adds
    either control vertices (CVs) or edit points to an existing curve.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
