"""Stub files for General category in Maya commands, command: containerPublish."""

from typing import Any, overload

@overload #Overload for containerPublish in ['create']
def containerPublish(bindNode: [string, string] = ..., bindTemplateStandins: bool = ..., inConnections: bool = ..., mergeShared: bool = ..., outConnections: bool = ..., publishNode: [string, string] = ..., unbindNode: str = ..., unpublishNode: str = ...) -> None:
    """containerPublish is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    advanced publishing operations on the container. For example, the
    "publishConnections" flag on the container will publish all the connections,
    but this command can be used to publish just the inputs, outputs, or to
    collapse the shared inputs into a single attribute before publishing.

    ---
    - Args:
        - bindNode (bn): Bind the specified node to the published node name.
        - bindTemplateStandins (bts): This flag will create a temporary stand-in attribute for any attributes that exist in the template but are not already bound. This enables you to set values for unbound attributes.
        - inConnections (ic): Specifies that the unpublished connections to nodes in the container from external nodes should be published.
        - mergeShared (ms): For use with the inConnections flag. Indicates that when an external attribute connects to multiple internal attributes within the container, a single published attribute should be used to correspond to all of the internal attributes.
        - outConnections (oc): Specifies that the unpublished connections from nodes in the container to external nodes should be published.
        - publishNode (pn): Publish a name and type. When first published, nothing will be bound. To bind a node to the published name, use the bindNode flag.
        - unbindNode (ubn): Unbind the node that is published with the name specified by the flag.
        - unpublishNode (upn): Unpublish the specified published node name.
    """
@overload #Overload for containerPublish in ['create']
def containerPublish(bn: [string, string] = ..., bts: bool = ..., ic: bool = ..., ms: bool = ..., oc: bool = ..., pn: [string, string] = ..., ubn: str = ..., upn: str = ...) -> None:
    """containerPublish is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    advanced publishing operations on the container. For example, the
    "publishConnections" flag on the container will publish all the connections,
    but this command can be used to publish just the inputs, outputs, or to
    collapse the shared inputs into a single attribute before publishing.

    ---
    - Args:
        - bindNode (bn): Bind the specified node to the published node name.
        - bindTemplateStandins (bts): This flag will create a temporary stand-in attribute for any attributes that exist in the template but are not already bound. This enables you to set values for unbound attributes.
        - inConnections (ic): Specifies that the unpublished connections to nodes in the container from external nodes should be published.
        - mergeShared (ms): For use with the inConnections flag. Indicates that when an external attribute connects to multiple internal attributes within the container, a single published attribute should be used to correspond to all of the internal attributes.
        - outConnections (oc): Specifies that the unpublished connections from nodes in the container to external nodes should be published.
        - publishNode (pn): Publish a name and type. When first published, nothing will be bound. To bind a node to the published name, use the bindNode flag.
        - unbindNode (ubn): Unbind the node that is published with the name specified by the flag.
        - unpublishNode (upn): Unpublish the specified published node name.
    """
@overload #Overload for containerPublish in ['create']
def containerPublish(bindNode: [string, string] = ..., bn: [string, string] = ..., bindTemplateStandins: bool = ..., bts: bool = ..., inConnections: bool = ..., ic: bool = ..., mergeShared: bool = ..., ms: bool = ..., outConnections: bool = ..., oc: bool = ..., publishNode: [string, string] = ..., pn: [string, string] = ..., unbindNode: str = ..., ubn: str = ..., unpublishNode: str = ..., upn: str = ...) -> None:
    """containerPublish is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    advanced publishing operations on the container. For example, the
    "publishConnections" flag on the container will publish all the connections,
    but this command can be used to publish just the inputs, outputs, or to
    collapse the shared inputs into a single attribute before publishing.

    ---
    - Args:
        - bindNode (bn): Bind the specified node to the published node name.
        - bindTemplateStandins (bts): This flag will create a temporary stand-in attribute for any attributes that exist in the template but are not already bound. This enables you to set values for unbound attributes.
        - inConnections (ic): Specifies that the unpublished connections to nodes in the container from external nodes should be published.
        - mergeShared (ms): For use with the inConnections flag. Indicates that when an external attribute connects to multiple internal attributes within the container, a single published attribute should be used to correspond to all of the internal attributes.
        - outConnections (oc): Specifies that the unpublished connections from nodes in the container to external nodes should be published.
        - publishNode (pn): Publish a name and type. When first published, nothing will be bound. To bind a node to the published name, use the bindNode flag.
        - unbindNode (ubn): Unbind the node that is published with the name specified by the flag.
        - unpublishNode (upn): Unpublish the specified published node name.
    """
@overload #Overload for containerPublish in ['query']
def containerPublish(bindNode: [string, string] = ..., bindTemplateStandins: bool = ..., publishNode: [string, string] = ..., unbindNode: str = ..., unpublishNode: str = ..., query: bool = ...) -> None:
    """containerPublish is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    advanced publishing operations on the container. For example, the
    "publishConnections" flag on the container will publish all the connections,
    but this command can be used to publish just the inputs, outputs, or to
    collapse the shared inputs into a single attribute before publishing.

    ---
    - Args:
        - bindNode (bn): Bind the specified node to the published node name.
        - bindTemplateStandins (bts): This flag will create a temporary stand-in attribute for any attributes that exist in the template but are not already bound. This enables you to set values for unbound attributes.
        - publishNode (pn): Publish a name and type. When first published, nothing will be bound. To bind a node to the published name, use the bindNode flag.
        - unbindNode (ubn): Unbind the node that is published with the name specified by the flag.
        - unpublishNode (upn): Unpublish the specified published node name.
        - query (q): Query mode flag
    """
