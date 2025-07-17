"""Stub files for Contexts category in Maya commands, command: texLatticeDeformContext."""

from typing import Any, overload

@overload #Overload for texLatticeDeformContext in ['create']
def texLatticeDeformContext(contextName: contextName, envelope: float = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., latticeColumns: int = ..., latticeRows: int = ..., name: str = ..., showMoveManipulator: bool = ..., snapPixelMode: bool = ..., useBoundingRect: bool = ...) -> int | int | float | bool | bool:
    """texLatticeDeformContext is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform UV maps with
    lattice manipulator. This context only works in the texture UV editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.texLatticeDeformContext( 'latticeContext', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.  The maximum size lattice is restricted to 8 columns.
        - latticeRows (lr): Specifies the number of rows the lattice contains. The maximum size lattice is restricted to 8 rows.
        - name (n): If this is a tool command, name the tool appropriately.
        - showMoveManipulator (smm): Specifies whether show move manipulator in UV Editor
        - snapPixelMode (spm): Specifies the influenced uv points should be snapped to a pixel center or corner.
        - useBoundingRect (ubr): When constructing the lattice use the bounding box of the selected UVs for the extents of the lattice.  When this is disabled the extents of the marquee selections are used as the extents for the lattice.
    """
@overload #Overload for texLatticeDeformContext in ['create']
def texLatticeDeformContext(contextName: contextName, ev: float = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., lc: int = ..., lr: int = ..., n: str = ..., smm: bool = ..., spm: bool = ..., ubr: bool = ...) -> int | int | float | bool | bool:
    """texLatticeDeformContext is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform UV maps with
    lattice manipulator. This context only works in the texture UV editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.texLatticeDeformContext( 'latticeContext', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.  The maximum size lattice is restricted to 8 columns.
        - latticeRows (lr): Specifies the number of rows the lattice contains. The maximum size lattice is restricted to 8 rows.
        - name (n): If this is a tool command, name the tool appropriately.
        - showMoveManipulator (smm): Specifies whether show move manipulator in UV Editor
        - snapPixelMode (spm): Specifies the influenced uv points should be snapped to a pixel center or corner.
        - useBoundingRect (ubr): When constructing the lattice use the bounding box of the selected UVs for the extents of the lattice.  When this is disabled the extents of the marquee selections are used as the extents for the lattice.
    """
@overload #Overload for texLatticeDeformContext in ['create']
def texLatticeDeformContext(contextName: contextName, envelope: float = ..., ev: float = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., latticeColumns: int = ..., lc: int = ..., latticeRows: int = ..., lr: int = ..., name: str = ..., n: str = ..., showMoveManipulator: bool = ..., smm: bool = ..., snapPixelMode: bool = ..., spm: bool = ..., useBoundingRect: bool = ..., ubr: bool = ...) -> int | int | float | bool | bool:
    """texLatticeDeformContext is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform UV maps with
    lattice manipulator. This context only works in the texture UV editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.texLatticeDeformContext( 'latticeContext', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.  The maximum size lattice is restricted to 8 columns.
        - latticeRows (lr): Specifies the number of rows the lattice contains. The maximum size lattice is restricted to 8 rows.
        - name (n): If this is a tool command, name the tool appropriately.
        - showMoveManipulator (smm): Specifies whether show move manipulator in UV Editor
        - snapPixelMode (spm): Specifies the influenced uv points should be snapped to a pixel center or corner.
        - useBoundingRect (ubr): When constructing the lattice use the bounding box of the selected UVs for the extents of the lattice.  When this is disabled the extents of the marquee selections are used as the extents for the lattice.
    """
@overload #Overload for texLatticeDeformContext in ['query']
def texLatticeDeformContext(contextName: contextName, envelope: float = ..., image1: str = ..., image2: str = ..., image3: str = ..., latticeColumns: int = ..., latticeRows: int = ..., showMoveManipulator: bool = ..., snapPixelMode: bool = ..., useBoundingRect: bool = ..., query: bool = ...) -> int | int | float | bool | bool:
    """texLatticeDeformContext is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform UV maps with
    lattice manipulator. This context only works in the texture UV editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.texLatticeDeformContext( 'latticeContext', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.  The maximum size lattice is restricted to 8 columns.
        - latticeRows (lr): Specifies the number of rows the lattice contains. The maximum size lattice is restricted to 8 rows.
        - showMoveManipulator (smm): Specifies whether show move manipulator in UV Editor
        - snapPixelMode (spm): Specifies the influenced uv points should be snapped to a pixel center or corner.
        - useBoundingRect (ubr): When constructing the lattice use the bounding box of the selected UVs for the extents of the lattice.  When this is disabled the extents of the marquee selections are used as the extents for the lattice.
        - query (q): Query mode flag
    """
@overload #Overload for texLatticeDeformContext in ['query']
def texLatticeDeformContext(contextName: contextName, ev: float = ..., i1: str = ..., i2: str = ..., i3: str = ..., lc: int = ..., lr: int = ..., smm: bool = ..., spm: bool = ..., ubr: bool = ..., q: bool = ...) -> int | int | float | bool | bool:
    """texLatticeDeformContext is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform UV maps with
    lattice manipulator. This context only works in the texture UV editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.texLatticeDeformContext( 'latticeContext', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.  The maximum size lattice is restricted to 8 columns.
        - latticeRows (lr): Specifies the number of rows the lattice contains. The maximum size lattice is restricted to 8 rows.
        - showMoveManipulator (smm): Specifies whether show move manipulator in UV Editor
        - snapPixelMode (spm): Specifies the influenced uv points should be snapped to a pixel center or corner.
        - useBoundingRect (ubr): When constructing the lattice use the bounding box of the selected UVs for the extents of the lattice.  When this is disabled the extents of the marquee selections are used as the extents for the lattice.
        - query (q): Query mode flag
    """
