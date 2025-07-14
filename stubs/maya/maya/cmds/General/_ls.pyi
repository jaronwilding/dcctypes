"""Stub files for General category in Maya commands, command: ls."""

from typing import Any, overload

@overload #Overload for ls in ['create']
def ls([object [object...]]: [object [object...]], absoluteName: bool = ..., allPaths: bool = ..., assemblies: bool = ..., cameras: bool = ..., containerType: str = ..., containers: bool = ..., dagObjects: bool = ..., defaultNodes: bool = ..., dependencyNodes: bool = ..., exactType: str = ..., excludeType: str = ..., flatten: bool = ..., geometry: bool = ..., ghost: bool = ..., head: int = ..., hilite: bool = ..., intermediateObjects: bool = ..., invisible: bool = ..., leaf: bool = ..., lights: bool = ..., live: bool = ..., lockedNodes: bool = ..., long: bool = ..., materials: bool = ..., modified: bool = ..., noIntermediate: bool = ..., nodeTypes: bool = ..., objectsOnly: bool = ..., orderedComponentSelection: bool = ..., orderedSelection: bool = ..., partitions: bool = ..., persistentNodes: bool = ..., planes: bool = ..., preSelectHilite: bool = ..., readOnly: bool = ..., recursive: bool = ..., referencedNodes: bool = ..., references: bool = ..., renderGlobals: bool = ..., renderQualities: bool = ..., renderResolutions: bool = ..., renderSetups: bool = ..., selection: bool = ..., sets: bool = ..., shapes: bool = ..., shortNames: bool = ..., showNamespace: bool = ..., showType: bool = ..., tail: int = ..., templated: bool = ..., textures: bool = ..., transforms: bool = ..., type: str = ..., ufeObjects: bool = ..., undeletable: bool = ..., untemplated: bool = ..., uuid: bool = ..., visible: bool = ...) -> list[str]:
    """ls is undoable, NOT queryable, and NOT editable.
    
    The `ls` command returns the names (and optionally the type names) of objects
    in the scene.
    
    The most common use of `ls` is to filter or match objects based on their name
    (using wildcards) or based on their type. By default `ls` will match any
    object in the scene but it can also be used to filter or list the selected
    objects when used in conjunction with the -selection flag.
    
    If type names are requested, using the showType flag, they will be interleaved
    with object names so the result will be pairs of <object, type> values.
    
    Internal nodes (for example itemFilter nodes) are typically filtered so that
    only scene objects are returned. However, using a wildcard will cause all the
    nodes matching the wild card to show up, including internal nodes. For
    example, `ls *` will list all nodes whether internal or not.
    
    Use the syntax "::" to denote a recursive namespace search when listing nodes.
    For example, `ls "::pSphere1"` would match objects named "pSphere1" in any
    namespace, at any depth. `ls "ns::*"` would match any node in namespace "ns"
    or children namespaces.
    
    When Maya is in relativeNames mode, the `ls` command will return names
    relative to the current namespace and `ls *` will list from the the current
    namespace. For more details, please refer to the `-relativeNames` flag of the
    `namespace` command.
    
    The command may also be passed node UUIDs instead of names/paths, and can
    return UUIDs instead of names via the -uuid flag.

    ---
    - Args:
        - [object [object...]]: Input item(s).
        - absoluteName (an): This flag can be used in conjunction with the showNamespace flag to specify that the namespace(s) returned by the command be in absolute namespace format. The absolute name of the namespace is a full namespace path, starting from the root
            namespace ":" and including all parent namespaces.  For example ":ns:ball" is an absolute namespace name while "ns:ball" is not. The absolute namespace name is invariant and is not affected by the current namespace or relative namespace
            modes.
        - allPaths (ap): List all paths to nodes in DAG. This flag only works if-dagis also specified or if an object name is supplied.
        - assemblies: List top level transform Dag objects
        - cameras (ca): List camera shapes.
        - containerType (ct): List containers with the specified user-defined type.This flag cannot be used in conjunction with the type or exactType flag.
        - containers (con): List containers. Includes both standard containers as well as other types of containers such as dagContainers.
        - dagObjects (dag): List Dag objects of any type. If object name arguments are passed to the command then this flag will list all Dag objects below the specified object(s).
        - defaultNodes (dn): Returns default nodes. A default node is one that Maya creates automatically and does not get saved out with the scene, although some of its attribute values may.
        - dependencyNodes (dep): List dependency nodes. (including Dag objects)
        - exactType (et): List all objects of the specified type, butnotobjects that are descendents of that type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This
            flag cannot be used in conjunction with the type or excludeType flag.
        - excludeType (ext): List all objects that are not of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This flag cannot be used in conjunction
            with the type or exactType flag.
        - flatten (fl): Flattens the returned list of objects so that each component is identified individually.
        - geometry (g): List geometric Dag objects.
        - ghost (gh): List ghosting objects.
        - head (hd): This flag  specifies the maximum number of elements to be returned from the beginning of the list of items. Note: each type flag will return at most this many items so if multiple type flags are specified then the number of items returned
            can be greater than this amount.
        - hilite (hl): List objects that are currently hilited for component selection.
        - intermediateObjects (io): List only intermediate dag nodes.
        - invisible (iv): List only invisible dag nodes.
        - leaf (lf): List all leaf nodes in Dag. This flag is a modifier and must be used in conjunction with the -dag flag.
        - lights (lt): List light shapes.
        - live (lv): List objects that are currently live.
        - lockedNodes (ln): Returns locked nodes, which cannot be deleted or renamed. However, their status may change.
        - long (l): Return full path names for Dag objects. By default the shortest unique name is returned.
        - materials (mat): List materials or shading groups.
        - modified (mod): When this flag is set, only nodes modified since the last save will be returned.
        - noIntermediate (ni): List only non intermediate dag nodes.
        - nodeTypes (nt): Lists all registered node types.
        - objectsOnly (o): When this flag is set only object names will be returned and components/attributes will be ignored.
        - orderedComponentSelection (ocs): Return component selections ordered by their shape instead of selection order.
        - orderedSelection (os): List objects and components that are currently selected in their order of selection.  This flag depends on the value of the -tso/trackSelectionOrder flag of the selectPref command.  If that flag is not enabled than this flag will return the
            same thing as the -sl/selection flag would.
        - partitions (pr): List partitions.
        - persistentNodes (pn): Returns persistent nodes, which are nodes that stay in the Maya session after a file > new. These are a special class of default nodes that do not get reset on file > new. Ex: itemFilter and selectionListOperator nodes.
        - planes (pl): List construction plane shapes.
        - preSelectHilite (psh): List components that are currently hilited for pre-selection.
        - readOnly (ro): Returns referenced nodes. Referenced nodes are read only. NOTE: Obsolete. Please use "-referencedNodes".
        - recursive (r): When set to true, this command will look for name matches in all namespaces. When set to false, this command will only look for matches in namespaces that are requested (e.g. by specifying a name containing the ':'... "ns1:pSphere1").
        - referencedNodes (rn): Returns referenced nodes. Referenced nodes are read only.
        - references (rf): List references associated with files. Excludes special reference nodes such as the sharedReferenceNode and unknown reference nodes.
        - renderGlobals (rg): List render globals.
        - renderQualities (rq): List named render qualities.
        - renderResolutions (rr): List render resolutions.
        - renderSetups (rs): Alias for-renderGlobals.
        - selection (sl): List objects that are currently selected.
        - sets (set): List sets.
        - shapes (s): List shape objects.
        - shortNames (sn): Return short attribute names. By default long attribute names are returned.
        - showNamespace (sns): Show the namespace of each object after the object name.This flag cannot be used in conjunction with the showType flag.
        - showType (st): List the type of each object after its name.
        - tail (tl): This flag specifies the maximum number of elements to be returned from the end of the list of items. Note: each    type flag will return at most this many items so if multiple type flags are specified then the number of items returned can
            be greater than this amount
        - templated (tm): List only templated dag nodes.
        - textures (tex): List textures.
        - transforms (tr): List transform objects.
        - type (typ): List all objects of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag. Note: some selection items in Maya do not have a
            specific object/data type associated with them and will return "untyped" when listed with this flag.This flag cannot be used in conjunction with the exactType or excludeType flag.
        - ufeObjects (ufe): When used in conjunction with the-sl/selectionflag, will return objects that are defined through the UFE interface as well as native Maya objects.
        - undeletable (ud): Returns nodes that cannot be deleted (which includes locked nodes). These nodes also cannot be renamed.
        - untemplated (ut): List only un-templated dag nodes.
        - uuid (uid): Return node UUIDs instead of names. Note that there are no "UUID paths" - combining this flag with e.g. the -long flag will not result in a path formed of node UUIDs.
        - visible (v): List only visible dag nodes.
    """
