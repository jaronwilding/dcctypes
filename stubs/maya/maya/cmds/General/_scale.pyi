"""Stub files for General category in Maya commands, command: scale."""

from typing import Any, overload

@overload #Overload for scale in ['create']
def scale(float float float [objects]: float float float [objects], absolute: bool = ..., centerPivot: bool = ..., componentSpace: bool = ..., constrainAlongNormal: bool = ..., deletePriorHistory: bool = ..., distanceOnly: bool = ..., localSpace: bool = ..., objectCenterPivot: bool = ..., objectSpace: bool = ..., orientAxes: [angle, angle, angle] = ..., pivot: [linear, linear, linear] = ..., preserveChildPosition: bool = ..., preserveGeometryPosition: bool = ..., preserveUV: bool = ..., reflection: bool = ..., reflectionAboutBBox: bool = ..., reflectionAboutOrigin: bool = ..., reflectionAboutX: bool = ..., reflectionAboutY: bool = ..., reflectionAboutZ: bool = ..., reflectionTolerance: float = ..., relative: bool = ..., scaleX: bool = ..., scaleXY: bool = ..., scaleXYZ: bool = ..., scaleXZ: bool = ..., scaleY: bool = ..., scaleYZ: bool = ..., scaleZ: bool = ..., symNegative: bool = ..., worldSpace: bool = ..., xformConstraint: str = ...) -> None:
    """scale is undoable, NOT queryable, and NOT editable.
    
    The scale command is used to change the sizes of geometric objects.
    
    The default behaviour, when no objects or flags are passed, is to do a
    relative scale on each currently selected object object using each object's
    existing scale pivot point.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.scale( 1, 1, 1 )
        cmds.scale( 3, 3, 3, 'curve1', pivot=(1, 0, 0), absolute=True )
    ```

    ---
    - Args:
        - float float float [objects]: Input item(s).
        - absolute (a): Perform an absolute operation.
        - centerPivot (cp): Let the pivot be the center of the bounding box of all objects
        - componentSpace (cs): Move in local component space
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - deletePriorHistory (dph): If true then delete the history prior to the current operation.
        - distanceOnly (dso): Scale only the distance between the objects.
        - localSpace (ls): Use local space for scaling
        - objectCenterPivot (ocp): Let the pivot be the center of the bounding box of each object
        - objectSpace (os): Use object space for scaling
        - orientAxes (oa): Use the angles for the orient axes.
        - pivot (p): Define the pivot point for the transformation
        - preserveChildPosition (pcp): When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.
        - preserveGeometryPosition (pgp): When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.
        - preserveUV (puv): When true, UV values on scaled components are projected along the axis of scaling in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected
            vertices. Default is false.
        - reflection (rfl): To move the corresponding symmetric components also.
        - reflectionAboutBBox (rab): Sets the position of the reflection axis  at the geometry bounding box
        - reflectionAboutOrigin (rao): Sets the position of the reflection axis  at the origin
        - reflectionAboutX (rax): Specifies the X=0 as reflection plane
        - reflectionAboutY (ray): Specifies the Y=0 as reflection plane
        - reflectionAboutZ (raz): Specifies the Z=0 as reflection plane
        - reflectionTolerance (rft): Specifies the tolerance to findout the corresponding reflected components
        - relative (r): Perform a operation relative to the object's current position
        - scaleX (x): Scale in X direction
        - scaleXY (xy): Scale in X and Y direction
        - scaleXYZ (xyz): Scale in all directions (default)
        - scaleXZ (xz): Scale in X and Z direction
        - scaleY (y): Scale in Y direction
        - scaleYZ (yz): Scale in Y and Z direction
        - scaleZ (z): Scale in Z direction
        - symNegative (smn): When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.
        - worldSpace (ws): Use world space for scaling
        - xformConstraint (xc): Apply a transform constraint to moving components.none - no constraintsurface - constrain components to the surfaceedge - constrain components to surface edgeslive - constraint components to the live surface
    """
