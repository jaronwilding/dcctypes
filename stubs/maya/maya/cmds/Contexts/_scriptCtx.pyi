"""Stub files for Contexts category in Maya commands, command: scriptCtx."""

from typing import Any, overload

@overload #Overload for scriptCtx in ['create']
def scriptCtx(string: str, allComponents: bool = ..., allObjects: bool = ..., animBreakdown: bool = ..., animCurve: bool = ..., animInTangent: bool = ..., animKeyframe: bool = ..., animOutTangent: bool = ..., baseClassName: str = ..., camera: bool = ..., cluster: bool = ..., collisionModel: bool = ..., controlVertex: bool = ..., cumulativeLists: bool = ..., curve: bool = ..., curveKnot: bool = ..., curveOnSurface: bool = ..., curveParameterPoint: bool = ..., dimension: bool = ..., dynamicConstraint: bool = ..., edge: bool = ..., editPoint: bool = ..., emitter: bool = ..., enableRootSelection: bool = ..., escToQuit: bool = ..., exists: bool = ..., exitUponCompletion: bool = ..., expandSelectionList: bool = ..., facet: bool = ..., field: bool = ..., finalCommandScript: script = ..., fluid: bool = ..., follicle: bool = ..., forceAddSelect: bool = ..., hairSystem: bool = ..., handle: bool = ..., history: bool = ..., hull: bool = ..., ignoreInvalidItems: bool = ..., ikEndEffector: bool = ..., ikHandle: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., imagePlane: bool = ..., implicitGeometry: bool = ..., isoparm: bool = ..., joint: bool = ..., jointPivot: bool = ..., lastAutoComplete: bool = ..., lattice: bool = ..., latticePoint: bool = ..., light: bool = ..., localRotationAxis: bool = ..., locator: bool = ..., locatorUV: bool = ..., locatorXYZ: bool = ..., nCloth: bool = ..., nParticle: bool = ..., nParticleShape: bool = ..., nRigid: bool = ..., name: str = ..., nonlinear: bool = ..., nurbsCurve: bool = ..., nurbsSurface: bool = ..., objectComponent: bool = ..., orientationLocator: bool = ..., particle: bool = ..., particleShape: bool = ..., plane: bool = ..., polymesh: bool = ..., polymeshEdge: bool = ..., polymeshFace: bool = ..., polymeshFreeEdge: bool = ..., polymeshUV: bool = ..., polymeshVertex: bool = ..., polymeshVtxFace: bool = ..., rigidBody: bool = ..., rigidConstraint: bool = ..., rotatePivot: bool = ..., scalePivot: bool = ..., sculpt: bool = ..., selectHandle: bool = ..., setAllowExcessCount: bool = ..., setAutoComplete: bool = ..., setAutoToggleSelection: bool = ..., setDoneSelectionPrompt: str = ..., setNoSelectionHeadsUp: str = ..., setNoSelectionPrompt: str = ..., setSelectionCount: int = ..., setSelectionHeadsUp: str = ..., setSelectionPrompt: str = ..., showManipulators: bool = ..., spring: bool = ..., springComponent: bool = ..., stroke: bool = ..., subdiv: bool = ..., subdivMeshEdge: bool = ..., subdivMeshFace: bool = ..., subdivMeshPoint: bool = ..., subdivMeshUV: bool = ..., surfaceEdge: bool = ..., surfaceFace: bool = ..., surfaceKnot: bool = ..., surfaceParameterPoint: bool = ..., surfaceRange: bool = ..., surfaceUV: bool = ..., texture: bool = ..., title: str = ..., toolCursorType: str = ..., toolFinish: script = ..., toolStart: script = ..., totalSelectionSets: int = ..., vertex: bool = ...) -> str:
    """scriptCtx is undoable, queryable, and editable.
    
    This command allows a user to create their own tools based on the selection
    tool. A number of selection lists can be collected, the behaviour of the
    selection and the selection masks are fully customizable, etc.
    
    The command is processed prior to being executed. The keyword "$Selection#"
    where # is a number 1 or greater specifies a selection set. The context can
    specify several selection sets which are substituted in place of the
    $Selection# keyword in the form of a Mel string array. Items that are specific
    per set need to be specified in each set, if they are going to be specified
    for any of the sets. See examples below.
    
    In addition, in order to specify the type of selection you need to be making,
    any of the selection type flags from "selectType" command can be used here.

    ---
    - Args:
        - string: Input item(s).
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - baseClassName (bcn): This string will be used to produce MEL function names for the property sheets for the tool.  For example, if "myScriptTool" was given, the functions "myScriptToolValues" and "myScriptToolProperties" will be used for the property sheets.
            The default is "scriptTool".
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - cumulativeLists (cls): If set, the selection lists will be cumulative.  For example, the second list will contain all the items from the first list, the third all the items from the second list etc.  Make sure your script specified above takes that into account.
            Relevant if there is more than one selection set.
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - enableRootSelection (ers): If set, the items to be selected are at their root transform level. Default is false.
        - escToQuit (esc): If set to true, exit the tool when press "Esc". Default is false.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - exitUponCompletion (euc): If set, completing the last selection set will exit the tool.  Default is true.
        - expandSelectionList (esl): If set, the selection lists will expand to have a single component in each item.  You probably want this as a default, otherwise two isoparms on the same surface will show up as 1 item.To ensure that components on the same object are
            returned in the order in which they are selected, use theselectPref -trackSelectionOrder oncommand in your-toolStartscript to enable ordered selection, then restore it to its original value in your-toolFinishscript.
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - finalCommandScript (fcs): Supply the script that will be run when the user presses the enter key and the context is completed.  Depending on the number of selection sets you have, the script can make use of variables string $Selection1[], $Selection2[], ...
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - forceAddSelect (fas): If set to true, together with -setAutoToggleSelection (see below) on the first selection set, causes the first selection after the computation of the previous result to be "shift" selection, unless a modifier key is pressed.  Default is
            false.Flags for each selection set.  These flags are multi-use.
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ignoreInvalidItems (iii): If you have multiple selection sets, the state of the selection set is recorded at the time you "complete it".  You could then delete some of the items in that list and end up with invalid items in one or more of your selection sets.  If
            this flag is set, those items will be detected and ignored.  You will never know it happened.  Its as if they were never selected in the first place, except that your selection set now does not have as many items as it may need.  If this
            flag is not set, you will get a warning and your final command callback script will likely not execute because of an error condition.
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lastAutoComplete (lac): True if auto complete is set for the last selection set, false otherwise.  Mostly used for query, but if present in conjuction with -sac/setAutoComplete flag, -sac flag takes precedence.
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
        - nCloth (ncl): Set nCloth selection mask on/off. (object flag)
        - nParticle (npr): Set nParticle point selection mask on/off. (component flag)
        - nParticleShape (nps): Set nParticle shape selection mask on/off. (object flag)
        - nRigid (nr): Set nRigid selection mask on/off. (object flag)
        - name (n): If this is a tool command, name the tool appropriately.
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
        - setAllowExcessCount (sae): If set, the number if items is to be interpreted as the minimum.
        - setAutoComplete (sac): If set to true, as soon as the specified number of items is selected the tool will start the next selection set or run the command.
        - setAutoToggleSelection (sat): If set to true, it is as if "shift" key is pressed when there are no modifiers pressed.  That means that you get the "toggle select" behaviour by default.  This only applies to the 3D view, and the selection done in the hypergraph, outliner
            or elsewhere is still a subject to the usual rules.
        - setDoneSelectionPrompt (dsp): If setAutoComplete is not set (see below) this string will be shown as soon as the tool has enough items for a particular selection set.  If this is not set, but is needed, the same string as set with -setSelectionPrompt flag will be used.
        - setNoSelectionHeadsUp (snh): Supply a string that will be shown as a heads up prompt when there is nothing selected.  This must be set separately for each selection set.
        - setNoSelectionPrompt (snp): Supply a string that will be shown as help when there is nothing selected.  This must be set separately for each selection set.
        - setSelectionCount (ssc): The number of items in this selection set.  0 means as many as you need until completion.
        - setSelectionHeadsUp (ssh): Supply a string that will be shown as a heads up prompt when there is something selected.  This must be set separately for each selection set.
        - setSelectionPrompt (ssp): Supply a string that will be shown as help when there is something selected.  This must be set separately for each selection set.
        - showManipulators (sm): If set, the manipulators will be shown for any active objects. Basically, it is as if you are in the Show Manipulator tool.
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
        - title (t): Supply a string that will be used as a precursor to all the messages; i.e., the "name" of the tool.
        - toolCursorType (tct): Supply the string identifier to set the tool cursor type when inside of tool. The following are the valid ids: "create", "dolly", "edit", "pencil", "track", "trackHorizontal", "trackVertical", "transformation", "tumble", "zoom", "zoomIn",
            "zoomOut", "flyThrough", "dot", "fleur", "leftArrow", "question", "doubleHorizArrow", "doubleVertArrow", "sizing", "dollyIn", "dollyOut", "brush", "camera", "noAccess", "input", "output", "leftCycle", "rightCycle", "rightExpand", "knife".
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
        - totalSelectionSets (tss): Total number of selection sets.
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
    """
