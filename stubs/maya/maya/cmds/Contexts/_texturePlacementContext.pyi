"""Stub files for Contexts category in Maya commands, command: texturePlacementContext."""

from typing import Any, overload

@overload #Overload for texturePlacementContext in ['create']
def texturePlacementContext(exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., labelMapping: bool = ..., name: str = ...) -> str:
    """texturePlacementContext is undoable, queryable, and editable.
    
    Create a command for creating new texture placement contexts. By default label
    mapping is on when the context is created.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - labelMapping (lm): Set the context to label mapping.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for texturePlacementContext in ['create']
def texturePlacementContext(ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., lm: bool = ..., n: str = ...) -> str:
    """texturePlacementContext is undoable, queryable, and editable.
    
    Create a command for creating new texture placement contexts. By default label
    mapping is on when the context is created.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - labelMapping (lm): Set the context to label mapping.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for texturePlacementContext in ['create']
def texturePlacementContext(exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., labelMapping: bool = ..., lm: bool = ..., name: str = ..., n: str = ...) -> str:
    """texturePlacementContext is undoable, queryable, and editable.
    
    Create a command for creating new texture placement contexts. By default label
    mapping is on when the context is created.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - labelMapping (lm): Set the context to label mapping.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for texturePlacementContext in ['query']
def texturePlacementContext(image1: str = ..., image2: str = ..., image3: str = ..., labelMapping: bool = ..., query: bool = ...) -> str:
    """texturePlacementContext is undoable, queryable, and editable.
    
    Create a command for creating new texture placement contexts. By default label
    mapping is on when the context is created.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - labelMapping (lm): Set the context to label mapping.
        - query (q): Query mode flag
    """
@overload #Overload for texturePlacementContext in ['query']
def texturePlacementContext(i1: str = ..., i2: str = ..., i3: str = ..., lm: bool = ..., q: bool = ...) -> str:
    """texturePlacementContext is undoable, queryable, and editable.
    
    Create a command for creating new texture placement contexts. By default label
    mapping is on when the context is created.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - labelMapping (lm): Set the context to label mapping.
        - query (q): Query mode flag
    """
@overload #Overload for texturePlacementContext in ['query']
def texturePlacementContext(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., labelMapping: bool = ..., lm: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """texturePlacementContext is undoable, queryable, and editable.
    
    Create a command for creating new texture placement contexts. By default label
    mapping is on when the context is created.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - labelMapping (lm): Set the context to label mapping.
        - query (q): Query mode flag
    """
@overload #Overload for texturePlacementContext in ['edit']
def texturePlacementContext(image1: str = ..., image2: str = ..., image3: str = ..., labelMapping: bool = ..., edit: bool = ...) -> str:
    """texturePlacementContext is undoable, queryable, and editable.
    
    Create a command for creating new texture placement contexts. By default label
    mapping is on when the context is created.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - labelMapping (lm): Set the context to label mapping.
        - edit (e): Edit mode flag
    """
@overload #Overload for texturePlacementContext in ['edit']
def texturePlacementContext(i1: str = ..., i2: str = ..., i3: str = ..., lm: bool = ..., e: bool = ...) -> str:
    """texturePlacementContext is undoable, queryable, and editable.
    
    Create a command for creating new texture placement contexts. By default label
    mapping is on when the context is created.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - labelMapping (lm): Set the context to label mapping.
        - edit (e): Edit mode flag
    """
@overload #Overload for texturePlacementContext in ['edit']
def texturePlacementContext(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., labelMapping: bool = ..., lm: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """texturePlacementContext is undoable, queryable, and editable.
    
    Create a command for creating new texture placement contexts. By default label
    mapping is on when the context is created.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - labelMapping (lm): Set the context to label mapping.
        - edit (e): Edit mode flag
    """
