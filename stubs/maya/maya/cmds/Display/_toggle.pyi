"""Stub files for Display category in Maya commands, command: toggle."""

from typing import Any, overload

@overload #Overload for toggle in ['create']
def toggle([objects]: [objects], above: bool = ..., below: bool = ..., boundary: bool = ..., boundingBox: bool = ..., controlVertex: bool = ..., doNotWrite: bool = ..., editPoint: bool = ..., extent: bool = ..., facet: bool = ..., geometry: bool = ..., gl: bool = ..., highPrecisionNurbs: bool = ..., hull: bool = ..., latticePoint: bool = ..., latticeShape: bool = ..., localAxis: bool = ..., newCurve: bool = ..., newPolymesh: bool = ..., newSurface: bool = ..., normal: bool = ..., origin: bool = ..., point: bool = ..., pointDisplay: bool = ..., pointFacet: bool = ..., rotatePivot: bool = ..., scalePivot: bool = ..., selectHandle: bool = ..., state: bool = ..., surfaceFace: bool = ..., template: bool = ..., uvCoords: bool = ..., vertex: bool = ...) -> bool:
    """toggle is undoable, queryable, and NOT editable.
    
    The toggle command is used to toggle the display of various object features
    for objects which have these components. For example, CV and edit point
    display may be toggled for those listed NURB curves or surfaces.
    
    Note: This command is not undoable.

    Example:
    ```python
        import maya.cmds as cmds
        surface1 = cmds.sphere()
        cmds.toggle( surface1, cv=True )
        cmds.toggle( g=True, cv=True )
        cmds.toggle( q=True, cv=True )
        # Returns 0 if the queried state is false.
        # Returns 1 if the queried state is true.
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - above (a): Toggle state for all objects above listed objects.
        - below (b): Toggle state for all objects below listed objects.
        - boundary (bn): Toggle boundary display of listed mesh objects.
        - boundingBox (box): Toggle or query the bounding box display of listed objects.
        - controlVertex (cv): Toggle CV display of listed curves and surfaces.
        - doNotWrite (dnw): Toggle the "this should be written to the file" state.
        - editPoint (ep): Toggle edit point display of listed curves and surfaces.
        - extent (et): Toggle display of extents of listed mesh objects.
        - facet (f): For use withnormalflag. Set the normal display style to facet display.
        - geometry (g): Toggle geometry display of listed objects.
        - gl: Toggle state for all objects
        - highPrecisionNurbs (hpn): Toggle high precision display for Nurbs
        - hull (hl): Toggle hull display of listed curves and surfaces.
        - latticePoint (lp): Toggle point display of listed lattices
        - latticeShape (ls): Toggle display of listed lattices
        - localAxis (la): Toggle local axis display of listed objects.
        - newCurve (nc): Set component display state of new curve objects
        - newPolymesh (np): Set component display state of new polymesh objects
        - newSurface (ns): Set component display state of new surface objects
        - normal (nr): Toggle display of normals of listed surface and mesh objects.
        - origin (o): Toggle origin display of listed surfaces.
        - point (pt): For use withnormal flag. Set the normal display style to vertex display.
        - pointDisplay (pd): Toggle point display of listed surfaces.
        - pointFacet (pf): For use withnormalflag. Set the normal display style to vertex and face display.
        - rotatePivot (rp): Toggle rotate pivot display of listed objects.
        - scalePivot (sp): Toggle scale pivot display of listed objects.
        - selectHandle (sh): Toggle select handle display of listed objects.
        - state (st): Explicitly set the state to true or false instead of toggling the state. Can not be queried.
        - surfaceFace (sf): Toggle surface face handle display of listed surfaces.
        - template (te): Toggle template state of listed objects
        - uvCoords (uv): Toggle display uv coords of listed mesh objects.
        - vertex (vt): Toggle vertex display of listed mesh objects.
    """
