"""Stub files for Contexts category in Maya commands, command: wrinkleContext."""

from typing import Any, overload

@overload #Overload for wrinkleContext in ['create']
def wrinkleContext(string: str, branchCount: int = ..., branchDepth: int = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., randomness: linear = ..., style: str = ..., thickness: linear = ..., wrinkleCount: int = ..., wrinkleIntensity: linear = ...) -> str:
    """wrinkleContext is undoable, queryable, and editable.
    
    This command creates a context that creates wrinkles.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wrinkleContext( 'wrinkleCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - branchCount (brc): Set the number of branches spawned from a crease for radial wrinkles. Default is 2.
        - branchDepth (bd): Set the depth of branching for radial wrinkles. Defaults to 0.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - randomness (rnd): Set the deviation of the wrinkle creases from straight lines and other elements of the wrinkle structure. Defaults to 0.2.
        - style (st): Set the wrinkle characteristic shape."lines"|"radial"|"custom. Default is "radial".
        - thickness (th): Set the thickness of wrinkle creases by setting the dropoff distance on the underlying wires.
        - wrinkleCount (wc): Set the number of wrinkle creases. Default is 3.
        - wrinkleIntensity (wi): Set the depth intensity of the wrinkle furrows. Defaults to 0.5.
    """
@overload #Overload for wrinkleContext in ['create']
def wrinkleContext(string: str, brc: int = ..., bd: int = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., rnd: linear = ..., st: str = ..., th: linear = ..., wc: int = ..., wi: linear = ...) -> str:
    """wrinkleContext is undoable, queryable, and editable.
    
    This command creates a context that creates wrinkles.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wrinkleContext( 'wrinkleCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - branchCount (brc): Set the number of branches spawned from a crease for radial wrinkles. Default is 2.
        - branchDepth (bd): Set the depth of branching for radial wrinkles. Defaults to 0.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - randomness (rnd): Set the deviation of the wrinkle creases from straight lines and other elements of the wrinkle structure. Defaults to 0.2.
        - style (st): Set the wrinkle characteristic shape."lines"|"radial"|"custom. Default is "radial".
        - thickness (th): Set the thickness of wrinkle creases by setting the dropoff distance on the underlying wires.
        - wrinkleCount (wc): Set the number of wrinkle creases. Default is 3.
        - wrinkleIntensity (wi): Set the depth intensity of the wrinkle furrows. Defaults to 0.5.
    """
@overload #Overload for wrinkleContext in ['create']
def wrinkleContext(string: str, branchCount: int = ..., brc: int = ..., branchDepth: int = ..., bd: int = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., randomness: linear = ..., rnd: linear = ..., style: str = ..., st: str = ..., thickness: linear = ..., th: linear = ..., wrinkleCount: int = ..., wc: int = ..., wrinkleIntensity: linear = ..., wi: linear = ...) -> str:
    """wrinkleContext is undoable, queryable, and editable.
    
    This command creates a context that creates wrinkles.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wrinkleContext( 'wrinkleCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - branchCount (brc): Set the number of branches spawned from a crease for radial wrinkles. Default is 2.
        - branchDepth (bd): Set the depth of branching for radial wrinkles. Defaults to 0.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - randomness (rnd): Set the deviation of the wrinkle creases from straight lines and other elements of the wrinkle structure. Defaults to 0.2.
        - style (st): Set the wrinkle characteristic shape."lines"|"radial"|"custom. Default is "radial".
        - thickness (th): Set the thickness of wrinkle creases by setting the dropoff distance on the underlying wires.
        - wrinkleCount (wc): Set the number of wrinkle creases. Default is 3.
        - wrinkleIntensity (wi): Set the depth intensity of the wrinkle furrows. Defaults to 0.5.
    """
@overload #Overload for wrinkleContext in ['query']
def wrinkleContext(string: str, branchCount: int = ..., branchDepth: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., randomness: linear = ..., style: str = ..., thickness: linear = ..., wrinkleCount: int = ..., wrinkleIntensity: linear = ..., query: bool = ...) -> str:
    """wrinkleContext is undoable, queryable, and editable.
    
    This command creates a context that creates wrinkles.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wrinkleContext( 'wrinkleCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - branchCount (brc): Set the number of branches spawned from a crease for radial wrinkles. Default is 2.
        - branchDepth (bd): Set the depth of branching for radial wrinkles. Defaults to 0.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - randomness (rnd): Set the deviation of the wrinkle creases from straight lines and other elements of the wrinkle structure. Defaults to 0.2.
        - style (st): Set the wrinkle characteristic shape."lines"|"radial"|"custom. Default is "radial".
        - thickness (th): Set the thickness of wrinkle creases by setting the dropoff distance on the underlying wires.
        - wrinkleCount (wc): Set the number of wrinkle creases. Default is 3.
        - wrinkleIntensity (wi): Set the depth intensity of the wrinkle furrows. Defaults to 0.5.
        - query (q): Query mode flag
    """
@overload #Overload for wrinkleContext in ['query']
def wrinkleContext(string: str, brc: int = ..., bd: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., rnd: linear = ..., st: str = ..., th: linear = ..., wc: int = ..., wi: linear = ..., q: bool = ...) -> str:
    """wrinkleContext is undoable, queryable, and editable.
    
    This command creates a context that creates wrinkles.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wrinkleContext( 'wrinkleCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - branchCount (brc): Set the number of branches spawned from a crease for radial wrinkles. Default is 2.
        - branchDepth (bd): Set the depth of branching for radial wrinkles. Defaults to 0.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - randomness (rnd): Set the deviation of the wrinkle creases from straight lines and other elements of the wrinkle structure. Defaults to 0.2.
        - style (st): Set the wrinkle characteristic shape."lines"|"radial"|"custom. Default is "radial".
        - thickness (th): Set the thickness of wrinkle creases by setting the dropoff distance on the underlying wires.
        - wrinkleCount (wc): Set the number of wrinkle creases. Default is 3.
        - wrinkleIntensity (wi): Set the depth intensity of the wrinkle furrows. Defaults to 0.5.
        - query (q): Query mode flag
    """
