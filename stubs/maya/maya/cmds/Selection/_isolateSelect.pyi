"""Stub files for Selection category in Maya commands, command: isolateSelect."""

from typing import Any, overload

@overload #Overload for isolateSelect in ['query']
def isolateSelect(string: str, state: bool = ..., viewObjects: bool = ..., query: bool = ...) -> bool:
    """isolateSelect is undoable, queryable, and NOT editable.
    
    This command turns on/off isolate select mode in a specified modeling view,
    specified as the argument. Isolate select mode is a display mode where the
    currently selected objects are added to a list and only those objects are
    displayed in the view. It allows for selective viewing of specific objects and
    object components.

    Example:
    ```python
        import maya.cmds as cmds
        # create some primitives and go into component selection mode
        cmds.sphere( n='sphere1' )
        cmds.cone( n='cone1' )
        cmds.selectMode( component=True )
        # Use the current modelPanel for isolation
        isolated_panel = cmds.paneLayout('viewPanes', q=True, pane1=True)
        # turn on isolate select mode for a particular 3d view. Only
        # the sphere and the selected CVs will be displayed.
        cmds.select( 'sphere1.cv[0:2][*]' )
        # Connect the selected objects with editor and
        # locks the current list of objects within the mainConnection
        cmds.editor( isolated_panel, edit=True, lockMainConnection=True, mainListConnection='activeList' )
        cmds.isolateSelect( isolated_panel, state=1 )
        # add the cone to the list of objects to be viewed
        cmds.select( 'cone1' )
        cmds.isolateSelect( isolated_panel, addSelected=True )
        # make just the sphere the object to be viewed
        cmds.select( 'sphere1' )
        # Unlock the current list of objects within the editor
        cmds.editor( isolated_panel, edit=True, mainListConnection='activeList' )
        cmds.isolateSelect( isolated_panel, loadSelected=True )
    ```

    ---
    - Args:
        - string: Input item(s).
        - state (s): Turns isolate select mode on/off.
        - viewObjects (vo): Returns the name (if any) of the objectSet which contains the list of objects visible in the view if isolate select mode is on. If isolate select mode is off, an empty string is returned.
        - query (q): Query mode flag
    """
@overload #Overload for isolateSelect in ['query']
def isolateSelect(string: str, s: bool = ..., vo: bool = ..., q: bool = ...) -> bool:
    """isolateSelect is undoable, queryable, and NOT editable.
    
    This command turns on/off isolate select mode in a specified modeling view,
    specified as the argument. Isolate select mode is a display mode where the
    currently selected objects are added to a list and only those objects are
    displayed in the view. It allows for selective viewing of specific objects and
    object components.

    Example:
    ```python
        import maya.cmds as cmds
        # create some primitives and go into component selection mode
        cmds.sphere( n='sphere1' )
        cmds.cone( n='cone1' )
        cmds.selectMode( component=True )
        # Use the current modelPanel for isolation
        isolated_panel = cmds.paneLayout('viewPanes', q=True, pane1=True)
        # turn on isolate select mode for a particular 3d view. Only
        # the sphere and the selected CVs will be displayed.
        cmds.select( 'sphere1.cv[0:2][*]' )
        # Connect the selected objects with editor and
        # locks the current list of objects within the mainConnection
        cmds.editor( isolated_panel, edit=True, lockMainConnection=True, mainListConnection='activeList' )
        cmds.isolateSelect( isolated_panel, state=1 )
        # add the cone to the list of objects to be viewed
        cmds.select( 'cone1' )
        cmds.isolateSelect( isolated_panel, addSelected=True )
        # make just the sphere the object to be viewed
        cmds.select( 'sphere1' )
        # Unlock the current list of objects within the editor
        cmds.editor( isolated_panel, edit=True, mainListConnection='activeList' )
        cmds.isolateSelect( isolated_panel, loadSelected=True )
    ```

    ---
    - Args:
        - string: Input item(s).
        - state (s): Turns isolate select mode on/off.
        - viewObjects (vo): Returns the name (if any) of the objectSet which contains the list of objects visible in the view if isolate select mode is on. If isolate select mode is off, an empty string is returned.
        - query (q): Query mode flag
    """
@overload #Overload for isolateSelect in ['query']
def isolateSelect(string: str, state: bool = ..., s: bool = ..., viewObjects: bool = ..., vo: bool = ..., query: bool = ..., q: bool = ...) -> bool:
    """isolateSelect is undoable, queryable, and NOT editable.
    
    This command turns on/off isolate select mode in a specified modeling view,
    specified as the argument. Isolate select mode is a display mode where the
    currently selected objects are added to a list and only those objects are
    displayed in the view. It allows for selective viewing of specific objects and
    object components.

    Example:
    ```python
        import maya.cmds as cmds
        # create some primitives and go into component selection mode
        cmds.sphere( n='sphere1' )
        cmds.cone( n='cone1' )
        cmds.selectMode( component=True )
        # Use the current modelPanel for isolation
        isolated_panel = cmds.paneLayout('viewPanes', q=True, pane1=True)
        # turn on isolate select mode for a particular 3d view. Only
        # the sphere and the selected CVs will be displayed.
        cmds.select( 'sphere1.cv[0:2][*]' )
        # Connect the selected objects with editor and
        # locks the current list of objects within the mainConnection
        cmds.editor( isolated_panel, edit=True, lockMainConnection=True, mainListConnection='activeList' )
        cmds.isolateSelect( isolated_panel, state=1 )
        # add the cone to the list of objects to be viewed
        cmds.select( 'cone1' )
        cmds.isolateSelect( isolated_panel, addSelected=True )
        # make just the sphere the object to be viewed
        cmds.select( 'sphere1' )
        # Unlock the current list of objects within the editor
        cmds.editor( isolated_panel, edit=True, mainListConnection='activeList' )
        cmds.isolateSelect( isolated_panel, loadSelected=True )
    ```

    ---
    - Args:
        - string: Input item(s).
        - state (s): Turns isolate select mode on/off.
        - viewObjects (vo): Returns the name (if any) of the objectSet which contains the list of objects visible in the view if isolate select mode is on. If isolate select mode is off, an empty string is returned.
        - query (q): Query mode flag
    """
