"""Stub files for Contexts category in Maya commands, command: modelCurrentTimeCtx."""

from typing import Any, overload

@overload #Overload for modelCurrentTimeCtx in ['create']
def modelCurrentTimeCtx(contextName: contextName, exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., percent: float = ...) -> str:
    """modelCurrentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the model views.

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - percent (per): Percent of the screen space that represents the full time slider range (default is 50%)
    """
@overload #Overload for modelCurrentTimeCtx in ['create']
def modelCurrentTimeCtx(contextName: contextName, ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., per: float = ...) -> str:
    """modelCurrentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the model views.

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - percent (per): Percent of the screen space that represents the full time slider range (default is 50%)
    """
@overload #Overload for modelCurrentTimeCtx in ['create']
def modelCurrentTimeCtx(contextName: contextName, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., percent: float = ..., per: float = ...) -> str:
    """modelCurrentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the model views.

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - percent (per): Percent of the screen space that represents the full time slider range (default is 50%)
    """
@overload #Overload for modelCurrentTimeCtx in ['query']
def modelCurrentTimeCtx(contextName: contextName, image1: str = ..., image2: str = ..., image3: str = ..., percent: float = ..., query: bool = ...) -> str:
    """modelCurrentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the model views.

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - percent (per): Percent of the screen space that represents the full time slider range (default is 50%)
        - query (q): Query mode flag
    """
@overload #Overload for modelCurrentTimeCtx in ['query']
def modelCurrentTimeCtx(contextName: contextName, i1: str = ..., i2: str = ..., i3: str = ..., per: float = ..., q: bool = ...) -> str:
    """modelCurrentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the model views.

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - percent (per): Percent of the screen space that represents the full time slider range (default is 50%)
        - query (q): Query mode flag
    """
@overload #Overload for modelCurrentTimeCtx in ['query']
def modelCurrentTimeCtx(contextName: contextName, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., percent: float = ..., per: float = ..., query: bool = ..., q: bool = ...) -> str:
    """modelCurrentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the model views.

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - percent (per): Percent of the screen space that represents the full time slider range (default is 50%)
        - query (q): Query mode flag
    """
@overload #Overload for modelCurrentTimeCtx in ['edit']
def modelCurrentTimeCtx(contextName: contextName, image1: str = ..., image2: str = ..., image3: str = ..., percent: float = ..., edit: bool = ...) -> str:
    """modelCurrentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the model views.

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - percent (per): Percent of the screen space that represents the full time slider range (default is 50%)
        - edit (e): Edit mode flag
    """
@overload #Overload for modelCurrentTimeCtx in ['edit']
def modelCurrentTimeCtx(contextName: contextName, i1: str = ..., i2: str = ..., i3: str = ..., per: float = ..., e: bool = ...) -> str:
    """modelCurrentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the model views.

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - percent (per): Percent of the screen space that represents the full time slider range (default is 50%)
        - edit (e): Edit mode flag
    """
@overload #Overload for modelCurrentTimeCtx in ['edit']
def modelCurrentTimeCtx(contextName: contextName, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., percent: float = ..., per: float = ..., edit: bool = ..., e: bool = ...) -> str:
    """modelCurrentTimeCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to change current time within
    the model views.

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - percent (per): Percent of the screen space that represents the full time slider range (default is 50%)
        - edit (e): Edit mode flag
    """
