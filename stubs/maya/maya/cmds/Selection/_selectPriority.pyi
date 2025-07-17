"""Stub files for Selection category in Maya commands, command: selectPriority."""

from typing import Any, overload

@overload #Overload for selectPriority in ['create']
def selectPriority(allComponents: int = ..., allObjects: int = ..., animBreakdown: int = ..., animCurve: int = ..., animInTangent: int = ..., animKeyframe: int = ..., animOutTangent: int = ..., byName: [string, boolean] = ..., camera: int = ..., cluster: int = ..., collisionModel: int = ..., controlVertex: int = ..., curve: int = ..., curveKnot: int = ..., curveOnSurface: int = ..., curveParameterPoint: int = ..., dimension: int = ..., dynamicConstraint: int = ..., edge: int = ..., editPoint: int = ..., emitter: int = ..., facet: int = ..., field: int = ..., fluid: int = ..., follicle: int = ..., hairSystem: int = ..., handle: int = ..., hull: int = ..., ikEndEffector: int = ..., ikHandle: int = ..., imagePlane: int = ..., implicitGeometry: int = ..., isoparm: int = ..., joint: int = ..., jointPivot: int = ..., lattice: int = ..., latticePoint: int = ..., light: int = ..., localRotationAxis: int = ..., locator: int = ..., locatorUV: int = ..., locatorXYZ: int = ..., meshUVShell: int = ..., motionTrailPoint: int = ..., motionTrailTangent: int = ..., nCloth: int = ..., nParticle: int = ..., nParticleShape: int = ..., nRigid: int = ..., nonlinear: int = ..., nurbsCurve: int = ..., nurbsSurface: int = ..., orientationLocator: int = ..., particle: int = ..., particleShape: int = ..., plane: int = ..., polymesh: int = ..., polymeshEdge: int = ..., polymeshFace: int = ..., polymeshFreeEdge: int = ..., polymeshUV: int = ..., polymeshVertex: int = ..., polymeshVtxFace: int = ..., rigidBody: int = ..., rigidConstraint: int = ..., rotatePivot: int = ..., scalePivot: int = ..., sculpt: int = ..., selectHandle: int = ..., spring: int = ..., springComponent: int = ..., stroke: int = ..., subdiv: int = ..., subdivMeshEdge: int = ..., subdivMeshFace: int = ..., subdivMeshPoint: int = ..., subdivMeshUV: int = ..., surfaceEdge: int = ..., surfaceFace: int = ..., surfaceKnot: int = ..., surfaceParameterPoint: int = ..., surfaceRange: int = ..., texture: int = ..., vertex: int = ...) -> int:
    """selectPriority is undoable, queryable, and NOT editable.
    
    The selectPriority command is used to change the selection priority of
    particular types of objects that can be selected when using the select tool.
    It accepts no other arguments besides the flags. These flags are the same as
    used by the 'selectType' command.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.selectPriority( q=True, nurbsCurve=True )
        cmds.selectPriority( nurbsCurve=10 )
        cmds.selectPriority( handle=9, ikHandle=8 )
    ```

    ---
    - Args:
        - allComponents (alc): Set all component selection priority
        - allObjects (alo): Set all object selection priority
        - animBreakdown (abd): Set animation breakdown selection priority
        - animCurve (ac): Set animation curve selection priority
        - animInTangent (ait): Set animation in-tangent selection priority
        - animKeyframe (ak): Set animation keyframe selection priority
        - animOutTangent (aot): Set animation out-tangent selection priority
        - byName (bn): Set selection priority for the specified user-defined selection type
        - camera (ca): Set camera selection priority
        - cluster (cl): Set cluster selection priority
        - collisionModel (clm): Set collision model selection priority
        - controlVertex (cv): Set control vertex selection priority
        - curve (c): Set curve selection priority
        - curveKnot (ck): Set curve knot selection priority
        - curveOnSurface (cos): Set curve-on-surface selection priority
        - curveParameterPoint (cpp): Set curve parameter point selection priority
        - dimension (dim): Set dimension shape selection priority
        - dynamicConstraint (dc): Set dynamicConstraint selection priority
        - edge (eg): Set mesh edge selection priority
        - editPoint (ep): Set edit-point selection priority
        - emitter (em): Set emitter selection priority
        - facet (fc): Set mesh face selection priority
        - field (fi): Set field selection priority
        - fluid (fl): Set fluid selection priority
        - follicle (fo): Set follicle selection priority
        - hairSystem (hs): Set hairSystem selection priority
        - handle (ha): Set object handle selection priority
        - hull (hl): Set hull selection priority
        - ikEndEffector (iee): Set ik end effector selection priority
        - ikHandle (ikh): Set ik handle selection priority
        - imagePlane (ip): Set image plane selection mask priority
        - implicitGeometry (ig): Set implicit geometry selection priority
        - isoparm (iso): Set surface iso-parm selection priority
        - joint (j): Set ik handle selection priority
        - jointPivot (jp): Set joint pivot selection priority
        - lattice (la): Set lattice selection priority
        - latticePoint (lp): Set lattice point selection priority
        - light (lt): Set light selection priority
        - localRotationAxis (ra): Set local rotation axis selection priority
        - locator (lc): Set locator (all types) selection priority
        - locatorUV (luv): Set uv locator selection priority
        - locatorXYZ (xyz): Set xyz locator selection priority
        - meshUVShell (msh): Set uv shell component mask on/off.
        - motionTrailPoint (mtp): Set motion point selection priority
        - motionTrailTangent (mtt): Set motion point tangent priority
        - nCloth (ncl): Set nCloth selection priority
        - nParticle (npr): Set nParticle point selection priority
        - nParticleShape (nps): Set nParticle shape selection priority
        - nRigid (nr): Set nRigid selection priority
        - nonlinear (nl): Set nonlinear selection priority
        - nurbsCurve (nc): Set nurbs-curve selection priority
        - nurbsSurface (ns): Set nurbs-surface selection priority
        - orientationLocator (ol): Set orientation locator selection priority
        - particle (pr): Set particle point selection priority
        - particleShape (ps): Set particle shape selection priority
        - plane (pl): Set sketch plane selection priority
        - polymesh (p): Set poly-mesh selection priority
        - polymeshEdge (pe): Set poly-mesh edge selection priority
        - polymeshFace (pf): Set poly-mesh face selection priority
        - polymeshFreeEdge (pfe): Set poly-mesh free-edge selection priority
        - polymeshUV (puv): Set poly-mesh UV point selection priority
        - polymeshVertex (pv): Set poly-mesh vertex selection priority
        - polymeshVtxFace (pvf): Set poly-mesh vtxFace selection priority
        - rigidBody (rb): Set rigid body selection priority
        - rigidConstraint (rc): Set rigid constraint selection priority
        - rotatePivot (rp): Set rotate pivot selection priority
        - scalePivot (sp): Set scale pivot selection priority
        - sculpt (sc): Set sculpt selection priority
        - selectHandle (sh): Set select handle selection priority
        - spring (spr): Set spring shape selection priority
        - springComponent (spc): Set individual spring selection priority
        - stroke (str): Set stroke selection priority
        - subdiv (sd): Set subdivision surface selection priority
        - subdivMeshEdge (sme): Set subdivision surface mesh edge selection priority
        - subdivMeshFace (smf): Set subdivision surface mesh face selection priority
        - subdivMeshPoint (smp): Set subdivision surface mesh point selection priority
        - subdivMeshUV (smu): Set subdivision surface mesh UV map selection priority
        - surfaceEdge (se): Set surface edge selection priority
        - surfaceFace (sf): Set surface face selection priority
        - surfaceKnot (sk): Set surface knot selection priority
        - surfaceParameterPoint (spp): Set surface parameter point selection priority
        - surfaceRange (sr): Set surface range selection priority
        - texture (tx): Set texture selection priority
        - vertex (v): Set mesh vertex selection priority
    """
