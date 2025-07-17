"""Stub files for Contexts category in Maya commands, command: polyMergeEdgeCtx."""

from typing import Any, overload

@overload #Overload for polyMergeEdgeCtx in ['create']
def polyMergeEdgeCtx(caching: bool = ..., constructionHistory: bool = ..., exists: bool = ..., firstEdge: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., mergeMode: int = ..., mergeTexture: bool = ..., name: str = ..., nodeState: int = ..., secondEdge: int = ...) -> str:
    """polyMergeEdgeCtx is undoable, queryable, and editable.
    
    Sews two border edges together.
    The new edge is located either on the first, last, or between both selected
    edges, depending on the mode.
    
    Both edges must belong to the same object, and orientations must match (i.e.
    normals on corresponding faces must point in the same direction).
    Edge flags are mandatory.
    
    Create a new context to merge edges on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        def blockTree(root):
        nodesToBlock = []
        for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
        nodesToBlock += cmds.listConnections(node, source=True, destination=True )
        for node in {source:1 for source in nodesToBlock}.keys():
        cmds.setAttr( '%s.nodeState' % node, 2 )
    ```

    ---
    - Args:
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - constructionHistory (ch): Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed
            directly on the object.Note:If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - firstEdge (fe): First edge to merge. Invalid default value to force the value to be set.Default:-1
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeMode (mm): Merge mode : 0=first, 1=halfway between both edges, 2=second.Default:1
        - mergeTexture (mt): Boolean which is used to decide if uv coordinates should be merged or not - along with the geometry.Default:false
        - name (n): If this is a tool command, name the tool appropriately.
        - nodeState (nds): Maya dependency nodes have 6 possible states. TheNormal (0),HasNoEffect (1), andBlocking (2)states can be used to alter how the graph is evaluated.TheWaiting-Normal (3),Waiting-HasNoEffect (4),Waiting-Blocking (5)are for internal use only.
            They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g.Waiting-Blockingwill reset back
            toBlocking.TheNormalandBlockingcases apply to all nodes, whileHasNoEffectis node specific; many nodes do not support this option. Plug-ins store state in theMPxNode::stateattribute. Anyone can set it or check this attribute.  Additional
            details about each of these 3 states follow.StateDescriptionNormalThe normal node state. This is the default.HasNoEffectTheHasNoEffectoption (a.k.a. pass-through), is used in cases where there is an operation on an input producing an output
            of the same data type. Nearly all deformers support this state, as do a few other nodes. As stated earlier, it is not supported by all nodes.It’s typical to implement support for theHasNoEffectstate in the node’s compute method and to
            perform appropriate operations. Plug-ins can also supportHasNoEffect.The usual implementation of this state is to copy the input directly to the matching output without applying the algorithm in the node. For deformers, applying this state
            leaves the input geometry undeformed on the output.BlockingThis is implemented in the depend node base class and applies to all nodes.Blockingis applied during the evaluation phase to connections. An evaluation request to a blocked
            connection will return as failures, causing the destination plug to retain its current value. Dirty propagation is indirectly affected by this state since blocked connections are never cleaned.When a node is set toBlockingthe behavior is
            supposed to be the same as if all outgoing connections were broken. As long as nobody requests evaluation of the blocked node directly it won’t evaluate after that. Note that a blocked node will still respond togetAttrrequests but
            agetAttron a downstream node will not reevaluate the blocked node.Setting the root transform of a hierarchy toBlockingwon’t automatically influence child transforms in the hierarchy. To do this, you’d need to explicitly set all child nodes
            to theBlockingstate.For example, to set all child transforms toBlocking, you could use the following script.import maya.cmds as cmds def blockTree(root): nodesToBlock = [] for node in {child:1 for child in cmds.listRelatives( root,
            path=True, allDescendents=True )}.keys(): nodesToBlock += cmds.listConnections(node, source=True, destination=True ) for node in {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' % node, 2 )Applying this script
            would continue to draw objects but things would not be animated.Default:kdnNormal
        - secondEdge (se): Second edge to merge. Invalid default value to force the value to be set.Default:-1
    """
