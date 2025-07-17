"""Stub files for Attributes category in Maya commands, command: listNodeTypes."""

from typing import Any, overload

@overload #Overload for listNodeTypes in ['create']
def listNodeTypes(string: str, exclude: str = ...) -> list[str]:
    """listNodeTypes is undoable, NOT queryable, and NOT editable.
    
    Lists dependency node types satisfying a specified classification string.
    
    See the 'getClassification' command for a list of the standard classification
    strings.

    Example:
    ```python
        import maya.cmds as cmds
        # List all shader types in the system
        cmds.listNodeTypes( 'shader' )
        # List all 2D textures that are also shaders
        cmds.listNodeTypes( 'texture/2D:shader' )
        # List all volume shading nodes that are neither utility nodes nor particle nodes
        cmds.listNodeTypes( 'shader/volume', ex='shader/volume/utility:shader/volume/particle' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - exclude (ex): Nodes that satisfies this exclude classification will be filtered out.
    """
@overload #Overload for listNodeTypes in ['create']
def listNodeTypes(string: str, ex: str = ...) -> list[str]:
    """listNodeTypes is undoable, NOT queryable, and NOT editable.
    
    Lists dependency node types satisfying a specified classification string.
    
    See the 'getClassification' command for a list of the standard classification
    strings.

    Example:
    ```python
        import maya.cmds as cmds
        # List all shader types in the system
        cmds.listNodeTypes( 'shader' )
        # List all 2D textures that are also shaders
        cmds.listNodeTypes( 'texture/2D:shader' )
        # List all volume shading nodes that are neither utility nodes nor particle nodes
        cmds.listNodeTypes( 'shader/volume', ex='shader/volume/utility:shader/volume/particle' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - exclude (ex): Nodes that satisfies this exclude classification will be filtered out.
    """
@overload #Overload for listNodeTypes in ['create']
def listNodeTypes(string: str, exclude: str = ..., ex: str = ...) -> list[str]:
    """listNodeTypes is undoable, NOT queryable, and NOT editable.
    
    Lists dependency node types satisfying a specified classification string.
    
    See the 'getClassification' command for a list of the standard classification
    strings.

    Example:
    ```python
        import maya.cmds as cmds
        # List all shader types in the system
        cmds.listNodeTypes( 'shader' )
        # List all 2D textures that are also shaders
        cmds.listNodeTypes( 'texture/2D:shader' )
        # List all volume shading nodes that are neither utility nodes nor particle nodes
        cmds.listNodeTypes( 'shader/volume', ex='shader/volume/utility:shader/volume/particle' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - exclude (ex): Nodes that satisfies this exclude classification will be filtered out.
    """
