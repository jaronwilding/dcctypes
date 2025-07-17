"""Stub files for Attributes category in Maya commands, command: isDirty."""

from typing import Any, overload

@overload #Overload for isDirty in ['create']
def isDirty(string...: string..., connection: bool = ..., datablock: bool = ...) -> bool:
    """isDirty is undoable, NOT queryable, and NOT editable.
    
    The isDirty command is used to check if a plug is dirty. The return value is 0
    if it is not and 1 if it is. If more than one plug is specified then the
    result is the logical "or" of all objects (ie. returns 1 if *any* of the plugs
    are dirty).

    Example:
    ```python
        import maya.cmds as cmds
        # Create a plusMinusAverage node and a transform. We set the 'skipSelect'
        # flag so that they are not displayed in the Attribute Editor because
        # that would force an evaluation and cause the plugs to become clean.
        import maya.cmds as cmds
        cmds.createNode('plusMinusAverage', n='pma', skipSelect=True)
        cmds.createNode('transform', n='t', skipSelect=True)
        # Hide the transform so that Maya's draw won't force an evaluation which
        # would clean its plugs.
        cmds.hide('t')
        # Connect the transform's 'tx' to one of the plusMinusAverage node's
        # inputs.
        cmds.connectAttr('t.tx', 'pma.input1D[0]')
        # Set the value of the transform's 'tx' and check that the
        # target of the connection has become dirty.
        cmds.setAttr('t.tx', 13)
        cmds.isDirty('pma.input1D[0]')
        # Result: 1 #
        # If we retrieve the value of the destination attribute
        # then the connection becomes clean.
        cmds.getAttr('pma.input1D[0]')
        # Result: 13.0 #
        cmds.isDirty('pma.input1D[0]')
        # Result: 0 #
        # A plusMinusAverage node's 'output1D' attribute depends
        # upon the values in its 'input1D' array. Since we haven't
        # retrieved its value yet, it should still be dirty. However,
        # it seems to be clean:
        cmds.isDirty('pma.output1D')
        # Result: 0 #
        # The reason for this is that the 'isDirty' command
        # by default only checks connections and 'output1D' has
        # no connection to be dirty. If we instead check its
        # value in the datablock, we get the expected result:
        cmds.isDirty('pma.output1D', d=True)
        # Result: 1 #
        # The output value will remain dirty until we
        # force its evaluation by retrieving it.
        cmds.getAttr('pma.output1D')
        # Result: 13.0 #
        cmds.isDirty('pma.output1D', d=True)
        # Result: 0 #
    ```

    ---
    - Args:
        - string...: Input item(s).
        - connection (c): Check the connection of the plug (default).
        - datablock (d): Check the datablock entry for the plug.
    """
