"""Stub files for Contexts category in Maya commands, command: polyCutUVCtx."""

from typing import Any, overload

@overload #Overload for polyCutUVCtx in ['query']
def polyCutUVCtx(contextName: contextName, loopSpeed: int = ..., mapBordersColor: [float, float, float] = ..., showCheckerMap: bool = ..., showTextureBorders: bool = ..., showUVShellColoring: bool = ..., steadyStroke: bool = ..., steadyStrokeDistance: float = ..., symmetry: int = ..., query: bool = ...) -> bool | float:
    """polyCutUVCtx is undoable, queryable, and editable.
    
    Create a new context to cut UVs on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new cut facets context, then switch to it
        cmds.polyCutUVCtx('polyCutUVCtx1')
        cmds.setToolTo('polyCutUVCtx1')
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - loopSpeed (ls): Edit the speed of loop cutting.
        - mapBordersColor (mbc): Color of UV map border edges in 3d view.
        - showCheckerMap (scm): Display checker map.
        - showTextureBorders (stb): Display texture border edges.
        - showUVShellColoring (ssc): Turn on UV shell coloring or not.
        - steadyStroke (ss): Turn on steady stroke or not.
        - steadyStrokeDistance (ssd): The distance for steady stroke.
        - symmetry (sym): Symmetric modeling.
        - query (q): Query mode flag
    """
@overload #Overload for polyCutUVCtx in ['query']
def polyCutUVCtx(contextName: contextName, ls: int = ..., mbc: [float, float, float] = ..., scm: bool = ..., stb: bool = ..., ssc: bool = ..., ss: bool = ..., ssd: float = ..., sym: int = ..., q: bool = ...) -> bool | float:
    """polyCutUVCtx is undoable, queryable, and editable.
    
    Create a new context to cut UVs on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new cut facets context, then switch to it
        cmds.polyCutUVCtx('polyCutUVCtx1')
        cmds.setToolTo('polyCutUVCtx1')
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - loopSpeed (ls): Edit the speed of loop cutting.
        - mapBordersColor (mbc): Color of UV map border edges in 3d view.
        - showCheckerMap (scm): Display checker map.
        - showTextureBorders (stb): Display texture border edges.
        - showUVShellColoring (ssc): Turn on UV shell coloring or not.
        - steadyStroke (ss): Turn on steady stroke or not.
        - steadyStrokeDistance (ssd): The distance for steady stroke.
        - symmetry (sym): Symmetric modeling.
        - query (q): Query mode flag
    """
@overload #Overload for polyCutUVCtx in ['query']
def polyCutUVCtx(contextName: contextName, loopSpeed: int = ..., ls: int = ..., mapBordersColor: [float, float, float] = ..., mbc: [float, float, float] = ..., showCheckerMap: bool = ..., scm: bool = ..., showTextureBorders: bool = ..., stb: bool = ..., showUVShellColoring: bool = ..., ssc: bool = ..., steadyStroke: bool = ..., ss: bool = ..., steadyStrokeDistance: float = ..., ssd: float = ..., symmetry: int = ..., sym: int = ..., query: bool = ..., q: bool = ...) -> bool | float:
    """polyCutUVCtx is undoable, queryable, and editable.
    
    Create a new context to cut UVs on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new cut facets context, then switch to it
        cmds.polyCutUVCtx('polyCutUVCtx1')
        cmds.setToolTo('polyCutUVCtx1')
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - loopSpeed (ls): Edit the speed of loop cutting.
        - mapBordersColor (mbc): Color of UV map border edges in 3d view.
        - showCheckerMap (scm): Display checker map.
        - showTextureBorders (stb): Display texture border edges.
        - showUVShellColoring (ssc): Turn on UV shell coloring or not.
        - steadyStroke (ss): Turn on steady stroke or not.
        - steadyStrokeDistance (ssd): The distance for steady stroke.
        - symmetry (sym): Symmetric modeling.
        - query (q): Query mode flag
    """
