"""Stub files for Selection category in Maya commands, command: selectType."""

from typing import Any, overload

@overload #Overload for selectType in ['create']
def selectType(allComponents: bool = ..., allObjects: bool = ..., animBreakdown: bool = ..., animCurve: bool = ..., animInTangent: bool = ..., animKeyframe: bool = ..., animOutTangent: bool = ..., byName: [string, boolean] = ..., camera: bool = ..., cluster: bool = ..., collisionModel: bool = ..., controlVertex: bool = ..., curve: bool = ..., curveKnot: bool = ..., curveOnSurface: bool = ..., curveParameterPoint: bool = ..., dimension: bool = ..., dynamicConstraint: bool = ..., edge: bool = ..., editPoint: bool = ..., emitter: bool = ..., facet: bool = ..., field: bool = ..., fluid: bool = ..., follicle: bool = ..., hairSystem: bool = ..., handle: bool = ..., hull: bool = ..., ikEndEffector: bool = ..., ikHandle: bool = ..., imagePlane: bool = ..., implicitGeometry: bool = ..., isoparm: bool = ..., joint: bool = ..., jointPivot: bool = ..., lattice: bool = ..., latticePoint: bool = ..., light: bool = ..., localRotationAxis: bool = ..., locator: bool = ..., locatorUV: bool = ..., locatorXYZ: bool = ..., meshUVShell: bool = ..., motionTrailPoint: bool = ..., motionTrailTangent: bool = ..., nCloth: bool = ..., nParticle: bool = ..., nParticleShape: bool = ..., nRigid: bool = ..., nonlinear: bool = ..., nurbsCurve: bool = ..., nurbsSurface: bool = ..., objectComponent: bool = ..., orientationLocator: bool = ..., particle: bool = ..., particleShape: bool = ..., plane: bool = ..., polymesh: bool = ..., polymeshEdge: bool = ..., polymeshFace: bool = ..., polymeshFreeEdge: bool = ..., polymeshUV: bool = ..., polymeshVertex: bool = ..., polymeshVtxFace: bool = ..., rigidBody: bool = ..., rigidConstraint: bool = ..., rotatePivot: bool = ..., scalePivot: bool = ..., sculpt: bool = ..., selectHandle: bool = ..., spring: bool = ..., springComponent: bool = ..., stroke: bool = ..., subdiv: bool = ..., subdivMeshEdge: bool = ..., subdivMeshFace: bool = ..., subdivMeshPoint: bool = ..., subdivMeshUV: bool = ..., surfaceEdge: bool = ..., surfaceFace: bool = ..., surfaceKnot: bool = ..., surfaceParameterPoint: bool = ..., surfaceRange: bool = ..., surfaceUV: bool = ..., texture: bool = ..., vertex: bool = ...) -> bool:
    """selectType is undoable, queryable, and NOT editable.
    
    The selectType command is used to change the set of allowable types of objects
    that can be selected when using the select tool. It accepts no other arguments
    besides the flags.
    
    There are basically two different types of items that are selectable when
    interactively selecting objects in the 3D views. They are classified as
    objects (entire objects) or components (parts of objects). The object and
    component command flags control which class of objects are selectable.
    
    It is possible to select components while in the object selection mode. To set
    the components which are selectable in object selection mode you must use the
    -ocm flag when specifying the component flags.

    ---
    - Args:
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - byName (bn): Set the specified user-defined selection mask on/off. (object flag)
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
        - meshUVShell (msh): Set uv shell component mask on/off.
        - motionTrailPoint (mtp): Set motion point selection mask on/off.
        - motionTrailTangent (mtt): Set motion point tangent mask on/off.
        - nCloth (ncl): Set nCloth selection mask on/off. (object flag)
        - nParticle (npr): Set nParticle point selection mask on/off. (component flag)
        - nParticleShape (nps): Set nParticle shape selection mask on/off. (object flag)
        - nRigid (nr): Set nRigid selection mask on/off. (object flag)
        - nonlinear (nl): Set nonlinear selection mask on/off. (object flag)
        - nurbsCurve (nc): Set nurbs-curve selection mask on/off. (object flag)
        - nurbsSurface (ns): Set nurbs-surface selection mask on/off. (object flag)
        - objectComponent (ocm): Component flags apply to object mode.
        - orientationLocator (ol): Set orientation locator selection mask on/off. (object flag)
        - particle (pr): Set particle point selection mask on/off. (component flag)
        - particleShape (ps): Set particle shape selection mask on/off. (object flag)
        - plane (pl): Set sketch plane selection mask on/off. (object flag)
        - polymesh (p): Set poly-mesh selection mask on/off. (object flag)
        - polymeshEdge (pe): Set poly-mesh edge selection mask on/off. (component flag)
        - polymeshFace (pf): Set poly-mesh face selection mask on/off. (component flag)
        - polymeshFreeEdge (pfe): Set poly-mesh free-edge selection mask on/off. (component flag)
        - polymeshUV (puv): Set poly-mesh UV point selection mask on/off. (component flag)
        - polymeshVertex (pv): Set poly-mesh vertex selection mask on/off. (component flag)
        - polymeshVtxFace (pvf): Set poly-mesh vertexFace selection mask on/off. (component flag)
        - rigidBody (rb): Set rigid body selection mask on/off. (object flag)
        - rigidConstraint (rc): Set rigid constraint selection mask on/off. (object flag)
        - rotatePivot (rp): Set rotate pivot selection mask on/off. (component flag)
        - scalePivot (sp): Set scale pivot selection mask on/off. (component flag)
        - sculpt (sc): Set sculpt selection mask on/off. (object flag)
        - selectHandle (sh): Set select handle selection mask on/off. (component flag)
        - spring (spr): Set spring shape selection mask on/off. (object flag)
        - springComponent (spc): Set individual spring selection mask on/off. (component flag)
        - stroke (str): Set the Paint Effects stroke selection mask on/off. (object flag)
        - subdiv (sd): Set subdivision surfaces selection mask on/off. (object flag)
        - subdivMeshEdge (sme): Set subdivision surfaces mesh edge selection mask on/off. (component flag)
        - subdivMeshFace (smf): Set subdivision surfaces mesh face selection mask on/off. (component flag)
        - subdivMeshPoint (smp): Set subdivision surfaces mesh point selection mask on/off. (component flag)
        - subdivMeshUV (smu): Set subdivision surfaces mesh UV map selection mask on/off. (component flag)
        - surfaceEdge (se): Set surface edge selection mask on/off. (component flag)
        - surfaceFace (sf): Set surface face selection mask on/off. (component flag)
        - surfaceKnot (sk): Set surface knot selection mask on/off. (component flag)
        - surfaceParameterPoint (spp): Set surface parameter point selection mask on/off. (component flag)
        - surfaceRange (sr): Set surface range selection mask on/off. (component flag)
        - surfaceUV (suv): Set surface uv selection mask on/off. (component flag)
        - texture (tx): Set texture selection mask on/off. (object flag)
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
    """
