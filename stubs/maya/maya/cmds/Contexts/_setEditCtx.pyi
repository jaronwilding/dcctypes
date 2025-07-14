"""Stub files for Contexts category in Maya commands, command: setEditCtx."""

from typing import Any, overload

@overload #Overload for setEditCtx in ['create']
def setEditCtx(name: name, exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ...) -> str:
    """setEditCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to modify set membership.

    ---
    - Args:
        - name: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for setEditCtx in ['create']
def setEditCtx(name: name, ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ...) -> str:
    """setEditCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to modify set membership.

    ---
    - Args:
        - name: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for setEditCtx in ['create']
def setEditCtx(name: name, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ...) -> str:
    """setEditCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to modify set membership.

    ---
    - Args:
        - name: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for setEditCtx in ['query']
def setEditCtx(name: name, image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> str:
    """setEditCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to modify set membership.

    ---
    - Args:
        - name: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for setEditCtx in ['query']
def setEditCtx(name: name, i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> str:
    """setEditCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to modify set membership.

    ---
    - Args:
        - name: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for setEditCtx in ['query']
def setEditCtx(name: name, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> str:
    """setEditCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to modify set membership.

    ---
    - Args:
        - name: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for setEditCtx in ['edit']
def setEditCtx(name: name, image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> str:
    """setEditCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to modify set membership.

    ---
    - Args:
        - name: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for setEditCtx in ['edit']
def setEditCtx(name: name, i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> str:
    """setEditCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to modify set membership.

    ---
    - Args:
        - name: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for setEditCtx in ['edit']
def setEditCtx(name: name, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """setEditCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to modify set membership.

    ---
    - Args:
        - name: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
