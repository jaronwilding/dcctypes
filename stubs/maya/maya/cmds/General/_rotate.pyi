"""Stub files for General category in Maya commands, command: rotate."""

from typing import Any, overload

@overload #Overload for rotate in ['create']
def rotate(float float float [objects]: float float float [objects], absolute: bool = ..., centerPivot: bool = ..., componentSpace: bool = ..., constrainAlongNormal: bool = ..., deletePriorHistory: bool = ..., euler: bool = ..., forceOrderXYZ: bool = ..., objectCenterPivot: bool = ..., objectSpace: bool = ..., orientAxes: [angle, angle, angle] = ..., pivot: [linear, linear, linear] = ..., preserveChildPosition: bool = ..., preserveGeometryPosition: bool = ..., preserveUV: bool = ..., reflection: bool = ..., reflectionAboutBBox: bool = ..., reflectionAboutOrigin: bool = ..., reflectionAboutX: bool = ..., reflectionAboutY: bool = ..., reflectionAboutZ: bool = ..., reflectionTolerance: float = ..., relative: bool = ..., rotateX: bool = ..., rotateXY: bool = ..., rotateXYZ: bool = ..., rotateXZ: bool = ..., rotateY: bool = ..., rotateYZ: bool = ..., rotateZ: bool = ..., symNegative: bool = ..., translate: bool = ..., worldSpace: bool = ..., xformConstraint: str = ...) -> None:
    """rotate is undoable, NOT queryable, and NOT editable.
    
    The rotate command is used to change the rotation of geometric objects. The
    rotation values are specified as Euler angles (rx, ry, rz). The values are
    interpreted based on the current working unit for Angular measurements. Most
    often this is degrees.
    
    The default behaviour, when no objects or flags are passed, is to do a
    absolute rotate on each currently selected object in the world space.

    ---
    - Args:
        - float float float [objects]: Input item(s).
        - absolute (a): Perform an absolute operation.
        - centerPivot (cp): Let the pivot be the center of the bounding box of all objects
        - componentSpace (cs): Rotate in local component space
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - deletePriorHistory (dph): If true then delete the history prior to the current operation.
        - euler (eu): Modifer for -relative flag that specifies rotation values should be added to current XYZ rotation values.
        - forceOrderXYZ (fo): When true, euler rotation value will be understood in XYZ rotation order not per transform node basis.
        - objectCenterPivot (ocp): Let the pivot be the center of the bounding box of each object
        - objectSpace (os): Perform rotation about object-space axis.
        - orientAxes (oa): Euler axis for orientation.
        - pivot (p): Define the pivot point for the transformation
        - preserveChildPosition (pcp): When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.
        - preserveGeometryPosition (pgp): When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.
        - preserveUV (puv): When true, UV values on rotated components are projected across the rotation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices.
            Default is false.
        - reflection (rfl): To move the corresponding symmetric components also.
        - reflectionAboutBBox (rab): Sets the position of the reflection axis  at the geometry bounding box
        - reflectionAboutOrigin (rao): Sets the position of the reflection axis  at the origin
        - reflectionAboutX (rax): Specifies the X=0 as reflection plane
        - reflectionAboutY (ray): Specifies the Y=0 as reflection plane
        - reflectionAboutZ (raz): Specifies the Z=0 as reflection plane
        - reflectionTolerance (rft): Specifies the tolerance to findout the corresponding reflected components
        - relative (r): Perform a operation relative to the object's current position
        - rotateX (x): Rotate in X direction
        - rotateXY (xy): Rotate in X and Y direction
        - rotateXYZ (xyz): Rotate in all directions (default)
        - rotateXZ (xz): Rotate in X and Z direction
        - rotateY (y): Rotate in Y direction
        - rotateYZ (yz): Rotate in Y and Z direction
        - rotateZ (z): Rotate in Z direction
        - symNegative (smn): When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.
        - translate (t): When true, the command will modify the node's translate attribute instead of its rotateTranslate attribute, when rotating around a pivot other than the object's own rotate pivot.
        - worldSpace (ws): Perform rotation about global world-space axis.
        - xformConstraint (xc): Apply a transform constraint to moving components.none - no constraintsurface - constrain components to the surfaceedge - constrain components to surface edgeslive - constraint components to the live surface
    """
