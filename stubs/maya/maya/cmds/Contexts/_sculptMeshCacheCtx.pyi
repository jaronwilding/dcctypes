"""Stub files for Contexts category in Maya commands, command: sculptMeshCacheCtx."""

from typing import Any, overload

@overload #Overload for sculptMeshCacheCtx in ['create']
def sculptMeshCacheCtx(affectAllLayers: bool = ..., cloneHideSource: bool = ..., cloneMethod: int = ..., cloneShapeSource: str = ..., cloneTargetSource: str = ..., constrainToSurface: bool = ..., displayFrozen: bool = ..., displayMask: bool = ..., displayWireframe: bool = ..., flood: float = ..., floodFreeze: float = ..., frame: bool = ..., freezeSelection: bool = ..., grabFollowPath: bool = ..., grabSilhouette: bool = ..., grabTwist: bool = ..., inverted: bool = ..., lockShellBorder: bool = ..., orientToSurface: bool = ..., stampFlipX: bool = ..., stampFlipY: bool = ..., stampOrientToStroke: bool = ..., stampRandomization: bool = ..., stampRandomizeFlipX: bool = ..., stampRandomizeFlipY: bool = ..., updatePlane: bool = ..., useGlobalSize: bool = ..., useScreenSpace: bool = ..., useStampDistance: bool = ..., useStampImage: bool = ..., useSteadyStroke: bool = ..., wholeStroke: bool = ..., wireframeAlpha: float = ..., wireframeColor: [float, float, float] = ...) -> None:
    """sculptMeshCacheCtx is undoable, queryable, and editable.
    
    This is a tool context command for mesh cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext')
        cmds.setToolTo('sculptMeshCacheContext')
        # Set sculptMeshCacheContext's brush size to 10.0
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext', edit=True, sz=10.0)
    ```

    ---
    - Args:
        - affectAllLayers (aal): If true, the brush affects all layers at once.
        - cloneHideSource (chs): True if the cloned source should be hidden.
        - cloneMethod (cm): Controls how the source delta vectors should change the target. 0=copy 1=add
        - cloneShapeSource (css): Name of the shape source to clone.
        - cloneTargetSource (cas): Name of the target source of the clone.
        - constrainToSurface (cts): If true, the modification keeps the surface curvature.
        - displayFrozen (df): If false, turns off the display of frozen area on the object.
        - displayMask (dm): If false, turns off the display of masked area on the object.
        - displayWireframe (dw): If false, turns off the wireframe display of the object.
        - flood (fl): Sets the brush effect for each vertex to the given value.
        - floodFreeze (ff): Sets the freeze value for each vertex to the given value.
        - frame (frm): Frames on the sculpted area.
        - freezeSelection (fsl): Freezes selected components.
        - grabFollowPath (gfp): If true, the grab brush effect follows mouse movement.
        - grabSilhouette (gs): If true, the grab brush uses paint-through mode.
        - grabTwist (gtw): If true, the grab brush twists the vertices.
        - inverted (inv): If true, inverts the effect of the brush.
        - lockShellBorder (lsb): Lock the shell borders so that they won't be moved by a UV texture brush.
        - orientToSurface (ots): If true, aligns the brush display to the surface of the mesh.
        - stampFlipX (sfx): Specifies if the brush stamp is flipped on the X axis.
        - stampFlipY (sfy): Specifies if the brush stamp is flipped on the Y axis.
        - stampOrientToStroke (sos): Specifies if the brush stamp is aligned to the stroke direction.
        - stampRandomization (srd): Specifies if the brush stamp is randomized.
        - stampRandomizeFlipX (srx): Specifies if the brush stamp flipping is randomized on the X axis.
        - stampRandomizeFlipY (sry): Specifies if the brush stamp flipping is randomized on the Y axis.
        - updatePlane (upl): Recalculates the underlying tool plane for each stamp in a stroke.
        - useGlobalSize (ugs): If true, all the brushes have a shared size property; otherwise size is local.
        - useScreenSpace (ssp): If true, the brush size is in screen space pixels.
        - useStampDistance (usd): Force the stamps to be spread out along the stroke, rather than building up continually.
        - useStampImage (usi): Specifies if the brush uses a stamp image.
        - useSteadyStroke (uss): Turns using steady stroke on/off.
        - wholeStroke (wst): Continuously recalculates the underlying tool plane from all the vertices affected during the stroke.
        - wireframeAlpha (wa): Sets the alpha value of the wireframe for the object that is being sculpted.
        - wireframeColor (wc): Sets the color of the wireframe for the object that is being sculpted. Values should be 0-1 RGB.
    """
@overload #Overload for sculptMeshCacheCtx in ['create']
def sculptMeshCacheCtx(aal: bool = ..., chs: bool = ..., cm: int = ..., css: str = ..., cas: str = ..., cts: bool = ..., df: bool = ..., dm: bool = ..., dw: bool = ..., fl: float = ..., ff: float = ..., frm: bool = ..., fsl: bool = ..., gfp: bool = ..., gs: bool = ..., gtw: bool = ..., inv: bool = ..., lsb: bool = ..., ots: bool = ..., sfx: bool = ..., sfy: bool = ..., sos: bool = ..., srd: bool = ..., srx: bool = ..., sry: bool = ..., upl: bool = ..., ugs: bool = ..., ssp: bool = ..., usd: bool = ..., usi: bool = ..., uss: bool = ..., wst: bool = ..., wa: float = ..., wc: [float, float, float] = ...) -> None:
    """sculptMeshCacheCtx is undoable, queryable, and editable.
    
    This is a tool context command for mesh cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext')
        cmds.setToolTo('sculptMeshCacheContext')
        # Set sculptMeshCacheContext's brush size to 10.0
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext', edit=True, sz=10.0)
    ```

    ---
    - Args:
        - affectAllLayers (aal): If true, the brush affects all layers at once.
        - cloneHideSource (chs): True if the cloned source should be hidden.
        - cloneMethod (cm): Controls how the source delta vectors should change the target. 0=copy 1=add
        - cloneShapeSource (css): Name of the shape source to clone.
        - cloneTargetSource (cas): Name of the target source of the clone.
        - constrainToSurface (cts): If true, the modification keeps the surface curvature.
        - displayFrozen (df): If false, turns off the display of frozen area on the object.
        - displayMask (dm): If false, turns off the display of masked area on the object.
        - displayWireframe (dw): If false, turns off the wireframe display of the object.
        - flood (fl): Sets the brush effect for each vertex to the given value.
        - floodFreeze (ff): Sets the freeze value for each vertex to the given value.
        - frame (frm): Frames on the sculpted area.
        - freezeSelection (fsl): Freezes selected components.
        - grabFollowPath (gfp): If true, the grab brush effect follows mouse movement.
        - grabSilhouette (gs): If true, the grab brush uses paint-through mode.
        - grabTwist (gtw): If true, the grab brush twists the vertices.
        - inverted (inv): If true, inverts the effect of the brush.
        - lockShellBorder (lsb): Lock the shell borders so that they won't be moved by a UV texture brush.
        - orientToSurface (ots): If true, aligns the brush display to the surface of the mesh.
        - stampFlipX (sfx): Specifies if the brush stamp is flipped on the X axis.
        - stampFlipY (sfy): Specifies if the brush stamp is flipped on the Y axis.
        - stampOrientToStroke (sos): Specifies if the brush stamp is aligned to the stroke direction.
        - stampRandomization (srd): Specifies if the brush stamp is randomized.
        - stampRandomizeFlipX (srx): Specifies if the brush stamp flipping is randomized on the X axis.
        - stampRandomizeFlipY (sry): Specifies if the brush stamp flipping is randomized on the Y axis.
        - updatePlane (upl): Recalculates the underlying tool plane for each stamp in a stroke.
        - useGlobalSize (ugs): If true, all the brushes have a shared size property; otherwise size is local.
        - useScreenSpace (ssp): If true, the brush size is in screen space pixels.
        - useStampDistance (usd): Force the stamps to be spread out along the stroke, rather than building up continually.
        - useStampImage (usi): Specifies if the brush uses a stamp image.
        - useSteadyStroke (uss): Turns using steady stroke on/off.
        - wholeStroke (wst): Continuously recalculates the underlying tool plane from all the vertices affected during the stroke.
        - wireframeAlpha (wa): Sets the alpha value of the wireframe for the object that is being sculpted.
        - wireframeColor (wc): Sets the color of the wireframe for the object that is being sculpted. Values should be 0-1 RGB.
    """