@overload #Overload for polyMergeEdgeCtx in ['create']
def polyMergeEdgeCtx(cch: bool = ..., ch: bool = ..., ex: bool = ..., fe: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., mm: int = ..., mt: bool = ..., n: str = ..., nds: int = ..., se: int = ...) -> str:
    """polyMergeEdgeCtx is undoable, queryable, and editable.
    
    Sews two border edges together.
    The new edge is located either on the first, last, or between both selected
    edges, depending on the mode.
    
    Both edges must belong to the same object, and orientations must match (i.e.
    normals on corresponding faces must point in the same direction).
    Edge flags are mandatory.
    
    Create a new context to merge edges on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        def blockTree(root):
        nodesToBlock = []
        for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
        nodesToBlock += cmds.listConnections(node, source=True, destination=True )
        for node in {source:1 for source in nodesToBlock}.keys():
        cmds.setAttr( '%s.nodeState' % node, 2 )
    ```

    ---
    - Args:
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - constructionHistory (ch): Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed
            directly on the object.Note:If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - firstEdge (fe): First edge to merge. Invalid default value to force the value to be set.Default:-1
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeMode (mm): Merge mode : 0=first, 1=halfway between both edges, 2=second.Default:1
        - mergeTexture (mt): Boolean which is used to decide if uv coordinates should be merged or not - along with the geometry.Default:false
        - name (n): If this is a tool command, name the tool appropriately.
        - nodeState (nds): Maya dependency nodes have 6 possible states. TheNormal (0),HasNoEffect (1), andBlocking (2)states can be used to alter how the graph is evaluated.TheWaiting-Normal (3),Waiting-HasNoEffect (4),Waiting-Blocking (5)are for internal use only.
            They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g.Waiting-Blockingwill reset back
            toBlocking.TheNormalandBlockingcases apply to all nodes, whileHasNoEffectis node specific; many nodes do not support this option. Plug-ins store state in theMPxNode::stateattribute. Anyone can set it or check this attribute.  Additional
            details about each of these 3 states follow.StateDescriptionNormalThe normal node state. This is the default.HasNoEffectTheHasNoEffectoption (a.k.a. pass-through), is used in cases where there is an operation on an input producing an output
            of the same data type. Nearly all deformers support this state, as do a few other nodes. As stated earlier, it is not supported by all nodes.It’s typical to implement support for theHasNoEffectstate in the node’s compute method and to
            perform appropriate operations. Plug-ins can also supportHasNoEffect.The usual implementation of this state is to copy the input directly to the matching output without applying the algorithm in the node. For deformers, applying this state
            leaves the input geometry undeformed on the output.BlockingThis is implemented in the depend node base class and applies to all nodes.Blockingis applied during the evaluation phase to connections. An evaluation request to a blocked
            connection will return as failures, causing the destination plug to retain its current value. Dirty propagation is indirectly affected by this state since blocked connections are never cleaned.When a node is set toBlockingthe behavior is
            supposed to be the same as if all outgoing connections were broken. As long as nobody requests evaluation of the blocked node directly it won’t evaluate after that. Note that a blocked node will still respond togetAttrrequests but
            agetAttron a downstream node will not reevaluate the blocked node.Setting the root transform of a hierarchy toBlockingwon’t automatically influence child transforms in the hierarchy. To do this, you’d need to explicitly set all child nodes
            to theBlockingstate.For example, to set all child transforms toBlocking, you could use the following script.import maya.cmds as cmds def blockTree(root): nodesToBlock = [] for node in {child:1 for child in cmds.listRelatives( root,
            path=True, allDescendents=True )}.keys(): nodesToBlock += cmds.listConnections(node, source=True, destination=True ) for node in {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' % node, 2 )Applying this script
            would continue to draw objects but things would not be animated.Default:kdnNormal
        - secondEdge (se): Second edge to merge. Invalid default value to force the value to be set.Default:-1
    """
