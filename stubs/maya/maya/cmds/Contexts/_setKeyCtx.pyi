"""Stub files for Contexts category in Maya commands, command: setKeyCtx."""

from typing import Any, overload

@overload #Overload for setKeyCtx in ['create']
def setKeyCtx(contextName: contextName, breakdown: bool = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., preserveTangent: bool = ...) -> bool:
    """setKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to set keys within the graph
    editor

    ---
    - Args:
        - contextName: Input item(s).
        - breakdown (bd): Specifies whether or not to create breakdown keys
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - preserveTangent (pt): Specifies whether or not to preserve tangent
    """
@overload #Overload for setKeyCtx in ['create']
def setKeyCtx(contextName: contextName, bd: bool = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., pt: bool = ...) -> bool:
    """setKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to set keys within the graph
    editor

    ---
    - Args:
        - contextName: Input item(s).
        - breakdown (bd): Specifies whether or not to create breakdown keys
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - preserveTangent (pt): Specifies whether or not to preserve tangent
    """
@overload #Overload for setKeyCtx in ['create']
def setKeyCtx(contextName: contextName, breakdown: bool = ..., bd: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., preserveTangent: bool = ..., pt: bool = ...) -> bool:
    """setKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to set keys within the graph
    editor

    ---
    - Args:
        - contextName: Input item(s).
        - breakdown (bd): Specifies whether or not to create breakdown keys
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - preserveTangent (pt): Specifies whether or not to preserve tangent
    """
@overload #Overload for setKeyCtx in ['query']
def setKeyCtx(contextName: contextName, breakdown: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., preserveTangent: bool = ..., query: bool = ...) -> bool:
    """setKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to set keys within the graph
    editor

    ---
    - Args:
        - contextName: Input item(s).
        - breakdown (bd): Specifies whether or not to create breakdown keys
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - preserveTangent (pt): Specifies whether or not to preserve tangent
        - query (q): Query mode flag
    """
@overload #Overload for setKeyCtx in ['query']
def setKeyCtx(contextName: contextName, bd: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., pt: bool = ..., q: bool = ...) -> bool:
    """setKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to set keys within the graph
    editor

    ---
    - Args:
        - contextName: Input item(s).
        - breakdown (bd): Specifies whether or not to create breakdown keys
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - preserveTangent (pt): Specifies whether or not to preserve tangent
        - query (q): Query mode flag
    """
@overload #Overload for setKeyCtx in ['query']
def setKeyCtx(contextName: contextName, breakdown: bool = ..., bd: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., preserveTangent: bool = ..., pt: bool = ..., query: bool = ..., q: bool = ...) -> bool:
    """setKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to set keys within the graph
    editor

    ---
    - Args:
        - contextName: Input item(s).
        - breakdown (bd): Specifies whether or not to create breakdown keys
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - preserveTangent (pt): Specifies whether or not to preserve tangent
        - query (q): Query mode flag
    """
@overload #Overload for setKeyCtx in ['edit']
def setKeyCtx(contextName: contextName, breakdown: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., preserveTangent: bool = ..., edit: bool = ...) -> bool:
    """setKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to set keys within the graph
    editor

    ---
    - Args:
        - contextName: Input item(s).
        - breakdown (bd): Specifies whether or not to create breakdown keys
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - preserveTangent (pt): Specifies whether or not to preserve tangent
        - edit (e): Edit mode flag
    """
@overload #Overload for setKeyCtx in ['edit']
def setKeyCtx(contextName: contextName, bd: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., pt: bool = ..., e: bool = ...) -> bool:
    """setKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to set keys within the graph
    editor

    ---
    - Args:
        - contextName: Input item(s).
        - breakdown (bd): Specifies whether or not to create breakdown keys
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - preserveTangent (pt): Specifies whether or not to preserve tangent
        - edit (e): Edit mode flag
    """
@overload #Overload for setKeyCtx in ['edit']
def setKeyCtx(contextName: contextName, breakdown: bool = ..., bd: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., preserveTangent: bool = ..., pt: bool = ..., edit: bool = ..., e: bool = ...) -> bool:
    """setKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to set keys within the graph
    editor

    ---
    - Args:
        - contextName: Input item(s).
        - breakdown (bd): Specifies whether or not to create breakdown keys
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - preserveTangent (pt): Specifies whether or not to preserve tangent
        - edit (e): Edit mode flag
    """
