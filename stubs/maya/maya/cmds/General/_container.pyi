"""Stub files for General category in Maya commands, command: container."""

from typing import Any, overload

@overload #Overload for container in ['create']
def container([string...]: [string...], addNode: list[str] = ..., bindAttr: [string, string] = ..., current: bool = ..., force: bool = ..., includeHierarchyAbove: bool = ..., includeHierarchyBelow: bool = ..., includeNetwork: bool = ..., includeNetworkDetails: str = ..., includeShaders: bool = ..., includeShapes: bool = ..., includeTransform: bool = ..., name: str = ..., nodeNamePrefix: bool = ..., preview: bool = ..., publishAsChild: [string, string] = ..., publishAsParent: [string, string] = ..., publishAsRoot: [string, boolean] = ..., publishConnections: bool = ..., publishName: str = ..., type: str = ..., unbindAttr: [string, string] = ...) -> str:
    """container is undoable, queryable, and editable.
    
    This command can be used to create and query container nodes. It is also used
    to perform operations on containers such as:
    
    * add and remove nodes from the container
    * publish attributes from nodes inside the container
    * replace the connections and values from one container onto another one
    * remove a container without removing its member nodes

    ---
    - Args:
        - [string...]: Input item(s).
        - addNode (an): Specifies the list of nodes to add to container.
        - bindAttr (ba): Bind a contained attribute to an unbound published name on the interface of the container; returns a list of bound published names. The first string specifies the node and attribute name to be bound in "node.attr" format. The second string
            specifies the name of the unbound published name. In query mode, returns a string array of the published names and their corresponding attributes. The flag can also be used in query mode in conjunction with the -publishName,
            -publishAsParent, and -publishAsChild flags.
        - current (c): In create mode, specify that the newly created asset should be current. In edit mode, set the selected asset as current. In query, return the current asset.
        - force (f): This flag can be used in conjunction with -addNode and -removeNode flags only. If specified with -addNode, nodes will be disconnected from their current containers before they are added to new one. If specified with -removeNode, nodes will
            be removed from all containers, instead of remaining in the parent container if being removed from a nested container.
        - includeHierarchyAbove (iha): Used to specify that the parent hierarchy of the supplied node list should also be included in the container (or deleted from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeHierarchyBelow (ihb): Used to specify that the hierarchy below the supplied node list should also be included in the container (or delete from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeNetwork (inc): Used to specify that the node network connected to supplied node list should also be included in the container. Network traversal will stop at default nodes and nodes which are members of other containers.
        - includeNetworkDetails (ind): Used to specify specific parts of the network that should be included. Valid arguments to this flag are: "channels", "sdk", "constraints", "history" and "expressions", "inputs", "outputs". The difference between this flag and the
            includeNetwork flag, is that it will include all connected nodes regardless of their type. Note that dag containers include their children, so they will always include constraint nodes that are parented beneath the selected objects, even
            when constraints are not specified as an input.
        - includeShaders (isd): Used to specify that for any shapes included, their shaders will also be included in the container.
        - includeShapes (ish): Used to specify that for any transforms selected, their direct child shapes will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyBelow is used since the child shapes and all
            other descendents will automatically be included.
        - includeTransform (it): Used to specify that for any shapes selected, their parent transform will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyAbove is used since the parent transform and all of its
            parents will automatically be included.
        - name (n): Sets the name of the newly-created container.
        - nodeNamePrefix (nnp): Specifies that the name of published attributes should be of the form "node_attr". Must be used with the -publishConnections/-pc flag.
        - preview (p): This flag is valid in create mode only. It indicates that you do not want the container to be created, instead you want to preview its contents. When this flag is used, Maya will select the nodes that would be put in the container if you
            did create the container. For example you can see what would go into the container with -includeNetwork, then modify your selection as desired, and do a create container with the selected objects only.
        - publishAsChild (pac): Publish contained node to the interface of the container to indicate it can be a child of external nodes. The second string is the name of the published node. In query mode, returns a string of the published names and the corresponding
            nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsParent (pap): Publish contained node to the interface of the container to indicate it can be a parent to external nodes. The second string is the name of the published node. In query mode, returns a string of array of the published names and the
            corresponding nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsRoot (pro): Publish or unpublish a node as a root. The significance of root transform node is twofold. When container-centric selection is enabled, the root transform will be selected if a container node in the hierarchy below it is selected in the
            main scene view. Also, when exporting a container proxy, any published root transformation attributes such as translate, rotate or scale will be hooked up to attributes on a stand-in node. In query mode, returns the node that has been
            published as root.
        - publishConnections (pc): Publish all connections from nodes inside the container to nodes outside the container.
        - publishName (pn): Publish a name to the interface of the container, and returns the actual name published to the interface.  In query mode, returns the published names for the container. If the -bindAttr flag is specified, returns only the names that are
            bound; if the -unbindAttr flag is specified, returns only the names that are not bound; if the -publishAsParent/-publishAsChild flags are specified, returns only names of published parents/children. if the -publishAttr is specified with an
            attribute argument in the "node.attr" format, returns the published name for that attribute, if any.
        - type (typ): By default, a container node will be created. Alternatively, the type flag can be used to indicate that a different type of container should be created. At the present time, the only other valid type of container node is "dagContainer".
        - unbindAttr (ua): Unbind a published attribute from its published name on the interface of the container, leaving an unbound published name on the interface of the container; returns a list of unbound published names. The first string specifies the node and
            attribute name to be unbound in "node.attr" format, and the second string specifies the name of the bound published name. In query mode, can only be used with the -publishName, -publishAsParent and -publishAsChild flags.
    """