@overload #Overload for selectPriority in ['create']
def selectPriority(alc: int = ..., alo: int = ..., abd: int = ..., ac: int = ..., ait: int = ..., ak: int = ..., aot: int = ..., bn: [string, boolean] = ..., ca: int = ..., cl: int = ..., clm: int = ..., cv: int = ..., c: int = ..., ck: int = ..., cos: int = ..., cpp: int = ..., dim: int = ..., dc: int = ..., eg: int = ..., ep: int = ..., em: int = ..., fc: int = ..., fi: int = ..., fl: int = ..., fo: int = ..., hs: int = ..., ha: int = ..., hl: int = ..., iee: int = ..., ikh: int = ..., ip: int = ..., ig: int = ..., iso: int = ..., j: int = ..., jp: int = ..., la: int = ..., lp: int = ..., lt: int = ..., ra: int = ..., lc: int = ..., luv: int = ..., xyz: int = ..., msh: int = ..., mtp: int = ..., mtt: int = ..., ncl: int = ..., npr: int = ..., nps: int = ..., nr: int = ..., nl: int = ..., nc: int = ..., ns: int = ..., ol: int = ..., pr: int = ..., ps: int = ..., pl: int = ..., p: int = ..., pe: int = ..., pf: int = ..., pfe: int = ..., puv: int = ..., pv: int = ..., pvf: int = ..., rb: int = ..., rc: int = ..., rp: int = ..., sp: int = ..., sc: int = ..., sh: int = ..., spr: int = ..., spc: int = ..., str: int = ..., sd: int = ..., sme: int = ..., smf: int = ..., smp: int = ..., smu: int = ..., se: int = ..., sf: int = ..., sk: int = ..., spp: int = ..., sr: int = ..., tx: int = ..., v: int = ...) -> int:
    """selectPriority is undoable, queryable, and NOT editable.
    
    The selectPriority command is used to change the selection priority of
    particular types of objects that can be selected when using the select tool.
    It accepts no other arguments besides the flags. These flags are the same as
    used by the 'selectType' command.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.selectPriority( q=True, nurbsCurve=True )
        cmds.selectPriority( nurbsCurve=10 )
        cmds.selectPriority( handle=9, ikHandle=8 )
    ```

    ---
    - Args:
        - allComponents (alc): Set all component selection priority
        - allObjects (alo): Set all object selection priority
        - animBreakdown (abd): Set animation breakdown selection priority
        - animCurve (ac): Set animation curve selection priority
        - animInTangent (ait): Set animation in-tangent selection priority
        - animKeyframe (ak): Set animation keyframe selection priority
        - animOutTangent (aot): Set animation out-tangent selection priority
        - byName (bn): Set selection priority for the specified user-defined selection type
        - camera (ca): Set camera selection priority
        - cluster (cl): Set cluster selection priority
        - collisionModel (clm): Set collision model selection priority
        - controlVertex (cv): Set control vertex selection priority
        - curve (c): Set curve selection priority
        - curveKnot (ck): Set curve knot selection priority
        - curveOnSurface (cos): Set curve-on-surface selection priority
        - curveParameterPoint (cpp): Set curve parameter point selection priority
        - dimension (dim): Set dimension shape selection priority
        - dynamicConstraint (dc): Set dynamicConstraint selection priority
        - edge (eg): Set mesh edge selection priority
        - editPoint (ep): Set edit-point selection priority
        - emitter (em): Set emitter selection priority
        - facet (fc): Set mesh face selection priority
        - field (fi): Set field selection priority
        - fluid (fl): Set fluid selection priority
        - follicle (fo): Set follicle selection priority
        - hairSystem (hs): Set hairSystem selection priority
        - handle (ha): Set object handle selection priority
        - hull (hl): Set hull selection priority
        - ikEndEffector (iee): Set ik end effector selection priority
        - ikHandle (ikh): Set ik handle selection priority
        - imagePlane (ip): Set image plane selection mask priority
        - implicitGeometry (ig): Set implicit geometry selection priority
        - isoparm (iso): Set surface iso-parm selection priority
        - joint (j): Set ik handle selection priority
        - jointPivot (jp): Set joint pivot selection priority
        - lattice (la): Set lattice selection priority
        - latticePoint (lp): Set lattice point selection priority
        - light (lt): Set light selection priority
        - localRotationAxis (ra): Set local rotation axis selection priority
        - locator (lc): Set locator (all types) selection priority
        - locatorUV (luv): Set uv locator selection priority
        - locatorXYZ (xyz): Set xyz locator selection priority
        - meshUVShell (msh): Set uv shell component mask on/off.
        - motionTrailPoint (mtp): Set motion point selection priority
        - motionTrailTangent (mtt): Set motion point tangent priority
        - nCloth (ncl): Set nCloth selection priority
        - nParticle (npr): Set nParticle point selection priority
        - nParticleShape (nps): Set nParticle shape selection priority
        - nRigid (nr): Set nRigid selection priority
        - nonlinear (nl): Set nonlinear selection priority
        - nurbsCurve (nc): Set nurbs-curve selection priority
        - nurbsSurface (ns): Set nurbs-surface selection priority
        - orientationLocator (ol): Set orientation locator selection priority
        - particle (pr): Set particle point selection priority
        - particleShape (ps): Set particle shape selection priority
        - plane (pl): Set sketch plane selection priority
        - polymesh (p): Set poly-mesh selection priority
        - polymeshEdge (pe): Set poly-mesh edge selection priority
        - polymeshFace (pf): Set poly-mesh face selection priority
        - polymeshFreeEdge (pfe): Set poly-mesh free-edge selection priority
        - polymeshUV (puv): Set poly-mesh UV point selection priority
        - polymeshVertex (pv): Set poly-mesh vertex selection priority
        - polymeshVtxFace (pvf): Set poly-mesh vtxFace selection priority
        - rigidBody (rb): Set rigid body selection priority
        - rigidConstraint (rc): Set rigid constraint selection priority
        - rotatePivot (rp): Set rotate pivot selection priority
        - scalePivot (sp): Set scale pivot selection priority
        - sculpt (sc): Set sculpt selection priority
        - selectHandle (sh): Set select handle selection priority
        - spring (spr): Set spring shape selection priority
        - springComponent (spc): Set individual spring selection priority
        - stroke (str): Set stroke selection priority
        - subdiv (sd): Set subdivision surface selection priority
        - subdivMeshEdge (sme): Set subdivision surface mesh edge selection priority
        - subdivMeshFace (smf): Set subdivision surface mesh face selection priority
        - subdivMeshPoint (smp): Set subdivision surface mesh point selection priority
        - subdivMeshUV (smu): Set subdivision surface mesh UV map selection priority
        - surfaceEdge (se): Set surface edge selection priority
        - surfaceFace (sf): Set surface face selection priority
        - surfaceKnot (sk): Set surface knot selection priority
        - surfaceParameterPoint (spp): Set surface parameter point selection priority
        - surfaceRange (sr): Set surface range selection priority
        - texture (tx): Set texture selection priority
        - vertex (v): Set mesh vertex selection priority
    """