@overload #Overload for polyMergeEdgeCtx in ['create']
def polyMergeEdgeCtx(caching: bool = ..., cch: bool = ..., constructionHistory: bool = ..., ch: bool = ..., exists: bool = ..., ex: bool = ..., firstEdge: int = ..., fe: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., mergeMode: int = ..., mm: int = ..., mergeTexture: bool = ..., mt: bool = ..., name: str = ..., n: str = ..., nodeState: int = ..., nds: int = ..., secondEdge: int = ..., se: int = ...) -> str:
    """polyMergeEdgeCtx is undoable, queryable, and editable.
    
    Sews two border edges together.
    The new edge is located either on the first, last, or between both selected
    edges, depending on the mode.
    
    Both edges must belong to the same object, and orientations must match (i.e.
    normals on corresponding faces must point in the same direction).
    Edge flags are mandatory.
    
    Create a new context to merge edges on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        def blockTree(root):
        nodesToBlock = []
        for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
        nodesToBlock += cmds.listConnections(node, source=True, destination=True )
        for node in {source:1 for source in nodesToBlock}.keys():
        cmds.setAttr( '%s.nodeState' % node, 2 )
    ```

    ---
    - Args:
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - constructionHistory (ch): Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed
            directly on the object.Note:If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - firstEdge (fe): First edge to merge. Invalid default value to force the value to be set.Default:-1
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeMode (mm): Merge mode : 0=first, 1=halfway between both edges, 2=second.Default:1
        - mergeTexture (mt): Boolean which is used to decide if uv coordinates should be merged or not - along with the geometry.Default:false
        - name (n): If this is a tool command, name the tool appropriately.
        - nodeState (nds): Maya dependency nodes have 6 possible states. TheNormal (0),HasNoEffect (1), andBlocking (2)states can be used to alter how the graph is evaluated.TheWaiting-Normal (3),Waiting-HasNoEffect (4),Waiting-Blocking (5)are for internal use only.
            They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g.Waiting-Blockingwill reset back
            toBlocking.TheNormalandBlockingcases apply to all nodes, whileHasNoEffectis node specific; many nodes do not support this option. Plug-ins store state in theMPxNode::stateattribute. Anyone can set it or check this attribute.  Additional
            details about each of these 3 states follow.StateDescriptionNormalThe normal node state. This is the default.HasNoEffectTheHasNoEffectoption (a.k.a. pass-through), is used in cases where there is an operation on an input producing an output
            of the same data type. Nearly all deformers support this state, as do a few other nodes. As stated earlier, it is not supported by all nodes.It’s typical to implement support for theHasNoEffectstate in the node’s compute method and to
            perform appropriate operations. Plug-ins can also supportHasNoEffect.The usual implementation of this state is to copy the input directly to the matching output without applying the algorithm in the node. For deformers, applying this state
            leaves the input geometry undeformed on the output.BlockingThis is implemented in the depend node base class and applies to all nodes.Blockingis applied during the evaluation phase to connections. An evaluation request to a blocked
            connection will return as failures, causing the destination plug to retain its current value. Dirty propagation is indirectly affected by this state since blocked connections are never cleaned.When a node is set toBlockingthe behavior is
            supposed to be the same as if all outgoing connections were broken. As long as nobody requests evaluation of the blocked node directly it won’t evaluate after that. Note that a blocked node will still respond togetAttrrequests but
            agetAttron a downstream node will not reevaluate the blocked node.Setting the root transform of a hierarchy toBlockingwon’t automatically influence child transforms in the hierarchy. To do this, you’d need to explicitly set all child nodes
            to theBlockingstate.For example, to set all child transforms toBlocking, you could use the following script.import maya.cmds as cmds def blockTree(root): nodesToBlock = [] for node in {child:1 for child in cmds.listRelatives( root,
            path=True, allDescendents=True )}.keys(): nodesToBlock += cmds.listConnections(node, source=True, destination=True ) for node in {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' % node, 2 )Applying this script
            would continue to draw objects but things would not be animated.Default:kdnNormal
        - secondEdge (se): Second edge to merge. Invalid default value to force the value to be set.Default:-1
    """