@overload #Overload for ls in ['create']
def ls([object [object...]]: [object [object...]], an: bool = ..., ap: bool = ..., ca: bool = ..., ct: str = ..., con: bool = ..., dag: bool = ..., dn: bool = ..., dep: bool = ..., et: str = ..., ext: str = ..., fl: bool = ..., g: bool = ..., gh: bool = ..., hd: int = ..., hl: bool = ..., io: bool = ..., iv: bool = ..., lf: bool = ..., lt: bool = ..., lv: bool = ..., ln: bool = ..., l: bool = ..., mat: bool = ..., mod: bool = ..., ni: bool = ..., nt: bool = ..., o: bool = ..., ocs: bool = ..., os: bool = ..., pr: bool = ..., pn: bool = ..., pl: bool = ..., psh: bool = ..., ro: bool = ..., r: bool = ..., rn: bool = ..., rf: bool = ..., rg: bool = ..., rq: bool = ..., rr: bool = ..., rs: bool = ..., sl: bool = ..., set: bool = ..., s: bool = ..., sn: bool = ..., sns: bool = ..., st: bool = ..., tl: int = ..., tm: bool = ..., tex: bool = ..., tr: bool = ..., typ: str = ..., ufe: bool = ..., ud: bool = ..., ut: bool = ..., uid: bool = ..., v: bool = ...) -> list[str]:
    """ls is undoable, NOT queryable, and NOT editable.
    
    The `ls` command returns the names (and optionally the type names) of objects
    in the scene.
    
    The most common use of `ls` is to filter or match objects based on their name
    (using wildcards) or based on their type. By default `ls` will match any
    object in the scene but it can also be used to filter or list the selected
    objects when used in conjunction with the -selection flag.
    
    If type names are requested, using the showType flag, they will be interleaved
    with object names so the result will be pairs of <object, type> values.
    
    Internal nodes (for example itemFilter nodes) are typically filtered so that
    only scene objects are returned. However, using a wildcard will cause all the
    nodes matching the wild card to show up, including internal nodes. For
    example, `ls *` will list all nodes whether internal or not.
    
    Use the syntax "::" to denote a recursive namespace search when listing nodes.
    For example, `ls "::pSphere1"` would match objects named "pSphere1" in any
    namespace, at any depth. `ls "ns::*"` would match any node in namespace "ns"
    or children namespaces.
    
    When Maya is in relativeNames mode, the `ls` command will return names
    relative to the current namespace and `ls *` will list from the the current
    namespace. For more details, please refer to the `-relativeNames` flag of the
    `namespace` command.
    
    The command may also be passed node UUIDs instead of names/paths, and can
    return UUIDs instead of names via the -uuid flag.

    ---
    - Args:
        - [object [object...]]: Input item(s).
        - absoluteName (an): This flag can be used in conjunction with the showNamespace flag to specify that the namespace(s) returned by the command be in absolute namespace format. The absolute name of the namespace is a full namespace path, starting from the root
            namespace ":" and including all parent namespaces.  For example ":ns:ball" is an absolute namespace name while "ns:ball" is not. The absolute namespace name is invariant and is not affected by the current namespace or relative namespace
            modes.
        - allPaths (ap): List all paths to nodes in DAG. This flag only works if-dagis also specified or if an object name is supplied.
        - assemblies: List top level transform Dag objects
        - cameras (ca): List camera shapes.
        - containerType (ct): List containers with the specified user-defined type.This flag cannot be used in conjunction with the type or exactType flag.
        - containers (con): List containers. Includes both standard containers as well as other types of containers such as dagContainers.
        - dagObjects (dag): List Dag objects of any type. If object name arguments are passed to the command then this flag will list all Dag objects below the specified object(s).
        - defaultNodes (dn): Returns default nodes. A default node is one that Maya creates automatically and does not get saved out with the scene, although some of its attribute values may.
        - dependencyNodes (dep): List dependency nodes. (including Dag objects)
        - exactType (et): List all objects of the specified type, butnotobjects that are descendents of that type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This
            flag cannot be used in conjunction with the type or excludeType flag.
        - excludeType (ext): List all objects that are not of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This flag cannot be used in conjunction
            with the type or exactType flag.
        - flatten (fl): Flattens the returned list of objects so that each component is identified individually.
        - geometry (g): List geometric Dag objects.
        - ghost (gh): List ghosting objects.
        - head (hd): This flag  specifies the maximum number of elements to be returned from the beginning of the list of items. Note: each type flag will return at most this many items so if multiple type flags are specified then the number of items returned
            can be greater than this amount.
        - hilite (hl): List objects that are currently hilited for component selection.
        - intermediateObjects (io): List only intermediate dag nodes.
        - invisible (iv): List only invisible dag nodes.
        - leaf (lf): List all leaf nodes in Dag. This flag is a modifier and must be used in conjunction with the -dag flag.
        - lights (lt): List light shapes.
        - live (lv): List objects that are currently live.
        - lockedNodes (ln): Returns locked nodes, which cannot be deleted or renamed. However, their status may change.
        - long (l): Return full path names for Dag objects. By default the shortest unique name is returned.
        - materials (mat): List materials or shading groups.
        - modified (mod): When this flag is set, only nodes modified since the last save will be returned.
        - noIntermediate (ni): List only non intermediate dag nodes.
        - nodeTypes (nt): Lists all registered node types.
        - objectsOnly (o): When this flag is set only object names will be returned and components/attributes will be ignored.
        - orderedComponentSelection (ocs): Return component selections ordered by their shape instead of selection order.
        - orderedSelection (os): List objects and components that are currently selected in their order of selection.  This flag depends on the value of the -tso/trackSelectionOrder flag of the selectPref command.  If that flag is not enabled than this flag will return the
            same thing as the -sl/selection flag would.
        - partitions (pr): List partitions.
        - persistentNodes (pn): Returns persistent nodes, which are nodes that stay in the Maya session after a file > new. These are a special class of default nodes that do not get reset on file > new. Ex: itemFilter and selectionListOperator nodes.
        - planes (pl): List construction plane shapes.
        - preSelectHilite (psh): List components that are currently hilited for pre-selection.
        - readOnly (ro): Returns referenced nodes. Referenced nodes are read only. NOTE: Obsolete. Please use "-referencedNodes".
        - recursive (r): When set to true, this command will look for name matches in all namespaces. When set to false, this command will only look for matches in namespaces that are requested (e.g. by specifying a name containing the ':'... "ns1:pSphere1").
        - referencedNodes (rn): Returns referenced nodes. Referenced nodes are read only.
        - references (rf): List references associated with files. Excludes special reference nodes such as the sharedReferenceNode and unknown reference nodes.
        - renderGlobals (rg): List render globals.
        - renderQualities (rq): List named render qualities.
        - renderResolutions (rr): List render resolutions.
        - renderSetups (rs): Alias for-renderGlobals.
        - selection (sl): List objects that are currently selected.
        - sets (set): List sets.
        - shapes (s): List shape objects.
        - shortNames (sn): Return short attribute names. By default long attribute names are returned.
        - showNamespace (sns): Show the namespace of each object after the object name.This flag cannot be used in conjunction with the showType flag.
        - showType (st): List the type of each object after its name.
        - tail (tl): This flag specifies the maximum number of elements to be returned from the end of the list of items. Note: each    type flag will return at most this many items so if multiple type flags are specified then the number of items returned can
            be greater than this amount
        - templated (tm): List only templated dag nodes.
        - textures (tex): List textures.
        - transforms (tr): List transform objects.
        - type (typ): List all objects of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag. Note: some selection items in Maya do not have a
            specific object/data type associated with them and will return "untyped" when listed with this flag.This flag cannot be used in conjunction with the exactType or excludeType flag.
        - ufeObjects (ufe): When used in conjunction with the-sl/selectionflag, will return objects that are defined through the UFE interface as well as native Maya objects.
        - undeletable (ud): Returns nodes that cannot be deleted (which includes locked nodes). These nodes also cannot be renamed.
        - untemplated (ut): List only un-templated dag nodes.
        - uuid (uid): Return node UUIDs instead of names. Note that there are no "UUID paths" - combining this flag with e.g. the -long flag will not result in a path formed of node UUIDs.
        - visible (v): List only visible dag nodes.
    """