@overload #Overload for container in ['create']
def container([string...]: [string...], an: list[str] = ..., ba: [string, string] = ..., c: bool = ..., f: bool = ..., iha: bool = ..., ihb: bool = ..., inc: bool = ..., ind: str = ..., isd: bool = ..., ish: bool = ..., it: bool = ..., n: str = ..., nnp: bool = ..., p: bool = ..., pac: [string, string] = ..., pap: [string, string] = ..., pro: [string, boolean] = ..., pc: bool = ..., pn: str = ..., typ: str = ..., ua: [string, string] = ...) -> str:
    """container is undoable, queryable, and editable.
    
    This command can be used to create and query container nodes. It is also used
    to perform operations on containers such as:
    
    * add and remove nodes from the container
    * publish attributes from nodes inside the container
    * replace the connections and values from one container onto another one
    * remove a container without removing its member nodes

    ---
    - Args:
        - [string...]: Input item(s).
        - addNode (an): Specifies the list of nodes to add to container.
        - bindAttr (ba): Bind a contained attribute to an unbound published name on the interface of the container; returns a list of bound published names. The first string specifies the node and attribute name to be bound in "node.attr" format. The second string
            specifies the name of the unbound published name. In query mode, returns a string array of the published names and their corresponding attributes. The flag can also be used in query mode in conjunction with the -publishName,
            -publishAsParent, and -publishAsChild flags.
        - current (c): In create mode, specify that the newly created asset should be current. In edit mode, set the selected asset as current. In query, return the current asset.
        - force (f): This flag can be used in conjunction with -addNode and -removeNode flags only. If specified with -addNode, nodes will be disconnected from their current containers before they are added to new one. If specified with -removeNode, nodes will
            be removed from all containers, instead of remaining in the parent container if being removed from a nested container.
        - includeHierarchyAbove (iha): Used to specify that the parent hierarchy of the supplied node list should also be included in the container (or deleted from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeHierarchyBelow (ihb): Used to specify that the hierarchy below the supplied node list should also be included in the container (or delete from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeNetwork (inc): Used to specify that the node network connected to supplied node list should also be included in the container. Network traversal will stop at default nodes and nodes which are members of other containers.
        - includeNetworkDetails (ind): Used to specify specific parts of the network that should be included. Valid arguments to this flag are: "channels", "sdk", "constraints", "history" and "expressions", "inputs", "outputs". The difference between this flag and the
            includeNetwork flag, is that it will include all connected nodes regardless of their type. Note that dag containers include their children, so they will always include constraint nodes that are parented beneath the selected objects, even
            when constraints are not specified as an input.
        - includeShaders (isd): Used to specify that for any shapes included, their shaders will also be included in the container.
        - includeShapes (ish): Used to specify that for any transforms selected, their direct child shapes will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyBelow is used since the child shapes and all
            other descendents will automatically be included.
        - includeTransform (it): Used to specify that for any shapes selected, their parent transform will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyAbove is used since the parent transform and all of its
            parents will automatically be included.
        - name (n): Sets the name of the newly-created container.
        - nodeNamePrefix (nnp): Specifies that the name of published attributes should be of the form "node_attr". Must be used with the -publishConnections/-pc flag.
        - preview (p): This flag is valid in create mode only. It indicates that you do not want the container to be created, instead you want to preview its contents. When this flag is used, Maya will select the nodes that would be put in the container if you
            did create the container. For example you can see what would go into the container with -includeNetwork, then modify your selection as desired, and do a create container with the selected objects only.
        - publishAsChild (pac): Publish contained node to the interface of the container to indicate it can be a child of external nodes. The second string is the name of the published node. In query mode, returns a string of the published names and the corresponding
            nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsParent (pap): Publish contained node to the interface of the container to indicate it can be a parent to external nodes. The second string is the name of the published node. In query mode, returns a string of array of the published names and the
            corresponding nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsRoot (pro): Publish or unpublish a node as a root. The significance of root transform node is twofold. When container-centric selection is enabled, the root transform will be selected if a container node in the hierarchy below it is selected in the
            main scene view. Also, when exporting a container proxy, any published root transformation attributes such as translate, rotate or scale will be hooked up to attributes on a stand-in node. In query mode, returns the node that has been
            published as root.
        - publishConnections (pc): Publish all connections from nodes inside the container to nodes outside the container.
        - publishName (pn): Publish a name to the interface of the container, and returns the actual name published to the interface.  In query mode, returns the published names for the container. If the -bindAttr flag is specified, returns only the names that are
            bound; if the -unbindAttr flag is specified, returns only the names that are not bound; if the -publishAsParent/-publishAsChild flags are specified, returns only names of published parents/children. if the -publishAttr is specified with an
            attribute argument in the "node.attr" format, returns the published name for that attribute, if any.
        - type (typ): By default, a container node will be created. Alternatively, the type flag can be used to indicate that a different type of container should be created. At the present time, the only other valid type of container node is "dagContainer".
        - unbindAttr (ua): Unbind a published attribute from its published name on the interface of the container, leaving an unbound published name on the interface of the container; returns a list of unbound published names. The first string specifies the node and
            attribute name to be unbound in "node.attr" format, and the second string specifies the name of the bound published name. In query mode, can only be used with the -publishName, -publishAsParent and -publishAsChild flags.
    """
@overload #Overload for container in ['create']
def container([string...]: [string...], addNode: list[str] = ..., an: list[str] = ..., bindAttr: [string, string] = ..., ba: [string, string] = ..., current: bool = ..., c: bool = ..., force: bool = ..., f: bool = ..., includeHierarchyAbove: bool = ..., iha: bool = ..., includeHierarchyBelow: bool = ..., ihb: bool = ..., includeNetwork: bool = ..., inc: bool = ..., includeNetworkDetails: str = ..., ind: str = ..., includeShaders: bool = ..., isd: bool = ..., includeShapes: bool = ..., ish: bool = ..., includeTransform: bool = ..., it: bool = ..., name: str = ..., n: str = ..., nodeNamePrefix: bool = ..., nnp: bool = ..., preview: bool = ..., p: bool = ..., publishAsChild: [string, string] = ..., pac: [string, string] = ..., publishAsParent: [string, string] = ..., pap: [string, string] = ..., publishAsRoot: [string, boolean] = ..., pro: [string, boolean] = ..., publishConnections: bool = ..., pc: bool = ..., publishName: str = ..., pn: str = ..., type: str = ..., typ: str = ..., unbindAttr: [string, string] = ..., ua: [string, string] = ...) -> str:
    """container is undoable, queryable, and editable.
    
    This command can be used to create and query container nodes. It is also used
    to perform operations on containers such as:
    
    * add and remove nodes from the container
    * publish attributes from nodes inside the container
    * replace the connections and values from one container onto another one
    * remove a container without removing its member nodes

    ---
    - Args:
        - [string...]: Input item(s).
        - addNode (an): Specifies the list of nodes to add to container.
        - bindAttr (ba): Bind a contained attribute to an unbound published name on the interface of the container; returns a list of bound published names. The first string specifies the node and attribute name to be bound in "node.attr" format. The second string
            specifies the name of the unbound published name. In query mode, returns a string array of the published names and their corresponding attributes. The flag can also be used in query mode in conjunction with the -publishName,
            -publishAsParent, and -publishAsChild flags.
        - current (c): In create mode, specify that the newly created asset should be current. In edit mode, set the selected asset as current. In query, return the current asset.
        - force (f): This flag can be used in conjunction with -addNode and -removeNode flags only. If specified with -addNode, nodes will be disconnected from their current containers before they are added to new one. If specified with -removeNode, nodes will
            be removed from all containers, instead of remaining in the parent container if being removed from a nested container.
        - includeHierarchyAbove (iha): Used to specify that the parent hierarchy of the supplied node list should also be included in the container (or deleted from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeHierarchyBelow (ihb): Used to specify that the hierarchy below the supplied node list should also be included in the container (or delete from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeNetwork (inc): Used to specify that the node network connected to supplied node list should also be included in the container. Network traversal will stop at default nodes and nodes which are members of other containers.
        - includeNetworkDetails (ind): Used to specify specific parts of the network that should be included. Valid arguments to this flag are: "channels", "sdk", "constraints", "history" and "expressions", "inputs", "outputs". The difference between this flag and the
            includeNetwork flag, is that it will include all connected nodes regardless of their type. Note that dag containers include their children, so they will always include constraint nodes that are parented beneath the selected objects, even
            when constraints are not specified as an input.
        - includeShaders (isd): Used to specify that for any shapes included, their shaders will also be included in the container.
        - includeShapes (ish): Used to specify that for any transforms selected, their direct child shapes will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyBelow is used since the child shapes and all
            other descendents will automatically be included.
        - includeTransform (it): Used to specify that for any shapes selected, their parent transform will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyAbove is used since the parent transform and all of its
            parents will automatically be included.
        - name (n): Sets the name of the newly-created container.
        - nodeNamePrefix (nnp): Specifies that the name of published attributes should be of the form "node_attr". Must be used with the -publishConnections/-pc flag.
        - preview (p): This flag is valid in create mode only. It indicates that you do not want the container to be created, instead you want to preview its contents. When this flag is used, Maya will select the nodes that would be put in the container if you
            did create the container. For example you can see what would go into the container with -includeNetwork, then modify your selection as desired, and do a create container with the selected objects only.
        - publishAsChild (pac): Publish contained node to the interface of the container to indicate it can be a child of external nodes. The second string is the name of the published node. In query mode, returns a string of the published names and the corresponding
            nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsParent (pap): Publish contained node to the interface of the container to indicate it can be a parent to external nodes. The second string is the name of the published node. In query mode, returns a string of array of the published names and the
            corresponding nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsRoot (pro): Publish or unpublish a node as a root. The significance of root transform node is twofold. When container-centric selection is enabled, the root transform will be selected if a container node in the hierarchy below it is selected in the
            main scene view. Also, when exporting a container proxy, any published root transformation attributes such as translate, rotate or scale will be hooked up to attributes on a stand-in node. In query mode, returns the node that has been
            published as root.
        - publishConnections (pc): Publish all connections from nodes inside the container to nodes outside the container.
        - publishName (pn): Publish a name to the interface of the container, and returns the actual name published to the interface.  In query mode, returns the published names for the container. If the -bindAttr flag is specified, returns only the names that are
            bound; if the -unbindAttr flag is specified, returns only the names that are not bound; if the -publishAsParent/-publishAsChild flags are specified, returns only names of published parents/children. if the -publishAttr is specified with an
            attribute argument in the "node.attr" format, returns the published name for that attribute, if any.
        - type (typ): By default, a container node will be created. Alternatively, the type flag can be used to indicate that a different type of container should be created. At the present time, the only other valid type of container node is "dagContainer".
        - unbindAttr (ua): Unbind a published attribute from its published name on the interface of the container, leaving an unbound published name on the interface of the container; returns a list of unbound published names. The first string specifies the node and
            attribute name to be unbound in "node.attr" format, and the second string specifies the name of the bound published name. In query mode, can only be used with the -publishName, -publishAsParent and -publishAsChild flags.
    """