@overload #Overload for selectPriority in ['create']
def selectPriority(allComponents: int = ..., alc: int = ..., allObjects: int = ..., alo: int = ..., animBreakdown: int = ..., abd: int = ..., animCurve: int = ..., ac: int = ..., animInTangent: int = ..., ait: int = ..., animKeyframe: int = ..., ak: int = ..., animOutTangent: int = ..., aot: int = ..., byName: [string, boolean] = ..., bn: [string, boolean] = ..., camera: int = ..., ca: int = ..., cluster: int = ..., cl: int = ..., collisionModel: int = ..., clm: int = ..., controlVertex: int = ..., cv: int = ..., curve: int = ..., c: int = ..., curveKnot: int = ..., ck: int = ..., curveOnSurface: int = ..., cos: int = ..., curveParameterPoint: int = ..., cpp: int = ..., dimension: int = ..., dim: int = ..., dynamicConstraint: int = ..., dc: int = ..., edge: int = ..., eg: int = ..., editPoint: int = ..., ep: int = ..., emitter: int = ..., em: int = ..., facet: int = ..., fc: int = ..., field: int = ..., fi: int = ..., fluid: int = ..., fl: int = ..., follicle: int = ..., fo: int = ..., hairSystem: int = ..., hs: int = ..., handle: int = ..., ha: int = ..., hull: int = ..., hl: int = ..., ikEndEffector: int = ..., iee: int = ..., ikHandle: int = ..., ikh: int = ..., imagePlane: int = ..., ip: int = ..., implicitGeometry: int = ..., ig: int = ..., isoparm: int = ..., iso: int = ..., joint: int = ..., j: int = ..., jointPivot: int = ..., jp: int = ..., lattice: int = ..., la: int = ..., latticePoint: int = ..., lp: int = ..., light: int = ..., lt: int = ..., localRotationAxis: int = ..., ra: int = ..., locator: int = ..., lc: int = ..., locatorUV: int = ..., luv: int = ..., locatorXYZ: int = ..., xyz: int = ..., meshUVShell: int = ..., msh: int = ..., motionTrailPoint: int = ..., mtp: int = ..., motionTrailTangent: int = ..., mtt: int = ..., nCloth: int = ..., ncl: int = ..., nParticle: int = ..., npr: int = ..., nParticleShape: int = ..., nps: int = ..., nRigid: int = ..., nr: int = ..., nonlinear: int = ..., nl: int = ..., nurbsCurve: int = ..., nc: int = ..., nurbsSurface: int = ..., ns: int = ..., orientationLocator: int = ..., ol: int = ..., particle: int = ..., pr: int = ..., particleShape: int = ..., ps: int = ..., plane: int = ..., pl: int = ..., polymesh: int = ..., p: int = ..., polymeshEdge: int = ..., pe: int = ..., polymeshFace: int = ..., pf: int = ..., polymeshFreeEdge: int = ..., pfe: int = ..., polymeshUV: int = ..., puv: int = ..., polymeshVertex: int = ..., pv: int = ..., polymeshVtxFace: int = ..., pvf: int = ..., rigidBody: int = ..., rb: int = ..., rigidConstraint: int = ..., rc: int = ..., rotatePivot: int = ..., rp: int = ..., scalePivot: int = ..., sp: int = ..., sculpt: int = ..., sc: int = ..., selectHandle: int = ..., sh: int = ..., spring: int = ..., spr: int = ..., springComponent: int = ..., spc: int = ..., stroke: int = ..., str: int = ..., subdiv: int = ..., sd: int = ..., subdivMeshEdge: int = ..., sme: int = ..., subdivMeshFace: int = ..., smf: int = ..., subdivMeshPoint: int = ..., smp: int = ..., subdivMeshUV: int = ..., smu: int = ..., surfaceEdge: int = ..., se: int = ..., surfaceFace: int = ..., sf: int = ..., surfaceKnot: int = ..., sk: int = ..., surfaceParameterPoint: int = ..., spp: int = ..., surfaceRange: int = ..., sr: int = ..., texture: int = ..., tx: int = ..., vertex: int = ..., v: int = ...) -> int:
    """selectPriority is undoable, queryable, and NOT editable.
    
    The selectPriority command is used to change the selection priority of
    particular types of objects that can be selected when using the select tool.
    It accepts no other arguments besides the flags. These flags are the same as
    used by the 'selectType' command.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.selectPriority( q=True, nurbsCurve=True )
        cmds.selectPriority( nurbsCurve=10 )
        cmds.selectPriority( handle=9, ikHandle=8 )
    ```

    ---
    - Args:
        - allComponents (alc): Set all component selection priority
        - allObjects (alo): Set all object selection priority
        - animBreakdown (abd): Set animation breakdown selection priority
        - animCurve (ac): Set animation curve selection priority
        - animInTangent (ait): Set animation in-tangent selection priority
        - animKeyframe (ak): Set animation keyframe selection priority
        - animOutTangent (aot): Set animation out-tangent selection priority
        - byName (bn): Set selection priority for the specified user-defined selection type
        - camera (ca): Set camera selection priority
        - cluster (cl): Set cluster selection priority
        - collisionModel (clm): Set collision model selection priority
        - controlVertex (cv): Set control vertex selection priority
        - curve (c): Set curve selection priority
        - curveKnot (ck): Set curve knot selection priority
        - curveOnSurface (cos): Set curve-on-surface selection priority
        - curveParameterPoint (cpp): Set curve parameter point selection priority
        - dimension (dim): Set dimension shape selection priority
        - dynamicConstraint (dc): Set dynamicConstraint selection priority
        - edge (eg): Set mesh edge selection priority
        - editPoint (ep): Set edit-point selection priority
        - emitter (em): Set emitter selection priority
        - facet (fc): Set mesh face selection priority
        - field (fi): Set field selection priority
        - fluid (fl): Set fluid selection priority
        - follicle (fo): Set follicle selection priority
        - hairSystem (hs): Set hairSystem selection priority
        - handle (ha): Set object handle selection priority
        - hull (hl): Set hull selection priority
        - ikEndEffector (iee): Set ik end effector selection priority
        - ikHandle (ikh): Set ik handle selection priority
        - imagePlane (ip): Set image plane selection mask priority
        - implicitGeometry (ig): Set implicit geometry selection priority
        - isoparm (iso): Set surface iso-parm selection priority
        - joint (j): Set ik handle selection priority
        - jointPivot (jp): Set joint pivot selection priority
        - lattice (la): Set lattice selection priority
        - latticePoint (lp): Set lattice point selection priority
        - light (lt): Set light selection priority
        - localRotationAxis (ra): Set local rotation axis selection priority
        - locator (lc): Set locator (all types) selection priority
        - locatorUV (luv): Set uv locator selection priority
        - locatorXYZ (xyz): Set xyz locator selection priority
        - meshUVShell (msh): Set uv shell component mask on/off.
        - motionTrailPoint (mtp): Set motion point selection priority
        - motionTrailTangent (mtt): Set motion point tangent priority
        - nCloth (ncl): Set nCloth selection priority
        - nParticle (npr): Set nParticle point selection priority
        - nParticleShape (nps): Set nParticle shape selection priority
        - nRigid (nr): Set nRigid selection priority
        - nonlinear (nl): Set nonlinear selection priority
        - nurbsCurve (nc): Set nurbs-curve selection priority
        - nurbsSurface (ns): Set nurbs-surface selection priority
        - orientationLocator (ol): Set orientation locator selection priority
        - particle (pr): Set particle point selection priority
        - particleShape (ps): Set particle shape selection priority
        - plane (pl): Set sketch plane selection priority
        - polymesh (p): Set poly-mesh selection priority
        - polymeshEdge (pe): Set poly-mesh edge selection priority
        - polymeshFace (pf): Set poly-mesh face selection priority
        - polymeshFreeEdge (pfe): Set poly-mesh free-edge selection priority
        - polymeshUV (puv): Set poly-mesh UV point selection priority
        - polymeshVertex (pv): Set poly-mesh vertex selection priority
        - polymeshVtxFace (pvf): Set poly-mesh vtxFace selection priority
        - rigidBody (rb): Set rigid body selection priority
        - rigidConstraint (rc): Set rigid constraint selection priority
        - rotatePivot (rp): Set rotate pivot selection priority
        - scalePivot (sp): Set scale pivot selection priority
        - sculpt (sc): Set sculpt selection priority
        - selectHandle (sh): Set select handle selection priority
        - spring (spr): Set spring shape selection priority
        - springComponent (spc): Set individual spring selection priority
        - stroke (str): Set stroke selection priority
        - subdiv (sd): Set subdivision surface selection priority
        - subdivMeshEdge (sme): Set subdivision surface mesh edge selection priority
        - subdivMeshFace (smf): Set subdivision surface mesh face selection priority
        - subdivMeshPoint (smp): Set subdivision surface mesh point selection priority
        - subdivMeshUV (smu): Set subdivision surface mesh UV map selection priority
        - surfaceEdge (se): Set surface edge selection priority
        - surfaceFace (sf): Set surface face selection priority
        - surfaceKnot (sk): Set surface knot selection priority
        - surfaceParameterPoint (spp): Set surface parameter point selection priority
        - surfaceRange (sr): Set surface range selection priority
        - texture (tx): Set texture selection priority
        - vertex (v): Set mesh vertex selection priority
    """
