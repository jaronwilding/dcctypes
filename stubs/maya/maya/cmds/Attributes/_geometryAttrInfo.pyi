"""Stub files for Attributes category in Maya commands, command: geometryAttrInfo."""

from typing import Any, overload

@overload #Overload for geometryAttrInfo in ['create']
def geometryAttrInfo(attribute: attribute, boundingBox: bool = ..., castToEdges: bool = ..., castToFaces: bool = ..., castToVerts: bool = ..., componentTagCategory: bool = ..., componentTagExpression: str = ..., componentTagHash: bool = ..., componentTagHistory: bool = ..., componentTagHistoryHash: bool = ..., componentTagNames: bool = ..., components: bool = ..., deformerChain: bool = ..., elementCount: bool = ..., groupId: int = ..., matrix: bool = ..., nodeChain: bool = ..., originalGeometry: bool = ..., outputPlugChain: bool = ..., plugChain: bool = ..., pointCount: bool = ..., pointIndices: bool = ..., points: bool = ..., subsetState: bool = ...) -> Any:
    """geometryAttrInfo is undoable, NOT queryable, and NOT editable.
    
    This command provides information about the geometry in an attribute. This
    command therefore only works on attributes that contain geometry. A variety of
    types of information can be requested, like the number of verts, the
    boundingbox, which componentTags exist, etc.
    
    The requests can be made on a subset of the geometry, either limited by a
    specific groupId or by a componentTag expression. For example, when a
    componentTag expression is used, the requested indices will be the indices
    that match the subset as defined by that expression.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.polyCylinder(n="myGeo", r=1, h=6, sx=4, sy=5, sz=1)[0]
        cmds.select(['myGeo.vtx[12:23]', 'myGeo.vtx[25]'])
        clusterNode, clusterHandle = cmds.cluster()
        cmds.move(1.0, 0, 0, clusterHandle, absolute=True)
        # Find the groupId for the cluster node to test our queries
        gid = cmds.getAttr('{0}.input[0].groupId'.format(clusterNode))
        # Get the number of points
        n0 = cmds.geometryAttrInfo('myGeo.outMesh', pc=True)
        n1 = cmds.geometryAttrInfo('myGeo.outMesh', gid=gid, pc=True)
        print "Deforming {0} out of {1} points".format(n1, n0)
        # Deforming 13 out of 26 points
        # Get the indices that are being deformed
        cmds.geometryAttrInfo('myGeo.outMesh', gid=gid, pi=True)
        # Result: [12L, 13L, 14L, 15L, 16L, 17L, 18L, 19L, 20L, 21L, 22L, 23L, 25L] #
        # Get the components that are being deformed
        cmds.geometryAttrInfo('myGeo.outMesh', gid=gid, cmp=True)
        # Result: [u'vtx[12:23]', u'vtx[25]'] #
        # Get the bounding box of the total geometry
        cmds.geometryAttrInfo('myGeo.outMesh', bb=True)
        # Result: [-1.0, 2.0, -3.0, 3.0, -1.0, 1.0] #
        # Get the bounding box of what is being deformed
        cmds.geometryAttrInfo('myGeo.outMesh', gid=gid, bb=True)
        # Result: [0.0, 2.0, 0.6000001430511475, 3.0, -1.0, 1.0] #
        # Get the node chain leading up to the cluster]
        cmds.geometryAttrInfo('cluster1.outputGeometry[0]', nch=True)
        # Result: [u'polyCylinder1', u'myGeoShapeOrig', u'groupParts2', u'tweak1', u'cluster1GroupParts', u'cluster1'] #
        # Get the deformer chain leading up to the cluster
        cmds.geometryAttrInfo('cluster1.outputGeometry[0]', dch=True)
        # Result: [u'tweak1', u'cluster1'] #
        # Get the plug chain leading up to the cluster
        cmds.geometryAttrInfo('cluster1.outputGeometry[0]', pch=True)
        # Result: [u'polyCylinder1.output', u'myGeoShapeOrig.inMesh', u'myGeoShapeOrig.worldMesh[0]', u'groupParts2.inputGeometry', u'groupParts2.outputGeometry', u'tweak1.input[0].inputGeometry', u'tweak1.outputGeometry[0]', u'cluster1GroupParts.inputGeometry', u'cluster1GroupParts.outputGeometry', u'cluster1.input[0].inputGeometry', u'cluster1.outputGeometry[0]'] #
        # Get the output plug chain leading up to the cluster
        cmds.geometryAttrInfo('cluster1.outputGeometry[0]', och=True)
        # Result: [u'polyCylinder1.output', u'myGeoShapeOrig.worldMesh[0]', u'groupParts2.outputGeometry', u'tweak1.outputGeometry[0]', u'cluster1GroupParts.outputGeometry', u'cluster1.outputGeometry[0]'] #
    ```

    ---
    - Args:
        - attribute: Input item(s).
        - boundingBox (bb): Returns the bounding box of the geometry
        - castToEdges (cte): Ensures the componentTag expression will be resolved to edge components
        - castToFaces (ctf): Ensures the componentTag expression will be resolved to face components
        - castToVerts (ctv): Ensures the componentTag expression will be resolved to vert components
        - componentTagCategory (ccy): This flag will return the component tag category of the resulting components. Verts are "v", edges are "e", faces are "f". In case the the category can not be determined "unknown" is returned
        - componentTagExpression (cex): Specifies the componentTagExpression we want to query. When specified all answers to the information requests will be limited to the subset of the geometry as is contained in the combination of these componentTags
        - componentTagHash (hsh): This flag will return a unique hash value for the state of all the componentTags contained in the geometry. If a hash is different from before it means that something has changed, either tags have been added/removed/renamed and/or their
            component contents have been altered.
        - componentTagHistory (cth): This flag will return a description of the componentTags and the nodes in the chain where they were added to the geometry.
        - componentTagHistoryHash (chh): This flag will return a unique hash value for the componentTag history of the geometry in the plug. If a hash is different from before it means that something has changed, either different nodes have created the tags or the contents of the
            tags have been altered.
        - componentTagNames (cnm): Returns the names of the componentTags on the geometry
        - components (cmp): Returns the components of the geometry
        - deformerChain (dch): This flag will return the list of deformer nodes through which the geometry passes to the specified plug
        - elementCount (ec): Returns the element count of the components
        - groupId (gid): Specifies the groupId we want to query. When specified all answers to the information requests will be limited to the subset of the geometry as is contained in this groupId
        - matrix (mtx): Returns the matrix associated with the geometry
        - nodeChain (nch): This flag will return the list of nodes through which the geometry passes to the specified plug
        - originalGeometry (og): This flag will return the name of a plug on a node upstream (likely at the front end) that is the best candidate to be used as the originalGeometry. This can return an empty plug when none exists.
        - outputPlugChain (och): This flag will return the chain of plugs upstream of the specified plug (including only output plugs)
        - plugChain (pch): This flag will return the chain of plugs upstream of the specified plug (including both input and output plugs)
        - pointCount (pc): Returns the point count of the geometry
        - pointIndices (pi): Returns the indices of the geometry
        - points (pnt): Returns a list of points of the geometry
        - subsetState (sbs): Returns the state of the specified subset -1 means the subset was invalid 0 means the subset contains none of the points of the geometry 1 means the subset contains some (but not all) of the points of the geometry 2 means the subset
            contains all the points of the geometry
    """