@overload #Overload for selectType in ['create']
def selectType(alc: bool = ..., alo: bool = ..., abd: bool = ..., ac: bool = ..., ait: bool = ..., ak: bool = ..., aot: bool = ..., bn: [string, boolean] = ..., ca: bool = ..., cl: bool = ..., clm: bool = ..., cv: bool = ..., c: bool = ..., ck: bool = ..., cos: bool = ..., cpp: bool = ..., dim: bool = ..., dc: bool = ..., eg: bool = ..., ep: bool = ..., em: bool = ..., fc: bool = ..., fi: bool = ..., fl: bool = ..., fo: bool = ..., hs: bool = ..., ha: bool = ..., hl: bool = ..., iee: bool = ..., ikh: bool = ..., ip: bool = ..., ig: bool = ..., iso: bool = ..., j: bool = ..., jp: bool = ..., la: bool = ..., lp: bool = ..., lt: bool = ..., ra: bool = ..., lc: bool = ..., luv: bool = ..., xyz: bool = ..., msh: bool = ..., mtp: bool = ..., mtt: bool = ..., ncl: bool = ..., npr: bool = ..., nps: bool = ..., nr: bool = ..., nl: bool = ..., nc: bool = ..., ns: bool = ..., ocm: bool = ..., ol: bool = ..., pr: bool = ..., ps: bool = ..., pl: bool = ..., p: bool = ..., pe: bool = ..., pf: bool = ..., pfe: bool = ..., puv: bool = ..., pv: bool = ..., pvf: bool = ..., rb: bool = ..., rc: bool = ..., rp: bool = ..., sp: bool = ..., sc: bool = ..., sh: bool = ..., spr: bool = ..., spc: bool = ..., str: bool = ..., sd: bool = ..., sme: bool = ..., smf: bool = ..., smp: bool = ..., smu: bool = ..., se: bool = ..., sf: bool = ..., sk: bool = ..., spp: bool = ..., sr: bool = ..., suv: bool = ..., tx: bool = ..., v: bool = ...) -> bool:
    """selectType is undoable, queryable, and NOT editable.
    
    The selectType command is used to change the set of allowable types of objects
    that can be selected when using the select tool. It accepts no other arguments
    besides the flags.
    
    There are basically two different types of items that are selectable when
    interactively selecting objects in the 3D views. They are classified as
    objects (entire objects) or components (parts of objects). The object and
    component command flags control which class of objects are selectable.
    
    It is possible to select components while in the object selection mode. To set
    the components which are selectable in object selection mode you must use the
    -ocm flag when specifying the component flags.

    ---
    - Args:
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - byName (bn): Set the specified user-defined selection mask on/off. (object flag)
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
        - meshUVShell (msh): Set uv shell component mask on/off.
        - motionTrailPoint (mtp): Set motion point selection mask on/off.
        - motionTrailTangent (mtt): Set motion point tangent mask on/off.
        - nCloth (ncl): Set nCloth selection mask on/off. (object flag)
        - nParticle (npr): Set nParticle point selection mask on/off. (component flag)
        - nParticleShape (nps): Set nParticle shape selection mask on/off. (object flag)
        - nRigid (nr): Set nRigid selection mask on/off. (object flag)
        - nonlinear (nl): Set nonlinear selection mask on/off. (object flag)
        - nurbsCurve (nc): Set nurbs-curve selection mask on/off. (object flag)
        - nurbsSurface (ns): Set nurbs-surface selection mask on/off. (object flag)
        - objectComponent (ocm): Component flags apply to object mode.
        - orientationLocator (ol): Set orientation locator selection mask on/off. (object flag)
        - particle (pr): Set particle point selection mask on/off. (component flag)
        - particleShape (ps): Set particle shape selection mask on/off. (object flag)
        - plane (pl): Set sketch plane selection mask on/off. (object flag)
        - polymesh (p): Set poly-mesh selection mask on/off. (object flag)
        - polymeshEdge (pe): Set poly-mesh edge selection mask on/off. (component flag)
        - polymeshFace (pf): Set poly-mesh face selection mask on/off. (component flag)
        - polymeshFreeEdge (pfe): Set poly-mesh free-edge selection mask on/off. (component flag)
        - polymeshUV (puv): Set poly-mesh UV point selection mask on/off. (component flag)
        - polymeshVertex (pv): Set poly-mesh vertex selection mask on/off. (component flag)
        - polymeshVtxFace (pvf): Set poly-mesh vertexFace selection mask on/off. (component flag)
        - rigidBody (rb): Set rigid body selection mask on/off. (object flag)
        - rigidConstraint (rc): Set rigid constraint selection mask on/off. (object flag)
        - rotatePivot (rp): Set rotate pivot selection mask on/off. (component flag)
        - scalePivot (sp): Set scale pivot selection mask on/off. (component flag)
        - sculpt (sc): Set sculpt selection mask on/off. (object flag)
        - selectHandle (sh): Set select handle selection mask on/off. (component flag)
        - spring (spr): Set spring shape selection mask on/off. (object flag)
        - springComponent (spc): Set individual spring selection mask on/off. (component flag)
        - stroke (str): Set the Paint Effects stroke selection mask on/off. (object flag)
        - subdiv (sd): Set subdivision surfaces selection mask on/off. (object flag)
        - subdivMeshEdge (sme): Set subdivision surfaces mesh edge selection mask on/off. (component flag)
        - subdivMeshFace (smf): Set subdivision surfaces mesh face selection mask on/off. (component flag)
        - subdivMeshPoint (smp): Set subdivision surfaces mesh point selection mask on/off. (component flag)
        - subdivMeshUV (smu): Set subdivision surfaces mesh UV map selection mask on/off. (component flag)
        - surfaceEdge (se): Set surface edge selection mask on/off. (component flag)
        - surfaceFace (sf): Set surface face selection mask on/off. (component flag)
        - surfaceKnot (sk): Set surface knot selection mask on/off. (component flag)
        - surfaceParameterPoint (spp): Set surface parameter point selection mask on/off. (component flag)
        - surfaceRange (sr): Set surface range selection mask on/off. (component flag)
        - surfaceUV (suv): Set surface uv selection mask on/off. (component flag)
        - texture (tx): Set texture selection mask on/off. (object flag)
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
    """
