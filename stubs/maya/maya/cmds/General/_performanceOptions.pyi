"""Stub files for General category in Maya commands, command: performanceOptions."""

from typing import Any, overload

@overload #Overload for performanceOptions in ['query']
def performanceOptions(clusterResolution: float = ..., disableStitch: str = ..., disableTrimBoundaryDisplay: str = ..., disableTrimDisplay: str = ..., latticeResolution: float = ..., passThroughBindSkinAndFlexors: str = ..., passThroughBlendShape: str = ..., passThroughCluster: str = ..., passThroughDeltaMush: str = ..., passThroughFlexors: str = ..., passThroughLattice: str = ..., passThroughMeshBoolean: str = ..., passThroughPaintEffects: str = ..., passThroughSculpt: str = ..., passThroughWire: str = ..., regionOfEffect: str = ..., skipHierarchyTraversal: bool = ..., useClusterResolution: str = ..., useLatticeResolution: str = ..., query: bool = ...) -> str | float:
    """performanceOptions is undoable, queryable, and NOT editable.
    
    Sets the global performance options for the application. The options allow the
    disabling of features such as stitch surfaces or deformers to cut down on
    computation time in the scene.
    
    Performance options that are in effect may be on all the time, or they can be
    turned on only for interaction. In the latter case, the options will only take
    effect during UI interaction or playback.
    
    Note that none of these performance options will affect rendering.

    Example:
    ```python
        import maya.cmds as cmds
        # Disable the generation of stitch surfaces
        cmds.performanceOptions( ds=1 )
        # Put sculpt deformers into pass-through mode during interaction/playback
        cmds.performanceOptions( ps='interactive' )
    ```

    ---
    - Args:
        - clusterResolution (cr): Sets the global cluster resolution.  This value may range between 0.0 (exact calculation) and 10.0 (rough approximation)
        - disableStitch (ds): Sets the state of stitch surface disablement.  Setting this to "on" suppresses the generation of stitch surfaces. Valid values are "on", "off", "interactive".
        - disableTrimBoundaryDisplay (dtb): Sets the state of trim boundary drawing disablement.  Setting this to "on" suppresses the drawing of surface trim boundaries. Valid values are "on", "off", "interactive".
        - disableTrimDisplay (dt): Sets the state of trim drawing disablement.  Setting this to "on" suppresses the drawing of surface trims. Valid values are "on", "off", "interactive".
        - latticeResolution (lr): Sets the global lattice resolution.  This value may range between 0.0 (exact calculation) and 1.0 (rough approximation)
        - passThroughBindSkinAndFlexors (pbf): Sets the state of bind skin and all flexors pass through. Valid values are "on", "off", "interactive".
        - passThroughBlendShape (pbs): Sets the state of blend shape deformer pass through. Valid values are "on", "off", "interactive".
        - passThroughCluster (pc): Sets the state of cluster deformer pass through. Valid values are "on", "off", "interactive".
        - passThroughDeltaMush (pdm): Sets the state of delta mush deformer pass through. Valid values are "on", "off", "interactive".
        - passThroughFlexors (pf): Sets the state of flexor pass through. Valid values are "on", "off", "interactive".
        - passThroughLattice (pl): Sets the state of lattice deformer pass through. Valid values are "on", "off", "interactive".
        - passThroughMeshBoolean (pmb): Sets the state of mesh booleans pass through. Valid values are "on", "off", "interactive".
        - passThroughPaintEffects (pp): Sets the state of paint effects pass through. Valid values are "on", "off", "interactive".
        - passThroughSculpt (ps): Sets the state of sculpt deformer pass through. Valid values are "on", "off", "interactive".
        - passThroughWire (pw): Sets the state of wire deformer pass through. Valid values are "on", "off", "interactive".
        - regionOfEffect (roe): When enabled, an interactive update of translation commands will attempt to determine which components are being changed and only update effected components as a performance optimization while dragging a manip.
        - skipHierarchyTraversal (sht): When enabled, hierarchy traversal of invisible objects in the scene will be disabled in order to increase performance however this has a side effect of performing redundant viewport refreshes on certain actions such as manipulations,
            start/end of playback, idle refresh calls, etc.
        - useClusterResolution (ucr): Sets the state of cluster deformer global resolution.  This allows clusters to be calculated at a lower resolution. Valid values are "on", "off", "interactive".
        - useLatticeResolution (ulr): Sets the state of lattice deformer global resolution.  This allows lattices to be calculated at a lower resolution. Valid values are "on", "off", "interactive".
        - query (q): Query mode flag
    """
