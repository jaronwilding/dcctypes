"""Stub files for Contexts category in Maya commands, command: shadingLightRelCtx."""

from typing import Any, overload

@overload #Overload for shadingLightRelCtx in ['create']
def shadingLightRelCtx(exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., offCommand: str = ..., onCommand: str = ..., shadingCentric: bool = ...) -> str:
    """shadingLightRelCtx is undoable, queryable, and editable.
    
    This command creates a context that can be used for associating lights to
    shading groups. You can put the context into shading-centric mode by using the
    -shadingCentric flag and specifying true. This means that the shading group is
    selected first then lights associated with the shading group are highlighted.
    Subsequent selections result in assignments.
    
    Specifying -shadingCentric false means that the light is to be selected first.
    The shading groups associated with the light will then be selected and
    subsequent selections will result in assignments being made.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - offCommand (ofc): command to be issued when context is turned on
        - onCommand (onc): command to be issued when context is turned on
        - shadingCentric (s): shading-centric mode.
    """
@overload #Overload for shadingLightRelCtx in ['create']
def shadingLightRelCtx(ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., ofc: str = ..., onc: str = ..., s: bool = ...) -> str:
    """shadingLightRelCtx is undoable, queryable, and editable.
    
    This command creates a context that can be used for associating lights to
    shading groups. You can put the context into shading-centric mode by using the
    -shadingCentric flag and specifying true. This means that the shading group is
    selected first then lights associated with the shading group are highlighted.
    Subsequent selections result in assignments.
    
    Specifying -shadingCentric false means that the light is to be selected first.
    The shading groups associated with the light will then be selected and
    subsequent selections will result in assignments being made.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - offCommand (ofc): command to be issued when context is turned on
        - onCommand (onc): command to be issued when context is turned on
        - shadingCentric (s): shading-centric mode.
    """
@overload #Overload for shadingLightRelCtx in ['create']
def shadingLightRelCtx(exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., offCommand: str = ..., ofc: str = ..., onCommand: str = ..., onc: str = ..., shadingCentric: bool = ..., s: bool = ...) -> str:
    """shadingLightRelCtx is undoable, queryable, and editable.
    
    This command creates a context that can be used for associating lights to
    shading groups. You can put the context into shading-centric mode by using the
    -shadingCentric flag and specifying true. This means that the shading group is
    selected first then lights associated with the shading group are highlighted.
    Subsequent selections result in assignments.
    
    Specifying -shadingCentric false means that the light is to be selected first.
    The shading groups associated with the light will then be selected and
    subsequent selections will result in assignments being made.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - offCommand (ofc): command to be issued when context is turned on
        - onCommand (onc): command to be issued when context is turned on
        - shadingCentric (s): shading-centric mode.
    """
@overload #Overload for shadingLightRelCtx in ['query']
def shadingLightRelCtx(image1: str = ..., image2: str = ..., image3: str = ..., offCommand: str = ..., onCommand: str = ..., shadingCentric: bool = ..., query: bool = ...) -> str:
    """shadingLightRelCtx is undoable, queryable, and editable.
    
    This command creates a context that can be used for associating lights to
    shading groups. You can put the context into shading-centric mode by using the
    -shadingCentric flag and specifying true. This means that the shading group is
    selected first then lights associated with the shading group are highlighted.
    Subsequent selections result in assignments.
    
    Specifying -shadingCentric false means that the light is to be selected first.
    The shading groups associated with the light will then be selected and
    subsequent selections will result in assignments being made.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - offCommand (ofc): command to be issued when context is turned on
        - onCommand (onc): command to be issued when context is turned on
        - shadingCentric (s): shading-centric mode.
        - query (q): Query mode flag
    """
@overload #Overload for shadingLightRelCtx in ['query']
def shadingLightRelCtx(i1: str = ..., i2: str = ..., i3: str = ..., ofc: str = ..., onc: str = ..., s: bool = ..., q: bool = ...) -> str:
    """shadingLightRelCtx is undoable, queryable, and editable.
    
    This command creates a context that can be used for associating lights to
    shading groups. You can put the context into shading-centric mode by using the
    -shadingCentric flag and specifying true. This means that the shading group is
    selected first then lights associated with the shading group are highlighted.
    Subsequent selections result in assignments.
    
    Specifying -shadingCentric false means that the light is to be selected first.
    The shading groups associated with the light will then be selected and
    subsequent selections will result in assignments being made.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - offCommand (ofc): command to be issued when context is turned on
        - onCommand (onc): command to be issued when context is turned on
        - shadingCentric (s): shading-centric mode.
        - query (q): Query mode flag
    """