@overload #Overload for rotate in ['create']
def rotate(float float float [objects]: float float float [objects], a: bool = ..., cp: bool = ..., cs: bool = ..., xn: bool = ..., dph: bool = ..., eu: bool = ..., fo: bool = ..., ocp: bool = ..., os: bool = ..., oa: [angle, angle, angle] = ..., p: [linear, linear, linear] = ..., pcp: bool = ..., pgp: bool = ..., puv: bool = ..., rfl: bool = ..., rab: bool = ..., rao: bool = ..., rax: bool = ..., ray: bool = ..., raz: bool = ..., rft: float = ..., r: bool = ..., x: bool = ..., xy: bool = ..., xyz: bool = ..., xz: bool = ..., y: bool = ..., yz: bool = ..., z: bool = ..., smn: bool = ..., t: bool = ..., ws: bool = ..., xc: str = ...) -> None:
    """rotate is undoable, NOT queryable, and NOT editable.
    
    The rotate command is used to change the rotation of geometric objects. The
    rotation values are specified as Euler angles (rx, ry, rz). The values are
    interpreted based on the current working unit for Angular measurements. Most
    often this is degrees.
    
    The default behaviour, when no objects or flags are passed, is to do a
    absolute rotate on each currently selected object in the world space.

    ---
    - Args:
        - float float float [objects]: Input item(s).
        - absolute (a): Perform an absolute operation.
        - centerPivot (cp): Let the pivot be the center of the bounding box of all objects
        - componentSpace (cs): Rotate in local component space
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - deletePriorHistory (dph): If true then delete the history prior to the current operation.
        - euler (eu): Modifer for -relative flag that specifies rotation values should be added to current XYZ rotation values.
        - forceOrderXYZ (fo): When true, euler rotation value will be understood in XYZ rotation order not per transform node basis.
        - objectCenterPivot (ocp): Let the pivot be the center of the bounding box of each object
        - objectSpace (os): Perform rotation about object-space axis.
        - orientAxes (oa): Euler axis for orientation.
        - pivot (p): Define the pivot point for the transformation
        - preserveChildPosition (pcp): When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.
        - preserveGeometryPosition (pgp): When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.
        - preserveUV (puv): When true, UV values on rotated components are projected across the rotation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices.
            Default is false.
        - reflection (rfl): To move the corresponding symmetric components also.
        - reflectionAboutBBox (rab): Sets the position of the reflection axis  at the geometry bounding box
        - reflectionAboutOrigin (rao): Sets the position of the reflection axis  at the origin
        - reflectionAboutX (rax): Specifies the X=0 as reflection plane
        - reflectionAboutY (ray): Specifies the Y=0 as reflection plane
        - reflectionAboutZ (raz): Specifies the Z=0 as reflection plane
        - reflectionTolerance (rft): Specifies the tolerance to findout the corresponding reflected components
        - relative (r): Perform a operation relative to the object's current position
        - rotateX (x): Rotate in X direction
        - rotateXY (xy): Rotate in X and Y direction
        - rotateXYZ (xyz): Rotate in all directions (default)
        - rotateXZ (xz): Rotate in X and Z direction
        - rotateY (y): Rotate in Y direction
        - rotateYZ (yz): Rotate in Y and Z direction
        - rotateZ (z): Rotate in Z direction
        - symNegative (smn): When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.
        - translate (t): When true, the command will modify the node's translate attribute instead of its rotateTranslate attribute, when rotating around a pivot other than the object's own rotate pivot.
        - worldSpace (ws): Perform rotation about global world-space axis.
        - xformConstraint (xc): Apply a transform constraint to moving components.none - no constraintsurface - constrain components to the surfaceedge - constrain components to surface edgeslive - constraint components to the live surface
    """