@overload #Overload for selectType in ['create']
def selectType(allComponents: bool = ..., alc: bool = ..., allObjects: bool = ..., alo: bool = ..., animBreakdown: bool = ..., abd: bool = ..., animCurve: bool = ..., ac: bool = ..., animInTangent: bool = ..., ait: bool = ..., animKeyframe: bool = ..., ak: bool = ..., animOutTangent: bool = ..., aot: bool = ..., byName: [string, boolean] = ..., bn: [string, boolean] = ..., camera: bool = ..., ca: bool = ..., cluster: bool = ..., cl: bool = ..., collisionModel: bool = ..., clm: bool = ..., controlVertex: bool = ..., cv: bool = ..., curve: bool = ..., c: bool = ..., curveKnot: bool = ..., ck: bool = ..., curveOnSurface: bool = ..., cos: bool = ..., curveParameterPoint: bool = ..., cpp: bool = ..., dimension: bool = ..., dim: bool = ..., dynamicConstraint: bool = ..., dc: bool = ..., edge: bool = ..., eg: bool = ..., editPoint: bool = ..., ep: bool = ..., emitter: bool = ..., em: bool = ..., facet: bool = ..., fc: bool = ..., field: bool = ..., fi: bool = ..., fluid: bool = ..., fl: bool = ..., follicle: bool = ..., fo: bool = ..., hairSystem: bool = ..., hs: bool = ..., handle: bool = ..., ha: bool = ..., hull: bool = ..., hl: bool = ..., ikEndEffector: bool = ..., iee: bool = ..., ikHandle: bool = ..., ikh: bool = ..., imagePlane: bool = ..., ip: bool = ..., implicitGeometry: bool = ..., ig: bool = ..., isoparm: bool = ..., iso: bool = ..., joint: bool = ..., j: bool = ..., jointPivot: bool = ..., jp: bool = ..., lattice: bool = ..., la: bool = ..., latticePoint: bool = ..., lp: bool = ..., light: bool = ..., lt: bool = ..., localRotationAxis: bool = ..., ra: bool = ..., locator: bool = ..., lc: bool = ..., locatorUV: bool = ..., luv: bool = ..., locatorXYZ: bool = ..., xyz: bool = ..., meshUVShell: bool = ..., msh: bool = ..., motionTrailPoint: bool = ..., mtp: bool = ..., motionTrailTangent: bool = ..., mtt: bool = ..., nCloth: bool = ..., ncl: bool = ..., nParticle: bool = ..., npr: bool = ..., nParticleShape: bool = ..., nps: bool = ..., nRigid: bool = ..., nr: bool = ..., nonlinear: bool = ..., nl: bool = ..., nurbsCurve: bool = ..., nc: bool = ..., nurbsSurface: bool = ..., ns: bool = ..., objectComponent: bool = ..., ocm: bool = ..., orientationLocator: bool = ..., ol: bool = ..., particle: bool = ..., pr: bool = ..., particleShape: bool = ..., ps: bool = ..., plane: bool = ..., pl: bool = ..., polymesh: bool = ..., p: bool = ..., polymeshEdge: bool = ..., pe: bool = ..., polymeshFace: bool = ..., pf: bool = ..., polymeshFreeEdge: bool = ..., pfe: bool = ..., polymeshUV: bool = ..., puv: bool = ..., polymeshVertex: bool = ..., pv: bool = ..., polymeshVtxFace: bool = ..., pvf: bool = ..., rigidBody: bool = ..., rb: bool = ..., rigidConstraint: bool = ..., rc: bool = ..., rotatePivot: bool = ..., rp: bool = ..., scalePivot: bool = ..., sp: bool = ..., sculpt: bool = ..., sc: bool = ..., selectHandle: bool = ..., sh: bool = ..., spring: bool = ..., spr: bool = ..., springComponent: bool = ..., spc: bool = ..., stroke: bool = ..., str: bool = ..., subdiv: bool = ..., sd: bool = ..., subdivMeshEdge: bool = ..., sme: bool = ..., subdivMeshFace: bool = ..., smf: bool = ..., subdivMeshPoint: bool = ..., smp: bool = ..., subdivMeshUV: bool = ..., smu: bool = ..., surfaceEdge: bool = ..., se: bool = ..., surfaceFace: bool = ..., sf: bool = ..., surfaceKnot: bool = ..., sk: bool = ..., surfaceParameterPoint: bool = ..., spp: bool = ..., surfaceRange: bool = ..., sr: bool = ..., surfaceUV: bool = ..., suv: bool = ..., texture: bool = ..., tx: bool = ..., vertex: bool = ..., v: bool = ...) -> bool:
    """selectType is undoable, queryable, and NOT editable.
    
    The selectType command is used to change the set of allowable types of objects
    that can be selected when using the select tool. It accepts no other arguments
    besides the flags.
    
    There are basically two different types of items that are selectable when
    interactively selecting objects in the 3D views. They are classified as
    objects (entire objects) or components (parts of objects). The object and
    component command flags control which class of objects are selectable.
    
    It is possible to select components while in the object selection mode. To set
    the components which are selectable in object selection mode you must use the
    -ocm flag when specifying the component flags.

    ---
    - Args:
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - byName (bn): Set the specified user-defined selection mask on/off. (object flag)
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
        - meshUVShell (msh): Set uv shell component mask on/off.
        - motionTrailPoint (mtp): Set motion point selection mask on/off.
        - motionTrailTangent (mtt): Set motion point tangent mask on/off.
        - nCloth (ncl): Set nCloth selection mask on/off. (object flag)
        - nParticle (npr): Set nParticle point selection mask on/off. (component flag)
        - nParticleShape (nps): Set nParticle shape selection mask on/off. (object flag)
        - nRigid (nr): Set nRigid selection mask on/off. (object flag)
        - nonlinear (nl): Set nonlinear selection mask on/off. (object flag)
        - nurbsCurve (nc): Set nurbs-curve selection mask on/off. (object flag)
        - nurbsSurface (ns): Set nurbs-surface selection mask on/off. (object flag)
        - objectComponent (ocm): Component flags apply to object mode.
        - orientationLocator (ol): Set orientation locator selection mask on/off. (object flag)
        - particle (pr): Set particle point selection mask on/off. (component flag)
        - particleShape (ps): Set particle shape selection mask on/off. (object flag)
        - plane (pl): Set sketch plane selection mask on/off. (object flag)
        - polymesh (p): Set poly-mesh selection mask on/off. (object flag)
        - polymeshEdge (pe): Set poly-mesh edge selection mask on/off. (component flag)
        - polymeshFace (pf): Set poly-mesh face selection mask on/off. (component flag)
        - polymeshFreeEdge (pfe): Set poly-mesh free-edge selection mask on/off. (component flag)
        - polymeshUV (puv): Set poly-mesh UV point selection mask on/off. (component flag)
        - polymeshVertex (pv): Set poly-mesh vertex selection mask on/off. (component flag)
        - polymeshVtxFace (pvf): Set poly-mesh vertexFace selection mask on/off. (component flag)
        - rigidBody (rb): Set rigid body selection mask on/off. (object flag)
        - rigidConstraint (rc): Set rigid constraint selection mask on/off. (object flag)
        - rotatePivot (rp): Set rotate pivot selection mask on/off. (component flag)
        - scalePivot (sp): Set scale pivot selection mask on/off. (component flag)
        - sculpt (sc): Set sculpt selection mask on/off. (object flag)
        - selectHandle (sh): Set select handle selection mask on/off. (component flag)
        - spring (spr): Set spring shape selection mask on/off. (object flag)
        - springComponent (spc): Set individual spring selection mask on/off. (component flag)
        - stroke (str): Set the Paint Effects stroke selection mask on/off. (object flag)
        - subdiv (sd): Set subdivision surfaces selection mask on/off. (object flag)
        - subdivMeshEdge (sme): Set subdivision surfaces mesh edge selection mask on/off. (component flag)
        - subdivMeshFace (smf): Set subdivision surfaces mesh face selection mask on/off. (component flag)
        - subdivMeshPoint (smp): Set subdivision surfaces mesh point selection mask on/off. (component flag)
        - subdivMeshUV (smu): Set subdivision surfaces mesh UV map selection mask on/off. (component flag)
        - surfaceEdge (se): Set surface edge selection mask on/off. (component flag)
        - surfaceFace (sf): Set surface face selection mask on/off. (component flag)
        - surfaceKnot (sk): Set surface knot selection mask on/off. (component flag)
        - surfaceParameterPoint (spp): Set surface parameter point selection mask on/off. (component flag)
        - surfaceRange (sr): Set surface range selection mask on/off. (component flag)
        - surfaceUV (suv): Set surface uv selection mask on/off. (component flag)
        - texture (tx): Set texture selection mask on/off. (object flag)
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
    """
