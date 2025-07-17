"""Stub files for Contexts category in Maya commands, command: texWinToolCtx."""

from typing import Any, overload

@overload #Overload for texWinToolCtx in ['create']
def texWinToolCtx(alternateContext: bool = ..., boxzoom: bool = ..., dolly: bool = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., toolName: str = ..., track: bool = ...) -> str:
    """texWinToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the texture window.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new texture window tool context, set this tool to dolly in the texture window, then switch to it
        cmds.texWinToolCtx('texWinToolCtx1', do=True)
        cmds.setToolTo('texWinToolCtx1')
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
@overload #Overload for texWinToolCtx in ['create']
def texWinToolCtx(ac: bool = ..., bz: bool = ..., do: bool = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., tn: str = ..., tr: bool = ...) -> str:
    """texWinToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the texture window.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new texture window tool context, set this tool to dolly in the texture window, then switch to it
        cmds.texWinToolCtx('texWinToolCtx1', do=True)
        cmds.setToolTo('texWinToolCtx1')
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
@overload #Overload for texWinToolCtx in ['create']
def texWinToolCtx(alternateContext: bool = ..., ac: bool = ..., boxzoom: bool = ..., bz: bool = ..., dolly: bool = ..., do: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., toolName: str = ..., tn: str = ..., track: bool = ..., tr: bool = ...) -> str:
    """texWinToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the texture window.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new texture window tool context, set this tool to dolly in the texture window, then switch to it
        cmds.texWinToolCtx('texWinToolCtx1', do=True)
        cmds.setToolTo('texWinToolCtx1')
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
@overload #Overload for texWinToolCtx in ['query']
def texWinToolCtx(alternateContext: bool = ..., boxzoom: bool = ..., dolly: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., toolName: str = ..., track: bool = ..., query: bool = ...) -> str:
    """texWinToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the texture window.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new texture window tool context, set this tool to dolly in the texture window, then switch to it
        cmds.texWinToolCtx('texWinToolCtx1', do=True)
        cmds.setToolTo('texWinToolCtx1')
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
@overload #Overload for texWinToolCtx in ['query']
def texWinToolCtx(ac: bool = ..., bz: bool = ..., do: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., tn: str = ..., tr: bool = ..., q: bool = ...) -> str:
    """texWinToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the texture window.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new texture window tool context, set this tool to dolly in the texture window, then switch to it
        cmds.texWinToolCtx('texWinToolCtx1', do=True)
        cmds.setToolTo('texWinToolCtx1')
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
@overload #Overload for texWinToolCtx in ['query']
def texWinToolCtx(alternateContext: bool = ..., ac: bool = ..., boxzoom: bool = ..., bz: bool = ..., dolly: bool = ..., do: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., toolName: str = ..., tn: str = ..., track: bool = ..., tr: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """texWinToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the texture window.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new texture window tool context, set this tool to dolly in the texture window, then switch to it
        cmds.texWinToolCtx('texWinToolCtx1', do=True)
        cmds.setToolTo('texWinToolCtx1')
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
@overload #Overload for texWinToolCtx in ['edit']
def texWinToolCtx(boxzoom: bool = ..., dolly: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., track: bool = ..., edit: bool = ...) -> str:
    """texWinToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the texture window.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new texture window tool context, set this tool to dolly in the texture window, then switch to it
        cmds.texWinToolCtx('texWinToolCtx1', do=True)
        cmds.setToolTo('texWinToolCtx1')
    ```

    ---
    - Args:
        - boxzoom (bz): Perform Box Zoom
        - dolly (do): Dollies the view
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - track (tr): Tracks the view
        - edit (e): Edit mode flag
    """
@overload #Overload for texWinToolCtx in ['edit']
def texWinToolCtx(bz: bool = ..., do: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., tr: bool = ..., e: bool = ...) -> str:
    """texWinToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the texture window.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new texture window tool context, set this tool to dolly in the texture window, then switch to it
        cmds.texWinToolCtx('texWinToolCtx1', do=True)
        cmds.setToolTo('texWinToolCtx1')
    ```

    ---
    - Args:
        - boxzoom (bz): Perform Box Zoom
        - dolly (do): Dollies the view
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - track (tr): Tracks the view
        - edit (e): Edit mode flag
    """
@overload #Overload for texWinToolCtx in ['edit']
def texWinToolCtx(boxzoom: bool = ..., bz: bool = ..., dolly: bool = ..., do: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., track: bool = ..., tr: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """texWinToolCtx is undoable, queryable, and editable.
    
    This class creates a context for the View Tools "track", "dolly", and "box
    zoom" in the texture window.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new texture window tool context, set this tool to dolly in the texture window, then switch to it
        cmds.texWinToolCtx('texWinToolCtx1', do=True)
        cmds.setToolTo('texWinToolCtx1')
    ```

    ---
    - Args:
        - boxzoom (bz): Perform Box Zoom
        - dolly (do): Dollies the view
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - track (tr): Tracks the view
        - edit (e): Edit mode flag
    """