@overload #Overload for selectPriority in ['query']
def selectPriority(allComponents: int = ..., allObjects: int = ..., animBreakdown: int = ..., animCurve: int = ..., animInTangent: int = ..., animKeyframe: int = ..., animOutTangent: int = ..., camera: int = ..., cluster: int = ..., collisionModel: int = ..., controlVertex: int = ..., curve: int = ..., curveKnot: int = ..., curveOnSurface: int = ..., curveParameterPoint: int = ..., dimension: int = ..., dynamicConstraint: int = ..., edge: int = ..., editPoint: int = ..., emitter: int = ..., facet: int = ..., field: int = ..., fluid: int = ..., follicle: int = ..., hairSystem: int = ..., handle: int = ..., hull: int = ..., ikEndEffector: int = ..., ikHandle: int = ..., imagePlane: int = ..., implicitGeometry: int = ..., isoparm: int = ..., joint: int = ..., jointPivot: int = ..., lattice: int = ..., latticePoint: int = ..., light: int = ..., localRotationAxis: int = ..., locator: int = ..., locatorUV: int = ..., locatorXYZ: int = ..., meshUVShell: int = ..., motionTrailPoint: int = ..., motionTrailTangent: int = ..., nCloth: int = ..., nParticle: int = ..., nParticleShape: int = ..., nRigid: int = ..., nonlinear: int = ..., nurbsCurve: int = ..., nurbsSurface: int = ..., orientationLocator: int = ..., particle: int = ..., particleShape: int = ..., plane: int = ..., polymesh: int = ..., polymeshEdge: int = ..., polymeshFace: int = ..., polymeshFreeEdge: int = ..., polymeshUV: int = ..., polymeshVertex: int = ..., polymeshVtxFace: int = ..., queryByName: str = ..., rigidBody: int = ..., rigidConstraint: int = ..., rotatePivot: int = ..., scalePivot: int = ..., sculpt: int = ..., selectHandle: int = ..., spring: int = ..., springComponent: int = ..., stroke: int = ..., subdiv: int = ..., subdivMeshEdge: int = ..., subdivMeshFace: int = ..., subdivMeshPoint: int = ..., subdivMeshUV: int = ..., surfaceEdge: int = ..., surfaceFace: int = ..., surfaceKnot: int = ..., surfaceParameterPoint: int = ..., surfaceRange: int = ..., texture: int = ..., vertex: int = ..., query: bool = ...) -> int:
    """selectPriority is undoable, queryable, and NOT editable.
    
    The selectPriority command is used to change the selection priority of
    particular types of objects that can be selected when using the select tool.
    It accepts no other arguments besides the flags. These flags are the same as
    used by the 'selectType' command.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.selectPriority( q=True, nurbsCurve=True )
        cmds.selectPriority( nurbsCurve=10 )
        cmds.selectPriority( handle=9, ikHandle=8 )
    ```

    ---
    - Args:
        - allComponents (alc): Set all component selection priority
        - allObjects (alo): Set all object selection priority
        - animBreakdown (abd): Set animation breakdown selection priority
        - animCurve (ac): Set animation curve selection priority
        - animInTangent (ait): Set animation in-tangent selection priority
        - animKeyframe (ak): Set animation keyframe selection priority
        - animOutTangent (aot): Set animation out-tangent selection priority
        - camera (ca): Set camera selection priority
        - cluster (cl): Set cluster selection priority
        - collisionModel (clm): Set collision model selection priority
        - controlVertex (cv): Set control vertex selection priority
        - curve (c): Set curve selection priority
        - curveKnot (ck): Set curve knot selection priority
        - curveOnSurface (cos): Set curve-on-surface selection priority
        - curveParameterPoint (cpp): Set curve parameter point selection priority
        - dimension (dim): Set dimension shape selection priority
        - dynamicConstraint (dc): Set dynamicConstraint selection priority
        - edge (eg): Set mesh edge selection priority
        - editPoint (ep): Set edit-point selection priority
        - emitter (em): Set emitter selection priority
        - facet (fc): Set mesh face selection priority
        - field (fi): Set field selection priority
        - fluid (fl): Set fluid selection priority
        - follicle (fo): Set follicle selection priority
        - hairSystem (hs): Set hairSystem selection priority
        - handle (ha): Set object handle selection priority
        - hull (hl): Set hull selection priority
        - ikEndEffector (iee): Set ik end effector selection priority
        - ikHandle (ikh): Set ik handle selection priority
        - imagePlane (ip): Set image plane selection mask priority
        - implicitGeometry (ig): Set implicit geometry selection priority
        - isoparm (iso): Set surface iso-parm selection priority
        - joint (j): Set ik handle selection priority
        - jointPivot (jp): Set joint pivot selection priority
        - lattice (la): Set lattice selection priority
        - latticePoint (lp): Set lattice point selection priority
        - light (lt): Set light selection priority
        - localRotationAxis (ra): Set local rotation axis selection priority
        - locator (lc): Set locator (all types) selection priority
        - locatorUV (luv): Set uv locator selection priority
        - locatorXYZ (xyz): Set xyz locator selection priority
        - meshUVShell (msh): Set uv shell component mask on/off.
        - motionTrailPoint (mtp): Set motion point selection priority
        - motionTrailTangent (mtt): Set motion point tangent priority
        - nCloth (ncl): Set nCloth selection priority
        - nParticle (npr): Set nParticle point selection priority
        - nParticleShape (nps): Set nParticle shape selection priority
        - nRigid (nr): Set nRigid selection priority
        - nonlinear (nl): Set nonlinear selection priority
        - nurbsCurve (nc): Set nurbs-curve selection priority
        - nurbsSurface (ns): Set nurbs-surface selection priority
        - orientationLocator (ol): Set orientation locator selection priority
        - particle (pr): Set particle point selection priority
        - particleShape (ps): Set particle shape selection priority
        - plane (pl): Set sketch plane selection priority
        - polymesh (p): Set poly-mesh selection priority
        - polymeshEdge (pe): Set poly-mesh edge selection priority
        - polymeshFace (pf): Set poly-mesh face selection priority
        - polymeshFreeEdge (pfe): Set poly-mesh free-edge selection priority
        - polymeshUV (puv): Set poly-mesh UV point selection priority
        - polymeshVertex (pv): Set poly-mesh vertex selection priority
        - polymeshVtxFace (pvf): Set poly-mesh vtxFace selection priority
        - queryByName (qbn): Query selection priority for the specified user-defined selection typeIn query mode, this flag needs a value.
        - rigidBody (rb): Set rigid body selection priority
        - rigidConstraint (rc): Set rigid constraint selection priority
        - rotatePivot (rp): Set rotate pivot selection priority
        - scalePivot (sp): Set scale pivot selection priority
        - sculpt (sc): Set sculpt selection priority
        - selectHandle (sh): Set select handle selection priority
        - spring (spr): Set spring shape selection priority
        - springComponent (spc): Set individual spring selection priority
        - stroke (str): Set stroke selection priority
        - subdiv (sd): Set subdivision surface selection priority
        - subdivMeshEdge (sme): Set subdivision surface mesh edge selection priority
        - subdivMeshFace (smf): Set subdivision surface mesh face selection priority
        - subdivMeshPoint (smp): Set subdivision surface mesh point selection priority
        - subdivMeshUV (smu): Set subdivision surface mesh UV map selection priority
        - surfaceEdge (se): Set surface edge selection priority
        - surfaceFace (sf): Set surface face selection priority
        - surfaceKnot (sk): Set surface knot selection priority
        - surfaceParameterPoint (spp): Set surface parameter point selection priority
        - surfaceRange (sr): Set surface range selection priority
        - texture (tx): Set texture selection priority
        - vertex (v): Set mesh vertex selection priority
        - query (q): Query mode flag
    """
