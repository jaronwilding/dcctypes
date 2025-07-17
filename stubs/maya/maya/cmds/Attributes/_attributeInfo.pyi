"""Stub files for Attributes category in Maya commands, command: attributeInfo."""

from typing import Any, overload

@overload #Overload for attributeInfo in ['create']
def attributeInfo(allAttributes: bool = ..., bool: bool = ..., enumerated: bool = ..., hidden: bool = ..., inherited: bool = ..., internal: bool = ..., leaf: bool = ..., logicalAnd: bool = ..., multi: bool = ..., short: bool = ..., type: str = ..., userInterface: bool = ..., writable: bool = ...) -> list[str]:
    """attributeInfo is NOT undoable, NOT queryable, and NOT editable.
    
    This command lists all of the attributes that are marked with certain flags.
    Combinations of flags may be specified and all will be considered. (The method
    of combination depends on the state of the "logicalAnd/and" flag.) When the
    "allAttributes/all" flag is specified, attributes of all types will be listed.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.createNode( 'choice' )
        # Get the list of only hidden choice node attributes
        #
        cmds.attributeInfo( h=True, t='choice' )
        # Result: [u'message', u'isHistoricallyInteresting', u'binMembership'] #
        # Get the list of all attributes on choice nodes
        cmds.attributeInfo( all=True, t='choice' )
        # Result: [u'message', u'caching', u'isHistoricallyInteresting', u'nodeState', u'binMembership', u'selector', u'input', u'output'] #
        # Get the list of boolean or enumerated transform node attributes
        #
        cmds.attributeInfo( b=True, e=True, t='transform' )
        # Result: [u'caching', u'nodeState', u'visibility', u'intermediateObject', u'template', u'ghosting', u'useObjectColor', u'overrideDisplayType', u'overrideLevelOfDetail', u'overrideShading', u'overrideTexturing', u'overridePlayback', u'overrideEnabled', u'overrideVisibility', u'lodVisibility', u'layerRenderable', u'renderLayerRenderable', u'ghostingMode', u'rotateOrder', u'minTransXLimitEnable', u'minTransYLimitEnable', u'minTransZLimitEnable', u'maxTransXLimitEnable', u'maxTransYLimitEnable', u'maxTransZLimitEnable', u'minRotXLimitEnable', u'minRotYLimitEnable', u'minRotZLimitEnable', u'maxRotXLimitEnable', u'maxRotYLimitEnable', u'maxRotZLimitEnable', u'minScaleXLimitEnable', u'minScaleYLimitEnable', u'minScaleZLimitEnable', u'maxScaleXLimitEnable', u'maxScaleYLimitEnable', u'maxScaleZLimitEnable', u'inheritsTransform', u'displayHandle', u'displayScalePivot', u'displayRotatePivot', u'displayLocalAxis', u'dynamics', u'showManipDefault', u'rotationInterpolation', u'miDeriveFromMaya', u'miHide', u'miVisible', u'miTrace', u'miShadow', u'miCaustic', u'miGlobillum', u'miExportGeoShader'] #
        # Get the list of short names of enumerated attributes on a particular choice
        # node.
        #
        cmds.attributeInfo( 'choice1', s=True, e=True )
        # Result: message input output selector
        # Get the list of hidden or internal attributes on one particular choice node
        # using the UI name for the attributes (that is the one that will show up
        # in the attribute editor).
        #
        cmds.attributeInfo( 'choice1', ui=True, h=True, i=True )
        # Result: [u'Message', u'Caching', u'Is Historically Interesting', u'Node State', u'Bin Membership'] #
    ```

    ---
    - Args:
        - allAttributes (all): Show all attributes associated with the node regardless of type. Use of this flag overrides any other attribute type flags and logical operation that may be specified on the command.
        - bool (b): Show the attributes that are of type boolean. Use the 'on' state to get only boolean attributes; the 'off' state to ignore boolean attributes.
        - enumerated (e): Show the attributes that are of type enumerated. Use the 'on' state to get only enumerated attributes; the 'off' state to ignore enumerated attributes.
        - hidden (h): Show the attributes that are marked as hidden. Use the 'on' state to get hidden attributes; the 'off' state to get non-hidden attributes.
        - inherited: Filter the attributes based on whether they belong to the node type directly or have been inherited from a root type (e.g. meshShape/direct or dagObject/inherited). Use the 'on' state to get only inherited attributes, the 'off' state to get
            only directly owned attributes, and leave the flag unspecified to get both.
        - internal (i): Show the attributes that are marked as internal to the node. Use the 'on' state to get internal attributes; the 'off' state to get non-internal attributes.
        - leaf (l): Show the attributes that are complex leaves (ie. that have parent attributes and have no children themselves). Use the 'on' state to get leaf attributes; the 'off' state to get non-leaf attributes.
        - logicalAnd: The default is to take the logical 'or' of the above conditions. Specifying this flag switches to the logical 'and' instead.
        - multi (m): Show the attributes that are multis. Use the 'on' state to get multi attributes; the 'off' state to get non-multi attributes.
        - short (s): Show the short attribute names instead of the long names.
        - type (t): static node type from which to get 'affects' information
        - userInterface (ui): Show the UI-friendly attribute names instead of the Maya ASCII names. Takes precedence over the -s/-short flag if both are specified.
        - writable (w): Show the attributes that are writable (ie. can have input connections). Use the 'on' state to get writable attributes; the 'off' state to get non-writable attributes.
    """