@overload #Overload for sculptMeshCacheCtx in ['create']
def sculptMeshCacheCtx(affectAllLayers: bool = ..., aal: bool = ..., cloneHideSource: bool = ..., chs: bool = ..., cloneMethod: int = ..., cm: int = ..., cloneShapeSource: str = ..., css: str = ..., cloneTargetSource: str = ..., cas: str = ..., constrainToSurface: bool = ..., cts: bool = ..., displayFrozen: bool = ..., df: bool = ..., displayMask: bool = ..., dm: bool = ..., displayWireframe: bool = ..., dw: bool = ..., flood: float = ..., fl: float = ..., floodFreeze: float = ..., ff: float = ..., frame: bool = ..., frm: bool = ..., freezeSelection: bool = ..., fsl: bool = ..., grabFollowPath: bool = ..., gfp: bool = ..., grabSilhouette: bool = ..., gs: bool = ..., grabTwist: bool = ..., gtw: bool = ..., inverted: bool = ..., inv: bool = ..., lockShellBorder: bool = ..., lsb: bool = ..., orientToSurface: bool = ..., ots: bool = ..., stampFlipX: bool = ..., sfx: bool = ..., stampFlipY: bool = ..., sfy: bool = ..., stampOrientToStroke: bool = ..., sos: bool = ..., stampRandomization: bool = ..., srd: bool = ..., stampRandomizeFlipX: bool = ..., srx: bool = ..., stampRandomizeFlipY: bool = ..., sry: bool = ..., updatePlane: bool = ..., upl: bool = ..., useGlobalSize: bool = ..., ugs: bool = ..., useScreenSpace: bool = ..., ssp: bool = ..., useStampDistance: bool = ..., usd: bool = ..., useStampImage: bool = ..., usi: bool = ..., useSteadyStroke: bool = ..., uss: bool = ..., wholeStroke: bool = ..., wst: bool = ..., wireframeAlpha: float = ..., wa: float = ..., wireframeColor: [float, float, float] = ..., wc: [float, float, float] = ...) -> None:
    """sculptMeshCacheCtx is undoable, queryable, and editable.
    
    This is a tool context command for mesh cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext')
        cmds.setToolTo('sculptMeshCacheContext')
        # Set sculptMeshCacheContext's brush size to 10.0
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext', edit=True, sz=10.0)
    ```

    ---
    - Args:
        - affectAllLayers (aal): If true, the brush affects all layers at once.
        - cloneHideSource (chs): True if the cloned source should be hidden.
        - cloneMethod (cm): Controls how the source delta vectors should change the target. 0=copy 1=add
        - cloneShapeSource (css): Name of the shape source to clone.
        - cloneTargetSource (cas): Name of the target source of the clone.
        - constrainToSurface (cts): If true, the modification keeps the surface curvature.
        - displayFrozen (df): If false, turns off the display of frozen area on the object.
        - displayMask (dm): If false, turns off the display of masked area on the object.
        - displayWireframe (dw): If false, turns off the wireframe display of the object.
        - flood (fl): Sets the brush effect for each vertex to the given value.
        - floodFreeze (ff): Sets the freeze value for each vertex to the given value.
        - frame (frm): Frames on the sculpted area.
        - freezeSelection (fsl): Freezes selected components.
        - grabFollowPath (gfp): If true, the grab brush effect follows mouse movement.
        - grabSilhouette (gs): If true, the grab brush uses paint-through mode.
        - grabTwist (gtw): If true, the grab brush twists the vertices.
        - inverted (inv): If true, inverts the effect of the brush.
        - lockShellBorder (lsb): Lock the shell borders so that they won't be moved by a UV texture brush.
        - orientToSurface (ots): If true, aligns the brush display to the surface of the mesh.
        - stampFlipX (sfx): Specifies if the brush stamp is flipped on the X axis.
        - stampFlipY (sfy): Specifies if the brush stamp is flipped on the Y axis.
        - stampOrientToStroke (sos): Specifies if the brush stamp is aligned to the stroke direction.
        - stampRandomization (srd): Specifies if the brush stamp is randomized.
        - stampRandomizeFlipX (srx): Specifies if the brush stamp flipping is randomized on the X axis.
        - stampRandomizeFlipY (sry): Specifies if the brush stamp flipping is randomized on the Y axis.
        - updatePlane (upl): Recalculates the underlying tool plane for each stamp in a stroke.
        - useGlobalSize (ugs): If true, all the brushes have a shared size property; otherwise size is local.
        - useScreenSpace (ssp): If true, the brush size is in screen space pixels.
        - useStampDistance (usd): Force the stamps to be spread out along the stroke, rather than building up continually.
        - useStampImage (usi): Specifies if the brush uses a stamp image.
        - useSteadyStroke (uss): Turns using steady stroke on/off.
        - wholeStroke (wst): Continuously recalculates the underlying tool plane from all the vertices affected during the stroke.
        - wireframeAlpha (wa): Sets the alpha value of the wireframe for the object that is being sculpted.
        - wireframeColor (wc): Sets the color of the wireframe for the object that is being sculpted. Values should be 0-1 RGB.
    """
