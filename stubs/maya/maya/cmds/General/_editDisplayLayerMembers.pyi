"""Stub files for General category in Maya commands, command: editDisplayLayerMembers."""

from typing import Any, overload

@overload #Overload for editDisplayLayerMembers in ['create']
def editDisplayLayerMembers(clear: bool = ..., noRecurse: bool = ...) -> int | list[str]:
    """editDisplayLayerMembers is undoable, queryable, and NOT editable.
    
    This command is used to query and edit membership of display layers. No
    equivalent 'remove' command is necessary since all objects must be in exactly
    one display layer. Removing an object from a layer can be accomplished by
    adding it to a different layer.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.editDisplayLayerMembers( 'displayLayer1', 'sphere1', 'cone1' )
        # Result : 2
        cmds.editDisplayLayerMembers( 'displayLayer1', query=True )
        # Result : sphere1 cone1
        cmds.editDisplayLayerMembers( 'displayLayer1', 'expression1', 'sphere2' )
        # Warning : Only DAG objects can be in a display layer.  'expression1' ignored.
        # Result : 1
        ufeSel = cmds.ls(selection=True, ufe=True)
        cmds.editDisplayLayerMembers('layer1', ufeSel, noRecurse=True)
        // Result: 1
        cmds.editDisplayLayerMembers('layer1', clear=True)
        # Result: 1
    ```

    ---
    - Args:
        - clear (clr): Remove all the objects contained in the layer by moving them to the default layer.
        - noRecurse (nr): If set then only add selected objects to the display layer.  Otherwise all descendants of the selected objects will also be added.
    """
@overload #Overload for editDisplayLayerMembers in ['create']
def editDisplayLayerMembers(clr: bool = ..., nr: bool = ...) -> int | list[str]:
    """editDisplayLayerMembers is undoable, queryable, and NOT editable.
    
    This command is used to query and edit membership of display layers. No
    equivalent 'remove' command is necessary since all objects must be in exactly
    one display layer. Removing an object from a layer can be accomplished by
    adding it to a different layer.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.editDisplayLayerMembers( 'displayLayer1', 'sphere1', 'cone1' )
        # Result : 2
        cmds.editDisplayLayerMembers( 'displayLayer1', query=True )
        # Result : sphere1 cone1
        cmds.editDisplayLayerMembers( 'displayLayer1', 'expression1', 'sphere2' )
        # Warning : Only DAG objects can be in a display layer.  'expression1' ignored.
        # Result : 1
        ufeSel = cmds.ls(selection=True, ufe=True)
        cmds.editDisplayLayerMembers('layer1', ufeSel, noRecurse=True)
        // Result: 1
        cmds.editDisplayLayerMembers('layer1', clear=True)
        # Result: 1
    ```

    ---
    - Args:
        - clear (clr): Remove all the objects contained in the layer by moving them to the default layer.
        - noRecurse (nr): If set then only add selected objects to the display layer.  Otherwise all descendants of the selected objects will also be added.
    """
@overload #Overload for editDisplayLayerMembers in ['create']
def editDisplayLayerMembers(clear: bool = ..., clr: bool = ..., noRecurse: bool = ..., nr: bool = ...) -> int | list[str]:
    """editDisplayLayerMembers is undoable, queryable, and NOT editable.
    
    This command is used to query and edit membership of display layers. No
    equivalent 'remove' command is necessary since all objects must be in exactly
    one display layer. Removing an object from a layer can be accomplished by
    adding it to a different layer.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.editDisplayLayerMembers( 'displayLayer1', 'sphere1', 'cone1' )
        # Result : 2
        cmds.editDisplayLayerMembers( 'displayLayer1', query=True )
        # Result : sphere1 cone1
        cmds.editDisplayLayerMembers( 'displayLayer1', 'expression1', 'sphere2' )
        # Warning : Only DAG objects can be in a display layer.  'expression1' ignored.
        # Result : 1
        ufeSel = cmds.ls(selection=True, ufe=True)
        cmds.editDisplayLayerMembers('layer1', ufeSel, noRecurse=True)
        // Result: 1
        cmds.editDisplayLayerMembers('layer1', clear=True)
        # Result: 1
    ```

    ---
    - Args:
        - clear (clr): Remove all the objects contained in the layer by moving them to the default layer.
        - noRecurse (nr): If set then only add selected objects to the display layer.  Otherwise all descendants of the selected objects will also be added.
    """