@overload #Overload for rotate in ['create']
def rotate(float float float [objects]: float float float [objects], absolute: bool = ..., a: bool = ..., centerPivot: bool = ..., cp: bool = ..., componentSpace: bool = ..., cs: bool = ..., constrainAlongNormal: bool = ..., xn: bool = ..., deletePriorHistory: bool = ..., dph: bool = ..., euler: bool = ..., eu: bool = ..., forceOrderXYZ: bool = ..., fo: bool = ..., objectCenterPivot: bool = ..., ocp: bool = ..., objectSpace: bool = ..., os: bool = ..., orientAxes: [angle, angle, angle] = ..., oa: [angle, angle, angle] = ..., pivot: [linear, linear, linear] = ..., p: [linear, linear, linear] = ..., preserveChildPosition: bool = ..., pcp: bool = ..., preserveGeometryPosition: bool = ..., pgp: bool = ..., preserveUV: bool = ..., puv: bool = ..., reflection: bool = ..., rfl: bool = ..., reflectionAboutBBox: bool = ..., rab: bool = ..., reflectionAboutOrigin: bool = ..., rao: bool = ..., reflectionAboutX: bool = ..., rax: bool = ..., reflectionAboutY: bool = ..., ray: bool = ..., reflectionAboutZ: bool = ..., raz: bool = ..., reflectionTolerance: float = ..., rft: float = ..., relative: bool = ..., r: bool = ..., rotateX: bool = ..., x: bool = ..., rotateXY: bool = ..., xy: bool = ..., rotateXYZ: bool = ..., xyz: bool = ..., rotateXZ: bool = ..., xz: bool = ..., rotateY: bool = ..., y: bool = ..., rotateYZ: bool = ..., yz: bool = ..., rotateZ: bool = ..., z: bool = ..., symNegative: bool = ..., smn: bool = ..., translate: bool = ..., t: bool = ..., worldSpace: bool = ..., ws: bool = ..., xformConstraint: str = ..., xc: str = ...) -> None:
    """rotate is undoable, NOT queryable, and NOT editable.
    
    The rotate command is used to change the rotation of geometric objects. The
    rotation values are specified as Euler angles (rx, ry, rz). The values are
    interpreted based on the current working unit for Angular measurements. Most
    often this is degrees.
    
    The default behaviour, when no objects or flags are passed, is to do a
    absolute rotate on each currently selected object in the world space.

    ---
    - Args:
        - float float float [objects]: Input item(s).
        - absolute (a): Perform an absolute operation.
        - centerPivot (cp): Let the pivot be the center of the bounding box of all objects
        - componentSpace (cs): Rotate in local component space
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - deletePriorHistory (dph): If true then delete the history prior to the current operation.
        - euler (eu): Modifer for -relative flag that specifies rotation values should be added to current XYZ rotation values.
        - forceOrderXYZ (fo): When true, euler rotation value will be understood in XYZ rotation order not per transform node basis.
        - objectCenterPivot (ocp): Let the pivot be the center of the bounding box of each object
        - objectSpace (os): Perform rotation about object-space axis.
        - orientAxes (oa): Euler axis for orientation.
        - pivot (p): Define the pivot point for the transformation
        - preserveChildPosition (pcp): When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.
        - preserveGeometryPosition (pgp): When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.
        - preserveUV (puv): When true, UV values on rotated components are projected across the rotation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices.
            Default is false.
        - reflection (rfl): To move the corresponding symmetric components also.
        - reflectionAboutBBox (rab): Sets the position of the reflection axis  at the geometry bounding box
        - reflectionAboutOrigin (rao): Sets the position of the reflection axis  at the origin
        - reflectionAboutX (rax): Specifies the X=0 as reflection plane
        - reflectionAboutY (ray): Specifies the Y=0 as reflection plane
        - reflectionAboutZ (raz): Specifies the Z=0 as reflection plane
        - reflectionTolerance (rft): Specifies the tolerance to findout the corresponding reflected components
        - relative (r): Perform a operation relative to the object's current position
        - rotateX (x): Rotate in X direction
        - rotateXY (xy): Rotate in X and Y direction
        - rotateXYZ (xyz): Rotate in all directions (default)
        - rotateXZ (xz): Rotate in X and Z direction
        - rotateY (y): Rotate in Y direction
        - rotateYZ (yz): Rotate in Y and Z direction
        - rotateZ (z): Rotate in Z direction
        - symNegative (smn): When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.
        - translate (t): When true, the command will modify the node's translate attribute instead of its rotateTranslate attribute, when rotating around a pivot other than the object's own rotate pivot.
        - worldSpace (ws): Perform rotation about global world-space axis.
        - xformConstraint (xc): Apply a transform constraint to moving components.none - no constraintsurface - constrain components to the surfaceedge - constrain components to surface edgeslive - constraint components to the live surface
    """