@overload #Overload for scriptCtx in ['create']
def scriptCtx(string: str, alc: bool = ..., alo: bool = ..., abd: bool = ..., ac: bool = ..., ait: bool = ..., ak: bool = ..., aot: bool = ..., bcn: str = ..., ca: bool = ..., cl: bool = ..., clm: bool = ..., cv: bool = ..., cls: bool = ..., c: bool = ..., ck: bool = ..., cos: bool = ..., cpp: bool = ..., dim: bool = ..., dc: bool = ..., eg: bool = ..., ep: bool = ..., em: bool = ..., ers: bool = ..., esc: bool = ..., ex: bool = ..., euc: bool = ..., esl: bool = ..., fc: bool = ..., fi: bool = ..., fcs: script = ..., fl: bool = ..., fo: bool = ..., fas: bool = ..., hs: bool = ..., ha: bool = ..., ch: bool = ..., hl: bool = ..., iii: bool = ..., iee: bool = ..., ikh: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ip: bool = ..., ig: bool = ..., iso: bool = ..., j: bool = ..., jp: bool = ..., lac: bool = ..., la: bool = ..., lp: bool = ..., lt: bool = ..., ra: bool = ..., lc: bool = ..., luv: bool = ..., xyz: bool = ..., ncl: bool = ..., npr: bool = ..., nps: bool = ..., nr: bool = ..., n: str = ..., nl: bool = ..., nc: bool = ..., ns: bool = ..., ocm: bool = ..., ol: bool = ..., pr: bool = ..., ps: bool = ..., pl: bool = ..., p: bool = ..., pe: bool = ..., pf: bool = ..., pfe: bool = ..., puv: bool = ..., pv: bool = ..., pvf: bool = ..., rb: bool = ..., rc: bool = ..., rp: bool = ..., sp: bool = ..., sc: bool = ..., sh: bool = ..., sae: bool = ..., sac: bool = ..., sat: bool = ..., dsp: str = ..., snh: str = ..., snp: str = ..., ssc: int = ..., ssh: str = ..., ssp: str = ..., sm: bool = ..., spr: bool = ..., spc: bool = ..., str: bool = ..., sd: bool = ..., sme: bool = ..., smf: bool = ..., smp: bool = ..., smu: bool = ..., se: bool = ..., sf: bool = ..., sk: bool = ..., spp: bool = ..., sr: bool = ..., suv: bool = ..., tx: bool = ..., t: str = ..., tct: str = ..., tf: script = ..., ts: script = ..., tss: int = ..., v: bool = ...) -> str:
    """scriptCtx is undoable, queryable, and editable.
    
    This command allows a user to create their own tools based on the selection
    tool. A number of selection lists can be collected, the behaviour of the
    selection and the selection masks are fully customizable, etc.
    
    The command is processed prior to being executed. The keyword "$Selection#"
    where # is a number 1 or greater specifies a selection set. The context can
    specify several selection sets which are substituted in place of the
    $Selection# keyword in the form of a Mel string array. Items that are specific
    per set need to be specified in each set, if they are going to be specified
    for any of the sets. See examples below.
    
    In addition, in order to specify the type of selection you need to be making,
    any of the selection type flags from "selectType" command can be used here.

    ---
    - Args:
        - string: Input item(s).
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - baseClassName (bcn): This string will be used to produce MEL function names for the property sheets for the tool.  For example, if "myScriptTool" was given, the functions "myScriptToolValues" and "myScriptToolProperties" will be used for the property sheets.
            The default is "scriptTool".
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - cumulativeLists (cls): If set, the selection lists will be cumulative.  For example, the second list will contain all the items from the first list, the third all the items from the second list etc.  Make sure your script specified above takes that into account.
            Relevant if there is more than one selection set.
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - enableRootSelection (ers): If set, the items to be selected are at their root transform level. Default is false.
        - escToQuit (esc): If set to true, exit the tool when press "Esc". Default is false.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - exitUponCompletion (euc): If set, completing the last selection set will exit the tool.  Default is true.
        - expandSelectionList (esl): If set, the selection lists will expand to have a single component in each item.  You probably want this as a default, otherwise two isoparms on the same surface will show up as 1 item.To ensure that components on the same object are
            returned in the order in which they are selected, use theselectPref -trackSelectionOrder oncommand in your-toolStartscript to enable ordered selection, then restore it to its original value in your-toolFinishscript.
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - finalCommandScript (fcs): Supply the script that will be run when the user presses the enter key and the context is completed.  Depending on the number of selection sets you have, the script can make use of variables string $Selection1[], $Selection2[], ...
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - forceAddSelect (fas): If set to true, together with -setAutoToggleSelection (see below) on the first selection set, causes the first selection after the computation of the previous result to be "shift" selection, unless a modifier key is pressed.  Default is
            false.Flags for each selection set.  These flags are multi-use.
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ignoreInvalidItems (iii): If you have multiple selection sets, the state of the selection set is recorded at the time you "complete it".  You could then delete some of the items in that list and end up with invalid items in one or more of your selection sets.  If
            this flag is set, those items will be detected and ignored.  You will never know it happened.  Its as if they were never selected in the first place, except that your selection set now does not have as many items as it may need.  If this
            flag is not set, you will get a warning and your final command callback script will likely not execute because of an error condition.
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lastAutoComplete (lac): True if auto complete is set for the last selection set, false otherwise.  Mostly used for query, but if present in conjuction with -sac/setAutoComplete flag, -sac flag takes precedence.
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
        - nCloth (ncl): Set nCloth selection mask on/off. (object flag)
        - nParticle (npr): Set nParticle point selection mask on/off. (component flag)
        - nParticleShape (nps): Set nParticle shape selection mask on/off. (object flag)
        - nRigid (nr): Set nRigid selection mask on/off. (object flag)
        - name (n): If this is a tool command, name the tool appropriately.
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
        - setAllowExcessCount (sae): If set, the number if items is to be interpreted as the minimum.
        - setAutoComplete (sac): If set to true, as soon as the specified number of items is selected the tool will start the next selection set or run the command.
        - setAutoToggleSelection (sat): If set to true, it is as if "shift" key is pressed when there are no modifiers pressed.  That means that you get the "toggle select" behaviour by default.  This only applies to the 3D view, and the selection done in the hypergraph, outliner
            or elsewhere is still a subject to the usual rules.
        - setDoneSelectionPrompt (dsp): If setAutoComplete is not set (see below) this string will be shown as soon as the tool has enough items for a particular selection set.  If this is not set, but is needed, the same string as set with -setSelectionPrompt flag will be used.
        - setNoSelectionHeadsUp (snh): Supply a string that will be shown as a heads up prompt when there is nothing selected.  This must be set separately for each selection set.
        - setNoSelectionPrompt (snp): Supply a string that will be shown as help when there is nothing selected.  This must be set separately for each selection set.
        - setSelectionCount (ssc): The number of items in this selection set.  0 means as many as you need until completion.
        - setSelectionHeadsUp (ssh): Supply a string that will be shown as a heads up prompt when there is something selected.  This must be set separately for each selection set.
        - setSelectionPrompt (ssp): Supply a string that will be shown as help when there is something selected.  This must be set separately for each selection set.
        - showManipulators (sm): If set, the manipulators will be shown for any active objects. Basically, it is as if you are in the Show Manipulator tool.
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
        - title (t): Supply a string that will be used as a precursor to all the messages; i.e., the "name" of the tool.
        - toolCursorType (tct): Supply the string identifier to set the tool cursor type when inside of tool. The following are the valid ids: "create", "dolly", "edit", "pencil", "track", "trackHorizontal", "trackVertical", "transformation", "tumble", "zoom", "zoomIn",
            "zoomOut", "flyThrough", "dot", "fleur", "leftArrow", "question", "doubleHorizArrow", "doubleVertArrow", "sizing", "dollyIn", "dollyOut", "brush", "camera", "noAccess", "input", "output", "leftCycle", "rightCycle", "rightExpand", "knife".
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
        - totalSelectionSets (tss): Total number of selection sets.
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
    """