@overload #Overload for ls in ['create']
def ls([object [object...]]: [object [object...]], absoluteName: bool = ..., an: bool = ..., allPaths: bool = ..., ap: bool = ..., assemblies: bool = ..., cameras: bool = ..., ca: bool = ..., containerType: str = ..., ct: str = ..., containers: bool = ..., con: bool = ..., dagObjects: bool = ..., dag: bool = ..., defaultNodes: bool = ..., dn: bool = ..., dependencyNodes: bool = ..., dep: bool = ..., exactType: str = ..., et: str = ..., excludeType: str = ..., ext: str = ..., flatten: bool = ..., fl: bool = ..., geometry: bool = ..., g: bool = ..., ghost: bool = ..., gh: bool = ..., head: int = ..., hd: int = ..., hilite: bool = ..., hl: bool = ..., intermediateObjects: bool = ..., io: bool = ..., invisible: bool = ..., iv: bool = ..., leaf: bool = ..., lf: bool = ..., lights: bool = ..., lt: bool = ..., live: bool = ..., lv: bool = ..., lockedNodes: bool = ..., ln: bool = ..., long: bool = ..., l: bool = ..., materials: bool = ..., mat: bool = ..., modified: bool = ..., mod: bool = ..., noIntermediate: bool = ..., ni: bool = ..., nodeTypes: bool = ..., nt: bool = ..., objectsOnly: bool = ..., o: bool = ..., orderedComponentSelection: bool = ..., ocs: bool = ..., orderedSelection: bool = ..., os: bool = ..., partitions: bool = ..., pr: bool = ..., persistentNodes: bool = ..., pn: bool = ..., planes: bool = ..., pl: bool = ..., preSelectHilite: bool = ..., psh: bool = ..., readOnly: bool = ..., ro: bool = ..., recursive: bool = ..., r: bool = ..., referencedNodes: bool = ..., rn: bool = ..., references: bool = ..., rf: bool = ..., renderGlobals: bool = ..., rg: bool = ..., renderQualities: bool = ..., rq: bool = ..., renderResolutions: bool = ..., rr: bool = ..., renderSetups: bool = ..., rs: bool = ..., selection: bool = ..., sl: bool = ..., sets: bool = ..., set: bool = ..., shapes: bool = ..., s: bool = ..., shortNames: bool = ..., sn: bool = ..., showNamespace: bool = ..., sns: bool = ..., showType: bool = ..., st: bool = ..., tail: int = ..., tl: int = ..., templated: bool = ..., tm: bool = ..., textures: bool = ..., tex: bool = ..., transforms: bool = ..., tr: bool = ..., type: str = ..., typ: str = ..., ufeObjects: bool = ..., ufe: bool = ..., undeletable: bool = ..., ud: bool = ..., untemplated: bool = ..., ut: bool = ..., uuid: bool = ..., uid: bool = ..., visible: bool = ..., v: bool = ...) -> list[str]:
    """ls is undoable, NOT queryable, and NOT editable.
    
    The `ls` command returns the names (and optionally the type names) of objects
    in the scene.
    
    The most common use of `ls` is to filter or match objects based on their name
    (using wildcards) or based on their type. By default `ls` will match any
    object in the scene but it can also be used to filter or list the selected
    objects when used in conjunction with the -selection flag.
    
    If type names are requested, using the showType flag, they will be interleaved
    with object names so the result will be pairs of <object, type> values.
    
    Internal nodes (for example itemFilter nodes) are typically filtered so that
    only scene objects are returned. However, using a wildcard will cause all the
    nodes matching the wild card to show up, including internal nodes. For
    example, `ls *` will list all nodes whether internal or not.
    
    Use the syntax "::" to denote a recursive namespace search when listing nodes.
    For example, `ls "::pSphere1"` would match objects named "pSphere1" in any
    namespace, at any depth. `ls "ns::*"` would match any node in namespace "ns"
    or children namespaces.
    
    When Maya is in relativeNames mode, the `ls` command will return names
    relative to the current namespace and `ls *` will list from the the current
    namespace. For more details, please refer to the `-relativeNames` flag of the
    `namespace` command.
    
    The command may also be passed node UUIDs instead of names/paths, and can
    return UUIDs instead of names via the -uuid flag.

    ---
    - Args:
        - [object [object...]]: Input item(s).
        - absoluteName (an): This flag can be used in conjunction with the showNamespace flag to specify that the namespace(s) returned by the command be in absolute namespace format. The absolute name of the namespace is a full namespace path, starting from the root
            namespace ":" and including all parent namespaces.  For example ":ns:ball" is an absolute namespace name while "ns:ball" is not. The absolute namespace name is invariant and is not affected by the current namespace or relative namespace
            modes.
        - allPaths (ap): List all paths to nodes in DAG. This flag only works if-dagis also specified or if an object name is supplied.
        - assemblies: List top level transform Dag objects
        - cameras (ca): List camera shapes.
        - containerType (ct): List containers with the specified user-defined type.This flag cannot be used in conjunction with the type or exactType flag.
        - containers (con): List containers. Includes both standard containers as well as other types of containers such as dagContainers.
        - dagObjects (dag): List Dag objects of any type. If object name arguments are passed to the command then this flag will list all Dag objects below the specified object(s).
        - defaultNodes (dn): Returns default nodes. A default node is one that Maya creates automatically and does not get saved out with the scene, although some of its attribute values may.
        - dependencyNodes (dep): List dependency nodes. (including Dag objects)
        - exactType (et): List all objects of the specified type, butnotobjects that are descendents of that type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This
            flag cannot be used in conjunction with the type or excludeType flag.
        - excludeType (ext): List all objects that are not of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This flag cannot be used in conjunction
            with the type or exactType flag.
        - flatten (fl): Flattens the returned list of objects so that each component is identified individually.
        - geometry (g): List geometric Dag objects.
        - ghost (gh): List ghosting objects.
        - head (hd): This flag  specifies the maximum number of elements to be returned from the beginning of the list of items. Note: each type flag will return at most this many items so if multiple type flags are specified then the number of items returned
            can be greater than this amount.
        - hilite (hl): List objects that are currently hilited for component selection.
        - intermediateObjects (io): List only intermediate dag nodes.
        - invisible (iv): List only invisible dag nodes.
        - leaf (lf): List all leaf nodes in Dag. This flag is a modifier and must be used in conjunction with the -dag flag.
        - lights (lt): List light shapes.
        - live (lv): List objects that are currently live.
        - lockedNodes (ln): Returns locked nodes, which cannot be deleted or renamed. However, their status may change.
        - long (l): Return full path names for Dag objects. By default the shortest unique name is returned.
        - materials (mat): List materials or shading groups.
        - modified (mod): When this flag is set, only nodes modified since the last save will be returned.
        - noIntermediate (ni): List only non intermediate dag nodes.
        - nodeTypes (nt): Lists all registered node types.
        - objectsOnly (o): When this flag is set only object names will be returned and components/attributes will be ignored.
        - orderedComponentSelection (ocs): Return component selections ordered by their shape instead of selection order.
        - orderedSelection (os): List objects and components that are currently selected in their order of selection.  This flag depends on the value of the -tso/trackSelectionOrder flag of the selectPref command.  If that flag is not enabled than this flag will return the
            same thing as the -sl/selection flag would.
        - partitions (pr): List partitions.
        - persistentNodes (pn): Returns persistent nodes, which are nodes that stay in the Maya session after a file > new. These are a special class of default nodes that do not get reset on file > new. Ex: itemFilter and selectionListOperator nodes.
        - planes (pl): List construction plane shapes.
        - preSelectHilite (psh): List components that are currently hilited for pre-selection.
        - readOnly (ro): Returns referenced nodes. Referenced nodes are read only. NOTE: Obsolete. Please use "-referencedNodes".
        - recursive (r): When set to true, this command will look for name matches in all namespaces. When set to false, this command will only look for matches in namespaces that are requested (e.g. by specifying a name containing the ':'... "ns1:pSphere1").
        - referencedNodes (rn): Returns referenced nodes. Referenced nodes are read only.
        - references (rf): List references associated with files. Excludes special reference nodes such as the sharedReferenceNode and unknown reference nodes.
        - renderGlobals (rg): List render globals.
        - renderQualities (rq): List named render qualities.
        - renderResolutions (rr): List render resolutions.
        - renderSetups (rs): Alias for-renderGlobals.
        - selection (sl): List objects that are currently selected.
        - sets (set): List sets.
        - shapes (s): List shape objects.
        - shortNames (sn): Return short attribute names. By default long attribute names are returned.
        - showNamespace (sns): Show the namespace of each object after the object name.This flag cannot be used in conjunction with the showType flag.
        - showType (st): List the type of each object after its name.
        - tail (tl): This flag specifies the maximum number of elements to be returned from the end of the list of items. Note: each    type flag will return at most this many items so if multiple type flags are specified then the number of items returned can
            be greater than this amount
        - templated (tm): List only templated dag nodes.
        - textures (tex): List textures.
        - transforms (tr): List transform objects.
        - type (typ): List all objects of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag. Note: some selection items in Maya do not have a
            specific object/data type associated with them and will return "untyped" when listed with this flag.This flag cannot be used in conjunction with the exactType or excludeType flag.
        - ufeObjects (ufe): When used in conjunction with the-sl/selectionflag, will return objects that are defined through the UFE interface as well as native Maya objects.
        - undeletable (ud): Returns nodes that cannot be deleted (which includes locked nodes). These nodes also cannot be renamed.
        - untemplated (ut): List only un-templated dag nodes.
        - uuid (uid): Return node UUIDs instead of names. Note that there are no "UUID paths" - combining this flag with e.g. the -long flag will not result in a path formed of node UUIDs.
        - visible (v): List only visible dag nodes.
    """
