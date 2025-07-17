"""Stub files for General category in Maya commands, command: makeLive."""

from typing import Any, overload

@overload #Overload for makeLive in ['create']
def makeLive([surface...]: [surface...], none: bool = ..., registry: int = ..., registryReset: bool = ..., registrySize: int = ...) -> None:
    """makeLive is undoable, queryable, and editable.
    
    This commmand makes one or several objects live. A live object defines the
    surface on which to create objects and to move objects relative to. Only
    construction planes, nurbs surfaces and polygon meshes can be made live.
    
    The makeLive command expects one of these types of objects as an explicit
    argument. If no argument is explicitly specified, then there are a number of
    default behaviours based on what is currently active. The command will fail if
    the active object(s) is/are not one of the valid types of objects. If there is
    nothing active, the current live object(s) will become dormant. Otherwise, the
    active object(s) will become the live object(s).
    
    The command allows for a limited number of objects collections to be saved in
    a registry entry. These collections can be queried and/or made live.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.makeLive( 'surface1' )
        cmds.makeLive( none=True )
    ```

    ---
    - Args:
        - [surface...]: Input item(s).
        - none (n): If the -n/none flag, the live object(s) will become dormant. Use of this flag causes any arguments to be ignored.
        - registry (r): Make live the objects defined in the specified registry entry. In Query mode, return the list of objects defined in the specified registry entry.
        - registryReset (rr): Reset the maximum number of registry entries to the default value and clear all stored data.
        - registrySize (rs): Defines the maximum number of registry entries that are remembered by the command. In Query mode, returns the maximum number currently set.
    """
@overload #Overload for makeLive in ['create']
def makeLive([surface...]: [surface...], n: bool = ..., r: int = ..., rr: bool = ..., rs: int = ...) -> None:
    """makeLive is undoable, queryable, and editable.
    
    This commmand makes one or several objects live. A live object defines the
    surface on which to create objects and to move objects relative to. Only
    construction planes, nurbs surfaces and polygon meshes can be made live.
    
    The makeLive command expects one of these types of objects as an explicit
    argument. If no argument is explicitly specified, then there are a number of
    default behaviours based on what is currently active. The command will fail if
    the active object(s) is/are not one of the valid types of objects. If there is
    nothing active, the current live object(s) will become dormant. Otherwise, the
    active object(s) will become the live object(s).
    
    The command allows for a limited number of objects collections to be saved in
    a registry entry. These collections can be queried and/or made live.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.makeLive( 'surface1' )
        cmds.makeLive( none=True )
    ```

    ---
    - Args:
        - [surface...]: Input item(s).
        - none (n): If the -n/none flag, the live object(s) will become dormant. Use of this flag causes any arguments to be ignored.
        - registry (r): Make live the objects defined in the specified registry entry. In Query mode, return the list of objects defined in the specified registry entry.
        - registryReset (rr): Reset the maximum number of registry entries to the default value and clear all stored data.
        - registrySize (rs): Defines the maximum number of registry entries that are remembered by the command. In Query mode, returns the maximum number currently set.
    """
@overload #Overload for makeLive in ['create']
def makeLive([surface...]: [surface...], none: bool = ..., n: bool = ..., registry: int = ..., r: int = ..., registryReset: bool = ..., rr: bool = ..., registrySize: int = ..., rs: int = ...) -> None:
    """makeLive is undoable, queryable, and editable.
    
    This commmand makes one or several objects live. A live object defines the
    surface on which to create objects and to move objects relative to. Only
    construction planes, nurbs surfaces and polygon meshes can be made live.
    
    The makeLive command expects one of these types of objects as an explicit
    argument. If no argument is explicitly specified, then there are a number of
    default behaviours based on what is currently active. The command will fail if
    the active object(s) is/are not one of the valid types of objects. If there is
    nothing active, the current live object(s) will become dormant. Otherwise, the
    active object(s) will become the live object(s).
    
    The command allows for a limited number of objects collections to be saved in
    a registry entry. These collections can be queried and/or made live.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.makeLive( 'surface1' )
        cmds.makeLive( none=True )
    ```

    ---
    - Args:
        - [surface...]: Input item(s).
        - none (n): If the -n/none flag, the live object(s) will become dormant. Use of this flag causes any arguments to be ignored.
        - registry (r): Make live the objects defined in the specified registry entry. In Query mode, return the list of objects defined in the specified registry entry.
        - registryReset (rr): Reset the maximum number of registry entries to the default value and clear all stored data.
        - registrySize (rs): Defines the maximum number of registry entries that are remembered by the command. In Query mode, returns the maximum number currently set.
    """
