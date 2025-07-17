"""Stub files for Contexts category in Maya commands, command: texSculptCacheContext."""

from typing import Any, overload

@overload #Overload for texSculptCacheContext in ['create']
def texSculptCacheContext(floodPin: float = ..., grabTwist: bool = ..., inverted: bool = ...) -> None:
    """texSculptCacheContext is undoable, queryable, and editable.
    
    This is a tool context command for uv cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.texSculptCacheContext('uvSculptCtx')
        cmds.setToolTo('uvSculptCtx')
        # Set uvSculptCtx's brush size to 10.0
        cmds.texSculptCacheContext('uvSculptCtx', edit=True, bs=10.0)
    ```

    ---
    - Args:
        - floodPin (fp): Sets the pin value for each UV to the given value
        - grabTwist (gtw): If true, the grab brush twists the UVs
        - inverted (inv): If true, inverts the effect of the brush.
    """
@overload #Overload for texSculptCacheContext in ['create']
def texSculptCacheContext(fp: float = ..., gtw: bool = ..., inv: bool = ...) -> None:
    """texSculptCacheContext is undoable, queryable, and editable.
    
    This is a tool context command for uv cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.texSculptCacheContext('uvSculptCtx')
        cmds.setToolTo('uvSculptCtx')
        # Set uvSculptCtx's brush size to 10.0
        cmds.texSculptCacheContext('uvSculptCtx', edit=True, bs=10.0)
    ```

    ---
    - Args:
        - floodPin (fp): Sets the pin value for each UV to the given value
        - grabTwist (gtw): If true, the grab brush twists the UVs
        - inverted (inv): If true, inverts the effect of the brush.
    """
@overload #Overload for texSculptCacheContext in ['create']
def texSculptCacheContext(floodPin: float = ..., fp: float = ..., grabTwist: bool = ..., gtw: bool = ..., inverted: bool = ..., inv: bool = ...) -> None:
    """texSculptCacheContext is undoable, queryable, and editable.
    
    This is a tool context command for uv cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.texSculptCacheContext('uvSculptCtx')
        cmds.setToolTo('uvSculptCtx')
        # Set uvSculptCtx's brush size to 10.0
        cmds.texSculptCacheContext('uvSculptCtx', edit=True, bs=10.0)
    ```

    ---
    - Args:
        - floodPin (fp): Sets the pin value for each UV to the given value
        - grabTwist (gtw): If true, the grab brush twists the UVs
        - inverted (inv): If true, inverts the effect of the brush.
    """
@overload #Overload for texSculptCacheContext in ['query']
def texSculptCacheContext(direction: int = ..., falloffType: int = ..., grabTwist: bool = ..., inverted: bool = ..., mode: str = ..., sculptFalloffCurve: str = ..., showBrushRingDuringStroke: bool = ..., size: float = ..., strength: float = ..., query: bool = ...) -> None:
    """texSculptCacheContext is undoable, queryable, and editable.
    
    This is a tool context command for uv cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.texSculptCacheContext('uvSculptCtx')
        cmds.setToolTo('uvSculptCtx')
        # Set uvSculptCtx's brush size to 10.0
        cmds.texSculptCacheContext('uvSculptCtx', edit=True, bs=10.0)
    ```

    ---
    - Args:
        - direction (d): Specifies how the brush determines where the uvs go.
        - falloffType (ft): Specifies how the brush determines which uvs to affect.
        - grabTwist (gtw): If true, the grab brush twists the UVs
        - inverted (inv): If true, inverts the effect of the brush.
        - mode (m): Specifies the type of sculpting effect the brush will perform.
        - sculptFalloffCurve (sfc): Specifies the falloff curve that affects the brush.
        - showBrushRingDuringStroke (sbr): Specifies whether or not to show the brush ring during stroke.
        - size (sz): Specifies the world-space size of the current brush.
        - strength (st): Specifies the world-space strength of the current brush.
        - query (q): Query mode flag
    """
