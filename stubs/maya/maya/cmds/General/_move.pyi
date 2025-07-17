"""Stub files for General category in Maya commands, command: move."""

from typing import Any, overload

@overload #Overload for move in ['create']
def move(float float float [objects]: float float float [objects], absolute: bool = ..., autoOrientSecondaryAxis: bool = ..., componentOffset: bool = ..., componentSpace: bool = ..., constrainAlongNormal: bool = ..., deletePriorHistory: bool = ..., localSpace: bool = ..., moveX: bool = ..., moveXY: bool = ..., moveXYZ: bool = ..., moveXZ: bool = ..., moveY: bool = ..., moveYZ: bool = ..., moveZ: bool = ..., objectSpace: bool = ..., orientJoint: str = ..., parameter: bool = ..., preserveChildPosition: bool = ..., preserveGeometryPosition: bool = ..., preserveUV: bool = ..., reflection: bool = ..., reflectionAboutBBox: bool = ..., reflectionAboutOrigin: bool = ..., reflectionAboutX: bool = ..., reflectionAboutY: bool = ..., reflectionAboutZ: bool = ..., reflectionTolerance: float = ..., relative: bool = ..., rotatePivotRelative: bool = ..., scalePivotRelative: bool = ..., secondaryAxisOrient: str = ..., symNegative: bool = ..., worldSpace: bool = ..., worldSpaceDistance: bool = ..., xformConstraint: str = ...) -> None:
    """move is undoable, NOT queryable, and NOT editable.
    
    The move command is used to change the positions of geometric objects.
    
    The default behaviour, when no objects or flags are passed, is to do a
    absolute move on each currently selected object in the world space. The value
    of the coordinates are interpreted as being defined in the current linear unit
    unless the unit is explicitly mentioned.
    
    When using -objectSpace there are two ways to use this command. If numbers are
    typed without units then the internal values of the object are set to these
    values. If, on the other hand a unit is specified then the internal value is
    set to the equivalent internal value that represents that world-space
    distance.
    
    The -localSpace flag moves the object in its parent space. In this space the
    x,y,z values correspond directly to the tx, ty, tz channels on the object.
    
    The -rotatePivotRelative/-scalePivotRelative flags can be used with the
    -absolute flag to translate an object so that its pivot point ends up at the
    given absolute position. These flags will be ignored if components are
    specified.
    
    The -worldSpaceDistance flag is a modifier flag that may be used in
    conjunction with the -objectSpace/-localSpace flags. When this flag is
    specified the command treats the x,y,z values as world space units so the
    object will move the specified world space distance but it will move along the
    axis specified by the -objectSpace/-localSpace flag. The default behaviour,
    without this flag, is to treat the x,y,z values as units in object space or
    local space. In other words, the worldspace distance moved will depend on the
    transformations applied to the object unless this flag is specified.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polySphere()
        cmds.move( 1, 1, 1 )
        cmds.move( 5, y=True )
        cmds.move( '1in', '1in', '1in', relative=True, objectSpace=True, worldSpaceDistance=True )
        cmds.move( 0, 0, 0, 'pSphere1', absolute=True )
    ```

    ---
    - Args:
        - float float float [objects]: Input item(s).
        - absolute (a): Perform an absolute operation.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - componentOffset (co): Move components individually in local space
        - componentSpace (cs): Move in local component space
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - deletePriorHistory (dph): If true then delete the history prior to the current operation.
        - localSpace (ls): Move in local space
        - moveX (x): Move in X direction
        - moveXY (xy): Move in XY direction
        - moveXYZ (xyz): Move in all directions (default)
        - moveXZ (xz): Move in XZ direction
        - moveY (y): Move in Y direction
        - moveYZ (yz): Move in YZ direction
        - moveZ (z): Move in Z direction
        - objectSpace (os): Move in object space
        - orientJoint (oj): Default is xyz.
        - parameter (p): Move in parametric space
        - preserveChildPosition (pcp): When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.
        - preserveGeometryPosition (pgp): When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.
        - preserveUV (puv): When true, UV values on translated components are projected along the translation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected
            vertices. Default is false.
        - reflection (rfl): To move the corresponding symmetric components also.
        - reflectionAboutBBox (rab): Sets the position of the reflection axis  at the geometry bounding box
        - reflectionAboutOrigin (rao): Sets the position of the reflection axis  at the origin
        - reflectionAboutX (rax): Specifies the X=0 as reflection plane
        - reflectionAboutY (ray): Specifies the Y=0 as reflection plane
        - reflectionAboutZ (raz): Specifies the Z=0 as reflection plane
        - reflectionTolerance (rft): Specifies the tolerance to findout the corresponding reflected components
        - relative (r): Perform a operation relative to the object's current position
        - rotatePivotRelative (rpr): Move relative to the object's rotate pivot point.
        - scalePivotRelative (spr): Move relative to the object's scale pivot point.
        - secondaryAxisOrient (sao): Default is xyz.
        - symNegative (smn): When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.
        - worldSpace (ws): Move in world space
        - worldSpaceDistance (wd): Move is specified in world space units
        - xformConstraint (xc): Apply a transform constraint to moving components.none - no constraintsurface - constrain components to the surfaceedge - constrain components to surface edgeslive - constraint components to the live surface
    """