@overload #Overload for sculptMeshCacheCtx in ['query']
def sculptMeshCacheCtx(affectAllLayers: bool = ..., brushDirection: int = ..., brushSize: float = ..., brushStrength: float = ..., buildUpRate: float = ..., cloneHideSource: bool = ..., cloneMethod: int = ..., cloneShapeSource: str = ..., cloneTargetSource: str = ..., constrainToSurface: bool = ..., direction: int = ..., displayFrozen: bool = ..., displayMask: bool = ..., displayWireframe: bool = ..., falloffType: int = ..., grabFollowPath: bool = ..., grabSilhouette: bool = ..., grabTwist: bool = ..., inverted: bool = ..., lastMode: str = ..., lockShellBorder: bool = ..., minSize: float = ..., minStrength: float = ..., mirror: int = ..., mode: str = ..., orientToSurface: bool = ..., recordStroke: bool = ..., sculptFalloffCurve: str = ..., size: float = ..., stampDistance: float = ..., stampFile: str = ..., stampFlipX: bool = ..., stampFlipY: bool = ..., stampOrientToStroke: bool = ..., stampPlacement: int = ..., stampRandomization: bool = ..., stampRandomizeFlipX: bool = ..., stampRandomizeFlipY: bool = ..., stampRandomizePosX: float = ..., stampRandomizePosY: float = ..., stampRandomizeRotation: float = ..., stampRandomizeScale: float = ..., stampRandomizeStrength: float = ..., stampRotation: float = ..., steadyStrokeDistance: float = ..., strength: float = ..., updatePlane: bool = ..., useGlobalSize: bool = ..., useScreenSpace: bool = ..., useStampDistance: bool = ..., useStampImage: bool = ..., useSteadyStroke: bool = ..., wholeStroke: bool = ..., wireframeAlpha: float = ..., wireframeColor: [float, float, float] = ..., query: bool = ...) -> None:
    """sculptMeshCacheCtx is undoable, queryable, and editable.
    
    This is a tool context command for mesh cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext')
        cmds.setToolTo('sculptMeshCacheContext')
        # Set sculptMeshCacheContext's brush size to 10.0
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext', edit=True, sz=10.0)
    ```

    ---
    - Args:
        - affectAllLayers (aal): If true, the brush affects all layers at once.
        - brushDirection (bd): Specifies the direction of the named brush.
        - brushSize (bsz): Specifies the world-space size of the named brush.
        - brushStrength (bst): Specifies the world-space strength of the named brush.
        - buildUpRate (bur): Specifies the brush strength increasing along the stroke.
        - cloneHideSource (chs): True if the cloned source should be hidden.
        - cloneMethod (cm): Controls how the source delta vectors should change the target. 0=copy 1=add
        - cloneShapeSource (css): Name of the shape source to clone.
        - cloneTargetSource (cas): Name of the target source of the clone.
        - constrainToSurface (cts): If true, the modification keeps the surface curvature.
        - direction (d): Specifies the direction in which the vertices are moved.
        - displayFrozen (df): If false, turns off the display of frozen area on the object.
        - displayMask (dm): If false, turns off the display of masked area on the object.
        - displayWireframe (dw): If false, turns off the wireframe display of the object.
        - falloffType (ft): Specifies how the brush determines which vertices to affect.
        - grabFollowPath (gfp): If true, the grab brush effect follows mouse movement.
        - grabSilhouette (gs): If true, the grab brush uses paint-through mode.
        - grabTwist (gtw): If true, the grab brush twists the vertices.
        - inverted (inv): If true, inverts the effect of the brush.
        - lastMode (lm): Specifies the type of the last active sculpting brush.
        - lockShellBorder (lsb): Lock the shell borders so that they won't be moved by a UV texture brush.
        - minSize (msz): Specifies the minimum size percentage of the current brush.
        - minStrength (mst): Specifies the minimum strength percentage of the current brush.
        - mirror (mr): Specifies the mirror mode of the brush.
        - mode (m): Specifies the type of sculpting effect the brush will perform.
        - orientToSurface (ots): If true, aligns the brush display to the surface of the mesh.
        - recordStroke (rcs): Set this flag to true to enable stroke recording that can be later played back with the makeStroke flag.
        - sculptFalloffCurve (sfc): Specifies the falloff curve of sculpting effect the brush will perform.
        - size (sz): Specifies the world-space size of the current brush.
        - stampDistance (s): Specifies the stamping distance of the brush.
        - stampFile (stp): Specifies an image file to use as stamp.
        - stampFlipX (sfx): Specifies if the brush stamp is flipped on the X axis.
        - stampFlipY (sfy): Specifies if the brush stamp is flipped on the Y axis.
        - stampOrientToStroke (sos): Specifies if the brush stamp is aligned to the stroke direction.
        - stampPlacement (sp): Specifies the placement mode of the stamp image.
        - stampRandomization (srd): Specifies if the brush stamp is randomized.
        - stampRandomizeFlipX (srx): Specifies if the brush stamp flipping is randomized on the X axis.
        - stampRandomizeFlipY (sry): Specifies if the brush stamp flipping is randomized on the Y axis.
        - stampRandomizePosX (spx): Specifies the stamp X position value is randomized.
        - stampRandomizePosY (spy): Specifies the stamp Y position value is randomized.
        - stampRandomizeRotation (srr): Specifies the stamp rotation value is randomized.
        - stampRandomizeScale (src): Specifies the stamp scale value is randomized.
        - stampRandomizeStrength (srs): Specifies the stamp strength value is randomized.
        - stampRotation (sr): Specifies the rotation value of the stamp image.
        - steadyStrokeDistance (ssd): Specifies the distance for the steady stroke.
        - strength (st): Specifies the world-space strength of the current brush.
        - updatePlane (upl): Recalculates the underlying tool plane for each stamp in a stroke.
        - useGlobalSize (ugs): If true, all the brushes have a shared size property; otherwise size is local.
        - useScreenSpace (ssp): If true, the brush size is in screen space pixels.
        - useStampDistance (usd): Force the stamps to be spread out along the stroke, rather than building up continually.
        - useStampImage (usi): Specifies if the brush uses a stamp image.
        - useSteadyStroke (uss): Turns using steady stroke on/off.
        - wholeStroke (wst): Continuously recalculates the underlying tool plane from all the vertices affected during the stroke.
        - wireframeAlpha (wa): Sets the alpha value of the wireframe for the object that is being sculpted.
        - wireframeColor (wc): Sets the color of the wireframe for the object that is being sculpted. Values should be 0-1 RGB.
        - query (q): Query mode flag
    """
