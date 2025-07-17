"""Stub files for Attributes category in Maya commands, command: listAttr."""

from typing import Any, overload

@overload #Overload for listAttr in ['create']
def listAttr([objects]: [objects], array: bool = ..., attributeType: str = ..., caching: bool = ..., category: str = ..., changedSinceFileOpen: bool = ..., channelBox: bool = ..., connectable: bool = ..., extension: bool = ..., fromPlugin: bool = ..., fullNodeName: bool = ..., hasData: bool = ..., hasNullData: bool = ..., inUse: bool = ..., keyable: bool = ..., leaf: bool = ..., locked: bool = ..., multi: bool = ..., nodeName: bool = ..., output: bool = ..., ramp: bool = ..., read: bool = ..., readOnly: bool = ..., scalar: bool = ..., scalarAndArray: bool = ..., settable: bool = ..., shortNames: bool = ..., string: str = ..., unlocked: bool = ..., usedAsFilename: bool = ..., userDefined: bool = ..., visible: bool = ..., write: bool = ...) -> list[str]:
    """listAttr is undoable, NOT queryable, and NOT editable.
    
    This command lists the attributes of a node. If no flags are specified all
    attributes are listed.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sphere()
        cmds.listAttr( r=True, s=True )
        # This will list the scalar readable attributes of the
        # selected nodes.  If more than one node is selected attributes
        # may be listed several times.
        cmds.listAttr( s=True, r=True, w=True, c=True, st=['centerX','centerY'] )
        # This will list all scalar, readable, writable, and connectable
        # attributes whose names are "centerX" or "centerY".
        cmds.listAttr( r=True, st='center*', ct='a*' )
        # This will list all readable attributes whose names match
        # "center*" (e.g. "centerX" or "centerpede") and who belong to
        # a category starting with the letter "a".
        cmds.listAttr( 'nurbsSphere1', s=True, cfo=True )
        # This will list all scalar attributes of
        # nurbsSphere1 that have been changed since the
        # file in which nurbsSphere1 is defined has been
        # opened.  If nurbsSphere1 comes from a referenced file,
        # the result will be all the attributes that have changed
        # since the referenced file was opened.
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - array (a): only list array (not multi) attributes
        - attributeType (at): Return attributes of a particular type.
        - caching (ca): only show attributes that are cached internally
        - category (ct): only show attributes belonging to the given category. Category string can be a regular expression.
        - changedSinceFileOpen (cfo): Only list the attributes that have been changed since the file they came from was opened. Typically useful only for objects/attributes coming from referenced files.
        - channelBox (cb): only show non-keyable attributes that appear in the channelbox
        - connectable (c): only show connectable attributes
        - extension (ex): list user-defined attributes for all nodes of this type (extension attributes)
        - fromPlugin (fp): only show attributes that were created by a plugin
        - fullNodeName (fnn): Return full node name in result.
        - hasData (hd): list only attributes that have data (all attributes except for message attributes)
        - hasNullData (hnd): list only attributes that have null data. This will list all attributes that have data (see hasData flag) but the data value is uninitialized. A common example where an attribute may have null data is when a string attribute is created but
            not yet assigned an initial value. Similarly array attribute data is often null until it is initialized.
        - inUse (iu): only show attributes that are currently marked as in use. This flag indicates that an attribute affects the scene data in some way. For example it has a non-default value or it is connected to another attribute.  This is the general concept
            though the precise implementation is subject to change.
        - keyable (k): only show attributes that can be keyframed
        - leaf (lf): Only list the leaf-level name of the attribute. controlPoints[44].xValue would be listed as "xValue".
        - locked (l): list only attributes which are locked
        - multi (m): list each currently existing element of a multi-attribute
        - nodeName (nn): Return node name in result.
        - output (o): List only the attributes which are numeric or which are compounds of numeric attributes.
        - ramp (ra): list only attributes which are ramps
        - read (r): list only attributes which are readable
        - readOnly (ro): List only the attributes which are readable and not writable.
        - scalar (s): only list scalar numerical attributes
        - scalarAndArray (sa): only list scalar and array attributes
        - settable (se): list attribute which are settable
        - shortNames (sn): list short attribute names (default is to list long names)
        - string (st): List only the attributes that match the other criteria AND match the string(s) passed from this flag. String can be a regular expression.
        - unlocked (u): list only attributes which are unlocked
        - usedAsFilename (uf): list only attributes which are designated to be treated as filenames
        - userDefined (ud): list user-defined (dynamic) attributes
        - visible (v): only show visible or non-hidden attributes
        - write (w): list only attributes which are writable
    """
