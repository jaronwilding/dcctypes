"""Stub files for Contexts category in Maya commands, command: view2dToolCtx."""

from typing import Any, overload

@overload #Overload for view2dToolCtx in ['create']
def view2dToolCtx(alternateContext: bool = ..., boxzoom: bool = ..., dolly: bool = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., toolName: str = ..., track: bool = ...) -> str:
    """view2dToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the Hypergraph.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new view2dTool context, set it to do dolly in the Hypergraph window, then switch to this tool
        cmds.view2dToolCtx('view2dToolCtx1', dolly=True)
        cmds.setToolTo('view2dToolCtx1')
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - boxzoom (bz): Perform Box Zoom
        - dolly (do): Dollies the view
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - toolName (tn): Name of the specific tool to which this command refers.
        - track (tr): Tracks the view
    """
@overload #Overload for view2dToolCtx in ['create']
def view2dToolCtx(ac: bool = ..., bz: bool = ..., do: bool = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., tn: str = ..., tr: bool = ...) -> str:
    """view2dToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the Hypergraph.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new view2dTool context, set it to do dolly in the Hypergraph window, then switch to this tool
        cmds.view2dToolCtx('view2dToolCtx1', dolly=True)
        cmds.setToolTo('view2dToolCtx1')
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - boxzoom (bz): Perform Box Zoom
        - dolly (do): Dollies the view
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - toolName (tn): Name of the specific tool to which this command refers.
        - track (tr): Tracks the view
    """
@overload #Overload for view2dToolCtx in ['create']
def view2dToolCtx(alternateContext: bool = ..., ac: bool = ..., boxzoom: bool = ..., bz: bool = ..., dolly: bool = ..., do: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., toolName: str = ..., tn: str = ..., track: bool = ..., tr: bool = ...) -> str:
    """view2dToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the Hypergraph.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new view2dTool context, set it to do dolly in the Hypergraph window, then switch to this tool
        cmds.view2dToolCtx('view2dToolCtx1', dolly=True)
        cmds.setToolTo('view2dToolCtx1')
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - boxzoom (bz): Perform Box Zoom
        - dolly (do): Dollies the view
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - toolName (tn): Name of the specific tool to which this command refers.
        - track (tr): Tracks the view
    """
@overload #Overload for view2dToolCtx in ['query']
def view2dToolCtx(alternateContext: bool = ..., boxzoom: bool = ..., dolly: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., toolName: str = ..., track: bool = ..., query: bool = ...) -> str:
    """view2dToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the Hypergraph.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new view2dTool context, set it to do dolly in the Hypergraph window, then switch to this tool
        cmds.view2dToolCtx('view2dToolCtx1', dolly=True)
        cmds.setToolTo('view2dToolCtx1')
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - boxzoom (bz): Perform Box Zoom
        - dolly (do): Dollies the view
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - track (tr): Tracks the view
        - query (q): Query mode flag
    """
@overload #Overload for view2dToolCtx in ['query']
def view2dToolCtx(ac: bool = ..., bz: bool = ..., do: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., tn: str = ..., tr: bool = ..., q: bool = ...) -> str:
    """view2dToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the Hypergraph.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new view2dTool context, set it to do dolly in the Hypergraph window, then switch to this tool
        cmds.view2dToolCtx('view2dToolCtx1', dolly=True)
        cmds.setToolTo('view2dToolCtx1')
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - boxzoom (bz): Perform Box Zoom
        - dolly (do): Dollies the view
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - track (tr): Tracks the view
        - query (q): Query mode flag
    """
@overload #Overload for view2dToolCtx in ['query']
def view2dToolCtx(alternateContext: bool = ..., ac: bool = ..., boxzoom: bool = ..., bz: bool = ..., dolly: bool = ..., do: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., toolName: str = ..., tn: str = ..., track: bool = ..., tr: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """view2dToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the Hypergraph.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new view2dTool context, set it to do dolly in the Hypergraph window, then switch to this tool
        cmds.view2dToolCtx('view2dToolCtx1', dolly=True)
        cmds.setToolTo('view2dToolCtx1')
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - boxzoom (bz): Perform Box Zoom
        - dolly (do): Dollies the view
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - track (tr): Tracks the view
        - query (q): Query mode flag
    """
@overload #Overload for view2dToolCtx in ['edit']
def view2dToolCtx(image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> str:
    """view2dToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the Hypergraph.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new view2dTool context, set it to do dolly in the Hypergraph window, then switch to this tool
        cmds.view2dToolCtx('view2dToolCtx1', dolly=True)
        cmds.setToolTo('view2dToolCtx1')
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for view2dToolCtx in ['edit']
def view2dToolCtx(i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> str:
    """view2dToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the Hypergraph.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new view2dTool context, set it to do dolly in the Hypergraph window, then switch to this tool
        cmds.view2dToolCtx('view2dToolCtx1', dolly=True)
        cmds.setToolTo('view2dToolCtx1')
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for view2dToolCtx in ['edit']
def view2dToolCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """view2dToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the Hypergraph.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new view2dTool context, set it to do dolly in the Hypergraph window, then switch to this tool
        cmds.view2dToolCtx('view2dToolCtx1', dolly=True)
        cmds.setToolTo('view2dToolCtx1')
    ```

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