@overload #Overload for editDisplayLayerMembers in ['query']
def editDisplayLayerMembers(fullNames: bool = ..., noRecurse: bool = ..., ufeObjects: bool = ..., query: bool = ...) -> int | list[str]:
    """editDisplayLayerMembers is undoable, queryable, and NOT editable.
    
    This command is used to query and edit membership of display layers. No
    equivalent 'remove' command is necessary since all objects must be in exactly
    one display layer. Removing an object from a layer can be accomplished by
    adding it to a different layer.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.editDisplayLayerMembers( 'displayLayer1', 'sphere1', 'cone1' )
        # Result : 2
        cmds.editDisplayLayerMembers( 'displayLayer1', query=True )
        # Result : sphere1 cone1
        cmds.editDisplayLayerMembers( 'displayLayer1', 'expression1', 'sphere2' )
        # Warning : Only DAG objects can be in a display layer.  'expression1' ignored.
        # Result : 1
        ufeSel = cmds.ls(selection=True, ufe=True)
        cmds.editDisplayLayerMembers('layer1', ufeSel, noRecurse=True)
        // Result: 1
        cmds.editDisplayLayerMembers('layer1', clear=True)
        # Result: 1
    ```

    ---
    - Args:
        - fullNames (fn): (Query only.) If set then return the full DAG paths of the objects in the layer.  Otherwise return just the name of the object.
        - noRecurse (nr): If set then only add selected objects to the display layer.  Otherwise all descendants of the selected objects will also be added.
        - ufeObjects (ufe): (Query only.) If set will return objects that are defined through the UFE interface as well as native Maya objects.
        - query (q): Query mode flag
    """
@overload #Overload for editDisplayLayerMembers in ['query']
def editDisplayLayerMembers(fn: bool = ..., nr: bool = ..., ufe: bool = ..., q: bool = ...) -> int | list[str]:
    """editDisplayLayerMembers is undoable, queryable, and NOT editable.
    
    This command is used to query and edit membership of display layers. No
    equivalent 'remove' command is necessary since all objects must be in exactly
    one display layer. Removing an object from a layer can be accomplished by
    adding it to a different layer.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.editDisplayLayerMembers( 'displayLayer1', 'sphere1', 'cone1' )
        # Result : 2
        cmds.editDisplayLayerMembers( 'displayLayer1', query=True )
        # Result : sphere1 cone1
        cmds.editDisplayLayerMembers( 'displayLayer1', 'expression1', 'sphere2' )
        # Warning : Only DAG objects can be in a display layer.  'expression1' ignored.
        # Result : 1
        ufeSel = cmds.ls(selection=True, ufe=True)
        cmds.editDisplayLayerMembers('layer1', ufeSel, noRecurse=True)
        // Result: 1
        cmds.editDisplayLayerMembers('layer1', clear=True)
        # Result: 1
    ```

    ---
    - Args:
        - fullNames (fn): (Query only.) If set then return the full DAG paths of the objects in the layer.  Otherwise return just the name of the object.
        - noRecurse (nr): If set then only add selected objects to the display layer.  Otherwise all descendants of the selected objects will also be added.
        - ufeObjects (ufe): (Query only.) If set will return objects that are defined through the UFE interface as well as native Maya objects.
        - query (q): Query mode flag
    """
@overload #Overload for editDisplayLayerMembers in ['query']
def editDisplayLayerMembers(fullNames: bool = ..., fn: bool = ..., noRecurse: bool = ..., nr: bool = ..., ufeObjects: bool = ..., ufe: bool = ..., query: bool = ..., q: bool = ...) -> int | list[str]:
    """editDisplayLayerMembers is undoable, queryable, and NOT editable.
    
    This command is used to query and edit membership of display layers. No
    equivalent 'remove' command is necessary since all objects must be in exactly
    one display layer. Removing an object from a layer can be accomplished by
    adding it to a different layer.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.editDisplayLayerMembers( 'displayLayer1', 'sphere1', 'cone1' )
        # Result : 2
        cmds.editDisplayLayerMembers( 'displayLayer1', query=True )
        # Result : sphere1 cone1
        cmds.editDisplayLayerMembers( 'displayLayer1', 'expression1', 'sphere2' )
        # Warning : Only DAG objects can be in a display layer.  'expression1' ignored.
        # Result : 1
        ufeSel = cmds.ls(selection=True, ufe=True)
        cmds.editDisplayLayerMembers('layer1', ufeSel, noRecurse=True)
        // Result: 1
        cmds.editDisplayLayerMembers('layer1', clear=True)
        # Result: 1
    ```

    ---
    - Args:
        - fullNames (fn): (Query only.) If set then return the full DAG paths of the objects in the layer.  Otherwise return just the name of the object.
        - noRecurse (nr): If set then only add selected objects to the display layer.  Otherwise all descendants of the selected objects will also be added.
        - ufeObjects (ufe): (Query only.) If set will return objects that are defined through the UFE interface as well as native Maya objects.
        - query (q): Query mode flag
    """