@overload #Overload for move in ['create']
def move(float float float [objects]: float float float [objects], a: bool = ..., aos: bool = ..., co: bool = ..., cs: bool = ..., xn: bool = ..., dph: bool = ..., ls: bool = ..., x: bool = ..., xy: bool = ..., xyz: bool = ..., xz: bool = ..., y: bool = ..., yz: bool = ..., z: bool = ..., os: bool = ..., oj: str = ..., p: bool = ..., pcp: bool = ..., pgp: bool = ..., puv: bool = ..., rfl: bool = ..., rab: bool = ..., rao: bool = ..., rax: bool = ..., ray: bool = ..., raz: bool = ..., rft: float = ..., r: bool = ..., rpr: bool = ..., spr: bool = ..., sao: str = ..., smn: bool = ..., ws: bool = ..., wd: bool = ..., xc: str = ...) -> None:
    """move is undoable, NOT queryable, and NOT editable.
    
    The move command is used to change the positions of geometric objects.
    
    The default behaviour, when no objects or flags are passed, is to do a
    absolute move on each currently selected object in the world space. The value
    of the coordinates are interpreted as being defined in the current linear unit
    unless the unit is explicitly mentioned.
    
    When using -objectSpace there are two ways to use this command. If numbers are
    typed without units then the internal values of the object are set to these
    values. If, on the other hand a unit is specified then the internal value is
    set to the equivalent internal value that represents that world-space
    distance.
    
    The -localSpace flag moves the object in its parent space. In this space the
    x,y,z values correspond directly to the tx, ty, tz channels on the object.
    
    The -rotatePivotRelative/-scalePivotRelative flags can be used with the
    -absolute flag to translate an object so that its pivot point ends up at the
    given absolute position. These flags will be ignored if components are
    specified.
    
    The -worldSpaceDistance flag is a modifier flag that may be used in
    conjunction with the -objectSpace/-localSpace flags. When this flag is
    specified the command treats the x,y,z values as world space units so the
    object will move the specified world space distance but it will move along the
    axis specified by the -objectSpace/-localSpace flag. The default behaviour,
    without this flag, is to treat the x,y,z values as units in object space or
    local space. In other words, the worldspace distance moved will depend on the
    transformations applied to the object unless this flag is specified.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polySphere()
        cmds.move( 1, 1, 1 )
        cmds.move( 5, y=True )
        cmds.move( '1in', '1in', '1in', relative=True, objectSpace=True, worldSpaceDistance=True )
        cmds.move( 0, 0, 0, 'pSphere1', absolute=True )
    ```

    ---
    - Args:
        - float float float [objects]: Input item(s).
        - absolute (a): Perform an absolute operation.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - componentOffset (co): Move components individually in local space
        - componentSpace (cs): Move in local component space
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - deletePriorHistory (dph): If true then delete the history prior to the current operation.
        - localSpace (ls): Move in local space
        - moveX (x): Move in X direction
        - moveXY (xy): Move in XY direction
        - moveXYZ (xyz): Move in all directions (default)
        - moveXZ (xz): Move in XZ direction
        - moveY (y): Move in Y direction
        - moveYZ (yz): Move in YZ direction
        - moveZ (z): Move in Z direction
        - objectSpace (os): Move in object space
        - orientJoint (oj): Default is xyz.
        - parameter (p): Move in parametric space
        - preserveChildPosition (pcp): When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.
        - preserveGeometryPosition (pgp): When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.
        - preserveUV (puv): When true, UV values on translated components are projected along the translation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected
            vertices. Default is false.
        - reflection (rfl): To move the corresponding symmetric components also.
        - reflectionAboutBBox (rab): Sets the position of the reflection axis  at the geometry bounding box
        - reflectionAboutOrigin (rao): Sets the position of the reflection axis  at the origin
        - reflectionAboutX (rax): Specifies the X=0 as reflection plane
        - reflectionAboutY (ray): Specifies the Y=0 as reflection plane
        - reflectionAboutZ (raz): Specifies the Z=0 as reflection plane
        - reflectionTolerance (rft): Specifies the tolerance to findout the corresponding reflected components
        - relative (r): Perform a operation relative to the object's current position
        - rotatePivotRelative (rpr): Move relative to the object's rotate pivot point.
        - scalePivotRelative (spr): Move relative to the object's scale pivot point.
        - secondaryAxisOrient (sao): Default is xyz.
        - symNegative (smn): When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.
        - worldSpace (ws): Move in world space
        - worldSpaceDistance (wd): Move is specified in world space units
        - xformConstraint (xc): Apply a transform constraint to moving components.none - no constraintsurface - constrain components to the surfaceedge - constrain components to surface edgeslive - constraint components to the live surface
    """
