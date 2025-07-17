"""Stub files for Display category in Maya commands, command: displaySmoothness."""

from typing import Any, overload

@overload #Overload for displaySmoothness in ['create']
def displaySmoothness([objects]: [objects], all: bool = ..., boundary: bool = ..., defaultCreation: bool = ..., divisionsU: int = ..., divisionsV: int = ..., full: bool = ..., hull: bool = ..., pointsShaded: int = ..., pointsWire: int = ..., polygonObject: int = ..., renderTessellation: bool = ..., simplifyU: int = ..., simplifyV: int = ...) -> None:
    """displaySmoothness is undoable, queryable, and NOT editable.
    
    This command is responsible for setting the display smoothness of NURBS curves
    and surfaces to either predefined or custom values. It also sets display modes
    for smoothness such as hulls and the hull simplification factors. At present,
    this command is NOT un-doable.

    Example:
    ```python
        import maya.cmds as cmds
        # create a surface
        cmds.sphere()
        # set rough smoothness settings
        cmds.displaySmoothness( du=0, dv=0, pw=4, ps=1 )
        # set medium smoothness settings
        cmds.displaySmoothness( du=1, dv=1, pw=8, ps=2 )
        # set fine smoothness settings
        cmds.displaySmoothness( du=2, dv=2, pw=16, ps=4 )
        # Display surface as a hull
        cmds.displaySmoothness( hull=True )
        # Display with reduced number of points
        cmds.displaySmoothness( hull=True, su=2, sv=2 )
        # Display rendering tesselation
        cmds.displaySmoothness( rt=1 )
        # Set default value for pointsShaded.
        # Subsequent surfaces created will have pointsShaded as 2.
        cmds.displaySmoothness( dc=True, ps=2 )
        # displaySmoothness queries
        #
        # query hull display, returns boolean
        cmds.displaySmoothness( q=True, hull=True )
        # query default pointsShaded value
        cmds.displaySmoothness( q=True, dc=True, ps=True )
        # query surface divisionsU value
        cmds.displaySmoothness( q=True, du=True )
        # Only the -pointsWire flag works on curves.
        cmds.circle()
        # change the number of points displayed per curve span.
        cmds.displaySmoothness( pw=3 )
        # query default pointsWire value for curves.
        cmds.displaySmoothness( q=True, dc=True, pw=True )
        cmds.polyCube()
        # Query the display resolution
        cmds.displaySmoothness( q=True, polygonObject=True )
        # Result: 0
        # Change the display resolution
        cmds.displaySmoothness( polygonObject=2 )
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - all: Change smoothness for all curves and surfaces
        - boundary (bn): Display wireframe surfaces using only the boundaries of the surface Not fully implemented yet
        - defaultCreation (dc): The default values at creation (applies only -du, -dv, -pw, -ps)
        - divisionsU (du): Number of isoparm divisions per span in the U direction. The valid range of values is [0,64].
        - divisionsV (dv): Number of isoparm divisions per span in the V direction. The valid range of values is [0,64].
        - full (f): Display surface at full resolution - the default.
        - hull (hl): Display surface using the hull (control points are drawn rather than surface knot points). This mode is a useful display performance improvement when modifying a surface since it doesn't require evaluating points on the surface.
        - pointsShaded (ps): Number of points per surface span in shaded mode. The valid range of values is [1,64].
        - pointsWire (pw): Number of points per surface isoparm span or the number of points per curve span in wireframe mode. The valid range of values is [1,128]. Note: This is the only flag that also applies to nurbs curves.
        - polygonObject (po): Display the polygon objects with the given resolution
        - renderTessellation (rt): Display using render tesselation parameters when in shaded mode.
        - simplifyU (su): Number of spans to skip in the U direction when in hull display mode.
        - simplifyV (sv): Number of spans to skip in the V direction when in hull display mode.
    """