@overload #Overload for performanceOptions in ['query']
def performanceOptions(cr: float = ..., ds: str = ..., dtb: str = ..., dt: str = ..., lr: float = ..., pbf: str = ..., pbs: str = ..., pc: str = ..., pdm: str = ..., pf: str = ..., pl: str = ..., pmb: str = ..., pp: str = ..., ps: str = ..., pw: str = ..., roe: str = ..., sht: bool = ..., ucr: str = ..., ulr: str = ..., q: bool = ...) -> str | float:
    """performanceOptions is undoable, queryable, and NOT editable.
    
    Sets the global performance options for the application. The options allow the
    disabling of features such as stitch surfaces or deformers to cut down on
    computation time in the scene.
    
    Performance options that are in effect may be on all the time, or they can be
    turned on only for interaction. In the latter case, the options will only take
    effect during UI interaction or playback.
    
    Note that none of these performance options will affect rendering.

    Example:
    ```python
        import maya.cmds as cmds
        # Disable the generation of stitch surfaces
        cmds.performanceOptions( ds=1 )
        # Put sculpt deformers into pass-through mode during interaction/playback
        cmds.performanceOptions( ps='interactive' )
    ```

    ---
    - Args:
        - clusterResolution (cr): Sets the global cluster resolution.  This value may range between 0.0 (exact calculation) and 10.0 (rough approximation)
        - disableStitch (ds): Sets the state of stitch surface disablement.  Setting this to "on" suppresses the generation of stitch surfaces. Valid values are "on", "off", "interactive".
        - disableTrimBoundaryDisplay (dtb): Sets the state of trim boundary drawing disablement.  Setting this to "on" suppresses the drawing of surface trim boundaries. Valid values are "on", "off", "interactive".
        - disableTrimDisplay (dt): Sets the state of trim drawing disablement.  Setting this to "on" suppresses the drawing of surface trims. Valid values are "on", "off", "interactive".
        - latticeResolution (lr): Sets the global lattice resolution.  This value may range between 0.0 (exact calculation) and 1.0 (rough approximation)
        - passThroughBindSkinAndFlexors (pbf): Sets the state of bind skin and all flexors pass through. Valid values are "on", "off", "interactive".
        - passThroughBlendShape (pbs): Sets the state of blend shape deformer pass through. Valid values are "on", "off", "interactive".
        - passThroughCluster (pc): Sets the state of cluster deformer pass through. Valid values are "on", "off", "interactive".
        - passThroughDeltaMush (pdm): Sets the state of delta mush deformer pass through. Valid values are "on", "off", "interactive".
        - passThroughFlexors (pf): Sets the state of flexor pass through. Valid values are "on", "off", "interactive".
        - passThroughLattice (pl): Sets the state of lattice deformer pass through. Valid values are "on", "off", "interactive".
        - passThroughMeshBoolean (pmb): Sets the state of mesh booleans pass through. Valid values are "on", "off", "interactive".
        - passThroughPaintEffects (pp): Sets the state of paint effects pass through. Valid values are "on", "off", "interactive".
        - passThroughSculpt (ps): Sets the state of sculpt deformer pass through. Valid values are "on", "off", "interactive".
        - passThroughWire (pw): Sets the state of wire deformer pass through. Valid values are "on", "off", "interactive".
        - regionOfEffect (roe): When enabled, an interactive update of translation commands will attempt to determine which components are being changed and only update effected components as a performance optimization while dragging a manip.
        - skipHierarchyTraversal (sht): When enabled, hierarchy traversal of invisible objects in the scene will be disabled in order to increase performance however this has a side effect of performing redundant viewport refreshes on certain actions such as manipulations,
            start/end of playback, idle refresh calls, etc.
        - useClusterResolution (ucr): Sets the state of cluster deformer global resolution.  This allows clusters to be calculated at a lower resolution. Valid values are "on", "off", "interactive".
        - useLatticeResolution (ulr): Sets the state of lattice deformer global resolution.  This allows lattices to be calculated at a lower resolution. Valid values are "on", "off", "interactive".
        - query (q): Query mode flag
    """