@overload #Overload for move in ['create']
def move(float float float [objects]: float float float [objects], absolute: bool = ..., a: bool = ..., autoOrientSecondaryAxis: bool = ..., aos: bool = ..., componentOffset: bool = ..., co: bool = ..., componentSpace: bool = ..., cs: bool = ..., constrainAlongNormal: bool = ..., xn: bool = ..., deletePriorHistory: bool = ..., dph: bool = ..., localSpace: bool = ..., ls: bool = ..., moveX: bool = ..., x: bool = ..., moveXY: bool = ..., xy: bool = ..., moveXYZ: bool = ..., xyz: bool = ..., moveXZ: bool = ..., xz: bool = ..., moveY: bool = ..., y: bool = ..., moveYZ: bool = ..., yz: bool = ..., moveZ: bool = ..., z: bool = ..., objectSpace: bool = ..., os: bool = ..., orientJoint: str = ..., oj: str = ..., parameter: bool = ..., p: bool = ..., preserveChildPosition: bool = ..., pcp: bool = ..., preserveGeometryPosition: bool = ..., pgp: bool = ..., preserveUV: bool = ..., puv: bool = ..., reflection: bool = ..., rfl: bool = ..., reflectionAboutBBox: bool = ..., rab: bool = ..., reflectionAboutOrigin: bool = ..., rao: bool = ..., reflectionAboutX: bool = ..., rax: bool = ..., reflectionAboutY: bool = ..., ray: bool = ..., reflectionAboutZ: bool = ..., raz: bool = ..., reflectionTolerance: float = ..., rft: float = ..., relative: bool = ..., r: bool = ..., rotatePivotRelative: bool = ..., rpr: bool = ..., scalePivotRelative: bool = ..., spr: bool = ..., secondaryAxisOrient: str = ..., sao: str = ..., symNegative: bool = ..., smn: bool = ..., worldSpace: bool = ..., ws: bool = ..., worldSpaceDistance: bool = ..., wd: bool = ..., xformConstraint: str = ..., xc: str = ...) -> None:
    """move is undoable, NOT queryable, and NOT editable.
    
    The move command is used to change the positions of geometric objects.
    
    The default behaviour, when no objects or flags are passed, is to do a
    absolute move on each currently selected object in the world space. The value
    of the coordinates are interpreted as being defined in the current linear unit
    unless the unit is explicitly mentioned.
    
    When using -objectSpace there are two ways to use this command. If numbers are
    typed without units then the internal values of the object are set to these
    values. If, on the other hand a unit is specified then the internal value is
    set to the equivalent internal value that represents that world-space
    distance.
    
    The -localSpace flag moves the object in its parent space. In this space the
    x,y,z values correspond directly to the tx, ty, tz channels on the object.
    
    The -rotatePivotRelative/-scalePivotRelative flags can be used with the
    -absolute flag to translate an object so that its pivot point ends up at the
    given absolute position. These flags will be ignored if components are
    specified.
    
    The -worldSpaceDistance flag is a modifier flag that may be used in
    conjunction with the -objectSpace/-localSpace flags. When this flag is
    specified the command treats the x,y,z values as world space units so the
    object will move the specified world space distance but it will move along the
    axis specified by the -objectSpace/-localSpace flag. The default behaviour,
    without this flag, is to treat the x,y,z values as units in object space or
    local space. In other words, the worldspace distance moved will depend on the
    transformations applied to the object unless this flag is specified.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polySphere()
        cmds.move( 1, 1, 1 )
        cmds.move( 5, y=True )
        cmds.move( '1in', '1in', '1in', relative=True, objectSpace=True, worldSpaceDistance=True )
        cmds.move( 0, 0, 0, 'pSphere1', absolute=True )
    ```

    ---
    - Args:
        - float float float [objects]: Input item(s).
        - absolute (a): Perform an absolute operation.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - componentOffset (co): Move components individually in local space
        - componentSpace (cs): Move in local component space
        - constrainAlongNormal (xn): When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        - deletePriorHistory (dph): If true then delete the history prior to the current operation.
        - localSpace (ls): Move in local space
        - moveX (x): Move in X direction
        - moveXY (xy): Move in XY direction
        - moveXYZ (xyz): Move in all directions (default)
        - moveXZ (xz): Move in XZ direction
        - moveY (y): Move in Y direction
        - moveYZ (yz): Move in YZ direction
        - moveZ (z): Move in Z direction
        - objectSpace (os): Move in object space
        - orientJoint (oj): Default is xyz.
        - parameter (p): Move in parametric space
        - preserveChildPosition (pcp): When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.
        - preserveGeometryPosition (pgp): When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.
        - preserveUV (puv): When true, UV values on translated components are projected along the translation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected
            vertices. Default is false.
        - reflection (rfl): To move the corresponding symmetric components also.
        - reflectionAboutBBox (rab): Sets the position of the reflection axis  at the geometry bounding box
        - reflectionAboutOrigin (rao): Sets the position of the reflection axis  at the origin
        - reflectionAboutX (rax): Specifies the X=0 as reflection plane
        - reflectionAboutY (ray): Specifies the Y=0 as reflection plane
        - reflectionAboutZ (raz): Specifies the Z=0 as reflection plane
        - reflectionTolerance (rft): Specifies the tolerance to findout the corresponding reflected components
        - relative (r): Perform a operation relative to the object's current position
        - rotatePivotRelative (rpr): Move relative to the object's rotate pivot point.
        - scalePivotRelative (spr): Move relative to the object's scale pivot point.
        - secondaryAxisOrient (sao): Default is xyz.
        - symNegative (smn): When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.
        - worldSpace (ws): Move in world space
        - worldSpaceDistance (wd): Move is specified in world space units
        - xformConstraint (xc): Apply a transform constraint to moving components.none - no constraintsurface - constrain components to the surfaceedge - constrain components to surface edgeslive - constraint components to the live surface
    """