@overload #Overload for geometryAttrInfo in ['create']
def geometryAttrInfo(attribute: attribute, bb: bool = ..., cte: bool = ..., ctf: bool = ..., ctv: bool = ..., ccy: bool = ..., cex: str = ..., hsh: bool = ..., cth: bool = ..., chh: bool = ..., cnm: bool = ..., cmp: bool = ..., dch: bool = ..., ec: bool = ..., gid: int = ..., mtx: bool = ..., nch: bool = ..., og: bool = ..., och: bool = ..., pch: bool = ..., pc: bool = ..., pi: bool = ..., pnt: bool = ..., sbs: bool = ...) -> Any:
    """geometryAttrInfo is undoable, NOT queryable, and NOT editable.
    
    This command provides information about the geometry in an attribute. This
    command therefore only works on attributes that contain geometry. A variety of
    types of information can be requested, like the number of verts, the
    boundingbox, which componentTags exist, etc.
    
    The requests can be made on a subset of the geometry, either limited by a
    specific groupId or by a componentTag expression. For example, when a
    componentTag expression is used, the requested indices will be the indices
    that match the subset as defined by that expression.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.polyCylinder(n="myGeo", r=1, h=6, sx=4, sy=5, sz=1)[0]
        cmds.select(['myGeo.vtx[12:23]', 'myGeo.vtx[25]'])
        clusterNode, clusterHandle = cmds.cluster()
        cmds.move(1.0, 0, 0, clusterHandle, absolute=True)
        # Find the groupId for the cluster node to test our queries
        gid = cmds.getAttr('{0}.input[0].groupId'.format(clusterNode))
        # Get the number of points
        n0 = cmds.geometryAttrInfo('myGeo.outMesh', pc=True)
        n1 = cmds.geometryAttrInfo('myGeo.outMesh', gid=gid, pc=True)
        print "Deforming {0} out of {1} points".format(n1, n0)
        # Deforming 13 out of 26 points
        # Get the indices that are being deformed
        cmds.geometryAttrInfo('myGeo.outMesh', gid=gid, pi=True)
        # Result: [12L, 13L, 14L, 15L, 16L, 17L, 18L, 19L, 20L, 21L, 22L, 23L, 25L] #
        # Get the components that are being deformed
        cmds.geometryAttrInfo('myGeo.outMesh', gid=gid, cmp=True)
        # Result: [u'vtx[12:23]', u'vtx[25]'] #
        # Get the bounding box of the total geometry
        cmds.geometryAttrInfo('myGeo.outMesh', bb=True)
        # Result: [-1.0, 2.0, -3.0, 3.0, -1.0, 1.0] #
        # Get the bounding box of what is being deformed
        cmds.geometryAttrInfo('myGeo.outMesh', gid=gid, bb=True)
        # Result: [0.0, 2.0, 0.6000001430511475, 3.0, -1.0, 1.0] #
        # Get the node chain leading up to the cluster]
        cmds.geometryAttrInfo('cluster1.outputGeometry[0]', nch=True)
        # Result: [u'polyCylinder1', u'myGeoShapeOrig', u'groupParts2', u'tweak1', u'cluster1GroupParts', u'cluster1'] #
        # Get the deformer chain leading up to the cluster
        cmds.geometryAttrInfo('cluster1.outputGeometry[0]', dch=True)
        # Result: [u'tweak1', u'cluster1'] #
        # Get the plug chain leading up to the cluster
        cmds.geometryAttrInfo('cluster1.outputGeometry[0]', pch=True)
        # Result: [u'polyCylinder1.output', u'myGeoShapeOrig.inMesh', u'myGeoShapeOrig.worldMesh[0]', u'groupParts2.inputGeometry', u'groupParts2.outputGeometry', u'tweak1.input[0].inputGeometry', u'tweak1.outputGeometry[0]', u'cluster1GroupParts.inputGeometry', u'cluster1GroupParts.outputGeometry', u'cluster1.input[0].inputGeometry', u'cluster1.outputGeometry[0]'] #
        # Get the output plug chain leading up to the cluster
        cmds.geometryAttrInfo('cluster1.outputGeometry[0]', och=True)
        # Result: [u'polyCylinder1.output', u'myGeoShapeOrig.worldMesh[0]', u'groupParts2.outputGeometry', u'tweak1.outputGeometry[0]', u'cluster1GroupParts.outputGeometry', u'cluster1.outputGeometry[0]'] #
    ```

    ---
    - Args:
        - attribute: Input item(s).
        - boundingBox (bb): Returns the bounding box of the geometry
        - castToEdges (cte): Ensures the componentTag expression will be resolved to edge components
        - castToFaces (ctf): Ensures the componentTag expression will be resolved to face components
        - castToVerts (ctv): Ensures the componentTag expression will be resolved to vert components
        - componentTagCategory (ccy): This flag will return the component tag category of the resulting components. Verts are "v", edges are "e", faces are "f". In case the the category can not be determined "unknown" is returned
        - componentTagExpression (cex): Specifies the componentTagExpression we want to query. When specified all answers to the information requests will be limited to the subset of the geometry as is contained in the combination of these componentTags
        - componentTagHash (hsh): This flag will return a unique hash value for the state of all the componentTags contained in the geometry. If a hash is different from before it means that something has changed, either tags have been added/removed/renamed and/or their
            component contents have been altered.
        - componentTagHistory (cth): This flag will return a description of the componentTags and the nodes in the chain where they were added to the geometry.
        - componentTagHistoryHash (chh): This flag will return a unique hash value for the componentTag history of the geometry in the plug. If a hash is different from before it means that something has changed, either different nodes have created the tags or the contents of the
            tags have been altered.
        - componentTagNames (cnm): Returns the names of the componentTags on the geometry
        - components (cmp): Returns the components of the geometry
        - deformerChain (dch): This flag will return the list of deformer nodes through which the geometry passes to the specified plug
        - elementCount (ec): Returns the element count of the components
        - groupId (gid): Specifies the groupId we want to query. When specified all answers to the information requests will be limited to the subset of the geometry as is contained in this groupId
        - matrix (mtx): Returns the matrix associated with the geometry
        - nodeChain (nch): This flag will return the list of nodes through which the geometry passes to the specified plug
        - originalGeometry (og): This flag will return the name of a plug on a node upstream (likely at the front end) that is the best candidate to be used as the originalGeometry. This can return an empty plug when none exists.
        - outputPlugChain (och): This flag will return the chain of plugs upstream of the specified plug (including only output plugs)
        - plugChain (pch): This flag will return the chain of plugs upstream of the specified plug (including both input and output plugs)
        - pointCount (pc): Returns the point count of the geometry
        - pointIndices (pi): Returns the indices of the geometry
        - points (pnt): Returns a list of points of the geometry
        - subsetState (sbs): Returns the state of the specified subset -1 means the subset was invalid 0 means the subset contains none of the points of the geometry 1 means the subset contains some (but not all) of the points of the geometry 2 means the subset
            contains all the points of the geometry
    """
