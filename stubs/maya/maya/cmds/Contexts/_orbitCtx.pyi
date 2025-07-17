"""Stub files for Contexts category in Maya commands, command: orbitCtx."""

from typing import Any, overload

@overload #Overload for orbitCtx in ['create']
def orbitCtx(alternateContext: bool = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., localOrbit: bool = ..., name: str = ..., orbitScale: float = ..., toolName: str = ...) -> str:
    """orbitCtx is undoable, queryable, and editable.
    
    Create, edit, or query an orbit context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.orbitCtx( 'orbitContext', os=30.0, lo=False )
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localOrbit (lo): Orbit around the camera's center of interest.
        - name (n): If this is a tool command, name the tool appropriately.
        - orbitScale (os): In degrees of rotation per 100 pixels of cursor drag.
        - toolName (tn): Name of the specific tool to which this command refers.
    """
@overload #Overload for orbitCtx in ['create']
def orbitCtx(ac: bool = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., lo: bool = ..., n: str = ..., os: float = ..., tn: str = ...) -> str:
    """orbitCtx is undoable, queryable, and editable.
    
    Create, edit, or query an orbit context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.orbitCtx( 'orbitContext', os=30.0, lo=False )
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localOrbit (lo): Orbit around the camera's center of interest.
        - name (n): If this is a tool command, name the tool appropriately.
        - orbitScale (os): In degrees of rotation per 100 pixels of cursor drag.
        - toolName (tn): Name of the specific tool to which this command refers.
    """
@overload #Overload for orbitCtx in ['create']
def orbitCtx(alternateContext: bool = ..., ac: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., localOrbit: bool = ..., lo: bool = ..., name: str = ..., n: str = ..., orbitScale: float = ..., os: float = ..., toolName: str = ..., tn: str = ...) -> str:
    """orbitCtx is undoable, queryable, and editable.
    
    Create, edit, or query an orbit context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.orbitCtx( 'orbitContext', os=30.0, lo=False )
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localOrbit (lo): Orbit around the camera's center of interest.
        - name (n): If this is a tool command, name the tool appropriately.
        - orbitScale (os): In degrees of rotation per 100 pixels of cursor drag.
        - toolName (tn): Name of the specific tool to which this command refers.
    """
@overload #Overload for orbitCtx in ['query']
def orbitCtx(alternateContext: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., localOrbit: bool = ..., orbitScale: float = ..., toolName: str = ..., query: bool = ...) -> str:
    """orbitCtx is undoable, queryable, and editable.
    
    Create, edit, or query an orbit context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.orbitCtx( 'orbitContext', os=30.0, lo=False )
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localOrbit (lo): Orbit around the camera's center of interest.
        - orbitScale (os): In degrees of rotation per 100 pixels of cursor drag.
        - toolName (tn): Name of the specific tool to which this command refers.
        - query (q): Query mode flag
    """
@overload #Overload for orbitCtx in ['query']
def orbitCtx(ac: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., lo: bool = ..., os: float = ..., tn: str = ..., q: bool = ...) -> str:
    """orbitCtx is undoable, queryable, and editable.
    
    Create, edit, or query an orbit context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.orbitCtx( 'orbitContext', os=30.0, lo=False )
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localOrbit (lo): Orbit around the camera's center of interest.
        - orbitScale (os): In degrees of rotation per 100 pixels of cursor drag.
        - toolName (tn): Name of the specific tool to which this command refers.
        - query (q): Query mode flag
    """
@overload #Overload for orbitCtx in ['query']
def orbitCtx(alternateContext: bool = ..., ac: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., localOrbit: bool = ..., lo: bool = ..., orbitScale: float = ..., os: float = ..., toolName: str = ..., tn: str = ..., query: bool = ..., q: bool = ...) -> str:
    """orbitCtx is undoable, queryable, and editable.
    
    Create, edit, or query an orbit context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.orbitCtx( 'orbitContext', os=30.0, lo=False )
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localOrbit (lo): Orbit around the camera's center of interest.
        - orbitScale (os): In degrees of rotation per 100 pixels of cursor drag.
        - toolName (tn): Name of the specific tool to which this command refers.
        - query (q): Query mode flag
    """
@overload #Overload for orbitCtx in ['edit']
def orbitCtx(image1: str = ..., image2: str = ..., image3: str = ..., localOrbit: bool = ..., orbitScale: float = ..., edit: bool = ...) -> str:
    """orbitCtx is undoable, queryable, and editable.
    
    Create, edit, or query an orbit context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.orbitCtx( 'orbitContext', os=30.0, lo=False )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localOrbit (lo): Orbit around the camera's center of interest.
        - orbitScale (os): In degrees of rotation per 100 pixels of cursor drag.
        - edit (e): Edit mode flag
    """
@overload #Overload for orbitCtx in ['edit']
def orbitCtx(i1: str = ..., i2: str = ..., i3: str = ..., lo: bool = ..., os: float = ..., e: bool = ...) -> str:
    """orbitCtx is undoable, queryable, and editable.
    
    Create, edit, or query an orbit context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.orbitCtx( 'orbitContext', os=30.0, lo=False )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localOrbit (lo): Orbit around the camera's center of interest.
        - orbitScale (os): In degrees of rotation per 100 pixels of cursor drag.
        - edit (e): Edit mode flag
    """
@overload #Overload for orbitCtx in ['edit']
def orbitCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., localOrbit: bool = ..., lo: bool = ..., orbitScale: float = ..., os: float = ..., edit: bool = ..., e: bool = ...) -> str:
    """orbitCtx is undoable, queryable, and editable.
    
    Create, edit, or query an orbit context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.orbitCtx( 'orbitContext', os=30.0, lo=False )
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localOrbit (lo): Orbit around the camera's center of interest.
        - orbitScale (os): In degrees of rotation per 100 pixels of cursor drag.
        - edit (e): Edit mode flag
    """