@overload #Overload for selectType in ['query']
def selectType(allComponents: bool = ..., allObjects: bool = ..., animBreakdown: bool = ..., animCurve: bool = ..., animInTangent: bool = ..., animKeyframe: bool = ..., animOutTangent: bool = ..., byName: [string, boolean] = ..., camera: bool = ..., cluster: bool = ..., collisionModel: bool = ..., controlVertex: bool = ..., curve: bool = ..., curveKnot: bool = ..., curveOnSurface: bool = ..., curveParameterPoint: bool = ..., dimension: bool = ..., dynamicConstraint: bool = ..., edge: bool = ..., editPoint: bool = ..., emitter: bool = ..., facet: bool = ..., field: bool = ..., fluid: bool = ..., follicle: bool = ..., hairSystem: bool = ..., handle: bool = ..., hull: bool = ..., ikEndEffector: bool = ..., ikHandle: bool = ..., imagePlane: bool = ..., implicitGeometry: bool = ..., isoparm: bool = ..., joint: bool = ..., jointPivot: bool = ..., lattice: bool = ..., latticePoint: bool = ..., light: bool = ..., localRotationAxis: bool = ..., locator: bool = ..., locatorUV: bool = ..., locatorXYZ: bool = ..., meshUVShell: bool = ..., motionTrailPoint: bool = ..., motionTrailTangent: bool = ..., nCloth: bool = ..., nParticle: bool = ..., nParticleShape: bool = ..., nRigid: bool = ..., nonlinear: bool = ..., nurbsCurve: bool = ..., nurbsSurface: bool = ..., objectComponent: bool = ..., orientationLocator: bool = ..., particle: bool = ..., particleShape: bool = ..., plane: bool = ..., polymesh: bool = ..., polymeshEdge: bool = ..., polymeshFace: bool = ..., polymeshFreeEdge: bool = ..., polymeshUV: bool = ..., polymeshVertex: bool = ..., polymeshVtxFace: bool = ..., queryByName: str = ..., rigidBody: bool = ..., rigidConstraint: bool = ..., rotatePivot: bool = ..., scalePivot: bool = ..., sculpt: bool = ..., selectHandle: bool = ..., spring: bool = ..., springComponent: bool = ..., stroke: bool = ..., subdiv: bool = ..., subdivMeshEdge: bool = ..., subdivMeshFace: bool = ..., subdivMeshPoint: bool = ..., subdivMeshUV: bool = ..., surfaceEdge: bool = ..., surfaceFace: bool = ..., surfaceKnot: bool = ..., surfaceParameterPoint: bool = ..., surfaceRange: bool = ..., surfaceUV: bool = ..., texture: bool = ..., vertex: bool = ..., query: bool = ...) -> bool:
    """selectType is undoable, queryable, and NOT editable.
    
    The selectType command is used to change the set of allowable types of objects
    that can be selected when using the select tool. It accepts no other arguments
    besides the flags.
    
    There are basically two different types of items that are selectable when
    interactively selecting objects in the 3D views. They are classified as
    objects (entire objects) or components (parts of objects). The object and
    component command flags control which class of objects are selectable.
    
    It is possible to select components while in the object selection mode. To set
    the components which are selectable in object selection mode you must use the
    -ocm flag when specifying the component flags.

    ---
    - Args:
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - byName (bn): Set the specified user-defined selection mask on/off. (object flag)
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
        - meshUVShell (msh): Set uv shell component mask on/off.
        - motionTrailPoint (mtp): Set motion point selection mask on/off.
        - motionTrailTangent (mtt): Set motion point tangent mask on/off.
        - nCloth (ncl): Set nCloth selection mask on/off. (object flag)
        - nParticle (npr): Set nParticle point selection mask on/off. (component flag)
        - nParticleShape (nps): Set nParticle shape selection mask on/off. (object flag)
        - nRigid (nr): Set nRigid selection mask on/off. (object flag)
        - nonlinear (nl): Set nonlinear selection mask on/off. (object flag)
        - nurbsCurve (nc): Set nurbs-curve selection mask on/off. (object flag)
        - nurbsSurface (ns): Set nurbs-surface selection mask on/off. (object flag)
        - objectComponent (ocm): Component flags apply to object mode.
        - orientationLocator (ol): Set orientation locator selection mask on/off. (object flag)
        - particle (pr): Set particle point selection mask on/off. (component flag)
        - particleShape (ps): Set particle shape selection mask on/off. (object flag)
        - plane (pl): Set sketch plane selection mask on/off. (object flag)
        - polymesh (p): Set poly-mesh selection mask on/off. (object flag)
        - polymeshEdge (pe): Set poly-mesh edge selection mask on/off. (component flag)
        - polymeshFace (pf): Set poly-mesh face selection mask on/off. (component flag)
        - polymeshFreeEdge (pfe): Set poly-mesh free-edge selection mask on/off. (component flag)
        - polymeshUV (puv): Set poly-mesh UV point selection mask on/off. (component flag)
        - polymeshVertex (pv): Set poly-mesh vertex selection mask on/off. (component flag)
        - polymeshVtxFace (pvf): Set poly-mesh vertexFace selection mask on/off. (component flag)
        - queryByName (qbn): Query the specified user-defined selection mask. (object flag)In query mode, this flag needs a value.
        - rigidBody (rb): Set rigid body selection mask on/off. (object flag)
        - rigidConstraint (rc): Set rigid constraint selection mask on/off. (object flag)
        - rotatePivot (rp): Set rotate pivot selection mask on/off. (component flag)
        - scalePivot (sp): Set scale pivot selection mask on/off. (component flag)
        - sculpt (sc): Set sculpt selection mask on/off. (object flag)
        - selectHandle (sh): Set select handle selection mask on/off. (component flag)
        - spring (spr): Set spring shape selection mask on/off. (object flag)
        - springComponent (spc): Set individual spring selection mask on/off. (component flag)
        - stroke (str): Set the Paint Effects stroke selection mask on/off. (object flag)
        - subdiv (sd): Set subdivision surfaces selection mask on/off. (object flag)
        - subdivMeshEdge (sme): Set subdivision surfaces mesh edge selection mask on/off. (component flag)
        - subdivMeshFace (smf): Set subdivision surfaces mesh face selection mask on/off. (component flag)
        - subdivMeshPoint (smp): Set subdivision surfaces mesh point selection mask on/off. (component flag)
        - subdivMeshUV (smu): Set subdivision surfaces mesh UV map selection mask on/off. (component flag)
        - surfaceEdge (se): Set surface edge selection mask on/off. (component flag)
        - surfaceFace (sf): Set surface face selection mask on/off. (component flag)
        - surfaceKnot (sk): Set surface knot selection mask on/off. (component flag)
        - surfaceParameterPoint (spp): Set surface parameter point selection mask on/off. (component flag)
        - surfaceRange (sr): Set surface range selection mask on/off. (component flag)
        - surfaceUV (suv): Set surface uv selection mask on/off. (component flag)
        - texture (tx): Set texture selection mask on/off. (object flag)
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
        - query (q): Query mode flag
    """
@overload #Overload for selectType in ['query']
def selectType(alc: bool = ..., alo: bool = ..., abd: bool = ..., ac: bool = ..., ait: bool = ..., ak: bool = ..., aot: bool = ..., bn: [string, boolean] = ..., ca: bool = ..., cl: bool = ..., clm: bool = ..., cv: bool = ..., c: bool = ..., ck: bool = ..., cos: bool = ..., cpp: bool = ..., dim: bool = ..., dc: bool = ..., eg: bool = ..., ep: bool = ..., em: bool = ..., fc: bool = ..., fi: bool = ..., fl: bool = ..., fo: bool = ..., hs: bool = ..., ha: bool = ..., hl: bool = ..., iee: bool = ..., ikh: bool = ..., ip: bool = ..., ig: bool = ..., iso: bool = ..., j: bool = ..., jp: bool = ..., la: bool = ..., lp: bool = ..., lt: bool = ..., ra: bool = ..., lc: bool = ..., luv: bool = ..., xyz: bool = ..., msh: bool = ..., mtp: bool = ..., mtt: bool = ..., ncl: bool = ..., npr: bool = ..., nps: bool = ..., nr: bool = ..., nl: bool = ..., nc: bool = ..., ns: bool = ..., ocm: bool = ..., ol: bool = ..., pr: bool = ..., ps: bool = ..., pl: bool = ..., p: bool = ..., pe: bool = ..., pf: bool = ..., pfe: bool = ..., puv: bool = ..., pv: bool = ..., pvf: bool = ..., qbn: str = ..., rb: bool = ..., rc: bool = ..., rp: bool = ..., sp: bool = ..., sc: bool = ..., sh: bool = ..., spr: bool = ..., spc: bool = ..., str: bool = ..., sd: bool = ..., sme: bool = ..., smf: bool = ..., smp: bool = ..., smu: bool = ..., se: bool = ..., sf: bool = ..., sk: bool = ..., spp: bool = ..., sr: bool = ..., suv: bool = ..., tx: bool = ..., v: bool = ..., q: bool = ...) -> bool:
    """selectType is undoable, queryable, and NOT editable.
    
    The selectType command is used to change the set of allowable types of objects
    that can be selected when using the select tool. It accepts no other arguments
    besides the flags.
    
    There are basically two different types of items that are selectable when
    interactively selecting objects in the 3D views. They are classified as
    objects (entire objects) or components (parts of objects). The object and
    component command flags control which class of objects are selectable.
    
    It is possible to select components while in the object selection mode. To set
    the components which are selectable in object selection mode you must use the
    -ocm flag when specifying the component flags.

    ---
    - Args:
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - byName (bn): Set the specified user-defined selection mask on/off. (object flag)
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
        - meshUVShell (msh): Set uv shell component mask on/off.
        - motionTrailPoint (mtp): Set motion point selection mask on/off.
        - motionTrailTangent (mtt): Set motion point tangent mask on/off.
        - nCloth (ncl): Set nCloth selection mask on/off. (object flag)
        - nParticle (npr): Set nParticle point selection mask on/off. (component flag)
        - nParticleShape (nps): Set nParticle shape selection mask on/off. (object flag)
        - nRigid (nr): Set nRigid selection mask on/off. (object flag)
        - nonlinear (nl): Set nonlinear selection mask on/off. (object flag)
        - nurbsCurve (nc): Set nurbs-curve selection mask on/off. (object flag)
        - nurbsSurface (ns): Set nurbs-surface selection mask on/off. (object flag)
        - objectComponent (ocm): Component flags apply to object mode.
        - orientationLocator (ol): Set orientation locator selection mask on/off. (object flag)
        - particle (pr): Set particle point selection mask on/off. (component flag)
        - particleShape (ps): Set particle shape selection mask on/off. (object flag)
        - plane (pl): Set sketch plane selection mask on/off. (object flag)
        - polymesh (p): Set poly-mesh selection mask on/off. (object flag)
        - polymeshEdge (pe): Set poly-mesh edge selection mask on/off. (component flag)
        - polymeshFace (pf): Set poly-mesh face selection mask on/off. (component flag)
        - polymeshFreeEdge (pfe): Set poly-mesh free-edge selection mask on/off. (component flag)
        - polymeshUV (puv): Set poly-mesh UV point selection mask on/off. (component flag)
        - polymeshVertex (pv): Set poly-mesh vertex selection mask on/off. (component flag)
        - polymeshVtxFace (pvf): Set poly-mesh vertexFace selection mask on/off. (component flag)
        - queryByName (qbn): Query the specified user-defined selection mask. (object flag)In query mode, this flag needs a value.
        - rigidBody (rb): Set rigid body selection mask on/off. (object flag)
        - rigidConstraint (rc): Set rigid constraint selection mask on/off. (object flag)
        - rotatePivot (rp): Set rotate pivot selection mask on/off. (component flag)
        - scalePivot (sp): Set scale pivot selection mask on/off. (component flag)
        - sculpt (sc): Set sculpt selection mask on/off. (object flag)
        - selectHandle (sh): Set select handle selection mask on/off. (component flag)
        - spring (spr): Set spring shape selection mask on/off. (object flag)
        - springComponent (spc): Set individual spring selection mask on/off. (component flag)
        - stroke (str): Set the Paint Effects stroke selection mask on/off. (object flag)
        - subdiv (sd): Set subdivision surfaces selection mask on/off. (object flag)
        - subdivMeshEdge (sme): Set subdivision surfaces mesh edge selection mask on/off. (component flag)
        - subdivMeshFace (smf): Set subdivision surfaces mesh face selection mask on/off. (component flag)
        - subdivMeshPoint (smp): Set subdivision surfaces mesh point selection mask on/off. (component flag)
        - subdivMeshUV (smu): Set subdivision surfaces mesh UV map selection mask on/off. (component flag)
        - surfaceEdge (se): Set surface edge selection mask on/off. (component flag)
        - surfaceFace (sf): Set surface face selection mask on/off. (component flag)
        - surfaceKnot (sk): Set surface knot selection mask on/off. (component flag)
        - surfaceParameterPoint (spp): Set surface parameter point selection mask on/off. (component flag)
        - surfaceRange (sr): Set surface range selection mask on/off. (component flag)
        - surfaceUV (suv): Set surface uv selection mask on/off. (component flag)
        - texture (tx): Set texture selection mask on/off. (object flag)
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
        - query (q): Query mode flag
    """