@overload #Overload for listAttr in ['create']
def listAttr([objects]: [objects], a: bool = ..., at: str = ..., ca: bool = ..., ct: str = ..., cfo: bool = ..., cb: bool = ..., c: bool = ..., ex: bool = ..., fp: bool = ..., fnn: bool = ..., hd: bool = ..., hnd: bool = ..., iu: bool = ..., k: bool = ..., lf: bool = ..., l: bool = ..., m: bool = ..., nn: bool = ..., o: bool = ..., ra: bool = ..., r: bool = ..., ro: bool = ..., s: bool = ..., sa: bool = ..., se: bool = ..., sn: bool = ..., st: str = ..., u: bool = ..., uf: bool = ..., ud: bool = ..., v: bool = ..., w: bool = ...) -> list[str]:
    """listAttr is undoable, NOT queryable, and NOT editable.
    
    This command lists the attributes of a node. If no flags are specified all
    attributes are listed.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sphere()
        cmds.listAttr( r=True, s=True )
        # This will list the scalar readable attributes of the
        # selected nodes.  If more than one node is selected attributes
        # may be listed several times.
        cmds.listAttr( s=True, r=True, w=True, c=True, st=['centerX','centerY'] )
        # This will list all scalar, readable, writable, and connectable
        # attributes whose names are "centerX" or "centerY".
        cmds.listAttr( r=True, st='center*', ct='a*' )
        # This will list all readable attributes whose names match
        # "center*" (e.g. "centerX" or "centerpede") and who belong to
        # a category starting with the letter "a".
        cmds.listAttr( 'nurbsSphere1', s=True, cfo=True )
        # This will list all scalar attributes of
        # nurbsSphere1 that have been changed since the
        # file in which nurbsSphere1 is defined has been
        # opened.  If nurbsSphere1 comes from a referenced file,
        # the result will be all the attributes that have changed
        # since the referenced file was opened.
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - array (a): only list array (not multi) attributes
        - attributeType (at): Return attributes of a particular type.
        - caching (ca): only show attributes that are cached internally
        - category (ct): only show attributes belonging to the given category. Category string can be a regular expression.
        - changedSinceFileOpen (cfo): Only list the attributes that have been changed since the file they came from was opened. Typically useful only for objects/attributes coming from referenced files.
        - channelBox (cb): only show non-keyable attributes that appear in the channelbox
        - connectable (c): only show connectable attributes
        - extension (ex): list user-defined attributes for all nodes of this type (extension attributes)
        - fromPlugin (fp): only show attributes that were created by a plugin
        - fullNodeName (fnn): Return full node name in result.
        - hasData (hd): list only attributes that have data (all attributes except for message attributes)
        - hasNullData (hnd): list only attributes that have null data. This will list all attributes that have data (see hasData flag) but the data value is uninitialized. A common example where an attribute may have null data is when a string attribute is created but
            not yet assigned an initial value. Similarly array attribute data is often null until it is initialized.
        - inUse (iu): only show attributes that are currently marked as in use. This flag indicates that an attribute affects the scene data in some way. For example it has a non-default value or it is connected to another attribute.  This is the general concept
            though the precise implementation is subject to change.
        - keyable (k): only show attributes that can be keyframed
        - leaf (lf): Only list the leaf-level name of the attribute. controlPoints[44].xValue would be listed as "xValue".
        - locked (l): list only attributes which are locked
        - multi (m): list each currently existing element of a multi-attribute
        - nodeName (nn): Return node name in result.
        - output (o): List only the attributes which are numeric or which are compounds of numeric attributes.
        - ramp (ra): list only attributes which are ramps
        - read (r): list only attributes which are readable
        - readOnly (ro): List only the attributes which are readable and not writable.
        - scalar (s): only list scalar numerical attributes
        - scalarAndArray (sa): only list scalar and array attributes
        - settable (se): list attribute which are settable
        - shortNames (sn): list short attribute names (default is to list long names)
        - string (st): List only the attributes that match the other criteria AND match the string(s) passed from this flag. String can be a regular expression.
        - unlocked (u): list only attributes which are unlocked
        - usedAsFilename (uf): list only attributes which are designated to be treated as filenames
        - userDefined (ud): list user-defined (dynamic) attributes
        - visible (v): only show visible or non-hidden attributes
        - write (w): list only attributes which are writable
    """
