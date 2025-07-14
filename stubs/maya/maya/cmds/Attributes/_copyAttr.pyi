"""Stub files for Attributes category in Maya commands, command: copyAttr."""

from typing import Any, overload

@overload #Overload for copyAttr in ['create']
def copyAttr(attribute: str = ..., containerParentChild: bool = ..., inConnections: bool = ..., keepSourceConnections: bool = ..., outConnections: bool = ..., renameTargetContainer: bool = ..., values: bool = ...) -> None:
    """copyAttr is undoable, queryable, and editable.
    
    Given two nodes, transfer the connections and/or the values from the first
    node to the second for all attributes whose names and data types match. When
    values are transferred, they are transferred directly. They are not mapped or
    modified in any way. The transferAttributes command can be used to transfer
    and remap some mesh attributes. The attributes flag can be used to specify a
    list of attributes to be processed. If the attributes flag is unused, all
    attributes will be processed. For dynamic attributes, the values and/or
    connections will only be transferred if the attributes names on both nodes
    match. This command does not support geometry shape nodes such as meshes,
    subds and nurbs. This command does not support transfer of multi-attribute
    values such as weight arrays.

    ---
    - Args:
        - attribute (at): The name of the attribute(s) for which connections and/or values will be transferred. If no attributes are specified, then all attributes will be transferred.
        - containerParentChild (cpc): For use when copying from one container to another only. This option indicates that the published parent and/or child relationships on the original container should be transferred to the target container if the published names match.
        - inConnections (ic): Indicates that incoming connections should be transferred.
        - keepSourceConnections (ksc): For use with the outConnections flag only. Indicates that the connections should be maintained on the first node, in addition to making them to the second node. If outConnections is used and keepSourceConnections is not used, the out
            connections on the source node will be broken and made to the target node.
        - outConnections (oc): Indicates that outgoing connections should be transferred.
        - renameTargetContainer (rtc): For use when copying from one container to another only. This option will rename the target container to the name of the original container, and rename the original container to its old name + "Orig". You would want to use this option if
            your original container was referenced and edited, and you want those edits from the main scene to now apply to the new container.
        - values (v): Indicates that values should be transferred.
    """
@overload #Overload for copyAttr in ['create']
def copyAttr(at: str = ..., cpc: bool = ..., ic: bool = ..., ksc: bool = ..., oc: bool = ..., rtc: bool = ..., v: bool = ...) -> None:
    """copyAttr is undoable, queryable, and editable.
    
    Given two nodes, transfer the connections and/or the values from the first
    node to the second for all attributes whose names and data types match. When
    values are transferred, they are transferred directly. They are not mapped or
    modified in any way. The transferAttributes command can be used to transfer
    and remap some mesh attributes. The attributes flag can be used to specify a
    list of attributes to be processed. If the attributes flag is unused, all
    attributes will be processed. For dynamic attributes, the values and/or
    connections will only be transferred if the attributes names on both nodes
    match. This command does not support geometry shape nodes such as meshes,
    subds and nurbs. This command does not support transfer of multi-attribute
    values such as weight arrays.

    ---
    - Args:
        - attribute (at): The name of the attribute(s) for which connections and/or values will be transferred. If no attributes are specified, then all attributes will be transferred.
        - containerParentChild (cpc): For use when copying from one container to another only. This option indicates that the published parent and/or child relationships on the original container should be transferred to the target container if the published names match.
        - inConnections (ic): Indicates that incoming connections should be transferred.
        - keepSourceConnections (ksc): For use with the outConnections flag only. Indicates that the connections should be maintained on the first node, in addition to making them to the second node. If outConnections is used and keepSourceConnections is not used, the out
            connections on the source node will be broken and made to the target node.
        - outConnections (oc): Indicates that outgoing connections should be transferred.
        - renameTargetContainer (rtc): For use when copying from one container to another only. This option will rename the target container to the name of the original container, and rename the original container to its old name + "Orig". You would want to use this option if
            your original container was referenced and edited, and you want those edits from the main scene to now apply to the new container.
        - values (v): Indicates that values should be transferred.
    """