@overload #Overload for selectType in ['query']
def selectType(allComponents: bool = ..., alc: bool = ..., allObjects: bool = ..., alo: bool = ..., animBreakdown: bool = ..., abd: bool = ..., animCurve: bool = ..., ac: bool = ..., animInTangent: bool = ..., ait: bool = ..., animKeyframe: bool = ..., ak: bool = ..., animOutTangent: bool = ..., aot: bool = ..., byName: [string, boolean] = ..., bn: [string, boolean] = ..., camera: bool = ..., ca: bool = ..., cluster: bool = ..., cl: bool = ..., collisionModel: bool = ..., clm: bool = ..., controlVertex: bool = ..., cv: bool = ..., curve: bool = ..., c: bool = ..., curveKnot: bool = ..., ck: bool = ..., curveOnSurface: bool = ..., cos: bool = ..., curveParameterPoint: bool = ..., cpp: bool = ..., dimension: bool = ..., dim: bool = ..., dynamicConstraint: bool = ..., dc: bool = ..., edge: bool = ..., eg: bool = ..., editPoint: bool = ..., ep: bool = ..., emitter: bool = ..., em: bool = ..., facet: bool = ..., fc: bool = ..., field: bool = ..., fi: bool = ..., fluid: bool = ..., fl: bool = ..., follicle: bool = ..., fo: bool = ..., hairSystem: bool = ..., hs: bool = ..., handle: bool = ..., ha: bool = ..., hull: bool = ..., hl: bool = ..., ikEndEffector: bool = ..., iee: bool = ..., ikHandle: bool = ..., ikh: bool = ..., imagePlane: bool = ..., ip: bool = ..., implicitGeometry: bool = ..., ig: bool = ..., isoparm: bool = ..., iso: bool = ..., joint: bool = ..., j: bool = ..., jointPivot: bool = ..., jp: bool = ..., lattice: bool = ..., la: bool = ..., latticePoint: bool = ..., lp: bool = ..., light: bool = ..., lt: bool = ..., localRotationAxis: bool = ..., ra: bool = ..., locator: bool = ..., lc: bool = ..., locatorUV: bool = ..., luv: bool = ..., locatorXYZ: bool = ..., xyz: bool = ..., meshUVShell: bool = ..., msh: bool = ..., motionTrailPoint: bool = ..., mtp: bool = ..., motionTrailTangent: bool = ..., mtt: bool = ..., nCloth: bool = ..., ncl: bool = ..., nParticle: bool = ..., npr: bool = ..., nParticleShape: bool = ..., nps: bool = ..., nRigid: bool = ..., nr: bool = ..., nonlinear: bool = ..., nl: bool = ..., nurbsCurve: bool = ..., nc: bool = ..., nurbsSurface: bool = ..., ns: bool = ..., objectComponent: bool = ..., ocm: bool = ..., orientationLocator: bool = ..., ol: bool = ..., particle: bool = ..., pr: bool = ..., particleShape: bool = ..., ps: bool = ..., plane: bool = ..., pl: bool = ..., polymesh: bool = ..., p: bool = ..., polymeshEdge: bool = ..., pe: bool = ..., polymeshFace: bool = ..., pf: bool = ..., polymeshFreeEdge: bool = ..., pfe: bool = ..., polymeshUV: bool = ..., puv: bool = ..., polymeshVertex: bool = ..., pv: bool = ..., polymeshVtxFace: bool = ..., pvf: bool = ..., queryByName: str = ..., qbn: str = ..., rigidBody: bool = ..., rb: bool = ..., rigidConstraint: bool = ..., rc: bool = ..., rotatePivot: bool = ..., rp: bool = ..., scalePivot: bool = ..., sp: bool = ..., sculpt: bool = ..., sc: bool = ..., selectHandle: bool = ..., sh: bool = ..., spring: bool = ..., spr: bool = ..., springComponent: bool = ..., spc: bool = ..., stroke: bool = ..., str: bool = ..., subdiv: bool = ..., sd: bool = ..., subdivMeshEdge: bool = ..., sme: bool = ..., subdivMeshFace: bool = ..., smf: bool = ..., subdivMeshPoint: bool = ..., smp: bool = ..., subdivMeshUV: bool = ..., smu: bool = ..., surfaceEdge: bool = ..., se: bool = ..., surfaceFace: bool = ..., sf: bool = ..., surfaceKnot: bool = ..., sk: bool = ..., surfaceParameterPoint: bool = ..., spp: bool = ..., surfaceRange: bool = ..., sr: bool = ..., surfaceUV: bool = ..., suv: bool = ..., texture: bool = ..., tx: bool = ..., vertex: bool = ..., v: bool = ..., query: bool = ..., q: bool = ...) -> bool:
    """selectType is undoable, queryable, and NOT editable.
    
    The selectType command is used to change the set of allowable types of objects
    that can be selected when using the select tool. It accepts no other arguments
    besides the flags.
    
    There are basically two different types of items that are selectable when
    interactively selecting objects in the 3D views. They are classified as
    objects (entire objects) or components (parts of objects). The object and
    component command flags control which class of objects are selectable.
    
    It is possible to select components while in the object selection mode. To set
    the components which are selectable in object selection mode you must use the
    -ocm flag when specifying the component flags.

    ---
    - Args:
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - byName (bn): Set the specified user-defined selection mask on/off. (object flag)
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
        - meshUVShell (msh): Set uv shell component mask on/off.
        - motionTrailPoint (mtp): Set motion point selection mask on/off.
        - motionTrailTangent (mtt): Set motion point tangent mask on/off.
        - nCloth (ncl): Set nCloth selection mask on/off. (object flag)
        - nParticle (npr): Set nParticle point selection mask on/off. (component flag)
        - nParticleShape (nps): Set nParticle shape selection mask on/off. (object flag)
        - nRigid (nr): Set nRigid selection mask on/off. (object flag)
        - nonlinear (nl): Set nonlinear selection mask on/off. (object flag)
        - nurbsCurve (nc): Set nurbs-curve selection mask on/off. (object flag)
        - nurbsSurface (ns): Set nurbs-surface selection mask on/off. (object flag)
        - objectComponent (ocm): Component flags apply to object mode.
        - orientationLocator (ol): Set orientation locator selection mask on/off. (object flag)
        - particle (pr): Set particle point selection mask on/off. (component flag)
        - particleShape (ps): Set particle shape selection mask on/off. (object flag)
        - plane (pl): Set sketch plane selection mask on/off. (object flag)
        - polymesh (p): Set poly-mesh selection mask on/off. (object flag)
        - polymeshEdge (pe): Set poly-mesh edge selection mask on/off. (component flag)
        - polymeshFace (pf): Set poly-mesh face selection mask on/off. (component flag)
        - polymeshFreeEdge (pfe): Set poly-mesh free-edge selection mask on/off. (component flag)
        - polymeshUV (puv): Set poly-mesh UV point selection mask on/off. (component flag)
        - polymeshVertex (pv): Set poly-mesh vertex selection mask on/off. (component flag)
        - polymeshVtxFace (pvf): Set poly-mesh vertexFace selection mask on/off. (component flag)
        - queryByName (qbn): Query the specified user-defined selection mask. (object flag)In query mode, this flag needs a value.
        - rigidBody (rb): Set rigid body selection mask on/off. (object flag)
        - rigidConstraint (rc): Set rigid constraint selection mask on/off. (object flag)
        - rotatePivot (rp): Set rotate pivot selection mask on/off. (component flag)
        - scalePivot (sp): Set scale pivot selection mask on/off. (component flag)
        - sculpt (sc): Set sculpt selection mask on/off. (object flag)
        - selectHandle (sh): Set select handle selection mask on/off. (component flag)
        - spring (spr): Set spring shape selection mask on/off. (object flag)
        - springComponent (spc): Set individual spring selection mask on/off. (component flag)
        - stroke (str): Set the Paint Effects stroke selection mask on/off. (object flag)
        - subdiv (sd): Set subdivision surfaces selection mask on/off. (object flag)
        - subdivMeshEdge (sme): Set subdivision surfaces mesh edge selection mask on/off. (component flag)
        - subdivMeshFace (smf): Set subdivision surfaces mesh face selection mask on/off. (component flag)
        - subdivMeshPoint (smp): Set subdivision surfaces mesh point selection mask on/off. (component flag)
        - subdivMeshUV (smu): Set subdivision surfaces mesh UV map selection mask on/off. (component flag)
        - surfaceEdge (se): Set surface edge selection mask on/off. (component flag)
        - surfaceFace (sf): Set surface face selection mask on/off. (component flag)
        - surfaceKnot (sk): Set surface knot selection mask on/off. (component flag)
        - surfaceParameterPoint (spp): Set surface parameter point selection mask on/off. (component flag)
        - surfaceRange (sr): Set surface range selection mask on/off. (component flag)
        - surfaceUV (suv): Set surface uv selection mask on/off. (component flag)
        - texture (tx): Set texture selection mask on/off. (object flag)
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
        - query (q): Query mode flag
    """