@overload #Overload for container in ['query']
def container([string...]: [string...], addNode: list[str] = ..., asset: list[str] = ..., assetMember: str = ..., bindAttr: [string, string] = ..., connectionList: bool = ..., current: bool = ..., fileName: list[str] = ..., findContainer: list[str] = ..., force: bool = ..., includeHierarchyAbove: bool = ..., includeHierarchyBelow: bool = ..., includeNetwork: bool = ..., includeNetworkDetails: str = ..., includeShaders: bool = ..., includeShapes: bool = ..., includeTransform: bool = ..., isContainer: bool = ..., nodeList: bool = ..., nodeNamePrefix: bool = ..., parentContainer: bool = ..., publishAsChild: [string, string] = ..., publishAsParent: [string, string] = ..., publishAsRoot: [string, boolean] = ..., publishAttr: str = ..., publishConnections: bool = ..., publishName: str = ..., type: str = ..., unbindAttr: [string, string] = ..., unsortedOrder: bool = ..., query: bool = ...) -> str:
    """container is undoable, queryable, and editable.
    
    This command can be used to create and query container nodes. It is also used
    to perform operations on containers such as:
    
    * add and remove nodes from the container
    * publish attributes from nodes inside the container
    * replace the connections and values from one container onto another one
    * remove a container without removing its member nodes

    ---
    - Args:
        - [string...]: Input item(s).
        - addNode (an): Specifies the list of nodes to add to container.
        - asset (a): When queried, if all the nodes in nodeList belong to the same container, returns container's name. Otherwise returns empty string. This flag is functionally equivalent to the findContainer flag.
        - assetMember (am): Can be used during query in conjunction with the bindAttr flag to query for the only published attributes related to the specified node within the container.In query mode, this flag needs a value.
        - bindAttr (ba): Bind a contained attribute to an unbound published name on the interface of the container; returns a list of bound published names. The first string specifies the node and attribute name to be bound in "node.attr" format. The second string
            specifies the name of the unbound published name. In query mode, returns a string array of the published names and their corresponding attributes. The flag can also be used in query mode in conjunction with the -publishName,
            -publishAsParent, and -publishAsChild flags.
        - connectionList (cl): Returns a list of the exterior connections to the container node.
        - current (c): In create mode, specify that the newly created asset should be current. In edit mode, set the selected asset as current. In query, return the current asset.
        - fileName (fn): Used to query for the assets associated with a given file name.In query mode, this flag needs a value.
        - findContainer (fc): When queried, if all the nodes in nodeList belong to the same container, returns container's name. Otherwise returns empty string.In query mode, this flag needs a value.
        - force (f): This flag can be used in conjunction with -addNode and -removeNode flags only. If specified with -addNode, nodes will be disconnected from their current containers before they are added to new one. If specified with -removeNode, nodes will
            be removed from all containers, instead of remaining in the parent container if being removed from a nested container.
        - includeHierarchyAbove (iha): Used to specify that the parent hierarchy of the supplied node list should also be included in the container (or deleted from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeHierarchyBelow (ihb): Used to specify that the hierarchy below the supplied node list should also be included in the container (or delete from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeNetwork (inc): Used to specify that the node network connected to supplied node list should also be included in the container. Network traversal will stop at default nodes and nodes which are members of other containers.
        - includeNetworkDetails (ind): Used to specify specific parts of the network that should be included. Valid arguments to this flag are: "channels", "sdk", "constraints", "history" and "expressions", "inputs", "outputs". The difference between this flag and the
            includeNetwork flag, is that it will include all connected nodes regardless of their type. Note that dag containers include their children, so they will always include constraint nodes that are parented beneath the selected objects, even
            when constraints are not specified as an input.
        - includeShaders (isd): Used to specify that for any shapes included, their shaders will also be included in the container.
        - includeShapes (ish): Used to specify that for any transforms selected, their direct child shapes will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyBelow is used since the child shapes and all
            other descendents will automatically be included.
        - includeTransform (it): Used to specify that for any shapes selected, their parent transform will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyAbove is used since the parent transform and all of its
            parents will automatically be included.
        - isContainer (isc): Return true if the selected or specified node is a container node. If multiple containers are queried, only the state of the first will be returned.
        - nodeList (nl): When queried, returns a list of nodes in container. The list will be sorted in the order they were added to the container. This will also display any reordering done with the reorderContainer command.
        - nodeNamePrefix (nnp): Specifies that the name of published attributes should be of the form "node_attr". Must be used with the -publishConnections/-pc flag.
        - parentContainer (par): Flag to query the parent container of a specified container.
        - publishAsChild (pac): Publish contained node to the interface of the container to indicate it can be a child of external nodes. The second string is the name of the published node. In query mode, returns a string of the published names and the corresponding
            nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsParent (pap): Publish contained node to the interface of the container to indicate it can be a parent to external nodes. The second string is the name of the published node. In query mode, returns a string of array of the published names and the
            corresponding nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsRoot (pro): Publish or unpublish a node as a root. The significance of root transform node is twofold. When container-centric selection is enabled, the root transform will be selected if a container node in the hierarchy below it is selected in the
            main scene view. Also, when exporting a container proxy, any published root transformation attributes such as translate, rotate or scale will be hooked up to attributes on a stand-in node. In query mode, returns the node that has been
            published as root.
        - publishAttr (pa): In query mode, can only be used with the -publishName(-pn) flag, and takes an attribute as an argument; returns the published name of the attribute, if any.In query mode, this flag needs a value.
        - publishConnections (pc): Publish all connections from nodes inside the container to nodes outside the container.
        - publishName (pn): Publish a name to the interface of the container, and returns the actual name published to the interface.  In query mode, returns the published names for the container. If the -bindAttr flag is specified, returns only the names that are
            bound; if the -unbindAttr flag is specified, returns only the names that are not bound; if the -publishAsParent/-publishAsChild flags are specified, returns only names of published parents/children. if the -publishAttr is specified with an
            attribute argument in the "node.attr" format, returns the published name for that attribute, if any.
        - type (typ): By default, a container node will be created. Alternatively, the type flag can be used to indicate that a different type of container should be created. At the present time, the only other valid type of container node is "dagContainer".
        - unbindAttr (ua): Unbind a published attribute from its published name on the interface of the container, leaving an unbound published name on the interface of the container; returns a list of unbound published names. The first string specifies the node and
            attribute name to be unbound in "node.attr" format, and the second string specifies the name of the bound published name. In query mode, can only be used with the -publishName, -publishAsParent and -publishAsChild flags.
        - unsortedOrder (uso): This flag has no effect on the operation of the container command (OBSOLETE).
        - query (q): Query mode flag
    """