@overload #Overload for attributeInfo in ['create']
def attributeInfo(all: bool = ..., b: bool = ..., e: bool = ..., h: bool = ..., i: bool = ..., l: bool = ..., m: bool = ..., s: bool = ..., t: str = ..., ui: bool = ..., w: bool = ...) -> list[str]:
    """attributeInfo is NOT undoable, NOT queryable, and NOT editable.
    
    This command lists all of the attributes that are marked with certain flags.
    Combinations of flags may be specified and all will be considered. (The method
    of combination depends on the state of the "logicalAnd/and" flag.) When the
    "allAttributes/all" flag is specified, attributes of all types will be listed.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.createNode( 'choice' )
        # Get the list of only hidden choice node attributes
        #
        cmds.attributeInfo( h=True, t='choice' )
        # Result: [u'message', u'isHistoricallyInteresting', u'binMembership'] #
        # Get the list of all attributes on choice nodes
        cmds.attributeInfo( all=True, t='choice' )
        # Result: [u'message', u'caching', u'isHistoricallyInteresting', u'nodeState', u'binMembership', u'selector', u'input', u'output'] #
        # Get the list of boolean or enumerated transform node attributes
        #
        cmds.attributeInfo( b=True, e=True, t='transform' )
        # Result: [u'caching', u'nodeState', u'visibility', u'intermediateObject', u'template', u'ghosting', u'useObjectColor', u'overrideDisplayType', u'overrideLevelOfDetail', u'overrideShading', u'overrideTexturing', u'overridePlayback', u'overrideEnabled', u'overrideVisibility', u'lodVisibility', u'layerRenderable', u'renderLayerRenderable', u'ghostingMode', u'rotateOrder', u'minTransXLimitEnable', u'minTransYLimitEnable', u'minTransZLimitEnable', u'maxTransXLimitEnable', u'maxTransYLimitEnable', u'maxTransZLimitEnable', u'minRotXLimitEnable', u'minRotYLimitEnable', u'minRotZLimitEnable', u'maxRotXLimitEnable', u'maxRotYLimitEnable', u'maxRotZLimitEnable', u'minScaleXLimitEnable', u'minScaleYLimitEnable', u'minScaleZLimitEnable', u'maxScaleXLimitEnable', u'maxScaleYLimitEnable', u'maxScaleZLimitEnable', u'inheritsTransform', u'displayHandle', u'displayScalePivot', u'displayRotatePivot', u'displayLocalAxis', u'dynamics', u'showManipDefault', u'rotationInterpolation', u'miDeriveFromMaya', u'miHide', u'miVisible', u'miTrace', u'miShadow', u'miCaustic', u'miGlobillum', u'miExportGeoShader'] #
        # Get the list of short names of enumerated attributes on a particular choice
        # node.
        #
        cmds.attributeInfo( 'choice1', s=True, e=True )
        # Result: message input output selector
        # Get the list of hidden or internal attributes on one particular choice node
        # using the UI name for the attributes (that is the one that will show up
        # in the attribute editor).
        #
        cmds.attributeInfo( 'choice1', ui=True, h=True, i=True )
        # Result: [u'Message', u'Caching', u'Is Historically Interesting', u'Node State', u'Bin Membership'] #
    ```

    ---
    - Args:
        - allAttributes (all): Show all attributes associated with the node regardless of type. Use of this flag overrides any other attribute type flags and logical operation that may be specified on the command.
        - bool (b): Show the attributes that are of type boolean. Use the 'on' state to get only boolean attributes; the 'off' state to ignore boolean attributes.
        - enumerated (e): Show the attributes that are of type enumerated. Use the 'on' state to get only enumerated attributes; the 'off' state to ignore enumerated attributes.
        - hidden (h): Show the attributes that are marked as hidden. Use the 'on' state to get hidden attributes; the 'off' state to get non-hidden attributes.
        - inherited: Filter the attributes based on whether they belong to the node type directly or have been inherited from a root type (e.g. meshShape/direct or dagObject/inherited). Use the 'on' state to get only inherited attributes, the 'off' state to get
            only directly owned attributes, and leave the flag unspecified to get both.
        - internal (i): Show the attributes that are marked as internal to the node. Use the 'on' state to get internal attributes; the 'off' state to get non-internal attributes.
        - leaf (l): Show the attributes that are complex leaves (ie. that have parent attributes and have no children themselves). Use the 'on' state to get leaf attributes; the 'off' state to get non-leaf attributes.
        - logicalAnd: The default is to take the logical 'or' of the above conditions. Specifying this flag switches to the logical 'and' instead.
        - multi (m): Show the attributes that are multis. Use the 'on' state to get multi attributes; the 'off' state to get non-multi attributes.
        - short (s): Show the short attribute names instead of the long names.
        - type (t): static node type from which to get 'affects' information
        - userInterface (ui): Show the UI-friendly attribute names instead of the Maya ASCII names. Takes precedence over the -s/-short flag if both are specified.
        - writable (w): Show the attributes that are writable (ie. can have input connections). Use the 'on' state to get writable attributes; the 'off' state to get non-writable attributes.
    """