@overload #Overload for sculptMeshCacheCtx in ['query']
def sculptMeshCacheCtx(aal: bool = ..., bd: int = ..., bsz: float = ..., bst: float = ..., bur: float = ..., chs: bool = ..., cm: int = ..., css: str = ..., cas: str = ..., cts: bool = ..., d: int = ..., df: bool = ..., dm: bool = ..., dw: bool = ..., ft: int = ..., gfp: bool = ..., gs: bool = ..., gtw: bool = ..., inv: bool = ..., lm: str = ..., lsb: bool = ..., msz: float = ..., mst: float = ..., mr: int = ..., m: str = ..., ots: bool = ..., rcs: bool = ..., sfc: str = ..., sz: float = ..., s: float = ..., stp: str = ..., sfx: bool = ..., sfy: bool = ..., sos: bool = ..., sp: int = ..., srd: bool = ..., srx: bool = ..., sry: bool = ..., spx: float = ..., spy: float = ..., srr: float = ..., src: float = ..., srs: float = ..., sr: float = ..., ssd: float = ..., st: float = ..., upl: bool = ..., ugs: bool = ..., ssp: bool = ..., usd: bool = ..., usi: bool = ..., uss: bool = ..., wst: bool = ..., wa: float = ..., wc: [float, float, float] = ..., q: bool = ...) -> None:
    """sculptMeshCacheCtx is undoable, queryable, and editable.
    
    This is a tool context command for mesh cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext')
        cmds.setToolTo('sculptMeshCacheContext')
        # Set sculptMeshCacheContext's brush size to 10.0
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext', edit=True, sz=10.0)
    ```

    ---
    - Args:
        - affectAllLayers (aal): If true, the brush affects all layers at once.
        - brushDirection (bd): Specifies the direction of the named brush.
        - brushSize (bsz): Specifies the world-space size of the named brush.
        - brushStrength (bst): Specifies the world-space strength of the named brush.
        - buildUpRate (bur): Specifies the brush strength increasing along the stroke.
        - cloneHideSource (chs): True if the cloned source should be hidden.
        - cloneMethod (cm): Controls how the source delta vectors should change the target. 0=copy 1=add
        - cloneShapeSource (css): Name of the shape source to clone.
        - cloneTargetSource (cas): Name of the target source of the clone.
        - constrainToSurface (cts): If true, the modification keeps the surface curvature.
        - direction (d): Specifies the direction in which the vertices are moved.
        - displayFrozen (df): If false, turns off the display of frozen area on the object.
        - displayMask (dm): If false, turns off the display of masked area on the object.
        - displayWireframe (dw): If false, turns off the wireframe display of the object.
        - falloffType (ft): Specifies how the brush determines which vertices to affect.
        - grabFollowPath (gfp): If true, the grab brush effect follows mouse movement.
        - grabSilhouette (gs): If true, the grab brush uses paint-through mode.
        - grabTwist (gtw): If true, the grab brush twists the vertices.
        - inverted (inv): If true, inverts the effect of the brush.
        - lastMode (lm): Specifies the type of the last active sculpting brush.
        - lockShellBorder (lsb): Lock the shell borders so that they won't be moved by a UV texture brush.
        - minSize (msz): Specifies the minimum size percentage of the current brush.
        - minStrength (mst): Specifies the minimum strength percentage of the current brush.
        - mirror (mr): Specifies the mirror mode of the brush.
        - mode (m): Specifies the type of sculpting effect the brush will perform.
        - orientToSurface (ots): If true, aligns the brush display to the surface of the mesh.
        - recordStroke (rcs): Set this flag to true to enable stroke recording that can be later played back with the makeStroke flag.
        - sculptFalloffCurve (sfc): Specifies the falloff curve of sculpting effect the brush will perform.
        - size (sz): Specifies the world-space size of the current brush.
        - stampDistance (s): Specifies the stamping distance of the brush.
        - stampFile (stp): Specifies an image file to use as stamp.
        - stampFlipX (sfx): Specifies if the brush stamp is flipped on the X axis.
        - stampFlipY (sfy): Specifies if the brush stamp is flipped on the Y axis.
        - stampOrientToStroke (sos): Specifies if the brush stamp is aligned to the stroke direction.
        - stampPlacement (sp): Specifies the placement mode of the stamp image.
        - stampRandomization (srd): Specifies if the brush stamp is randomized.
        - stampRandomizeFlipX (srx): Specifies if the brush stamp flipping is randomized on the X axis.
        - stampRandomizeFlipY (sry): Specifies if the brush stamp flipping is randomized on the Y axis.
        - stampRandomizePosX (spx): Specifies the stamp X position value is randomized.
        - stampRandomizePosY (spy): Specifies the stamp Y position value is randomized.
        - stampRandomizeRotation (srr): Specifies the stamp rotation value is randomized.
        - stampRandomizeScale (src): Specifies the stamp scale value is randomized.
        - stampRandomizeStrength (srs): Specifies the stamp strength value is randomized.
        - stampRotation (sr): Specifies the rotation value of the stamp image.
        - steadyStrokeDistance (ssd): Specifies the distance for the steady stroke.
        - strength (st): Specifies the world-space strength of the current brush.
        - updatePlane (upl): Recalculates the underlying tool plane for each stamp in a stroke.
        - useGlobalSize (ugs): If true, all the brushes have a shared size property; otherwise size is local.
        - useScreenSpace (ssp): If true, the brush size is in screen space pixels.
        - useStampDistance (usd): Force the stamps to be spread out along the stroke, rather than building up continually.
        - useStampImage (usi): Specifies if the brush uses a stamp image.
        - useSteadyStroke (uss): Turns using steady stroke on/off.
        - wholeStroke (wst): Continuously recalculates the underlying tool plane from all the vertices affected during the stroke.
        - wireframeAlpha (wa): Sets the alpha value of the wireframe for the object that is being sculpted.
        - wireframeColor (wc): Sets the color of the wireframe for the object that is being sculpted. Values should be 0-1 RGB.
        - query (q): Query mode flag
    """