@overload #Overload for container in ['query']
def container([string...]: [string...], an: list[str] = ..., a: list[str] = ..., am: str = ..., ba: [string, string] = ..., cl: bool = ..., c: bool = ..., fn: list[str] = ..., fc: list[str] = ..., f: bool = ..., iha: bool = ..., ihb: bool = ..., inc: bool = ..., ind: str = ..., isd: bool = ..., ish: bool = ..., it: bool = ..., isc: bool = ..., nl: bool = ..., nnp: bool = ..., par: bool = ..., pac: [string, string] = ..., pap: [string, string] = ..., pro: [string, boolean] = ..., pa: str = ..., pc: bool = ..., pn: str = ..., typ: str = ..., ua: [string, string] = ..., uso: bool = ..., q: bool = ...) -> str:
    """container is undoable, queryable, and editable.
    
    This command can be used to create and query container nodes. It is also used
    to perform operations on containers such as:
    
    * add and remove nodes from the container
    * publish attributes from nodes inside the container
    * replace the connections and values from one container onto another one
    * remove a container without removing its member nodes

    ---
    - Args:
        - [string...]: Input item(s).
        - addNode (an): Specifies the list of nodes to add to container.
        - asset (a): When queried, if all the nodes in nodeList belong to the same container, returns container's name. Otherwise returns empty string. This flag is functionally equivalent to the findContainer flag.
        - assetMember (am): Can be used during query in conjunction with the bindAttr flag to query for the only published attributes related to the specified node within the container.In query mode, this flag needs a value.
        - bindAttr (ba): Bind a contained attribute to an unbound published name on the interface of the container; returns a list of bound published names. The first string specifies the node and attribute name to be bound in "node.attr" format. The second string
            specifies the name of the unbound published name. In query mode, returns a string array of the published names and their corresponding attributes. The flag can also be used in query mode in conjunction with the -publishName,
            -publishAsParent, and -publishAsChild flags.
        - connectionList (cl): Returns a list of the exterior connections to the container node.
        - current (c): In create mode, specify that the newly created asset should be current. In edit mode, set the selected asset as current. In query, return the current asset.
        - fileName (fn): Used to query for the assets associated with a given file name.In query mode, this flag needs a value.
        - findContainer (fc): When queried, if all the nodes in nodeList belong to the same container, returns container's name. Otherwise returns empty string.In query mode, this flag needs a value.
        - force (f): This flag can be used in conjunction with -addNode and -removeNode flags only. If specified with -addNode, nodes will be disconnected from their current containers before they are added to new one. If specified with -removeNode, nodes will
            be removed from all containers, instead of remaining in the parent container if being removed from a nested container.
        - includeHierarchyAbove (iha): Used to specify that the parent hierarchy of the supplied node list should also be included in the container (or deleted from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeHierarchyBelow (ihb): Used to specify that the hierarchy below the supplied node list should also be included in the container (or delete from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeNetwork (inc): Used to specify that the node network connected to supplied node list should also be included in the container. Network traversal will stop at default nodes and nodes which are members of other containers.
        - includeNetworkDetails (ind): Used to specify specific parts of the network that should be included. Valid arguments to this flag are: "channels", "sdk", "constraints", "history" and "expressions", "inputs", "outputs". The difference between this flag and the
            includeNetwork flag, is that it will include all connected nodes regardless of their type. Note that dag containers include their children, so they will always include constraint nodes that are parented beneath the selected objects, even
            when constraints are not specified as an input.
        - includeShaders (isd): Used to specify that for any shapes included, their shaders will also be included in the container.
        - includeShapes (ish): Used to specify that for any transforms selected, their direct child shapes will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyBelow is used since the child shapes and all
            other descendents will automatically be included.
        - includeTransform (it): Used to specify that for any shapes selected, their parent transform will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyAbove is used since the parent transform and all of its
            parents will automatically be included.
        - isContainer (isc): Return true if the selected or specified node is a container node. If multiple containers are queried, only the state of the first will be returned.
        - nodeList (nl): When queried, returns a list of nodes in container. The list will be sorted in the order they were added to the container. This will also display any reordering done with the reorderContainer command.
        - nodeNamePrefix (nnp): Specifies that the name of published attributes should be of the form "node_attr". Must be used with the -publishConnections/-pc flag.
        - parentContainer (par): Flag to query the parent container of a specified container.
        - publishAsChild (pac): Publish contained node to the interface of the container to indicate it can be a child of external nodes. The second string is the name of the published node. In query mode, returns a string of the published names and the corresponding
            nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsParent (pap): Publish contained node to the interface of the container to indicate it can be a parent to external nodes. The second string is the name of the published node. In query mode, returns a string of array of the published names and the
            corresponding nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsRoot (pro): Publish or unpublish a node as a root. The significance of root transform node is twofold. When container-centric selection is enabled, the root transform will be selected if a container node in the hierarchy below it is selected in the
            main scene view. Also, when exporting a container proxy, any published root transformation attributes such as translate, rotate or scale will be hooked up to attributes on a stand-in node. In query mode, returns the node that has been
            published as root.
        - publishAttr (pa): In query mode, can only be used with the -publishName(-pn) flag, and takes an attribute as an argument; returns the published name of the attribute, if any.In query mode, this flag needs a value.
        - publishConnections (pc): Publish all connections from nodes inside the container to nodes outside the container.
        - publishName (pn): Publish a name to the interface of the container, and returns the actual name published to the interface.  In query mode, returns the published names for the container. If the -bindAttr flag is specified, returns only the names that are
            bound; if the -unbindAttr flag is specified, returns only the names that are not bound; if the -publishAsParent/-publishAsChild flags are specified, returns only names of published parents/children. if the -publishAttr is specified with an
            attribute argument in the "node.attr" format, returns the published name for that attribute, if any.
        - type (typ): By default, a container node will be created. Alternatively, the type flag can be used to indicate that a different type of container should be created. At the present time, the only other valid type of container node is "dagContainer".
        - unbindAttr (ua): Unbind a published attribute from its published name on the interface of the container, leaving an unbound published name on the interface of the container; returns a list of unbound published names. The first string specifies the node and
            attribute name to be unbound in "node.attr" format, and the second string specifies the name of the bound published name. In query mode, can only be used with the -publishName, -publishAsParent and -publishAsChild flags.
        - unsortedOrder (uso): This flag has no effect on the operation of the container command (OBSOLETE).
        - query (q): Query mode flag
    """