@overload #Overload for toggle in ['create']
def toggle([objects]: [objects], a: bool = ..., b: bool = ..., bn: bool = ..., box: bool = ..., cv: bool = ..., dnw: bool = ..., ep: bool = ..., et: bool = ..., f: bool = ..., g: bool = ..., hpn: bool = ..., hl: bool = ..., lp: bool = ..., ls: bool = ..., la: bool = ..., nc: bool = ..., np: bool = ..., ns: bool = ..., nr: bool = ..., o: bool = ..., pt: bool = ..., pd: bool = ..., pf: bool = ..., rp: bool = ..., sp: bool = ..., sh: bool = ..., st: bool = ..., sf: bool = ..., te: bool = ..., uv: bool = ..., vt: bool = ...) -> bool:
    """toggle is undoable, queryable, and NOT editable.
    
    The toggle command is used to toggle the display of various object features
    for objects which have these components. For example, CV and edit point
    display may be toggled for those listed NURB curves or surfaces.
    
    Note: This command is not undoable.

    Example:
    ```python
        import maya.cmds as cmds
        surface1 = cmds.sphere()
        cmds.toggle( surface1, cv=True )
        cmds.toggle( g=True, cv=True )
        cmds.toggle( q=True, cv=True )
        # Returns 0 if the queried state is false.
        # Returns 1 if the queried state is true.
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - above (a): Toggle state for all objects above listed objects.
        - below (b): Toggle state for all objects below listed objects.
        - boundary (bn): Toggle boundary display of listed mesh objects.
        - boundingBox (box): Toggle or query the bounding box display of listed objects.
        - controlVertex (cv): Toggle CV display of listed curves and surfaces.
        - doNotWrite (dnw): Toggle the "this should be written to the file" state.
        - editPoint (ep): Toggle edit point display of listed curves and surfaces.
        - extent (et): Toggle display of extents of listed mesh objects.
        - facet (f): For use withnormalflag. Set the normal display style to facet display.
        - geometry (g): Toggle geometry display of listed objects.
        - gl: Toggle state for all objects
        - highPrecisionNurbs (hpn): Toggle high precision display for Nurbs
        - hull (hl): Toggle hull display of listed curves and surfaces.
        - latticePoint (lp): Toggle point display of listed lattices
        - latticeShape (ls): Toggle display of listed lattices
        - localAxis (la): Toggle local axis display of listed objects.
        - newCurve (nc): Set component display state of new curve objects
        - newPolymesh (np): Set component display state of new polymesh objects
        - newSurface (ns): Set component display state of new surface objects
        - normal (nr): Toggle display of normals of listed surface and mesh objects.
        - origin (o): Toggle origin display of listed surfaces.
        - point (pt): For use withnormal flag. Set the normal display style to vertex display.
        - pointDisplay (pd): Toggle point display of listed surfaces.
        - pointFacet (pf): For use withnormalflag. Set the normal display style to vertex and face display.
        - rotatePivot (rp): Toggle rotate pivot display of listed objects.
        - scalePivot (sp): Toggle scale pivot display of listed objects.
        - selectHandle (sh): Toggle select handle display of listed objects.
        - state (st): Explicitly set the state to true or false instead of toggling the state. Can not be queried.
        - surfaceFace (sf): Toggle surface face handle display of listed surfaces.
        - template (te): Toggle template state of listed objects
        - uvCoords (uv): Toggle display uv coords of listed mesh objects.
        - vertex (vt): Toggle vertex display of listed mesh objects.
    """