@overload #Overload for scale in ['create']
def scale(float float float [objects]: float float float [objects], a: bool = ..., cp: bool = ..., cs: bool = ..., xn: bool = ..., dph: bool = ..., dso: bool = ..., ls: bool = ..., ocp: bool = ..., os: bool = ..., oa: [angle, angle, angle] = ..., p: [linear, linear, linear] = ..., pcp: bool = ..., pgp: bool = ..., puv: bool = ..., rfl: bool = ..., rab: bool = ..., rao: bool = ..., rax: bool = ..., ray: bool = ..., raz: bool = ..., rft: float = ..., r: bool = ..., x: bool = ..., xy: bool = ..., xyz: bool = ..., xz: bool = ..., y: bool = ..., yz: bool = ..., z: bool = ..., smn: bool = ..., ws: bool = ..., xc: str = ...) -> None:
    """scale is undoable, NOT queryable, and NOT editable.
    
    The scale command is used to change the sizes of geometric objects.
    
    The default behaviour, when no objects or flags are passed, is to do a
    relative scale on each currently selected object object using each object's
    existing scale pivot point.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.scale( 1, 1, 1 )
        cmds.scale( 3, 3, 3, 'curve1', pivot=(1, 0, 0), absolute=True )
    ```

    ---
    - Args:
        - float float float [objects]: Input item(s).
        - absolute (a): Perform an absolute operation.
        - centerPivot (cp): Let the pivot be the center of the bounding box of all objects
        - componentSpace (cs): Move in local component space
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - deletePriorHistory (dph): If true then delete the history prior to the current operation.
        - distanceOnly (dso): Scale only the distance between the objects.
        - localSpace (ls): Use local space for scaling
        - objectCenterPivot (ocp): Let the pivot be the center of the bounding box of each object
        - objectSpace (os): Use object space for scaling
        - orientAxes (oa): Use the angles for the orient axes.
        - pivot (p): Define the pivot point for the transformation
        - preserveChildPosition (pcp): When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.
        - preserveGeometryPosition (pgp): When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.
        - preserveUV (puv): When true, UV values on scaled components are projected along the axis of scaling in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected
            vertices. Default is false.
        - reflection (rfl): To move the corresponding symmetric components also.
        - reflectionAboutBBox (rab): Sets the position of the reflection axis  at the geometry bounding box
        - reflectionAboutOrigin (rao): Sets the position of the reflection axis  at the origin
        - reflectionAboutX (rax): Specifies the X=0 as reflection plane
        - reflectionAboutY (ray): Specifies the Y=0 as reflection plane
        - reflectionAboutZ (raz): Specifies the Z=0 as reflection plane
        - reflectionTolerance (rft): Specifies the tolerance to findout the corresponding reflected components
        - relative (r): Perform a operation relative to the object's current position
        - scaleX (x): Scale in X direction
        - scaleXY (xy): Scale in X and Y direction
        - scaleXYZ (xyz): Scale in all directions (default)
        - scaleXZ (xz): Scale in X and Z direction
        - scaleY (y): Scale in Y direction
        - scaleYZ (yz): Scale in Y and Z direction
        - scaleZ (z): Scale in Z direction
        - symNegative (smn): When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.
        - worldSpace (ws): Use world space for scaling
        - xformConstraint (xc): Apply a transform constraint to moving components.none - no constraintsurface - constrain components to the surfaceedge - constrain components to surface edgeslive - constraint components to the live surface
    """