@overload #Overload for ls in ['query']
def ls([object [object...]]: [object [object...]], containerType: str = ..., exactType: str = ..., excludeType: str = ..., type: str = ..., query: bool = ...) -> list[str]:
    """ls is undoable, NOT queryable, and NOT editable.
    
    The `ls` command returns the names (and optionally the type names) of objects
    in the scene.
    
    The most common use of `ls` is to filter or match objects based on their name
    (using wildcards) or based on their type. By default `ls` will match any
    object in the scene but it can also be used to filter or list the selected
    objects when used in conjunction with the -selection flag.
    
    If type names are requested, using the showType flag, they will be interleaved
    with object names so the result will be pairs of <object, type> values.
    
    Internal nodes (for example itemFilter nodes) are typically filtered so that
    only scene objects are returned. However, using a wildcard will cause all the
    nodes matching the wild card to show up, including internal nodes. For
    example, `ls *` will list all nodes whether internal or not.
    
    Use the syntax "::" to denote a recursive namespace search when listing nodes.
    For example, `ls "::pSphere1"` would match objects named "pSphere1" in any
    namespace, at any depth. `ls "ns::*"` would match any node in namespace "ns"
    or children namespaces.
    
    When Maya is in relativeNames mode, the `ls` command will return names
    relative to the current namespace and `ls *` will list from the the current
    namespace. For more details, please refer to the `-relativeNames` flag of the
    `namespace` command.
    
    The command may also be passed node UUIDs instead of names/paths, and can
    return UUIDs instead of names via the -uuid flag.

    ---
    - Args:
        - [object [object...]]: Input item(s).
        - containerType (ct): List containers with the specified user-defined type.This flag cannot be used in conjunction with the type or exactType flag.
        - exactType (et): List all objects of the specified type, butnotobjects that are descendents of that type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This
            flag cannot be used in conjunction with the type or excludeType flag.
        - excludeType (ext): List all objects that are not of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This flag cannot be used in conjunction
            with the type or exactType flag.
        - type (typ): List all objects of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag. Note: some selection items in Maya do not have a
            specific object/data type associated with them and will return "untyped" when listed with this flag.This flag cannot be used in conjunction with the exactType or excludeType flag.
        - query (q): Query mode flag
    """