@overload #Overload for shadingLightRelCtx in ['query']
def shadingLightRelCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., offCommand: str = ..., ofc: str = ..., onCommand: str = ..., onc: str = ..., shadingCentric: bool = ..., s: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """shadingLightRelCtx is undoable, queryable, and editable.
    
    This command creates a context that can be used for associating lights to
    shading groups. You can put the context into shading-centric mode by using the
    -shadingCentric flag and specifying true. This means that the shading group is
    selected first then lights associated with the shading group are highlighted.
    Subsequent selections result in assignments.
    
    Specifying -shadingCentric false means that the light is to be selected first.
    The shading groups associated with the light will then be selected and
    subsequent selections will result in assignments being made.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - offCommand (ofc): command to be issued when context is turned on
        - onCommand (onc): command to be issued when context is turned on
        - shadingCentric (s): shading-centric mode.
        - query (q): Query mode flag
    """
@overload #Overload for shadingLightRelCtx in ['edit']
def shadingLightRelCtx(image1: str = ..., image2: str = ..., image3: str = ..., offCommand: str = ..., onCommand: str = ..., shadingCentric: bool = ..., edit: bool = ...) -> str:
    """shadingLightRelCtx is undoable, queryable, and editable.
    
    This command creates a context that can be used for associating lights to
    shading groups. You can put the context into shading-centric mode by using the
    -shadingCentric flag and specifying true. This means that the shading group is
    selected first then lights associated with the shading group are highlighted.
    Subsequent selections result in assignments.
    
    Specifying -shadingCentric false means that the light is to be selected first.
    The shading groups associated with the light will then be selected and
    subsequent selections will result in assignments being made.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - offCommand (ofc): command to be issued when context is turned on
        - onCommand (onc): command to be issued when context is turned on
        - shadingCentric (s): shading-centric mode.
        - edit (e): Edit mode flag
    """
@overload #Overload for shadingLightRelCtx in ['edit']
def shadingLightRelCtx(i1: str = ..., i2: str = ..., i3: str = ..., ofc: str = ..., onc: str = ..., s: bool = ..., e: bool = ...) -> str:
    """shadingLightRelCtx is undoable, queryable, and editable.
    
    This command creates a context that can be used for associating lights to
    shading groups. You can put the context into shading-centric mode by using the
    -shadingCentric flag and specifying true. This means that the shading group is
    selected first then lights associated with the shading group are highlighted.
    Subsequent selections result in assignments.
    
    Specifying -shadingCentric false means that the light is to be selected first.
    The shading groups associated with the light will then be selected and
    subsequent selections will result in assignments being made.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - offCommand (ofc): command to be issued when context is turned on
        - onCommand (onc): command to be issued when context is turned on
        - shadingCentric (s): shading-centric mode.
        - edit (e): Edit mode flag
    """
@overload #Overload for shadingLightRelCtx in ['edit']
def shadingLightRelCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., offCommand: str = ..., ofc: str = ..., onCommand: str = ..., onc: str = ..., shadingCentric: bool = ..., s: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """shadingLightRelCtx is undoable, queryable, and editable.
    
    This command creates a context that can be used for associating lights to
    shading groups. You can put the context into shading-centric mode by using the
    -shadingCentric flag and specifying true. This means that the shading group is
    selected first then lights associated with the shading group are highlighted.
    Subsequent selections result in assignments.
    
    Specifying -shadingCentric false means that the light is to be selected first.
    The shading groups associated with the light will then be selected and
    subsequent selections will result in assignments being made.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - offCommand (ofc): command to be issued when context is turned on
        - onCommand (onc): command to be issued when context is turned on
        - shadingCentric (s): shading-centric mode.
        - edit (e): Edit mode flag
    """