@overload #Overload for scriptCtx in ['create']
def scriptCtx(string: str, allComponents: bool = ..., alc: bool = ..., allObjects: bool = ..., alo: bool = ..., animBreakdown: bool = ..., abd: bool = ..., animCurve: bool = ..., ac: bool = ..., animInTangent: bool = ..., ait: bool = ..., animKeyframe: bool = ..., ak: bool = ..., animOutTangent: bool = ..., aot: bool = ..., baseClassName: str = ..., bcn: str = ..., camera: bool = ..., ca: bool = ..., cluster: bool = ..., cl: bool = ..., collisionModel: bool = ..., clm: bool = ..., controlVertex: bool = ..., cv: bool = ..., cumulativeLists: bool = ..., cls: bool = ..., curve: bool = ..., c: bool = ..., curveKnot: bool = ..., ck: bool = ..., curveOnSurface: bool = ..., cos: bool = ..., curveParameterPoint: bool = ..., cpp: bool = ..., dimension: bool = ..., dim: bool = ..., dynamicConstraint: bool = ..., dc: bool = ..., edge: bool = ..., eg: bool = ..., editPoint: bool = ..., ep: bool = ..., emitter: bool = ..., em: bool = ..., enableRootSelection: bool = ..., ers: bool = ..., escToQuit: bool = ..., esc: bool = ..., exists: bool = ..., ex: bool = ..., exitUponCompletion: bool = ..., euc: bool = ..., expandSelectionList: bool = ..., esl: bool = ..., facet: bool = ..., fc: bool = ..., field: bool = ..., fi: bool = ..., finalCommandScript: script = ..., fcs: script = ..., fluid: bool = ..., fl: bool = ..., follicle: bool = ..., fo: bool = ..., forceAddSelect: bool = ..., fas: bool = ..., hairSystem: bool = ..., hs: bool = ..., handle: bool = ..., ha: bool = ..., history: bool = ..., ch: bool = ..., hull: bool = ..., hl: bool = ..., ignoreInvalidItems: bool = ..., iii: bool = ..., ikEndEffector: bool = ..., iee: bool = ..., ikHandle: bool = ..., ikh: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., imagePlane: bool = ..., ip: bool = ..., implicitGeometry: bool = ..., ig: bool = ..., isoparm: bool = ..., iso: bool = ..., joint: bool = ..., j: bool = ..., jointPivot: bool = ..., jp: bool = ..., lastAutoComplete: bool = ..., lac: bool = ..., lattice: bool = ..., la: bool = ..., latticePoint: bool = ..., lp: bool = ..., light: bool = ..., lt: bool = ..., localRotationAxis: bool = ..., ra: bool = ..., locator: bool = ..., lc: bool = ..., locatorUV: bool = ..., luv: bool = ..., locatorXYZ: bool = ..., xyz: bool = ..., nCloth: bool = ..., ncl: bool = ..., nParticle: bool = ..., npr: bool = ..., nParticleShape: bool = ..., nps: bool = ..., nRigid: bool = ..., nr: bool = ..., name: str = ..., n: str = ..., nonlinear: bool = ..., nl: bool = ..., nurbsCurve: bool = ..., nc: bool = ..., nurbsSurface: bool = ..., ns: bool = ..., objectComponent: bool = ..., ocm: bool = ..., orientationLocator: bool = ..., ol: bool = ..., particle: bool = ..., pr: bool = ..., particleShape: bool = ..., ps: bool = ..., plane: bool = ..., pl: bool = ..., polymesh: bool = ..., p: bool = ..., polymeshEdge: bool = ..., pe: bool = ..., polymeshFace: bool = ..., pf: bool = ..., polymeshFreeEdge: bool = ..., pfe: bool = ..., polymeshUV: bool = ..., puv: bool = ..., polymeshVertex: bool = ..., pv: bool = ..., polymeshVtxFace: bool = ..., pvf: bool = ..., rigidBody: bool = ..., rb: bool = ..., rigidConstraint: bool = ..., rc: bool = ..., rotatePivot: bool = ..., rp: bool = ..., scalePivot: bool = ..., sp: bool = ..., sculpt: bool = ..., sc: bool = ..., selectHandle: bool = ..., sh: bool = ..., setAllowExcessCount: bool = ..., sae: bool = ..., setAutoComplete: bool = ..., sac: bool = ..., setAutoToggleSelection: bool = ..., sat: bool = ..., setDoneSelectionPrompt: str = ..., dsp: str = ..., setNoSelectionHeadsUp: str = ..., snh: str = ..., setNoSelectionPrompt: str = ..., snp: str = ..., setSelectionCount: int = ..., ssc: int = ..., setSelectionHeadsUp: str = ..., ssh: str = ..., setSelectionPrompt: str = ..., ssp: str = ..., showManipulators: bool = ..., sm: bool = ..., spring: bool = ..., spr: bool = ..., springComponent: bool = ..., spc: bool = ..., stroke: bool = ..., str: bool = ..., subdiv: bool = ..., sd: bool = ..., subdivMeshEdge: bool = ..., sme: bool = ..., subdivMeshFace: bool = ..., smf: bool = ..., subdivMeshPoint: bool = ..., smp: bool = ..., subdivMeshUV: bool = ..., smu: bool = ..., surfaceEdge: bool = ..., se: bool = ..., surfaceFace: bool = ..., sf: bool = ..., surfaceKnot: bool = ..., sk: bool = ..., surfaceParameterPoint: bool = ..., spp: bool = ..., surfaceRange: bool = ..., sr: bool = ..., surfaceUV: bool = ..., suv: bool = ..., texture: bool = ..., tx: bool = ..., title: str = ..., t: str = ..., toolCursorType: str = ..., tct: str = ..., toolFinish: script = ..., tf: script = ..., toolStart: script = ..., ts: script = ..., totalSelectionSets: int = ..., tss: int = ..., vertex: bool = ..., v: bool = ...) -> str:
    """scriptCtx is undoable, queryable, and editable.
    
    This command allows a user to create their own tools based on the selection
    tool. A number of selection lists can be collected, the behaviour of the
    selection and the selection masks are fully customizable, etc.
    
    The command is processed prior to being executed. The keyword "$Selection#"
    where # is a number 1 or greater specifies a selection set. The context can
    specify several selection sets which are substituted in place of the
    $Selection# keyword in the form of a Mel string array. Items that are specific
    per set need to be specified in each set, if they are going to be specified
    for any of the sets. See examples below.
    
    In addition, in order to specify the type of selection you need to be making,
    any of the selection type flags from "selectType" command can be used here.

    ---
    - Args:
        - string: Input item(s).
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - baseClassName (bcn): This string will be used to produce MEL function names for the property sheets for the tool.  For example, if "myScriptTool" was given, the functions "myScriptToolValues" and "myScriptToolProperties" will be used for the property sheets.
            The default is "scriptTool".
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - cumulativeLists (cls): If set, the selection lists will be cumulative.  For example, the second list will contain all the items from the first list, the third all the items from the second list etc.  Make sure your script specified above takes that into account.
            Relevant if there is more than one selection set.
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - enableRootSelection (ers): If set, the items to be selected are at their root transform level. Default is false.
        - escToQuit (esc): If set to true, exit the tool when press "Esc". Default is false.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - exitUponCompletion (euc): If set, completing the last selection set will exit the tool.  Default is true.
        - expandSelectionList (esl): If set, the selection lists will expand to have a single component in each item.  You probably want this as a default, otherwise two isoparms on the same surface will show up as 1 item.To ensure that components on the same object are
            returned in the order in which they are selected, use theselectPref -trackSelectionOrder oncommand in your-toolStartscript to enable ordered selection, then restore it to its original value in your-toolFinishscript.
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - finalCommandScript (fcs): Supply the script that will be run when the user presses the enter key and the context is completed.  Depending on the number of selection sets you have, the script can make use of variables string $Selection1[], $Selection2[], ...
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - forceAddSelect (fas): If set to true, together with -setAutoToggleSelection (see below) on the first selection set, causes the first selection after the computation of the previous result to be "shift" selection, unless a modifier key is pressed.  Default is
            false.Flags for each selection set.  These flags are multi-use.
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ignoreInvalidItems (iii): If you have multiple selection sets, the state of the selection set is recorded at the time you "complete it".  You could then delete some of the items in that list and end up with invalid items in one or more of your selection sets.  If
            this flag is set, those items will be detected and ignored.  You will never know it happened.  Its as if they were never selected in the first place, except that your selection set now does not have as many items as it may need.  If this
            flag is not set, you will get a warning and your final command callback script will likely not execute because of an error condition.
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lastAutoComplete (lac): True if auto complete is set for the last selection set, false otherwise.  Mostly used for query, but if present in conjuction with -sac/setAutoComplete flag, -sac flag takes precedence.
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
        - nCloth (ncl): Set nCloth selection mask on/off. (object flag)
        - nParticle (npr): Set nParticle point selection mask on/off. (component flag)
        - nParticleShape (nps): Set nParticle shape selection mask on/off. (object flag)
        - nRigid (nr): Set nRigid selection mask on/off. (object flag)
        - name (n): If this is a tool command, name the tool appropriately.
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
        - setAllowExcessCount (sae): If set, the number if items is to be interpreted as the minimum.
        - setAutoComplete (sac): If set to true, as soon as the specified number of items is selected the tool will start the next selection set or run the command.
        - setAutoToggleSelection (sat): If set to true, it is as if "shift" key is pressed when there are no modifiers pressed.  That means that you get the "toggle select" behaviour by default.  This only applies to the 3D view, and the selection done in the hypergraph, outliner
            or elsewhere is still a subject to the usual rules.
        - setDoneSelectionPrompt (dsp): If setAutoComplete is not set (see below) this string will be shown as soon as the tool has enough items for a particular selection set.  If this is not set, but is needed, the same string as set with -setSelectionPrompt flag will be used.
        - setNoSelectionHeadsUp (snh): Supply a string that will be shown as a heads up prompt when there is nothing selected.  This must be set separately for each selection set.
        - setNoSelectionPrompt (snp): Supply a string that will be shown as help when there is nothing selected.  This must be set separately for each selection set.
        - setSelectionCount (ssc): The number of items in this selection set.  0 means as many as you need until completion.
        - setSelectionHeadsUp (ssh): Supply a string that will be shown as a heads up prompt when there is something selected.  This must be set separately for each selection set.
        - setSelectionPrompt (ssp): Supply a string that will be shown as help when there is something selected.  This must be set separately for each selection set.
        - showManipulators (sm): If set, the manipulators will be shown for any active objects. Basically, it is as if you are in the Show Manipulator tool.
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
        - title (t): Supply a string that will be used as a precursor to all the messages; i.e., the "name" of the tool.
        - toolCursorType (tct): Supply the string identifier to set the tool cursor type when inside of tool. The following are the valid ids: "create", "dolly", "edit", "pencil", "track", "trackHorizontal", "trackVertical", "transformation", "tumble", "zoom", "zoomIn",
            "zoomOut", "flyThrough", "dot", "fleur", "leftArrow", "question", "doubleHorizArrow", "doubleVertArrow", "sizing", "dollyIn", "dollyOut", "brush", "camera", "noAccess", "input", "output", "leftCycle", "rightCycle", "rightExpand", "knife".
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
        - totalSelectionSets (tss): Total number of selection sets.
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
    """