@overload #Overload for ls in ['query']
def ls([object [object...]]: [object [object...]], ct: str = ..., et: str = ..., ext: str = ..., typ: str = ..., q: bool = ...) -> list[str]:
    """ls is undoable, NOT queryable, and NOT editable.
    
    The `ls` command returns the names (and optionally the type names) of objects
    in the scene.
    
    The most common use of `ls` is to filter or match objects based on their name
    (using wildcards) or based on their type. By default `ls` will match any
    object in the scene but it can also be used to filter or list the selected
    objects when used in conjunction with the -selection flag.
    
    If type names are requested, using the showType flag, they will be interleaved
    with object names so the result will be pairs of <object, type> values.
    
    Internal nodes (for example itemFilter nodes) are typically filtered so that
    only scene objects are returned. However, using a wildcard will cause all the
    nodes matching the wild card to show up, including internal nodes. For
    example, `ls *` will list all nodes whether internal or not.
    
    Use the syntax "::" to denote a recursive namespace search when listing nodes.
    For example, `ls "::pSphere1"` would match objects named "pSphere1" in any
    namespace, at any depth. `ls "ns::*"` would match any node in namespace "ns"
    or children namespaces.
    
    When Maya is in relativeNames mode, the `ls` command will return names
    relative to the current namespace and `ls *` will list from the the current
    namespace. For more details, please refer to the `-relativeNames` flag of the
    `namespace` command.
    
    The command may also be passed node UUIDs instead of names/paths, and can
    return UUIDs instead of names via the -uuid flag.

    ---
    - Args:
        - [object [object...]]: Input item(s).
        - containerType (ct): List containers with the specified user-defined type.This flag cannot be used in conjunction with the type or exactType flag.
        - exactType (et): List all objects of the specified type, butnotobjects that are descendents of that type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This
            flag cannot be used in conjunction with the type or excludeType flag.
        - excludeType (ext): List all objects that are not of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This flag cannot be used in conjunction
            with the type or exactType flag.
        - type (typ): List all objects of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag. Note: some selection items in Maya do not have a
            specific object/data type associated with them and will return "untyped" when listed with this flag.This flag cannot be used in conjunction with the exactType or excludeType flag.
        - query (q): Query mode flag
    """
