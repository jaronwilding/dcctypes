"""Stub files for General category in Maya commands, command: spaceLocator."""

from typing import Any, overload

@overload #Overload for spaceLocator in ['create']
def spaceLocator(absolute: bool = ..., name: str = ..., position: [linear, linear, linear] = ..., relative: bool = ...) -> list[str]:
    """spaceLocator is undoable, queryable, and editable.
    
    The command creates a locator at the specified position in space. By default
    it is created at (0,0,0).

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a space locator at (1, 1, 1).
        cmds.spaceLocator( p=(1, 1, 1) )
        # Creates a space locator at (1, 1, 1) in inches.
        cmds.spaceLocator( p=('1in', '1in', '1in') )
        # Creates a space locator at the default position (0, 0, 0).
        cmds.spaceLocator()
    ```

    ---
    - Args:
        - absolute (a): If set, the locator's position is in world space.
        - name (n): Name for the locator.
        - position (p): Location in  3-dimensional space where locator is to be created.
        - relative (r): If set, the locator's position is relative to its local space. The locator is created in relative mode by default.
    """
@overload #Overload for spaceLocator in ['create']
def spaceLocator(a: bool = ..., n: str = ..., p: [linear, linear, linear] = ..., r: bool = ...) -> list[str]:
    """spaceLocator is undoable, queryable, and editable.
    
    The command creates a locator at the specified position in space. By default
    it is created at (0,0,0).

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a space locator at (1, 1, 1).
        cmds.spaceLocator( p=(1, 1, 1) )
        # Creates a space locator at (1, 1, 1) in inches.
        cmds.spaceLocator( p=('1in', '1in', '1in') )
        # Creates a space locator at the default position (0, 0, 0).
        cmds.spaceLocator()
    ```

    ---
    - Args:
        - absolute (a): If set, the locator's position is in world space.
        - name (n): Name for the locator.
        - position (p): Location in  3-dimensional space where locator is to be created.
        - relative (r): If set, the locator's position is relative to its local space. The locator is created in relative mode by default.
    """
@overload #Overload for spaceLocator in ['create']
def spaceLocator(absolute: bool = ..., a: bool = ..., name: str = ..., n: str = ..., position: [linear, linear, linear] = ..., p: [linear, linear, linear] = ..., relative: bool = ..., r: bool = ...) -> list[str]:
    """spaceLocator is undoable, queryable, and editable.
    
    The command creates a locator at the specified position in space. By default
    it is created at (0,0,0).

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a space locator at (1, 1, 1).
        cmds.spaceLocator( p=(1, 1, 1) )
        # Creates a space locator at (1, 1, 1) in inches.
        cmds.spaceLocator( p=('1in', '1in', '1in') )
        # Creates a space locator at the default position (0, 0, 0).
        cmds.spaceLocator()
    ```

    ---
    - Args:
        - absolute (a): If set, the locator's position is in world space.
        - name (n): Name for the locator.
        - position (p): Location in  3-dimensional space where locator is to be created.
        - relative (r): If set, the locator's position is relative to its local space. The locator is created in relative mode by default.
    """
@overload #Overload for spaceLocator in ['query']
def spaceLocator(position: [linear, linear, linear] = ..., query: bool = ...) -> list[str]:
    """spaceLocator is undoable, queryable, and editable.
    
    The command creates a locator at the specified position in space. By default
    it is created at (0,0,0).

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a space locator at (1, 1, 1).
        cmds.spaceLocator( p=(1, 1, 1) )
        # Creates a space locator at (1, 1, 1) in inches.
        cmds.spaceLocator( p=('1in', '1in', '1in') )
        # Creates a space locator at the default position (0, 0, 0).
        cmds.spaceLocator()
    ```

    ---
    - Args:
        - position (p): Location in  3-dimensional space where locator is to be created.
        - query (q): Query mode flag
    """
@overload #Overload for spaceLocator in ['query']
def spaceLocator(p: [linear, linear, linear] = ..., q: bool = ...) -> list[str]:
    """spaceLocator is undoable, queryable, and editable.
    
    The command creates a locator at the specified position in space. By default
    it is created at (0,0,0).

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a space locator at (1, 1, 1).
        cmds.spaceLocator( p=(1, 1, 1) )
        # Creates a space locator at (1, 1, 1) in inches.
        cmds.spaceLocator( p=('1in', '1in', '1in') )
        # Creates a space locator at the default position (0, 0, 0).
        cmds.spaceLocator()
    ```

    ---
    - Args:
        - position (p): Location in  3-dimensional space where locator is to be created.
        - query (q): Query mode flag
    """
