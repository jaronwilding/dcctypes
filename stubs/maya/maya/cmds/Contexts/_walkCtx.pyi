"""Stub files for Contexts category in Maya commands, command: walkCtx."""

from typing import Any, overload

@overload #Overload for walkCtx in ['create']
def walkCtx(alternateContext: bool = ..., crouchCount: float = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., toolName: str = ..., walkHeight: float = ..., walkSensitivity: float = ..., walkSpeed: float = ..., walkToolHud: bool = ...) -> str:
    """walkCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a walk context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.walkCtx( 'walkContext', ws=2.0 )
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - crouchCount (wcc): The camera crouch count.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - toolName (tn): Name of the specific tool to which this command refers.
        - walkHeight (wh): The camera initial height.
        - walkSensitivity (wsv): The camera rotate sensitivity.
        - walkSpeed (ws): The camera move speed.
        - walkToolHud (wth): Control whether show walk tool HUD.
    """
@overload #Overload for walkCtx in ['create']
def walkCtx(ac: bool = ..., wcc: float = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., tn: str = ..., wh: float = ..., wsv: float = ..., ws: float = ..., wth: bool = ...) -> str:
    """walkCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a walk context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.walkCtx( 'walkContext', ws=2.0 )
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - crouchCount (wcc): The camera crouch count.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - toolName (tn): Name of the specific tool to which this command refers.
        - walkHeight (wh): The camera initial height.
        - walkSensitivity (wsv): The camera rotate sensitivity.
        - walkSpeed (ws): The camera move speed.
        - walkToolHud (wth): Control whether show walk tool HUD.
    """
@overload #Overload for walkCtx in ['create']
def walkCtx(alternateContext: bool = ..., ac: bool = ..., crouchCount: float = ..., wcc: float = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., toolName: str = ..., tn: str = ..., walkHeight: float = ..., wh: float = ..., walkSensitivity: float = ..., wsv: float = ..., walkSpeed: float = ..., ws: float = ..., walkToolHud: bool = ..., wth: bool = ...) -> str:
    """walkCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a walk context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.walkCtx( 'walkContext', ws=2.0 )
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - crouchCount (wcc): The camera crouch count.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - toolName (tn): Name of the specific tool to which this command refers.
        - walkHeight (wh): The camera initial height.
        - walkSensitivity (wsv): The camera rotate sensitivity.
        - walkSpeed (ws): The camera move speed.
        - walkToolHud (wth): Control whether show walk tool HUD.
    """
@overload #Overload for walkCtx in ['query']
def walkCtx(alternateContext: bool = ..., crouchCount: float = ..., image1: str = ..., image2: str = ..., image3: str = ..., toolName: str = ..., walkHeight: float = ..., walkSensitivity: float = ..., walkSpeed: float = ..., walkToolHud: bool = ..., query: bool = ...) -> str:
    """walkCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a walk context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.walkCtx( 'walkContext', ws=2.0 )
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - crouchCount (wcc): The camera crouch count.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - walkHeight (wh): The camera initial height.
        - walkSensitivity (wsv): The camera rotate sensitivity.
        - walkSpeed (ws): The camera move speed.
        - walkToolHud (wth): Control whether show walk tool HUD.
        - query (q): Query mode flag
    """
@overload #Overload for walkCtx in ['query']
def walkCtx(ac: bool = ..., wcc: float = ..., i1: str = ..., i2: str = ..., i3: str = ..., tn: str = ..., wh: float = ..., wsv: float = ..., ws: float = ..., wth: bool = ..., q: bool = ...) -> str:
    """walkCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a walk context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.walkCtx( 'walkContext', ws=2.0 )
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - crouchCount (wcc): The camera crouch count.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - walkHeight (wh): The camera initial height.
        - walkSensitivity (wsv): The camera rotate sensitivity.
        - walkSpeed (ws): The camera move speed.
        - walkToolHud (wth): Control whether show walk tool HUD.
        - query (q): Query mode flag
    """
@overload #Overload for walkCtx in ['query']
def walkCtx(alternateContext: bool = ..., ac: bool = ..., crouchCount: float = ..., wcc: float = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., toolName: str = ..., tn: str = ..., walkHeight: float = ..., wh: float = ..., walkSensitivity: float = ..., wsv: float = ..., walkSpeed: float = ..., ws: float = ..., walkToolHud: bool = ..., wth: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """walkCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a walk context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.walkCtx( 'walkContext', ws=2.0 )
    ```

    ---
    - Args:
        - alternateContext (ac): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        - crouchCount (wcc): The camera crouch count.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - toolName (tn): Name of the specific tool to which this command refers.
        - walkHeight (wh): The camera initial height.
        - walkSensitivity (wsv): The camera rotate sensitivity.
        - walkSpeed (ws): The camera move speed.
        - walkToolHud (wth): Control whether show walk tool HUD.
        - query (q): Query mode flag
    """
@overload #Overload for walkCtx in ['edit']
def walkCtx(crouchCount: float = ..., image1: str = ..., image2: str = ..., image3: str = ..., walkHeight: float = ..., walkSensitivity: float = ..., walkSpeed: float = ..., walkToolHud: bool = ..., edit: bool = ...) -> str:
    """walkCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a walk context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.walkCtx( 'walkContext', ws=2.0 )
    ```

    ---
    - Args:
        - crouchCount (wcc): The camera crouch count.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - walkHeight (wh): The camera initial height.
        - walkSensitivity (wsv): The camera rotate sensitivity.
        - walkSpeed (ws): The camera move speed.
        - walkToolHud (wth): Control whether show walk tool HUD.
        - edit (e): Edit mode flag
    """
@overload #Overload for walkCtx in ['edit']
def walkCtx(wcc: float = ..., i1: str = ..., i2: str = ..., i3: str = ..., wh: float = ..., wsv: float = ..., ws: float = ..., wth: bool = ..., e: bool = ...) -> str:
    """walkCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a walk context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.walkCtx( 'walkContext', ws=2.0 )
    ```

    ---
    - Args:
        - crouchCount (wcc): The camera crouch count.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - walkHeight (wh): The camera initial height.
        - walkSensitivity (wsv): The camera rotate sensitivity.
        - walkSpeed (ws): The camera move speed.
        - walkToolHud (wth): Control whether show walk tool HUD.
        - edit (e): Edit mode flag
    """
@overload #Overload for walkCtx in ['edit']
def walkCtx(crouchCount: float = ..., wcc: float = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., walkHeight: float = ..., wh: float = ..., walkSensitivity: float = ..., wsv: float = ..., walkSpeed: float = ..., ws: float = ..., walkToolHud: bool = ..., wth: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """walkCtx is undoable, queryable, and editable.
    
    This command can be used to create, edit, or query a walk context.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.walkCtx( 'walkContext', ws=2.0 )
    ```

    ---
    - Args:
        - crouchCount (wcc): The camera crouch count.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - walkHeight (wh): The camera initial height.
        - walkSensitivity (wsv): The camera rotate sensitivity.
        - walkSpeed (ws): The camera move speed.
        - walkToolHud (wth): Control whether show walk tool HUD.
        - edit (e): Edit mode flag
    """