@overload #Overload for ls in ['query']
def ls([object [object...]]: [object [object...]], containerType: str = ..., ct: str = ..., exactType: str = ..., et: str = ..., excludeType: str = ..., ext: str = ..., type: str = ..., typ: str = ..., query: bool = ..., q: bool = ...) -> list[str]:
    """ls is undoable, NOT queryable, and NOT editable.
    
    The `ls` command returns the names (and optionally the type names) of objects
    in the scene.
    
    The most common use of `ls` is to filter or match objects based on their name
    (using wildcards) or based on their type. By default `ls` will match any
    object in the scene but it can also be used to filter or list the selected
    objects when used in conjunction with the -selection flag.
    
    If type names are requested, using the showType flag, they will be interleaved
    with object names so the result will be pairs of <object, type> values.
    
    Internal nodes (for example itemFilter nodes) are typically filtered so that
    only scene objects are returned. However, using a wildcard will cause all the
    nodes matching the wild card to show up, including internal nodes. For
    example, `ls *` will list all nodes whether internal or not.
    
    Use the syntax "::" to denote a recursive namespace search when listing nodes.
    For example, `ls "::pSphere1"` would match objects named "pSphere1" in any
    namespace, at any depth. `ls "ns::*"` would match any node in namespace "ns"
    or children namespaces.
    
    When Maya is in relativeNames mode, the `ls` command will return names
    relative to the current namespace and `ls *` will list from the the current
    namespace. For more details, please refer to the `-relativeNames` flag of the
    `namespace` command.
    
    The command may also be passed node UUIDs instead of names/paths, and can
    return UUIDs instead of names via the -uuid flag.

    ---
    - Args:
        - [object [object...]]: Input item(s).
        - containerType (ct): List containers with the specified user-defined type.This flag cannot be used in conjunction with the type or exactType flag.
        - exactType (et): List all objects of the specified type, butnotobjects that are descendents of that type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This
            flag cannot be used in conjunction with the type or excludeType flag.
        - excludeType (ext): List all objects that are not of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This flag cannot be used in conjunction
            with the type or exactType flag.
        - type (typ): List all objects of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag. Note: some selection items in Maya do not have a
            specific object/data type associated with them and will return "untyped" when listed with this flag.This flag cannot be used in conjunction with the exactType or excludeType flag.
        - query (q): Query mode flag
    """
