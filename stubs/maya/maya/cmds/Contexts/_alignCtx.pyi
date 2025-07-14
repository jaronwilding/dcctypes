"""Stub files for Contexts category in Maya commands, command: alignCtx."""

from typing import Any, overload

@overload #Overload for alignCtx in ['create']
def alignCtx([contextName]: [contextName], align: bool = ..., anchorFirstObject: bool = ..., distribute: bool = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., showAlignTouch: bool = ...) -> str:
    """alignCtx is undoable, queryable, and editable.
    
    The alignCtx command creates a tool for aligning and distributing objects.

    ---
    - Args:
        - [contextName]: Input item(s).
        - align (a): Align objects
        - anchorFirstObject (afo): Anchor first or last selected object. Default false. Only applicable when aligning objects.
        - distribute (d): Distribute objects
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - showAlignTouch (sat): Show or hide align touching handles. Default true. Only applicable when aligning objects.
    """
@overload #Overload for alignCtx in ['create']
def alignCtx([contextName]: [contextName], a: bool = ..., afo: bool = ..., d: bool = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., sat: bool = ...) -> str:
    """alignCtx is undoable, queryable, and editable.
    
    The alignCtx command creates a tool for aligning and distributing objects.

    ---
    - Args:
        - [contextName]: Input item(s).
        - align (a): Align objects
        - anchorFirstObject (afo): Anchor first or last selected object. Default false. Only applicable when aligning objects.
        - distribute (d): Distribute objects
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - showAlignTouch (sat): Show or hide align touching handles. Default true. Only applicable when aligning objects.
    """
@overload #Overload for alignCtx in ['create']
def alignCtx([contextName]: [contextName], align: bool = ..., a: bool = ..., anchorFirstObject: bool = ..., afo: bool = ..., distribute: bool = ..., d: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., showAlignTouch: bool = ..., sat: bool = ...) -> str:
    """alignCtx is undoable, queryable, and editable.
    
    The alignCtx command creates a tool for aligning and distributing objects.

    ---
    - Args:
        - [contextName]: Input item(s).
        - align (a): Align objects
        - anchorFirstObject (afo): Anchor first or last selected object. Default false. Only applicable when aligning objects.
        - distribute (d): Distribute objects
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - showAlignTouch (sat): Show or hide align touching handles. Default true. Only applicable when aligning objects.
    """
@overload #Overload for alignCtx in ['query']
def alignCtx([contextName]: [contextName], align: bool = ..., anchorFirstObject: bool = ..., distribute: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., showAlignTouch: bool = ..., query: bool = ...) -> str:
    """alignCtx is undoable, queryable, and editable.
    
    The alignCtx command creates a tool for aligning and distributing objects.

    ---
    - Args:
        - [contextName]: Input item(s).
        - align (a): Align objects
        - anchorFirstObject (afo): Anchor first or last selected object. Default false. Only applicable when aligning objects.
        - distribute (d): Distribute objects
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - showAlignTouch (sat): Show or hide align touching handles. Default true. Only applicable when aligning objects.
        - query (q): Query mode flag
    """
@overload #Overload for alignCtx in ['query']
def alignCtx([contextName]: [contextName], a: bool = ..., afo: bool = ..., d: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., sat: bool = ..., q: bool = ...) -> str:
    """alignCtx is undoable, queryable, and editable.
    
    The alignCtx command creates a tool for aligning and distributing objects.

    ---
    - Args:
        - [contextName]: Input item(s).
        - align (a): Align objects
        - anchorFirstObject (afo): Anchor first or last selected object. Default false. Only applicable when aligning objects.
        - distribute (d): Distribute objects
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - showAlignTouch (sat): Show or hide align touching handles. Default true. Only applicable when aligning objects.
        - query (q): Query mode flag
    """
@overload #Overload for alignCtx in ['query']
def alignCtx([contextName]: [contextName], align: bool = ..., a: bool = ..., anchorFirstObject: bool = ..., afo: bool = ..., distribute: bool = ..., d: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., showAlignTouch: bool = ..., sat: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """alignCtx is undoable, queryable, and editable.
    
    The alignCtx command creates a tool for aligning and distributing objects.

    ---
    - Args:
        - [contextName]: Input item(s).
        - align (a): Align objects
        - anchorFirstObject (afo): Anchor first or last selected object. Default false. Only applicable when aligning objects.
        - distribute (d): Distribute objects
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - showAlignTouch (sat): Show or hide align touching handles. Default true. Only applicable when aligning objects.
        - query (q): Query mode flag
    """
@overload #Overload for alignCtx in ['edit']
def alignCtx([contextName]: [contextName], align: bool = ..., anchorFirstObject: bool = ..., distribute: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., showAlignTouch: bool = ..., edit: bool = ...) -> str:
    """alignCtx is undoable, queryable, and editable.
    
    The alignCtx command creates a tool for aligning and distributing objects.

    ---
    - Args:
        - [contextName]: Input item(s).
        - align (a): Align objects
        - anchorFirstObject (afo): Anchor first or last selected object. Default false. Only applicable when aligning objects.
        - distribute (d): Distribute objects
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - showAlignTouch (sat): Show or hide align touching handles. Default true. Only applicable when aligning objects.
        - edit (e): Edit mode flag
    """
@overload #Overload for alignCtx in ['edit']
def alignCtx([contextName]: [contextName], a: bool = ..., afo: bool = ..., d: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., sat: bool = ..., e: bool = ...) -> str:
    """alignCtx is undoable, queryable, and editable.
    
    The alignCtx command creates a tool for aligning and distributing objects.

    ---
    - Args:
        - [contextName]: Input item(s).
        - align (a): Align objects
        - anchorFirstObject (afo): Anchor first or last selected object. Default false. Only applicable when aligning objects.
        - distribute (d): Distribute objects
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - showAlignTouch (sat): Show or hide align touching handles. Default true. Only applicable when aligning objects.
        - edit (e): Edit mode flag
    """
@overload #Overload for alignCtx in ['edit']
def alignCtx([contextName]: [contextName], align: bool = ..., a: bool = ..., anchorFirstObject: bool = ..., afo: bool = ..., distribute: bool = ..., d: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., showAlignTouch: bool = ..., sat: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """alignCtx is undoable, queryable, and editable.
    
    The alignCtx command creates a tool for aligning and distributing objects.

    ---
    - Args:
        - [contextName]: Input item(s).
        - align (a): Align objects
        - anchorFirstObject (afo): Anchor first or last selected object. Default false. Only applicable when aligning objects.
        - distribute (d): Distribute objects
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - showAlignTouch (sat): Show or hide align touching handles. Default true. Only applicable when aligning objects.
        - edit (e): Edit mode flag
    """