@overload #Overload for makeLive in ['query']
def makeLive([surface...]: [surface...], registry: int = ..., registryCount: bool = ..., registrySize: int = ..., query: bool = ...) -> None:
    """makeLive is undoable, queryable, and editable.
    
    This commmand makes one or several objects live. A live object defines the
    surface on which to create objects and to move objects relative to. Only
    construction planes, nurbs surfaces and polygon meshes can be made live.
    
    The makeLive command expects one of these types of objects as an explicit
    argument. If no argument is explicitly specified, then there are a number of
    default behaviours based on what is currently active. The command will fail if
    the active object(s) is/are not one of the valid types of objects. If there is
    nothing active, the current live object(s) will become dormant. Otherwise, the
    active object(s) will become the live object(s).
    
    The command allows for a limited number of objects collections to be saved in
    a registry entry. These collections can be queried and/or made live.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.makeLive( 'surface1' )
        cmds.makeLive( none=True )
    ```

    ---
    - Args:
        - [surface...]: Input item(s).
        - registry (r): Make live the objects defined in the specified registry entry. In Query mode, return the list of objects defined in the specified registry entry.
        - registryCount (rc): Return the actual number of registry entries. This number ranges from 0 to 'registrySize' - 1.
        - registrySize (rs): Defines the maximum number of registry entries that are remembered by the command. In Query mode, returns the maximum number currently set.
        - query (q): Query mode flag
    """
@overload #Overload for makeLive in ['query']
def makeLive([surface...]: [surface...], r: int = ..., rc: bool = ..., rs: int = ..., q: bool = ...) -> None:
    """makeLive is undoable, queryable, and editable.
    
    This commmand makes one or several objects live. A live object defines the
    surface on which to create objects and to move objects relative to. Only
    construction planes, nurbs surfaces and polygon meshes can be made live.
    
    The makeLive command expects one of these types of objects as an explicit
    argument. If no argument is explicitly specified, then there are a number of
    default behaviours based on what is currently active. The command will fail if
    the active object(s) is/are not one of the valid types of objects. If there is
    nothing active, the current live object(s) will become dormant. Otherwise, the
    active object(s) will become the live object(s).
    
    The command allows for a limited number of objects collections to be saved in
    a registry entry. These collections can be queried and/or made live.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.makeLive( 'surface1' )
        cmds.makeLive( none=True )
    ```

    ---
    - Args:
        - [surface...]: Input item(s).
        - registry (r): Make live the objects defined in the specified registry entry. In Query mode, return the list of objects defined in the specified registry entry.
        - registryCount (rc): Return the actual number of registry entries. This number ranges from 0 to 'registrySize' - 1.
        - registrySize (rs): Defines the maximum number of registry entries that are remembered by the command. In Query mode, returns the maximum number currently set.
        - query (q): Query mode flag
    """
@overload #Overload for makeLive in ['query']
def makeLive([surface...]: [surface...], registry: int = ..., r: int = ..., registryCount: bool = ..., rc: bool = ..., registrySize: int = ..., rs: int = ..., query: bool = ..., q: bool = ...) -> None:
    """makeLive is undoable, queryable, and editable.
    
    This commmand makes one or several objects live. A live object defines the
    surface on which to create objects and to move objects relative to. Only
    construction planes, nurbs surfaces and polygon meshes can be made live.
    
    The makeLive command expects one of these types of objects as an explicit
    argument. If no argument is explicitly specified, then there are a number of
    default behaviours based on what is currently active. The command will fail if
    the active object(s) is/are not one of the valid types of objects. If there is
    nothing active, the current live object(s) will become dormant. Otherwise, the
    active object(s) will become the live object(s).
    
    The command allows for a limited number of objects collections to be saved in
    a registry entry. These collections can be queried and/or made live.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.makeLive( 'surface1' )
        cmds.makeLive( none=True )
    ```

    ---
    - Args:
        - [surface...]: Input item(s).
        - registry (r): Make live the objects defined in the specified registry entry. In Query mode, return the list of objects defined in the specified registry entry.
        - registryCount (rc): Return the actual number of registry entries. This number ranges from 0 to 'registrySize' - 1.
        - registrySize (rs): Defines the maximum number of registry entries that are remembered by the command. In Query mode, returns the maximum number currently set.
        - query (q): Query mode flag
    """