@overload #Overload for displaySmoothness in ['create']
def displaySmoothness([objects]: [objects], bn: bool = ..., dc: bool = ..., du: int = ..., dv: int = ..., f: bool = ..., hl: bool = ..., ps: int = ..., pw: int = ..., po: int = ..., rt: bool = ..., su: int = ..., sv: int = ...) -> None:
    """displaySmoothness is undoable, queryable, and NOT editable.
    
    This command is responsible for setting the display smoothness of NURBS curves
    and surfaces to either predefined or custom values. It also sets display modes
    for smoothness such as hulls and the hull simplification factors. At present,
    this command is NOT un-doable.

    Example:
    ```python
        import maya.cmds as cmds
        # create a surface
        cmds.sphere()
        # set rough smoothness settings
        cmds.displaySmoothness( du=0, dv=0, pw=4, ps=1 )
        # set medium smoothness settings
        cmds.displaySmoothness( du=1, dv=1, pw=8, ps=2 )
        # set fine smoothness settings
        cmds.displaySmoothness( du=2, dv=2, pw=16, ps=4 )
        # Display surface as a hull
        cmds.displaySmoothness( hull=True )
        # Display with reduced number of points
        cmds.displaySmoothness( hull=True, su=2, sv=2 )
        # Display rendering tesselation
        cmds.displaySmoothness( rt=1 )
        # Set default value for pointsShaded.
        # Subsequent surfaces created will have pointsShaded as 2.
        cmds.displaySmoothness( dc=True, ps=2 )
        # displaySmoothness queries
        #
        # query hull display, returns boolean
        cmds.displaySmoothness( q=True, hull=True )
        # query default pointsShaded value
        cmds.displaySmoothness( q=True, dc=True, ps=True )
        # query surface divisionsU value
        cmds.displaySmoothness( q=True, du=True )
        # Only the -pointsWire flag works on curves.
        cmds.circle()
        # change the number of points displayed per curve span.
        cmds.displaySmoothness( pw=3 )
        # query default pointsWire value for curves.
        cmds.displaySmoothness( q=True, dc=True, pw=True )
        cmds.polyCube()
        # Query the display resolution
        cmds.displaySmoothness( q=True, polygonObject=True )
        # Result: 0
        # Change the display resolution
        cmds.displaySmoothness( polygonObject=2 )
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - all: Change smoothness for all curves and surfaces
        - boundary (bn): Display wireframe surfaces using only the boundaries of the surface Not fully implemented yet
        - defaultCreation (dc): The default values at creation (applies only -du, -dv, -pw, -ps)
        - divisionsU (du): Number of isoparm divisions per span in the U direction. The valid range of values is [0,64].
        - divisionsV (dv): Number of isoparm divisions per span in the V direction. The valid range of values is [0,64].
        - full (f): Display surface at full resolution - the default.
        - hull (hl): Display surface using the hull (control points are drawn rather than surface knot points). This mode is a useful display performance improvement when modifying a surface since it doesn't require evaluating points on the surface.
        - pointsShaded (ps): Number of points per surface span in shaded mode. The valid range of values is [1,64].
        - pointsWire (pw): Number of points per surface isoparm span or the number of points per curve span in wireframe mode. The valid range of values is [1,128]. Note: This is the only flag that also applies to nurbs curves.
        - polygonObject (po): Display the polygon objects with the given resolution
        - renderTessellation (rt): Display using render tesselation parameters when in shaded mode.
        - simplifyU (su): Number of spans to skip in the U direction when in hull display mode.
        - simplifyV (sv): Number of spans to skip in the V direction when in hull display mode.
    """