@overload #Overload for ls in ['edit']
def ls([object [object...]]: [object [object...]], containerType: str = ..., exactType: str = ..., excludeType: str = ..., type: str = ..., edit: bool = ...) -> list[str]:
    """ls is undoable, NOT queryable, and NOT editable.
    
    The `ls` command returns the names (and optionally the type names) of objects
    in the scene.
    
    The most common use of `ls` is to filter or match objects based on their name
    (using wildcards) or based on their type. By default `ls` will match any
    object in the scene but it can also be used to filter or list the selected
    objects when used in conjunction with the -selection flag.
    
    If type names are requested, using the showType flag, they will be interleaved
    with object names so the result will be pairs of <object, type> values.
    
    Internal nodes (for example itemFilter nodes) are typically filtered so that
    only scene objects are returned. However, using a wildcard will cause all the
    nodes matching the wild card to show up, including internal nodes. For
    example, `ls *` will list all nodes whether internal or not.
    
    Use the syntax "::" to denote a recursive namespace search when listing nodes.
    For example, `ls "::pSphere1"` would match objects named "pSphere1" in any
    namespace, at any depth. `ls "ns::*"` would match any node in namespace "ns"
    or children namespaces.
    
    When Maya is in relativeNames mode, the `ls` command will return names
    relative to the current namespace and `ls *` will list from the the current
    namespace. For more details, please refer to the `-relativeNames` flag of the
    `namespace` command.
    
    The command may also be passed node UUIDs instead of names/paths, and can
    return UUIDs instead of names via the -uuid flag.

    ---
    - Args:
        - [object [object...]]: Input item(s).
        - containerType (ct): List containers with the specified user-defined type.This flag cannot be used in conjunction with the type or exactType flag.
        - exactType (et): List all objects of the specified type, butnotobjects that are descendents of that type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This
            flag cannot be used in conjunction with the type or excludeType flag.
        - excludeType (ext): List all objects that are not of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This flag cannot be used in conjunction
            with the type or exactType flag.
        - type (typ): List all objects of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag. Note: some selection items in Maya do not have a
            specific object/data type associated with them and will return "untyped" when listed with this flag.This flag cannot be used in conjunction with the exactType or excludeType flag.
        - edit (e): Edit mode flag
    """
