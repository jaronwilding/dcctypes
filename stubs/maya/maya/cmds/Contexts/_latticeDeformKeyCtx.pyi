"""Stub files for Contexts category in Maya commands, command: latticeDeformKeyCtx."""

from typing import Any, overload

@overload #Overload for latticeDeformKeyCtx in ['create']
def latticeDeformKeyCtx(contextName: contextName, exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.latticeDeformKeyCtx( 'latticeContex', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for latticeDeformKeyCtx in ['create']
def latticeDeformKeyCtx(contextName: contextName, ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.latticeDeformKeyCtx( 'latticeContex', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for latticeDeformKeyCtx in ['create']
def latticeDeformKeyCtx(contextName: contextName, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.latticeDeformKeyCtx( 'latticeContex', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for latticeDeformKeyCtx in ['query']
def latticeDeformKeyCtx(contextName: contextName, envelope: float = ..., image1: str = ..., image2: str = ..., image3: str = ..., latticeColumns: int = ..., latticeRows: int = ..., scaleLatticePts: bool = ..., query: bool = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.latticeDeformKeyCtx( 'latticeContex', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.
        - latticeRows (lr): Specifies the number of rows the lattice contains.
        - scaleLatticePts (slp): Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'
        - query (q): Query mode flag
    """
@overload #Overload for latticeDeformKeyCtx in ['query']
def latticeDeformKeyCtx(contextName: contextName, ev: float = ..., i1: str = ..., i2: str = ..., i3: str = ..., lc: int = ..., lr: int = ..., slp: bool = ..., q: bool = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.latticeDeformKeyCtx( 'latticeContex', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.
        - latticeRows (lr): Specifies the number of rows the lattice contains.
        - scaleLatticePts (slp): Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'
        - query (q): Query mode flag
    """
@overload #Overload for latticeDeformKeyCtx in ['query']
def latticeDeformKeyCtx(contextName: contextName, envelope: float = ..., ev: float = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., latticeColumns: int = ..., lc: int = ..., latticeRows: int = ..., lr: int = ..., scaleLatticePts: bool = ..., slp: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.latticeDeformKeyCtx( 'latticeContex', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.
        - latticeRows (lr): Specifies the number of rows the lattice contains.
        - scaleLatticePts (slp): Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'
        - query (q): Query mode flag
    """
@overload #Overload for latticeDeformKeyCtx in ['edit']
def latticeDeformKeyCtx(contextName: contextName, envelope: float = ..., image1: str = ..., image2: str = ..., image3: str = ..., latticeColumns: int = ..., latticeRows: int = ..., scaleLatticePts: bool = ..., edit: bool = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.latticeDeformKeyCtx( 'latticeContex', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.
        - latticeRows (lr): Specifies the number of rows the lattice contains.
        - scaleLatticePts (slp): Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'
        - edit (e): Edit mode flag
    """
@overload #Overload for latticeDeformKeyCtx in ['edit']
def latticeDeformKeyCtx(contextName: contextName, ev: float = ..., i1: str = ..., i2: str = ..., i3: str = ..., lc: int = ..., lr: int = ..., slp: bool = ..., e: bool = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.latticeDeformKeyCtx( 'latticeContex', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.
        - latticeRows (lr): Specifies the number of rows the lattice contains.
        - scaleLatticePts (slp): Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'
        - edit (e): Edit mode flag
    """
@overload #Overload for latticeDeformKeyCtx in ['edit']
def latticeDeformKeyCtx(contextName: contextName, envelope: float = ..., ev: float = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., latticeColumns: int = ..., lc: int = ..., latticeRows: int = ..., lr: int = ..., scaleLatticePts: bool = ..., slp: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a lattice manipulator with 4 x 4 lattice.
        #
        cmds.latticeDeformKeyCtx( 'latticeContex', latticeColumns=4, latticeRows=4 )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.
        - latticeRows (lr): Specifies the number of rows the lattice contains.
        - scaleLatticePts (slp): Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'
        - edit (e): Edit mode flag
    """