@overload #Overload for performanceOptions in ['query']
def performanceOptions(clusterResolution: float = ..., cr: float = ..., disableStitch: str = ..., ds: str = ..., disableTrimBoundaryDisplay: str = ..., dtb: str = ..., disableTrimDisplay: str = ..., dt: str = ..., latticeResolution: float = ..., lr: float = ..., passThroughBindSkinAndFlexors: str = ..., pbf: str = ..., passThroughBlendShape: str = ..., pbs: str = ..., passThroughCluster: str = ..., pc: str = ..., passThroughDeltaMush: str = ..., pdm: str = ..., passThroughFlexors: str = ..., pf: str = ..., passThroughLattice: str = ..., pl: str = ..., passThroughMeshBoolean: str = ..., pmb: str = ..., passThroughPaintEffects: str = ..., pp: str = ..., passThroughSculpt: str = ..., ps: str = ..., passThroughWire: str = ..., pw: str = ..., regionOfEffect: str = ..., roe: str = ..., skipHierarchyTraversal: bool = ..., sht: bool = ..., useClusterResolution: str = ..., ucr: str = ..., useLatticeResolution: str = ..., ulr: str = ..., query: bool = ..., q: bool = ...) -> str | float:
    """performanceOptions is undoable, queryable, and NOT editable.
    
    Sets the global performance options for the application. The options allow the
    disabling of features such as stitch surfaces or deformers to cut down on
    computation time in the scene.
    
    Performance options that are in effect may be on all the time, or they can be
    turned on only for interaction. In the latter case, the options will only take
    effect during UI interaction or playback.
    
    Note that none of these performance options will affect rendering.

    Example:
    ```python
        import maya.cmds as cmds
        # Disable the generation of stitch surfaces
        cmds.performanceOptions( ds=1 )
        # Put sculpt deformers into pass-through mode during interaction/playback
        cmds.performanceOptions( ps='interactive' )
    ```

    ---
    - Args:
        - clusterResolution (cr): Sets the global cluster resolution.  This value may range between 0.0 (exact calculation) and 10.0 (rough approximation)
        - disableStitch (ds): Sets the state of stitch surface disablement.  Setting this to "on" suppresses the generation of stitch surfaces. Valid values are "on", "off", "interactive".
        - disableTrimBoundaryDisplay (dtb): Sets the state of trim boundary drawing disablement.  Setting this to "on" suppresses the drawing of surface trim boundaries. Valid values are "on", "off", "interactive".
        - disableTrimDisplay (dt): Sets the state of trim drawing disablement.  Setting this to "on" suppresses the drawing of surface trims. Valid values are "on", "off", "interactive".
        - latticeResolution (lr): Sets the global lattice resolution.  This value may range between 0.0 (exact calculation) and 1.0 (rough approximation)
        - passThroughBindSkinAndFlexors (pbf): Sets the state of bind skin and all flexors pass through. Valid values are "on", "off", "interactive".
        - passThroughBlendShape (pbs): Sets the state of blend shape deformer pass through. Valid values are "on", "off", "interactive".
        - passThroughCluster (pc): Sets the state of cluster deformer pass through. Valid values are "on", "off", "interactive".
        - passThroughDeltaMush (pdm): Sets the state of delta mush deformer pass through. Valid values are "on", "off", "interactive".
        - passThroughFlexors (pf): Sets the state of flexor pass through. Valid values are "on", "off", "interactive".
        - passThroughLattice (pl): Sets the state of lattice deformer pass through. Valid values are "on", "off", "interactive".
        - passThroughMeshBoolean (pmb): Sets the state of mesh booleans pass through. Valid values are "on", "off", "interactive".
        - passThroughPaintEffects (pp): Sets the state of paint effects pass through. Valid values are "on", "off", "interactive".
        - passThroughSculpt (ps): Sets the state of sculpt deformer pass through. Valid values are "on", "off", "interactive".
        - passThroughWire (pw): Sets the state of wire deformer pass through. Valid values are "on", "off", "interactive".
        - regionOfEffect (roe): When enabled, an interactive update of translation commands will attempt to determine which components are being changed and only update effected components as a performance optimization while dragging a manip.
        - skipHierarchyTraversal (sht): When enabled, hierarchy traversal of invisible objects in the scene will be disabled in order to increase performance however this has a side effect of performing redundant viewport refreshes on certain actions such as manipulations,
            start/end of playback, idle refresh calls, etc.
        - useClusterResolution (ucr): Sets the state of cluster deformer global resolution.  This allows clusters to be calculated at a lower resolution. Valid values are "on", "off", "interactive".
        - useLatticeResolution (ulr): Sets the state of lattice deformer global resolution.  This allows lattices to be calculated at a lower resolution. Valid values are "on", "off", "interactive".
        - query (q): Query mode flag
    """