@overload #Overload for containerPublish in ['query']
def containerPublish(bn: [string, string] = ..., bts: bool = ..., pn: [string, string] = ..., ubn: str = ..., upn: str = ..., q: bool = ...) -> None:
    """containerPublish is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    advanced publishing operations on the container. For example, the
    "publishConnections" flag on the container will publish all the connections,
    but this command can be used to publish just the inputs, outputs, or to
    collapse the shared inputs into a single attribute before publishing.

    ---
    - Args:
        - bindNode (bn): Bind the specified node to the published node name.
        - bindTemplateStandins (bts): This flag will create a temporary stand-in attribute for any attributes that exist in the template but are not already bound. This enables you to set values for unbound attributes.
        - publishNode (pn): Publish a name and type. When first published, nothing will be bound. To bind a node to the published name, use the bindNode flag.
        - unbindNode (ubn): Unbind the node that is published with the name specified by the flag.
        - unpublishNode (upn): Unpublish the specified published node name.
        - query (q): Query mode flag
    """
@overload #Overload for containerPublish in ['query']
def containerPublish(bindNode: [string, string] = ..., bn: [string, string] = ..., bindTemplateStandins: bool = ..., bts: bool = ..., publishNode: [string, string] = ..., pn: [string, string] = ..., unbindNode: str = ..., ubn: str = ..., unpublishNode: str = ..., upn: str = ..., query: bool = ..., q: bool = ...) -> None:
    """containerPublish is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    advanced publishing operations on the container. For example, the
    "publishConnections" flag on the container will publish all the connections,
    but this command can be used to publish just the inputs, outputs, or to
    collapse the shared inputs into a single attribute before publishing.

    ---
    - Args:
        - bindNode (bn): Bind the specified node to the published node name.
        - bindTemplateStandins (bts): This flag will create a temporary stand-in attribute for any attributes that exist in the template but are not already bound. This enables you to set values for unbound attributes.
        - publishNode (pn): Publish a name and type. When first published, nothing will be bound. To bind a node to the published name, use the bindNode flag.
        - unbindNode (ubn): Unbind the node that is published with the name specified by the flag.
        - unpublishNode (upn): Unpublish the specified published node name.
        - query (q): Query mode flag
    """
@overload #Overload for containerPublish in ['edit']
def containerPublish(bindNode: [string, string] = ..., bindTemplateStandins: bool = ..., publishNode: [string, string] = ..., unbindNode: str = ..., unpublishNode: str = ..., edit: bool = ...) -> None:
    """containerPublish is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    advanced publishing operations on the container. For example, the
    "publishConnections" flag on the container will publish all the connections,
    but this command can be used to publish just the inputs, outputs, or to
    collapse the shared inputs into a single attribute before publishing.

    ---
    - Args:
        - bindNode (bn): Bind the specified node to the published node name.
        - bindTemplateStandins (bts): This flag will create a temporary stand-in attribute for any attributes that exist in the template but are not already bound. This enables you to set values for unbound attributes.
        - publishNode (pn): Publish a name and type. When first published, nothing will be bound. To bind a node to the published name, use the bindNode flag.
        - unbindNode (ubn): Unbind the node that is published with the name specified by the flag.
        - unpublishNode (upn): Unpublish the specified published node name.
        - edit (e): Edit mode flag
    """
@overload #Overload for containerPublish in ['edit']
def containerPublish(bn: [string, string] = ..., bts: bool = ..., pn: [string, string] = ..., ubn: str = ..., upn: str = ..., e: bool = ...) -> None:
    """containerPublish is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    advanced publishing operations on the container. For example, the
    "publishConnections" flag on the container will publish all the connections,
    but this command can be used to publish just the inputs, outputs, or to
    collapse the shared inputs into a single attribute before publishing.

    ---
    - Args:
        - bindNode (bn): Bind the specified node to the published node name.
        - bindTemplateStandins (bts): This flag will create a temporary stand-in attribute for any attributes that exist in the template but are not already bound. This enables you to set values for unbound attributes.
        - publishNode (pn): Publish a name and type. When first published, nothing will be bound. To bind a node to the published name, use the bindNode flag.
        - unbindNode (ubn): Unbind the node that is published with the name specified by the flag.
        - unpublishNode (upn): Unpublish the specified published node name.
        - edit (e): Edit mode flag
    """
@overload #Overload for containerPublish in ['edit']
def containerPublish(bindNode: [string, string] = ..., bn: [string, string] = ..., bindTemplateStandins: bool = ..., bts: bool = ..., publishNode: [string, string] = ..., pn: [string, string] = ..., unbindNode: str = ..., ubn: str = ..., unpublishNode: str = ..., upn: str = ..., edit: bool = ..., e: bool = ...) -> None:
    """containerPublish is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    advanced publishing operations on the container. For example, the
    "publishConnections" flag on the container will publish all the connections,
    but this command can be used to publish just the inputs, outputs, or to
    collapse the shared inputs into a single attribute before publishing.

    ---
    - Args:
        - bindNode (bn): Bind the specified node to the published node name.
        - bindTemplateStandins (bts): This flag will create a temporary stand-in attribute for any attributes that exist in the template but are not already bound. This enables you to set values for unbound attributes.
        - publishNode (pn): Publish a name and type. When first published, nothing will be bound. To bind a node to the published name, use the bindNode flag.
        - unbindNode (ubn): Unbind the node that is published with the name specified by the flag.
        - unpublishNode (upn): Unpublish the specified published node name.
        - edit (e): Edit mode flag
    """