@overload #Overload for displaySmoothness in ['create']
def displaySmoothness([objects]: [objects], all: bool = ..., boundary: bool = ..., bn: bool = ..., defaultCreation: bool = ..., dc: bool = ..., divisionsU: int = ..., du: int = ..., divisionsV: int = ..., dv: int = ..., full: bool = ..., f: bool = ..., hull: bool = ..., hl: bool = ..., pointsShaded: int = ..., ps: int = ..., pointsWire: int = ..., pw: int = ..., polygonObject: int = ..., po: int = ..., renderTessellation: bool = ..., rt: bool = ..., simplifyU: int = ..., su: int = ..., simplifyV: int = ..., sv: int = ...) -> None:
    """displaySmoothness is undoable, queryable, and NOT editable.
    
    This command is responsible for setting the display smoothness of NURBS curves
    and surfaces to either predefined or custom values. It also sets display modes
    for smoothness such as hulls and the hull simplification factors. At present,
    this command is NOT un-doable.

    Example:
    ```python
        import maya.cmds as cmds
        # create a surface
        cmds.sphere()
        # set rough smoothness settings
        cmds.displaySmoothness( du=0, dv=0, pw=4, ps=1 )
        # set medium smoothness settings
        cmds.displaySmoothness( du=1, dv=1, pw=8, ps=2 )
        # set fine smoothness settings
        cmds.displaySmoothness( du=2, dv=2, pw=16, ps=4 )
        # Display surface as a hull
        cmds.displaySmoothness( hull=True )
        # Display with reduced number of points
        cmds.displaySmoothness( hull=True, su=2, sv=2 )
        # Display rendering tesselation
        cmds.displaySmoothness( rt=1 )
        # Set default value for pointsShaded.
        # Subsequent surfaces created will have pointsShaded as 2.
        cmds.displaySmoothness( dc=True, ps=2 )
        # displaySmoothness queries
        #
        # query hull display, returns boolean
        cmds.displaySmoothness( q=True, hull=True )
        # query default pointsShaded value
        cmds.displaySmoothness( q=True, dc=True, ps=True )
        # query surface divisionsU value
        cmds.displaySmoothness( q=True, du=True )
        # Only the -pointsWire flag works on curves.
        cmds.circle()
        # change the number of points displayed per curve span.
        cmds.displaySmoothness( pw=3 )
        # query default pointsWire value for curves.
        cmds.displaySmoothness( q=True, dc=True, pw=True )
        cmds.polyCube()
        # Query the display resolution
        cmds.displaySmoothness( q=True, polygonObject=True )
        # Result: 0
        # Change the display resolution
        cmds.displaySmoothness( polygonObject=2 )
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - all: Change smoothness for all curves and surfaces
        - boundary (bn): Display wireframe surfaces using only the boundaries of the surface Not fully implemented yet
        - defaultCreation (dc): The default values at creation (applies only -du, -dv, -pw, -ps)
        - divisionsU (du): Number of isoparm divisions per span in the U direction. The valid range of values is [0,64].
        - divisionsV (dv): Number of isoparm divisions per span in the V direction. The valid range of values is [0,64].
        - full (f): Display surface at full resolution - the default.
        - hull (hl): Display surface using the hull (control points are drawn rather than surface knot points). This mode is a useful display performance improvement when modifying a surface since it doesn't require evaluating points on the surface.
        - pointsShaded (ps): Number of points per surface span in shaded mode. The valid range of values is [1,64].
        - pointsWire (pw): Number of points per surface isoparm span or the number of points per curve span in wireframe mode. The valid range of values is [1,128]. Note: This is the only flag that also applies to nurbs curves.
        - polygonObject (po): Display the polygon objects with the given resolution
        - renderTessellation (rt): Display using render tesselation parameters when in shaded mode.
        - simplifyU (su): Number of spans to skip in the U direction when in hull display mode.
        - simplifyV (sv): Number of spans to skip in the V direction when in hull display mode.
    """
@overload #Overload for displaySmoothness in ['query']
def displaySmoothness([objects]: [objects], all: bool = ..., boundary: bool = ..., defaultCreation: bool = ..., divisionsU: int = ..., divisionsV: int = ..., full: bool = ..., hull: bool = ..., pointsShaded: int = ..., pointsWire: int = ..., polygonObject: int = ..., renderTessellation: bool = ..., simplifyU: int = ..., simplifyV: int = ..., query: bool = ...) -> None:
    """displaySmoothness is undoable, queryable, and NOT editable.
    
    This command is responsible for setting the display smoothness of NURBS curves
    and surfaces to either predefined or custom values. It also sets display modes
    for smoothness such as hulls and the hull simplification factors. At present,
    this command is NOT un-doable.

    Example:
    ```python
        import maya.cmds as cmds
        # create a surface
        cmds.sphere()
        # set rough smoothness settings
        cmds.displaySmoothness( du=0, dv=0, pw=4, ps=1 )
        # set medium smoothness settings
        cmds.displaySmoothness( du=1, dv=1, pw=8, ps=2 )
        # set fine smoothness settings
        cmds.displaySmoothness( du=2, dv=2, pw=16, ps=4 )
        # Display surface as a hull
        cmds.displaySmoothness( hull=True )
        # Display with reduced number of points
        cmds.displaySmoothness( hull=True, su=2, sv=2 )
        # Display rendering tesselation
        cmds.displaySmoothness( rt=1 )
        # Set default value for pointsShaded.
        # Subsequent surfaces created will have pointsShaded as 2.
        cmds.displaySmoothness( dc=True, ps=2 )
        # displaySmoothness queries
        #
        # query hull display, returns boolean
        cmds.displaySmoothness( q=True, hull=True )
        # query default pointsShaded value
        cmds.displaySmoothness( q=True, dc=True, ps=True )
        # query surface divisionsU value
        cmds.displaySmoothness( q=True, du=True )
        # Only the -pointsWire flag works on curves.
        cmds.circle()
        # change the number of points displayed per curve span.
        cmds.displaySmoothness( pw=3 )
        # query default pointsWire value for curves.
        cmds.displaySmoothness( q=True, dc=True, pw=True )
        cmds.polyCube()
        # Query the display resolution
        cmds.displaySmoothness( q=True, polygonObject=True )
        # Result: 0
        # Change the display resolution
        cmds.displaySmoothness( polygonObject=2 )
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - all: Change smoothness for all curves and surfaces
        - boundary (bn): Display wireframe surfaces using only the boundaries of the surface Not fully implemented yet
        - defaultCreation (dc): The default values at creation (applies only -du, -dv, -pw, -ps)
        - divisionsU (du): Number of isoparm divisions per span in the U direction. The valid range of values is [0,64].
        - divisionsV (dv): Number of isoparm divisions per span in the V direction. The valid range of values is [0,64].
        - full (f): Display surface at full resolution - the default.
        - hull (hl): Display surface using the hull (control points are drawn rather than surface knot points). This mode is a useful display performance improvement when modifying a surface since it doesn't require evaluating points on the surface.
        - pointsShaded (ps): Number of points per surface span in shaded mode. The valid range of values is [1,64].
        - pointsWire (pw): Number of points per surface isoparm span or the number of points per curve span in wireframe mode. The valid range of values is [1,128]. Note: This is the only flag that also applies to nurbs curves.
        - polygonObject (po): Display the polygon objects with the given resolution
        - renderTessellation (rt): Display using render tesselation parameters when in shaded mode.
        - simplifyU (su): Number of spans to skip in the U direction when in hull display mode.
        - simplifyV (sv): Number of spans to skip in the V direction when in hull display mode.
        - query (q): Query mode flag
    """
