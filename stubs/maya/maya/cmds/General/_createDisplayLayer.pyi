"""Stub files for General category in Maya commands, command: createDisplayLayer."""

from typing import Any, overload

@overload #Overload for createDisplayLayer in ['create']
def createDisplayLayer(empty: bool = ..., makeCurrent: bool = ..., name: str = ..., noRecurse: bool = ..., number: int = ...) -> str:
    """createDisplayLayer is undoable, NOT queryable, and NOT editable.
    
    Create a new display layer. The display layer number will be assigned based on
    the first unassigned number not less than the base index number found in the
    display layer global parameters. Normally all objects and their descendants
    will be added to the new display layer but if the '-nr' flag is specified then
    only the objects themselves will be added.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a sphere.
        #
        objectArray = cmds.sphere()
        #    Select the sphere.
        #
        cmds.select( objectArray[0] )
        #    Create a layer. The selected object will be placed
        #    in this layer. Note in this case both the nurbsSphere
        #    and nurbsSphere shape are placed in the layer.
        #
        cmds.createDisplayLayer()
        #    Create a cone.
        #
        objectArray = cmds.cone()
        #    Select the cone.
        #
        cmds.select( objectArray[0] )
        #    Create a layer but only put the nurbsCone in the layer.
        #    The nurbsConeShape will remain in the default layer
        #    as a result of specifying the -nr/noRecurse flag.
        #
        #    Note also that you can specify the name of the layer
        #    with the -n/name flag.
        #
        cmds.createDisplayLayer( noRecurse=True, name='ExampleLayer' )
    ```

    ---
    - Args:
        - empty (e): If set then create an empty display layer.  ie. Do not add the selected items to the new display layer.
        - makeCurrent (mc): If set then make the new display layer the current one.
        - name (n): Name of the new display layer being created.
        - noRecurse (nr): If set then only add selected objects to the display layer.  Otherwise all descendants of the selected objects will also be added.
        - number (num): Number for the new display layer being created.
    """
@overload #Overload for createDisplayLayer in ['create']
def createDisplayLayer(e: bool = ..., mc: bool = ..., n: str = ..., nr: bool = ..., num: int = ...) -> str:
    """createDisplayLayer is undoable, NOT queryable, and NOT editable.
    
    Create a new display layer. The display layer number will be assigned based on
    the first unassigned number not less than the base index number found in the
    display layer global parameters. Normally all objects and their descendants
    will be added to the new display layer but if the '-nr' flag is specified then
    only the objects themselves will be added.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a sphere.
        #
        objectArray = cmds.sphere()
        #    Select the sphere.
        #
        cmds.select( objectArray[0] )
        #    Create a layer. The selected object will be placed
        #    in this layer. Note in this case both the nurbsSphere
        #    and nurbsSphere shape are placed in the layer.
        #
        cmds.createDisplayLayer()
        #    Create a cone.
        #
        objectArray = cmds.cone()
        #    Select the cone.
        #
        cmds.select( objectArray[0] )
        #    Create a layer but only put the nurbsCone in the layer.
        #    The nurbsConeShape will remain in the default layer
        #    as a result of specifying the -nr/noRecurse flag.
        #
        #    Note also that you can specify the name of the layer
        #    with the -n/name flag.
        #
        cmds.createDisplayLayer( noRecurse=True, name='ExampleLayer' )
    ```

    ---
    - Args:
        - empty (e): If set then create an empty display layer.  ie. Do not add the selected items to the new display layer.
        - makeCurrent (mc): If set then make the new display layer the current one.
        - name (n): Name of the new display layer being created.
        - noRecurse (nr): If set then only add selected objects to the display layer.  Otherwise all descendants of the selected objects will also be added.
        - number (num): Number for the new display layer being created.
    """
@overload #Overload for createDisplayLayer in ['create']
def createDisplayLayer(empty: bool = ..., e: bool = ..., makeCurrent: bool = ..., mc: bool = ..., name: str = ..., n: str = ..., noRecurse: bool = ..., nr: bool = ..., number: int = ..., num: int = ...) -> str:
    """createDisplayLayer is undoable, NOT queryable, and NOT editable.
    
    Create a new display layer. The display layer number will be assigned based on
    the first unassigned number not less than the base index number found in the
    display layer global parameters. Normally all objects and their descendants
    will be added to the new display layer but if the '-nr' flag is specified then
    only the objects themselves will be added.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a sphere.
        #
        objectArray = cmds.sphere()
        #    Select the sphere.
        #
        cmds.select( objectArray[0] )
        #    Create a layer. The selected object will be placed
        #    in this layer. Note in this case both the nurbsSphere
        #    and nurbsSphere shape are placed in the layer.
        #
        cmds.createDisplayLayer()
        #    Create a cone.
        #
        objectArray = cmds.cone()
        #    Select the cone.
        #
        cmds.select( objectArray[0] )
        #    Create a layer but only put the nurbsCone in the layer.
        #    The nurbsConeShape will remain in the default layer
        #    as a result of specifying the -nr/noRecurse flag.
        #
        #    Note also that you can specify the name of the layer
        #    with the -n/name flag.
        #
        cmds.createDisplayLayer( noRecurse=True, name='ExampleLayer' )
    ```

    ---
    - Args:
        - empty (e): If set then create an empty display layer.  ie. Do not add the selected items to the new display layer.
        - makeCurrent (mc): If set then make the new display layer the current one.
        - name (n): Name of the new display layer being created.
        - noRecurse (nr): If set then only add selected objects to the display layer.  Otherwise all descendants of the selected objects will also be added.
        - number (num): Number for the new display layer being created.
    """
