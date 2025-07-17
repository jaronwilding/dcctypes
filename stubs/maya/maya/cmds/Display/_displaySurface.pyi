"""Stub files for Display category in Maya commands, command: displaySurface."""

from typing import Any, overload

@overload #Overload for displaySurface in ['query']
def displaySurface([objects...]: [objects...], flipNormals: bool = ..., twoSidedLighting: bool = ..., xRay: bool = ..., query: bool = ...) -> bool:
    """displaySurface is undoable, queryable, and NOT editable.
    
    This command toggles display options on the specified or active surfaces.
    Typically this command applies to NURBS or poly mesh surfaces and ignores
    other type of objects.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sphere(n='mySphere1')
        cmds.sphere(n='mySphere2')
        cmds.displaySurface( ['mySphere1', 'mySphere2'], two=False )
        cmds.displaySurface( xRay=True )
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - flipNormals (flp): flip normal direction on the surface
        - twoSidedLighting (two): toggle if the surface should be considered two-sided.  If it's single-sided, drawing and rendering may use single sided lighting and back face cull to improve performance.
        - xRay (x): toggle X ray mode (make surface transparent)
        - query (q): Query mode flag
    """
@overload #Overload for displaySurface in ['query']
def displaySurface([objects...]: [objects...], flp: bool = ..., two: bool = ..., x: bool = ..., q: bool = ...) -> bool:
    """displaySurface is undoable, queryable, and NOT editable.
    
    This command toggles display options on the specified or active surfaces.
    Typically this command applies to NURBS or poly mesh surfaces and ignores
    other type of objects.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sphere(n='mySphere1')
        cmds.sphere(n='mySphere2')
        cmds.displaySurface( ['mySphere1', 'mySphere2'], two=False )
        cmds.displaySurface( xRay=True )
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - flipNormals (flp): flip normal direction on the surface
        - twoSidedLighting (two): toggle if the surface should be considered two-sided.  If it's single-sided, drawing and rendering may use single sided lighting and back face cull to improve performance.
        - xRay (x): toggle X ray mode (make surface transparent)
        - query (q): Query mode flag
    """
@overload #Overload for displaySurface in ['query']
def displaySurface([objects...]: [objects...], flipNormals: bool = ..., flp: bool = ..., twoSidedLighting: bool = ..., two: bool = ..., xRay: bool = ..., x: bool = ..., query: bool = ..., q: bool = ...) -> bool:
    """displaySurface is undoable, queryable, and NOT editable.
    
    This command toggles display options on the specified or active surfaces.
    Typically this command applies to NURBS or poly mesh surfaces and ignores
    other type of objects.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sphere(n='mySphere1')
        cmds.sphere(n='mySphere2')
        cmds.displaySurface( ['mySphere1', 'mySphere2'], two=False )
        cmds.displaySurface( xRay=True )
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - flipNormals (flp): flip normal direction on the surface
        - twoSidedLighting (two): toggle if the surface should be considered two-sided.  If it's single-sided, drawing and rendering may use single sided lighting and back face cull to improve performance.
        - xRay (x): toggle X ray mode (make surface transparent)
        - query (q): Query mode flag
    """