@overload #Overload for polyMergeEdgeCtx in ['query']
def polyMergeEdgeCtx(activeNodes: bool = ..., caching: bool = ..., constructionHistory: bool = ..., firstEdge: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., mergeMode: int = ..., mergeTexture: bool = ..., nodeState: int = ..., secondEdge: int = ..., toolNode: bool = ..., query: bool = ...) -> str:
    """polyMergeEdgeCtx is undoable, queryable, and editable.
    
    Sews two border edges together.
    The new edge is located either on the first, last, or between both selected
    edges, depending on the mode.
    
    Both edges must belong to the same object, and orientations must match (i.e.
    normals on corresponding faces must point in the same direction).
    Edge flags are mandatory.
    
    Create a new context to merge edges on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        def blockTree(root):
        nodesToBlock = []
        for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
        nodesToBlock += cmds.listConnections(node, source=True, destination=True )
        for node in {source:1 for source in nodesToBlock}.keys():
        cmds.setAttr( '%s.nodeState' % node, 2 )
    ```

    ---
    - Args:
        - activeNodes (anq): Return the active nodes in the tool
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - constructionHistory (ch): Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed
            directly on the object.Note:If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        - firstEdge (fe): First edge to merge. Invalid default value to force the value to be set.Default:-1
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeMode (mm): Merge mode : 0=first, 1=halfway between both edges, 2=second.Default:1
        - mergeTexture (mt): Boolean which is used to decide if uv coordinates should be merged or not - along with the geometry.Default:false
        - nodeState (nds): Maya dependency nodes have 6 possible states. TheNormal (0),HasNoEffect (1), andBlocking (2)states can be used to alter how the graph is evaluated.TheWaiting-Normal (3),Waiting-HasNoEffect (4),Waiting-Blocking (5)are for internal use only.
            They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g.Waiting-Blockingwill reset back
            toBlocking.TheNormalandBlockingcases apply to all nodes, whileHasNoEffectis node specific; many nodes do not support this option. Plug-ins store state in theMPxNode::stateattribute. Anyone can set it or check this attribute.  Additional
            details about each of these 3 states follow.StateDescriptionNormalThe normal node state. This is the default.HasNoEffectTheHasNoEffectoption (a.k.a. pass-through), is used in cases where there is an operation on an input producing an output
            of the same data type. Nearly all deformers support this state, as do a few other nodes. As stated earlier, it is not supported by all nodes.It’s typical to implement support for theHasNoEffectstate in the node’s compute method and to
            perform appropriate operations. Plug-ins can also supportHasNoEffect.The usual implementation of this state is to copy the input directly to the matching output without applying the algorithm in the node. For deformers, applying this state
            leaves the input geometry undeformed on the output.BlockingThis is implemented in the depend node base class and applies to all nodes.Blockingis applied during the evaluation phase to connections. An evaluation request to a blocked
            connection will return as failures, causing the destination plug to retain its current value. Dirty propagation is indirectly affected by this state since blocked connections are never cleaned.When a node is set toBlockingthe behavior is
            supposed to be the same as if all outgoing connections were broken. As long as nobody requests evaluation of the blocked node directly it won’t evaluate after that. Note that a blocked node will still respond togetAttrrequests but
            agetAttron a downstream node will not reevaluate the blocked node.Setting the root transform of a hierarchy toBlockingwon’t automatically influence child transforms in the hierarchy. To do this, you’d need to explicitly set all child nodes
            to theBlockingstate.For example, to set all child transforms toBlocking, you could use the following script.import maya.cmds as cmds def blockTree(root): nodesToBlock = [] for node in {child:1 for child in cmds.listRelatives( root,
            path=True, allDescendents=True )}.keys(): nodesToBlock += cmds.listConnections(node, source=True, destination=True ) for node in {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' % node, 2 )Applying this script
            would continue to draw objects but things would not be animated.Default:kdnNormal
        - secondEdge (se): Second edge to merge. Invalid default value to force the value to be set.Default:-1
        - toolNode (tnq): Return the node used for tool defaults
        - query (q): Query mode flag
    """
@overload #Overload for polyMergeEdgeCtx in ['query']
def polyMergeEdgeCtx(anq: bool = ..., cch: bool = ..., ch: bool = ..., fe: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., mm: int = ..., mt: bool = ..., nds: int = ..., se: int = ..., tnq: bool = ..., q: bool = ...) -> str:
    """polyMergeEdgeCtx is undoable, queryable, and editable.
    
    Sews two border edges together.
    The new edge is located either on the first, last, or between both selected
    edges, depending on the mode.
    
    Both edges must belong to the same object, and orientations must match (i.e.
    normals on corresponding faces must point in the same direction).
    Edge flags are mandatory.
    
    Create a new context to merge edges on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        def blockTree(root):
        nodesToBlock = []
        for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
        nodesToBlock += cmds.listConnections(node, source=True, destination=True )
        for node in {source:1 for source in nodesToBlock}.keys():
        cmds.setAttr( '%s.nodeState' % node, 2 )
    ```

    ---
    - Args:
        - activeNodes (anq): Return the active nodes in the tool
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - constructionHistory (ch): Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed
            directly on the object.Note:If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        - firstEdge (fe): First edge to merge. Invalid default value to force the value to be set.Default:-1
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeMode (mm): Merge mode : 0=first, 1=halfway between both edges, 2=second.Default:1
        - mergeTexture (mt): Boolean which is used to decide if uv coordinates should be merged or not - along with the geometry.Default:false
        - nodeState (nds): Maya dependency nodes have 6 possible states. TheNormal (0),HasNoEffect (1), andBlocking (2)states can be used to alter how the graph is evaluated.TheWaiting-Normal (3),Waiting-HasNoEffect (4),Waiting-Blocking (5)are for internal use only.
            They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g.Waiting-Blockingwill reset back
            toBlocking.TheNormalandBlockingcases apply to all nodes, whileHasNoEffectis node specific; many nodes do not support this option. Plug-ins store state in theMPxNode::stateattribute. Anyone can set it or check this attribute.  Additional
            details about each of these 3 states follow.StateDescriptionNormalThe normal node state. This is the default.HasNoEffectTheHasNoEffectoption (a.k.a. pass-through), is used in cases where there is an operation on an input producing an output
            of the same data type. Nearly all deformers support this state, as do a few other nodes. As stated earlier, it is not supported by all nodes.It’s typical to implement support for theHasNoEffectstate in the node’s compute method and to
            perform appropriate operations. Plug-ins can also supportHasNoEffect.The usual implementation of this state is to copy the input directly to the matching output without applying the algorithm in the node. For deformers, applying this state
            leaves the input geometry undeformed on the output.BlockingThis is implemented in the depend node base class and applies to all nodes.Blockingis applied during the evaluation phase to connections. An evaluation request to a blocked
            connection will return as failures, causing the destination plug to retain its current value. Dirty propagation is indirectly affected by this state since blocked connections are never cleaned.When a node is set toBlockingthe behavior is
            supposed to be the same as if all outgoing connections were broken. As long as nobody requests evaluation of the blocked node directly it won’t evaluate after that. Note that a blocked node will still respond togetAttrrequests but
            agetAttron a downstream node will not reevaluate the blocked node.Setting the root transform of a hierarchy toBlockingwon’t automatically influence child transforms in the hierarchy. To do this, you’d need to explicitly set all child nodes
            to theBlockingstate.For example, to set all child transforms toBlocking, you could use the following script.import maya.cmds as cmds def blockTree(root): nodesToBlock = [] for node in {child:1 for child in cmds.listRelatives( root,
            path=True, allDescendents=True )}.keys(): nodesToBlock += cmds.listConnections(node, source=True, destination=True ) for node in {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' % node, 2 )Applying this script
            would continue to draw objects but things would not be animated.Default:kdnNormal
        - secondEdge (se): Second edge to merge. Invalid default value to force the value to be set.Default:-1
        - toolNode (tnq): Return the node used for tool defaults
        - query (q): Query mode flag
    """
