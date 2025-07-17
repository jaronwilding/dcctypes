"""Stub files for Contexts category in Maya commands, command: sculptMeshCacheChangeCloneSource."""

from typing import Any, overload

@overload #Overload for sculptMeshCacheChangeCloneSource in ['create']
def sculptMeshCacheChangeCloneSource(blendShape: str = ..., target: str = ...) -> None:
    """sculptMeshCacheChangeCloneSource is undoable, queryable, and editable.
    
    This command changes the source blend shape and target for the clone target
    tool. Used internally for undo/redo, and should not be called directly.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sculptMeshCacheChangeCloneSource( bs='blendShape1', t='pSphere4' )
    ```

    ---
    - Args:
        - blendShape (bs): Set which blend shape should be used as the source when using the clone tool. When queried, returns the current blend shape name as a string.
        - target (t): Set which blend shape should be used as the target when using the clone tool. When queried, returns the current blend shape target name as a string.
    """
@overload #Overload for sculptMeshCacheChangeCloneSource in ['create']
def sculptMeshCacheChangeCloneSource(bs: str = ..., t: str = ...) -> None:
    """sculptMeshCacheChangeCloneSource is undoable, queryable, and editable.
    
    This command changes the source blend shape and target for the clone target
    tool. Used internally for undo/redo, and should not be called directly.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sculptMeshCacheChangeCloneSource( bs='blendShape1', t='pSphere4' )
    ```

    ---
    - Args:
        - blendShape (bs): Set which blend shape should be used as the source when using the clone tool. When queried, returns the current blend shape name as a string.
        - target (t): Set which blend shape should be used as the target when using the clone tool. When queried, returns the current blend shape target name as a string.
    """
@overload #Overload for sculptMeshCacheChangeCloneSource in ['create']
def sculptMeshCacheChangeCloneSource(blendShape: str = ..., bs: str = ..., target: str = ..., t: str = ...) -> None:
    """sculptMeshCacheChangeCloneSource is undoable, queryable, and editable.
    
    This command changes the source blend shape and target for the clone target
    tool. Used internally for undo/redo, and should not be called directly.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sculptMeshCacheChangeCloneSource( bs='blendShape1', t='pSphere4' )
    ```

    ---
    - Args:
        - blendShape (bs): Set which blend shape should be used as the source when using the clone tool. When queried, returns the current blend shape name as a string.
        - target (t): Set which blend shape should be used as the target when using the clone tool. When queried, returns the current blend shape target name as a string.
    """
@overload #Overload for sculptMeshCacheChangeCloneSource in ['query']
def sculptMeshCacheChangeCloneSource(blendShape: str = ..., target: str = ..., query: bool = ...) -> None:
    """sculptMeshCacheChangeCloneSource is undoable, queryable, and editable.
    
    This command changes the source blend shape and target for the clone target
    tool. Used internally for undo/redo, and should not be called directly.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sculptMeshCacheChangeCloneSource( bs='blendShape1', t='pSphere4' )
    ```

    ---
    - Args:
        - blendShape (bs): Set which blend shape should be used as the source when using the clone tool. When queried, returns the current blend shape name as a string.
        - target (t): Set which blend shape should be used as the target when using the clone tool. When queried, returns the current blend shape target name as a string.
        - query (q): Query mode flag
    """
@overload #Overload for sculptMeshCacheChangeCloneSource in ['query']
def sculptMeshCacheChangeCloneSource(bs: str = ..., t: str = ..., q: bool = ...) -> None:
    """sculptMeshCacheChangeCloneSource is undoable, queryable, and editable.
    
    This command changes the source blend shape and target for the clone target
    tool. Used internally for undo/redo, and should not be called directly.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sculptMeshCacheChangeCloneSource( bs='blendShape1', t='pSphere4' )
    ```

    ---
    - Args:
        - blendShape (bs): Set which blend shape should be used as the source when using the clone tool. When queried, returns the current blend shape name as a string.
        - target (t): Set which blend shape should be used as the target when using the clone tool. When queried, returns the current blend shape target name as a string.
        - query (q): Query mode flag
    """
@overload #Overload for sculptMeshCacheChangeCloneSource in ['query']
def sculptMeshCacheChangeCloneSource(blendShape: str = ..., bs: str = ..., target: str = ..., t: str = ..., query: bool = ..., q: bool = ...) -> None:
    """sculptMeshCacheChangeCloneSource is undoable, queryable, and editable.
    
    This command changes the source blend shape and target for the clone target
    tool. Used internally for undo/redo, and should not be called directly.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sculptMeshCacheChangeCloneSource( bs='blendShape1', t='pSphere4' )
    ```

    ---
    - Args:
        - blendShape (bs): Set which blend shape should be used as the source when using the clone tool. When queried, returns the current blend shape name as a string.
        - target (t): Set which blend shape should be used as the target when using the clone tool. When queried, returns the current blend shape target name as a string.
        - query (q): Query mode flag
    """
@overload #Overload for sculptMeshCacheChangeCloneSource in ['edit']
def sculptMeshCacheChangeCloneSource(blendShape: str = ..., target: str = ..., edit: bool = ...) -> None:
    """sculptMeshCacheChangeCloneSource is undoable, queryable, and editable.
    
    This command changes the source blend shape and target for the clone target
    tool. Used internally for undo/redo, and should not be called directly.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sculptMeshCacheChangeCloneSource( bs='blendShape1', t='pSphere4' )
    ```

    ---
    - Args:
        - blendShape (bs): Set which blend shape should be used as the source when using the clone tool. When queried, returns the current blend shape name as a string.
        - target (t): Set which blend shape should be used as the target when using the clone tool. When queried, returns the current blend shape target name as a string.
        - edit (e): Edit mode flag
    """
@overload #Overload for sculptMeshCacheChangeCloneSource in ['edit']
def sculptMeshCacheChangeCloneSource(bs: str = ..., t: str = ..., e: bool = ...) -> None:
    """sculptMeshCacheChangeCloneSource is undoable, queryable, and editable.
    
    This command changes the source blend shape and target for the clone target
    tool. Used internally for undo/redo, and should not be called directly.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sculptMeshCacheChangeCloneSource( bs='blendShape1', t='pSphere4' )
    ```

    ---
    - Args:
        - blendShape (bs): Set which blend shape should be used as the source when using the clone tool. When queried, returns the current blend shape name as a string.
        - target (t): Set which blend shape should be used as the target when using the clone tool. When queried, returns the current blend shape target name as a string.
        - edit (e): Edit mode flag
    """
@overload #Overload for sculptMeshCacheChangeCloneSource in ['edit']
def sculptMeshCacheChangeCloneSource(blendShape: str = ..., bs: str = ..., target: str = ..., t: str = ..., edit: bool = ..., e: bool = ...) -> None:
    """sculptMeshCacheChangeCloneSource is undoable, queryable, and editable.
    
    This command changes the source blend shape and target for the clone target
    tool. Used internally for undo/redo, and should not be called directly.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sculptMeshCacheChangeCloneSource( bs='blendShape1', t='pSphere4' )
    ```

    ---
    - Args:
        - blendShape (bs): Set which blend shape should be used as the source when using the clone tool. When queried, returns the current blend shape name as a string.
        - target (t): Set which blend shape should be used as the target when using the clone tool. When queried, returns the current blend shape target name as a string.
        - edit (e): Edit mode flag
    """
