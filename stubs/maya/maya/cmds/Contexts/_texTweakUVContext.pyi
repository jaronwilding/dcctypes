"""Stub files for Contexts category in Maya commands, command: texTweakUVContext."""

from typing import Any, overload

@overload #Overload for texTweakUVContext in ['create']
def texTweakUVContext([object]: [object], exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., tolerance: float = ...) -> str:
    """texTweakUVContext is undoable, queryable, and editable.
    
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
        - tolerance (t): Controls the initial selection snapping tolerance.
    """
@overload #Overload for texTweakUVContext in ['create']
def texTweakUVContext([object]: [object], ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., t: float = ...) -> str:
    """texTweakUVContext is undoable, queryable, and editable.
    
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
        - tolerance (t): Controls the initial selection snapping tolerance.
    """
@overload #Overload for texTweakUVContext in ['create']
def texTweakUVContext([object]: [object], exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., tolerance: float = ..., t: float = ...) -> str:
    """texTweakUVContext is undoable, queryable, and editable.
    
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
        - tolerance (t): Controls the initial selection snapping tolerance.
    """
@overload #Overload for texTweakUVContext in ['query']
def texTweakUVContext([object]: [object], image1: str = ..., image2: str = ..., image3: str = ..., position: bool = ..., tolerance: float = ..., query: bool = ...) -> str:
    """texTweakUVContext is undoable, queryable, and editable.
    
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
        - position (p): Returns the current position of the manipulator
        - tolerance (t): Controls the initial selection snapping tolerance.
        - query (q): Query mode flag
    """
@overload #Overload for texTweakUVContext in ['query']
def texTweakUVContext([object]: [object], i1: str = ..., i2: str = ..., i3: str = ..., p: bool = ..., t: float = ..., q: bool = ...) -> str:
    """texTweakUVContext is undoable, queryable, and editable.
    
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
        - position (p): Returns the current position of the manipulator
        - tolerance (t): Controls the initial selection snapping tolerance.
        - query (q): Query mode flag
    """
@overload #Overload for texTweakUVContext in ['query']
def texTweakUVContext([object]: [object], image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., position: bool = ..., p: bool = ..., tolerance: float = ..., t: float = ..., query: bool = ..., q: bool = ...) -> str:
    """texTweakUVContext is undoable, queryable, and editable.
    
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
        - position (p): Returns the current position of the manipulator
        - tolerance (t): Controls the initial selection snapping tolerance.
        - query (q): Query mode flag
    """
@overload #Overload for texTweakUVContext in ['edit']
def texTweakUVContext([object]: [object], image1: str = ..., image2: str = ..., image3: str = ..., tolerance: float = ..., edit: bool = ...) -> str:
    """texTweakUVContext is undoable, queryable, and editable.
    
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
        - tolerance (t): Controls the initial selection snapping tolerance.
        - edit (e): Edit mode flag
    """
@overload #Overload for texTweakUVContext in ['edit']
def texTweakUVContext([object]: [object], i1: str = ..., i2: str = ..., i3: str = ..., t: float = ..., e: bool = ...) -> str:
    """texTweakUVContext is undoable, queryable, and editable.
    
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
        - tolerance (t): Controls the initial selection snapping tolerance.
        - edit (e): Edit mode flag
    """
@overload #Overload for texTweakUVContext in ['edit']
def texTweakUVContext([object]: [object], image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., tolerance: float = ..., t: float = ..., edit: bool = ..., e: bool = ...) -> str:
    """texTweakUVContext is undoable, queryable, and editable.
    
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
        - tolerance (t): Controls the initial selection snapping tolerance.
        - edit (e): Edit mode flag
    """