@overload #Overload for geometryAttrInfo in ['create']
def geometryAttrInfo(attribute: attribute, boundingBox: bool = ..., bb: bool = ..., castToEdges: bool = ..., cte: bool = ..., castToFaces: bool = ..., ctf: bool = ..., castToVerts: bool = ..., ctv: bool = ..., componentTagCategory: bool = ..., ccy: bool = ..., componentTagExpression: str = ..., cex: str = ..., componentTagHash: bool = ..., hsh: bool = ..., componentTagHistory: bool = ..., cth: bool = ..., componentTagHistoryHash: bool = ..., chh: bool = ..., componentTagNames: bool = ..., cnm: bool = ..., components: bool = ..., cmp: bool = ..., deformerChain: bool = ..., dch: bool = ..., elementCount: bool = ..., ec: bool = ..., groupId: int = ..., gid: int = ..., matrix: bool = ..., mtx: bool = ..., nodeChain: bool = ..., nch: bool = ..., originalGeometry: bool = ..., og: bool = ..., outputPlugChain: bool = ..., och: bool = ..., plugChain: bool = ..., pch: bool = ..., pointCount: bool = ..., pc: bool = ..., pointIndices: bool = ..., pi: bool = ..., points: bool = ..., pnt: bool = ..., subsetState: bool = ..., sbs: bool = ...) -> Any:
    """geometryAttrInfo is undoable, NOT queryable, and NOT editable.
    
    This command provides information about the geometry in an attribute. This
    command therefore only works on attributes that contain geometry. A variety of
    types of information can be requested, like the number of verts, the
    boundingbox, which componentTags exist, etc.
    
    The requests can be made on a subset of the geometry, either limited by a
    specific groupId or by a componentTag expression. For example, when a
    componentTag expression is used, the requested indices will be the indices
    that match the subset as defined by that expression.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.polyCylinder(n="myGeo", r=1, h=6, sx=4, sy=5, sz=1)[0]
        cmds.select(['myGeo.vtx[12:23]', 'myGeo.vtx[25]'])
        clusterNode, clusterHandle = cmds.cluster()
        cmds.move(1.0, 0, 0, clusterHandle, absolute=True)
        # Find the groupId for the cluster node to test our queries
        gid = cmds.getAttr('{0}.input[0].groupId'.format(clusterNode))
        # Get the number of points
        n0 = cmds.geometryAttrInfo('myGeo.outMesh', pc=True)
        n1 = cmds.geometryAttrInfo('myGeo.outMesh', gid=gid, pc=True)
        print "Deforming {0} out of {1} points".format(n1, n0)
        # Deforming 13 out of 26 points
        # Get the indices that are being deformed
        cmds.geometryAttrInfo('myGeo.outMesh', gid=gid, pi=True)
        # Result: [12L, 13L, 14L, 15L, 16L, 17L, 18L, 19L, 20L, 21L, 22L, 23L, 25L] #
        # Get the components that are being deformed
        cmds.geometryAttrInfo('myGeo.outMesh', gid=gid, cmp=True)
        # Result: [u'vtx[12:23]', u'vtx[25]'] #
        # Get the bounding box of the total geometry
        cmds.geometryAttrInfo('myGeo.outMesh', bb=True)
        # Result: [-1.0, 2.0, -3.0, 3.0, -1.0, 1.0] #
        # Get the bounding box of what is being deformed
        cmds.geometryAttrInfo('myGeo.outMesh', gid=gid, bb=True)
        # Result: [0.0, 2.0, 0.6000001430511475, 3.0, -1.0, 1.0] #
        # Get the node chain leading up to the cluster]
        cmds.geometryAttrInfo('cluster1.outputGeometry[0]', nch=True)
        # Result: [u'polyCylinder1', u'myGeoShapeOrig', u'groupParts2', u'tweak1', u'cluster1GroupParts', u'cluster1'] #
        # Get the deformer chain leading up to the cluster
        cmds.geometryAttrInfo('cluster1.outputGeometry[0]', dch=True)
        # Result: [u'tweak1', u'cluster1'] #
        # Get the plug chain leading up to the cluster
        cmds.geometryAttrInfo('cluster1.outputGeometry[0]', pch=True)
        # Result: [u'polyCylinder1.output', u'myGeoShapeOrig.inMesh', u'myGeoShapeOrig.worldMesh[0]', u'groupParts2.inputGeometry', u'groupParts2.outputGeometry', u'tweak1.input[0].inputGeometry', u'tweak1.outputGeometry[0]', u'cluster1GroupParts.inputGeometry', u'cluster1GroupParts.outputGeometry', u'cluster1.input[0].inputGeometry', u'cluster1.outputGeometry[0]'] #
        # Get the output plug chain leading up to the cluster
        cmds.geometryAttrInfo('cluster1.outputGeometry[0]', och=True)
        # Result: [u'polyCylinder1.output', u'myGeoShapeOrig.worldMesh[0]', u'groupParts2.outputGeometry', u'tweak1.outputGeometry[0]', u'cluster1GroupParts.outputGeometry', u'cluster1.outputGeometry[0]'] #
    ```

    ---
    - Args:
        - attribute: Input item(s).
        - boundingBox (bb): Returns the bounding box of the geometry
        - castToEdges (cte): Ensures the componentTag expression will be resolved to edge components
        - castToFaces (ctf): Ensures the componentTag expression will be resolved to face components
        - castToVerts (ctv): Ensures the componentTag expression will be resolved to vert components
        - componentTagCategory (ccy): This flag will return the component tag category of the resulting components. Verts are "v", edges are "e", faces are "f". In case the the category can not be determined "unknown" is returned
        - componentTagExpression (cex): Specifies the componentTagExpression we want to query. When specified all answers to the information requests will be limited to the subset of the geometry as is contained in the combination of these componentTags
        - componentTagHash (hsh): This flag will return a unique hash value for the state of all the componentTags contained in the geometry. If a hash is different from before it means that something has changed, either tags have been added/removed/renamed and/or their
            component contents have been altered.
        - componentTagHistory (cth): This flag will return a description of the componentTags and the nodes in the chain where they were added to the geometry.
        - componentTagHistoryHash (chh): This flag will return a unique hash value for the componentTag history of the geometry in the plug. If a hash is different from before it means that something has changed, either different nodes have created the tags or the contents of the
            tags have been altered.
        - componentTagNames (cnm): Returns the names of the componentTags on the geometry
        - components (cmp): Returns the components of the geometry
        - deformerChain (dch): This flag will return the list of deformer nodes through which the geometry passes to the specified plug
        - elementCount (ec): Returns the element count of the components
        - groupId (gid): Specifies the groupId we want to query. When specified all answers to the information requests will be limited to the subset of the geometry as is contained in this groupId
        - matrix (mtx): Returns the matrix associated with the geometry
        - nodeChain (nch): This flag will return the list of nodes through which the geometry passes to the specified plug
        - originalGeometry (og): This flag will return the name of a plug on a node upstream (likely at the front end) that is the best candidate to be used as the originalGeometry. This can return an empty plug when none exists.
        - outputPlugChain (och): This flag will return the chain of plugs upstream of the specified plug (including only output plugs)
        - plugChain (pch): This flag will return the chain of plugs upstream of the specified plug (including both input and output plugs)
        - pointCount (pc): Returns the point count of the geometry
        - pointIndices (pi): Returns the indices of the geometry
        - points (pnt): Returns a list of points of the geometry
        - subsetState (sbs): Returns the state of the specified subset -1 means the subset was invalid 0 means the subset contains none of the points of the geometry 1 means the subset contains some (but not all) of the points of the geometry 2 means the subset
            contains all the points of the geometry
    """
