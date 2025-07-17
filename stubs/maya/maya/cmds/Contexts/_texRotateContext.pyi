"""Stub files for Contexts category in Maya commands, command: texRotateContext."""

from typing import Any, overload

@overload #Overload for texRotateContext in ['create']
def texRotateContext(exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ...) -> str:
    """texRotateContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a rotate context for the UV
    Editor. Note that the above flag controls the global behaviour of all texture
    editor rotate contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flag, will change all existing
    texture editor rotate contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new rotate context:
        cmds.texRotateContext()
        # To query the position of the manipulator
        cmds.texRotateContext( 'texRotateContext', q=True, position=True )
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for texRotateContext in ['create']
def texRotateContext(ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ...) -> str:
    """texRotateContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a rotate context for the UV
    Editor. Note that the above flag controls the global behaviour of all texture
    editor rotate contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flag, will change all existing
    texture editor rotate contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new rotate context:
        cmds.texRotateContext()
        # To query the position of the manipulator
        cmds.texRotateContext( 'texRotateContext', q=True, position=True )
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for texRotateContext in ['create']
def texRotateContext(exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ...) -> str:
    """texRotateContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a rotate context for the UV
    Editor. Note that the above flag controls the global behaviour of all texture
    editor rotate contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flag, will change all existing
    texture editor rotate contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new rotate context:
        cmds.texRotateContext()
        # To query the position of the manipulator
        cmds.texRotateContext( 'texRotateContext', q=True, position=True )
    ```

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for texRotateContext in ['query']
def texRotateContext(editPivotMode: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., position: bool = ..., snap: bool = ..., snapRelative: bool = ..., snapValue: float = ..., tweakMode: bool = ..., query: bool = ...) -> str:
    """texRotateContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a rotate context for the UV
    Editor. Note that the above flag controls the global behaviour of all texture
    editor rotate contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flag, will change all existing
    texture editor rotate contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new rotate context:
        cmds.texRotateContext()
        # To query the position of the manipulator
        cmds.texRotateContext( 'texRotateContext', q=True, position=True )
    ```

    ---
    - Args:
        - editPivotMode (epm): Returns true when the manipulator is in edit pivot mode.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - position (p): Returns the current position of the manipulator.
        - snap (s): Sets or queries whether snapping is to be used.
        - snapRelative (sr): Sets or queries whether snapping is relative.
        - snapValue (sv): Sets or queries the size of the snapping increment.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and rotated in one step using a click-drag interaction.
        - query (q): Query mode flag
    """
@overload #Overload for texRotateContext in ['query']
def texRotateContext(epm: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., p: bool = ..., s: bool = ..., sr: bool = ..., sv: float = ..., twk: bool = ..., q: bool = ...) -> str:
    """texRotateContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a rotate context for the UV
    Editor. Note that the above flag controls the global behaviour of all texture
    editor rotate contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flag, will change all existing
    texture editor rotate contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new rotate context:
        cmds.texRotateContext()
        # To query the position of the manipulator
        cmds.texRotateContext( 'texRotateContext', q=True, position=True )
    ```

    ---
    - Args:
        - editPivotMode (epm): Returns true when the manipulator is in edit pivot mode.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - position (p): Returns the current position of the manipulator.
        - snap (s): Sets or queries whether snapping is to be used.
        - snapRelative (sr): Sets or queries whether snapping is relative.
        - snapValue (sv): Sets or queries the size of the snapping increment.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and rotated in one step using a click-drag interaction.
        - query (q): Query mode flag
    """
@overload #Overload for texRotateContext in ['query']
def texRotateContext(editPivotMode: bool = ..., epm: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., position: bool = ..., p: bool = ..., snap: bool = ..., s: bool = ..., snapRelative: bool = ..., sr: bool = ..., snapValue: float = ..., sv: float = ..., tweakMode: bool = ..., twk: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """texRotateContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a rotate context for the UV
    Editor. Note that the above flag controls the global behaviour of all texture
    editor rotate contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flag, will change all existing
    texture editor rotate contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new rotate context:
        cmds.texRotateContext()
        # To query the position of the manipulator
        cmds.texRotateContext( 'texRotateContext', q=True, position=True )
    ```

    ---
    - Args:
        - editPivotMode (epm): Returns true when the manipulator is in edit pivot mode.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - position (p): Returns the current position of the manipulator.
        - snap (s): Sets or queries whether snapping is to be used.
        - snapRelative (sr): Sets or queries whether snapping is relative.
        - snapValue (sv): Sets or queries the size of the snapping increment.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and rotated in one step using a click-drag interaction.
        - query (q): Query mode flag
    """
@overload #Overload for texRotateContext in ['edit']
def texRotateContext(image1: str = ..., image2: str = ..., image3: str = ..., snap: bool = ..., snapRelative: bool = ..., snapValue: float = ..., tweakMode: bool = ..., edit: bool = ...) -> str:
    """texRotateContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a rotate context for the UV
    Editor. Note that the above flag controls the global behaviour of all texture
    editor rotate contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flag, will change all existing
    texture editor rotate contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new rotate context:
        cmds.texRotateContext()
        # To query the position of the manipulator
        cmds.texRotateContext( 'texRotateContext', q=True, position=True )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - snap (s): Sets or queries whether snapping is to be used.
        - snapRelative (sr): Sets or queries whether snapping is relative.
        - snapValue (sv): Sets or queries the size of the snapping increment.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and rotated in one step using a click-drag interaction.
        - edit (e): Edit mode flag
    """
@overload #Overload for texRotateContext in ['edit']
def texRotateContext(i1: str = ..., i2: str = ..., i3: str = ..., s: bool = ..., sr: bool = ..., sv: float = ..., twk: bool = ..., e: bool = ...) -> str:
    """texRotateContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a rotate context for the UV
    Editor. Note that the above flag controls the global behaviour of all texture
    editor rotate contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flag, will change all existing
    texture editor rotate contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new rotate context:
        cmds.texRotateContext()
        # To query the position of the manipulator
        cmds.texRotateContext( 'texRotateContext', q=True, position=True )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - snap (s): Sets or queries whether snapping is to be used.
        - snapRelative (sr): Sets or queries whether snapping is relative.
        - snapValue (sv): Sets or queries the size of the snapping increment.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and rotated in one step using a click-drag interaction.
        - edit (e): Edit mode flag
    """
@overload #Overload for texRotateContext in ['edit']
def texRotateContext(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., snap: bool = ..., s: bool = ..., snapRelative: bool = ..., sr: bool = ..., snapValue: float = ..., sv: float = ..., tweakMode: bool = ..., twk: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """texRotateContext is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a rotate context for the UV
    Editor. Note that the above flag controls the global behaviour of all texture
    editor rotate contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flag, will change all existing
    texture editor rotate contexts.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a new rotate context:
        cmds.texRotateContext()
        # To query the position of the manipulator
        cmds.texRotateContext( 'texRotateContext', q=True, position=True )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - snap (s): Sets or queries whether snapping is to be used.
        - snapRelative (sr): Sets or queries whether snapping is relative.
        - snapValue (sv): Sets or queries the size of the snapping increment.
        - tweakMode (twk): When true, the manipulator is hidden and highlighted components can be selected and rotated in one step using a click-drag interaction.
        - edit (e): Edit mode flag
    """