@overload #Overload for selectType in ['edit']
def selectType(allComponents: bool = ..., allObjects: bool = ..., animBreakdown: bool = ..., animCurve: bool = ..., animInTangent: bool = ..., animKeyframe: bool = ..., animOutTangent: bool = ..., byName: [string, boolean] = ..., camera: bool = ..., cluster: bool = ..., collisionModel: bool = ..., controlVertex: bool = ..., curve: bool = ..., curveKnot: bool = ..., curveOnSurface: bool = ..., curveParameterPoint: bool = ..., dimension: bool = ..., dynamicConstraint: bool = ..., edge: bool = ..., editPoint: bool = ..., emitter: bool = ..., facet: bool = ..., field: bool = ..., fluid: bool = ..., follicle: bool = ..., hairSystem: bool = ..., handle: bool = ..., hull: bool = ..., ikEndEffector: bool = ..., ikHandle: bool = ..., imagePlane: bool = ..., implicitGeometry: bool = ..., isoparm: bool = ..., joint: bool = ..., jointPivot: bool = ..., lattice: bool = ..., latticePoint: bool = ..., light: bool = ..., localRotationAxis: bool = ..., locator: bool = ..., locatorUV: bool = ..., locatorXYZ: bool = ..., meshUVShell: bool = ..., motionTrailPoint: bool = ..., motionTrailTangent: bool = ..., nCloth: bool = ..., nParticle: bool = ..., nParticleShape: bool = ..., nRigid: bool = ..., nonlinear: bool = ..., nurbsCurve: bool = ..., nurbsSurface: bool = ..., objectComponent: bool = ..., orientationLocator: bool = ..., particle: bool = ..., particleShape: bool = ..., plane: bool = ..., polymesh: bool = ..., polymeshEdge: bool = ..., polymeshFace: bool = ..., polymeshFreeEdge: bool = ..., polymeshUV: bool = ..., polymeshVertex: bool = ..., polymeshVtxFace: bool = ..., rigidBody: bool = ..., rigidConstraint: bool = ..., rotatePivot: bool = ..., scalePivot: bool = ..., sculpt: bool = ..., selectHandle: bool = ..., spring: bool = ..., springComponent: bool = ..., stroke: bool = ..., subdiv: bool = ..., subdivMeshEdge: bool = ..., subdivMeshFace: bool = ..., subdivMeshPoint: bool = ..., subdivMeshUV: bool = ..., surfaceEdge: bool = ..., surfaceFace: bool = ..., surfaceKnot: bool = ..., surfaceParameterPoint: bool = ..., surfaceRange: bool = ..., surfaceUV: bool = ..., texture: bool = ..., vertex: bool = ..., edit: bool = ...) -> bool:
    """selectType is undoable, queryable, and NOT editable.
    
    The selectType command is used to change the set of allowable types of objects
    that can be selected when using the select tool. It accepts no other arguments
    besides the flags.
    
    There are basically two different types of items that are selectable when
    interactively selecting objects in the 3D views. They are classified as
    objects (entire objects) or components (parts of objects). The object and
    component command flags control which class of objects are selectable.
    
    It is possible to select components while in the object selection mode. To set
    the components which are selectable in object selection mode you must use the
    -ocm flag when specifying the component flags.

    ---
    - Args:
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - byName (bn): Set the specified user-defined selection mask on/off. (object flag)
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
        - meshUVShell (msh): Set uv shell component mask on/off.
        - motionTrailPoint (mtp): Set motion point selection mask on/off.
        - motionTrailTangent (mtt): Set motion point tangent mask on/off.
        - nCloth (ncl): Set nCloth selection mask on/off. (object flag)
        - nParticle (npr): Set nParticle point selection mask on/off. (component flag)
        - nParticleShape (nps): Set nParticle shape selection mask on/off. (object flag)
        - nRigid (nr): Set nRigid selection mask on/off. (object flag)
        - nonlinear (nl): Set nonlinear selection mask on/off. (object flag)
        - nurbsCurve (nc): Set nurbs-curve selection mask on/off. (object flag)
        - nurbsSurface (ns): Set nurbs-surface selection mask on/off. (object flag)
        - objectComponent (ocm): Component flags apply to object mode.
        - orientationLocator (ol): Set orientation locator selection mask on/off. (object flag)
        - particle (pr): Set particle point selection mask on/off. (component flag)
        - particleShape (ps): Set particle shape selection mask on/off. (object flag)
        - plane (pl): Set sketch plane selection mask on/off. (object flag)
        - polymesh (p): Set poly-mesh selection mask on/off. (object flag)
        - polymeshEdge (pe): Set poly-mesh edge selection mask on/off. (component flag)
        - polymeshFace (pf): Set poly-mesh face selection mask on/off. (component flag)
        - polymeshFreeEdge (pfe): Set poly-mesh free-edge selection mask on/off. (component flag)
        - polymeshUV (puv): Set poly-mesh UV point selection mask on/off. (component flag)
        - polymeshVertex (pv): Set poly-mesh vertex selection mask on/off. (component flag)
        - polymeshVtxFace (pvf): Set poly-mesh vertexFace selection mask on/off. (component flag)
        - rigidBody (rb): Set rigid body selection mask on/off. (object flag)
        - rigidConstraint (rc): Set rigid constraint selection mask on/off. (object flag)
        - rotatePivot (rp): Set rotate pivot selection mask on/off. (component flag)
        - scalePivot (sp): Set scale pivot selection mask on/off. (component flag)
        - sculpt (sc): Set sculpt selection mask on/off. (object flag)
        - selectHandle (sh): Set select handle selection mask on/off. (component flag)
        - spring (spr): Set spring shape selection mask on/off. (object flag)
        - springComponent (spc): Set individual spring selection mask on/off. (component flag)
        - stroke (str): Set the Paint Effects stroke selection mask on/off. (object flag)
        - subdiv (sd): Set subdivision surfaces selection mask on/off. (object flag)
        - subdivMeshEdge (sme): Set subdivision surfaces mesh edge selection mask on/off. (component flag)
        - subdivMeshFace (smf): Set subdivision surfaces mesh face selection mask on/off. (component flag)
        - subdivMeshPoint (smp): Set subdivision surfaces mesh point selection mask on/off. (component flag)
        - subdivMeshUV (smu): Set subdivision surfaces mesh UV map selection mask on/off. (component flag)
        - surfaceEdge (se): Set surface edge selection mask on/off. (component flag)
        - surfaceFace (sf): Set surface face selection mask on/off. (component flag)
        - surfaceKnot (sk): Set surface knot selection mask on/off. (component flag)
        - surfaceParameterPoint (spp): Set surface parameter point selection mask on/off. (component flag)
        - surfaceRange (sr): Set surface range selection mask on/off. (component flag)
        - surfaceUV (suv): Set surface uv selection mask on/off. (component flag)
        - texture (tx): Set texture selection mask on/off. (object flag)
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
        - edit (e): Edit mode flag
    """