@overload #Overload for displaySmoothness in ['query']
def displaySmoothness([objects]: [objects], bn: bool = ..., dc: bool = ..., du: int = ..., dv: int = ..., f: bool = ..., hl: bool = ..., ps: int = ..., pw: int = ..., po: int = ..., rt: bool = ..., su: int = ..., sv: int = ..., q: bool = ...) -> None:
    """displaySmoothness is undoable, queryable, and NOT editable.
    
    This command is responsible for setting the display smoothness of NURBS curves
    and surfaces to either predefined or custom values. It also sets display modes
    for smoothness such as hulls and the hull simplification factors. At present,
    this command is NOT un-doable.

    Example:
    ```python
        import maya.cmds as cmds
        # create a surface
        cmds.sphere()
        # set rough smoothness settings
        cmds.displaySmoothness( du=0, dv=0, pw=4, ps=1 )
        # set medium smoothness settings
        cmds.displaySmoothness( du=1, dv=1, pw=8, ps=2 )
        # set fine smoothness settings
        cmds.displaySmoothness( du=2, dv=2, pw=16, ps=4 )
        # Display surface as a hull
        cmds.displaySmoothness( hull=True )
        # Display with reduced number of points
        cmds.displaySmoothness( hull=True, su=2, sv=2 )
        # Display rendering tesselation
        cmds.displaySmoothness( rt=1 )
        # Set default value for pointsShaded.
        # Subsequent surfaces created will have pointsShaded as 2.
        cmds.displaySmoothness( dc=True, ps=2 )
        # displaySmoothness queries
        #
        # query hull display, returns boolean
        cmds.displaySmoothness( q=True, hull=True )
        # query default pointsShaded value
        cmds.displaySmoothness( q=True, dc=True, ps=True )
        # query surface divisionsU value
        cmds.displaySmoothness( q=True, du=True )
        # Only the -pointsWire flag works on curves.
        cmds.circle()
        # change the number of points displayed per curve span.
        cmds.displaySmoothness( pw=3 )
        # query default pointsWire value for curves.
        cmds.displaySmoothness( q=True, dc=True, pw=True )
        cmds.polyCube()
        # Query the display resolution
        cmds.displaySmoothness( q=True, polygonObject=True )
        # Result: 0
        # Change the display resolution
        cmds.displaySmoothness( polygonObject=2 )
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - all: Change smoothness for all curves and surfaces
        - boundary (bn): Display wireframe surfaces using only the boundaries of the surface Not fully implemented yet
        - defaultCreation (dc): The default values at creation (applies only -du, -dv, -pw, -ps)
        - divisionsU (du): Number of isoparm divisions per span in the U direction. The valid range of values is [0,64].
        - divisionsV (dv): Number of isoparm divisions per span in the V direction. The valid range of values is [0,64].
        - full (f): Display surface at full resolution - the default.
        - hull (hl): Display surface using the hull (control points are drawn rather than surface knot points). This mode is a useful display performance improvement when modifying a surface since it doesn't require evaluating points on the surface.
        - pointsShaded (ps): Number of points per surface span in shaded mode. The valid range of values is [1,64].
        - pointsWire (pw): Number of points per surface isoparm span or the number of points per curve span in wireframe mode. The valid range of values is [1,128]. Note: This is the only flag that also applies to nurbs curves.
        - polygonObject (po): Display the polygon objects with the given resolution
        - renderTessellation (rt): Display using render tesselation parameters when in shaded mode.
        - simplifyU (su): Number of spans to skip in the U direction when in hull display mode.
        - simplifyV (sv): Number of spans to skip in the V direction when in hull display mode.
        - query (q): Query mode flag
    """