@overload #Overload for texLatticeDeformContext in ['query']
def texLatticeDeformContext(contextName: contextName, envelope: float = ..., ev: float = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., latticeColumns: int = ..., lc: int = ..., latticeRows: int = ..., lr: int = ..., showMoveManipulator: bool = ..., smm: bool = ..., snapPixelMode: bool = ..., spm: bool = ..., useBoundingRect: bool = ..., ubr: bool = ..., query: bool = ..., q: bool = ...) -> int | int | float | bool | bool:
    """texLatticeDeformContext is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform UV maps with
    lattice manipulator. This context only works in the texture UV editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.texLatticeDeformContext( 'latticeContext', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.  The maximum size lattice is restricted to 8 columns.
        - latticeRows (lr): Specifies the number of rows the lattice contains. The maximum size lattice is restricted to 8 rows.
        - showMoveManipulator (smm): Specifies whether show move manipulator in UV Editor
        - snapPixelMode (spm): Specifies the influenced uv points should be snapped to a pixel center or corner.
        - useBoundingRect (ubr): When constructing the lattice use the bounding box of the selected UVs for the extents of the lattice.  When this is disabled the extents of the marquee selections are used as the extents for the lattice.
        - query (q): Query mode flag
    """
@overload #Overload for texLatticeDeformContext in ['edit']
def texLatticeDeformContext(contextName: contextName, envelope: float = ..., image1: str = ..., image2: str = ..., image3: str = ..., latticeColumns: int = ..., latticeRows: int = ..., showMoveManipulator: bool = ..., snapPixelMode: bool = ..., useBoundingRect: bool = ..., edit: bool = ...) -> int | int | float | bool | bool:
    """texLatticeDeformContext is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform UV maps with
    lattice manipulator. This context only works in the texture UV editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.texLatticeDeformContext( 'latticeContext', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.  The maximum size lattice is restricted to 8 columns.
        - latticeRows (lr): Specifies the number of rows the lattice contains. The maximum size lattice is restricted to 8 rows.
        - showMoveManipulator (smm): Specifies whether show move manipulator in UV Editor
        - snapPixelMode (spm): Specifies the influenced uv points should be snapped to a pixel center or corner.
        - useBoundingRect (ubr): When constructing the lattice use the bounding box of the selected UVs for the extents of the lattice.  When this is disabled the extents of the marquee selections are used as the extents for the lattice.
        - edit (e): Edit mode flag
    """
@overload #Overload for texLatticeDeformContext in ['edit']
def texLatticeDeformContext(contextName: contextName, ev: float = ..., i1: str = ..., i2: str = ..., i3: str = ..., lc: int = ..., lr: int = ..., smm: bool = ..., spm: bool = ..., ubr: bool = ..., e: bool = ...) -> int | int | float | bool | bool:
    """texLatticeDeformContext is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform UV maps with
    lattice manipulator. This context only works in the texture UV editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.texLatticeDeformContext( 'latticeContext', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.  The maximum size lattice is restricted to 8 columns.
        - latticeRows (lr): Specifies the number of rows the lattice contains. The maximum size lattice is restricted to 8 rows.
        - showMoveManipulator (smm): Specifies whether show move manipulator in UV Editor
        - snapPixelMode (spm): Specifies the influenced uv points should be snapped to a pixel center or corner.
        - useBoundingRect (ubr): When constructing the lattice use the bounding box of the selected UVs for the extents of the lattice.  When this is disabled the extents of the marquee selections are used as the extents for the lattice.
        - edit (e): Edit mode flag
    """
@overload #Overload for texLatticeDeformContext in ['edit']
def texLatticeDeformContext(contextName: contextName, envelope: float = ..., ev: float = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., latticeColumns: int = ..., lc: int = ..., latticeRows: int = ..., lr: int = ..., showMoveManipulator: bool = ..., smm: bool = ..., snapPixelMode: bool = ..., spm: bool = ..., useBoundingRect: bool = ..., ubr: bool = ..., edit: bool = ..., e: bool = ...) -> int | int | float | bool | bool:
    """texLatticeDeformContext is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform UV maps with
    lattice manipulator. This context only works in the texture UV editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.texLatticeDeformContext( 'latticeContext', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.  The maximum size lattice is restricted to 8 columns.
        - latticeRows (lr): Specifies the number of rows the lattice contains. The maximum size lattice is restricted to 8 rows.
        - showMoveManipulator (smm): Specifies whether show move manipulator in UV Editor
        - snapPixelMode (spm): Specifies the influenced uv points should be snapped to a pixel center or corner.
        - useBoundingRect (ubr): When constructing the lattice use the bounding box of the selected UVs for the extents of the lattice.  When this is disabled the extents of the marquee selections are used as the extents for the lattice.
        - edit (e): Edit mode flag
    """