@overload #Overload for scriptCtx in ['query']
def scriptCtx(string: str, allComponents: bool = ..., allObjects: bool = ..., animBreakdown: bool = ..., animCurve: bool = ..., animInTangent: bool = ..., animKeyframe: bool = ..., animOutTangent: bool = ..., baseClassName: str = ..., camera: bool = ..., cluster: bool = ..., collisionModel: bool = ..., controlVertex: bool = ..., cumulativeLists: bool = ..., curve: bool = ..., curveKnot: bool = ..., curveOnSurface: bool = ..., curveParameterPoint: bool = ..., dimension: bool = ..., dynamicConstraint: bool = ..., edge: bool = ..., editPoint: bool = ..., emitter: bool = ..., enableRootSelection: bool = ..., escToQuit: bool = ..., exitUponCompletion: bool = ..., expandSelectionList: bool = ..., facet: bool = ..., field: bool = ..., finalCommandScript: script = ..., fluid: bool = ..., follicle: bool = ..., forceAddSelect: bool = ..., hairSystem: bool = ..., handle: bool = ..., hull: bool = ..., ignoreInvalidItems: bool = ..., ikEndEffector: bool = ..., ikHandle: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., imagePlane: bool = ..., implicitGeometry: bool = ..., isoparm: bool = ..., joint: bool = ..., jointPivot: bool = ..., lastAutoComplete: bool = ..., lattice: bool = ..., latticePoint: bool = ..., light: bool = ..., localRotationAxis: bool = ..., locator: bool = ..., locatorUV: bool = ..., locatorXYZ: bool = ..., nCloth: bool = ..., nParticle: bool = ..., nParticleShape: bool = ..., nRigid: bool = ..., nonlinear: bool = ..., nurbsCurve: bool = ..., nurbsSurface: bool = ..., objectComponent: bool = ..., orientationLocator: bool = ..., particle: bool = ..., particleShape: bool = ..., plane: bool = ..., polymesh: bool = ..., polymeshEdge: bool = ..., polymeshFace: bool = ..., polymeshFreeEdge: bool = ..., polymeshUV: bool = ..., polymeshVertex: bool = ..., polymeshVtxFace: bool = ..., rigidBody: bool = ..., rigidConstraint: bool = ..., rotatePivot: bool = ..., scalePivot: bool = ..., sculpt: bool = ..., selectHandle: bool = ..., setAllowExcessCount: bool = ..., setAutoComplete: bool = ..., setAutoToggleSelection: bool = ..., setDoneSelectionPrompt: str = ..., setNoSelectionHeadsUp: str = ..., setNoSelectionPrompt: str = ..., setSelectionCount: int = ..., setSelectionHeadsUp: str = ..., setSelectionPrompt: str = ..., showManipulators: bool = ..., spring: bool = ..., springComponent: bool = ..., stroke: bool = ..., subdiv: bool = ..., subdivMeshEdge: bool = ..., subdivMeshFace: bool = ..., subdivMeshPoint: bool = ..., subdivMeshUV: bool = ..., surfaceEdge: bool = ..., surfaceFace: bool = ..., surfaceKnot: bool = ..., surfaceParameterPoint: bool = ..., surfaceRange: bool = ..., surfaceUV: bool = ..., texture: bool = ..., title: str = ..., toolCursorType: str = ..., toolFinish: script = ..., toolStart: script = ..., totalSelectionSets: int = ..., vertex: bool = ..., query: bool = ...) -> str:
    """scriptCtx is undoable, queryable, and editable.
    
    This command allows a user to create their own tools based on the selection
    tool. A number of selection lists can be collected, the behaviour of the
    selection and the selection masks are fully customizable, etc.
    
    The command is processed prior to being executed. The keyword "$Selection#"
    where # is a number 1 or greater specifies a selection set. The context can
    specify several selection sets which are substituted in place of the
    $Selection# keyword in the form of a Mel string array. Items that are specific
    per set need to be specified in each set, if they are going to be specified
    for any of the sets. See examples below.
    
    In addition, in order to specify the type of selection you need to be making,
    any of the selection type flags from "selectType" command can be used here.

    ---
    - Args:
        - string: Input item(s).
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - baseClassName (bcn): This string will be used to produce MEL function names for the property sheets for the tool.  For example, if "myScriptTool" was given, the functions "myScriptToolValues" and "myScriptToolProperties" will be used for the property sheets.
            The default is "scriptTool".
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - cumulativeLists (cls): If set, the selection lists will be cumulative.  For example, the second list will contain all the items from the first list, the third all the items from the second list etc.  Make sure your script specified above takes that into account.
            Relevant if there is more than one selection set.
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - enableRootSelection (ers): If set, the items to be selected are at their root transform level. Default is false.
        - escToQuit (esc): If set to true, exit the tool when press "Esc". Default is false.
        - exitUponCompletion (euc): If set, completing the last selection set will exit the tool.  Default is true.
        - expandSelectionList (esl): If set, the selection lists will expand to have a single component in each item.  You probably want this as a default, otherwise two isoparms on the same surface will show up as 1 item.To ensure that components on the same object are
            returned in the order in which they are selected, use theselectPref -trackSelectionOrder oncommand in your-toolStartscript to enable ordered selection, then restore it to its original value in your-toolFinishscript.
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - finalCommandScript (fcs): Supply the script that will be run when the user presses the enter key and the context is completed.  Depending on the number of selection sets you have, the script can make use of variables string $Selection1[], $Selection2[], ...
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - forceAddSelect (fas): If set to true, together with -setAutoToggleSelection (see below) on the first selection set, causes the first selection after the computation of the previous result to be "shift" selection, unless a modifier key is pressed.  Default is
            false.Flags for each selection set.  These flags are multi-use.
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ignoreInvalidItems (iii): If you have multiple selection sets, the state of the selection set is recorded at the time you "complete it".  You could then delete some of the items in that list and end up with invalid items in one or more of your selection sets.  If
            this flag is set, those items will be detected and ignored.  You will never know it happened.  Its as if they were never selected in the first place, except that your selection set now does not have as many items as it may need.  If this
            flag is not set, you will get a warning and your final command callback script will likely not execute because of an error condition.
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lastAutoComplete (lac): True if auto complete is set for the last selection set, false otherwise.  Mostly used for query, but if present in conjuction with -sac/setAutoComplete flag, -sac flag takes precedence.
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
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
        - setAllowExcessCount (sae): If set, the number if items is to be interpreted as the minimum.
        - setAutoComplete (sac): If set to true, as soon as the specified number of items is selected the tool will start the next selection set or run the command.
        - setAutoToggleSelection (sat): If set to true, it is as if "shift" key is pressed when there are no modifiers pressed.  That means that you get the "toggle select" behaviour by default.  This only applies to the 3D view, and the selection done in the hypergraph, outliner
            or elsewhere is still a subject to the usual rules.
        - setDoneSelectionPrompt (dsp): If setAutoComplete is not set (see below) this string will be shown as soon as the tool has enough items for a particular selection set.  If this is not set, but is needed, the same string as set with -setSelectionPrompt flag will be used.
        - setNoSelectionHeadsUp (snh): Supply a string that will be shown as a heads up prompt when there is nothing selected.  This must be set separately for each selection set.
        - setNoSelectionPrompt (snp): Supply a string that will be shown as help when there is nothing selected.  This must be set separately for each selection set.
        - setSelectionCount (ssc): The number of items in this selection set.  0 means as many as you need until completion.
        - setSelectionHeadsUp (ssh): Supply a string that will be shown as a heads up prompt when there is something selected.  This must be set separately for each selection set.
        - setSelectionPrompt (ssp): Supply a string that will be shown as help when there is something selected.  This must be set separately for each selection set.
        - showManipulators (sm): If set, the manipulators will be shown for any active objects. Basically, it is as if you are in the Show Manipulator tool.
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
        - title (t): Supply a string that will be used as a precursor to all the messages; i.e., the "name" of the tool.
        - toolCursorType (tct): Supply the string identifier to set the tool cursor type when inside of tool. The following are the valid ids: "create", "dolly", "edit", "pencil", "track", "trackHorizontal", "trackVertical", "transformation", "tumble", "zoom", "zoomIn",
            "zoomOut", "flyThrough", "dot", "fleur", "leftArrow", "question", "doubleHorizArrow", "doubleVertArrow", "sizing", "dollyIn", "dollyOut", "brush", "camera", "noAccess", "input", "output", "leftCycle", "rightCycle", "rightExpand", "knife".
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
        - totalSelectionSets (tss): Total number of selection sets.
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
        - query (q): Query mode flag
    """
@overload #Overload for scriptCtx in ['query']
def scriptCtx(string: str, alc: bool = ..., alo: bool = ..., abd: bool = ..., ac: bool = ..., ait: bool = ..., ak: bool = ..., aot: bool = ..., bcn: str = ..., ca: bool = ..., cl: bool = ..., clm: bool = ..., cv: bool = ..., cls: bool = ..., c: bool = ..., ck: bool = ..., cos: bool = ..., cpp: bool = ..., dim: bool = ..., dc: bool = ..., eg: bool = ..., ep: bool = ..., em: bool = ..., ers: bool = ..., esc: bool = ..., euc: bool = ..., esl: bool = ..., fc: bool = ..., fi: bool = ..., fcs: script = ..., fl: bool = ..., fo: bool = ..., fas: bool = ..., hs: bool = ..., ha: bool = ..., hl: bool = ..., iii: bool = ..., iee: bool = ..., ikh: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ip: bool = ..., ig: bool = ..., iso: bool = ..., j: bool = ..., jp: bool = ..., lac: bool = ..., la: bool = ..., lp: bool = ..., lt: bool = ..., ra: bool = ..., lc: bool = ..., luv: bool = ..., xyz: bool = ..., ncl: bool = ..., npr: bool = ..., nps: bool = ..., nr: bool = ..., nl: bool = ..., nc: bool = ..., ns: bool = ..., ocm: bool = ..., ol: bool = ..., pr: bool = ..., ps: bool = ..., pl: bool = ..., p: bool = ..., pe: bool = ..., pf: bool = ..., pfe: bool = ..., puv: bool = ..., pv: bool = ..., pvf: bool = ..., rb: bool = ..., rc: bool = ..., rp: bool = ..., sp: bool = ..., sc: bool = ..., sh: bool = ..., sae: bool = ..., sac: bool = ..., sat: bool = ..., dsp: str = ..., snh: str = ..., snp: str = ..., ssc: int = ..., ssh: str = ..., ssp: str = ..., sm: bool = ..., spr: bool = ..., spc: bool = ..., str: bool = ..., sd: bool = ..., sme: bool = ..., smf: bool = ..., smp: bool = ..., smu: bool = ..., se: bool = ..., sf: bool = ..., sk: bool = ..., spp: bool = ..., sr: bool = ..., suv: bool = ..., tx: bool = ..., t: str = ..., tct: str = ..., tf: script = ..., ts: script = ..., tss: int = ..., v: bool = ..., q: bool = ...) -> str:
    """scriptCtx is undoable, queryable, and editable.
    
    This command allows a user to create their own tools based on the selection
    tool. A number of selection lists can be collected, the behaviour of the
    selection and the selection masks are fully customizable, etc.
    
    The command is processed prior to being executed. The keyword "$Selection#"
    where # is a number 1 or greater specifies a selection set. The context can
    specify several selection sets which are substituted in place of the
    $Selection# keyword in the form of a Mel string array. Items that are specific
    per set need to be specified in each set, if they are going to be specified
    for any of the sets. See examples below.
    
    In addition, in order to specify the type of selection you need to be making,
    any of the selection type flags from "selectType" command can be used here.

    ---
    - Args:
        - string: Input item(s).
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - baseClassName (bcn): This string will be used to produce MEL function names for the property sheets for the tool.  For example, if "myScriptTool" was given, the functions "myScriptToolValues" and "myScriptToolProperties" will be used for the property sheets.
            The default is "scriptTool".
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - cumulativeLists (cls): If set, the selection lists will be cumulative.  For example, the second list will contain all the items from the first list, the third all the items from the second list etc.  Make sure your script specified above takes that into account.
            Relevant if there is more than one selection set.
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - enableRootSelection (ers): If set, the items to be selected are at their root transform level. Default is false.
        - escToQuit (esc): If set to true, exit the tool when press "Esc". Default is false.
        - exitUponCompletion (euc): If set, completing the last selection set will exit the tool.  Default is true.
        - expandSelectionList (esl): If set, the selection lists will expand to have a single component in each item.  You probably want this as a default, otherwise two isoparms on the same surface will show up as 1 item.To ensure that components on the same object are
            returned in the order in which they are selected, use theselectPref -trackSelectionOrder oncommand in your-toolStartscript to enable ordered selection, then restore it to its original value in your-toolFinishscript.
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - finalCommandScript (fcs): Supply the script that will be run when the user presses the enter key and the context is completed.  Depending on the number of selection sets you have, the script can make use of variables string $Selection1[], $Selection2[], ...
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - forceAddSelect (fas): If set to true, together with -setAutoToggleSelection (see below) on the first selection set, causes the first selection after the computation of the previous result to be "shift" selection, unless a modifier key is pressed.  Default is
            false.Flags for each selection set.  These flags are multi-use.
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ignoreInvalidItems (iii): If you have multiple selection sets, the state of the selection set is recorded at the time you "complete it".  You could then delete some of the items in that list and end up with invalid items in one or more of your selection sets.  If
            this flag is set, those items will be detected and ignored.  You will never know it happened.  Its as if they were never selected in the first place, except that your selection set now does not have as many items as it may need.  If this
            flag is not set, you will get a warning and your final command callback script will likely not execute because of an error condition.
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lastAutoComplete (lac): True if auto complete is set for the last selection set, false otherwise.  Mostly used for query, but if present in conjuction with -sac/setAutoComplete flag, -sac flag takes precedence.
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
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
        - setAllowExcessCount (sae): If set, the number if items is to be interpreted as the minimum.
        - setAutoComplete (sac): If set to true, as soon as the specified number of items is selected the tool will start the next selection set or run the command.
        - setAutoToggleSelection (sat): If set to true, it is as if "shift" key is pressed when there are no modifiers pressed.  That means that you get the "toggle select" behaviour by default.  This only applies to the 3D view, and the selection done in the hypergraph, outliner
            or elsewhere is still a subject to the usual rules.
        - setDoneSelectionPrompt (dsp): If setAutoComplete is not set (see below) this string will be shown as soon as the tool has enough items for a particular selection set.  If this is not set, but is needed, the same string as set with -setSelectionPrompt flag will be used.
        - setNoSelectionHeadsUp (snh): Supply a string that will be shown as a heads up prompt when there is nothing selected.  This must be set separately for each selection set.
        - setNoSelectionPrompt (snp): Supply a string that will be shown as help when there is nothing selected.  This must be set separately for each selection set.
        - setSelectionCount (ssc): The number of items in this selection set.  0 means as many as you need until completion.
        - setSelectionHeadsUp (ssh): Supply a string that will be shown as a heads up prompt when there is something selected.  This must be set separately for each selection set.
        - setSelectionPrompt (ssp): Supply a string that will be shown as help when there is something selected.  This must be set separately for each selection set.
        - showManipulators (sm): If set, the manipulators will be shown for any active objects. Basically, it is as if you are in the Show Manipulator tool.
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
        - title (t): Supply a string that will be used as a precursor to all the messages; i.e., the "name" of the tool.
        - toolCursorType (tct): Supply the string identifier to set the tool cursor type when inside of tool. The following are the valid ids: "create", "dolly", "edit", "pencil", "track", "trackHorizontal", "trackVertical", "transformation", "tumble", "zoom", "zoomIn",
            "zoomOut", "flyThrough", "dot", "fleur", "leftArrow", "question", "doubleHorizArrow", "doubleVertArrow", "sizing", "dollyIn", "dollyOut", "brush", "camera", "noAccess", "input", "output", "leftCycle", "rightCycle", "rightExpand", "knife".
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
        - totalSelectionSets (tss): Total number of selection sets.
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
        - query (q): Query mode flag
    """