@overload #Overload for toggle in ['create']
def toggle([objects]: [objects], above: bool = ..., a: bool = ..., below: bool = ..., b: bool = ..., boundary: bool = ..., bn: bool = ..., boundingBox: bool = ..., box: bool = ..., controlVertex: bool = ..., cv: bool = ..., doNotWrite: bool = ..., dnw: bool = ..., editPoint: bool = ..., ep: bool = ..., extent: bool = ..., et: bool = ..., facet: bool = ..., f: bool = ..., geometry: bool = ..., g: bool = ..., gl: bool = ..., highPrecisionNurbs: bool = ..., hpn: bool = ..., hull: bool = ..., hl: bool = ..., latticePoint: bool = ..., lp: bool = ..., latticeShape: bool = ..., ls: bool = ..., localAxis: bool = ..., la: bool = ..., newCurve: bool = ..., nc: bool = ..., newPolymesh: bool = ..., np: bool = ..., newSurface: bool = ..., ns: bool = ..., normal: bool = ..., nr: bool = ..., origin: bool = ..., o: bool = ..., point: bool = ..., pt: bool = ..., pointDisplay: bool = ..., pd: bool = ..., pointFacet: bool = ..., pf: bool = ..., rotatePivot: bool = ..., rp: bool = ..., scalePivot: bool = ..., sp: bool = ..., selectHandle: bool = ..., sh: bool = ..., state: bool = ..., st: bool = ..., surfaceFace: bool = ..., sf: bool = ..., template: bool = ..., te: bool = ..., uvCoords: bool = ..., uv: bool = ..., vertex: bool = ..., vt: bool = ...) -> bool:
    """toggle is undoable, queryable, and NOT editable.
    
    The toggle command is used to toggle the display of various object features
    for objects which have these components. For example, CV and edit point
    display may be toggled for those listed NURB curves or surfaces.
    
    Note: This command is not undoable.

    Example:
    ```python
        import maya.cmds as cmds
        surface1 = cmds.sphere()
        cmds.toggle( surface1, cv=True )
        cmds.toggle( g=True, cv=True )
        cmds.toggle( q=True, cv=True )
        # Returns 0 if the queried state is false.
        # Returns 1 if the queried state is true.
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - above (a): Toggle state for all objects above listed objects.
        - below (b): Toggle state for all objects below listed objects.
        - boundary (bn): Toggle boundary display of listed mesh objects.
        - boundingBox (box): Toggle or query the bounding box display of listed objects.
        - controlVertex (cv): Toggle CV display of listed curves and surfaces.
        - doNotWrite (dnw): Toggle the "this should be written to the file" state.
        - editPoint (ep): Toggle edit point display of listed curves and surfaces.
        - extent (et): Toggle display of extents of listed mesh objects.
        - facet (f): For use withnormalflag. Set the normal display style to facet display.
        - geometry (g): Toggle geometry display of listed objects.
        - gl: Toggle state for all objects
        - highPrecisionNurbs (hpn): Toggle high precision display for Nurbs
        - hull (hl): Toggle hull display of listed curves and surfaces.
        - latticePoint (lp): Toggle point display of listed lattices
        - latticeShape (ls): Toggle display of listed lattices
        - localAxis (la): Toggle local axis display of listed objects.
        - newCurve (nc): Set component display state of new curve objects
        - newPolymesh (np): Set component display state of new polymesh objects
        - newSurface (ns): Set component display state of new surface objects
        - normal (nr): Toggle display of normals of listed surface and mesh objects.
        - origin (o): Toggle origin display of listed surfaces.
        - point (pt): For use withnormal flag. Set the normal display style to vertex display.
        - pointDisplay (pd): Toggle point display of listed surfaces.
        - pointFacet (pf): For use withnormalflag. Set the normal display style to vertex and face display.
        - rotatePivot (rp): Toggle rotate pivot display of listed objects.
        - scalePivot (sp): Toggle scale pivot display of listed objects.
        - selectHandle (sh): Toggle select handle display of listed objects.
        - state (st): Explicitly set the state to true or false instead of toggling the state. Can not be queried.
        - surfaceFace (sf): Toggle surface face handle display of listed surfaces.
        - template (te): Toggle template state of listed objects
        - uvCoords (uv): Toggle display uv coords of listed mesh objects.
        - vertex (vt): Toggle vertex display of listed mesh objects.
    """
@overload #Overload for toggle in ['query']
def toggle([objects]: [objects], boundary: bool = ..., boundingBox: bool = ..., controlVertex: bool = ..., doNotWrite: bool = ..., editPoint: bool = ..., extent: bool = ..., facet: bool = ..., geometry: bool = ..., highPrecisionNurbs: bool = ..., hull: bool = ..., latticePoint: bool = ..., latticeShape: bool = ..., localAxis: bool = ..., newCurve: bool = ..., newPolymesh: bool = ..., newSurface: bool = ..., normal: bool = ..., origin: bool = ..., point: bool = ..., pointDisplay: bool = ..., pointFacet: bool = ..., rotatePivot: bool = ..., scalePivot: bool = ..., selectHandle: bool = ..., surfaceFace: bool = ..., template: bool = ..., uvCoords: bool = ..., vertex: bool = ..., query: bool = ...) -> bool:
    """toggle is undoable, queryable, and NOT editable.
    
    The toggle command is used to toggle the display of various object features
    for objects which have these components. For example, CV and edit point
    display may be toggled for those listed NURB curves or surfaces.
    
    Note: This command is not undoable.

    Example:
    ```python
        import maya.cmds as cmds
        surface1 = cmds.sphere()
        cmds.toggle( surface1, cv=True )
        cmds.toggle( g=True, cv=True )
        cmds.toggle( q=True, cv=True )
        # Returns 0 if the queried state is false.
        # Returns 1 if the queried state is true.
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - boundary (bn): Toggle boundary display of listed mesh objects.
        - boundingBox (box): Toggle or query the bounding box display of listed objects.
        - controlVertex (cv): Toggle CV display of listed curves and surfaces.
        - doNotWrite (dnw): Toggle the "this should be written to the file" state.
        - editPoint (ep): Toggle edit point display of listed curves and surfaces.
        - extent (et): Toggle display of extents of listed mesh objects.
        - facet (f): For use withnormalflag. Set the normal display style to facet display.
        - geometry (g): Toggle geometry display of listed objects.
        - highPrecisionNurbs (hpn): Toggle high precision display for Nurbs
        - hull (hl): Toggle hull display of listed curves and surfaces.
        - latticePoint (lp): Toggle point display of listed lattices
        - latticeShape (ls): Toggle display of listed lattices
        - localAxis (la): Toggle local axis display of listed objects.
        - newCurve (nc): Set component display state of new curve objects
        - newPolymesh (np): Set component display state of new polymesh objects
        - newSurface (ns): Set component display state of new surface objects
        - normal (nr): Toggle display of normals of listed surface and mesh objects.
        - origin (o): Toggle origin display of listed surfaces.
        - point (pt): For use withnormal flag. Set the normal display style to vertex display.
        - pointDisplay (pd): Toggle point display of listed surfaces.
        - pointFacet (pf): For use withnormalflag. Set the normal display style to vertex and face display.
        - rotatePivot (rp): Toggle rotate pivot display of listed objects.
        - scalePivot (sp): Toggle scale pivot display of listed objects.
        - selectHandle (sh): Toggle select handle display of listed objects.
        - surfaceFace (sf): Toggle surface face handle display of listed surfaces.
        - template (te): Toggle template state of listed objects
        - uvCoords (uv): Toggle display uv coords of listed mesh objects.
        - vertex (vt): Toggle vertex display of listed mesh objects.
        - query (q): Query mode flag
    """