@overload #Overload for selectType in ['edit']
def selectType(alc: bool = ..., alo: bool = ..., abd: bool = ..., ac: bool = ..., ait: bool = ..., ak: bool = ..., aot: bool = ..., bn: [string, boolean] = ..., ca: bool = ..., cl: bool = ..., clm: bool = ..., cv: bool = ..., c: bool = ..., ck: bool = ..., cos: bool = ..., cpp: bool = ..., dim: bool = ..., dc: bool = ..., eg: bool = ..., ep: bool = ..., em: bool = ..., fc: bool = ..., fi: bool = ..., fl: bool = ..., fo: bool = ..., hs: bool = ..., ha: bool = ..., hl: bool = ..., iee: bool = ..., ikh: bool = ..., ip: bool = ..., ig: bool = ..., iso: bool = ..., j: bool = ..., jp: bool = ..., la: bool = ..., lp: bool = ..., lt: bool = ..., ra: bool = ..., lc: bool = ..., luv: bool = ..., xyz: bool = ..., msh: bool = ..., mtp: bool = ..., mtt: bool = ..., ncl: bool = ..., npr: bool = ..., nps: bool = ..., nr: bool = ..., nl: bool = ..., nc: bool = ..., ns: bool = ..., ocm: bool = ..., ol: bool = ..., pr: bool = ..., ps: bool = ..., pl: bool = ..., p: bool = ..., pe: bool = ..., pf: bool = ..., pfe: bool = ..., puv: bool = ..., pv: bool = ..., pvf: bool = ..., rb: bool = ..., rc: bool = ..., rp: bool = ..., sp: bool = ..., sc: bool = ..., sh: bool = ..., spr: bool = ..., spc: bool = ..., str: bool = ..., sd: bool = ..., sme: bool = ..., smf: bool = ..., smp: bool = ..., smu: bool = ..., se: bool = ..., sf: bool = ..., sk: bool = ..., spp: bool = ..., sr: bool = ..., suv: bool = ..., tx: bool = ..., v: bool = ..., e: bool = ...) -> bool:
    """selectType is undoable, queryable, and NOT editable.
    
    The selectType command is used to change the set of allowable types of objects
    that can be selected when using the select tool. It accepts no other arguments
    besides the flags.
    
    There are basically two different types of items that are selectable when
    interactively selecting objects in the 3D views. They are classified as
    objects (entire objects) or components (parts of objects). The object and
    component command flags control which class of objects are selectable.
    
    It is possible to select components while in the object selection mode. To set
    the components which are selectable in object selection mode you must use the
    -ocm flag when specifying the component flags.

    ---
    - Args:
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - byName (bn): Set the specified user-defined selection mask on/off. (object flag)
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
        - meshUVShell (msh): Set uv shell component mask on/off.
        - motionTrailPoint (mtp): Set motion point selection mask on/off.
        - motionTrailTangent (mtt): Set motion point tangent mask on/off.
        - nCloth (ncl): Set nCloth selection mask on/off. (object flag)
        - nParticle (npr): Set nParticle point selection mask on/off. (component flag)
        - nParticleShape (nps): Set nParticle shape selection mask on/off. (object flag)
        - nRigid (nr): Set nRigid selection mask on/off. (object flag)
        - nonlinear (nl): Set nonlinear selection mask on/off. (object flag)
        - nurbsCurve (nc): Set nurbs-curve selection mask on/off. (object flag)
        - nurbsSurface (ns): Set nurbs-surface selection mask on/off. (object flag)
        - objectComponent (ocm): Component flags apply to object mode.
        - orientationLocator (ol): Set orientation locator selection mask on/off. (object flag)
        - particle (pr): Set particle point selection mask on/off. (component flag)
        - particleShape (ps): Set particle shape selection mask on/off. (object flag)
        - plane (pl): Set sketch plane selection mask on/off. (object flag)
        - polymesh (p): Set poly-mesh selection mask on/off. (object flag)
        - polymeshEdge (pe): Set poly-mesh edge selection mask on/off. (component flag)
        - polymeshFace (pf): Set poly-mesh face selection mask on/off. (component flag)
        - polymeshFreeEdge (pfe): Set poly-mesh free-edge selection mask on/off. (component flag)
        - polymeshUV (puv): Set poly-mesh UV point selection mask on/off. (component flag)
        - polymeshVertex (pv): Set poly-mesh vertex selection mask on/off. (component flag)
        - polymeshVtxFace (pvf): Set poly-mesh vertexFace selection mask on/off. (component flag)
        - rigidBody (rb): Set rigid body selection mask on/off. (object flag)
        - rigidConstraint (rc): Set rigid constraint selection mask on/off. (object flag)
        - rotatePivot (rp): Set rotate pivot selection mask on/off. (component flag)
        - scalePivot (sp): Set scale pivot selection mask on/off. (component flag)
        - sculpt (sc): Set sculpt selection mask on/off. (object flag)
        - selectHandle (sh): Set select handle selection mask on/off. (component flag)
        - spring (spr): Set spring shape selection mask on/off. (object flag)
        - springComponent (spc): Set individual spring selection mask on/off. (component flag)
        - stroke (str): Set the Paint Effects stroke selection mask on/off. (object flag)
        - subdiv (sd): Set subdivision surfaces selection mask on/off. (object flag)
        - subdivMeshEdge (sme): Set subdivision surfaces mesh edge selection mask on/off. (component flag)
        - subdivMeshFace (smf): Set subdivision surfaces mesh face selection mask on/off. (component flag)
        - subdivMeshPoint (smp): Set subdivision surfaces mesh point selection mask on/off. (component flag)
        - subdivMeshUV (smu): Set subdivision surfaces mesh UV map selection mask on/off. (component flag)
        - surfaceEdge (se): Set surface edge selection mask on/off. (component flag)
        - surfaceFace (sf): Set surface face selection mask on/off. (component flag)
        - surfaceKnot (sk): Set surface knot selection mask on/off. (component flag)
        - surfaceParameterPoint (spp): Set surface parameter point selection mask on/off. (component flag)
        - surfaceRange (sr): Set surface range selection mask on/off. (component flag)
        - surfaceUV (suv): Set surface uv selection mask on/off. (component flag)
        - texture (tx): Set texture selection mask on/off. (object flag)
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
        - edit (e): Edit mode flag
    """
