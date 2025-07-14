"""Stub files for General category in Maya commands, command: containerProxy."""

from typing import Any, overload

@overload #Overload for containerProxy in ['create']
def containerProxy(fromTemplate: str = ..., type: str = ...) -> None:
    """containerProxy is undoable, queryable, and editable.
    
    Creates a new container with the same published interface, dynamic attributes
    and attribute values as the specified container but with fewer container
    members. This proxy container can be used as a reference proxy so that values
    can be set on container attributes without loading in the full container. The
    proxy container will contain one or more locator nodes. The first locator has
    dynamic attributes that serve as stand-ins for the original published
    attributes. The remaining locators serve as stand-ins for any dag nodes that
    have been published as parent or as child and will be placed at the world
    space location of the published parent/child nodes. The expected usage of
    container proxies is to serve as a reference proxy for a referenced container.
    For automated creation, export and setup of the proxy see the
    doExportContainerProxy.mel script which is invoked by the "Export Container
    Proxy" menu item.

    ---
    - Args:
        - fromTemplate (ft): Specifies the name of a template file which will be used to create the new container proxy. Stand-in attributes will be created and published for all the numeric attributes on the proxy.
        - type (typ): Specifies the type of container node to use for the proxy. This flag is only valid in conjunction with the fromTemplate flag. When creating a proxy for an existing container, the type created will always be identical to that of the source
            container. The default value for this flag is 'container'.
    """
@overload #Overload for containerProxy in ['create']
def containerProxy(ft: str = ..., typ: str = ...) -> None:
    """containerProxy is undoable, queryable, and editable.
    
    Creates a new container with the same published interface, dynamic attributes
    and attribute values as the specified container but with fewer container
    members. This proxy container can be used as a reference proxy so that values
    can be set on container attributes without loading in the full container. The
    proxy container will contain one or more locator nodes. The first locator has
    dynamic attributes that serve as stand-ins for the original published
    attributes. The remaining locators serve as stand-ins for any dag nodes that
    have been published as parent or as child and will be placed at the world
    space location of the published parent/child nodes. The expected usage of
    container proxies is to serve as a reference proxy for a referenced container.
    For automated creation, export and setup of the proxy see the
    doExportContainerProxy.mel script which is invoked by the "Export Container
    Proxy" menu item.

    ---
    - Args:
        - fromTemplate (ft): Specifies the name of a template file which will be used to create the new container proxy. Stand-in attributes will be created and published for all the numeric attributes on the proxy.
        - type (typ): Specifies the type of container node to use for the proxy. This flag is only valid in conjunction with the fromTemplate flag. When creating a proxy for an existing container, the type created will always be identical to that of the source
            container. The default value for this flag is 'container'.
    """
@overload #Overload for containerProxy in ['create']
def containerProxy(fromTemplate: str = ..., ft: str = ..., type: str = ..., typ: str = ...) -> None:
    """containerProxy is undoable, queryable, and editable.
    
    Creates a new container with the same published interface, dynamic attributes
    and attribute values as the specified container but with fewer container
    members. This proxy container can be used as a reference proxy so that values
    can be set on container attributes without loading in the full container. The
    proxy container will contain one or more locator nodes. The first locator has
    dynamic attributes that serve as stand-ins for the original published
    attributes. The remaining locators serve as stand-ins for any dag nodes that
    have been published as parent or as child and will be placed at the world
    space location of the published parent/child nodes. The expected usage of
    container proxies is to serve as a reference proxy for a referenced container.
    For automated creation, export and setup of the proxy see the
    doExportContainerProxy.mel script which is invoked by the "Export Container
    Proxy" menu item.

    ---
    - Args:
        - fromTemplate (ft): Specifies the name of a template file which will be used to create the new container proxy. Stand-in attributes will be created and published for all the numeric attributes on the proxy.
        - type (typ): Specifies the type of container node to use for the proxy. This flag is only valid in conjunction with the fromTemplate flag. When creating a proxy for an existing container, the type created will always be identical to that of the source
            container. The default value for this flag is 'container'.
    """
