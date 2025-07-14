"""Stub files for Contexts category in Maya commands, command: polyMergeFacetCtx."""

from typing import Any, overload

@overload #Overload for polyMergeFacetCtx in ['create']
def polyMergeFacetCtx(caching: bool = ..., constructionHistory: bool = ..., exists: bool = ..., firstFacet: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., mergeMode: int = ..., name: str = ..., nodeState: int = ..., secondFacet: int = ...) -> str:
    """polyMergeFacetCtx is undoable, queryable, and editable.
    
    The second face becomes a hole in the first face.
    The new holed face is located either on the first, last, or between both
    selected faces, depending on the mode.
    
    Both faces must belong to the same object.
    Facet flags are mandatory.
    
    Create a new context to merge facets on polygonal objects

    ---
    - Args:
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - constructionHistory (ch): Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed
            directly on the object.Note:If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - firstFacet (ff): The number of the first (outer) face to merge.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeMode (mm): This flag specifies how faces are merged: 0: moves second face to first one 1: moves both faces to average 2: moves first face to second one 3, 4, 5: same as above, except faces are projected but not centred 6: Nothing moves.C: Default is
            None (6).
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
        - secondFacet (sf): The number of the second (hole) face to merge.
    """
@overload #Overload for polyMergeFacetCtx in ['create']
def polyMergeFacetCtx(cch: bool = ..., ch: bool = ..., ex: bool = ..., ff: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., mm: int = ..., n: str = ..., nds: int = ..., sf: int = ...) -> str:
    """polyMergeFacetCtx is undoable, queryable, and editable.
    
    The second face becomes a hole in the first face.
    The new holed face is located either on the first, last, or between both
    selected faces, depending on the mode.
    
    Both faces must belong to the same object.
    Facet flags are mandatory.
    
    Create a new context to merge facets on polygonal objects

    ---
    - Args:
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - constructionHistory (ch): Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed
            directly on the object.Note:If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - firstFacet (ff): The number of the first (outer) face to merge.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeMode (mm): This flag specifies how faces are merged: 0: moves second face to first one 1: moves both faces to average 2: moves first face to second one 3, 4, 5: same as above, except faces are projected but not centred 6: Nothing moves.C: Default is
            None (6).
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
        - secondFacet (sf): The number of the second (hole) face to merge.
    """
@overload #Overload for polyMergeFacetCtx in ['create']
def polyMergeFacetCtx(caching: bool = ..., cch: bool = ..., constructionHistory: bool = ..., ch: bool = ..., exists: bool = ..., ex: bool = ..., firstFacet: int = ..., ff: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., mergeMode: int = ..., mm: int = ..., name: str = ..., n: str = ..., nodeState: int = ..., nds: int = ..., secondFacet: int = ..., sf: int = ...) -> str:
    """polyMergeFacetCtx is undoable, queryable, and editable.
    
    The second face becomes a hole in the first face.
    The new holed face is located either on the first, last, or between both
    selected faces, depending on the mode.
    
    Both faces must belong to the same object.
    Facet flags are mandatory.
    
    Create a new context to merge facets on polygonal objects

    ---
    - Args:
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - constructionHistory (ch): Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed
            directly on the object.Note:If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - firstFacet (ff): The number of the first (outer) face to merge.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeMode (mm): This flag specifies how faces are merged: 0: moves second face to first one 1: moves both faces to average 2: moves first face to second one 3, 4, 5: same as above, except faces are projected but not centred 6: Nothing moves.C: Default is
            None (6).
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
        - secondFacet (sf): The number of the second (hole) face to merge.
    """
@overload #Overload for polyMergeFacetCtx in ['query']
def polyMergeFacetCtx(activeNodes: bool = ..., caching: bool = ..., constructionHistory: bool = ..., firstFacet: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., mergeMode: int = ..., nodeState: int = ..., secondFacet: int = ..., toolNode: bool = ..., query: bool = ...) -> str:
    """polyMergeFacetCtx is undoable, queryable, and editable.
    
    The second face becomes a hole in the first face.
    The new holed face is located either on the first, last, or between both
    selected faces, depending on the mode.
    
    Both faces must belong to the same object.
    Facet flags are mandatory.
    
    Create a new context to merge facets on polygonal objects

    ---
    - Args:
        - activeNodes (anq): Return the active nodes in the tool
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - constructionHistory (ch): Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed
            directly on the object.Note:If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        - firstFacet (ff): The number of the first (outer) face to merge.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeMode (mm): This flag specifies how faces are merged: 0: moves second face to first one 1: moves both faces to average 2: moves first face to second one 3, 4, 5: same as above, except faces are projected but not centred 6: Nothing moves.C: Default is
            None (6).
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
        - secondFacet (sf): The number of the second (hole) face to merge.
        - toolNode (tnq): Return the node used for tool defaults
        - query (q): Query mode flag
    """
@overload #Overload for polyMergeFacetCtx in ['query']
def polyMergeFacetCtx(anq: bool = ..., cch: bool = ..., ch: bool = ..., ff: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., mm: int = ..., nds: int = ..., sf: int = ..., tnq: bool = ..., q: bool = ...) -> str:
    """polyMergeFacetCtx is undoable, queryable, and editable.
    
    The second face becomes a hole in the first face.
    The new holed face is located either on the first, last, or between both
    selected faces, depending on the mode.
    
    Both faces must belong to the same object.
    Facet flags are mandatory.
    
    Create a new context to merge facets on polygonal objects

    ---
    - Args:
        - activeNodes (anq): Return the active nodes in the tool
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - constructionHistory (ch): Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed
            directly on the object.Note:If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        - firstFacet (ff): The number of the first (outer) face to merge.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeMode (mm): This flag specifies how faces are merged: 0: moves second face to first one 1: moves both faces to average 2: moves first face to second one 3, 4, 5: same as above, except faces are projected but not centred 6: Nothing moves.C: Default is
            None (6).
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
        - secondFacet (sf): The number of the second (hole) face to merge.
        - toolNode (tnq): Return the node used for tool defaults
        - query (q): Query mode flag
    """