@overload #Overload for displaySmoothness in ['query']
def displaySmoothness([objects]: [objects], all: bool = ..., boundary: bool = ..., bn: bool = ..., defaultCreation: bool = ..., dc: bool = ..., divisionsU: int = ..., du: int = ..., divisionsV: int = ..., dv: int = ..., full: bool = ..., f: bool = ..., hull: bool = ..., hl: bool = ..., pointsShaded: int = ..., ps: int = ..., pointsWire: int = ..., pw: int = ..., polygonObject: int = ..., po: int = ..., renderTessellation: bool = ..., rt: bool = ..., simplifyU: int = ..., su: int = ..., simplifyV: int = ..., sv: int = ..., query: bool = ..., q: bool = ...) -> None:
    """displaySmoothness is undoable, queryable, and NOT editable.
    
    This command is responsible for setting the display smoothness of NURBS curves
    and surfaces to either predefined or custom values. It also sets display modes
    for smoothness such as hulls and the hull simplification factors. At present,
    this command is NOT un-doable.

    Example:
    ```python
        import maya.cmds as cmds
        # create a surface
        cmds.sphere()
        # set rough smoothness settings
        cmds.displaySmoothness( du=0, dv=0, pw=4, ps=1 )
        # set medium smoothness settings
        cmds.displaySmoothness( du=1, dv=1, pw=8, ps=2 )
        # set fine smoothness settings
        cmds.displaySmoothness( du=2, dv=2, pw=16, ps=4 )
        # Display surface as a hull
        cmds.displaySmoothness( hull=True )
        # Display with reduced number of points
        cmds.displaySmoothness( hull=True, su=2, sv=2 )
        # Display rendering tesselation
        cmds.displaySmoothness( rt=1 )
        # Set default value for pointsShaded.
        # Subsequent surfaces created will have pointsShaded as 2.
        cmds.displaySmoothness( dc=True, ps=2 )
        # displaySmoothness queries
        #
        # query hull display, returns boolean
        cmds.displaySmoothness( q=True, hull=True )
        # query default pointsShaded value
        cmds.displaySmoothness( q=True, dc=True, ps=True )
        # query surface divisionsU value
        cmds.displaySmoothness( q=True, du=True )
        # Only the -pointsWire flag works on curves.
        cmds.circle()
        # change the number of points displayed per curve span.
        cmds.displaySmoothness( pw=3 )
        # query default pointsWire value for curves.
        cmds.displaySmoothness( q=True, dc=True, pw=True )
        cmds.polyCube()
        # Query the display resolution
        cmds.displaySmoothness( q=True, polygonObject=True )
        # Result: 0
        # Change the display resolution
        cmds.displaySmoothness( polygonObject=2 )
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - all: Change smoothness for all curves and surfaces
        - boundary (bn): Display wireframe surfaces using only the boundaries of the surface Not fully implemented yet
        - defaultCreation (dc): The default values at creation (applies only -du, -dv, -pw, -ps)
        - divisionsU (du): Number of isoparm divisions per span in the U direction. The valid range of values is [0,64].
        - divisionsV (dv): Number of isoparm divisions per span in the V direction. The valid range of values is [0,64].
        - full (f): Display surface at full resolution - the default.
        - hull (hl): Display surface using the hull (control points are drawn rather than surface knot points). This mode is a useful display performance improvement when modifying a surface since it doesn't require evaluating points on the surface.
        - pointsShaded (ps): Number of points per surface span in shaded mode. The valid range of values is [1,64].
        - pointsWire (pw): Number of points per surface isoparm span or the number of points per curve span in wireframe mode. The valid range of values is [1,128]. Note: This is the only flag that also applies to nurbs curves.
        - polygonObject (po): Display the polygon objects with the given resolution
        - renderTessellation (rt): Display using render tesselation parameters when in shaded mode.
        - simplifyU (su): Number of spans to skip in the U direction when in hull display mode.
        - simplifyV (sv): Number of spans to skip in the V direction when in hull display mode.
        - query (q): Query mode flag
    """
