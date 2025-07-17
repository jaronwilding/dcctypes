"""Stub files for Display category in Maya commands, command: displayCull."""

from typing import Any, overload

@overload #Overload for displayCull in ['create']
def displayCull([objects]: [objects], backFaceCulling: bool = ...) -> None:
    """displayCull is undoable, queryable, and NOT editable.
    
    This command is responsible for setting the display culling property of back
    faces of surfaces.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.displayCull( bfc=True )
        cmds.displayCull( bfc=False )
        cmds.displayCull( q=True, bfc=True )
        # Returns 0 if the back-face-culling on the selected object is false.
        # Returns 1 if the back-face-culling on the selected object is true.
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - backFaceCulling (bfc): Enable/disable culling of back faces.
    """
@overload #Overload for displayCull in ['create']
def displayCull([objects]: [objects], bfc: bool = ...) -> None:
    """displayCull is undoable, queryable, and NOT editable.
    
    This command is responsible for setting the display culling property of back
    faces of surfaces.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.displayCull( bfc=True )
        cmds.displayCull( bfc=False )
        cmds.displayCull( q=True, bfc=True )
        # Returns 0 if the back-face-culling on the selected object is false.
        # Returns 1 if the back-face-culling on the selected object is true.
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - backFaceCulling (bfc): Enable/disable culling of back faces.
    """
@overload #Overload for displayCull in ['create']
def displayCull([objects]: [objects], backFaceCulling: bool = ..., bfc: bool = ...) -> None:
    """displayCull is undoable, queryable, and NOT editable.
    
    This command is responsible for setting the display culling property of back
    faces of surfaces.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.displayCull( bfc=True )
        cmds.displayCull( bfc=False )
        cmds.displayCull( q=True, bfc=True )
        # Returns 0 if the back-face-culling on the selected object is false.
        # Returns 1 if the back-face-culling on the selected object is true.
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - backFaceCulling (bfc): Enable/disable culling of back faces.
    """
@overload #Overload for displayCull in ['query']
def displayCull([objects]: [objects], backFaceCulling: bool = ..., query: bool = ...) -> None:
    """displayCull is undoable, queryable, and NOT editable.
    
    This command is responsible for setting the display culling property of back
    faces of surfaces.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.displayCull( bfc=True )
        cmds.displayCull( bfc=False )
        cmds.displayCull( q=True, bfc=True )
        # Returns 0 if the back-face-culling on the selected object is false.
        # Returns 1 if the back-face-culling on the selected object is true.
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - backFaceCulling (bfc): Enable/disable culling of back faces.
        - query (q): Query mode flag
    """
@overload #Overload for displayCull in ['query']
def displayCull([objects]: [objects], bfc: bool = ..., q: bool = ...) -> None:
    """displayCull is undoable, queryable, and NOT editable.
    
    This command is responsible for setting the display culling property of back
    faces of surfaces.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.displayCull( bfc=True )
        cmds.displayCull( bfc=False )
        cmds.displayCull( q=True, bfc=True )
        # Returns 0 if the back-face-culling on the selected object is false.
        # Returns 1 if the back-face-culling on the selected object is true.
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - backFaceCulling (bfc): Enable/disable culling of back faces.
        - query (q): Query mode flag
    """
@overload #Overload for displayCull in ['query']
def displayCull([objects]: [objects], backFaceCulling: bool = ..., bfc: bool = ..., query: bool = ..., q: bool = ...) -> None:
    """displayCull is undoable, queryable, and NOT editable.
    
    This command is responsible for setting the display culling property of back
    faces of surfaces.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.displayCull( bfc=True )
        cmds.displayCull( bfc=False )
        cmds.displayCull( q=True, bfc=True )
        # Returns 0 if the back-face-culling on the selected object is false.
        # Returns 1 if the back-face-culling on the selected object is true.
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - backFaceCulling (bfc): Enable/disable culling of back faces.
        - query (q): Query mode flag
    """