@overload #Overload for texSculptCacheContext in ['query']
def texSculptCacheContext(d: int = ..., ft: int = ..., gtw: bool = ..., inv: bool = ..., m: str = ..., sfc: str = ..., sbr: bool = ..., sz: float = ..., st: float = ..., q: bool = ...) -> None:
    """texSculptCacheContext is undoable, queryable, and editable.
    
    This is a tool context command for uv cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.texSculptCacheContext('uvSculptCtx')
        cmds.setToolTo('uvSculptCtx')
        # Set uvSculptCtx's brush size to 10.0
        cmds.texSculptCacheContext('uvSculptCtx', edit=True, bs=10.0)
    ```

    ---
    - Args:
        - direction (d): Specifies how the brush determines where the uvs go.
        - falloffType (ft): Specifies how the brush determines which uvs to affect.
        - grabTwist (gtw): If true, the grab brush twists the UVs
        - inverted (inv): If true, inverts the effect of the brush.
        - mode (m): Specifies the type of sculpting effect the brush will perform.
        - sculptFalloffCurve (sfc): Specifies the falloff curve that affects the brush.
        - showBrushRingDuringStroke (sbr): Specifies whether or not to show the brush ring during stroke.
        - size (sz): Specifies the world-space size of the current brush.
        - strength (st): Specifies the world-space strength of the current brush.
        - query (q): Query mode flag
    """
@overload #Overload for texSculptCacheContext in ['query']
def texSculptCacheContext(direction: int = ..., d: int = ..., falloffType: int = ..., ft: int = ..., grabTwist: bool = ..., gtw: bool = ..., inverted: bool = ..., inv: bool = ..., mode: str = ..., m: str = ..., sculptFalloffCurve: str = ..., sfc: str = ..., showBrushRingDuringStroke: bool = ..., sbr: bool = ..., size: float = ..., sz: float = ..., strength: float = ..., st: float = ..., query: bool = ..., q: bool = ...) -> None:
    """texSculptCacheContext is undoable, queryable, and editable.
    
    This is a tool context command for uv cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.texSculptCacheContext('uvSculptCtx')
        cmds.setToolTo('uvSculptCtx')
        # Set uvSculptCtx's brush size to 10.0
        cmds.texSculptCacheContext('uvSculptCtx', edit=True, bs=10.0)
    ```

    ---
    - Args:
        - direction (d): Specifies how the brush determines where the uvs go.
        - falloffType (ft): Specifies how the brush determines which uvs to affect.
        - grabTwist (gtw): If true, the grab brush twists the UVs
        - inverted (inv): If true, inverts the effect of the brush.
        - mode (m): Specifies the type of sculpting effect the brush will perform.
        - sculptFalloffCurve (sfc): Specifies the falloff curve that affects the brush.
        - showBrushRingDuringStroke (sbr): Specifies whether or not to show the brush ring during stroke.
        - size (sz): Specifies the world-space size of the current brush.
        - strength (st): Specifies the world-space strength of the current brush.
        - query (q): Query mode flag
    """
@overload #Overload for texSculptCacheContext in ['edit']
def texSculptCacheContext(adjustSize: bool = ..., adjustStrength: bool = ..., direction: int = ..., falloffType: int = ..., floodPin: float = ..., grabTwist: bool = ..., inverted: bool = ..., mode: str = ..., sculptFalloffCurve: str = ..., showBrushRingDuringStroke: bool = ..., size: float = ..., strength: float = ..., edit: bool = ...) -> None:
    """texSculptCacheContext is undoable, queryable, and editable.
    
    This is a tool context command for uv cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.texSculptCacheContext('uvSculptCtx')
        cmds.setToolTo('uvSculptCtx')
        # Set uvSculptCtx's brush size to 10.0
        cmds.texSculptCacheContext('uvSculptCtx', edit=True, bs=10.0)
    ```

    ---
    - Args:
        - adjustSize (asz): If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous sculpt mode.
        - adjustStrength (ast): If true, puts the tool into the mode where dragging the mouse will edit the brush strength. If false, puts the tool back into the previous sculpt mode.
        - direction (d): Specifies how the brush determines where the uvs go.
        - falloffType (ft): Specifies how the brush determines which uvs to affect.
        - floodPin (fp): Sets the pin value for each UV to the given value
        - grabTwist (gtw): If true, the grab brush twists the UVs
        - inverted (inv): If true, inverts the effect of the brush.
        - mode (m): Specifies the type of sculpting effect the brush will perform.
        - sculptFalloffCurve (sfc): Specifies the falloff curve that affects the brush.
        - showBrushRingDuringStroke (sbr): Specifies whether or not to show the brush ring during stroke.
        - size (sz): Specifies the world-space size of the current brush.
        - strength (st): Specifies the world-space strength of the current brush.
        - edit (e): Edit mode flag
    """