@overload #Overload for polyMergeEdgeCtx in ['query']
def polyMergeEdgeCtx(activeNodes: bool = ..., anq: bool = ..., caching: bool = ..., cch: bool = ..., constructionHistory: bool = ..., ch: bool = ..., firstEdge: int = ..., fe: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., mergeMode: int = ..., mm: int = ..., mergeTexture: bool = ..., mt: bool = ..., nodeState: int = ..., nds: int = ..., secondEdge: int = ..., se: int = ..., toolNode: bool = ..., tnq: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """polyMergeEdgeCtx is undoable, queryable, and editable.
    
    Sews two border edges together.
    The new edge is located either on the first, last, or between both selected
    edges, depending on the mode.
    
    Both edges must belong to the same object, and orientations must match (i.e.
    normals on corresponding faces must point in the same direction).
    Edge flags are mandatory.
    
    Create a new context to merge edges on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        def blockTree(root):
        nodesToBlock = []
        for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
        nodesToBlock += cmds.listConnections(node, source=True, destination=True )
        for node in {source:1 for source in nodesToBlock}.keys():
        cmds.setAttr( '%s.nodeState' % node, 2 )
    ```

    ---
    - Args:
        - activeNodes (anq): Return the active nodes in the tool
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - constructionHistory (ch): Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed
            directly on the object.Note:If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        - firstEdge (fe): First edge to merge. Invalid default value to force the value to be set.Default:-1
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeMode (mm): Merge mode : 0=first, 1=halfway between both edges, 2=second.Default:1
        - mergeTexture (mt): Boolean which is used to decide if uv coordinates should be merged or not - along with the geometry.Default:false
        - nodeState (nds): Maya dependency nodes have 6 possible states. TheNormal (0),HasNoEffect (1), andBlocking (2)states can be used to alter how the graph is evaluated.TheWaiting-Normal (3),Waiting-HasNoEffect (4),Waiting-Blocking (5)are for internal use only.
            They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g.Waiting-Blockingwill reset back
            toBlocking.TheNormalandBlockingcases apply to all nodes, whileHasNoEffectis node specific; many nodes do not support this option. Plug-ins store state in theMPxNode::stateattribute. Anyone can set it or check this attribute.  Additional
            details about each of these 3 states follow.StateDescriptionNormalThe normal node state. This is the default.HasNoEffectTheHasNoEffectoption (a.k.a. pass-through), is used in cases where there is an operation on an input producing an output
            of the same data type. Nearly all deformers support this state, as do a few other nodes. As stated earlier, it is not supported by all nodes.It’s typical to implement support for theHasNoEffectstate in the node’s compute method and to
            perform appropriate operations. Plug-ins can also supportHasNoEffect.The usual implementation of this state is to copy the input directly to the matching output without applying the algorithm in the node. For deformers, applying this state
            leaves the input geometry undeformed on the output.BlockingThis is implemented in the depend node base class and applies to all nodes.Blockingis applied during the evaluation phase to connections. An evaluation request to a blocked
            connection will return as failures, causing the destination plug to retain its current value. Dirty propagation is indirectly affected by this state since blocked connections are never cleaned.When a node is set toBlockingthe behavior is
            supposed to be the same as if all outgoing connections were broken. As long as nobody requests evaluation of the blocked node directly it won’t evaluate after that. Note that a blocked node will still respond togetAttrrequests but
            agetAttron a downstream node will not reevaluate the blocked node.Setting the root transform of a hierarchy toBlockingwon’t automatically influence child transforms in the hierarchy. To do this, you’d need to explicitly set all child nodes
            to theBlockingstate.For example, to set all child transforms toBlocking, you could use the following script.import maya.cmds as cmds def blockTree(root): nodesToBlock = [] for node in {child:1 for child in cmds.listRelatives( root,
            path=True, allDescendents=True )}.keys(): nodesToBlock += cmds.listConnections(node, source=True, destination=True ) for node in {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' % node, 2 )Applying this script
            would continue to draw objects but things would not be animated.Default:kdnNormal
        - secondEdge (se): Second edge to merge. Invalid default value to force the value to be set.Default:-1
        - toolNode (tnq): Return the node used for tool defaults
        - query (q): Query mode flag
    """
@overload #Overload for polyMergeEdgeCtx in ['edit']
def polyMergeEdgeCtx(caching: bool = ..., firstEdge: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., immediate: bool = ..., mergeMode: int = ..., mergeTexture: bool = ..., nodeState: int = ..., previous: bool = ..., reset: bool = ..., secondEdge: int = ..., edit: bool = ...) -> str:
    """polyMergeEdgeCtx is undoable, queryable, and editable.
    
    Sews two border edges together.
    The new edge is located either on the first, last, or between both selected
    edges, depending on the mode.
    
    Both edges must belong to the same object, and orientations must match (i.e.
    normals on corresponding faces must point in the same direction).
    Edge flags are mandatory.
    
    Create a new context to merge edges on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        def blockTree(root):
        nodesToBlock = []
        for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
        nodesToBlock += cmds.listConnections(node, source=True, destination=True )
        for node in {source:1 for source in nodesToBlock}.keys():
        cmds.setAttr( '%s.nodeState' % node, 2 )
    ```

    ---
    - Args:
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - firstEdge (fe): First edge to merge. Invalid default value to force the value to be set.Default:-1
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - immediate (im): Acts on the object not the tool defaults
        - mergeMode (mm): Merge mode : 0=first, 1=halfway between both edges, 2=second.Default:1
        - mergeTexture (mt): Boolean which is used to decide if uv coordinates should be merged or not - along with the geometry.Default:false
        - nodeState (nds): Maya dependency nodes have 6 possible states. TheNormal (0),HasNoEffect (1), andBlocking (2)states can be used to alter how the graph is evaluated.TheWaiting-Normal (3),Waiting-HasNoEffect (4),Waiting-Blocking (5)are for internal use only.
            They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g.Waiting-Blockingwill reset back
            toBlocking.TheNormalandBlockingcases apply to all nodes, whileHasNoEffectis node specific; many nodes do not support this option. Plug-ins store state in theMPxNode::stateattribute. Anyone can set it or check this attribute.  Additional
            details about each of these 3 states follow.StateDescriptionNormalThe normal node state. This is the default.HasNoEffectTheHasNoEffectoption (a.k.a. pass-through), is used in cases where there is an operation on an input producing an output
            of the same data type. Nearly all deformers support this state, as do a few other nodes. As stated earlier, it is not supported by all nodes.It’s typical to implement support for theHasNoEffectstate in the node’s compute method and to
            perform appropriate operations. Plug-ins can also supportHasNoEffect.The usual implementation of this state is to copy the input directly to the matching output without applying the algorithm in the node. For deformers, applying this state
            leaves the input geometry undeformed on the output.BlockingThis is implemented in the depend node base class and applies to all nodes.Blockingis applied during the evaluation phase to connections. An evaluation request to a blocked
            connection will return as failures, causing the destination plug to retain its current value. Dirty propagation is indirectly affected by this state since blocked connections are never cleaned.When a node is set toBlockingthe behavior is
            supposed to be the same as if all outgoing connections were broken. As long as nobody requests evaluation of the blocked node directly it won’t evaluate after that. Note that a blocked node will still respond togetAttrrequests but
            agetAttron a downstream node will not reevaluate the blocked node.Setting the root transform of a hierarchy toBlockingwon’t automatically influence child transforms in the hierarchy. To do this, you’d need to explicitly set all child nodes
            to theBlockingstate.For example, to set all child transforms toBlocking, you could use the following script.import maya.cmds as cmds def blockTree(root): nodesToBlock = [] for node in {child:1 for child in cmds.listRelatives( root,
            path=True, allDescendents=True )}.keys(): nodesToBlock += cmds.listConnections(node, source=True, destination=True ) for node in {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' % node, 2 )Applying this script
            would continue to draw objects but things would not be animated.Default:kdnNormal
        - previous (pv): Reset to previously stored values
        - reset (rs): Reset to default values
        - secondEdge (se): Second edge to merge. Invalid default value to force the value to be set.Default:-1
        - edit (e): Edit mode flag
    """
@overload #Overload for polyMergeEdgeCtx in ['edit']
def polyMergeEdgeCtx(cch: bool = ..., fe: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., im: bool = ..., mm: int = ..., mt: bool = ..., nds: int = ..., pv: bool = ..., rs: bool = ..., se: int = ..., e: bool = ...) -> str:
    """polyMergeEdgeCtx is undoable, queryable, and editable.
    
    Sews two border edges together.
    The new edge is located either on the first, last, or between both selected
    edges, depending on the mode.
    
    Both edges must belong to the same object, and orientations must match (i.e.
    normals on corresponding faces must point in the same direction).
    Edge flags are mandatory.
    
    Create a new context to merge edges on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        def blockTree(root):
        nodesToBlock = []
        for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
        nodesToBlock += cmds.listConnections(node, source=True, destination=True )
        for node in {source:1 for source in nodesToBlock}.keys():
        cmds.setAttr( '%s.nodeState' % node, 2 )
    ```

    ---
    - Args:
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - firstEdge (fe): First edge to merge. Invalid default value to force the value to be set.Default:-1
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - immediate (im): Acts on the object not the tool defaults
        - mergeMode (mm): Merge mode : 0=first, 1=halfway between both edges, 2=second.Default:1
        - mergeTexture (mt): Boolean which is used to decide if uv coordinates should be merged or not - along with the geometry.Default:false
        - nodeState (nds): Maya dependency nodes have 6 possible states. TheNormal (0),HasNoEffect (1), andBlocking (2)states can be used to alter how the graph is evaluated.TheWaiting-Normal (3),Waiting-HasNoEffect (4),Waiting-Blocking (5)are for internal use only.
            They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g.Waiting-Blockingwill reset back
            toBlocking.TheNormalandBlockingcases apply to all nodes, whileHasNoEffectis node specific; many nodes do not support this option. Plug-ins store state in theMPxNode::stateattribute. Anyone can set it or check this attribute.  Additional
            details about each of these 3 states follow.StateDescriptionNormalThe normal node state. This is the default.HasNoEffectTheHasNoEffectoption (a.k.a. pass-through), is used in cases where there is an operation on an input producing an output
            of the same data type. Nearly all deformers support this state, as do a few other nodes. As stated earlier, it is not supported by all nodes.It’s typical to implement support for theHasNoEffectstate in the node’s compute method and to
            perform appropriate operations. Plug-ins can also supportHasNoEffect.The usual implementation of this state is to copy the input directly to the matching output without applying the algorithm in the node. For deformers, applying this state
            leaves the input geometry undeformed on the output.BlockingThis is implemented in the depend node base class and applies to all nodes.Blockingis applied during the evaluation phase to connections. An evaluation request to a blocked
            connection will return as failures, causing the destination plug to retain its current value. Dirty propagation is indirectly affected by this state since blocked connections are never cleaned.When a node is set toBlockingthe behavior is
            supposed to be the same as if all outgoing connections were broken. As long as nobody requests evaluation of the blocked node directly it won’t evaluate after that. Note that a blocked node will still respond togetAttrrequests but
            agetAttron a downstream node will not reevaluate the blocked node.Setting the root transform of a hierarchy toBlockingwon’t automatically influence child transforms in the hierarchy. To do this, you’d need to explicitly set all child nodes
            to theBlockingstate.For example, to set all child transforms toBlocking, you could use the following script.import maya.cmds as cmds def blockTree(root): nodesToBlock = [] for node in {child:1 for child in cmds.listRelatives( root,
            path=True, allDescendents=True )}.keys(): nodesToBlock += cmds.listConnections(node, source=True, destination=True ) for node in {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' % node, 2 )Applying this script
            would continue to draw objects but things would not be animated.Default:kdnNormal
        - previous (pv): Reset to previously stored values
        - reset (rs): Reset to default values
        - secondEdge (se): Second edge to merge. Invalid default value to force the value to be set.Default:-1
        - edit (e): Edit mode flag
    """
@overload #Overload for polyMergeEdgeCtx in ['edit']
def polyMergeEdgeCtx(caching: bool = ..., cch: bool = ..., firstEdge: int = ..., fe: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., immediate: bool = ..., im: bool = ..., mergeMode: int = ..., mm: int = ..., mergeTexture: bool = ..., mt: bool = ..., nodeState: int = ..., nds: int = ..., previous: bool = ..., pv: bool = ..., reset: bool = ..., rs: bool = ..., secondEdge: int = ..., se: int = ..., edit: bool = ..., e: bool = ...) -> str:
    """polyMergeEdgeCtx is undoable, queryable, and editable.
    
    Sews two border edges together.
    The new edge is located either on the first, last, or between both selected
    edges, depending on the mode.
    
    Both edges must belong to the same object, and orientations must match (i.e.
    normals on corresponding faces must point in the same direction).
    Edge flags are mandatory.
    
    Create a new context to merge edges on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        def blockTree(root):
        nodesToBlock = []
        for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
        nodesToBlock += cmds.listConnections(node, source=True, destination=True )
        for node in {source:1 for source in nodesToBlock}.keys():
        cmds.setAttr( '%s.nodeState' % node, 2 )
    ```

    ---
    - Args:
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - firstEdge (fe): First edge to merge. Invalid default value to force the value to be set.Default:-1
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - immediate (im): Acts on the object not the tool defaults
        - mergeMode (mm): Merge mode : 0=first, 1=halfway between both edges, 2=second.Default:1
        - mergeTexture (mt): Boolean which is used to decide if uv coordinates should be merged or not - along with the geometry.Default:false
        - nodeState (nds): Maya dependency nodes have 6 possible states. TheNormal (0),HasNoEffect (1), andBlocking (2)states can be used to alter how the graph is evaluated.TheWaiting-Normal (3),Waiting-HasNoEffect (4),Waiting-Blocking (5)are for internal use only.
            They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g.Waiting-Blockingwill reset back
            toBlocking.TheNormalandBlockingcases apply to all nodes, whileHasNoEffectis node specific; many nodes do not support this option. Plug-ins store state in theMPxNode::stateattribute. Anyone can set it or check this attribute.  Additional
            details about each of these 3 states follow.StateDescriptionNormalThe normal node state. This is the default.HasNoEffectTheHasNoEffectoption (a.k.a. pass-through), is used in cases where there is an operation on an input producing an output
            of the same data type. Nearly all deformers support this state, as do a few other nodes. As stated earlier, it is not supported by all nodes.It’s typical to implement support for theHasNoEffectstate in the node’s compute method and to
            perform appropriate operations. Plug-ins can also supportHasNoEffect.The usual implementation of this state is to copy the input directly to the matching output without applying the algorithm in the node. For deformers, applying this state
            leaves the input geometry undeformed on the output.BlockingThis is implemented in the depend node base class and applies to all nodes.Blockingis applied during the evaluation phase to connections. An evaluation request to a blocked
            connection will return as failures, causing the destination plug to retain its current value. Dirty propagation is indirectly affected by this state since blocked connections are never cleaned.When a node is set toBlockingthe behavior is
            supposed to be the same as if all outgoing connections were broken. As long as nobody requests evaluation of the blocked node directly it won’t evaluate after that. Note that a blocked node will still respond togetAttrrequests but
            agetAttron a downstream node will not reevaluate the blocked node.Setting the root transform of a hierarchy toBlockingwon’t automatically influence child transforms in the hierarchy. To do this, you’d need to explicitly set all child nodes
            to theBlockingstate.For example, to set all child transforms toBlocking, you could use the following script.import maya.cmds as cmds def blockTree(root): nodesToBlock = [] for node in {child:1 for child in cmds.listRelatives( root,
            path=True, allDescendents=True )}.keys(): nodesToBlock += cmds.listConnections(node, source=True, destination=True ) for node in {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' % node, 2 )Applying this script
            would continue to draw objects but things would not be animated.Default:kdnNormal
        - previous (pv): Reset to previously stored values
        - reset (rs): Reset to default values
        - secondEdge (se): Second edge to merge. Invalid default value to force the value to be set.Default:-1
        - edit (e): Edit mode flag
    """