@overload #Overload for sculptMeshCacheCtx in ['query']
def sculptMeshCacheCtx(affectAllLayers: bool = ..., aal: bool = ..., brushDirection: int = ..., bd: int = ..., brushSize: float = ..., bsz: float = ..., brushStrength: float = ..., bst: float = ..., buildUpRate: float = ..., bur: float = ..., cloneHideSource: bool = ..., chs: bool = ..., cloneMethod: int = ..., cm: int = ..., cloneShapeSource: str = ..., css: str = ..., cloneTargetSource: str = ..., cas: str = ..., constrainToSurface: bool = ..., cts: bool = ..., direction: int = ..., d: int = ..., displayFrozen: bool = ..., df: bool = ..., displayMask: bool = ..., dm: bool = ..., displayWireframe: bool = ..., dw: bool = ..., falloffType: int = ..., ft: int = ..., grabFollowPath: bool = ..., gfp: bool = ..., grabSilhouette: bool = ..., gs: bool = ..., grabTwist: bool = ..., gtw: bool = ..., inverted: bool = ..., inv: bool = ..., lastMode: str = ..., lm: str = ..., lockShellBorder: bool = ..., lsb: bool = ..., minSize: float = ..., msz: float = ..., minStrength: float = ..., mst: float = ..., mirror: int = ..., mr: int = ..., mode: str = ..., m: str = ..., orientToSurface: bool = ..., ots: bool = ..., recordStroke: bool = ..., rcs: bool = ..., sculptFalloffCurve: str = ..., sfc: str = ..., size: float = ..., sz: float = ..., stampDistance: float = ..., s: float = ..., stampFile: str = ..., stp: str = ..., stampFlipX: bool = ..., sfx: bool = ..., stampFlipY: bool = ..., sfy: bool = ..., stampOrientToStroke: bool = ..., sos: bool = ..., stampPlacement: int = ..., sp: int = ..., stampRandomization: bool = ..., srd: bool = ..., stampRandomizeFlipX: bool = ..., srx: bool = ..., stampRandomizeFlipY: bool = ..., sry: bool = ..., stampRandomizePosX: float = ..., spx: float = ..., stampRandomizePosY: float = ..., spy: float = ..., stampRandomizeRotation: float = ..., srr: float = ..., stampRandomizeScale: float = ..., src: float = ..., stampRandomizeStrength: float = ..., srs: float = ..., stampRotation: float = ..., sr: float = ..., steadyStrokeDistance: float = ..., ssd: float = ..., strength: float = ..., st: float = ..., updatePlane: bool = ..., upl: bool = ..., useGlobalSize: bool = ..., ugs: bool = ..., useScreenSpace: bool = ..., ssp: bool = ..., useStampDistance: bool = ..., usd: bool = ..., useStampImage: bool = ..., usi: bool = ..., useSteadyStroke: bool = ..., uss: bool = ..., wholeStroke: bool = ..., wst: bool = ..., wireframeAlpha: float = ..., wa: float = ..., wireframeColor: [float, float, float] = ..., wc: [float, float, float] = ..., query: bool = ..., q: bool = ...) -> None:
    """sculptMeshCacheCtx is undoable, queryable, and editable.
    
    This is a tool context command for mesh cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext')
        cmds.setToolTo('sculptMeshCacheContext')
        # Set sculptMeshCacheContext's brush size to 10.0
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext', edit=True, sz=10.0)
    ```

    ---
    - Args:
        - affectAllLayers (aal): If true, the brush affects all layers at once.
        - brushDirection (bd): Specifies the direction of the named brush.
        - brushSize (bsz): Specifies the world-space size of the named brush.
        - brushStrength (bst): Specifies the world-space strength of the named brush.
        - buildUpRate (bur): Specifies the brush strength increasing along the stroke.
        - cloneHideSource (chs): True if the cloned source should be hidden.
        - cloneMethod (cm): Controls how the source delta vectors should change the target. 0=copy 1=add
        - cloneShapeSource (css): Name of the shape source to clone.
        - cloneTargetSource (cas): Name of the target source of the clone.
        - constrainToSurface (cts): If true, the modification keeps the surface curvature.
        - direction (d): Specifies the direction in which the vertices are moved.
        - displayFrozen (df): If false, turns off the display of frozen area on the object.
        - displayMask (dm): If false, turns off the display of masked area on the object.
        - displayWireframe (dw): If false, turns off the wireframe display of the object.
        - falloffType (ft): Specifies how the brush determines which vertices to affect.
        - grabFollowPath (gfp): If true, the grab brush effect follows mouse movement.
        - grabSilhouette (gs): If true, the grab brush uses paint-through mode.
        - grabTwist (gtw): If true, the grab brush twists the vertices.
        - inverted (inv): If true, inverts the effect of the brush.
        - lastMode (lm): Specifies the type of the last active sculpting brush.
        - lockShellBorder (lsb): Lock the shell borders so that they won't be moved by a UV texture brush.
        - minSize (msz): Specifies the minimum size percentage of the current brush.
        - minStrength (mst): Specifies the minimum strength percentage of the current brush.
        - mirror (mr): Specifies the mirror mode of the brush.
        - mode (m): Specifies the type of sculpting effect the brush will perform.
        - orientToSurface (ots): If true, aligns the brush display to the surface of the mesh.
        - recordStroke (rcs): Set this flag to true to enable stroke recording that can be later played back with the makeStroke flag.
        - sculptFalloffCurve (sfc): Specifies the falloff curve of sculpting effect the brush will perform.
        - size (sz): Specifies the world-space size of the current brush.
        - stampDistance (s): Specifies the stamping distance of the brush.
        - stampFile (stp): Specifies an image file to use as stamp.
        - stampFlipX (sfx): Specifies if the brush stamp is flipped on the X axis.
        - stampFlipY (sfy): Specifies if the brush stamp is flipped on the Y axis.
        - stampOrientToStroke (sos): Specifies if the brush stamp is aligned to the stroke direction.
        - stampPlacement (sp): Specifies the placement mode of the stamp image.
        - stampRandomization (srd): Specifies if the brush stamp is randomized.
        - stampRandomizeFlipX (srx): Specifies if the brush stamp flipping is randomized on the X axis.
        - stampRandomizeFlipY (sry): Specifies if the brush stamp flipping is randomized on the Y axis.
        - stampRandomizePosX (spx): Specifies the stamp X position value is randomized.
        - stampRandomizePosY (spy): Specifies the stamp Y position value is randomized.
        - stampRandomizeRotation (srr): Specifies the stamp rotation value is randomized.
        - stampRandomizeScale (src): Specifies the stamp scale value is randomized.
        - stampRandomizeStrength (srs): Specifies the stamp strength value is randomized.
        - stampRotation (sr): Specifies the rotation value of the stamp image.
        - steadyStrokeDistance (ssd): Specifies the distance for the steady stroke.
        - strength (st): Specifies the world-space strength of the current brush.
        - updatePlane (upl): Recalculates the underlying tool plane for each stamp in a stroke.
        - useGlobalSize (ugs): If true, all the brushes have a shared size property; otherwise size is local.
        - useScreenSpace (ssp): If true, the brush size is in screen space pixels.
        - useStampDistance (usd): Force the stamps to be spread out along the stroke, rather than building up continually.
        - useStampImage (usi): Specifies if the brush uses a stamp image.
        - useSteadyStroke (uss): Turns using steady stroke on/off.
        - wholeStroke (wst): Continuously recalculates the underlying tool plane from all the vertices affected during the stroke.
        - wireframeAlpha (wa): Sets the alpha value of the wireframe for the object that is being sculpted.
        - wireframeColor (wc): Sets the color of the wireframe for the object that is being sculpted. Values should be 0-1 RGB.
        - query (q): Query mode flag
    """