@overload #Overload for makeLive in ['edit']
def makeLive([surface...]: [surface...], addObjects: bool = ..., removeObjects: bool = ..., edit: bool = ...) -> None:
    """makeLive is undoable, queryable, and editable.
    
    This commmand makes one or several objects live. A live object defines the
    surface on which to create objects and to move objects relative to. Only
    construction planes, nurbs surfaces and polygon meshes can be made live.
    
    The makeLive command expects one of these types of objects as an explicit
    argument. If no argument is explicitly specified, then there are a number of
    default behaviours based on what is currently active. The command will fail if
    the active object(s) is/are not one of the valid types of objects. If there is
    nothing active, the current live object(s) will become dormant. Otherwise, the
    active object(s) will become the live object(s).
    
    The command allows for a limited number of objects collections to be saved in
    a registry entry. These collections can be queried and/or made live.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.makeLive( 'surface1' )
        cmds.makeLive( none=True )
    ```

    ---
    - Args:
        - [surface...]: Input item(s).
        - addObjects (ao): Add the listed object(s) to the current live list. If an object is already in the live list, it is ignored.
        - removeObjects (ro): Remove the listed object(s) from the current live list. If an object is not in the list, it is ignored.
        - edit (e): Edit mode flag
    """
@overload #Overload for makeLive in ['edit']
def makeLive([surface...]: [surface...], ao: bool = ..., ro: bool = ..., e: bool = ...) -> None:
    """makeLive is undoable, queryable, and editable.
    
    This commmand makes one or several objects live. A live object defines the
    surface on which to create objects and to move objects relative to. Only
    construction planes, nurbs surfaces and polygon meshes can be made live.
    
    The makeLive command expects one of these types of objects as an explicit
    argument. If no argument is explicitly specified, then there are a number of
    default behaviours based on what is currently active. The command will fail if
    the active object(s) is/are not one of the valid types of objects. If there is
    nothing active, the current live object(s) will become dormant. Otherwise, the
    active object(s) will become the live object(s).
    
    The command allows for a limited number of objects collections to be saved in
    a registry entry. These collections can be queried and/or made live.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.makeLive( 'surface1' )
        cmds.makeLive( none=True )
    ```

    ---
    - Args:
        - [surface...]: Input item(s).
        - addObjects (ao): Add the listed object(s) to the current live list. If an object is already in the live list, it is ignored.
        - removeObjects (ro): Remove the listed object(s) from the current live list. If an object is not in the list, it is ignored.
        - edit (e): Edit mode flag
    """
@overload #Overload for makeLive in ['edit']
def makeLive([surface...]: [surface...], addObjects: bool = ..., ao: bool = ..., removeObjects: bool = ..., ro: bool = ..., edit: bool = ..., e: bool = ...) -> None:
    """makeLive is undoable, queryable, and editable.
    
    This commmand makes one or several objects live. A live object defines the
    surface on which to create objects and to move objects relative to. Only
    construction planes, nurbs surfaces and polygon meshes can be made live.
    
    The makeLive command expects one of these types of objects as an explicit
    argument. If no argument is explicitly specified, then there are a number of
    default behaviours based on what is currently active. The command will fail if
    the active object(s) is/are not one of the valid types of objects. If there is
    nothing active, the current live object(s) will become dormant. Otherwise, the
    active object(s) will become the live object(s).
    
    The command allows for a limited number of objects collections to be saved in
    a registry entry. These collections can be queried and/or made live.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.makeLive( 'surface1' )
        cmds.makeLive( none=True )
    ```

    ---
    - Args:
        - [surface...]: Input item(s).
        - addObjects (ao): Add the listed object(s) to the current live list. If an object is already in the live list, it is ignored.
        - removeObjects (ro): Remove the listed object(s) from the current live list. If an object is not in the list, it is ignored.
        - edit (e): Edit mode flag
    """