@overload #Overload for copyAttr in ['create']
def copyAttr(attribute: str = ..., at: str = ..., containerParentChild: bool = ..., cpc: bool = ..., inConnections: bool = ..., ic: bool = ..., keepSourceConnections: bool = ..., ksc: bool = ..., outConnections: bool = ..., oc: bool = ..., renameTargetContainer: bool = ..., rtc: bool = ..., values: bool = ..., v: bool = ...) -> None:
    """copyAttr is undoable, queryable, and editable.
    
    Given two nodes, transfer the connections and/or the values from the first
    node to the second for all attributes whose names and data types match. When
    values are transferred, they are transferred directly. They are not mapped or
    modified in any way. The transferAttributes command can be used to transfer
    and remap some mesh attributes. The attributes flag can be used to specify a
    list of attributes to be processed. If the attributes flag is unused, all
    attributes will be processed. For dynamic attributes, the values and/or
    connections will only be transferred if the attributes names on both nodes
    match. This command does not support geometry shape nodes such as meshes,
    subds and nurbs. This command does not support transfer of multi-attribute
    values such as weight arrays.

    ---
    - Args:
        - attribute (at): The name of the attribute(s) for which connections and/or values will be transferred. If no attributes are specified, then all attributes will be transferred.
        - containerParentChild (cpc): For use when copying from one container to another only. This option indicates that the published parent and/or child relationships on the original container should be transferred to the target container if the published names match.
        - inConnections (ic): Indicates that incoming connections should be transferred.
        - keepSourceConnections (ksc): For use with the outConnections flag only. Indicates that the connections should be maintained on the first node, in addition to making them to the second node. If outConnections is used and keepSourceConnections is not used, the out
            connections on the source node will be broken and made to the target node.
        - outConnections (oc): Indicates that outgoing connections should be transferred.
        - renameTargetContainer (rtc): For use when copying from one container to another only. This option will rename the target container to the name of the original container, and rename the original container to its old name + "Orig". You would want to use this option if
            your original container was referenced and edited, and you want those edits from the main scene to now apply to the new container.
        - values (v): Indicates that values should be transferred.
    """
@overload #Overload for copyAttr in ['query']
def copyAttr(attribute: str = ..., query: bool = ...) -> None:
    """copyAttr is undoable, queryable, and editable.
    
    Given two nodes, transfer the connections and/or the values from the first
    node to the second for all attributes whose names and data types match. When
    values are transferred, they are transferred directly. They are not mapped or
    modified in any way. The transferAttributes command can be used to transfer
    and remap some mesh attributes. The attributes flag can be used to specify a
    list of attributes to be processed. If the attributes flag is unused, all
    attributes will be processed. For dynamic attributes, the values and/or
    connections will only be transferred if the attributes names on both nodes
    match. This command does not support geometry shape nodes such as meshes,
    subds and nurbs. This command does not support transfer of multi-attribute
    values such as weight arrays.

    ---
    - Args:
        - attribute (at): The name of the attribute(s) for which connections and/or values will be transferred. If no attributes are specified, then all attributes will be transferred.
        - query (q): Query mode flag
    """
@overload #Overload for copyAttr in ['query']
def copyAttr(at: str = ..., q: bool = ...) -> None:
    """copyAttr is undoable, queryable, and editable.
    
    Given two nodes, transfer the connections and/or the values from the first
    node to the second for all attributes whose names and data types match. When
    values are transferred, they are transferred directly. They are not mapped or
    modified in any way. The transferAttributes command can be used to transfer
    and remap some mesh attributes. The attributes flag can be used to specify a
    list of attributes to be processed. If the attributes flag is unused, all
    attributes will be processed. For dynamic attributes, the values and/or
    connections will only be transferred if the attributes names on both nodes
    match. This command does not support geometry shape nodes such as meshes,
    subds and nurbs. This command does not support transfer of multi-attribute
    values such as weight arrays.

    ---
    - Args:
        - attribute (at): The name of the attribute(s) for which connections and/or values will be transferred. If no attributes are specified, then all attributes will be transferred.
        - query (q): Query mode flag
    """