@overload #Overload for sculptMeshCacheCtx in ['edit']
def sculptMeshCacheCtx(adjustSize: bool = ..., adjustStrength: bool = ..., affectAllLayers: bool = ..., brushDirection: int = ..., brushSize: float = ..., brushStrength: float = ..., buildUpRate: float = ..., cloneHideSource: bool = ..., cloneMethod: int = ..., cloneShapeSource: str = ..., cloneTargetSource: str = ..., constrainToSurface: bool = ..., direction: int = ..., displayFrozen: bool = ..., displayMask: bool = ..., displayWireframe: bool = ..., falloffType: int = ..., flood: float = ..., floodFreeze: float = ..., frame: bool = ..., freezeSelection: bool = ..., grabFollowPath: bool = ..., grabSilhouette: bool = ..., grabTwist: bool = ..., inverted: bool = ..., lastMode: str = ..., lockShellBorder: bool = ..., makeStroke: [uint, uint, uint, float, float] = ..., minSize: float = ..., minStrength: float = ..., mirror: int = ..., mode: str = ..., orientToSurface: bool = ..., recordStroke: bool = ..., sculptFalloffCurve: str = ..., size: float = ..., stampDistance: float = ..., stampFile: str = ..., stampFlipX: bool = ..., stampFlipY: bool = ..., stampOrientToStroke: bool = ..., stampPlacement: int = ..., stampRandomization: bool = ..., stampRandomizationSeed: int = ..., stampRandomizeFlipX: bool = ..., stampRandomizeFlipY: bool = ..., stampRandomizePosX: float = ..., stampRandomizePosY: float = ..., stampRandomizeRotation: float = ..., stampRandomizeScale: float = ..., stampRandomizeStrength: float = ..., stampRotation: float = ..., steadyStrokeDistance: float = ..., strength: float = ..., updatePlane: bool = ..., useGlobalSize: bool = ..., useScreenSpace: bool = ..., useStampDistance: bool = ..., useStampImage: bool = ..., useSteadyStroke: bool = ..., wholeStroke: bool = ..., wireframeAlpha: float = ..., wireframeColor: [float, float, float] = ..., edit: bool = ...) -> None:
    """sculptMeshCacheCtx is undoable, queryable, and editable.
    
    This is a tool context command for mesh cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext')
        cmds.setToolTo('sculptMeshCacheContext')
        # Set sculptMeshCacheContext's brush size to 10.0
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext', edit=True, sz=10.0)
    ```

    ---
    - Args:
        - adjustSize (asz): If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous sculpt mode.
        - adjustStrength (ast): If true, puts the tool into the mode where dragging the mouse will edit the brush strength. If false, puts the tool back into the previous sculpt mode.
        - affectAllLayers (aal): If true, the brush affects all layers at once.
        - brushDirection (bd): Specifies the direction of the named brush.
        - brushSize (bsz): Specifies the world-space size of the named brush.
        - brushStrength (bst): Specifies the world-space strength of the named brush.
        - buildUpRate (bur): Specifies the brush strength increasing along the stroke.
        - cloneHideSource (chs): True if the cloned source should be hidden.
        - cloneMethod (cm): Controls how the source delta vectors should change the target. 0=copy 1=add
        - cloneShapeSource (css): Name of the shape source to clone.
        - cloneTargetSource (cas): Name of the target source of the clone.
        - constrainToSurface (cts): If true, the modification keeps the surface curvature.
        - direction (d): Specifies the direction in which the vertices are moved.
        - displayFrozen (df): If false, turns off the display of frozen area on the object.
        - displayMask (dm): If false, turns off the display of masked area on the object.
        - displayWireframe (dw): If false, turns off the wireframe display of the object.
        - falloffType (ft): Specifies how the brush determines which vertices to affect.
        - flood (fl): Sets the brush effect for each vertex to the given value.
        - floodFreeze (ff): Sets the freeze value for each vertex to the given value.
        - frame (frm): Frames on the sculpted area.
        - freezeSelection (fsl): Freezes selected components.
        - grabFollowPath (gfp): If true, the grab brush effect follows mouse movement.
        - grabSilhouette (gs): If true, the grab brush uses paint-through mode.
        - grabTwist (gtw): If true, the grab brush twists the vertices.
        - inverted (inv): If true, inverts the effect of the brush.
        - lastMode (lm): Specifies the type of the last active sculpting brush.
        - lockShellBorder (lsb): Lock the shell borders so that they won't be moved by a UV texture brush.
        - makeStroke (mt): Specify a surface point patch for a brush stroke. Multiple patches can be specified to form a brush stroke. The first argument is the mesh index. The second argument is the side index. use 0 for the original side, and 1 for the mirrored
            side The third argument is the face index within the specified mesh. The fourth and fifth arguments are the face coordinates within the specified face.
        - minSize (msz): Specifies the minimum size percentage of the current brush.
        - minStrength (mst): Specifies the minimum strength percentage of the current brush.
        - mirror (mr): Specifies the mirror mode of the brush.
        - mode (m): Specifies the type of sculpting effect the brush will perform.
        - orientToSurface (ots): If true, aligns the brush display to the surface of the mesh.
        - recordStroke (rcs): Set this flag to true to enable stroke recording that can be later played back with the makeStroke flag.
        - sculptFalloffCurve (sfc): Specifies the falloff curve of sculpting effect the brush will perform.
        - size (sz): Specifies the world-space size of the current brush.
        - stampDistance (s): Specifies the stamping distance of the brush.
        - stampFile (stp): Specifies an image file to use as stamp.
        - stampFlipX (sfx): Specifies if the brush stamp is flipped on the X axis.
        - stampFlipY (sfy): Specifies if the brush stamp is flipped on the Y axis.
        - stampOrientToStroke (sos): Specifies if the brush stamp is aligned to the stroke direction.
        - stampPlacement (sp): Specifies the placement mode of the stamp image.
        - stampRandomization (srd): Specifies if the brush stamp is randomized.
        - stampRandomizationSeed (sre): Specifies the stamp randomization seed value. Use a value of 0 to generate a random seed value.
        - stampRandomizeFlipX (srx): Specifies if the brush stamp flipping is randomized on the X axis.
        - stampRandomizeFlipY (sry): Specifies if the brush stamp flipping is randomized on the Y axis.
        - stampRandomizePosX (spx): Specifies the stamp X position value is randomized.
        - stampRandomizePosY (spy): Specifies the stamp Y position value is randomized.
        - stampRandomizeRotation (srr): Specifies the stamp rotation value is randomized.
        - stampRandomizeScale (src): Specifies the stamp scale value is randomized.
        - stampRandomizeStrength (srs): Specifies the stamp strength value is randomized.
        - stampRotation (sr): Specifies the rotation value of the stamp image.
        - steadyStrokeDistance (ssd): Specifies the distance for the steady stroke.
        - strength (st): Specifies the world-space strength of the current brush.
        - updatePlane (upl): Recalculates the underlying tool plane for each stamp in a stroke.
        - useGlobalSize (ugs): If true, all the brushes have a shared size property; otherwise size is local.
        - useScreenSpace (ssp): If true, the brush size is in screen space pixels.
        - useStampDistance (usd): Force the stamps to be spread out along the stroke, rather than building up continually.
        - useStampImage (usi): Specifies if the brush uses a stamp image.
        - useSteadyStroke (uss): Turns using steady stroke on/off.
        - wholeStroke (wst): Continuously recalculates the underlying tool plane from all the vertices affected during the stroke.
        - wireframeAlpha (wa): Sets the alpha value of the wireframe for the object that is being sculpted.
        - wireframeColor (wc): Sets the color of the wireframe for the object that is being sculpted. Values should be 0-1 RGB.
        - edit (e): Edit mode flag
    """