@overload #Overload for selectPriority in ['query']
def selectPriority(alc: int = ..., alo: int = ..., abd: int = ..., ac: int = ..., ait: int = ..., ak: int = ..., aot: int = ..., ca: int = ..., cl: int = ..., clm: int = ..., cv: int = ..., c: int = ..., ck: int = ..., cos: int = ..., cpp: int = ..., dim: int = ..., dc: int = ..., eg: int = ..., ep: int = ..., em: int = ..., fc: int = ..., fi: int = ..., fl: int = ..., fo: int = ..., hs: int = ..., ha: int = ..., hl: int = ..., iee: int = ..., ikh: int = ..., ip: int = ..., ig: int = ..., iso: int = ..., j: int = ..., jp: int = ..., la: int = ..., lp: int = ..., lt: int = ..., ra: int = ..., lc: int = ..., luv: int = ..., xyz: int = ..., msh: int = ..., mtp: int = ..., mtt: int = ..., ncl: int = ..., npr: int = ..., nps: int = ..., nr: int = ..., nl: int = ..., nc: int = ..., ns: int = ..., ol: int = ..., pr: int = ..., ps: int = ..., pl: int = ..., p: int = ..., pe: int = ..., pf: int = ..., pfe: int = ..., puv: int = ..., pv: int = ..., pvf: int = ..., qbn: str = ..., rb: int = ..., rc: int = ..., rp: int = ..., sp: int = ..., sc: int = ..., sh: int = ..., spr: int = ..., spc: int = ..., str: int = ..., sd: int = ..., sme: int = ..., smf: int = ..., smp: int = ..., smu: int = ..., se: int = ..., sf: int = ..., sk: int = ..., spp: int = ..., sr: int = ..., tx: int = ..., v: int = ..., q: bool = ...) -> int:
    """selectPriority is undoable, queryable, and NOT editable.
    
    The selectPriority command is used to change the selection priority of
    particular types of objects that can be selected when using the select tool.
    It accepts no other arguments besides the flags. These flags are the same as
    used by the 'selectType' command.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.selectPriority( q=True, nurbsCurve=True )
        cmds.selectPriority( nurbsCurve=10 )
        cmds.selectPriority( handle=9, ikHandle=8 )
    ```

    ---
    - Args:
        - allComponents (alc): Set all component selection priority
        - allObjects (alo): Set all object selection priority
        - animBreakdown (abd): Set animation breakdown selection priority
        - animCurve (ac): Set animation curve selection priority
        - animInTangent (ait): Set animation in-tangent selection priority
        - animKeyframe (ak): Set animation keyframe selection priority
        - animOutTangent (aot): Set animation out-tangent selection priority
        - camera (ca): Set camera selection priority
        - cluster (cl): Set cluster selection priority
        - collisionModel (clm): Set collision model selection priority
        - controlVertex (cv): Set control vertex selection priority
        - curve (c): Set curve selection priority
        - curveKnot (ck): Set curve knot selection priority
        - curveOnSurface (cos): Set curve-on-surface selection priority
        - curveParameterPoint (cpp): Set curve parameter point selection priority
        - dimension (dim): Set dimension shape selection priority
        - dynamicConstraint (dc): Set dynamicConstraint selection priority
        - edge (eg): Set mesh edge selection priority
        - editPoint (ep): Set edit-point selection priority
        - emitter (em): Set emitter selection priority
        - facet (fc): Set mesh face selection priority
        - field (fi): Set field selection priority
        - fluid (fl): Set fluid selection priority
        - follicle (fo): Set follicle selection priority
        - hairSystem (hs): Set hairSystem selection priority
        - handle (ha): Set object handle selection priority
        - hull (hl): Set hull selection priority
        - ikEndEffector (iee): Set ik end effector selection priority
        - ikHandle (ikh): Set ik handle selection priority
        - imagePlane (ip): Set image plane selection mask priority
        - implicitGeometry (ig): Set implicit geometry selection priority
        - isoparm (iso): Set surface iso-parm selection priority
        - joint (j): Set ik handle selection priority
        - jointPivot (jp): Set joint pivot selection priority
        - lattice (la): Set lattice selection priority
        - latticePoint (lp): Set lattice point selection priority
        - light (lt): Set light selection priority
        - localRotationAxis (ra): Set local rotation axis selection priority
        - locator (lc): Set locator (all types) selection priority
        - locatorUV (luv): Set uv locator selection priority
        - locatorXYZ (xyz): Set xyz locator selection priority
        - meshUVShell (msh): Set uv shell component mask on/off.
        - motionTrailPoint (mtp): Set motion point selection priority
        - motionTrailTangent (mtt): Set motion point tangent priority
        - nCloth (ncl): Set nCloth selection priority
        - nParticle (npr): Set nParticle point selection priority
        - nParticleShape (nps): Set nParticle shape selection priority
        - nRigid (nr): Set nRigid selection priority
        - nonlinear (nl): Set nonlinear selection priority
        - nurbsCurve (nc): Set nurbs-curve selection priority
        - nurbsSurface (ns): Set nurbs-surface selection priority
        - orientationLocator (ol): Set orientation locator selection priority
        - particle (pr): Set particle point selection priority
        - particleShape (ps): Set particle shape selection priority
        - plane (pl): Set sketch plane selection priority
        - polymesh (p): Set poly-mesh selection priority
        - polymeshEdge (pe): Set poly-mesh edge selection priority
        - polymeshFace (pf): Set poly-mesh face selection priority
        - polymeshFreeEdge (pfe): Set poly-mesh free-edge selection priority
        - polymeshUV (puv): Set poly-mesh UV point selection priority
        - polymeshVertex (pv): Set poly-mesh vertex selection priority
        - polymeshVtxFace (pvf): Set poly-mesh vtxFace selection priority
        - queryByName (qbn): Query selection priority for the specified user-defined selection typeIn query mode, this flag needs a value.
        - rigidBody (rb): Set rigid body selection priority
        - rigidConstraint (rc): Set rigid constraint selection priority
        - rotatePivot (rp): Set rotate pivot selection priority
        - scalePivot (sp): Set scale pivot selection priority
        - sculpt (sc): Set sculpt selection priority
        - selectHandle (sh): Set select handle selection priority
        - spring (spr): Set spring shape selection priority
        - springComponent (spc): Set individual spring selection priority
        - stroke (str): Set stroke selection priority
        - subdiv (sd): Set subdivision surface selection priority
        - subdivMeshEdge (sme): Set subdivision surface mesh edge selection priority
        - subdivMeshFace (smf): Set subdivision surface mesh face selection priority
        - subdivMeshPoint (smp): Set subdivision surface mesh point selection priority
        - subdivMeshUV (smu): Set subdivision surface mesh UV map selection priority
        - surfaceEdge (se): Set surface edge selection priority
        - surfaceFace (sf): Set surface face selection priority
        - surfaceKnot (sk): Set surface knot selection priority
        - surfaceParameterPoint (spp): Set surface parameter point selection priority
        - surfaceRange (sr): Set surface range selection priority
        - texture (tx): Set texture selection priority
        - vertex (v): Set mesh vertex selection priority
        - query (q): Query mode flag
    """