@overload #Overload for container in ['query']
def container([string...]: [string...], addNode: list[str] = ..., an: list[str] = ..., asset: list[str] = ..., a: list[str] = ..., assetMember: str = ..., am: str = ..., bindAttr: [string, string] = ..., ba: [string, string] = ..., connectionList: bool = ..., cl: bool = ..., current: bool = ..., c: bool = ..., fileName: list[str] = ..., fn: list[str] = ..., findContainer: list[str] = ..., fc: list[str] = ..., force: bool = ..., f: bool = ..., includeHierarchyAbove: bool = ..., iha: bool = ..., includeHierarchyBelow: bool = ..., ihb: bool = ..., includeNetwork: bool = ..., inc: bool = ..., includeNetworkDetails: str = ..., ind: str = ..., includeShaders: bool = ..., isd: bool = ..., includeShapes: bool = ..., ish: bool = ..., includeTransform: bool = ..., it: bool = ..., isContainer: bool = ..., isc: bool = ..., nodeList: bool = ..., nl: bool = ..., nodeNamePrefix: bool = ..., nnp: bool = ..., parentContainer: bool = ..., par: bool = ..., publishAsChild: [string, string] = ..., pac: [string, string] = ..., publishAsParent: [string, string] = ..., pap: [string, string] = ..., publishAsRoot: [string, boolean] = ..., pro: [string, boolean] = ..., publishAttr: str = ..., pa: str = ..., publishConnections: bool = ..., pc: bool = ..., publishName: str = ..., pn: str = ..., type: str = ..., typ: str = ..., unbindAttr: [string, string] = ..., ua: [string, string] = ..., unsortedOrder: bool = ..., uso: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """container is undoable, queryable, and editable.
    
    This command can be used to create and query container nodes. It is also used
    to perform operations on containers such as:
    
    * add and remove nodes from the container
    * publish attributes from nodes inside the container
    * replace the connections and values from one container onto another one
    * remove a container without removing its member nodes

    ---
    - Args:
        - [string...]: Input item(s).
        - addNode (an): Specifies the list of nodes to add to container.
        - asset (a): When queried, if all the nodes in nodeList belong to the same container, returns container's name. Otherwise returns empty string. This flag is functionally equivalent to the findContainer flag.
        - assetMember (am): Can be used during query in conjunction with the bindAttr flag to query for the only published attributes related to the specified node within the container.In query mode, this flag needs a value.
        - bindAttr (ba): Bind a contained attribute to an unbound published name on the interface of the container; returns a list of bound published names. The first string specifies the node and attribute name to be bound in "node.attr" format. The second string
            specifies the name of the unbound published name. In query mode, returns a string array of the published names and their corresponding attributes. The flag can also be used in query mode in conjunction with the -publishName,
            -publishAsParent, and -publishAsChild flags.
        - connectionList (cl): Returns a list of the exterior connections to the container node.
        - current (c): In create mode, specify that the newly created asset should be current. In edit mode, set the selected asset as current. In query, return the current asset.
        - fileName (fn): Used to query for the assets associated with a given file name.In query mode, this flag needs a value.
        - findContainer (fc): When queried, if all the nodes in nodeList belong to the same container, returns container's name. Otherwise returns empty string.In query mode, this flag needs a value.
        - force (f): This flag can be used in conjunction with -addNode and -removeNode flags only. If specified with -addNode, nodes will be disconnected from their current containers before they are added to new one. If specified with -removeNode, nodes will
            be removed from all containers, instead of remaining in the parent container if being removed from a nested container.
        - includeHierarchyAbove (iha): Used to specify that the parent hierarchy of the supplied node list should also be included in the container (or deleted from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeHierarchyBelow (ihb): Used to specify that the hierarchy below the supplied node list should also be included in the container (or delete from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeNetwork (inc): Used to specify that the node network connected to supplied node list should also be included in the container. Network traversal will stop at default nodes and nodes which are members of other containers.
        - includeNetworkDetails (ind): Used to specify specific parts of the network that should be included. Valid arguments to this flag are: "channels", "sdk", "constraints", "history" and "expressions", "inputs", "outputs". The difference between this flag and the
            includeNetwork flag, is that it will include all connected nodes regardless of their type. Note that dag containers include their children, so they will always include constraint nodes that are parented beneath the selected objects, even
            when constraints are not specified as an input.
        - includeShaders (isd): Used to specify that for any shapes included, their shaders will also be included in the container.
        - includeShapes (ish): Used to specify that for any transforms selected, their direct child shapes will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyBelow is used since the child shapes and all
            other descendents will automatically be included.
        - includeTransform (it): Used to specify that for any shapes selected, their parent transform will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyAbove is used since the parent transform and all of its
            parents will automatically be included.
        - isContainer (isc): Return true if the selected or specified node is a container node. If multiple containers are queried, only the state of the first will be returned.
        - nodeList (nl): When queried, returns a list of nodes in container. The list will be sorted in the order they were added to the container. This will also display any reordering done with the reorderContainer command.
        - nodeNamePrefix (nnp): Specifies that the name of published attributes should be of the form "node_attr". Must be used with the -publishConnections/-pc flag.
        - parentContainer (par): Flag to query the parent container of a specified container.
        - publishAsChild (pac): Publish contained node to the interface of the container to indicate it can be a child of external nodes. The second string is the name of the published node. In query mode, returns a string of the published names and the corresponding
            nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsParent (pap): Publish contained node to the interface of the container to indicate it can be a parent to external nodes. The second string is the name of the published node. In query mode, returns a string of array of the published names and the
            corresponding nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsRoot (pro): Publish or unpublish a node as a root. The significance of root transform node is twofold. When container-centric selection is enabled, the root transform will be selected if a container node in the hierarchy below it is selected in the
            main scene view. Also, when exporting a container proxy, any published root transformation attributes such as translate, rotate or scale will be hooked up to attributes on a stand-in node. In query mode, returns the node that has been
            published as root.
        - publishAttr (pa): In query mode, can only be used with the -publishName(-pn) flag, and takes an attribute as an argument; returns the published name of the attribute, if any.In query mode, this flag needs a value.
        - publishConnections (pc): Publish all connections from nodes inside the container to nodes outside the container.
        - publishName (pn): Publish a name to the interface of the container, and returns the actual name published to the interface.  In query mode, returns the published names for the container. If the -bindAttr flag is specified, returns only the names that are
            bound; if the -unbindAttr flag is specified, returns only the names that are not bound; if the -publishAsParent/-publishAsChild flags are specified, returns only names of published parents/children. if the -publishAttr is specified with an
            attribute argument in the "node.attr" format, returns the published name for that attribute, if any.
        - type (typ): By default, a container node will be created. Alternatively, the type flag can be used to indicate that a different type of container should be created. At the present time, the only other valid type of container node is "dagContainer".
        - unbindAttr (ua): Unbind a published attribute from its published name on the interface of the container, leaving an unbound published name on the interface of the container; returns a list of unbound published names. The first string specifies the node and
            attribute name to be unbound in "node.attr" format, and the second string specifies the name of the bound published name. In query mode, can only be used with the -publishName, -publishAsParent and -publishAsChild flags.
        - unsortedOrder (uso): This flag has no effect on the operation of the container command (OBSOLETE).
        - query (q): Query mode flag
    """
@overload #Overload for container in ['edit']
def container([string...]: [string...], addNode: list[str] = ..., bindAttr: [string, string] = ..., current: bool = ..., force: bool = ..., includeHierarchyAbove: bool = ..., includeHierarchyBelow: bool = ..., includeNetwork: bool = ..., includeNetworkDetails: str = ..., includeShaders: bool = ..., includeShapes: bool = ..., includeTransform: bool = ..., nodeNamePrefix: bool = ..., publishAndBind: [string, string] = ..., publishAsChild: [string, string] = ..., publishAsParent: [string, string] = ..., publishAsRoot: [string, boolean] = ..., publishConnections: bool = ..., publishName: str = ..., removeContainer: bool = ..., removeNode: list[str] = ..., type: str = ..., unbindAndUnpublish: str = ..., unbindAttr: [string, string] = ..., unbindChild: str = ..., unbindParent: str = ..., unpublishChild: str = ..., unpublishName: str = ..., unpublishParent: str = ..., edit: bool = ...) -> str:
    """container is undoable, queryable, and editable.
    
    This command can be used to create and query container nodes. It is also used
    to perform operations on containers such as:
    
    * add and remove nodes from the container
    * publish attributes from nodes inside the container
    * replace the connections and values from one container onto another one
    * remove a container without removing its member nodes

    ---
    - Args:
        - [string...]: Input item(s).
        - addNode (an): Specifies the list of nodes to add to container.
        - bindAttr (ba): Bind a contained attribute to an unbound published name on the interface of the container; returns a list of bound published names. The first string specifies the node and attribute name to be bound in "node.attr" format. The second string
            specifies the name of the unbound published name. In query mode, returns a string array of the published names and their corresponding attributes. The flag can also be used in query mode in conjunction with the -publishName,
            -publishAsParent, and -publishAsChild flags.
        - current (c): In create mode, specify that the newly created asset should be current. In edit mode, set the selected asset as current. In query, return the current asset.
        - force (f): This flag can be used in conjunction with -addNode and -removeNode flags only. If specified with -addNode, nodes will be disconnected from their current containers before they are added to new one. If specified with -removeNode, nodes will
            be removed from all containers, instead of remaining in the parent container if being removed from a nested container.
        - includeHierarchyAbove (iha): Used to specify that the parent hierarchy of the supplied node list should also be included in the container (or deleted from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeHierarchyBelow (ihb): Used to specify that the hierarchy below the supplied node list should also be included in the container (or delete from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeNetwork (inc): Used to specify that the node network connected to supplied node list should also be included in the container. Network traversal will stop at default nodes and nodes which are members of other containers.
        - includeNetworkDetails (ind): Used to specify specific parts of the network that should be included. Valid arguments to this flag are: "channels", "sdk", "constraints", "history" and "expressions", "inputs", "outputs". The difference between this flag and the
            includeNetwork flag, is that it will include all connected nodes regardless of their type. Note that dag containers include their children, so they will always include constraint nodes that are parented beneath the selected objects, even
            when constraints are not specified as an input.
        - includeShaders (isd): Used to specify that for any shapes included, their shaders will also be included in the container.
        - includeShapes (ish): Used to specify that for any transforms selected, their direct child shapes will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyBelow is used since the child shapes and all
            other descendents will automatically be included.
        - includeTransform (it): Used to specify that for any shapes selected, their parent transform will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyAbove is used since the parent transform and all of its
            parents will automatically be included.
        - nodeNamePrefix (nnp): Specifies that the name of published attributes should be of the form "node_attr". Must be used with the -publishConnections/-pc flag.
        - publishAndBind (pb): Publish the given name and bind the attribute to the given name. First string specifies the node and attribute name in "node.attr" format. Second string specifies the name it should be published with.
        - publishAsChild (pac): Publish contained node to the interface of the container to indicate it can be a child of external nodes. The second string is the name of the published node. In query mode, returns a string of the published names and the corresponding
            nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsParent (pap): Publish contained node to the interface of the container to indicate it can be a parent to external nodes. The second string is the name of the published node. In query mode, returns a string of array of the published names and the
            corresponding nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsRoot (pro): Publish or unpublish a node as a root. The significance of root transform node is twofold. When container-centric selection is enabled, the root transform will be selected if a container node in the hierarchy below it is selected in the
            main scene view. Also, when exporting a container proxy, any published root transformation attributes such as translate, rotate or scale will be hooked up to attributes on a stand-in node. In query mode, returns the node that has been
            published as root.
        - publishConnections (pc): Publish all connections from nodes inside the container to nodes outside the container.
        - publishName (pn): Publish a name to the interface of the container, and returns the actual name published to the interface.  In query mode, returns the published names for the container. If the -bindAttr flag is specified, returns only the names that are
            bound; if the -unbindAttr flag is specified, returns only the names that are not bound; if the -publishAsParent/-publishAsChild flags are specified, returns only names of published parents/children. if the -publishAttr is specified with an
            attribute argument in the "node.attr" format, returns the published name for that attribute, if any.
        - removeContainer (rc): Disconnects all the nodes from container and deletes container node.
        - removeNode (rn): Specifies the list of nodes to remove from container. If node is a member of a nested container, it will be added to the parent container. To remove from all containers completely, use the -force flag.
        - type (typ): By default, a container node will be created. Alternatively, the type flag can be used to indicate that a different type of container should be created. At the present time, the only other valid type of container node is "dagContainer".
        - unbindAndUnpublish (ubp): Unbind the given attribute (in "node.attr" format) and unpublish its associated name. Unbinding a compound may trigger unbinds of its compound parents/children. So the advantage of using this one flag is that it will automatically unpublish
            the names associated with these automatic unbinds.
        - unbindAttr (ua): Unbind a published attribute from its published name on the interface of the container, leaving an unbound published name on the interface of the container; returns a list of unbound published names. The first string specifies the node and
            attribute name to be unbound in "node.attr" format, and the second string specifies the name of the bound published name. In query mode, can only be used with the -publishName, -publishAsParent and -publishAsChild flags.
        - unbindChild (unc): Unbind the node published as child, but do not remove its published name from the interface of the container.
        - unbindParent (unp): Unbind the node published as parent, but do not remove its published name from the interface of the container.
        - unpublishChild (upc): Unpublish node published as child from the interface of the container
        - unpublishName (un): Unpublish an unbound name from the interface of the container.
        - unpublishParent (upp): Unpublish node published as parent from the interface of the container
        - edit (e): Edit mode flag
    """
@overload #Overload for container in ['edit']
def container([string...]: [string...], an: list[str] = ..., ba: [string, string] = ..., c: bool = ..., f: bool = ..., iha: bool = ..., ihb: bool = ..., inc: bool = ..., ind: str = ..., isd: bool = ..., ish: bool = ..., it: bool = ..., nnp: bool = ..., pb: [string, string] = ..., pac: [string, string] = ..., pap: [string, string] = ..., pro: [string, boolean] = ..., pc: bool = ..., pn: str = ..., rc: bool = ..., rn: list[str] = ..., typ: str = ..., ubp: str = ..., ua: [string, string] = ..., unc: str = ..., unp: str = ..., upc: str = ..., un: str = ..., upp: str = ..., e: bool = ...) -> str:
    """container is undoable, queryable, and editable.
    
    This command can be used to create and query container nodes. It is also used
    to perform operations on containers such as:
    
    * add and remove nodes from the container
    * publish attributes from nodes inside the container
    * replace the connections and values from one container onto another one
    * remove a container without removing its member nodes

    ---
    - Args:
        - [string...]: Input item(s).
        - addNode (an): Specifies the list of nodes to add to container.
        - bindAttr (ba): Bind a contained attribute to an unbound published name on the interface of the container; returns a list of bound published names. The first string specifies the node and attribute name to be bound in "node.attr" format. The second string
            specifies the name of the unbound published name. In query mode, returns a string array of the published names and their corresponding attributes. The flag can also be used in query mode in conjunction with the -publishName,
            -publishAsParent, and -publishAsChild flags.
        - current (c): In create mode, specify that the newly created asset should be current. In edit mode, set the selected asset as current. In query, return the current asset.
        - force (f): This flag can be used in conjunction with -addNode and -removeNode flags only. If specified with -addNode, nodes will be disconnected from their current containers before they are added to new one. If specified with -removeNode, nodes will
            be removed from all containers, instead of remaining in the parent container if being removed from a nested container.
        - includeHierarchyAbove (iha): Used to specify that the parent hierarchy of the supplied node list should also be included in the container (or deleted from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeHierarchyBelow (ihb): Used to specify that the hierarchy below the supplied node list should also be included in the container (or delete from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeNetwork (inc): Used to specify that the node network connected to supplied node list should also be included in the container. Network traversal will stop at default nodes and nodes which are members of other containers.
        - includeNetworkDetails (ind): Used to specify specific parts of the network that should be included. Valid arguments to this flag are: "channels", "sdk", "constraints", "history" and "expressions", "inputs", "outputs". The difference between this flag and the
            includeNetwork flag, is that it will include all connected nodes regardless of their type. Note that dag containers include their children, so they will always include constraint nodes that are parented beneath the selected objects, even
            when constraints are not specified as an input.
        - includeShaders (isd): Used to specify that for any shapes included, their shaders will also be included in the container.
        - includeShapes (ish): Used to specify that for any transforms selected, their direct child shapes will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyBelow is used since the child shapes and all
            other descendents will automatically be included.
        - includeTransform (it): Used to specify that for any shapes selected, their parent transform will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyAbove is used since the parent transform and all of its
            parents will automatically be included.
        - nodeNamePrefix (nnp): Specifies that the name of published attributes should be of the form "node_attr". Must be used with the -publishConnections/-pc flag.
        - publishAndBind (pb): Publish the given name and bind the attribute to the given name. First string specifies the node and attribute name in "node.attr" format. Second string specifies the name it should be published with.
        - publishAsChild (pac): Publish contained node to the interface of the container to indicate it can be a child of external nodes. The second string is the name of the published node. In query mode, returns a string of the published names and the corresponding
            nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsParent (pap): Publish contained node to the interface of the container to indicate it can be a parent to external nodes. The second string is the name of the published node. In query mode, returns a string of array of the published names and the
            corresponding nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsRoot (pro): Publish or unpublish a node as a root. The significance of root transform node is twofold. When container-centric selection is enabled, the root transform will be selected if a container node in the hierarchy below it is selected in the
            main scene view. Also, when exporting a container proxy, any published root transformation attributes such as translate, rotate or scale will be hooked up to attributes on a stand-in node. In query mode, returns the node that has been
            published as root.
        - publishConnections (pc): Publish all connections from nodes inside the container to nodes outside the container.
        - publishName (pn): Publish a name to the interface of the container, and returns the actual name published to the interface.  In query mode, returns the published names for the container. If the -bindAttr flag is specified, returns only the names that are
            bound; if the -unbindAttr flag is specified, returns only the names that are not bound; if the -publishAsParent/-publishAsChild flags are specified, returns only names of published parents/children. if the -publishAttr is specified with an
            attribute argument in the "node.attr" format, returns the published name for that attribute, if any.
        - removeContainer (rc): Disconnects all the nodes from container and deletes container node.
        - removeNode (rn): Specifies the list of nodes to remove from container. If node is a member of a nested container, it will be added to the parent container. To remove from all containers completely, use the -force flag.
        - type (typ): By default, a container node will be created. Alternatively, the type flag can be used to indicate that a different type of container should be created. At the present time, the only other valid type of container node is "dagContainer".
        - unbindAndUnpublish (ubp): Unbind the given attribute (in "node.attr" format) and unpublish its associated name. Unbinding a compound may trigger unbinds of its compound parents/children. So the advantage of using this one flag is that it will automatically unpublish
            the names associated with these automatic unbinds.
        - unbindAttr (ua): Unbind a published attribute from its published name on the interface of the container, leaving an unbound published name on the interface of the container; returns a list of unbound published names. The first string specifies the node and
            attribute name to be unbound in "node.attr" format, and the second string specifies the name of the bound published name. In query mode, can only be used with the -publishName, -publishAsParent and -publishAsChild flags.
        - unbindChild (unc): Unbind the node published as child, but do not remove its published name from the interface of the container.
        - unbindParent (unp): Unbind the node published as parent, but do not remove its published name from the interface of the container.
        - unpublishChild (upc): Unpublish node published as child from the interface of the container
        - unpublishName (un): Unpublish an unbound name from the interface of the container.
        - unpublishParent (upp): Unpublish node published as parent from the interface of the container
        - edit (e): Edit mode flag
    """
@overload #Overload for container in ['edit']
def container([string...]: [string...], addNode: list[str] = ..., an: list[str] = ..., bindAttr: [string, string] = ..., ba: [string, string] = ..., current: bool = ..., c: bool = ..., force: bool = ..., f: bool = ..., includeHierarchyAbove: bool = ..., iha: bool = ..., includeHierarchyBelow: bool = ..., ihb: bool = ..., includeNetwork: bool = ..., inc: bool = ..., includeNetworkDetails: str = ..., ind: str = ..., includeShaders: bool = ..., isd: bool = ..., includeShapes: bool = ..., ish: bool = ..., includeTransform: bool = ..., it: bool = ..., nodeNamePrefix: bool = ..., nnp: bool = ..., publishAndBind: [string, string] = ..., pb: [string, string] = ..., publishAsChild: [string, string] = ..., pac: [string, string] = ..., publishAsParent: [string, string] = ..., pap: [string, string] = ..., publishAsRoot: [string, boolean] = ..., pro: [string, boolean] = ..., publishConnections: bool = ..., pc: bool = ..., publishName: str = ..., pn: str = ..., removeContainer: bool = ..., rc: bool = ..., removeNode: list[str] = ..., rn: list[str] = ..., type: str = ..., typ: str = ..., unbindAndUnpublish: str = ..., ubp: str = ..., unbindAttr: [string, string] = ..., ua: [string, string] = ..., unbindChild: str = ..., unc: str = ..., unbindParent: str = ..., unp: str = ..., unpublishChild: str = ..., upc: str = ..., unpublishName: str = ..., un: str = ..., unpublishParent: str = ..., upp: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """container is undoable, queryable, and editable.
    
    This command can be used to create and query container nodes. It is also used
    to perform operations on containers such as:
    
    * add and remove nodes from the container
    * publish attributes from nodes inside the container
    * replace the connections and values from one container onto another one
    * remove a container without removing its member nodes

    ---
    - Args:
        - [string...]: Input item(s).
        - addNode (an): Specifies the list of nodes to add to container.
        - bindAttr (ba): Bind a contained attribute to an unbound published name on the interface of the container; returns a list of bound published names. The first string specifies the node and attribute name to be bound in "node.attr" format. The second string
            specifies the name of the unbound published name. In query mode, returns a string array of the published names and their corresponding attributes. The flag can also be used in query mode in conjunction with the -publishName,
            -publishAsParent, and -publishAsChild flags.
        - current (c): In create mode, specify that the newly created asset should be current. In edit mode, set the selected asset as current. In query, return the current asset.
        - force (f): This flag can be used in conjunction with -addNode and -removeNode flags only. If specified with -addNode, nodes will be disconnected from their current containers before they are added to new one. If specified with -removeNode, nodes will
            be removed from all containers, instead of remaining in the parent container if being removed from a nested container.
        - includeHierarchyAbove (iha): Used to specify that the parent hierarchy of the supplied node list should also be included in the container (or deleted from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeHierarchyBelow (ihb): Used to specify that the hierarchy below the supplied node list should also be included in the container (or delete from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        - includeNetwork (inc): Used to specify that the node network connected to supplied node list should also be included in the container. Network traversal will stop at default nodes and nodes which are members of other containers.
        - includeNetworkDetails (ind): Used to specify specific parts of the network that should be included. Valid arguments to this flag are: "channels", "sdk", "constraints", "history" and "expressions", "inputs", "outputs". The difference between this flag and the
            includeNetwork flag, is that it will include all connected nodes regardless of their type. Note that dag containers include their children, so they will always include constraint nodes that are parented beneath the selected objects, even
            when constraints are not specified as an input.
        - includeShaders (isd): Used to specify that for any shapes included, their shaders will also be included in the container.
        - includeShapes (ish): Used to specify that for any transforms selected, their direct child shapes will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyBelow is used since the child shapes and all
            other descendents will automatically be included.
        - includeTransform (it): Used to specify that for any shapes selected, their parent transform will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyAbove is used since the parent transform and all of its
            parents will automatically be included.
        - nodeNamePrefix (nnp): Specifies that the name of published attributes should be of the form "node_attr". Must be used with the -publishConnections/-pc flag.
        - publishAndBind (pb): Publish the given name and bind the attribute to the given name. First string specifies the node and attribute name in "node.attr" format. Second string specifies the name it should be published with.
        - publishAsChild (pac): Publish contained node to the interface of the container to indicate it can be a child of external nodes. The second string is the name of the published node. In query mode, returns a string of the published names and the corresponding
            nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsParent (pap): Publish contained node to the interface of the container to indicate it can be a parent to external nodes. The second string is the name of the published node. In query mode, returns a string of array of the published names and the
            corresponding nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        - publishAsRoot (pro): Publish or unpublish a node as a root. The significance of root transform node is twofold. When container-centric selection is enabled, the root transform will be selected if a container node in the hierarchy below it is selected in the
            main scene view. Also, when exporting a container proxy, any published root transformation attributes such as translate, rotate or scale will be hooked up to attributes on a stand-in node. In query mode, returns the node that has been
            published as root.
        - publishConnections (pc): Publish all connections from nodes inside the container to nodes outside the container.
        - publishName (pn): Publish a name to the interface of the container, and returns the actual name published to the interface.  In query mode, returns the published names for the container. If the -bindAttr flag is specified, returns only the names that are
            bound; if the -unbindAttr flag is specified, returns only the names that are not bound; if the -publishAsParent/-publishAsChild flags are specified, returns only names of published parents/children. if the -publishAttr is specified with an
            attribute argument in the "node.attr" format, returns the published name for that attribute, if any.
        - removeContainer (rc): Disconnects all the nodes from container and deletes container node.
        - removeNode (rn): Specifies the list of nodes to remove from container. If node is a member of a nested container, it will be added to the parent container. To remove from all containers completely, use the -force flag.
        - type (typ): By default, a container node will be created. Alternatively, the type flag can be used to indicate that a different type of container should be created. At the present time, the only other valid type of container node is "dagContainer".
        - unbindAndUnpublish (ubp): Unbind the given attribute (in "node.attr" format) and unpublish its associated name. Unbinding a compound may trigger unbinds of its compound parents/children. So the advantage of using this one flag is that it will automatically unpublish
            the names associated with these automatic unbinds.
        - unbindAttr (ua): Unbind a published attribute from its published name on the interface of the container, leaving an unbound published name on the interface of the container; returns a list of unbound published names. The first string specifies the node and
            attribute name to be unbound in "node.attr" format, and the second string specifies the name of the bound published name. In query mode, can only be used with the -publishName, -publishAsParent and -publishAsChild flags.
        - unbindChild (unc): Unbind the node published as child, but do not remove its published name from the interface of the container.
        - unbindParent (unp): Unbind the node published as parent, but do not remove its published name from the interface of the container.
        - unpublishChild (upc): Unpublish node published as child from the interface of the container
        - unpublishName (un): Unpublish an unbound name from the interface of the container.
        - unpublishParent (upp): Unpublish node published as parent from the interface of the container
        - edit (e): Edit mode flag
    """