@overload #Overload for toggle in ['query']
def toggle([objects]: [objects], bn: bool = ..., box: bool = ..., cv: bool = ..., dnw: bool = ..., ep: bool = ..., et: bool = ..., f: bool = ..., g: bool = ..., hpn: bool = ..., hl: bool = ..., lp: bool = ..., ls: bool = ..., la: bool = ..., nc: bool = ..., np: bool = ..., ns: bool = ..., nr: bool = ..., o: bool = ..., pt: bool = ..., pd: bool = ..., pf: bool = ..., rp: bool = ..., sp: bool = ..., sh: bool = ..., sf: bool = ..., te: bool = ..., uv: bool = ..., vt: bool = ..., q: bool = ...) -> bool:
    """toggle is undoable, queryable, and NOT editable.
    
    The toggle command is used to toggle the display of various object features
    for objects which have these components. For example, CV and edit point
    display may be toggled for those listed NURB curves or surfaces.
    
    Note: This command is not undoable.

    Example:
    ```python
        import maya.cmds as cmds
        surface1 = cmds.sphere()
        cmds.toggle( surface1, cv=True )
        cmds.toggle( g=True, cv=True )
        cmds.toggle( q=True, cv=True )
        # Returns 0 if the queried state is false.
        # Returns 1 if the queried state is true.
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - boundary (bn): Toggle boundary display of listed mesh objects.
        - boundingBox (box): Toggle or query the bounding box display of listed objects.
        - controlVertex (cv): Toggle CV display of listed curves and surfaces.
        - doNotWrite (dnw): Toggle the "this should be written to the file" state.
        - editPoint (ep): Toggle edit point display of listed curves and surfaces.
        - extent (et): Toggle display of extents of listed mesh objects.
        - facet (f): For use withnormalflag. Set the normal display style to facet display.
        - geometry (g): Toggle geometry display of listed objects.
        - highPrecisionNurbs (hpn): Toggle high precision display for Nurbs
        - hull (hl): Toggle hull display of listed curves and surfaces.
        - latticePoint (lp): Toggle point display of listed lattices
        - latticeShape (ls): Toggle display of listed lattices
        - localAxis (la): Toggle local axis display of listed objects.
        - newCurve (nc): Set component display state of new curve objects
        - newPolymesh (np): Set component display state of new polymesh objects
        - newSurface (ns): Set component display state of new surface objects
        - normal (nr): Toggle display of normals of listed surface and mesh objects.
        - origin (o): Toggle origin display of listed surfaces.
        - point (pt): For use withnormal flag. Set the normal display style to vertex display.
        - pointDisplay (pd): Toggle point display of listed surfaces.
        - pointFacet (pf): For use withnormalflag. Set the normal display style to vertex and face display.
        - rotatePivot (rp): Toggle rotate pivot display of listed objects.
        - scalePivot (sp): Toggle scale pivot display of listed objects.
        - selectHandle (sh): Toggle select handle display of listed objects.
        - surfaceFace (sf): Toggle surface face handle display of listed surfaces.
        - template (te): Toggle template state of listed objects
        - uvCoords (uv): Toggle display uv coords of listed mesh objects.
        - vertex (vt): Toggle vertex display of listed mesh objects.
        - query (q): Query mode flag
    """