@overload #Overload for spaceLocator in ['query']
def spaceLocator(position: [linear, linear, linear] = ..., p: [linear, linear, linear] = ..., query: bool = ..., q: bool = ...) -> list[str]:
    """spaceLocator is undoable, queryable, and editable.
    
    The command creates a locator at the specified position in space. By default
    it is created at (0,0,0).

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a space locator at (1, 1, 1).
        cmds.spaceLocator( p=(1, 1, 1) )
        # Creates a space locator at (1, 1, 1) in inches.
        cmds.spaceLocator( p=('1in', '1in', '1in') )
        # Creates a space locator at the default position (0, 0, 0).
        cmds.spaceLocator()
    ```

    ---
    - Args:
        - position (p): Location in  3-dimensional space where locator is to be created.
        - query (q): Query mode flag
    """
@overload #Overload for spaceLocator in ['edit']
def spaceLocator(absolute: bool = ..., name: str = ..., position: [linear, linear, linear] = ..., relative: bool = ..., edit: bool = ...) -> list[str]:
    """spaceLocator is undoable, queryable, and editable.
    
    The command creates a locator at the specified position in space. By default
    it is created at (0,0,0).

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a space locator at (1, 1, 1).
        cmds.spaceLocator( p=(1, 1, 1) )
        # Creates a space locator at (1, 1, 1) in inches.
        cmds.spaceLocator( p=('1in', '1in', '1in') )
        # Creates a space locator at the default position (0, 0, 0).
        cmds.spaceLocator()
    ```

    ---
    - Args:
        - absolute (a): If set, the locator's position is in world space.
        - name (n): Name for the locator.
        - position (p): Location in  3-dimensional space where locator is to be created.
        - relative (r): If set, the locator's position is relative to its local space. The locator is created in relative mode by default.
        - edit (e): Edit mode flag
    """
@overload #Overload for spaceLocator in ['edit']
def spaceLocator(a: bool = ..., n: str = ..., p: [linear, linear, linear] = ..., r: bool = ..., e: bool = ...) -> list[str]:
    """spaceLocator is undoable, queryable, and editable.
    
    The command creates a locator at the specified position in space. By default
    it is created at (0,0,0).

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a space locator at (1, 1, 1).
        cmds.spaceLocator( p=(1, 1, 1) )
        # Creates a space locator at (1, 1, 1) in inches.
        cmds.spaceLocator( p=('1in', '1in', '1in') )
        # Creates a space locator at the default position (0, 0, 0).
        cmds.spaceLocator()
    ```

    ---
    - Args:
        - absolute (a): If set, the locator's position is in world space.
        - name (n): Name for the locator.
        - position (p): Location in  3-dimensional space where locator is to be created.
        - relative (r): If set, the locator's position is relative to its local space. The locator is created in relative mode by default.
        - edit (e): Edit mode flag
    """
@overload #Overload for spaceLocator in ['edit']
def spaceLocator(absolute: bool = ..., a: bool = ..., name: str = ..., n: str = ..., position: [linear, linear, linear] = ..., p: [linear, linear, linear] = ..., relative: bool = ..., r: bool = ..., edit: bool = ..., e: bool = ...) -> list[str]:
    """spaceLocator is undoable, queryable, and editable.
    
    The command creates a locator at the specified position in space. By default
    it is created at (0,0,0).

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a space locator at (1, 1, 1).
        cmds.spaceLocator( p=(1, 1, 1) )
        # Creates a space locator at (1, 1, 1) in inches.
        cmds.spaceLocator( p=('1in', '1in', '1in') )
        # Creates a space locator at the default position (0, 0, 0).
        cmds.spaceLocator()
    ```

    ---
    - Args:
        - absolute (a): If set, the locator's position is in world space.
        - name (n): Name for the locator.
        - position (p): Location in  3-dimensional space where locator is to be created.
        - relative (r): If set, the locator's position is relative to its local space. The locator is created in relative mode by default.
        - edit (e): Edit mode flag
    """