@overload #Overload for selectPriority in ['query']
def selectPriority(allComponents: int = ..., alc: int = ..., allObjects: int = ..., alo: int = ..., animBreakdown: int = ..., abd: int = ..., animCurve: int = ..., ac: int = ..., animInTangent: int = ..., ait: int = ..., animKeyframe: int = ..., ak: int = ..., animOutTangent: int = ..., aot: int = ..., camera: int = ..., ca: int = ..., cluster: int = ..., cl: int = ..., collisionModel: int = ..., clm: int = ..., controlVertex: int = ..., cv: int = ..., curve: int = ..., c: int = ..., curveKnot: int = ..., ck: int = ..., curveOnSurface: int = ..., cos: int = ..., curveParameterPoint: int = ..., cpp: int = ..., dimension: int = ..., dim: int = ..., dynamicConstraint: int = ..., dc: int = ..., edge: int = ..., eg: int = ..., editPoint: int = ..., ep: int = ..., emitter: int = ..., em: int = ..., facet: int = ..., fc: int = ..., field: int = ..., fi: int = ..., fluid: int = ..., fl: int = ..., follicle: int = ..., fo: int = ..., hairSystem: int = ..., hs: int = ..., handle: int = ..., ha: int = ..., hull: int = ..., hl: int = ..., ikEndEffector: int = ..., iee: int = ..., ikHandle: int = ..., ikh: int = ..., imagePlane: int = ..., ip: int = ..., implicitGeometry: int = ..., ig: int = ..., isoparm: int = ..., iso: int = ..., joint: int = ..., j: int = ..., jointPivot: int = ..., jp: int = ..., lattice: int = ..., la: int = ..., latticePoint: int = ..., lp: int = ..., light: int = ..., lt: int = ..., localRotationAxis: int = ..., ra: int = ..., locator: int = ..., lc: int = ..., locatorUV: int = ..., luv: int = ..., locatorXYZ: int = ..., xyz: int = ..., meshUVShell: int = ..., msh: int = ..., motionTrailPoint: int = ..., mtp: int = ..., motionTrailTangent: int = ..., mtt: int = ..., nCloth: int = ..., ncl: int = ..., nParticle: int = ..., npr: int = ..., nParticleShape: int = ..., nps: int = ..., nRigid: int = ..., nr: int = ..., nonlinear: int = ..., nl: int = ..., nurbsCurve: int = ..., nc: int = ..., nurbsSurface: int = ..., ns: int = ..., orientationLocator: int = ..., ol: int = ..., particle: int = ..., pr: int = ..., particleShape: int = ..., ps: int = ..., plane: int = ..., pl: int = ..., polymesh: int = ..., p: int = ..., polymeshEdge: int = ..., pe: int = ..., polymeshFace: int = ..., pf: int = ..., polymeshFreeEdge: int = ..., pfe: int = ..., polymeshUV: int = ..., puv: int = ..., polymeshVertex: int = ..., pv: int = ..., polymeshVtxFace: int = ..., pvf: int = ..., queryByName: str = ..., qbn: str = ..., rigidBody: int = ..., rb: int = ..., rigidConstraint: int = ..., rc: int = ..., rotatePivot: int = ..., rp: int = ..., scalePivot: int = ..., sp: int = ..., sculpt: int = ..., sc: int = ..., selectHandle: int = ..., sh: int = ..., spring: int = ..., spr: int = ..., springComponent: int = ..., spc: int = ..., stroke: int = ..., str: int = ..., subdiv: int = ..., sd: int = ..., subdivMeshEdge: int = ..., sme: int = ..., subdivMeshFace: int = ..., smf: int = ..., subdivMeshPoint: int = ..., smp: int = ..., subdivMeshUV: int = ..., smu: int = ..., surfaceEdge: int = ..., se: int = ..., surfaceFace: int = ..., sf: int = ..., surfaceKnot: int = ..., sk: int = ..., surfaceParameterPoint: int = ..., spp: int = ..., surfaceRange: int = ..., sr: int = ..., texture: int = ..., tx: int = ..., vertex: int = ..., v: int = ..., query: bool = ..., q: bool = ...) -> int:
    """selectPriority is undoable, queryable, and NOT editable.
    
    The selectPriority command is used to change the selection priority of
    particular types of objects that can be selected when using the select tool.
    It accepts no other arguments besides the flags. These flags are the same as
    used by the 'selectType' command.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.selectPriority( q=True, nurbsCurve=True )
        cmds.selectPriority( nurbsCurve=10 )
        cmds.selectPriority( handle=9, ikHandle=8 )
    ```

    ---
    - Args:
        - allComponents (alc): Set all component selection priority
        - allObjects (alo): Set all object selection priority
        - animBreakdown (abd): Set animation breakdown selection priority
        - animCurve (ac): Set animation curve selection priority
        - animInTangent (ait): Set animation in-tangent selection priority
        - animKeyframe (ak): Set animation keyframe selection priority
        - animOutTangent (aot): Set animation out-tangent selection priority
        - camera (ca): Set camera selection priority
        - cluster (cl): Set cluster selection priority
        - collisionModel (clm): Set collision model selection priority
        - controlVertex (cv): Set control vertex selection priority
        - curve (c): Set curve selection priority
        - curveKnot (ck): Set curve knot selection priority
        - curveOnSurface (cos): Set curve-on-surface selection priority
        - curveParameterPoint (cpp): Set curve parameter point selection priority
        - dimension (dim): Set dimension shape selection priority
        - dynamicConstraint (dc): Set dynamicConstraint selection priority
        - edge (eg): Set mesh edge selection priority
        - editPoint (ep): Set edit-point selection priority
        - emitter (em): Set emitter selection priority
        - facet (fc): Set mesh face selection priority
        - field (fi): Set field selection priority
        - fluid (fl): Set fluid selection priority
        - follicle (fo): Set follicle selection priority
        - hairSystem (hs): Set hairSystem selection priority
        - handle (ha): Set object handle selection priority
        - hull (hl): Set hull selection priority
        - ikEndEffector (iee): Set ik end effector selection priority
        - ikHandle (ikh): Set ik handle selection priority
        - imagePlane (ip): Set image plane selection mask priority
        - implicitGeometry (ig): Set implicit geometry selection priority
        - isoparm (iso): Set surface iso-parm selection priority
        - joint (j): Set ik handle selection priority
        - jointPivot (jp): Set joint pivot selection priority
        - lattice (la): Set lattice selection priority
        - latticePoint (lp): Set lattice point selection priority
        - light (lt): Set light selection priority
        - localRotationAxis (ra): Set local rotation axis selection priority
        - locator (lc): Set locator (all types) selection priority
        - locatorUV (luv): Set uv locator selection priority
        - locatorXYZ (xyz): Set xyz locator selection priority
        - meshUVShell (msh): Set uv shell component mask on/off.
        - motionTrailPoint (mtp): Set motion point selection priority
        - motionTrailTangent (mtt): Set motion point tangent priority
        - nCloth (ncl): Set nCloth selection priority
        - nParticle (npr): Set nParticle point selection priority
        - nParticleShape (nps): Set nParticle shape selection priority
        - nRigid (nr): Set nRigid selection priority
        - nonlinear (nl): Set nonlinear selection priority
        - nurbsCurve (nc): Set nurbs-curve selection priority
        - nurbsSurface (ns): Set nurbs-surface selection priority
        - orientationLocator (ol): Set orientation locator selection priority
        - particle (pr): Set particle point selection priority
        - particleShape (ps): Set particle shape selection priority
        - plane (pl): Set sketch plane selection priority
        - polymesh (p): Set poly-mesh selection priority
        - polymeshEdge (pe): Set poly-mesh edge selection priority
        - polymeshFace (pf): Set poly-mesh face selection priority
        - polymeshFreeEdge (pfe): Set poly-mesh free-edge selection priority
        - polymeshUV (puv): Set poly-mesh UV point selection priority
        - polymeshVertex (pv): Set poly-mesh vertex selection priority
        - polymeshVtxFace (pvf): Set poly-mesh vtxFace selection priority
        - queryByName (qbn): Query selection priority for the specified user-defined selection typeIn query mode, this flag needs a value.
        - rigidBody (rb): Set rigid body selection priority
        - rigidConstraint (rc): Set rigid constraint selection priority
        - rotatePivot (rp): Set rotate pivot selection priority
        - scalePivot (sp): Set scale pivot selection priority
        - sculpt (sc): Set sculpt selection priority
        - selectHandle (sh): Set select handle selection priority
        - spring (spr): Set spring shape selection priority
        - springComponent (spc): Set individual spring selection priority
        - stroke (str): Set stroke selection priority
        - subdiv (sd): Set subdivision surface selection priority
        - subdivMeshEdge (sme): Set subdivision surface mesh edge selection priority
        - subdivMeshFace (smf): Set subdivision surface mesh face selection priority
        - subdivMeshPoint (smp): Set subdivision surface mesh point selection priority
        - subdivMeshUV (smu): Set subdivision surface mesh UV map selection priority
        - surfaceEdge (se): Set surface edge selection priority
        - surfaceFace (sf): Set surface face selection priority
        - surfaceKnot (sk): Set surface knot selection priority
        - surfaceParameterPoint (spp): Set surface parameter point selection priority
        - surfaceRange (sr): Set surface range selection priority
        - texture (tx): Set texture selection priority
        - vertex (v): Set mesh vertex selection priority
        - query (q): Query mode flag
    """