@overload #Overload for listAttr in ['create']
def listAttr([objects]: [objects], array: bool = ..., a: bool = ..., attributeType: str = ..., at: str = ..., caching: bool = ..., ca: bool = ..., category: str = ..., ct: str = ..., changedSinceFileOpen: bool = ..., cfo: bool = ..., channelBox: bool = ..., cb: bool = ..., connectable: bool = ..., c: bool = ..., extension: bool = ..., ex: bool = ..., fromPlugin: bool = ..., fp: bool = ..., fullNodeName: bool = ..., fnn: bool = ..., hasData: bool = ..., hd: bool = ..., hasNullData: bool = ..., hnd: bool = ..., inUse: bool = ..., iu: bool = ..., keyable: bool = ..., k: bool = ..., leaf: bool = ..., lf: bool = ..., locked: bool = ..., l: bool = ..., multi: bool = ..., m: bool = ..., nodeName: bool = ..., nn: bool = ..., output: bool = ..., o: bool = ..., ramp: bool = ..., ra: bool = ..., read: bool = ..., r: bool = ..., readOnly: bool = ..., ro: bool = ..., scalar: bool = ..., s: bool = ..., scalarAndArray: bool = ..., sa: bool = ..., settable: bool = ..., se: bool = ..., shortNames: bool = ..., sn: bool = ..., string: str = ..., st: str = ..., unlocked: bool = ..., u: bool = ..., usedAsFilename: bool = ..., uf: bool = ..., userDefined: bool = ..., ud: bool = ..., visible: bool = ..., v: bool = ..., write: bool = ..., w: bool = ...) -> list[str]:
    """listAttr is undoable, NOT queryable, and NOT editable.
    
    This command lists the attributes of a node. If no flags are specified all
    attributes are listed.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sphere()
        cmds.listAttr( r=True, s=True )
        # This will list the scalar readable attributes of the
        # selected nodes.  If more than one node is selected attributes
        # may be listed several times.
        cmds.listAttr( s=True, r=True, w=True, c=True, st=['centerX','centerY'] )
        # This will list all scalar, readable, writable, and connectable
        # attributes whose names are "centerX" or "centerY".
        cmds.listAttr( r=True, st='center*', ct='a*' )
        # This will list all readable attributes whose names match
        # "center*" (e.g. "centerX" or "centerpede") and who belong to
        # a category starting with the letter "a".
        cmds.listAttr( 'nurbsSphere1', s=True, cfo=True )
        # This will list all scalar attributes of
        # nurbsSphere1 that have been changed since the
        # file in which nurbsSphere1 is defined has been
        # opened.  If nurbsSphere1 comes from a referenced file,
        # the result will be all the attributes that have changed
        # since the referenced file was opened.
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - array (a): only list array (not multi) attributes
        - attributeType (at): Return attributes of a particular type.
        - caching (ca): only show attributes that are cached internally
        - category (ct): only show attributes belonging to the given category. Category string can be a regular expression.
        - changedSinceFileOpen (cfo): Only list the attributes that have been changed since the file they came from was opened. Typically useful only for objects/attributes coming from referenced files.
        - channelBox (cb): only show non-keyable attributes that appear in the channelbox
        - connectable (c): only show connectable attributes
        - extension (ex): list user-defined attributes for all nodes of this type (extension attributes)
        - fromPlugin (fp): only show attributes that were created by a plugin
        - fullNodeName (fnn): Return full node name in result.
        - hasData (hd): list only attributes that have data (all attributes except for message attributes)
        - hasNullData (hnd): list only attributes that have null data. This will list all attributes that have data (see hasData flag) but the data value is uninitialized. A common example where an attribute may have null data is when a string attribute is created but
            not yet assigned an initial value. Similarly array attribute data is often null until it is initialized.
        - inUse (iu): only show attributes that are currently marked as in use. This flag indicates that an attribute affects the scene data in some way. For example it has a non-default value or it is connected to another attribute.  This is the general concept
            though the precise implementation is subject to change.
        - keyable (k): only show attributes that can be keyframed
        - leaf (lf): Only list the leaf-level name of the attribute. controlPoints[44].xValue would be listed as "xValue".
        - locked (l): list only attributes which are locked
        - multi (m): list each currently existing element of a multi-attribute
        - nodeName (nn): Return node name in result.
        - output (o): List only the attributes which are numeric or which are compounds of numeric attributes.
        - ramp (ra): list only attributes which are ramps
        - read (r): list only attributes which are readable
        - readOnly (ro): List only the attributes which are readable and not writable.
        - scalar (s): only list scalar numerical attributes
        - scalarAndArray (sa): only list scalar and array attributes
        - settable (se): list attribute which are settable
        - shortNames (sn): list short attribute names (default is to list long names)
        - string (st): List only the attributes that match the other criteria AND match the string(s) passed from this flag. String can be a regular expression.
        - unlocked (u): list only attributes which are unlocked
        - usedAsFilename (uf): list only attributes which are designated to be treated as filenames
        - userDefined (ud): list user-defined (dynamic) attributes
        - visible (v): only show visible or non-hidden attributes
        - write (w): list only attributes which are writable
    """