@overload #Overload for attributeInfo in ['create']
def attributeInfo(allAttributes: bool = ..., all: bool = ..., bool: bool = ..., b: bool = ..., enumerated: bool = ..., e: bool = ..., hidden: bool = ..., h: bool = ..., inherited: bool = ..., internal: bool = ..., i: bool = ..., leaf: bool = ..., l: bool = ..., logicalAnd: bool = ..., multi: bool = ..., m: bool = ..., short: bool = ..., s: bool = ..., type: str = ..., t: str = ..., userInterface: bool = ..., ui: bool = ..., writable: bool = ..., w: bool = ...) -> list[str]:
    """attributeInfo is NOT undoable, NOT queryable, and NOT editable.
    
    This command lists all of the attributes that are marked with certain flags.
    Combinations of flags may be specified and all will be considered. (The method
    of combination depends on the state of the "logicalAnd/and" flag.) When the
    "allAttributes/all" flag is specified, attributes of all types will be listed.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.createNode( 'choice' )
        # Get the list of only hidden choice node attributes
        #
        cmds.attributeInfo( h=True, t='choice' )
        # Result: [u'message', u'isHistoricallyInteresting', u'binMembership'] #
        # Get the list of all attributes on choice nodes
        cmds.attributeInfo( all=True, t='choice' )
        # Result: [u'message', u'caching', u'isHistoricallyInteresting', u'nodeState', u'binMembership', u'selector', u'input', u'output'] #
        # Get the list of boolean or enumerated transform node attributes
        #
        cmds.attributeInfo( b=True, e=True, t='transform' )
        # Result: [u'caching', u'nodeState', u'visibility', u'intermediateObject', u'template', u'ghosting', u'useObjectColor', u'overrideDisplayType', u'overrideLevelOfDetail', u'overrideShading', u'overrideTexturing', u'overridePlayback', u'overrideEnabled', u'overrideVisibility', u'lodVisibility', u'layerRenderable', u'renderLayerRenderable', u'ghostingMode', u'rotateOrder', u'minTransXLimitEnable', u'minTransYLimitEnable', u'minTransZLimitEnable', u'maxTransXLimitEnable', u'maxTransYLimitEnable', u'maxTransZLimitEnable', u'minRotXLimitEnable', u'minRotYLimitEnable', u'minRotZLimitEnable', u'maxRotXLimitEnable', u'maxRotYLimitEnable', u'maxRotZLimitEnable', u'minScaleXLimitEnable', u'minScaleYLimitEnable', u'minScaleZLimitEnable', u'maxScaleXLimitEnable', u'maxScaleYLimitEnable', u'maxScaleZLimitEnable', u'inheritsTransform', u'displayHandle', u'displayScalePivot', u'displayRotatePivot', u'displayLocalAxis', u'dynamics', u'showManipDefault', u'rotationInterpolation', u'miDeriveFromMaya', u'miHide', u'miVisible', u'miTrace', u'miShadow', u'miCaustic', u'miGlobillum', u'miExportGeoShader'] #
        # Get the list of short names of enumerated attributes on a particular choice
        # node.
        #
        cmds.attributeInfo( 'choice1', s=True, e=True )
        # Result: message input output selector
        # Get the list of hidden or internal attributes on one particular choice node
        # using the UI name for the attributes (that is the one that will show up
        # in the attribute editor).
        #
        cmds.attributeInfo( 'choice1', ui=True, h=True, i=True )
        # Result: [u'Message', u'Caching', u'Is Historically Interesting', u'Node State', u'Bin Membership'] #
    ```

    ---
    - Args:
        - allAttributes (all): Show all attributes associated with the node regardless of type. Use of this flag overrides any other attribute type flags and logical operation that may be specified on the command.
        - bool (b): Show the attributes that are of type boolean. Use the 'on' state to get only boolean attributes; the 'off' state to ignore boolean attributes.
        - enumerated (e): Show the attributes that are of type enumerated. Use the 'on' state to get only enumerated attributes; the 'off' state to ignore enumerated attributes.
        - hidden (h): Show the attributes that are marked as hidden. Use the 'on' state to get hidden attributes; the 'off' state to get non-hidden attributes.
        - inherited: Filter the attributes based on whether they belong to the node type directly or have been inherited from a root type (e.g. meshShape/direct or dagObject/inherited). Use the 'on' state to get only inherited attributes, the 'off' state to get
            only directly owned attributes, and leave the flag unspecified to get both.
        - internal (i): Show the attributes that are marked as internal to the node. Use the 'on' state to get internal attributes; the 'off' state to get non-internal attributes.
        - leaf (l): Show the attributes that are complex leaves (ie. that have parent attributes and have no children themselves). Use the 'on' state to get leaf attributes; the 'off' state to get non-leaf attributes.
        - logicalAnd: The default is to take the logical 'or' of the above conditions. Specifying this flag switches to the logical 'and' instead.
        - multi (m): Show the attributes that are multis. Use the 'on' state to get multi attributes; the 'off' state to get non-multi attributes.
        - short (s): Show the short attribute names instead of the long names.
        - type (t): static node type from which to get 'affects' information
        - userInterface (ui): Show the UI-friendly attribute names instead of the Maya ASCII names. Takes precedence over the -s/-short flag if both are specified.
        - writable (w): Show the attributes that are writable (ie. can have input connections). Use the 'on' state to get writable attributes; the 'off' state to get non-writable attributes.
    """