@overload #Overload for copyAttr in ['query']
def copyAttr(attribute: str = ..., at: str = ..., query: bool = ..., q: bool = ...) -> None:
    """copyAttr is undoable, queryable, and editable.
    
    Given two nodes, transfer the connections and/or the values from the first
    node to the second for all attributes whose names and data types match. When
    values are transferred, they are transferred directly. They are not mapped or
    modified in any way. The transferAttributes command can be used to transfer
    and remap some mesh attributes. The attributes flag can be used to specify a
    list of attributes to be processed. If the attributes flag is unused, all
    attributes will be processed. For dynamic attributes, the values and/or
    connections will only be transferred if the attributes names on both nodes
    match. This command does not support geometry shape nodes such as meshes,
    subds and nurbs. This command does not support transfer of multi-attribute
    values such as weight arrays.

    ---
    - Args:
        - attribute (at): The name of the attribute(s) for which connections and/or values will be transferred. If no attributes are specified, then all attributes will be transferred.
        - query (q): Query mode flag
    """
@overload #Overload for copyAttr in ['edit']
def copyAttr(attribute: str = ..., edit: bool = ...) -> None:
    """copyAttr is undoable, queryable, and editable.
    
    Given two nodes, transfer the connections and/or the values from the first
    node to the second for all attributes whose names and data types match. When
    values are transferred, they are transferred directly. They are not mapped or
    modified in any way. The transferAttributes command can be used to transfer
    and remap some mesh attributes. The attributes flag can be used to specify a
    list of attributes to be processed. If the attributes flag is unused, all
    attributes will be processed. For dynamic attributes, the values and/or
    connections will only be transferred if the attributes names on both nodes
    match. This command does not support geometry shape nodes such as meshes,
    subds and nurbs. This command does not support transfer of multi-attribute
    values such as weight arrays.

    ---
    - Args:
        - attribute (at): The name of the attribute(s) for which connections and/or values will be transferred. If no attributes are specified, then all attributes will be transferred.
        - edit (e): Edit mode flag
    """
@overload #Overload for copyAttr in ['edit']
def copyAttr(at: str = ..., e: bool = ...) -> None:
    """copyAttr is undoable, queryable, and editable.
    
    Given two nodes, transfer the connections and/or the values from the first
    node to the second for all attributes whose names and data types match. When
    values are transferred, they are transferred directly. They are not mapped or
    modified in any way. The transferAttributes command can be used to transfer
    and remap some mesh attributes. The attributes flag can be used to specify a
    list of attributes to be processed. If the attributes flag is unused, all
    attributes will be processed. For dynamic attributes, the values and/or
    connections will only be transferred if the attributes names on both nodes
    match. This command does not support geometry shape nodes such as meshes,
    subds and nurbs. This command does not support transfer of multi-attribute
    values such as weight arrays.

    ---
    - Args:
        - attribute (at): The name of the attribute(s) for which connections and/or values will be transferred. If no attributes are specified, then all attributes will be transferred.
        - edit (e): Edit mode flag
    """
@overload #Overload for copyAttr in ['edit']
def copyAttr(attribute: str = ..., at: str = ..., edit: bool = ..., e: bool = ...) -> None:
    """copyAttr is undoable, queryable, and editable.
    
    Given two nodes, transfer the connections and/or the values from the first
    node to the second for all attributes whose names and data types match. When
    values are transferred, they are transferred directly. They are not mapped or
    modified in any way. The transferAttributes command can be used to transfer
    and remap some mesh attributes. The attributes flag can be used to specify a
    list of attributes to be processed. If the attributes flag is unused, all
    attributes will be processed. For dynamic attributes, the values and/or
    connections will only be transferred if the attributes names on both nodes
    match. This command does not support geometry shape nodes such as meshes,
    subds and nurbs. This command does not support transfer of multi-attribute
    values such as weight arrays.

    ---
    - Args:
        - attribute (at): The name of the attribute(s) for which connections and/or values will be transferred. If no attributes are specified, then all attributes will be transferred.
        - edit (e): Edit mode flag
    """