@overload #Overload for sculptMeshCacheCtx in ['edit']
def sculptMeshCacheCtx(asz: bool = ..., ast: bool = ..., aal: bool = ..., bd: int = ..., bsz: float = ..., bst: float = ..., bur: float = ..., chs: bool = ..., cm: int = ..., css: str = ..., cas: str = ..., cts: bool = ..., d: int = ..., df: bool = ..., dm: bool = ..., dw: bool = ..., ft: int = ..., fl: float = ..., ff: float = ..., frm: bool = ..., fsl: bool = ..., gfp: bool = ..., gs: bool = ..., gtw: bool = ..., inv: bool = ..., lm: str = ..., lsb: bool = ..., mt: [uint, uint, uint, float, float] = ..., msz: float = ..., mst: float = ..., mr: int = ..., m: str = ..., ots: bool = ..., rcs: bool = ..., sfc: str = ..., sz: float = ..., s: float = ..., stp: str = ..., sfx: bool = ..., sfy: bool = ..., sos: bool = ..., sp: int = ..., srd: bool = ..., sre: int = ..., srx: bool = ..., sry: bool = ..., spx: float = ..., spy: float = ..., srr: float = ..., src: float = ..., srs: float = ..., sr: float = ..., ssd: float = ..., st: float = ..., upl: bool = ..., ugs: bool = ..., ssp: bool = ..., usd: bool = ..., usi: bool = ..., uss: bool = ..., wst: bool = ..., wa: float = ..., wc: [float, float, float] = ..., e: bool = ...) -> None:
    """sculptMeshCacheCtx is undoable, queryable, and editable.
    
    This is a tool context command for mesh cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext')
        cmds.setToolTo('sculptMeshCacheContext')
        # Set sculptMeshCacheContext's brush size to 10.0
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext', edit=True, sz=10.0)
    ```

    ---
    - Args:
        - adjustSize (asz): If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous sculpt mode.
        - adjustStrength (ast): If true, puts the tool into the mode where dragging the mouse will edit the brush strength. If false, puts the tool back into the previous sculpt mode.
        - affectAllLayers (aal): If true, the brush affects all layers at once.
        - brushDirection (bd): Specifies the direction of the named brush.
        - brushSize (bsz): Specifies the world-space size of the named brush.
        - brushStrength (bst): Specifies the world-space strength of the named brush.
        - buildUpRate (bur): Specifies the brush strength increasing along the stroke.
        - cloneHideSource (chs): True if the cloned source should be hidden.
        - cloneMethod (cm): Controls how the source delta vectors should change the target. 0=copy 1=add
        - cloneShapeSource (css): Name of the shape source to clone.
        - cloneTargetSource (cas): Name of the target source of the clone.
        - constrainToSurface (cts): If true, the modification keeps the surface curvature.
        - direction (d): Specifies the direction in which the vertices are moved.
        - displayFrozen (df): If false, turns off the display of frozen area on the object.
        - displayMask (dm): If false, turns off the display of masked area on the object.
        - displayWireframe (dw): If false, turns off the wireframe display of the object.
        - falloffType (ft): Specifies how the brush determines which vertices to affect.
        - flood (fl): Sets the brush effect for each vertex to the given value.
        - floodFreeze (ff): Sets the freeze value for each vertex to the given value.
        - frame (frm): Frames on the sculpted area.
        - freezeSelection (fsl): Freezes selected components.
        - grabFollowPath (gfp): If true, the grab brush effect follows mouse movement.
        - grabSilhouette (gs): If true, the grab brush uses paint-through mode.
        - grabTwist (gtw): If true, the grab brush twists the vertices.
        - inverted (inv): If true, inverts the effect of the brush.
        - lastMode (lm): Specifies the type of the last active sculpting brush.
        - lockShellBorder (lsb): Lock the shell borders so that they won't be moved by a UV texture brush.
        - makeStroke (mt): Specify a surface point patch for a brush stroke. Multiple patches can be specified to form a brush stroke. The first argument is the mesh index. The second argument is the side index. use 0 for the original side, and 1 for the mirrored
            side The third argument is the face index within the specified mesh. The fourth and fifth arguments are the face coordinates within the specified face.
        - minSize (msz): Specifies the minimum size percentage of the current brush.
        - minStrength (mst): Specifies the minimum strength percentage of the current brush.
        - mirror (mr): Specifies the mirror mode of the brush.
        - mode (m): Specifies the type of sculpting effect the brush will perform.
        - orientToSurface (ots): If true, aligns the brush display to the surface of the mesh.
        - recordStroke (rcs): Set this flag to true to enable stroke recording that can be later played back with the makeStroke flag.
        - sculptFalloffCurve (sfc): Specifies the falloff curve of sculpting effect the brush will perform.
        - size (sz): Specifies the world-space size of the current brush.
        - stampDistance (s): Specifies the stamping distance of the brush.
        - stampFile (stp): Specifies an image file to use as stamp.
        - stampFlipX (sfx): Specifies if the brush stamp is flipped on the X axis.
        - stampFlipY (sfy): Specifies if the brush stamp is flipped on the Y axis.
        - stampOrientToStroke (sos): Specifies if the brush stamp is aligned to the stroke direction.
        - stampPlacement (sp): Specifies the placement mode of the stamp image.
        - stampRandomization (srd): Specifies if the brush stamp is randomized.
        - stampRandomizationSeed (sre): Specifies the stamp randomization seed value. Use a value of 0 to generate a random seed value.
        - stampRandomizeFlipX (srx): Specifies if the brush stamp flipping is randomized on the X axis.
        - stampRandomizeFlipY (sry): Specifies if the brush stamp flipping is randomized on the Y axis.
        - stampRandomizePosX (spx): Specifies the stamp X position value is randomized.
        - stampRandomizePosY (spy): Specifies the stamp Y position value is randomized.
        - stampRandomizeRotation (srr): Specifies the stamp rotation value is randomized.
        - stampRandomizeScale (src): Specifies the stamp scale value is randomized.
        - stampRandomizeStrength (srs): Specifies the stamp strength value is randomized.
        - stampRotation (sr): Specifies the rotation value of the stamp image.
        - steadyStrokeDistance (ssd): Specifies the distance for the steady stroke.
        - strength (st): Specifies the world-space strength of the current brush.
        - updatePlane (upl): Recalculates the underlying tool plane for each stamp in a stroke.
        - useGlobalSize (ugs): If true, all the brushes have a shared size property; otherwise size is local.
        - useScreenSpace (ssp): If true, the brush size is in screen space pixels.
        - useStampDistance (usd): Force the stamps to be spread out along the stroke, rather than building up continually.
        - useStampImage (usi): Specifies if the brush uses a stamp image.
        - useSteadyStroke (uss): Turns using steady stroke on/off.
        - wholeStroke (wst): Continuously recalculates the underlying tool plane from all the vertices affected during the stroke.
        - wireframeAlpha (wa): Sets the alpha value of the wireframe for the object that is being sculpted.
        - wireframeColor (wc): Sets the color of the wireframe for the object that is being sculpted. Values should be 0-1 RGB.
        - edit (e): Edit mode flag
    """
