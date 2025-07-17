"""Stub files for Contexts category in Maya commands, command: texMoveContext."""

from typing import Any, overload

@overload #Overload for texMoveContext in ['create']
def texMoveContext([object]: [object], exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ...) -> str:
    """texMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.texMoveContext()
        # To query the position of the manipulator
        cmds.texMoveContext( 'texMoveContext', q=True, position=True )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for texMoveContext in ['create']
def texMoveContext([object]: [object], ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ...) -> str:
    """texMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.texMoveContext()
        # To query the position of the manipulator
        cmds.texMoveContext( 'texMoveContext', q=True, position=True )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for texMoveContext in ['create']
def texMoveContext([object]: [object], exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ...) -> str:
    """texMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.texMoveContext()
        # To query the position of the manipulator
        cmds.texMoveContext( 'texMoveContext', q=True, position=True )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for texMoveContext in ['query']
def texMoveContext([object]: [object], editPivotMode: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., position: bool = ..., snap: bool = ..., snapComponentsRelative: bool = ..., snapPixelMode: int = ..., snapValue: float = ..., tweakMode: bool = ..., query: bool = ...) -> str:
    """texMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.texMoveContext()
        # To query the position of the manipulator
        cmds.texMoveContext( 'texMoveContext', q=True, position=True )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - editPivotMode (epm): Returns true when the manipulator is in edit pivot mode.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - position (p): Returns the current position of the manipulator
        - snap (s): Sets or queries whether snapping is to be used.
        - snapComponentsRelative (scr): Value can be : true or false. If true, while snapping a group of UVs, the relative spacing between them will be preserved. If false, all the UVs will be snapped to the target point
        - snapPixelMode (spm): Sets the snapping mode to be the pixel center or upper left corner.
        - snapValue (sv): Sets or queries the size of the snapping increment.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.
        - query (q): Query mode flag
    """
@overload #Overload for texMoveContext in ['query']
def texMoveContext([object]: [object], epm: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., p: bool = ..., s: bool = ..., scr: bool = ..., spm: int = ..., sv: float = ..., twk: bool = ..., q: bool = ...) -> str:
    """texMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.texMoveContext()
        # To query the position of the manipulator
        cmds.texMoveContext( 'texMoveContext', q=True, position=True )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - editPivotMode (epm): Returns true when the manipulator is in edit pivot mode.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - position (p): Returns the current position of the manipulator
        - snap (s): Sets or queries whether snapping is to be used.
        - snapComponentsRelative (scr): Value can be : true or false. If true, while snapping a group of UVs, the relative spacing between them will be preserved. If false, all the UVs will be snapped to the target point
        - snapPixelMode (spm): Sets the snapping mode to be the pixel center or upper left corner.
        - snapValue (sv): Sets or queries the size of the snapping increment.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.
        - query (q): Query mode flag
    """
@overload #Overload for texMoveContext in ['query']
def texMoveContext([object]: [object], editPivotMode: bool = ..., epm: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., position: bool = ..., p: bool = ..., snap: bool = ..., s: bool = ..., snapComponentsRelative: bool = ..., scr: bool = ..., snapPixelMode: int = ..., spm: int = ..., snapValue: float = ..., sv: float = ..., tweakMode: bool = ..., twk: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """texMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.texMoveContext()
        # To query the position of the manipulator
        cmds.texMoveContext( 'texMoveContext', q=True, position=True )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - editPivotMode (epm): Returns true when the manipulator is in edit pivot mode.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - position (p): Returns the current position of the manipulator
        - snap (s): Sets or queries whether snapping is to be used.
        - snapComponentsRelative (scr): Value can be : true or false. If true, while snapping a group of UVs, the relative spacing between them will be preserved. If false, all the UVs will be snapped to the target point
        - snapPixelMode (spm): Sets the snapping mode to be the pixel center or upper left corner.
        - snapValue (sv): Sets or queries the size of the snapping increment.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.
        - query (q): Query mode flag
    """
@overload #Overload for texMoveContext in ['edit']
def texMoveContext([object]: [object], image1: str = ..., image2: str = ..., image3: str = ..., snap: bool = ..., snapComponentsRelative: bool = ..., snapPixelMode: int = ..., snapValue: float = ..., tweakMode: bool = ..., edit: bool = ...) -> str:
    """texMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.texMoveContext()
        # To query the position of the manipulator
        cmds.texMoveContext( 'texMoveContext', q=True, position=True )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - snap (s): Sets or queries whether snapping is to be used.
        - snapComponentsRelative (scr): Value can be : true or false. If true, while snapping a group of UVs, the relative spacing between them will be preserved. If false, all the UVs will be snapped to the target point
        - snapPixelMode (spm): Sets the snapping mode to be the pixel center or upper left corner.
        - snapValue (sv): Sets or queries the size of the snapping increment.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.
        - edit (e): Edit mode flag
    """
@overload #Overload for texMoveContext in ['edit']
def texMoveContext([object]: [object], i1: str = ..., i2: str = ..., i3: str = ..., s: bool = ..., scr: bool = ..., spm: int = ..., sv: float = ..., twk: bool = ..., e: bool = ...) -> str:
    """texMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.texMoveContext()
        # To query the position of the manipulator
        cmds.texMoveContext( 'texMoveContext', q=True, position=True )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - snap (s): Sets or queries whether snapping is to be used.
        - snapComponentsRelative (scr): Value can be : true or false. If true, while snapping a group of UVs, the relative spacing between them will be preserved. If false, all the UVs will be snapped to the target point
        - snapPixelMode (spm): Sets the snapping mode to be the pixel center or upper left corner.
        - snapValue (sv): Sets or queries the size of the snapping increment.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.
        - edit (e): Edit mode flag
    """
@overload #Overload for texMoveContext in ['edit']
def texMoveContext([object]: [object], image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., snap: bool = ..., s: bool = ..., snapComponentsRelative: bool = ..., scr: bool = ..., snapPixelMode: int = ..., spm: int = ..., snapValue: float = ..., sv: float = ..., tweakMode: bool = ..., twk: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """texMoveContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a texture editor move manip
    context. Note that the above flags control the global behaviour of all texture
    editor move manip contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    texture editor move manip contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new move context:
        cmds.texMoveContext()
        # To query the position of the manipulator
        cmds.texMoveContext( 'texMoveContext', q=True, position=True )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - snap (s): Sets or queries whether snapping is to be used.
        - snapComponentsRelative (scr): Value can be : true or false. If true, while snapping a group of UVs, the relative spacing between them will be preserved. If false, all the UVs will be snapped to the target point
        - snapPixelMode (spm): Sets the snapping mode to be the pixel center or upper left corner.
        - snapValue (sv): Sets or queries the size of the snapping increment.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.
        - edit (e): Edit mode flag
    """