@overload #Overload for texSculptCacheContext in ['edit']
def texSculptCacheContext(asz: bool = ..., ast: bool = ..., d: int = ..., ft: int = ..., fp: float = ..., gtw: bool = ..., inv: bool = ..., m: str = ..., sfc: str = ..., sbr: bool = ..., sz: float = ..., st: float = ..., e: bool = ...) -> None:
    """texSculptCacheContext is undoable, queryable, and editable.
    
    This is a tool context command for uv cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.texSculptCacheContext('uvSculptCtx')
        cmds.setToolTo('uvSculptCtx')
        # Set uvSculptCtx's brush size to 10.0
        cmds.texSculptCacheContext('uvSculptCtx', edit=True, bs=10.0)
    ```

    ---
    - Args:
        - adjustSize (asz): If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous sculpt mode.
        - adjustStrength (ast): If true, puts the tool into the mode where dragging the mouse will edit the brush strength. If false, puts the tool back into the previous sculpt mode.
        - direction (d): Specifies how the brush determines where the uvs go.
        - falloffType (ft): Specifies how the brush determines which uvs to affect.
        - floodPin (fp): Sets the pin value for each UV to the given value
        - grabTwist (gtw): If true, the grab brush twists the UVs
        - inverted (inv): If true, inverts the effect of the brush.
        - mode (m): Specifies the type of sculpting effect the brush will perform.
        - sculptFalloffCurve (sfc): Specifies the falloff curve that affects the brush.
        - showBrushRingDuringStroke (sbr): Specifies whether or not to show the brush ring during stroke.
        - size (sz): Specifies the world-space size of the current brush.
        - strength (st): Specifies the world-space strength of the current brush.
        - edit (e): Edit mode flag
    """
@overload #Overload for texSculptCacheContext in ['edit']
def texSculptCacheContext(adjustSize: bool = ..., asz: bool = ..., adjustStrength: bool = ..., ast: bool = ..., direction: int = ..., d: int = ..., falloffType: int = ..., ft: int = ..., floodPin: float = ..., fp: float = ..., grabTwist: bool = ..., gtw: bool = ..., inverted: bool = ..., inv: bool = ..., mode: str = ..., m: str = ..., sculptFalloffCurve: str = ..., sfc: str = ..., showBrushRingDuringStroke: bool = ..., sbr: bool = ..., size: float = ..., sz: float = ..., strength: float = ..., st: float = ..., edit: bool = ..., e: bool = ...) -> None:
    """texSculptCacheContext is undoable, queryable, and editable.
    
    This is a tool context command for uv cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.texSculptCacheContext('uvSculptCtx')
        cmds.setToolTo('uvSculptCtx')
        # Set uvSculptCtx's brush size to 10.0
        cmds.texSculptCacheContext('uvSculptCtx', edit=True, bs=10.0)
    ```

    ---
    - Args:
        - adjustSize (asz): If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous sculpt mode.
        - adjustStrength (ast): If true, puts the tool into the mode where dragging the mouse will edit the brush strength. If false, puts the tool back into the previous sculpt mode.
        - direction (d): Specifies how the brush determines where the uvs go.
        - falloffType (ft): Specifies how the brush determines which uvs to affect.
        - floodPin (fp): Sets the pin value for each UV to the given value
        - grabTwist (gtw): If true, the grab brush twists the UVs
        - inverted (inv): If true, inverts the effect of the brush.
        - mode (m): Specifies the type of sculpting effect the brush will perform.
        - sculptFalloffCurve (sfc): Specifies the falloff curve that affects the brush.
        - showBrushRingDuringStroke (sbr): Specifies whether or not to show the brush ring during stroke.
        - size (sz): Specifies the world-space size of the current brush.
        - strength (st): Specifies the world-space strength of the current brush.
        - edit (e): Edit mode flag
    """