@overload #Overload for scale in ['create']
def scale(float float float [objects]: float float float [objects], absolute: bool = ..., a: bool = ..., centerPivot: bool = ..., cp: bool = ..., componentSpace: bool = ..., cs: bool = ..., constrainAlongNormal: bool = ..., xn: bool = ..., deletePriorHistory: bool = ..., dph: bool = ..., distanceOnly: bool = ..., dso: bool = ..., localSpace: bool = ..., ls: bool = ..., objectCenterPivot: bool = ..., ocp: bool = ..., objectSpace: bool = ..., os: bool = ..., orientAxes: [angle, angle, angle] = ..., oa: [angle, angle, angle] = ..., pivot: [linear, linear, linear] = ..., p: [linear, linear, linear] = ..., preserveChildPosition: bool = ..., pcp: bool = ..., preserveGeometryPosition: bool = ..., pgp: bool = ..., preserveUV: bool = ..., puv: bool = ..., reflection: bool = ..., rfl: bool = ..., reflectionAboutBBox: bool = ..., rab: bool = ..., reflectionAboutOrigin: bool = ..., rao: bool = ..., reflectionAboutX: bool = ..., rax: bool = ..., reflectionAboutY: bool = ..., ray: bool = ..., reflectionAboutZ: bool = ..., raz: bool = ..., reflectionTolerance: float = ..., rft: float = ..., relative: bool = ..., r: bool = ..., scaleX: bool = ..., x: bool = ..., scaleXY: bool = ..., xy: bool = ..., scaleXYZ: bool = ..., xyz: bool = ..., scaleXZ: bool = ..., xz: bool = ..., scaleY: bool = ..., y: bool = ..., scaleYZ: bool = ..., yz: bool = ..., scaleZ: bool = ..., z: bool = ..., symNegative: bool = ..., smn: bool = ..., worldSpace: bool = ..., ws: bool = ..., xformConstraint: str = ..., xc: str = ...) -> None:
    """scale is undoable, NOT queryable, and NOT editable.
    
    The scale command is used to change the sizes of geometric objects.
    
    The default behaviour, when no objects or flags are passed, is to do a
    relative scale on each currently selected object object using each object's
    existing scale pivot point.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.scale( 1, 1, 1 )
        cmds.scale( 3, 3, 3, 'curve1', pivot=(1, 0, 0), absolute=True )
    ```

    ---
    - Args:
        - float float float [objects]: Input item(s).
        - absolute (a): Perform an absolute operation.
        - centerPivot (cp): Let the pivot be the center of the bounding box of all objects
        - componentSpace (cs): Move in local component space
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - deletePriorHistory (dph): If true then delete the history prior to the current operation.
        - distanceOnly (dso): Scale only the distance between the objects.
        - localSpace (ls): Use local space for scaling
        - objectCenterPivot (ocp): Let the pivot be the center of the bounding box of each object
        - objectSpace (os): Use object space for scaling
        - orientAxes (oa): Use the angles for the orient axes.
        - pivot (p): Define the pivot point for the transformation
        - preserveChildPosition (pcp): When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.
        - preserveGeometryPosition (pgp): When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.
        - preserveUV (puv): When true, UV values on scaled components are projected along the axis of scaling in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected
            vertices. Default is false.
        - reflection (rfl): To move the corresponding symmetric components also.
        - reflectionAboutBBox (rab): Sets the position of the reflection axis  at the geometry bounding box
        - reflectionAboutOrigin (rao): Sets the position of the reflection axis  at the origin
        - reflectionAboutX (rax): Specifies the X=0 as reflection plane
        - reflectionAboutY (ray): Specifies the Y=0 as reflection plane
        - reflectionAboutZ (raz): Specifies the Z=0 as reflection plane
        - reflectionTolerance (rft): Specifies the tolerance to findout the corresponding reflected components
        - relative (r): Perform a operation relative to the object's current position
        - scaleX (x): Scale in X direction
        - scaleXY (xy): Scale in X and Y direction
        - scaleXYZ (xyz): Scale in all directions (default)
        - scaleXZ (xz): Scale in X and Z direction
        - scaleY (y): Scale in Y direction
        - scaleYZ (yz): Scale in Y and Z direction
        - scaleZ (z): Scale in Z direction
        - symNegative (smn): When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.
        - worldSpace (ws): Use world space for scaling
        - xformConstraint (xc): Apply a transform constraint to moving components.none - no constraintsurface - constrain components to the surfaceedge - constrain components to surface edgeslive - constraint components to the live surface
    """