@overload #Overload for ls in ['edit']
def ls([object [object...]]: [object [object...]], ct: str = ..., et: str = ..., ext: str = ..., typ: str = ..., e: bool = ...) -> list[str]:
    """ls is undoable, NOT queryable, and NOT editable.
    
    The `ls` command returns the names (and optionally the type names) of objects
    in the scene.
    
    The most common use of `ls` is to filter or match objects based on their name
    (using wildcards) or based on their type. By default `ls` will match any
    object in the scene but it can also be used to filter or list the selected
    objects when used in conjunction with the -selection flag.
    
    If type names are requested, using the showType flag, they will be interleaved
    with object names so the result will be pairs of <object, type> values.
    
    Internal nodes (for example itemFilter nodes) are typically filtered so that
    only scene objects are returned. However, using a wildcard will cause all the
    nodes matching the wild card to show up, including internal nodes. For
    example, `ls *` will list all nodes whether internal or not.
    
    Use the syntax "::" to denote a recursive namespace search when listing nodes.
    For example, `ls "::pSphere1"` would match objects named "pSphere1" in any
    namespace, at any depth. `ls "ns::*"` would match any node in namespace "ns"
    or children namespaces.
    
    When Maya is in relativeNames mode, the `ls` command will return names
    relative to the current namespace and `ls *` will list from the the current
    namespace. For more details, please refer to the `-relativeNames` flag of the
    `namespace` command.
    
    The command may also be passed node UUIDs instead of names/paths, and can
    return UUIDs instead of names via the -uuid flag.

    ---
    - Args:
        - [object [object...]]: Input item(s).
        - containerType (ct): List containers with the specified user-defined type.This flag cannot be used in conjunction with the type or exactType flag.
        - exactType (et): List all objects of the specified type, butnotobjects that are descendents of that type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This
            flag cannot be used in conjunction with the type or excludeType flag.
        - excludeType (ext): List all objects that are not of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This flag cannot be used in conjunction
            with the type or exactType flag.
        - type (typ): List all objects of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag. Note: some selection items in Maya do not have a
            specific object/data type associated with them and will return "untyped" when listed with this flag.This flag cannot be used in conjunction with the exactType or excludeType flag.
        - edit (e): Edit mode flag
    """
@overload #Overload for ls in ['edit']
def ls([object [object...]]: [object [object...]], containerType: str = ..., ct: str = ..., exactType: str = ..., et: str = ..., excludeType: str = ..., ext: str = ..., type: str = ..., typ: str = ..., edit: bool = ..., e: bool = ...) -> list[str]:
    """ls is undoable, NOT queryable, and NOT editable.
    
    The `ls` command returns the names (and optionally the type names) of objects
    in the scene.
    
    The most common use of `ls` is to filter or match objects based on their name
    (using wildcards) or based on their type. By default `ls` will match any
    object in the scene but it can also be used to filter or list the selected
    objects when used in conjunction with the -selection flag.
    
    If type names are requested, using the showType flag, they will be interleaved
    with object names so the result will be pairs of <object, type> values.
    
    Internal nodes (for example itemFilter nodes) are typically filtered so that
    only scene objects are returned. However, using a wildcard will cause all the
    nodes matching the wild card to show up, including internal nodes. For
    example, `ls *` will list all nodes whether internal or not.
    
    Use the syntax "::" to denote a recursive namespace search when listing nodes.
    For example, `ls "::pSphere1"` would match objects named "pSphere1" in any
    namespace, at any depth. `ls "ns::*"` would match any node in namespace "ns"
    or children namespaces.
    
    When Maya is in relativeNames mode, the `ls` command will return names
    relative to the current namespace and `ls *` will list from the the current
    namespace. For more details, please refer to the `-relativeNames` flag of the
    `namespace` command.
    
    The command may also be passed node UUIDs instead of names/paths, and can
    return UUIDs instead of names via the -uuid flag.

    ---
    - Args:
        - [object [object...]]: Input item(s).
        - containerType (ct): List containers with the specified user-defined type.This flag cannot be used in conjunction with the type or exactType flag.
        - exactType (et): List all objects of the specified type, butnotobjects that are descendents of that type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This
            flag cannot be used in conjunction with the type or excludeType flag.
        - excludeType (ext): List all objects that are not of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.This flag cannot be used in conjunction
            with the type or exactType flag.
        - type (typ): List all objects of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag. Note: some selection items in Maya do not have a
            specific object/data type associated with them and will return "untyped" when listed with this flag.This flag cannot be used in conjunction with the exactType or excludeType flag.
        - edit (e): Edit mode flag
    """