@overload #Overload for scriptCtx in ['query']
def scriptCtx(string: str, allComponents: bool = ..., alc: bool = ..., allObjects: bool = ..., alo: bool = ..., animBreakdown: bool = ..., abd: bool = ..., animCurve: bool = ..., ac: bool = ..., animInTangent: bool = ..., ait: bool = ..., animKeyframe: bool = ..., ak: bool = ..., animOutTangent: bool = ..., aot: bool = ..., baseClassName: str = ..., bcn: str = ..., camera: bool = ..., ca: bool = ..., cluster: bool = ..., cl: bool = ..., collisionModel: bool = ..., clm: bool = ..., controlVertex: bool = ..., cv: bool = ..., cumulativeLists: bool = ..., cls: bool = ..., curve: bool = ..., c: bool = ..., curveKnot: bool = ..., ck: bool = ..., curveOnSurface: bool = ..., cos: bool = ..., curveParameterPoint: bool = ..., cpp: bool = ..., dimension: bool = ..., dim: bool = ..., dynamicConstraint: bool = ..., dc: bool = ..., edge: bool = ..., eg: bool = ..., editPoint: bool = ..., ep: bool = ..., emitter: bool = ..., em: bool = ..., enableRootSelection: bool = ..., ers: bool = ..., escToQuit: bool = ..., esc: bool = ..., exitUponCompletion: bool = ..., euc: bool = ..., expandSelectionList: bool = ..., esl: bool = ..., facet: bool = ..., fc: bool = ..., field: bool = ..., fi: bool = ..., finalCommandScript: script = ..., fcs: script = ..., fluid: bool = ..., fl: bool = ..., follicle: bool = ..., fo: bool = ..., forceAddSelect: bool = ..., fas: bool = ..., hairSystem: bool = ..., hs: bool = ..., handle: bool = ..., ha: bool = ..., hull: bool = ..., hl: bool = ..., ignoreInvalidItems: bool = ..., iii: bool = ..., ikEndEffector: bool = ..., iee: bool = ..., ikHandle: bool = ..., ikh: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., imagePlane: bool = ..., ip: bool = ..., implicitGeometry: bool = ..., ig: bool = ..., isoparm: bool = ..., iso: bool = ..., joint: bool = ..., j: bool = ..., jointPivot: bool = ..., jp: bool = ..., lastAutoComplete: bool = ..., lac: bool = ..., lattice: bool = ..., la: bool = ..., latticePoint: bool = ..., lp: bool = ..., light: bool = ..., lt: bool = ..., localRotationAxis: bool = ..., ra: bool = ..., locator: bool = ..., lc: bool = ..., locatorUV: bool = ..., luv: bool = ..., locatorXYZ: bool = ..., xyz: bool = ..., nCloth: bool = ..., ncl: bool = ..., nParticle: bool = ..., npr: bool = ..., nParticleShape: bool = ..., nps: bool = ..., nRigid: bool = ..., nr: bool = ..., nonlinear: bool = ..., nl: bool = ..., nurbsCurve: bool = ..., nc: bool = ..., nurbsSurface: bool = ..., ns: bool = ..., objectComponent: bool = ..., ocm: bool = ..., orientationLocator: bool = ..., ol: bool = ..., particle: bool = ..., pr: bool = ..., particleShape: bool = ..., ps: bool = ..., plane: bool = ..., pl: bool = ..., polymesh: bool = ..., p: bool = ..., polymeshEdge: bool = ..., pe: bool = ..., polymeshFace: bool = ..., pf: bool = ..., polymeshFreeEdge: bool = ..., pfe: bool = ..., polymeshUV: bool = ..., puv: bool = ..., polymeshVertex: bool = ..., pv: bool = ..., polymeshVtxFace: bool = ..., pvf: bool = ..., rigidBody: bool = ..., rb: bool = ..., rigidConstraint: bool = ..., rc: bool = ..., rotatePivot: bool = ..., rp: bool = ..., scalePivot: bool = ..., sp: bool = ..., sculpt: bool = ..., sc: bool = ..., selectHandle: bool = ..., sh: bool = ..., setAllowExcessCount: bool = ..., sae: bool = ..., setAutoComplete: bool = ..., sac: bool = ..., setAutoToggleSelection: bool = ..., sat: bool = ..., setDoneSelectionPrompt: str = ..., dsp: str = ..., setNoSelectionHeadsUp: str = ..., snh: str = ..., setNoSelectionPrompt: str = ..., snp: str = ..., setSelectionCount: int = ..., ssc: int = ..., setSelectionHeadsUp: str = ..., ssh: str = ..., setSelectionPrompt: str = ..., ssp: str = ..., showManipulators: bool = ..., sm: bool = ..., spring: bool = ..., spr: bool = ..., springComponent: bool = ..., spc: bool = ..., stroke: bool = ..., str: bool = ..., subdiv: bool = ..., sd: bool = ..., subdivMeshEdge: bool = ..., sme: bool = ..., subdivMeshFace: bool = ..., smf: bool = ..., subdivMeshPoint: bool = ..., smp: bool = ..., subdivMeshUV: bool = ..., smu: bool = ..., surfaceEdge: bool = ..., se: bool = ..., surfaceFace: bool = ..., sf: bool = ..., surfaceKnot: bool = ..., sk: bool = ..., surfaceParameterPoint: bool = ..., spp: bool = ..., surfaceRange: bool = ..., sr: bool = ..., surfaceUV: bool = ..., suv: bool = ..., texture: bool = ..., tx: bool = ..., title: str = ..., t: str = ..., toolCursorType: str = ..., tct: str = ..., toolFinish: script = ..., tf: script = ..., toolStart: script = ..., ts: script = ..., totalSelectionSets: int = ..., tss: int = ..., vertex: bool = ..., v: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """scriptCtx is undoable, queryable, and editable.
    
    This command allows a user to create their own tools based on the selection
    tool. A number of selection lists can be collected, the behaviour of the
    selection and the selection masks are fully customizable, etc.
    
    The command is processed prior to being executed. The keyword "$Selection#"
    where # is a number 1 or greater specifies a selection set. The context can
    specify several selection sets which are substituted in place of the
    $Selection# keyword in the form of a Mel string array. Items that are specific
    per set need to be specified in each set, if they are going to be specified
    for any of the sets. See examples below.
    
    In addition, in order to specify the type of selection you need to be making,
    any of the selection type flags from "selectType" command can be used here.

    ---
    - Args:
        - string: Input item(s).
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - baseClassName (bcn): This string will be used to produce MEL function names for the property sheets for the tool.  For example, if "myScriptTool" was given, the functions "myScriptToolValues" and "myScriptToolProperties" will be used for the property sheets.
            The default is "scriptTool".
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - cumulativeLists (cls): If set, the selection lists will be cumulative.  For example, the second list will contain all the items from the first list, the third all the items from the second list etc.  Make sure your script specified above takes that into account.
            Relevant if there is more than one selection set.
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - enableRootSelection (ers): If set, the items to be selected are at their root transform level. Default is false.
        - escToQuit (esc): If set to true, exit the tool when press "Esc". Default is false.
        - exitUponCompletion (euc): If set, completing the last selection set will exit the tool.  Default is true.
        - expandSelectionList (esl): If set, the selection lists will expand to have a single component in each item.  You probably want this as a default, otherwise two isoparms on the same surface will show up as 1 item.To ensure that components on the same object are
            returned in the order in which they are selected, use theselectPref -trackSelectionOrder oncommand in your-toolStartscript to enable ordered selection, then restore it to its original value in your-toolFinishscript.
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - finalCommandScript (fcs): Supply the script that will be run when the user presses the enter key and the context is completed.  Depending on the number of selection sets you have, the script can make use of variables string $Selection1[], $Selection2[], ...
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - forceAddSelect (fas): If set to true, together with -setAutoToggleSelection (see below) on the first selection set, causes the first selection after the computation of the previous result to be "shift" selection, unless a modifier key is pressed.  Default is
            false.Flags for each selection set.  These flags are multi-use.
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ignoreInvalidItems (iii): If you have multiple selection sets, the state of the selection set is recorded at the time you "complete it".  You could then delete some of the items in that list and end up with invalid items in one or more of your selection sets.  If
            this flag is set, those items will be detected and ignored.  You will never know it happened.  Its as if they were never selected in the first place, except that your selection set now does not have as many items as it may need.  If this
            flag is not set, you will get a warning and your final command callback script will likely not execute because of an error condition.
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lastAutoComplete (lac): True if auto complete is set for the last selection set, false otherwise.  Mostly used for query, but if present in conjuction with -sac/setAutoComplete flag, -sac flag takes precedence.
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
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
        - setAllowExcessCount (sae): If set, the number if items is to be interpreted as the minimum.
        - setAutoComplete (sac): If set to true, as soon as the specified number of items is selected the tool will start the next selection set or run the command.
        - setAutoToggleSelection (sat): If set to true, it is as if "shift" key is pressed when there are no modifiers pressed.  That means that you get the "toggle select" behaviour by default.  This only applies to the 3D view, and the selection done in the hypergraph, outliner
            or elsewhere is still a subject to the usual rules.
        - setDoneSelectionPrompt (dsp): If setAutoComplete is not set (see below) this string will be shown as soon as the tool has enough items for a particular selection set.  If this is not set, but is needed, the same string as set with -setSelectionPrompt flag will be used.
        - setNoSelectionHeadsUp (snh): Supply a string that will be shown as a heads up prompt when there is nothing selected.  This must be set separately for each selection set.
        - setNoSelectionPrompt (snp): Supply a string that will be shown as help when there is nothing selected.  This must be set separately for each selection set.
        - setSelectionCount (ssc): The number of items in this selection set.  0 means as many as you need until completion.
        - setSelectionHeadsUp (ssh): Supply a string that will be shown as a heads up prompt when there is something selected.  This must be set separately for each selection set.
        - setSelectionPrompt (ssp): Supply a string that will be shown as help when there is something selected.  This must be set separately for each selection set.
        - showManipulators (sm): If set, the manipulators will be shown for any active objects. Basically, it is as if you are in the Show Manipulator tool.
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
        - title (t): Supply a string that will be used as a precursor to all the messages; i.e., the "name" of the tool.
        - toolCursorType (tct): Supply the string identifier to set the tool cursor type when inside of tool. The following are the valid ids: "create", "dolly", "edit", "pencil", "track", "trackHorizontal", "trackVertical", "transformation", "tumble", "zoom", "zoomIn",
            "zoomOut", "flyThrough", "dot", "fleur", "leftArrow", "question", "doubleHorizArrow", "doubleVertArrow", "sizing", "dollyIn", "dollyOut", "brush", "camera", "noAccess", "input", "output", "leftCycle", "rightCycle", "rightExpand", "knife".
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
        - totalSelectionSets (tss): Total number of selection sets.
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
        - query (q): Query mode flag
    """
@overload #Overload for scriptCtx in ['edit']
def scriptCtx(string: str, allComponents: bool = ..., allObjects: bool = ..., animBreakdown: bool = ..., animCurve: bool = ..., animInTangent: bool = ..., animKeyframe: bool = ..., animOutTangent: bool = ..., baseClassName: str = ..., camera: bool = ..., cluster: bool = ..., collisionModel: bool = ..., controlVertex: bool = ..., cumulativeLists: bool = ..., curve: bool = ..., curveKnot: bool = ..., curveOnSurface: bool = ..., curveParameterPoint: bool = ..., dimension: bool = ..., dynamicConstraint: bool = ..., edge: bool = ..., editPoint: bool = ..., emitter: bool = ..., enableRootSelection: bool = ..., escToQuit: bool = ..., exitUponCompletion: bool = ..., expandSelectionList: bool = ..., facet: bool = ..., field: bool = ..., finalCommandScript: script = ..., fluid: bool = ..., follicle: bool = ..., forceAddSelect: bool = ..., hairSystem: bool = ..., handle: bool = ..., hull: bool = ..., ignoreInvalidItems: bool = ..., ikEndEffector: bool = ..., ikHandle: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., imagePlane: bool = ..., implicitGeometry: bool = ..., isoparm: bool = ..., joint: bool = ..., jointPivot: bool = ..., lastAutoComplete: bool = ..., lattice: bool = ..., latticePoint: bool = ..., light: bool = ..., localRotationAxis: bool = ..., locator: bool = ..., locatorUV: bool = ..., locatorXYZ: bool = ..., nCloth: bool = ..., nParticle: bool = ..., nParticleShape: bool = ..., nRigid: bool = ..., nonlinear: bool = ..., nurbsCurve: bool = ..., nurbsSurface: bool = ..., objectComponent: bool = ..., orientationLocator: bool = ..., particle: bool = ..., particleShape: bool = ..., plane: bool = ..., polymesh: bool = ..., polymeshEdge: bool = ..., polymeshFace: bool = ..., polymeshFreeEdge: bool = ..., polymeshUV: bool = ..., polymeshVertex: bool = ..., polymeshVtxFace: bool = ..., rigidBody: bool = ..., rigidConstraint: bool = ..., rotatePivot: bool = ..., scalePivot: bool = ..., sculpt: bool = ..., selectHandle: bool = ..., setAllowExcessCount: bool = ..., setAutoComplete: bool = ..., setAutoToggleSelection: bool = ..., setDoneSelectionPrompt: str = ..., setNoSelectionHeadsUp: str = ..., setNoSelectionPrompt: str = ..., setSelectionCount: int = ..., setSelectionHeadsUp: str = ..., setSelectionPrompt: str = ..., showManipulators: bool = ..., spring: bool = ..., springComponent: bool = ..., stroke: bool = ..., subdiv: bool = ..., subdivMeshEdge: bool = ..., subdivMeshFace: bool = ..., subdivMeshPoint: bool = ..., subdivMeshUV: bool = ..., surfaceEdge: bool = ..., surfaceFace: bool = ..., surfaceKnot: bool = ..., surfaceParameterPoint: bool = ..., surfaceRange: bool = ..., surfaceUV: bool = ..., texture: bool = ..., title: str = ..., toolCursorType: str = ..., toolFinish: script = ..., toolStart: script = ..., totalSelectionSets: int = ..., vertex: bool = ..., edit: bool = ...) -> str:
    """scriptCtx is undoable, queryable, and editable.
    
    This command allows a user to create their own tools based on the selection
    tool. A number of selection lists can be collected, the behaviour of the
    selection and the selection masks are fully customizable, etc.
    
    The command is processed prior to being executed. The keyword "$Selection#"
    where # is a number 1 or greater specifies a selection set. The context can
    specify several selection sets which are substituted in place of the
    $Selection# keyword in the form of a Mel string array. Items that are specific
    per set need to be specified in each set, if they are going to be specified
    for any of the sets. See examples below.
    
    In addition, in order to specify the type of selection you need to be making,
    any of the selection type flags from "selectType" command can be used here.

    ---
    - Args:
        - string: Input item(s).
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - baseClassName (bcn): This string will be used to produce MEL function names for the property sheets for the tool.  For example, if "myScriptTool" was given, the functions "myScriptToolValues" and "myScriptToolProperties" will be used for the property sheets.
            The default is "scriptTool".
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - cumulativeLists (cls): If set, the selection lists will be cumulative.  For example, the second list will contain all the items from the first list, the third all the items from the second list etc.  Make sure your script specified above takes that into account.
            Relevant if there is more than one selection set.
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - enableRootSelection (ers): If set, the items to be selected are at their root transform level. Default is false.
        - escToQuit (esc): If set to true, exit the tool when press "Esc". Default is false.
        - exitUponCompletion (euc): If set, completing the last selection set will exit the tool.  Default is true.
        - expandSelectionList (esl): If set, the selection lists will expand to have a single component in each item.  You probably want this as a default, otherwise two isoparms on the same surface will show up as 1 item.To ensure that components on the same object are
            returned in the order in which they are selected, use theselectPref -trackSelectionOrder oncommand in your-toolStartscript to enable ordered selection, then restore it to its original value in your-toolFinishscript.
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - finalCommandScript (fcs): Supply the script that will be run when the user presses the enter key and the context is completed.  Depending on the number of selection sets you have, the script can make use of variables string $Selection1[], $Selection2[], ...
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - forceAddSelect (fas): If set to true, together with -setAutoToggleSelection (see below) on the first selection set, causes the first selection after the computation of the previous result to be "shift" selection, unless a modifier key is pressed.  Default is
            false.Flags for each selection set.  These flags are multi-use.
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ignoreInvalidItems (iii): If you have multiple selection sets, the state of the selection set is recorded at the time you "complete it".  You could then delete some of the items in that list and end up with invalid items in one or more of your selection sets.  If
            this flag is set, those items will be detected and ignored.  You will never know it happened.  Its as if they were never selected in the first place, except that your selection set now does not have as many items as it may need.  If this
            flag is not set, you will get a warning and your final command callback script will likely not execute because of an error condition.
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lastAutoComplete (lac): True if auto complete is set for the last selection set, false otherwise.  Mostly used for query, but if present in conjuction with -sac/setAutoComplete flag, -sac flag takes precedence.
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
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
        - setAllowExcessCount (sae): If set, the number if items is to be interpreted as the minimum.
        - setAutoComplete (sac): If set to true, as soon as the specified number of items is selected the tool will start the next selection set or run the command.
        - setAutoToggleSelection (sat): If set to true, it is as if "shift" key is pressed when there are no modifiers pressed.  That means that you get the "toggle select" behaviour by default.  This only applies to the 3D view, and the selection done in the hypergraph, outliner
            or elsewhere is still a subject to the usual rules.
        - setDoneSelectionPrompt (dsp): If setAutoComplete is not set (see below) this string will be shown as soon as the tool has enough items for a particular selection set.  If this is not set, but is needed, the same string as set with -setSelectionPrompt flag will be used.
        - setNoSelectionHeadsUp (snh): Supply a string that will be shown as a heads up prompt when there is nothing selected.  This must be set separately for each selection set.
        - setNoSelectionPrompt (snp): Supply a string that will be shown as help when there is nothing selected.  This must be set separately for each selection set.
        - setSelectionCount (ssc): The number of items in this selection set.  0 means as many as you need until completion.
        - setSelectionHeadsUp (ssh): Supply a string that will be shown as a heads up prompt when there is something selected.  This must be set separately for each selection set.
        - setSelectionPrompt (ssp): Supply a string that will be shown as help when there is something selected.  This must be set separately for each selection set.
        - showManipulators (sm): If set, the manipulators will be shown for any active objects. Basically, it is as if you are in the Show Manipulator tool.
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
        - title (t): Supply a string that will be used as a precursor to all the messages; i.e., the "name" of the tool.
        - toolCursorType (tct): Supply the string identifier to set the tool cursor type when inside of tool. The following are the valid ids: "create", "dolly", "edit", "pencil", "track", "trackHorizontal", "trackVertical", "transformation", "tumble", "zoom", "zoomIn",
            "zoomOut", "flyThrough", "dot", "fleur", "leftArrow", "question", "doubleHorizArrow", "doubleVertArrow", "sizing", "dollyIn", "dollyOut", "brush", "camera", "noAccess", "input", "output", "leftCycle", "rightCycle", "rightExpand", "knife".
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
        - totalSelectionSets (tss): Total number of selection sets.
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
        - edit (e): Edit mode flag
    """
@overload #Overload for scriptCtx in ['edit']
def scriptCtx(string: str, alc: bool = ..., alo: bool = ..., abd: bool = ..., ac: bool = ..., ait: bool = ..., ak: bool = ..., aot: bool = ..., bcn: str = ..., ca: bool = ..., cl: bool = ..., clm: bool = ..., cv: bool = ..., cls: bool = ..., c: bool = ..., ck: bool = ..., cos: bool = ..., cpp: bool = ..., dim: bool = ..., dc: bool = ..., eg: bool = ..., ep: bool = ..., em: bool = ..., ers: bool = ..., esc: bool = ..., euc: bool = ..., esl: bool = ..., fc: bool = ..., fi: bool = ..., fcs: script = ..., fl: bool = ..., fo: bool = ..., fas: bool = ..., hs: bool = ..., ha: bool = ..., hl: bool = ..., iii: bool = ..., iee: bool = ..., ikh: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ip: bool = ..., ig: bool = ..., iso: bool = ..., j: bool = ..., jp: bool = ..., lac: bool = ..., la: bool = ..., lp: bool = ..., lt: bool = ..., ra: bool = ..., lc: bool = ..., luv: bool = ..., xyz: bool = ..., ncl: bool = ..., npr: bool = ..., nps: bool = ..., nr: bool = ..., nl: bool = ..., nc: bool = ..., ns: bool = ..., ocm: bool = ..., ol: bool = ..., pr: bool = ..., ps: bool = ..., pl: bool = ..., p: bool = ..., pe: bool = ..., pf: bool = ..., pfe: bool = ..., puv: bool = ..., pv: bool = ..., pvf: bool = ..., rb: bool = ..., rc: bool = ..., rp: bool = ..., sp: bool = ..., sc: bool = ..., sh: bool = ..., sae: bool = ..., sac: bool = ..., sat: bool = ..., dsp: str = ..., snh: str = ..., snp: str = ..., ssc: int = ..., ssh: str = ..., ssp: str = ..., sm: bool = ..., spr: bool = ..., spc: bool = ..., str: bool = ..., sd: bool = ..., sme: bool = ..., smf: bool = ..., smp: bool = ..., smu: bool = ..., se: bool = ..., sf: bool = ..., sk: bool = ..., spp: bool = ..., sr: bool = ..., suv: bool = ..., tx: bool = ..., t: str = ..., tct: str = ..., tf: script = ..., ts: script = ..., tss: int = ..., v: bool = ..., e: bool = ...) -> str:
    """scriptCtx is undoable, queryable, and editable.
    
    This command allows a user to create their own tools based on the selection
    tool. A number of selection lists can be collected, the behaviour of the
    selection and the selection masks are fully customizable, etc.
    
    The command is processed prior to being executed. The keyword "$Selection#"
    where # is a number 1 or greater specifies a selection set. The context can
    specify several selection sets which are substituted in place of the
    $Selection# keyword in the form of a Mel string array. Items that are specific
    per set need to be specified in each set, if they are going to be specified
    for any of the sets. See examples below.
    
    In addition, in order to specify the type of selection you need to be making,
    any of the selection type flags from "selectType" command can be used here.

    ---
    - Args:
        - string: Input item(s).
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - baseClassName (bcn): This string will be used to produce MEL function names for the property sheets for the tool.  For example, if "myScriptTool" was given, the functions "myScriptToolValues" and "myScriptToolProperties" will be used for the property sheets.
            The default is "scriptTool".
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - cumulativeLists (cls): If set, the selection lists will be cumulative.  For example, the second list will contain all the items from the first list, the third all the items from the second list etc.  Make sure your script specified above takes that into account.
            Relevant if there is more than one selection set.
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - enableRootSelection (ers): If set, the items to be selected are at their root transform level. Default is false.
        - escToQuit (esc): If set to true, exit the tool when press "Esc". Default is false.
        - exitUponCompletion (euc): If set, completing the last selection set will exit the tool.  Default is true.
        - expandSelectionList (esl): If set, the selection lists will expand to have a single component in each item.  You probably want this as a default, otherwise two isoparms on the same surface will show up as 1 item.To ensure that components on the same object are
            returned in the order in which they are selected, use theselectPref -trackSelectionOrder oncommand in your-toolStartscript to enable ordered selection, then restore it to its original value in your-toolFinishscript.
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - finalCommandScript (fcs): Supply the script that will be run when the user presses the enter key and the context is completed.  Depending on the number of selection sets you have, the script can make use of variables string $Selection1[], $Selection2[], ...
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - forceAddSelect (fas): If set to true, together with -setAutoToggleSelection (see below) on the first selection set, causes the first selection after the computation of the previous result to be "shift" selection, unless a modifier key is pressed.  Default is
            false.Flags for each selection set.  These flags are multi-use.
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ignoreInvalidItems (iii): If you have multiple selection sets, the state of the selection set is recorded at the time you "complete it".  You could then delete some of the items in that list and end up with invalid items in one or more of your selection sets.  If
            this flag is set, those items will be detected and ignored.  You will never know it happened.  Its as if they were never selected in the first place, except that your selection set now does not have as many items as it may need.  If this
            flag is not set, you will get a warning and your final command callback script will likely not execute because of an error condition.
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lastAutoComplete (lac): True if auto complete is set for the last selection set, false otherwise.  Mostly used for query, but if present in conjuction with -sac/setAutoComplete flag, -sac flag takes precedence.
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
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
        - setAllowExcessCount (sae): If set, the number if items is to be interpreted as the minimum.
        - setAutoComplete (sac): If set to true, as soon as the specified number of items is selected the tool will start the next selection set or run the command.
        - setAutoToggleSelection (sat): If set to true, it is as if "shift" key is pressed when there are no modifiers pressed.  That means that you get the "toggle select" behaviour by default.  This only applies to the 3D view, and the selection done in the hypergraph, outliner
            or elsewhere is still a subject to the usual rules.
        - setDoneSelectionPrompt (dsp): If setAutoComplete is not set (see below) this string will be shown as soon as the tool has enough items for a particular selection set.  If this is not set, but is needed, the same string as set with -setSelectionPrompt flag will be used.
        - setNoSelectionHeadsUp (snh): Supply a string that will be shown as a heads up prompt when there is nothing selected.  This must be set separately for each selection set.
        - setNoSelectionPrompt (snp): Supply a string that will be shown as help when there is nothing selected.  This must be set separately for each selection set.
        - setSelectionCount (ssc): The number of items in this selection set.  0 means as many as you need until completion.
        - setSelectionHeadsUp (ssh): Supply a string that will be shown as a heads up prompt when there is something selected.  This must be set separately for each selection set.
        - setSelectionPrompt (ssp): Supply a string that will be shown as help when there is something selected.  This must be set separately for each selection set.
        - showManipulators (sm): If set, the manipulators will be shown for any active objects. Basically, it is as if you are in the Show Manipulator tool.
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
        - title (t): Supply a string that will be used as a precursor to all the messages; i.e., the "name" of the tool.
        - toolCursorType (tct): Supply the string identifier to set the tool cursor type when inside of tool. The following are the valid ids: "create", "dolly", "edit", "pencil", "track", "trackHorizontal", "trackVertical", "transformation", "tumble", "zoom", "zoomIn",
            "zoomOut", "flyThrough", "dot", "fleur", "leftArrow", "question", "doubleHorizArrow", "doubleVertArrow", "sizing", "dollyIn", "dollyOut", "brush", "camera", "noAccess", "input", "output", "leftCycle", "rightCycle", "rightExpand", "knife".
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
        - totalSelectionSets (tss): Total number of selection sets.
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
        - edit (e): Edit mode flag
    """
@overload #Overload for scriptCtx in ['edit']
def scriptCtx(string: str, allComponents: bool = ..., alc: bool = ..., allObjects: bool = ..., alo: bool = ..., animBreakdown: bool = ..., abd: bool = ..., animCurve: bool = ..., ac: bool = ..., animInTangent: bool = ..., ait: bool = ..., animKeyframe: bool = ..., ak: bool = ..., animOutTangent: bool = ..., aot: bool = ..., baseClassName: str = ..., bcn: str = ..., camera: bool = ..., ca: bool = ..., cluster: bool = ..., cl: bool = ..., collisionModel: bool = ..., clm: bool = ..., controlVertex: bool = ..., cv: bool = ..., cumulativeLists: bool = ..., cls: bool = ..., curve: bool = ..., c: bool = ..., curveKnot: bool = ..., ck: bool = ..., curveOnSurface: bool = ..., cos: bool = ..., curveParameterPoint: bool = ..., cpp: bool = ..., dimension: bool = ..., dim: bool = ..., dynamicConstraint: bool = ..., dc: bool = ..., edge: bool = ..., eg: bool = ..., editPoint: bool = ..., ep: bool = ..., emitter: bool = ..., em: bool = ..., enableRootSelection: bool = ..., ers: bool = ..., escToQuit: bool = ..., esc: bool = ..., exitUponCompletion: bool = ..., euc: bool = ..., expandSelectionList: bool = ..., esl: bool = ..., facet: bool = ..., fc: bool = ..., field: bool = ..., fi: bool = ..., finalCommandScript: script = ..., fcs: script = ..., fluid: bool = ..., fl: bool = ..., follicle: bool = ..., fo: bool = ..., forceAddSelect: bool = ..., fas: bool = ..., hairSystem: bool = ..., hs: bool = ..., handle: bool = ..., ha: bool = ..., hull: bool = ..., hl: bool = ..., ignoreInvalidItems: bool = ..., iii: bool = ..., ikEndEffector: bool = ..., iee: bool = ..., ikHandle: bool = ..., ikh: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., imagePlane: bool = ..., ip: bool = ..., implicitGeometry: bool = ..., ig: bool = ..., isoparm: bool = ..., iso: bool = ..., joint: bool = ..., j: bool = ..., jointPivot: bool = ..., jp: bool = ..., lastAutoComplete: bool = ..., lac: bool = ..., lattice: bool = ..., la: bool = ..., latticePoint: bool = ..., lp: bool = ..., light: bool = ..., lt: bool = ..., localRotationAxis: bool = ..., ra: bool = ..., locator: bool = ..., lc: bool = ..., locatorUV: bool = ..., luv: bool = ..., locatorXYZ: bool = ..., xyz: bool = ..., nCloth: bool = ..., ncl: bool = ..., nParticle: bool = ..., npr: bool = ..., nParticleShape: bool = ..., nps: bool = ..., nRigid: bool = ..., nr: bool = ..., nonlinear: bool = ..., nl: bool = ..., nurbsCurve: bool = ..., nc: bool = ..., nurbsSurface: bool = ..., ns: bool = ..., objectComponent: bool = ..., ocm: bool = ..., orientationLocator: bool = ..., ol: bool = ..., particle: bool = ..., pr: bool = ..., particleShape: bool = ..., ps: bool = ..., plane: bool = ..., pl: bool = ..., polymesh: bool = ..., p: bool = ..., polymeshEdge: bool = ..., pe: bool = ..., polymeshFace: bool = ..., pf: bool = ..., polymeshFreeEdge: bool = ..., pfe: bool = ..., polymeshUV: bool = ..., puv: bool = ..., polymeshVertex: bool = ..., pv: bool = ..., polymeshVtxFace: bool = ..., pvf: bool = ..., rigidBody: bool = ..., rb: bool = ..., rigidConstraint: bool = ..., rc: bool = ..., rotatePivot: bool = ..., rp: bool = ..., scalePivot: bool = ..., sp: bool = ..., sculpt: bool = ..., sc: bool = ..., selectHandle: bool = ..., sh: bool = ..., setAllowExcessCount: bool = ..., sae: bool = ..., setAutoComplete: bool = ..., sac: bool = ..., setAutoToggleSelection: bool = ..., sat: bool = ..., setDoneSelectionPrompt: str = ..., dsp: str = ..., setNoSelectionHeadsUp: str = ..., snh: str = ..., setNoSelectionPrompt: str = ..., snp: str = ..., setSelectionCount: int = ..., ssc: int = ..., setSelectionHeadsUp: str = ..., ssh: str = ..., setSelectionPrompt: str = ..., ssp: str = ..., showManipulators: bool = ..., sm: bool = ..., spring: bool = ..., spr: bool = ..., springComponent: bool = ..., spc: bool = ..., stroke: bool = ..., str: bool = ..., subdiv: bool = ..., sd: bool = ..., subdivMeshEdge: bool = ..., sme: bool = ..., subdivMeshFace: bool = ..., smf: bool = ..., subdivMeshPoint: bool = ..., smp: bool = ..., subdivMeshUV: bool = ..., smu: bool = ..., surfaceEdge: bool = ..., se: bool = ..., surfaceFace: bool = ..., sf: bool = ..., surfaceKnot: bool = ..., sk: bool = ..., surfaceParameterPoint: bool = ..., spp: bool = ..., surfaceRange: bool = ..., sr: bool = ..., surfaceUV: bool = ..., suv: bool = ..., texture: bool = ..., tx: bool = ..., title: str = ..., t: str = ..., toolCursorType: str = ..., tct: str = ..., toolFinish: script = ..., tf: script = ..., toolStart: script = ..., ts: script = ..., totalSelectionSets: int = ..., tss: int = ..., vertex: bool = ..., v: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """scriptCtx is undoable, queryable, and editable.
    
    This command allows a user to create their own tools based on the selection
    tool. A number of selection lists can be collected, the behaviour of the
    selection and the selection masks are fully customizable, etc.
    
    The command is processed prior to being executed. The keyword "$Selection#"
    where # is a number 1 or greater specifies a selection set. The context can
    specify several selection sets which are substituted in place of the
    $Selection# keyword in the form of a Mel string array. Items that are specific
    per set need to be specified in each set, if they are going to be specified
    for any of the sets. See examples below.
    
    In addition, in order to specify the type of selection you need to be making,
    any of the selection type flags from "selectType" command can be used here.

    ---
    - Args:
        - string: Input item(s).
        - allComponents (alc): Set all component selection masks on/off
        - allObjects (alo): Set all object selection masks on/off
        - animBreakdown (abd): Set animation breakdown selection mask on/off.
        - animCurve (ac): Set animation curve selection mask on/off.
        - animInTangent (ait): Set animation in-tangent selection mask on/off.
        - animKeyframe (ak): Set animation keyframe selection mask on/off.
        - animOutTangent (aot): Set animation out-tangent selection mask on/off.
        - baseClassName (bcn): This string will be used to produce MEL function names for the property sheets for the tool.  For example, if "myScriptTool" was given, the functions "myScriptToolValues" and "myScriptToolProperties" will be used for the property sheets.
            The default is "scriptTool".
        - camera (ca): Set camera selection mask on/off. (object flag)
        - cluster (cl): Set cluster selection mask on/off. (object flag)
        - collisionModel (clm): Set collision model selection mask on/off. (object flag)
        - controlVertex (cv): Set control vertex selection mask on/off. (component flag)
        - cumulativeLists (cls): If set, the selection lists will be cumulative.  For example, the second list will contain all the items from the first list, the third all the items from the second list etc.  Make sure your script specified above takes that into account.
            Relevant if there is more than one selection set.
        - curve (c): Set curve selection mask on/off. (object flag)
        - curveKnot (ck): Set curve knot selection mask on/off. (component flag)
        - curveOnSurface (cos): Set curve-on-surface selection mask on/off. (object flag)
        - curveParameterPoint (cpp): Set curve parameter point selection mask on/off. (component flag)
        - dimension (dim): Set dimension shape selection mask on/off. (object flag)
        - dynamicConstraint (dc): Set dynamicConstraint selection mask on/off. (object flag)
        - edge (eg): Set mesh edge selection mask on/off. (component flag)
        - editPoint (ep): Set edit-point selection mask on/off. (component flag)
        - emitter (em): Set emitter selection mask on/off. (object flag)
        - enableRootSelection (ers): If set, the items to be selected are at their root transform level. Default is false.
        - escToQuit (esc): If set to true, exit the tool when press "Esc". Default is false.
        - exitUponCompletion (euc): If set, completing the last selection set will exit the tool.  Default is true.
        - expandSelectionList (esl): If set, the selection lists will expand to have a single component in each item.  You probably want this as a default, otherwise two isoparms on the same surface will show up as 1 item.To ensure that components on the same object are
            returned in the order in which they are selected, use theselectPref -trackSelectionOrder oncommand in your-toolStartscript to enable ordered selection, then restore it to its original value in your-toolFinishscript.
        - facet (fc): Set mesh face selection mask on/off. (component flag)
        - field (fi): Set field selection mask on/off. (object flag)
        - finalCommandScript (fcs): Supply the script that will be run when the user presses the enter key and the context is completed.  Depending on the number of selection sets you have, the script can make use of variables string $Selection1[], $Selection2[], ...
        - fluid (fl): Set fluid selection mask on/off. (object flag)
        - follicle (fo): Set follicle selection mask on/off. (object flag)
        - forceAddSelect (fas): If set to true, together with -setAutoToggleSelection (see below) on the first selection set, causes the first selection after the computation of the previous result to be "shift" selection, unless a modifier key is pressed.  Default is
            false.Flags for each selection set.  These flags are multi-use.
        - hairSystem (hs): Set hairSystem selection mask on/off. (object flag)
        - handle (ha): Set object handle selection mask on/off. (object flag)
        - hull (hl): Set hull selection mask on/off. (component flag)
        - ignoreInvalidItems (iii): If you have multiple selection sets, the state of the selection set is recorded at the time you "complete it".  You could then delete some of the items in that list and end up with invalid items in one or more of your selection sets.  If
            this flag is set, those items will be detected and ignored.  You will never know it happened.  Its as if they were never selected in the first place, except that your selection set now does not have as many items as it may need.  If this
            flag is not set, you will get a warning and your final command callback script will likely not execute because of an error condition.
        - ikEndEffector (iee): Set ik end effector selection mask on/off. (object flag)
        - ikHandle (ikh): Set ik handle selection mask on/off. (object flag)
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - imagePlane (ip): Set image plane selection mask on/off. (component flag)
        - implicitGeometry (ig): Set implicit geometry selection mask on/off. (object flag)
        - isoparm (iso): Set surface iso-parm selection mask on/off. (component flag)
        - joint (j): Set ik handle selection mask on/off. (object flag)
        - jointPivot (jp): Set joint pivot selection mask on/off. (component flag)
        - lastAutoComplete (lac): True if auto complete is set for the last selection set, false otherwise.  Mostly used for query, but if present in conjuction with -sac/setAutoComplete flag, -sac flag takes precedence.
        - lattice (la): Set lattice selection mask on/off. (object flag)
        - latticePoint (lp): Set lattice point selection mask on/off. (component flag)
        - light (lt): Set light selection mask on/off. (object flag)
        - localRotationAxis (ra): Set local rotation axis selection mask on/off. (component flag)
        - locator (lc): Set locator (all types) selection mask on/off. (object flag)
        - locatorUV (luv): Set uv locator selection mask on/off. (object flag)
        - locatorXYZ (xyz): Set xyz locator selection mask on/off. (object flag)
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
        - setAllowExcessCount (sae): If set, the number if items is to be interpreted as the minimum.
        - setAutoComplete (sac): If set to true, as soon as the specified number of items is selected the tool will start the next selection set or run the command.
        - setAutoToggleSelection (sat): If set to true, it is as if "shift" key is pressed when there are no modifiers pressed.  That means that you get the "toggle select" behaviour by default.  This only applies to the 3D view, and the selection done in the hypergraph, outliner
            or elsewhere is still a subject to the usual rules.
        - setDoneSelectionPrompt (dsp): If setAutoComplete is not set (see below) this string will be shown as soon as the tool has enough items for a particular selection set.  If this is not set, but is needed, the same string as set with -setSelectionPrompt flag will be used.
        - setNoSelectionHeadsUp (snh): Supply a string that will be shown as a heads up prompt when there is nothing selected.  This must be set separately for each selection set.
        - setNoSelectionPrompt (snp): Supply a string that will be shown as help when there is nothing selected.  This must be set separately for each selection set.
        - setSelectionCount (ssc): The number of items in this selection set.  0 means as many as you need until completion.
        - setSelectionHeadsUp (ssh): Supply a string that will be shown as a heads up prompt when there is something selected.  This must be set separately for each selection set.
        - setSelectionPrompt (ssp): Supply a string that will be shown as help when there is something selected.  This must be set separately for each selection set.
        - showManipulators (sm): If set, the manipulators will be shown for any active objects. Basically, it is as if you are in the Show Manipulator tool.
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
        - title (t): Supply a string that will be used as a precursor to all the messages; i.e., the "name" of the tool.
        - toolCursorType (tct): Supply the string identifier to set the tool cursor type when inside of tool. The following are the valid ids: "create", "dolly", "edit", "pencil", "track", "trackHorizontal", "trackVertical", "transformation", "tumble", "zoom", "zoomIn",
            "zoomOut", "flyThrough", "dot", "fleur", "leftArrow", "question", "doubleHorizArrow", "doubleVertArrow", "sizing", "dollyIn", "dollyOut", "brush", "camera", "noAccess", "input", "output", "leftCycle", "rightCycle", "rightExpand", "knife".
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
        - totalSelectionSets (tss): Total number of selection sets.
        - vertex (v): Set mesh vertex selection mask on/off. (component flag)
        - edit (e): Edit mode flag
    """