@overload #Overload for polyMergeFacetCtx in ['query']
def polyMergeFacetCtx(activeNodes: bool = ..., anq: bool = ..., caching: bool = ..., cch: bool = ..., constructionHistory: bool = ..., ch: bool = ..., firstFacet: int = ..., ff: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., mergeMode: int = ..., mm: int = ..., nodeState: int = ..., nds: int = ..., secondFacet: int = ..., sf: int = ..., toolNode: bool = ..., tnq: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """polyMergeFacetCtx is undoable, queryable, and editable.
    
    The second face becomes a hole in the first face.
    The new holed face is located either on the first, last, or between both
    selected faces, depending on the mode.
    
    Both faces must belong to the same object.
    Facet flags are mandatory.
    
    Create a new context to merge facets on polygonal objects

    ---
    - Args:
        - activeNodes (anq): Return the active nodes in the tool
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - constructionHistory (ch): Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed
            directly on the object.Note:If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        - firstFacet (ff): The number of the first (outer) face to merge.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeMode (mm): This flag specifies how faces are merged: 0: moves second face to first one 1: moves both faces to average 2: moves first face to second one 3, 4, 5: same as above, except faces are projected but not centred 6: Nothing moves.C: Default is
            None (6).
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
        - secondFacet (sf): The number of the second (hole) face to merge.
        - toolNode (tnq): Return the node used for tool defaults
        - query (q): Query mode flag
    """
@overload #Overload for polyMergeFacetCtx in ['edit']
def polyMergeFacetCtx(caching: bool = ..., constructionHistory: bool = ..., firstFacet: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., immediate: bool = ..., mergeMode: int = ..., nodeState: int = ..., previous: bool = ..., reset: bool = ..., secondFacet: int = ..., edit: bool = ...) -> str:
    """polyMergeFacetCtx is undoable, queryable, and editable.
    
    The second face becomes a hole in the first face.
    The new holed face is located either on the first, last, or between both
    selected faces, depending on the mode.
    
    Both faces must belong to the same object.
    Facet flags are mandatory.
    
    Create a new context to merge facets on polygonal objects

    ---
    - Args:
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - constructionHistory (ch): Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed
            directly on the object.Note:If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        - firstFacet (ff): The number of the first (outer) face to merge.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - immediate (im): Acts on the object not the tool defaults
        - mergeMode (mm): This flag specifies how faces are merged: 0: moves second face to first one 1: moves both faces to average 2: moves first face to second one 3, 4, 5: same as above, except faces are projected but not centred 6: Nothing moves.C: Default is
            None (6).
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
        - secondFacet (sf): The number of the second (hole) face to merge.
        - edit (e): Edit mode flag
    """
@overload #Overload for polyMergeFacetCtx in ['edit']
def polyMergeFacetCtx(cch: bool = ..., ch: bool = ..., ff: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., im: bool = ..., mm: int = ..., nds: int = ..., pv: bool = ..., rs: bool = ..., sf: int = ..., e: bool = ...) -> str:
    """polyMergeFacetCtx is undoable, queryable, and editable.
    
    The second face becomes a hole in the first face.
    The new holed face is located either on the first, last, or between both
    selected faces, depending on the mode.
    
    Both faces must belong to the same object.
    Facet flags are mandatory.
    
    Create a new context to merge facets on polygonal objects

    ---
    - Args:
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - constructionHistory (ch): Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed
            directly on the object.Note:If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        - firstFacet (ff): The number of the first (outer) face to merge.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - immediate (im): Acts on the object not the tool defaults
        - mergeMode (mm): This flag specifies how faces are merged: 0: moves second face to first one 1: moves both faces to average 2: moves first face to second one 3, 4, 5: same as above, except faces are projected but not centred 6: Nothing moves.C: Default is
            None (6).
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
        - secondFacet (sf): The number of the second (hole) face to merge.
        - edit (e): Edit mode flag
    """
@overload #Overload for polyMergeFacetCtx in ['edit']
def polyMergeFacetCtx(caching: bool = ..., cch: bool = ..., constructionHistory: bool = ..., ch: bool = ..., firstFacet: int = ..., ff: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., immediate: bool = ..., im: bool = ..., mergeMode: int = ..., mm: int = ..., nodeState: int = ..., nds: int = ..., previous: bool = ..., pv: bool = ..., reset: bool = ..., rs: bool = ..., secondFacet: int = ..., sf: int = ..., edit: bool = ..., e: bool = ...) -> str:
    """polyMergeFacetCtx is undoable, queryable, and editable.
    
    The second face becomes a hole in the first face.
    The new holed face is located either on the first, last, or between both
    selected faces, depending on the mode.
    
    Both faces must belong to the same object.
    Facet flags are mandatory.
    
    Create a new context to merge facets on polygonal objects

    ---
    - Args:
        - caching (cch): Toggle caching for all attributes so that no recomputation is needed
        - constructionHistory (ch): Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed
            directly on the object.Note:If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        - firstFacet (ff): The number of the first (outer) face to merge.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - immediate (im): Acts on the object not the tool defaults
        - mergeMode (mm): This flag specifies how faces are merged: 0: moves second face to first one 1: moves both faces to average 2: moves first face to second one 3, 4, 5: same as above, except faces are projected but not centred 6: Nothing moves.C: Default is
            None (6).
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
        - secondFacet (sf): The number of the second (hole) face to merge.
        - edit (e): Edit mode flag
    """
