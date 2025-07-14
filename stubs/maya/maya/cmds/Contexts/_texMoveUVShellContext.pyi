"""Stub files for Contexts category in Maya commands, command: texMoveUVShellContext."""

from typing import Any, overload

@overload #Overload for texMoveUVShellContext in ['create']
def texMoveUVShellContext([object]: [object], exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., iterations: int = ..., mask: bool = ..., shellBorder: float = ...) -> str:
    """texMoveUVShellContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    ---
    - Args:
        - [object]: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - iterations (it): Sets or queries the number of iterations to perform.
        - mask (m): Sets or queries masking on the shell.
        - shellBorder (sb): Sets or queries the size of the shell border.
    """
@overload #Overload for texMoveUVShellContext in ['create']
def texMoveUVShellContext([object]: [object], ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., it: int = ..., m: bool = ..., sb: float = ...) -> str:
    """texMoveUVShellContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    ---
    - Args:
        - [object]: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - iterations (it): Sets or queries the number of iterations to perform.
        - mask (m): Sets or queries masking on the shell.
        - shellBorder (sb): Sets or queries the size of the shell border.
    """
@overload #Overload for texMoveUVShellContext in ['create']
def texMoveUVShellContext([object]: [object], exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., iterations: int = ..., it: int = ..., mask: bool = ..., m: bool = ..., shellBorder: float = ..., sb: float = ...) -> str:
    """texMoveUVShellContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    ---
    - Args:
        - [object]: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - iterations (it): Sets or queries the number of iterations to perform.
        - mask (m): Sets or queries masking on the shell.
        - shellBorder (sb): Sets or queries the size of the shell border.
    """
@overload #Overload for texMoveUVShellContext in ['query']
def texMoveUVShellContext([object]: [object], image1: str = ..., image2: str = ..., image3: str = ..., iterations: int = ..., mask: bool = ..., position: bool = ..., shellBorder: float = ..., query: bool = ...) -> str:
    """texMoveUVShellContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    ---
    - Args:
        - [object]: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - iterations (it): Sets or queries the number of iterations to perform.
        - mask (m): Sets or queries masking on the shell.
        - position (p): Returns the current position of the manipulator
        - shellBorder (sb): Sets or queries the size of the shell border.
        - query (q): Query mode flag
    """
@overload #Overload for texMoveUVShellContext in ['query']
def texMoveUVShellContext([object]: [object], i1: str = ..., i2: str = ..., i3: str = ..., it: int = ..., m: bool = ..., p: bool = ..., sb: float = ..., q: bool = ...) -> str:
    """texMoveUVShellContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    ---
    - Args:
        - [object]: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - iterations (it): Sets or queries the number of iterations to perform.
        - mask (m): Sets or queries masking on the shell.
        - position (p): Returns the current position of the manipulator
        - shellBorder (sb): Sets or queries the size of the shell border.
        - query (q): Query mode flag
    """
@overload #Overload for texMoveUVShellContext in ['query']
def texMoveUVShellContext([object]: [object], image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., iterations: int = ..., it: int = ..., mask: bool = ..., m: bool = ..., position: bool = ..., p: bool = ..., shellBorder: float = ..., sb: float = ..., query: bool = ..., q: bool = ...) -> str:
    """texMoveUVShellContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    ---
    - Args:
        - [object]: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - iterations (it): Sets or queries the number of iterations to perform.
        - mask (m): Sets or queries masking on the shell.
        - position (p): Returns the current position of the manipulator
        - shellBorder (sb): Sets or queries the size of the shell border.
        - query (q): Query mode flag
    """
@overload #Overload for texMoveUVShellContext in ['edit']
def texMoveUVShellContext([object]: [object], image1: str = ..., image2: str = ..., image3: str = ..., iterations: int = ..., mask: bool = ..., shellBorder: float = ..., edit: bool = ...) -> str:
    """texMoveUVShellContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    ---
    - Args:
        - [object]: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - iterations (it): Sets or queries the number of iterations to perform.
        - mask (m): Sets or queries masking on the shell.
        - shellBorder (sb): Sets or queries the size of the shell border.
        - edit (e): Edit mode flag
    """
@overload #Overload for texMoveUVShellContext in ['edit']
def texMoveUVShellContext([object]: [object], i1: str = ..., i2: str = ..., i3: str = ..., it: int = ..., m: bool = ..., sb: float = ..., e: bool = ...) -> str:
    """texMoveUVShellContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    ---
    - Args:
        - [object]: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - iterations (it): Sets or queries the number of iterations to perform.
        - mask (m): Sets or queries masking on the shell.
        - shellBorder (sb): Sets or queries the size of the shell border.
        - edit (e): Edit mode flag
    """
@overload #Overload for texMoveUVShellContext in ['edit']
def texMoveUVShellContext([object]: [object], image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., iterations: int = ..., it: int = ..., mask: bool = ..., m: bool = ..., shellBorder: float = ..., sb: float = ..., edit: bool = ..., e: bool = ...) -> str:
    """texMoveUVShellContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    ---
    - Args:
        - [object]: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - iterations (it): Sets or queries the number of iterations to perform.
        - mask (m): Sets or queries masking on the shell.
        - shellBorder (sb): Sets or queries the size of the shell border.
        - edit (e): Edit mode flag
    """