@overload #Overload for toggle in ['query']
def toggle([objects]: [objects], boundary: bool = ..., bn: bool = ..., boundingBox: bool = ..., box: bool = ..., controlVertex: bool = ..., cv: bool = ..., doNotWrite: bool = ..., dnw: bool = ..., editPoint: bool = ..., ep: bool = ..., extent: bool = ..., et: bool = ..., facet: bool = ..., f: bool = ..., geometry: bool = ..., g: bool = ..., highPrecisionNurbs: bool = ..., hpn: bool = ..., hull: bool = ..., hl: bool = ..., latticePoint: bool = ..., lp: bool = ..., latticeShape: bool = ..., ls: bool = ..., localAxis: bool = ..., la: bool = ..., newCurve: bool = ..., nc: bool = ..., newPolymesh: bool = ..., np: bool = ..., newSurface: bool = ..., ns: bool = ..., normal: bool = ..., nr: bool = ..., origin: bool = ..., o: bool = ..., point: bool = ..., pt: bool = ..., pointDisplay: bool = ..., pd: bool = ..., pointFacet: bool = ..., pf: bool = ..., rotatePivot: bool = ..., rp: bool = ..., scalePivot: bool = ..., sp: bool = ..., selectHandle: bool = ..., sh: bool = ..., surfaceFace: bool = ..., sf: bool = ..., template: bool = ..., te: bool = ..., uvCoords: bool = ..., uv: bool = ..., vertex: bool = ..., vt: bool = ..., query: bool = ..., q: bool = ...) -> bool:
    """toggle is undoable, queryable, and NOT editable.
    
    The toggle command is used to toggle the display of various object features
    for objects which have these components. For example, CV and edit point
    display may be toggled for those listed NURB curves or surfaces.
    
    Note: This command is not undoable.

    Example:
    ```python
        import maya.cmds as cmds
        surface1 = cmds.sphere()
        cmds.toggle( surface1, cv=True )
        cmds.toggle( g=True, cv=True )
        cmds.toggle( q=True, cv=True )
        # Returns 0 if the queried state is false.
        # Returns 1 if the queried state is true.
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - boundary (bn): Toggle boundary display of listed mesh objects.
        - boundingBox (box): Toggle or query the bounding box display of listed objects.
        - controlVertex (cv): Toggle CV display of listed curves and surfaces.
        - doNotWrite (dnw): Toggle the "this should be written to the file" state.
        - editPoint (ep): Toggle edit point display of listed curves and surfaces.
        - extent (et): Toggle display of extents of listed mesh objects.
        - facet (f): For use withnormalflag. Set the normal display style to facet display.
        - geometry (g): Toggle geometry display of listed objects.
        - highPrecisionNurbs (hpn): Toggle high precision display for Nurbs
        - hull (hl): Toggle hull display of listed curves and surfaces.
        - latticePoint (lp): Toggle point display of listed lattices
        - latticeShape (ls): Toggle display of listed lattices
        - localAxis (la): Toggle local axis display of listed objects.
        - newCurve (nc): Set component display state of new curve objects
        - newPolymesh (np): Set component display state of new polymesh objects
        - newSurface (ns): Set component display state of new surface objects
        - normal (nr): Toggle display of normals of listed surface and mesh objects.
        - origin (o): Toggle origin display of listed surfaces.
        - point (pt): For use withnormal flag. Set the normal display style to vertex display.
        - pointDisplay (pd): Toggle point display of listed surfaces.
        - pointFacet (pf): For use withnormalflag. Set the normal display style to vertex and face display.
        - rotatePivot (rp): Toggle rotate pivot display of listed objects.
        - scalePivot (sp): Toggle scale pivot display of listed objects.
        - selectHandle (sh): Toggle select handle display of listed objects.
        - surfaceFace (sf): Toggle surface face handle display of listed surfaces.
        - template (te): Toggle template state of listed objects
        - uvCoords (uv): Toggle display uv coords of listed mesh objects.
        - vertex (vt): Toggle vertex display of listed mesh objects.
        - query (q): Query mode flag
    """