@overload #Overload for sculptMeshCacheCtx in ['edit']
def sculptMeshCacheCtx(adjustSize: bool = ..., asz: bool = ..., adjustStrength: bool = ..., ast: bool = ..., affectAllLayers: bool = ..., aal: bool = ..., brushDirection: int = ..., bd: int = ..., brushSize: float = ..., bsz: float = ..., brushStrength: float = ..., bst: float = ..., buildUpRate: float = ..., bur: float = ..., cloneHideSource: bool = ..., chs: bool = ..., cloneMethod: int = ..., cm: int = ..., cloneShapeSource: str = ..., css: str = ..., cloneTargetSource: str = ..., cas: str = ..., constrainToSurface: bool = ..., cts: bool = ..., direction: int = ..., d: int = ..., displayFrozen: bool = ..., df: bool = ..., displayMask: bool = ..., dm: bool = ..., displayWireframe: bool = ..., dw: bool = ..., falloffType: int = ..., ft: int = ..., flood: float = ..., fl: float = ..., floodFreeze: float = ..., ff: float = ..., frame: bool = ..., frm: bool = ..., freezeSelection: bool = ..., fsl: bool = ..., grabFollowPath: bool = ..., gfp: bool = ..., grabSilhouette: bool = ..., gs: bool = ..., grabTwist: bool = ..., gtw: bool = ..., inverted: bool = ..., inv: bool = ..., lastMode: str = ..., lm: str = ..., lockShellBorder: bool = ..., lsb: bool = ..., makeStroke: [uint, uint, uint, float, float] = ..., mt: [uint, uint, uint, float, float] = ..., minSize: float = ..., msz: float = ..., minStrength: float = ..., mst: float = ..., mirror: int = ..., mr: int = ..., mode: str = ..., m: str = ..., orientToSurface: bool = ..., ots: bool = ..., recordStroke: bool = ..., rcs: bool = ..., sculptFalloffCurve: str = ..., sfc: str = ..., size: float = ..., sz: float = ..., stampDistance: float = ..., s: float = ..., stampFile: str = ..., stp: str = ..., stampFlipX: bool = ..., sfx: bool = ..., stampFlipY: bool = ..., sfy: bool = ..., stampOrientToStroke: bool = ..., sos: bool = ..., stampPlacement: int = ..., sp: int = ..., stampRandomization: bool = ..., srd: bool = ..., stampRandomizationSeed: int = ..., sre: int = ..., stampRandomizeFlipX: bool = ..., srx: bool = ..., stampRandomizeFlipY: bool = ..., sry: bool = ..., stampRandomizePosX: float = ..., spx: float = ..., stampRandomizePosY: float = ..., spy: float = ..., stampRandomizeRotation: float = ..., srr: float = ..., stampRandomizeScale: float = ..., src: float = ..., stampRandomizeStrength: float = ..., srs: float = ..., stampRotation: float = ..., sr: float = ..., steadyStrokeDistance: float = ..., ssd: float = ..., strength: float = ..., st: float = ..., updatePlane: bool = ..., upl: bool = ..., useGlobalSize: bool = ..., ugs: bool = ..., useScreenSpace: bool = ..., ssp: bool = ..., useStampDistance: bool = ..., usd: bool = ..., useStampImage: bool = ..., usi: bool = ..., useSteadyStroke: bool = ..., uss: bool = ..., wholeStroke: bool = ..., wst: bool = ..., wireframeAlpha: float = ..., wa: float = ..., wireframeColor: [float, float, float] = ..., wc: [float, float, float] = ..., edit: bool = ..., e: bool = ...) -> None:
    """sculptMeshCacheCtx is undoable, queryable, and editable.
    
    This is a tool context command for mesh cache sculpting tool.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new sculpting context, then switch to it
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext')
        cmds.setToolTo('sculptMeshCacheContext')
        # Set sculptMeshCacheContext's brush size to 10.0
        cmds.sculptMeshCacheCtx('sculptMeshCacheContext', edit=True, sz=10.0)
    ```

    ---
    - Args:
        - adjustSize (asz): If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous sculpt mode.
        - adjustStrength (ast): If true, puts the tool into the mode where dragging the mouse will edit the brush strength. If false, puts the tool back into the previous sculpt mode.
        - affectAllLayers (aal): If true, the brush affects all layers at once.
        - brushDirection (bd): Specifies the direction of the named brush.
        - brushSize (bsz): Specifies the world-space size of the named brush.
        - brushStrength (bst): Specifies the world-space strength of the named brush.
        - buildUpRate (bur): Specifies the brush strength increasing along the stroke.
        - cloneHideSource (chs): True if the cloned source should be hidden.
        - cloneMethod (cm): Controls how the source delta vectors should change the target. 0=copy 1=add
        - cloneShapeSource (css): Name of the shape source to clone.
        - cloneTargetSource (cas): Name of the target source of the clone.
        - constrainToSurface (cts): If true, the modification keeps the surface curvature.
        - direction (d): Specifies the direction in which the vertices are moved.
        - displayFrozen (df): If false, turns off the display of frozen area on the object.
        - displayMask (dm): If false, turns off the display of masked area on the object.
        - displayWireframe (dw): If false, turns off the wireframe display of the object.
        - falloffType (ft): Specifies how the brush determines which vertices to affect.
        - flood (fl): Sets the brush effect for each vertex to the given value.
        - floodFreeze (ff): Sets the freeze value for each vertex to the given value.
        - frame (frm): Frames on the sculpted area.
        - freezeSelection (fsl): Freezes selected components.
        - grabFollowPath (gfp): If true, the grab brush effect follows mouse movement.
        - grabSilhouette (gs): If true, the grab brush uses paint-through mode.
        - grabTwist (gtw): If true, the grab brush twists the vertices.
        - inverted (inv): If true, inverts the effect of the brush.
        - lastMode (lm): Specifies the type of the last active sculpting brush.
        - lockShellBorder (lsb): Lock the shell borders so that they won't be moved by a UV texture brush.
        - makeStroke (mt): Specify a surface point patch for a brush stroke. Multiple patches can be specified to form a brush stroke. The first argument is the mesh index. The second argument is the side index. use 0 for the original side, and 1 for the mirrored
            side The third argument is the face index within the specified mesh. The fourth and fifth arguments are the face coordinates within the specified face.
        - minSize (msz): Specifies the minimum size percentage of the current brush.
        - minStrength (mst): Specifies the minimum strength percentage of the current brush.
        - mirror (mr): Specifies the mirror mode of the brush.
        - mode (m): Specifies the type of sculpting effect the brush will perform.
        - orientToSurface (ots): If true, aligns the brush display to the surface of the mesh.
        - recordStroke (rcs): Set this flag to true to enable stroke recording that can be later played back with the makeStroke flag.
        - sculptFalloffCurve (sfc): Specifies the falloff curve of sculpting effect the brush will perform.
        - size (sz): Specifies the world-space size of the current brush.
        - stampDistance (s): Specifies the stamping distance of the brush.
        - stampFile (stp): Specifies an image file to use as stamp.
        - stampFlipX (sfx): Specifies if the brush stamp is flipped on the X axis.
        - stampFlipY (sfy): Specifies if the brush stamp is flipped on the Y axis.
        - stampOrientToStroke (sos): Specifies if the brush stamp is aligned to the stroke direction.
        - stampPlacement (sp): Specifies the placement mode of the stamp image.
        - stampRandomization (srd): Specifies if the brush stamp is randomized.
        - stampRandomizationSeed (sre): Specifies the stamp randomization seed value. Use a value of 0 to generate a random seed value.
        - stampRandomizeFlipX (srx): Specifies if the brush stamp flipping is randomized on the X axis.
        - stampRandomizeFlipY (sry): Specifies if the brush stamp flipping is randomized on the Y axis.
        - stampRandomizePosX (spx): Specifies the stamp X position value is randomized.
        - stampRandomizePosY (spy): Specifies the stamp Y position value is randomized.
        - stampRandomizeRotation (srr): Specifies the stamp rotation value is randomized.
        - stampRandomizeScale (src): Specifies the stamp scale value is randomized.
        - stampRandomizeStrength (srs): Specifies the stamp strength value is randomized.
        - stampRotation (sr): Specifies the rotation value of the stamp image.
        - steadyStrokeDistance (ssd): Specifies the distance for the steady stroke.
        - strength (st): Specifies the world-space strength of the current brush.
        - updatePlane (upl): Recalculates the underlying tool plane for each stamp in a stroke.
        - useGlobalSize (ugs): If true, all the brushes have a shared size property; otherwise size is local.
        - useScreenSpace (ssp): If true, the brush size is in screen space pixels.
        - useStampDistance (usd): Force the stamps to be spread out along the stroke, rather than building up continually.
        - useStampImage (usi): Specifies if the brush uses a stamp image.
        - useSteadyStroke (uss): Turns using steady stroke on/off.
        - wholeStroke (wst): Continuously recalculates the underlying tool plane from all the vertices affected during the stroke.
        - wireframeAlpha (wa): Sets the alpha value of the wireframe for the object that is being sculpted.
        - wireframeColor (wc): Sets the color of the wireframe for the object that is being sculpted. Values should be 0-1 RGB.
        - edit (e): Edit mode flag
    """