@overload #Overload for wrinkleContext in ['query']
def wrinkleContext(string: str, branchCount: int = ..., brc: int = ..., branchDepth: int = ..., bd: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., randomness: linear = ..., rnd: linear = ..., style: str = ..., st: str = ..., thickness: linear = ..., th: linear = ..., wrinkleCount: int = ..., wc: int = ..., wrinkleIntensity: linear = ..., wi: linear = ..., query: bool = ..., q: bool = ...) -> str:
    """wrinkleContext is undoable, queryable, and editable.
    
    This command creates a context that creates wrinkles.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wrinkleContext( 'wrinkleCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - branchCount (brc): Set the number of branches spawned from a crease for radial wrinkles. Default is 2.
        - branchDepth (bd): Set the depth of branching for radial wrinkles. Defaults to 0.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - randomness (rnd): Set the deviation of the wrinkle creases from straight lines and other elements of the wrinkle structure. Defaults to 0.2.
        - style (st): Set the wrinkle characteristic shape."lines"|"radial"|"custom. Default is "radial".
        - thickness (th): Set the thickness of wrinkle creases by setting the dropoff distance on the underlying wires.
        - wrinkleCount (wc): Set the number of wrinkle creases. Default is 3.
        - wrinkleIntensity (wi): Set the depth intensity of the wrinkle furrows. Defaults to 0.5.
        - query (q): Query mode flag
    """
@overload #Overload for wrinkleContext in ['edit']
def wrinkleContext(string: str, branchCount: int = ..., branchDepth: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., randomness: linear = ..., style: str = ..., thickness: linear = ..., wrinkleCount: int = ..., wrinkleIntensity: linear = ..., edit: bool = ...) -> str:
    """wrinkleContext is undoable, queryable, and editable.
    
    This command creates a context that creates wrinkles.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wrinkleContext( 'wrinkleCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - branchCount (brc): Set the number of branches spawned from a crease for radial wrinkles. Default is 2.
        - branchDepth (bd): Set the depth of branching for radial wrinkles. Defaults to 0.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - randomness (rnd): Set the deviation of the wrinkle creases from straight lines and other elements of the wrinkle structure. Defaults to 0.2.
        - style (st): Set the wrinkle characteristic shape."lines"|"radial"|"custom. Default is "radial".
        - thickness (th): Set the thickness of wrinkle creases by setting the dropoff distance on the underlying wires.
        - wrinkleCount (wc): Set the number of wrinkle creases. Default is 3.
        - wrinkleIntensity (wi): Set the depth intensity of the wrinkle furrows. Defaults to 0.5.
        - edit (e): Edit mode flag
    """
@overload #Overload for wrinkleContext in ['edit']
def wrinkleContext(string: str, brc: int = ..., bd: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., rnd: linear = ..., st: str = ..., th: linear = ..., wc: int = ..., wi: linear = ..., e: bool = ...) -> str:
    """wrinkleContext is undoable, queryable, and editable.
    
    This command creates a context that creates wrinkles.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wrinkleContext( 'wrinkleCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - branchCount (brc): Set the number of branches spawned from a crease for radial wrinkles. Default is 2.
        - branchDepth (bd): Set the depth of branching for radial wrinkles. Defaults to 0.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - randomness (rnd): Set the deviation of the wrinkle creases from straight lines and other elements of the wrinkle structure. Defaults to 0.2.
        - style (st): Set the wrinkle characteristic shape."lines"|"radial"|"custom. Default is "radial".
        - thickness (th): Set the thickness of wrinkle creases by setting the dropoff distance on the underlying wires.
        - wrinkleCount (wc): Set the number of wrinkle creases. Default is 3.
        - wrinkleIntensity (wi): Set the depth intensity of the wrinkle furrows. Defaults to 0.5.
        - edit (e): Edit mode flag
    """
@overload #Overload for wrinkleContext in ['edit']
def wrinkleContext(string: str, branchCount: int = ..., brc: int = ..., branchDepth: int = ..., bd: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., randomness: linear = ..., rnd: linear = ..., style: str = ..., st: str = ..., thickness: linear = ..., th: linear = ..., wrinkleCount: int = ..., wc: int = ..., wrinkleIntensity: linear = ..., wi: linear = ..., edit: bool = ..., e: bool = ...) -> str:
    """wrinkleContext is undoable, queryable, and editable.
    
    This command creates a context that creates wrinkles.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wrinkleContext( 'wrinkleCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - branchCount (brc): Set the number of branches spawned from a crease for radial wrinkles. Default is 2.
        - branchDepth (bd): Set the depth of branching for radial wrinkles. Defaults to 0.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - randomness (rnd): Set the deviation of the wrinkle creases from straight lines and other elements of the wrinkle structure. Defaults to 0.2.
        - style (st): Set the wrinkle characteristic shape."lines"|"radial"|"custom. Default is "radial".
        - thickness (th): Set the thickness of wrinkle creases by setting the dropoff distance on the underlying wires.
        - wrinkleCount (wc): Set the number of wrinkle creases. Default is 3.
        - wrinkleIntensity (wi): Set the depth intensity of the wrinkle furrows. Defaults to 0.5.
        - edit (e): Edit mode flag
    """
