"""Stub files for Contexts category in Maya commands, command: currentTimeCtx."""

from typing import Any, overload

@overload #Overload for currentTimeCtx in ['create']
def currentTimeCtx(contextName: contextName, exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ...) -> str:
    """currentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for currentTimeCtx in ['create']
def currentTimeCtx(contextName: contextName, ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ...) -> str:
    """currentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for currentTimeCtx in ['create']
def currentTimeCtx(contextName: contextName, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ...) -> str:
    """currentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for currentTimeCtx in ['query']
def currentTimeCtx(contextName: contextName, image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> str:
    """currentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for currentTimeCtx in ['query']
def currentTimeCtx(contextName: contextName, i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> str:
    """currentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for currentTimeCtx in ['query']
def currentTimeCtx(contextName: contextName, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> str:
    """currentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for currentTimeCtx in ['edit']
def currentTimeCtx(contextName: contextName, image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> str:
    """currentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for currentTimeCtx in ['edit']
def currentTimeCtx(contextName: contextName, i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> str:
    """currentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for currentTimeCtx in ['edit']
def currentTimeCtx(contextName: contextName, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """currentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