@overload #Overload for polyCutUVCtx in ['edit']
def polyCutUVCtx(contextName: contextName, loopSpeed: int = ..., mapBordersColor: [float, float, float] = ..., showCheckerMap: bool = ..., showTextureBorders: bool = ..., showUVShellColoring: bool = ..., steadyStroke: bool = ..., steadyStrokeDistance: float = ..., symmetry: int = ..., edit: bool = ...) -> bool | float:
    """polyCutUVCtx is undoable, queryable, and editable.
    
    Create a new context to cut UVs on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new cut facets context, then switch to it
        cmds.polyCutUVCtx('polyCutUVCtx1')
        cmds.setToolTo('polyCutUVCtx1')
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - loopSpeed (ls): Edit the speed of loop cutting.
        - mapBordersColor (mbc): Color of UV map border edges in 3d view.
        - showCheckerMap (scm): Display checker map.
        - showTextureBorders (stb): Display texture border edges.
        - showUVShellColoring (ssc): Turn on UV shell coloring or not.
        - steadyStroke (ss): Turn on steady stroke or not.
        - steadyStrokeDistance (ssd): The distance for steady stroke.
        - symmetry (sym): Symmetric modeling.
        - edit (e): Edit mode flag
    """
@overload #Overload for polyCutUVCtx in ['edit']
def polyCutUVCtx(contextName: contextName, ls: int = ..., mbc: [float, float, float] = ..., scm: bool = ..., stb: bool = ..., ssc: bool = ..., ss: bool = ..., ssd: float = ..., sym: int = ..., e: bool = ...) -> bool | float:
    """polyCutUVCtx is undoable, queryable, and editable.
    
    Create a new context to cut UVs on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new cut facets context, then switch to it
        cmds.polyCutUVCtx('polyCutUVCtx1')
        cmds.setToolTo('polyCutUVCtx1')
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - loopSpeed (ls): Edit the speed of loop cutting.
        - mapBordersColor (mbc): Color of UV map border edges in 3d view.
        - showCheckerMap (scm): Display checker map.
        - showTextureBorders (stb): Display texture border edges.
        - showUVShellColoring (ssc): Turn on UV shell coloring or not.
        - steadyStroke (ss): Turn on steady stroke or not.
        - steadyStrokeDistance (ssd): The distance for steady stroke.
        - symmetry (sym): Symmetric modeling.
        - edit (e): Edit mode flag
    """
@overload #Overload for polyCutUVCtx in ['edit']
def polyCutUVCtx(contextName: contextName, loopSpeed: int = ..., ls: int = ..., mapBordersColor: [float, float, float] = ..., mbc: [float, float, float] = ..., showCheckerMap: bool = ..., scm: bool = ..., showTextureBorders: bool = ..., stb: bool = ..., showUVShellColoring: bool = ..., ssc: bool = ..., steadyStroke: bool = ..., ss: bool = ..., steadyStrokeDistance: float = ..., ssd: float = ..., symmetry: int = ..., sym: int = ..., edit: bool = ..., e: bool = ...) -> bool | float:
    """polyCutUVCtx is undoable, queryable, and editable.
    
    Create a new context to cut UVs on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new cut facets context, then switch to it
        cmds.polyCutUVCtx('polyCutUVCtx1')
        cmds.setToolTo('polyCutUVCtx1')
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - loopSpeed (ls): Edit the speed of loop cutting.
        - mapBordersColor (mbc): Color of UV map border edges in 3d view.
        - showCheckerMap (scm): Display checker map.
        - showTextureBorders (stb): Display texture border edges.
        - showUVShellColoring (ssc): Turn on UV shell coloring or not.
        - steadyStroke (ss): Turn on steady stroke or not.
        - steadyStrokeDistance (ssd): The distance for steady stroke.
        - symmetry (sym): Symmetric modeling.
        - edit (e): Edit mode flag
    """