@overload #Overload for isDirty in ['create']
def isDirty(string...: string..., c: bool = ..., d: bool = ...) -> bool:
    """isDirty is undoable, NOT queryable, and NOT editable.
    
    The isDirty command is used to check if a plug is dirty. The return value is 0
    if it is not and 1 if it is. If more than one plug is specified then the
    result is the logical "or" of all objects (ie. returns 1 if *any* of the plugs
    are dirty).

    Example:
    ```python
        import maya.cmds as cmds
        # Create a plusMinusAverage node and a transform. We set the 'skipSelect'
        # flag so that they are not displayed in the Attribute Editor because
        # that would force an evaluation and cause the plugs to become clean.
        import maya.cmds as cmds
        cmds.createNode('plusMinusAverage', n='pma', skipSelect=True)
        cmds.createNode('transform', n='t', skipSelect=True)
        # Hide the transform so that Maya's draw won't force an evaluation which
        # would clean its plugs.
        cmds.hide('t')
        # Connect the transform's 'tx' to one of the plusMinusAverage node's
        # inputs.
        cmds.connectAttr('t.tx', 'pma.input1D[0]')
        # Set the value of the transform's 'tx' and check that the
        # target of the connection has become dirty.
        cmds.setAttr('t.tx', 13)
        cmds.isDirty('pma.input1D[0]')
        # Result: 1 #
        # If we retrieve the value of the destination attribute
        # then the connection becomes clean.
        cmds.getAttr('pma.input1D[0]')
        # Result: 13.0 #
        cmds.isDirty('pma.input1D[0]')
        # Result: 0 #
        # A plusMinusAverage node's 'output1D' attribute depends
        # upon the values in its 'input1D' array. Since we haven't
        # retrieved its value yet, it should still be dirty. However,
        # it seems to be clean:
        cmds.isDirty('pma.output1D')
        # Result: 0 #
        # The reason for this is that the 'isDirty' command
        # by default only checks connections and 'output1D' has
        # no connection to be dirty. If we instead check its
        # value in the datablock, we get the expected result:
        cmds.isDirty('pma.output1D', d=True)
        # Result: 1 #
        # The output value will remain dirty until we
        # force its evaluation by retrieving it.
        cmds.getAttr('pma.output1D')
        # Result: 13.0 #
        cmds.isDirty('pma.output1D', d=True)
        # Result: 0 #
    ```

    ---
    - Args:
        - string...: Input item(s).
        - connection (c): Check the connection of the plug (default).
        - datablock (d): Check the datablock entry for the plug.
    """
@overload #Overload for isDirty in ['create']
def isDirty(string...: string..., connection: bool = ..., c: bool = ..., datablock: bool = ..., d: bool = ...) -> bool:
    """isDirty is undoable, NOT queryable, and NOT editable.
    
    The isDirty command is used to check if a plug is dirty. The return value is 0
    if it is not and 1 if it is. If more than one plug is specified then the
    result is the logical "or" of all objects (ie. returns 1 if *any* of the plugs
    are dirty).

    Example:
    ```python
        import maya.cmds as cmds
        # Create a plusMinusAverage node and a transform. We set the 'skipSelect'
        # flag so that they are not displayed in the Attribute Editor because
        # that would force an evaluation and cause the plugs to become clean.
        import maya.cmds as cmds
        cmds.createNode('plusMinusAverage', n='pma', skipSelect=True)
        cmds.createNode('transform', n='t', skipSelect=True)
        # Hide the transform so that Maya's draw won't force an evaluation which
        # would clean its plugs.
        cmds.hide('t')
        # Connect the transform's 'tx' to one of the plusMinusAverage node's
        # inputs.
        cmds.connectAttr('t.tx', 'pma.input1D[0]')
        # Set the value of the transform's 'tx' and check that the
        # target of the connection has become dirty.
        cmds.setAttr('t.tx', 13)
        cmds.isDirty('pma.input1D[0]')
        # Result: 1 #
        # If we retrieve the value of the destination attribute
        # then the connection becomes clean.
        cmds.getAttr('pma.input1D[0]')
        # Result: 13.0 #
        cmds.isDirty('pma.input1D[0]')
        # Result: 0 #
        # A plusMinusAverage node's 'output1D' attribute depends
        # upon the values in its 'input1D' array. Since we haven't
        # retrieved its value yet, it should still be dirty. However,
        # it seems to be clean:
        cmds.isDirty('pma.output1D')
        # Result: 0 #
        # The reason for this is that the 'isDirty' command
        # by default only checks connections and 'output1D' has
        # no connection to be dirty. If we instead check its
        # value in the datablock, we get the expected result:
        cmds.isDirty('pma.output1D', d=True)
        # Result: 1 #
        # The output value will remain dirty until we
        # force its evaluation by retrieving it.
        cmds.getAttr('pma.output1D')
        # Result: 13.0 #
        cmds.isDirty('pma.output1D', d=True)
        # Result: 0 #
    ```

    ---
    - Args:
        - string...: Input item(s).
        - connection (c): Check the connection of the plug (default).
        - datablock (d): Check the datablock entry for the plug.
    """