@overload #Overload for selectType in ['edit']
def selectType(allComponents: bool = ..., alc: bool = ..., allObjects: bool = ..., alo: bool = ..., animBreakdown: bool = ..., abd: bool = ..., animCurve: bool = ..., ac: bool = ..., animInTangent: bool = ..., ait: bool = ..., animKeyframe: bool = ..., ak: bool = ..., animOutTangent: bool = ..., aot: bool = ..., byName: [string, boolean] = ..., bn: [string, boolean] = ..., camera: bool = ..., ca: bool = ..., cluster: bool = ..., cl: bool = ..., collisionModel: bool = ..., clm: bool = ..., controlVertex: bool = ..., cv: bool = ..., curve: bool = ..., c: bool = ..., curveKnot: bool = ..., ck: bool = ..., curveOnSurface: bool = ..., cos: bool = ..., curveParameterPoint: bool = ..., cpp: bool = ..., dimension: bool = ..., dim: bool = ..., dynamicConstraint: bool = ..., dc: bool = ..., edge: bool = ..., eg: bool = ..., editPoint: bool = ..., ep: bool = ..., emitter: bool = ..., em: bool = ..., facet: bool = ..., fc: bool = ..., field: bool = ..., fi: bool = ..., fluid: bool = ..., fl: bool = ..., follicle: bool = ..., fo: bool = ..., hairSystem: bool = ..., hs: bool = ..., handle: bool = ..., ha: bool = ..., hull: bool = ..., hl: bool = ..., ikEndEffector: bool = ..., iee: bool = ..., ikHandle: bool = ..., ikh: bool = ..., imagePlane: bool = ..., ip: bool = ..., implicitGeometry: bool = ..., ig: bool = ..., isoparm: bool = ..., iso: bool = ..., joint: bool = ..., j: bool = ..., jointPivot: bool = ..., jp: bool = ..., lattice: bool = ..., la: bool = ..., latticePoint: bool = ..., lp: bool = ..., light: bool = ..., lt: bool = ..., localRotationAxis: bool = ..., ra: bool = ..., locator: bool = ..., lc: bool = ..., locatorUV: bool = ..., luv: bool = ..., locatorXYZ: bool = ..., xyz: bool = ..., meshUVShell: bool = ..., msh: bool = ..., motionTrailPoint: bool = ..., mtp: bool = ..., motionTrailTangent: bool = ..., mtt: bool = ..., nCloth: bool = ..., ncl: bool = ..., nParticle: bool = ..., npr: bool = ..., nParticleShape: bool = ..., nps: bool = ..., nRigid: bool = ..., nr: bool = ..., nonlinear: bool = ..., nl: bool = ..., nurbsCurve: bool = ..., nc: bool = ..., nurbsSurface: bool = ..., ns: bool = ..., objectComponent: bool = ..., ocm: bool = ..., orientationLocator: bool = ..., ol: bool = ..., particle: bool = ..., pr: bool = ..., particleShape: bool = ..., ps: bool = ..., plane: bool = ..., pl: bool = ..., polymesh: bool = ..., p: bool = ..., polymeshEdge: bool = ..., pe: bool = ..., polymeshFace: bool = ..., pf: bool = ..., polymeshFreeEdge: bool = ..., pfe: bool = ..., polymeshUV: bool = ..., puv: bool = ..., polymeshVertex: bool = ..., pv: bool = ..., polymeshVtxFace: bool = ..., pvf: bool = ..., rigidBody: bool = ..., rb: bool = ..., rigidConstraint: bool = ..., rc: bool = ..., rotatePivot: bool = ..., rp: bool = ..., scalePivot: bool = ..., sp: bool = ..., sculpt: bool = ..., sc: bool = ..., selectHandle: bool = ..., sh: bool = ..., spring: bool = ..., spr: bool = ..., springComponent: bool = ..., spc: bool = ..., stroke: bool = ..., str: bool = ..., subdiv: bool = ..., sd: bool = ..., subdivMeshEdge: bool = ..., sme: bool = ..., subdivMeshFace: bool = ..., smf: bool = ..., subdivMeshPoint: bool = ..., smp: bool = ..., subdivMeshUV: bool = ..., smu: bool = ..., surfaceEdge: bool = ..., se: bool = ..., surfaceFace: bool = ..., sf: bool = ..., surfaceKnot: bool = ..., sk: bool = ..., surfaceParameterPoint: bool = ..., spp: bool = ..., surfaceRange: bool = ..., sr: bool = ..., surfaceUV: bool = ..., suv: bool = ..., texture: bool = ..., tx: bool = ..., vertex: bool = ..., v: bool = ..., edit: bool = ..., e: bool = ...) -> bool:
    """selectType is undoable, queryable, and NOT editable.
    
    The selectType command is used to change the set of allowable types of objects
    that can be selected when using the select tool. It accepts no other arguments
    besides the flags.
    
    There are basically two different types of items that are selectable when
    interactively selecting objects in the 3D views. They are classified as
    objects (entire objects) or components (parts of objects). The object and
    component command flags control which class of objects are selectable.
    
    It is possible to select components while in the object selection mode. To set
    the components which are selectable in object selection mode you must use the
    -ocm flag when specifying the component flags.

    ---
    - Args:
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - byName (bn): Set the specified user-defined selection mask on/off. (object flag)
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
        - meshUVShell (msh): Set uv shell component mask on/off.
        - motionTrailPoint (mtp): Set motion point selection mask on/off.
        - motionTrailTangent (mtt): Set motion point tangent mask on/off.
        - nCloth (ncl): Set nCloth selection mask on/off. (object flag)
        - nParticle (npr): Set nParticle point selection mask on/off. (component flag)
        - nParticleShape (nps): Set nParticle shape selection mask on/off. (object flag)
        - nRigid (nr): Set nRigid selection mask on/off. (object flag)
        - nonlinear (nl): Set nonlinear selection mask on/off. (object flag)
        - nurbsCurve (nc): Set nurbs-curve selection mask on/off. (object flag)
        - nurbsSurface (ns): Set nurbs-surface selection mask on/off. (object flag)
        - objectComponent (ocm): Component flags apply to object mode.
        - orientationLocator (ol): Set orientation locator selection mask on/off. (object flag)
        - particle (pr): Set particle point selection mask on/off. (component flag)
        - particleShape (ps): Set particle shape selection mask on/off. (object flag)
        - plane (pl): Set sketch plane selection mask on/off. (object flag)
        - polymesh (p): Set poly-mesh selection mask on/off. (object flag)
        - polymeshEdge (pe): Set poly-mesh edge selection mask on/off. (component flag)
        - polymeshFace (pf): Set poly-mesh face selection mask on/off. (component flag)
        - polymeshFreeEdge (pfe): Set poly-mesh free-edge selection mask on/off. (component flag)
        - polymeshUV (puv): Set poly-mesh UV point selection mask on/off. (component flag)
        - polymeshVertex (pv): Set poly-mesh vertex selection mask on/off. (component flag)
        - polymeshVtxFace (pvf): Set poly-mesh vertexFace selection mask on/off. (component flag)
        - rigidBody (rb): Set rigid body selection mask on/off. (object flag)
        - rigidConstraint (rc): Set rigid constraint selection mask on/off. (object flag)
        - rotatePivot (rp): Set rotate pivot selection mask on/off. (component flag)
        - scalePivot (sp): Set scale pivot selection mask on/off. (component flag)
        - sculpt (sc): Set sculpt selection mask on/off. (object flag)
        - selectHandle (sh): Set select handle selection mask on/off. (component flag)
        - spring (spr): Set spring shape selection mask on/off. (object flag)
        - springComponent (spc): Set individual spring selection mask on/off. (component flag)
        - stroke (str): Set the Paint Effects stroke selection mask on/off. (object flag)
        - subdiv (sd): Set subdivision surfaces selection mask on/off. (object flag)
        - subdivMeshEdge (sme): Set subdivision surfaces mesh edge selection mask on/off. (component flag)
        - subdivMeshFace (smf): Set subdivision surfaces mesh face selection mask on/off. (component flag)
        - subdivMeshPoint (smp): Set subdivision surfaces mesh point selection mask on/off. (component flag)
        - subdivMeshUV (smu): Set subdivision surfaces mesh UV map selection mask on/off. (component flag)
        - surfaceEdge (se): Set surface edge selection mask on/off. (component flag)
        - surfaceFace (sf): Set surface face selection mask on/off. (component flag)
        - surfaceKnot (sk): Set surface knot selection mask on/off. (component flag)
        - surfaceParameterPoint (spp): Set surface parameter point selection mask on/off. (component flag)
        - surfaceRange (sr): Set surface range selection mask on/off. (component flag)
        - surfaceUV (suv): Set surface uv selection mask on/off. (component flag)
        - texture (tx): Set texture selection mask on/off. (object flag)
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
        - edit (e): Edit mode flag
    """
