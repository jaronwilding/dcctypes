"""Stub files for General category in Maya commands, command: sets."""

from typing import Any, overload

@overload #Overload for sets in ['create']
def sets(selectionList: selectionList, anyMember: name = ..., channelSetColor: [float, float, float] = ..., channelSetColorIndex: int = ..., color: int = ..., copy: name = ..., edges: bool = ..., editPoints: bool = ..., empty: bool = ..., facets: bool = ..., intersection: name = ..., isIntersecting: name = ..., isMember: name = ..., layer: bool = ..., name: str = ..., noIntermediate: bool = ..., noSurfaceShader: bool = ..., noWarnings: bool = ..., renderable: bool = ..., split: name = ..., subtract: name = ..., text: str = ..., union: name = ..., vertices: bool = ...) -> str | list[str] | bool:
    """sets is undoable, queryable, and editable.
    
    This command is used to create a set, query some state of a set, or perform
    operations to update the membership of a set. A set is a logical grouping of
    an arbitrary collection of objects, attributes, or components of objects. Sets
    are dependency nodes. Connections from objects to a set define membership in
    the set.
    
    Sets are used throughout Maya in a multitude of ways. They are used to define
    an association of material properties to objects, to define an association of
    lights to objects, to define a bookmark or named collection of objects, to
    define a character, and to define the components to be deformed by some
    deformation operation.
    
    Sets can be connected to any number of partitions. A partition is a node which
    enforces mutual exclusivity amoung the sets in the partition. That is, if an
    object is in a set which is in a partition, that object cannot be a member of
    any other set that is in the partition.
    
    Without any flags, the sets command will create a set with a default name of
    "set#" (where # is an integer). If no items are specified on the command line,
    the currently selected items are added to the set. The -em/empty flag can be
    used to create an empty set and not have the selected items added to the set.
    
    Sets can be created to have certain restrictions on membership. There can be
    "renderable" sets which only allow renderable objects (such as nurbs geometry
    or polymesh faces) to be members of the set. There can also be vertex (or
    control point), edit point, edge, or face sets which only allow those types of
    components to be members of a set. Note that for these sets, if an object with
    a valid type of component is to be added to a set, the components of the
    object are added to the set instead.
    
    Sets can have an associated color which is only of use when creating vertex
    sets. The color can be one of the eight user defined colors defined in the
    color preferences. This color can be used, for example to distinguish which
    vertices are being deformed by a particular deformation.
    
    Objects, components, or attributes can be added to a set using one of three
    flags. The -add/addElement flag will add the objects to a set as long as this
    won't break any mutual exclusivity constraints. If there are any items which
    can't be added, the command will fail. The -in/include flag will only add
    those items which can be added and warn of those which can't. The
    -fe/forceElement flag will add all the items to the set but will also remove
    any of those items that are in any other set which is in the same partition as
    the set.
    
    There are several operations on sets that can be performed with the sets
    command. Membership can be queried. Tests for whether an item is in a set or
    whether two sets share the same item can be performed. Also, the union,
    intersection and difference of sets can be performed which returns a list of
    members of the sets which are a result of the operation.

    Example:
    ```python
        import maya.cmds as cmds
        # create some objects
        cmds.sphere( n="sphere1" )
        cmds.cone( n="cone1" )
        # create a set with whatever is currently active
        cmds.select( 'sphere1' )
        newSet1 = cmds.sets()
        cmds.select( 'cone1' )
        newSet2 = cmds.sets()
        # Query the members of a set
        cmds.sets( newSet1, q=True )
        # create a set which contains two sets
        cmds.sets( newSet1, newSet2, n="setOfSets" )
        # To select a set, the -noExpand flag must be used. Otherwise
        # the members of a set are selected instead.
        cmds.select( newSet1, noExpand=True )
        cmds.ls( selection=True )
        # Select the members of a set
        cmds.select( newSet1 )
        cmds.ls( selection=True )
        # Create a vertex set named ballVertices. This will contain
        # all the vertices of the sphere.
        cmds.sets( 'sphere1', n="ballVertices", v=1 )
        cmds.select( 'ballVertices' )
        # Return the union of two sets
        cmds.sets( newSet2, un=newSet1 )
        # Test whether a list of sets have common members
        cmds.sets( 'ballVertices',ii=newSet1)
        # Test whether the sphere is a member of the set
        cmds.sets('sphere1',im=newSet1)
        # Remove the sphere from a set
        cmds.sets( 'sphere1', rm=newSet1 )
        # Test again whether the sphere is a member of the set
        cmds.sets( 'sphere1', im=newSet1 )
    ```

    ---
    - Args:
        - selectionList: Input item(s).
        - anyMember (am): An operation which tests whether any of the given items are members of the given set.
        - channelSetColor (csc): Defines the custom color for the channel set to be shown in the dope sheet. This custom color is used when the channelSetColorIndex is -1.
        - channelSetColorIndex (coi): Defines the index for the color used to show the channel set in the dope sheet. The color is assigned by the UI using the index to cycle through the available colors. A special case is if the index is == -1, then the channelSetColor RGB
            values define the color.
        - color (co): Defines the hilite color of the set. Must be a value in range [-1, 7] (one of the user defined colors).  -1 marks the color has being undefined and therefore not having any affect. Only the vertices of a vertex set will be displayed in this
            color.
        - copy (cp): Copies the members of the given set to a new set. This flag is for use in creation mode only.
        - edges (eg): Indicates the new set can contain edges only. This flag is for use in creation or query mode only. The default value is false.
        - editPoints (ep): Indicates the new set can contain editPoints only. This flag is for use in creation or query mode only. The default value is false.
        - empty (em): Indicates that the set to be created should be empty. That is, it ignores any arguments identifying objects to be added to the set. This flag is only valid for operations that create a new set.
        - facets (fc): Indicates the new set can contain facets only. This flag is for use in creation or query mode only. The default value is false.
        - intersection (int): An operation that returns a list of items which are members of all the sets in the list.
        - isIntersecting (ii): An operation which tests whether the sets in the list have common members.
        - isMember (im): An operation which tests whether all the given items are members of the given set.
        - layer (l): OBSOLETE. DO NOT USE.
        - name (n): Assigns string as the name for a new set. This flag is only valid for operations that create a new set.
        - noIntermediate (ni): Excludes intermediate objects when querying set members or using the subtract, union, itersection, or isIntersecting flags.
        - noSurfaceShader (nss): If set is renderable, do not connect it to the default surface shader.  Flag has no meaning or effect for non renderable sets. This flag is for use in creation mode only. The default value is false.
        - noWarnings (nw): Indicates that warning messages should not be reported such as when trying to add an invalid item to a set. (used by UI)
        - renderable (r): This flag indicates that a special type of set should be created. This type of set (shadingEngine as opposed to objectSet) has certain restrictions on its membership in that it can only contain renderable elements such as lights and
            geometry. These sets are referred to as shading groups and are automatically connected to the "renderPartition" node when created (to ensure mutual exclusivity of the set's members with the other sets in the partition). This flag is for use
            in creation or query mode only. The default value is false which means a normal set is created.
        - split (sp): Produces a new set with the list of items and removes each item in the list of items from the given set.
        - subtract (sub): An operation between two sets which returns the members of the first set that are not in the second set.
        - text (t): Defines an annotation string to be stored with the set.
        - union (un): An operation that returns a list of all the members of all sets listed.
        - vertices (v): Indicates the new set can contain vertices only. This flag is for use in creation or query mode only. The default value is false.
    """
@overload #Overload for sets in ['create']
def sets(selectionList: selectionList, am: name = ..., csc: [float, float, float] = ..., coi: int = ..., co: int = ..., cp: name = ..., eg: bool = ..., ep: bool = ..., em: bool = ..., fc: bool = ..., int: name = ..., ii: name = ..., im: name = ..., l: bool = ..., n: str = ..., ni: bool = ..., nss: bool = ..., nw: bool = ..., r: bool = ..., sp: name = ..., sub: name = ..., t: str = ..., un: name = ..., v: bool = ...) -> str | list[str] | bool:
    """sets is undoable, queryable, and editable.
    
    This command is used to create a set, query some state of a set, or perform
    operations to update the membership of a set. A set is a logical grouping of
    an arbitrary collection of objects, attributes, or components of objects. Sets
    are dependency nodes. Connections from objects to a set define membership in
    the set.
    
    Sets are used throughout Maya in a multitude of ways. They are used to define
    an association of material properties to objects, to define an association of
    lights to objects, to define a bookmark or named collection of objects, to
    define a character, and to define the components to be deformed by some
    deformation operation.
    
    Sets can be connected to any number of partitions. A partition is a node which
    enforces mutual exclusivity amoung the sets in the partition. That is, if an
    object is in a set which is in a partition, that object cannot be a member of
    any other set that is in the partition.
    
    Without any flags, the sets command will create a set with a default name of
    "set#" (where # is an integer). If no items are specified on the command line,
    the currently selected items are added to the set. The -em/empty flag can be
    used to create an empty set and not have the selected items added to the set.
    
    Sets can be created to have certain restrictions on membership. There can be
    "renderable" sets which only allow renderable objects (such as nurbs geometry
    or polymesh faces) to be members of the set. There can also be vertex (or
    control point), edit point, edge, or face sets which only allow those types of
    components to be members of a set. Note that for these sets, if an object with
    a valid type of component is to be added to a set, the components of the
    object are added to the set instead.
    
    Sets can have an associated color which is only of use when creating vertex
    sets. The color can be one of the eight user defined colors defined in the
    color preferences. This color can be used, for example to distinguish which
    vertices are being deformed by a particular deformation.
    
    Objects, components, or attributes can be added to a set using one of three
    flags. The -add/addElement flag will add the objects to a set as long as this
    won't break any mutual exclusivity constraints. If there are any items which
    can't be added, the command will fail. The -in/include flag will only add
    those items which can be added and warn of those which can't. The
    -fe/forceElement flag will add all the items to the set but will also remove
    any of those items that are in any other set which is in the same partition as
    the set.
    
    There are several operations on sets that can be performed with the sets
    command. Membership can be queried. Tests for whether an item is in a set or
    whether two sets share the same item can be performed. Also, the union,
    intersection and difference of sets can be performed which returns a list of
    members of the sets which are a result of the operation.

    Example:
    ```python
        import maya.cmds as cmds
        # create some objects
        cmds.sphere( n="sphere1" )
        cmds.cone( n="cone1" )
        # create a set with whatever is currently active
        cmds.select( 'sphere1' )
        newSet1 = cmds.sets()
        cmds.select( 'cone1' )
        newSet2 = cmds.sets()
        # Query the members of a set
        cmds.sets( newSet1, q=True )
        # create a set which contains two sets
        cmds.sets( newSet1, newSet2, n="setOfSets" )
        # To select a set, the -noExpand flag must be used. Otherwise
        # the members of a set are selected instead.
        cmds.select( newSet1, noExpand=True )
        cmds.ls( selection=True )
        # Select the members of a set
        cmds.select( newSet1 )
        cmds.ls( selection=True )
        # Create a vertex set named ballVertices. This will contain
        # all the vertices of the sphere.
        cmds.sets( 'sphere1', n="ballVertices", v=1 )
        cmds.select( 'ballVertices' )
        # Return the union of two sets
        cmds.sets( newSet2, un=newSet1 )
        # Test whether a list of sets have common members
        cmds.sets( 'ballVertices',ii=newSet1)
        # Test whether the sphere is a member of the set
        cmds.sets('sphere1',im=newSet1)
        # Remove the sphere from a set
        cmds.sets( 'sphere1', rm=newSet1 )
        # Test again whether the sphere is a member of the set
        cmds.sets( 'sphere1', im=newSet1 )
    ```

    ---
    - Args:
        - selectionList: Input item(s).
        - anyMember (am): An operation which tests whether any of the given items are members of the given set.
        - channelSetColor (csc): Defines the custom color for the channel set to be shown in the dope sheet. This custom color is used when the channelSetColorIndex is -1.
        - channelSetColorIndex (coi): Defines the index for the color used to show the channel set in the dope sheet. The color is assigned by the UI using the index to cycle through the available colors. A special case is if the index is == -1, then the channelSetColor RGB
            values define the color.
        - color (co): Defines the hilite color of the set. Must be a value in range [-1, 7] (one of the user defined colors).  -1 marks the color has being undefined and therefore not having any affect. Only the vertices of a vertex set will be displayed in this
            color.
        - copy (cp): Copies the members of the given set to a new set. This flag is for use in creation mode only.
        - edges (eg): Indicates the new set can contain edges only. This flag is for use in creation or query mode only. The default value is false.
        - editPoints (ep): Indicates the new set can contain editPoints only. This flag is for use in creation or query mode only. The default value is false.
        - empty (em): Indicates that the set to be created should be empty. That is, it ignores any arguments identifying objects to be added to the set. This flag is only valid for operations that create a new set.
        - facets (fc): Indicates the new set can contain facets only. This flag is for use in creation or query mode only. The default value is false.
        - intersection (int): An operation that returns a list of items which are members of all the sets in the list.
        - isIntersecting (ii): An operation which tests whether the sets in the list have common members.
        - isMember (im): An operation which tests whether all the given items are members of the given set.
        - layer (l): OBSOLETE. DO NOT USE.
        - name (n): Assigns string as the name for a new set. This flag is only valid for operations that create a new set.
        - noIntermediate (ni): Excludes intermediate objects when querying set members or using the subtract, union, itersection, or isIntersecting flags.
        - noSurfaceShader (nss): If set is renderable, do not connect it to the default surface shader.  Flag has no meaning or effect for non renderable sets. This flag is for use in creation mode only. The default value is false.
        - noWarnings (nw): Indicates that warning messages should not be reported such as when trying to add an invalid item to a set. (used by UI)
        - renderable (r): This flag indicates that a special type of set should be created. This type of set (shadingEngine as opposed to objectSet) has certain restrictions on its membership in that it can only contain renderable elements such as lights and
            geometry. These sets are referred to as shading groups and are automatically connected to the "renderPartition" node when created (to ensure mutual exclusivity of the set's members with the other sets in the partition). This flag is for use
            in creation or query mode only. The default value is false which means a normal set is created.
        - split (sp): Produces a new set with the list of items and removes each item in the list of items from the given set.
        - subtract (sub): An operation between two sets which returns the members of the first set that are not in the second set.
        - text (t): Defines an annotation string to be stored with the set.
        - union (un): An operation that returns a list of all the members of all sets listed.
        - vertices (v): Indicates the new set can contain vertices only. This flag is for use in creation or query mode only. The default value is false.
    """
@overload #Overload for sets in ['create']
def sets(selectionList: selectionList, anyMember: name = ..., am: name = ..., channelSetColor: [float, float, float] = ..., csc: [float, float, float] = ..., channelSetColorIndex: int = ..., coi: int = ..., color: int = ..., co: int = ..., copy: name = ..., cp: name = ..., edges: bool = ..., eg: bool = ..., editPoints: bool = ..., ep: bool = ..., empty: bool = ..., em: bool = ..., facets: bool = ..., fc: bool = ..., intersection: name = ..., int: name = ..., isIntersecting: name = ..., ii: name = ..., isMember: name = ..., im: name = ..., layer: bool = ..., l: bool = ..., name: str = ..., n: str = ..., noIntermediate: bool = ..., ni: bool = ..., noSurfaceShader: bool = ..., nss: bool = ..., noWarnings: bool = ..., nw: bool = ..., renderable: bool = ..., r: bool = ..., split: name = ..., sp: name = ..., subtract: name = ..., sub: name = ..., text: str = ..., t: str = ..., union: name = ..., un: name = ..., vertices: bool = ..., v: bool = ...) -> str | list[str] | bool:
    """sets is undoable, queryable, and editable.
    
    This command is used to create a set, query some state of a set, or perform
    operations to update the membership of a set. A set is a logical grouping of
    an arbitrary collection of objects, attributes, or components of objects. Sets
    are dependency nodes. Connections from objects to a set define membership in
    the set.
    
    Sets are used throughout Maya in a multitude of ways. They are used to define
    an association of material properties to objects, to define an association of
    lights to objects, to define a bookmark or named collection of objects, to
    define a character, and to define the components to be deformed by some
    deformation operation.
    
    Sets can be connected to any number of partitions. A partition is a node which
    enforces mutual exclusivity amoung the sets in the partition. That is, if an
    object is in a set which is in a partition, that object cannot be a member of
    any other set that is in the partition.
    
    Without any flags, the sets command will create a set with a default name of
    "set#" (where # is an integer). If no items are specified on the command line,
    the currently selected items are added to the set. The -em/empty flag can be
    used to create an empty set and not have the selected items added to the set.
    
    Sets can be created to have certain restrictions on membership. There can be
    "renderable" sets which only allow renderable objects (such as nurbs geometry
    or polymesh faces) to be members of the set. There can also be vertex (or
    control point), edit point, edge, or face sets which only allow those types of
    components to be members of a set. Note that for these sets, if an object with
    a valid type of component is to be added to a set, the components of the
    object are added to the set instead.
    
    Sets can have an associated color which is only of use when creating vertex
    sets. The color can be one of the eight user defined colors defined in the
    color preferences. This color can be used, for example to distinguish which
    vertices are being deformed by a particular deformation.
    
    Objects, components, or attributes can be added to a set using one of three
    flags. The -add/addElement flag will add the objects to a set as long as this
    won't break any mutual exclusivity constraints. If there are any items which
    can't be added, the command will fail. The -in/include flag will only add
    those items which can be added and warn of those which can't. The
    -fe/forceElement flag will add all the items to the set but will also remove
    any of those items that are in any other set which is in the same partition as
    the set.
    
    There are several operations on sets that can be performed with the sets
    command. Membership can be queried. Tests for whether an item is in a set or
    whether two sets share the same item can be performed. Also, the union,
    intersection and difference of sets can be performed which returns a list of
    members of the sets which are a result of the operation.

    Example:
    ```python
        import maya.cmds as cmds
        # create some objects
        cmds.sphere( n="sphere1" )
        cmds.cone( n="cone1" )
        # create a set with whatever is currently active
        cmds.select( 'sphere1' )
        newSet1 = cmds.sets()
        cmds.select( 'cone1' )
        newSet2 = cmds.sets()
        # Query the members of a set
        cmds.sets( newSet1, q=True )
        # create a set which contains two sets
        cmds.sets( newSet1, newSet2, n="setOfSets" )
        # To select a set, the -noExpand flag must be used. Otherwise
        # the members of a set are selected instead.
        cmds.select( newSet1, noExpand=True )
        cmds.ls( selection=True )
        # Select the members of a set
        cmds.select( newSet1 )
        cmds.ls( selection=True )
        # Create a vertex set named ballVertices. This will contain
        # all the vertices of the sphere.
        cmds.sets( 'sphere1', n="ballVertices", v=1 )
        cmds.select( 'ballVertices' )
        # Return the union of two sets
        cmds.sets( newSet2, un=newSet1 )
        # Test whether a list of sets have common members
        cmds.sets( 'ballVertices',ii=newSet1)
        # Test whether the sphere is a member of the set
        cmds.sets('sphere1',im=newSet1)
        # Remove the sphere from a set
        cmds.sets( 'sphere1', rm=newSet1 )
        # Test again whether the sphere is a member of the set
        cmds.sets( 'sphere1', im=newSet1 )
    ```

    ---
    - Args:
        - selectionList: Input item(s).
        - anyMember (am): An operation which tests whether any of the given items are members of the given set.
        - channelSetColor (csc): Defines the custom color for the channel set to be shown in the dope sheet. This custom color is used when the channelSetColorIndex is -1.
        - channelSetColorIndex (coi): Defines the index for the color used to show the channel set in the dope sheet. The color is assigned by the UI using the index to cycle through the available colors. A special case is if the index is == -1, then the channelSetColor RGB
            values define the color.
        - color (co): Defines the hilite color of the set. Must be a value in range [-1, 7] (one of the user defined colors).  -1 marks the color has being undefined and therefore not having any affect. Only the vertices of a vertex set will be displayed in this
            color.
        - copy (cp): Copies the members of the given set to a new set. This flag is for use in creation mode only.
        - edges (eg): Indicates the new set can contain edges only. This flag is for use in creation or query mode only. The default value is false.
        - editPoints (ep): Indicates the new set can contain editPoints only. This flag is for use in creation or query mode only. The default value is false.
        - empty (em): Indicates that the set to be created should be empty. That is, it ignores any arguments identifying objects to be added to the set. This flag is only valid for operations that create a new set.
        - facets (fc): Indicates the new set can contain facets only. This flag is for use in creation or query mode only. The default value is false.
        - intersection (int): An operation that returns a list of items which are members of all the sets in the list.
        - isIntersecting (ii): An operation which tests whether the sets in the list have common members.
        - isMember (im): An operation which tests whether all the given items are members of the given set.
        - layer (l): OBSOLETE. DO NOT USE.
        - name (n): Assigns string as the name for a new set. This flag is only valid for operations that create a new set.
        - noIntermediate (ni): Excludes intermediate objects when querying set members or using the subtract, union, itersection, or isIntersecting flags.
        - noSurfaceShader (nss): If set is renderable, do not connect it to the default surface shader.  Flag has no meaning or effect for non renderable sets. This flag is for use in creation mode only. The default value is false.
        - noWarnings (nw): Indicates that warning messages should not be reported such as when trying to add an invalid item to a set. (used by UI)
        - renderable (r): This flag indicates that a special type of set should be created. This type of set (shadingEngine as opposed to objectSet) has certain restrictions on its membership in that it can only contain renderable elements such as lights and
            geometry. These sets are referred to as shading groups and are automatically connected to the "renderPartition" node when created (to ensure mutual exclusivity of the set's members with the other sets in the partition). This flag is for use
            in creation or query mode only. The default value is false which means a normal set is created.
        - split (sp): Produces a new set with the list of items and removes each item in the list of items from the given set.
        - subtract (sub): An operation between two sets which returns the members of the first set that are not in the second set.
        - text (t): Defines an annotation string to be stored with the set.
        - union (un): An operation that returns a list of all the members of all sets listed.
        - vertices (v): Indicates the new set can contain vertices only. This flag is for use in creation or query mode only. The default value is false.
    """
@overload #Overload for sets in ['query']
def sets(selectionList: selectionList, channelSetColor: [float, float, float] = ..., channelSetColorIndex: int = ..., color: int = ..., edges: bool = ..., editPoints: bool = ..., facets: bool = ..., noIntermediate: bool = ..., nodesOnly: bool = ..., ordered: bool = ..., renderable: bool = ..., size: bool = ..., text: str = ..., vertices: bool = ..., query: bool = ...) -> str | list[str] | bool:
    """sets is undoable, queryable, and editable.
    
    This command is used to create a set, query some state of a set, or perform
    operations to update the membership of a set. A set is a logical grouping of
    an arbitrary collection of objects, attributes, or components of objects. Sets
    are dependency nodes. Connections from objects to a set define membership in
    the set.
    
    Sets are used throughout Maya in a multitude of ways. They are used to define
    an association of material properties to objects, to define an association of
    lights to objects, to define a bookmark or named collection of objects, to
    define a character, and to define the components to be deformed by some
    deformation operation.
    
    Sets can be connected to any number of partitions. A partition is a node which
    enforces mutual exclusivity amoung the sets in the partition. That is, if an
    object is in a set which is in a partition, that object cannot be a member of
    any other set that is in the partition.
    
    Without any flags, the sets command will create a set with a default name of
    "set#" (where # is an integer). If no items are specified on the command line,
    the currently selected items are added to the set. The -em/empty flag can be
    used to create an empty set and not have the selected items added to the set.
    
    Sets can be created to have certain restrictions on membership. There can be
    "renderable" sets which only allow renderable objects (such as nurbs geometry
    or polymesh faces) to be members of the set. There can also be vertex (or
    control point), edit point, edge, or face sets which only allow those types of
    components to be members of a set. Note that for these sets, if an object with
    a valid type of component is to be added to a set, the components of the
    object are added to the set instead.
    
    Sets can have an associated color which is only of use when creating vertex
    sets. The color can be one of the eight user defined colors defined in the
    color preferences. This color can be used, for example to distinguish which
    vertices are being deformed by a particular deformation.
    
    Objects, components, or attributes can be added to a set using one of three
    flags. The -add/addElement flag will add the objects to a set as long as this
    won't break any mutual exclusivity constraints. If there are any items which
    can't be added, the command will fail. The -in/include flag will only add
    those items which can be added and warn of those which can't. The
    -fe/forceElement flag will add all the items to the set but will also remove
    any of those items that are in any other set which is in the same partition as
    the set.
    
    There are several operations on sets that can be performed with the sets
    command. Membership can be queried. Tests for whether an item is in a set or
    whether two sets share the same item can be performed. Also, the union,
    intersection and difference of sets can be performed which returns a list of
    members of the sets which are a result of the operation.

    Example:
    ```python
        import maya.cmds as cmds
        # create some objects
        cmds.sphere( n="sphere1" )
        cmds.cone( n="cone1" )
        # create a set with whatever is currently active
        cmds.select( 'sphere1' )
        newSet1 = cmds.sets()
        cmds.select( 'cone1' )
        newSet2 = cmds.sets()
        # Query the members of a set
        cmds.sets( newSet1, q=True )
        # create a set which contains two sets
        cmds.sets( newSet1, newSet2, n="setOfSets" )
        # To select a set, the -noExpand flag must be used. Otherwise
        # the members of a set are selected instead.
        cmds.select( newSet1, noExpand=True )
        cmds.ls( selection=True )
        # Select the members of a set
        cmds.select( newSet1 )
        cmds.ls( selection=True )
        # Create a vertex set named ballVertices. This will contain
        # all the vertices of the sphere.
        cmds.sets( 'sphere1', n="ballVertices", v=1 )
        cmds.select( 'ballVertices' )
        # Return the union of two sets
        cmds.sets( newSet2, un=newSet1 )
        # Test whether a list of sets have common members
        cmds.sets( 'ballVertices',ii=newSet1)
        # Test whether the sphere is a member of the set
        cmds.sets('sphere1',im=newSet1)
        # Remove the sphere from a set
        cmds.sets( 'sphere1', rm=newSet1 )
        # Test again whether the sphere is a member of the set
        cmds.sets( 'sphere1', im=newSet1 )
    ```

    ---
    - Args:
        - selectionList: Input item(s).
        - channelSetColor (csc): Defines the custom color for the channel set to be shown in the dope sheet. This custom color is used when the channelSetColorIndex is -1.
        - channelSetColorIndex (coi): Defines the index for the color used to show the channel set in the dope sheet. The color is assigned by the UI using the index to cycle through the available colors. A special case is if the index is == -1, then the channelSetColor RGB
            values define the color.
        - color (co): Defines the hilite color of the set. Must be a value in range [-1, 7] (one of the user defined colors).  -1 marks the color has being undefined and therefore not having any affect. Only the vertices of a vertex set will be displayed in this
            color.
        - edges (eg): Indicates the new set can contain edges only. This flag is for use in creation or query mode only. The default value is false.
        - editPoints (ep): Indicates the new set can contain editPoints only. This flag is for use in creation or query mode only. The default value is false.
        - facets (fc): Indicates the new set can contain facets only. This flag is for use in creation or query mode only. The default value is false.
        - noIntermediate (ni): Excludes intermediate objects when querying set members or using the subtract, union, itersection, or isIntersecting flags.
        - nodesOnly (no): This flag is usable with the -q/query flag but is ignored if used with another queryable flags. This flag modifies the results of the set membership query such that when there are attributes (e.g. sphere1.tx) or components of nodes included
            in the set, only the nodes will be listed. Each node will only be listed once, even if more than one attribute or component of the node exists in the set.
        - ordered (o): When querying set members return them in the same order as they appear in the set.
        - renderable (r): This flag indicates that a special type of set should be created. This type of set (shadingEngine as opposed to objectSet) has certain restrictions on its membership in that it can only contain renderable elements such as lights and
            geometry. These sets are referred to as shading groups and are automatically connected to the "renderPartition" node when created (to ensure mutual exclusivity of the set's members with the other sets in the partition). This flag is for use
            in creation or query mode only. The default value is false which means a normal set is created.
        - size (s): Use the size flag to query the length of the set.
        - text (t): Defines an annotation string to be stored with the set.
        - vertices (v): Indicates the new set can contain vertices only. This flag is for use in creation or query mode only. The default value is false.
        - query (q): Query mode flag
    """
@overload #Overload for sets in ['query']
def sets(selectionList: selectionList, csc: [float, float, float] = ..., coi: int = ..., co: int = ..., eg: bool = ..., ep: bool = ..., fc: bool = ..., ni: bool = ..., no: bool = ..., o: bool = ..., r: bool = ..., s: bool = ..., t: str = ..., v: bool = ..., q: bool = ...) -> str | list[str] | bool:
    """sets is undoable, queryable, and editable.
    
    This command is used to create a set, query some state of a set, or perform
    operations to update the membership of a set. A set is a logical grouping of
    an arbitrary collection of objects, attributes, or components of objects. Sets
    are dependency nodes. Connections from objects to a set define membership in
    the set.
    
    Sets are used throughout Maya in a multitude of ways. They are used to define
    an association of material properties to objects, to define an association of
    lights to objects, to define a bookmark or named collection of objects, to
    define a character, and to define the components to be deformed by some
    deformation operation.
    
    Sets can be connected to any number of partitions. A partition is a node which
    enforces mutual exclusivity amoung the sets in the partition. That is, if an
    object is in a set which is in a partition, that object cannot be a member of
    any other set that is in the partition.
    
    Without any flags, the sets command will create a set with a default name of
    "set#" (where # is an integer). If no items are specified on the command line,
    the currently selected items are added to the set. The -em/empty flag can be
    used to create an empty set and not have the selected items added to the set.
    
    Sets can be created to have certain restrictions on membership. There can be
    "renderable" sets which only allow renderable objects (such as nurbs geometry
    or polymesh faces) to be members of the set. There can also be vertex (or
    control point), edit point, edge, or face sets which only allow those types of
    components to be members of a set. Note that for these sets, if an object with
    a valid type of component is to be added to a set, the components of the
    object are added to the set instead.
    
    Sets can have an associated color which is only of use when creating vertex
    sets. The color can be one of the eight user defined colors defined in the
    color preferences. This color can be used, for example to distinguish which
    vertices are being deformed by a particular deformation.
    
    Objects, components, or attributes can be added to a set using one of three
    flags. The -add/addElement flag will add the objects to a set as long as this
    won't break any mutual exclusivity constraints. If there are any items which
    can't be added, the command will fail. The -in/include flag will only add
    those items which can be added and warn of those which can't. The
    -fe/forceElement flag will add all the items to the set but will also remove
    any of those items that are in any other set which is in the same partition as
    the set.
    
    There are several operations on sets that can be performed with the sets
    command. Membership can be queried. Tests for whether an item is in a set or
    whether two sets share the same item can be performed. Also, the union,
    intersection and difference of sets can be performed which returns a list of
    members of the sets which are a result of the operation.

    Example:
    ```python
        import maya.cmds as cmds
        # create some objects
        cmds.sphere( n="sphere1" )
        cmds.cone( n="cone1" )
        # create a set with whatever is currently active
        cmds.select( 'sphere1' )
        newSet1 = cmds.sets()
        cmds.select( 'cone1' )
        newSet2 = cmds.sets()
        # Query the members of a set
        cmds.sets( newSet1, q=True )
        # create a set which contains two sets
        cmds.sets( newSet1, newSet2, n="setOfSets" )
        # To select a set, the -noExpand flag must be used. Otherwise
        # the members of a set are selected instead.
        cmds.select( newSet1, noExpand=True )
        cmds.ls( selection=True )
        # Select the members of a set
        cmds.select( newSet1 )
        cmds.ls( selection=True )
        # Create a vertex set named ballVertices. This will contain
        # all the vertices of the sphere.
        cmds.sets( 'sphere1', n="ballVertices", v=1 )
        cmds.select( 'ballVertices' )
        # Return the union of two sets
        cmds.sets( newSet2, un=newSet1 )
        # Test whether a list of sets have common members
        cmds.sets( 'ballVertices',ii=newSet1)
        # Test whether the sphere is a member of the set
        cmds.sets('sphere1',im=newSet1)
        # Remove the sphere from a set
        cmds.sets( 'sphere1', rm=newSet1 )
        # Test again whether the sphere is a member of the set
        cmds.sets( 'sphere1', im=newSet1 )
    ```

    ---
    - Args:
        - selectionList: Input item(s).
        - channelSetColor (csc): Defines the custom color for the channel set to be shown in the dope sheet. This custom color is used when the channelSetColorIndex is -1.
        - channelSetColorIndex (coi): Defines the index for the color used to show the channel set in the dope sheet. The color is assigned by the UI using the index to cycle through the available colors. A special case is if the index is == -1, then the channelSetColor RGB
            values define the color.
        - color (co): Defines the hilite color of the set. Must be a value in range [-1, 7] (one of the user defined colors).  -1 marks the color has being undefined and therefore not having any affect. Only the vertices of a vertex set will be displayed in this
            color.
        - edges (eg): Indicates the new set can contain edges only. This flag is for use in creation or query mode only. The default value is false.
        - editPoints (ep): Indicates the new set can contain editPoints only. This flag is for use in creation or query mode only. The default value is false.
        - facets (fc): Indicates the new set can contain facets only. This flag is for use in creation or query mode only. The default value is false.
        - noIntermediate (ni): Excludes intermediate objects when querying set members or using the subtract, union, itersection, or isIntersecting flags.
        - nodesOnly (no): This flag is usable with the -q/query flag but is ignored if used with another queryable flags. This flag modifies the results of the set membership query such that when there are attributes (e.g. sphere1.tx) or components of nodes included
            in the set, only the nodes will be listed. Each node will only be listed once, even if more than one attribute or component of the node exists in the set.
        - ordered (o): When querying set members return them in the same order as they appear in the set.
        - renderable (r): This flag indicates that a special type of set should be created. This type of set (shadingEngine as opposed to objectSet) has certain restrictions on its membership in that it can only contain renderable elements such as lights and
            geometry. These sets are referred to as shading groups and are automatically connected to the "renderPartition" node when created (to ensure mutual exclusivity of the set's members with the other sets in the partition). This flag is for use
            in creation or query mode only. The default value is false which means a normal set is created.
        - size (s): Use the size flag to query the length of the set.
        - text (t): Defines an annotation string to be stored with the set.
        - vertices (v): Indicates the new set can contain vertices only. This flag is for use in creation or query mode only. The default value is false.
        - query (q): Query mode flag
    """
@overload #Overload for sets in ['query']
def sets(selectionList: selectionList, channelSetColor: [float, float, float] = ..., csc: [float, float, float] = ..., channelSetColorIndex: int = ..., coi: int = ..., color: int = ..., co: int = ..., edges: bool = ..., eg: bool = ..., editPoints: bool = ..., ep: bool = ..., facets: bool = ..., fc: bool = ..., noIntermediate: bool = ..., ni: bool = ..., nodesOnly: bool = ..., no: bool = ..., ordered: bool = ..., o: bool = ..., renderable: bool = ..., r: bool = ..., size: bool = ..., s: bool = ..., text: str = ..., t: str = ..., vertices: bool = ..., v: bool = ..., query: bool = ..., q: bool = ...) -> str | list[str] | bool:
    """sets is undoable, queryable, and editable.
    
    This command is used to create a set, query some state of a set, or perform
    operations to update the membership of a set. A set is a logical grouping of
    an arbitrary collection of objects, attributes, or components of objects. Sets
    are dependency nodes. Connections from objects to a set define membership in
    the set.
    
    Sets are used throughout Maya in a multitude of ways. They are used to define
    an association of material properties to objects, to define an association of
    lights to objects, to define a bookmark or named collection of objects, to
    define a character, and to define the components to be deformed by some
    deformation operation.
    
    Sets can be connected to any number of partitions. A partition is a node which
    enforces mutual exclusivity amoung the sets in the partition. That is, if an
    object is in a set which is in a partition, that object cannot be a member of
    any other set that is in the partition.
    
    Without any flags, the sets command will create a set with a default name of
    "set#" (where # is an integer). If no items are specified on the command line,
    the currently selected items are added to the set. The -em/empty flag can be
    used to create an empty set and not have the selected items added to the set.
    
    Sets can be created to have certain restrictions on membership. There can be
    "renderable" sets which only allow renderable objects (such as nurbs geometry
    or polymesh faces) to be members of the set. There can also be vertex (or
    control point), edit point, edge, or face sets which only allow those types of
    components to be members of a set. Note that for these sets, if an object with
    a valid type of component is to be added to a set, the components of the
    object are added to the set instead.
    
    Sets can have an associated color which is only of use when creating vertex
    sets. The color can be one of the eight user defined colors defined in the
    color preferences. This color can be used, for example to distinguish which
    vertices are being deformed by a particular deformation.
    
    Objects, components, or attributes can be added to a set using one of three
    flags. The -add/addElement flag will add the objects to a set as long as this
    won't break any mutual exclusivity constraints. If there are any items which
    can't be added, the command will fail. The -in/include flag will only add
    those items which can be added and warn of those which can't. The
    -fe/forceElement flag will add all the items to the set but will also remove
    any of those items that are in any other set which is in the same partition as
    the set.
    
    There are several operations on sets that can be performed with the sets
    command. Membership can be queried. Tests for whether an item is in a set or
    whether two sets share the same item can be performed. Also, the union,
    intersection and difference of sets can be performed which returns a list of
    members of the sets which are a result of the operation.

    Example:
    ```python
        import maya.cmds as cmds
        # create some objects
        cmds.sphere( n="sphere1" )
        cmds.cone( n="cone1" )
        # create a set with whatever is currently active
        cmds.select( 'sphere1' )
        newSet1 = cmds.sets()
        cmds.select( 'cone1' )
        newSet2 = cmds.sets()
        # Query the members of a set
        cmds.sets( newSet1, q=True )
        # create a set which contains two sets
        cmds.sets( newSet1, newSet2, n="setOfSets" )
        # To select a set, the -noExpand flag must be used. Otherwise
        # the members of a set are selected instead.
        cmds.select( newSet1, noExpand=True )
        cmds.ls( selection=True )
        # Select the members of a set
        cmds.select( newSet1 )
        cmds.ls( selection=True )
        # Create a vertex set named ballVertices. This will contain
        # all the vertices of the sphere.
        cmds.sets( 'sphere1', n="ballVertices", v=1 )
        cmds.select( 'ballVertices' )
        # Return the union of two sets
        cmds.sets( newSet2, un=newSet1 )
        # Test whether a list of sets have common members
        cmds.sets( 'ballVertices',ii=newSet1)
        # Test whether the sphere is a member of the set
        cmds.sets('sphere1',im=newSet1)
        # Remove the sphere from a set
        cmds.sets( 'sphere1', rm=newSet1 )
        # Test again whether the sphere is a member of the set
        cmds.sets( 'sphere1', im=newSet1 )
    ```

    ---
    - Args:
        - selectionList: Input item(s).
        - channelSetColor (csc): Defines the custom color for the channel set to be shown in the dope sheet. This custom color is used when the channelSetColorIndex is -1.
        - channelSetColorIndex (coi): Defines the index for the color used to show the channel set in the dope sheet. The color is assigned by the UI using the index to cycle through the available colors. A special case is if the index is == -1, then the channelSetColor RGB
            values define the color.
        - color (co): Defines the hilite color of the set. Must be a value in range [-1, 7] (one of the user defined colors).  -1 marks the color has being undefined and therefore not having any affect. Only the vertices of a vertex set will be displayed in this
            color.
        - edges (eg): Indicates the new set can contain edges only. This flag is for use in creation or query mode only. The default value is false.
        - editPoints (ep): Indicates the new set can contain editPoints only. This flag is for use in creation or query mode only. The default value is false.
        - facets (fc): Indicates the new set can contain facets only. This flag is for use in creation or query mode only. The default value is false.
        - noIntermediate (ni): Excludes intermediate objects when querying set members or using the subtract, union, itersection, or isIntersecting flags.
        - nodesOnly (no): This flag is usable with the -q/query flag but is ignored if used with another queryable flags. This flag modifies the results of the set membership query such that when there are attributes (e.g. sphere1.tx) or components of nodes included
            in the set, only the nodes will be listed. Each node will only be listed once, even if more than one attribute or component of the node exists in the set.
        - ordered (o): When querying set members return them in the same order as they appear in the set.
        - renderable (r): This flag indicates that a special type of set should be created. This type of set (shadingEngine as opposed to objectSet) has certain restrictions on its membership in that it can only contain renderable elements such as lights and
            geometry. These sets are referred to as shading groups and are automatically connected to the "renderPartition" node when created (to ensure mutual exclusivity of the set's members with the other sets in the partition). This flag is for use
            in creation or query mode only. The default value is false which means a normal set is created.
        - size (s): Use the size flag to query the length of the set.
        - text (t): Defines an annotation string to be stored with the set.
        - vertices (v): Indicates the new set can contain vertices only. This flag is for use in creation or query mode only. The default value is false.
        - query (q): Query mode flag
    """
@overload #Overload for sets in ['edit']
def sets(selectionList: selectionList, addElement: name = ..., afterFilters: bool = ..., channelSetColor: [float, float, float] = ..., channelSetColorIndex: int = ..., clear: name = ..., color: int = ..., flatten: name = ..., forceElement: name = ..., include: name = ..., remove: name = ..., text: str = ..., edit: bool = ...) -> str | list[str] | bool:
    """sets is undoable, queryable, and editable.
    
    This command is used to create a set, query some state of a set, or perform
    operations to update the membership of a set. A set is a logical grouping of
    an arbitrary collection of objects, attributes, or components of objects. Sets
    are dependency nodes. Connections from objects to a set define membership in
    the set.
    
    Sets are used throughout Maya in a multitude of ways. They are used to define
    an association of material properties to objects, to define an association of
    lights to objects, to define a bookmark or named collection of objects, to
    define a character, and to define the components to be deformed by some
    deformation operation.
    
    Sets can be connected to any number of partitions. A partition is a node which
    enforces mutual exclusivity amoung the sets in the partition. That is, if an
    object is in a set which is in a partition, that object cannot be a member of
    any other set that is in the partition.
    
    Without any flags, the sets command will create a set with a default name of
    "set#" (where # is an integer). If no items are specified on the command line,
    the currently selected items are added to the set. The -em/empty flag can be
    used to create an empty set and not have the selected items added to the set.
    
    Sets can be created to have certain restrictions on membership. There can be
    "renderable" sets which only allow renderable objects (such as nurbs geometry
    or polymesh faces) to be members of the set. There can also be vertex (or
    control point), edit point, edge, or face sets which only allow those types of
    components to be members of a set. Note that for these sets, if an object with
    a valid type of component is to be added to a set, the components of the
    object are added to the set instead.
    
    Sets can have an associated color which is only of use when creating vertex
    sets. The color can be one of the eight user defined colors defined in the
    color preferences. This color can be used, for example to distinguish which
    vertices are being deformed by a particular deformation.
    
    Objects, components, or attributes can be added to a set using one of three
    flags. The -add/addElement flag will add the objects to a set as long as this
    won't break any mutual exclusivity constraints. If there are any items which
    can't be added, the command will fail. The -in/include flag will only add
    those items which can be added and warn of those which can't. The
    -fe/forceElement flag will add all the items to the set but will also remove
    any of those items that are in any other set which is in the same partition as
    the set.
    
    There are several operations on sets that can be performed with the sets
    command. Membership can be queried. Tests for whether an item is in a set or
    whether two sets share the same item can be performed. Also, the union,
    intersection and difference of sets can be performed which returns a list of
    members of the sets which are a result of the operation.

    Example:
    ```python
        import maya.cmds as cmds
        # create some objects
        cmds.sphere( n="sphere1" )
        cmds.cone( n="cone1" )
        # create a set with whatever is currently active
        cmds.select( 'sphere1' )
        newSet1 = cmds.sets()
        cmds.select( 'cone1' )
        newSet2 = cmds.sets()
        # Query the members of a set
        cmds.sets( newSet1, q=True )
        # create a set which contains two sets
        cmds.sets( newSet1, newSet2, n="setOfSets" )
        # To select a set, the -noExpand flag must be used. Otherwise
        # the members of a set are selected instead.
        cmds.select( newSet1, noExpand=True )
        cmds.ls( selection=True )
        # Select the members of a set
        cmds.select( newSet1 )
        cmds.ls( selection=True )
        # Create a vertex set named ballVertices. This will contain
        # all the vertices of the sphere.
        cmds.sets( 'sphere1', n="ballVertices", v=1 )
        cmds.select( 'ballVertices' )
        # Return the union of two sets
        cmds.sets( newSet2, un=newSet1 )
        # Test whether a list of sets have common members
        cmds.sets( 'ballVertices',ii=newSet1)
        # Test whether the sphere is a member of the set
        cmds.sets('sphere1',im=newSet1)
        # Remove the sphere from a set
        cmds.sets( 'sphere1', rm=newSet1 )
        # Test again whether the sphere is a member of the set
        cmds.sets( 'sphere1', im=newSet1 )
    ```

    ---
    - Args:
        - selectionList: Input item(s).
        - addElement (add): Adds the list of items to the given set.  If some of the items cannot be added to the set because they are in another set which is in the same partition as the set to edit, the command will fail.
        - afterFilters (af): Default state is false. This flag is valid in edit mode only. This flag is for use on sets that are acted on by deformers such as sculpt, lattice, blendShape. The default edit mode is to edit the membership of the group acted on by the
            deformer. If you want to edit the group but not change the membership of the deformer, set the flag to true.
        - channelSetColor (csc): Defines the custom color for the channel set to be shown in the dope sheet. This custom color is used when the channelSetColorIndex is -1.
        - channelSetColorIndex (coi): Defines the index for the color used to show the channel set in the dope sheet. The color is assigned by the UI using the index to cycle through the available colors. A special case is if the index is == -1, then the channelSetColor RGB
            values define the color.
        - clear (cl): An operation which removes all items from the given set making the set empty.
        - color (co): Defines the hilite color of the set. Must be a value in range [-1, 7] (one of the user defined colors).  -1 marks the color has being undefined and therefore not having any affect. Only the vertices of a vertex set will be displayed in this
            color.
        - flatten (fl): An operation that flattens the structure of the given set. That is, any sets contained by the given set will be replaced by its members so that the set no longer contains other sets but contains the other sets' members.
        - forceElement (fe): For use in edit mode only. Forces addition of the items to the set. If the items are in another set which is in the same partition as the given set, the items will be removed from the other set in order to keep the sets in the partition
            mutually exclusive with respect to membership.
        - include: Adds the list of items to the given set.  If some of the items cannot be added to the set, a warning will be issued. This is a less strict version of the -add/addElement operation.
        - remove (rm): Removes the list of items from the given set.
        - text (t): Defines an annotation string to be stored with the set.
        - edit (e): Edit mode flag
    """
@overload #Overload for sets in ['edit']
def sets(selectionList: selectionList, add: name = ..., af: bool = ..., csc: [float, float, float] = ..., coi: int = ..., cl: name = ..., co: int = ..., fl: name = ..., fe: name = ..., rm: name = ..., t: str = ..., e: bool = ...) -> str | list[str] | bool:
    """sets is undoable, queryable, and editable.
    
    This command is used to create a set, query some state of a set, or perform
    operations to update the membership of a set. A set is a logical grouping of
    an arbitrary collection of objects, attributes, or components of objects. Sets
    are dependency nodes. Connections from objects to a set define membership in
    the set.
    
    Sets are used throughout Maya in a multitude of ways. They are used to define
    an association of material properties to objects, to define an association of
    lights to objects, to define a bookmark or named collection of objects, to
    define a character, and to define the components to be deformed by some
    deformation operation.
    
    Sets can be connected to any number of partitions. A partition is a node which
    enforces mutual exclusivity amoung the sets in the partition. That is, if an
    object is in a set which is in a partition, that object cannot be a member of
    any other set that is in the partition.
    
    Without any flags, the sets command will create a set with a default name of
    "set#" (where # is an integer). If no items are specified on the command line,
    the currently selected items are added to the set. The -em/empty flag can be
    used to create an empty set and not have the selected items added to the set.
    
    Sets can be created to have certain restrictions on membership. There can be
    "renderable" sets which only allow renderable objects (such as nurbs geometry
    or polymesh faces) to be members of the set. There can also be vertex (or
    control point), edit point, edge, or face sets which only allow those types of
    components to be members of a set. Note that for these sets, if an object with
    a valid type of component is to be added to a set, the components of the
    object are added to the set instead.
    
    Sets can have an associated color which is only of use when creating vertex
    sets. The color can be one of the eight user defined colors defined in the
    color preferences. This color can be used, for example to distinguish which
    vertices are being deformed by a particular deformation.
    
    Objects, components, or attributes can be added to a set using one of three
    flags. The -add/addElement flag will add the objects to a set as long as this
    won't break any mutual exclusivity constraints. If there are any items which
    can't be added, the command will fail. The -in/include flag will only add
    those items which can be added and warn of those which can't. The
    -fe/forceElement flag will add all the items to the set but will also remove
    any of those items that are in any other set which is in the same partition as
    the set.
    
    There are several operations on sets that can be performed with the sets
    command. Membership can be queried. Tests for whether an item is in a set or
    whether two sets share the same item can be performed. Also, the union,
    intersection and difference of sets can be performed which returns a list of
    members of the sets which are a result of the operation.

    Example:
    ```python
        import maya.cmds as cmds
        # create some objects
        cmds.sphere( n="sphere1" )
        cmds.cone( n="cone1" )
        # create a set with whatever is currently active
        cmds.select( 'sphere1' )
        newSet1 = cmds.sets()
        cmds.select( 'cone1' )
        newSet2 = cmds.sets()
        # Query the members of a set
        cmds.sets( newSet1, q=True )
        # create a set which contains two sets
        cmds.sets( newSet1, newSet2, n="setOfSets" )
        # To select a set, the -noExpand flag must be used. Otherwise
        # the members of a set are selected instead.
        cmds.select( newSet1, noExpand=True )
        cmds.ls( selection=True )
        # Select the members of a set
        cmds.select( newSet1 )
        cmds.ls( selection=True )
        # Create a vertex set named ballVertices. This will contain
        # all the vertices of the sphere.
        cmds.sets( 'sphere1', n="ballVertices", v=1 )
        cmds.select( 'ballVertices' )
        # Return the union of two sets
        cmds.sets( newSet2, un=newSet1 )
        # Test whether a list of sets have common members
        cmds.sets( 'ballVertices',ii=newSet1)
        # Test whether the sphere is a member of the set
        cmds.sets('sphere1',im=newSet1)
        # Remove the sphere from a set
        cmds.sets( 'sphere1', rm=newSet1 )
        # Test again whether the sphere is a member of the set
        cmds.sets( 'sphere1', im=newSet1 )
    ```

    ---
    - Args:
        - selectionList: Input item(s).
        - addElement (add): Adds the list of items to the given set.  If some of the items cannot be added to the set because they are in another set which is in the same partition as the set to edit, the command will fail.
        - afterFilters (af): Default state is false. This flag is valid in edit mode only. This flag is for use on sets that are acted on by deformers such as sculpt, lattice, blendShape. The default edit mode is to edit the membership of the group acted on by the
            deformer. If you want to edit the group but not change the membership of the deformer, set the flag to true.
        - channelSetColor (csc): Defines the custom color for the channel set to be shown in the dope sheet. This custom color is used when the channelSetColorIndex is -1.
        - channelSetColorIndex (coi): Defines the index for the color used to show the channel set in the dope sheet. The color is assigned by the UI using the index to cycle through the available colors. A special case is if the index is == -1, then the channelSetColor RGB
            values define the color.
        - clear (cl): An operation which removes all items from the given set making the set empty.
        - color (co): Defines the hilite color of the set. Must be a value in range [-1, 7] (one of the user defined colors).  -1 marks the color has being undefined and therefore not having any affect. Only the vertices of a vertex set will be displayed in this
            color.
        - flatten (fl): An operation that flattens the structure of the given set. That is, any sets contained by the given set will be replaced by its members so that the set no longer contains other sets but contains the other sets' members.
        - forceElement (fe): For use in edit mode only. Forces addition of the items to the set. If the items are in another set which is in the same partition as the given set, the items will be removed from the other set in order to keep the sets in the partition
            mutually exclusive with respect to membership.
        - include: Adds the list of items to the given set.  If some of the items cannot be added to the set, a warning will be issued. This is a less strict version of the -add/addElement operation.
        - remove (rm): Removes the list of items from the given set.
        - text (t): Defines an annotation string to be stored with the set.
        - edit (e): Edit mode flag
    """
@overload #Overload for sets in ['edit']
def sets(selectionList: selectionList, addElement: name = ..., add: name = ..., afterFilters: bool = ..., af: bool = ..., channelSetColor: [float, float, float] = ..., csc: [float, float, float] = ..., channelSetColorIndex: int = ..., coi: int = ..., clear: name = ..., cl: name = ..., color: int = ..., co: int = ..., flatten: name = ..., fl: name = ..., forceElement: name = ..., fe: name = ..., include: name = ..., remove: name = ..., rm: name = ..., text: str = ..., t: str = ..., edit: bool = ..., e: bool = ...) -> str | list[str] | bool:
    """sets is undoable, queryable, and editable.
    
    This command is used to create a set, query some state of a set, or perform
    operations to update the membership of a set. A set is a logical grouping of
    an arbitrary collection of objects, attributes, or components of objects. Sets
    are dependency nodes. Connections from objects to a set define membership in
    the set.
    
    Sets are used throughout Maya in a multitude of ways. They are used to define
    an association of material properties to objects, to define an association of
    lights to objects, to define a bookmark or named collection of objects, to
    define a character, and to define the components to be deformed by some
    deformation operation.
    
    Sets can be connected to any number of partitions. A partition is a node which
    enforces mutual exclusivity amoung the sets in the partition. That is, if an
    object is in a set which is in a partition, that object cannot be a member of
    any other set that is in the partition.
    
    Without any flags, the sets command will create a set with a default name of
    "set#" (where # is an integer). If no items are specified on the command line,
    the currently selected items are added to the set. The -em/empty flag can be
    used to create an empty set and not have the selected items added to the set.
    
    Sets can be created to have certain restrictions on membership. There can be
    "renderable" sets which only allow renderable objects (such as nurbs geometry
    or polymesh faces) to be members of the set. There can also be vertex (or
    control point), edit point, edge, or face sets which only allow those types of
    components to be members of a set. Note that for these sets, if an object with
    a valid type of component is to be added to a set, the components of the
    object are added to the set instead.
    
    Sets can have an associated color which is only of use when creating vertex
    sets. The color can be one of the eight user defined colors defined in the
    color preferences. This color can be used, for example to distinguish which
    vertices are being deformed by a particular deformation.
    
    Objects, components, or attributes can be added to a set using one of three
    flags. The -add/addElement flag will add the objects to a set as long as this
    won't break any mutual exclusivity constraints. If there are any items which
    can't be added, the command will fail. The -in/include flag will only add
    those items which can be added and warn of those which can't. The
    -fe/forceElement flag will add all the items to the set but will also remove
    any of those items that are in any other set which is in the same partition as
    the set.
    
    There are several operations on sets that can be performed with the sets
    command. Membership can be queried. Tests for whether an item is in a set or
    whether two sets share the same item can be performed. Also, the union,
    intersection and difference of sets can be performed which returns a list of
    members of the sets which are a result of the operation.

    Example:
    ```python
        import maya.cmds as cmds
        # create some objects
        cmds.sphere( n="sphere1" )
        cmds.cone( n="cone1" )
        # create a set with whatever is currently active
        cmds.select( 'sphere1' )
        newSet1 = cmds.sets()
        cmds.select( 'cone1' )
        newSet2 = cmds.sets()
        # Query the members of a set
        cmds.sets( newSet1, q=True )
        # create a set which contains two sets
        cmds.sets( newSet1, newSet2, n="setOfSets" )
        # To select a set, the -noExpand flag must be used. Otherwise
        # the members of a set are selected instead.
        cmds.select( newSet1, noExpand=True )
        cmds.ls( selection=True )
        # Select the members of a set
        cmds.select( newSet1 )
        cmds.ls( selection=True )
        # Create a vertex set named ballVertices. This will contain
        # all the vertices of the sphere.
        cmds.sets( 'sphere1', n="ballVertices", v=1 )
        cmds.select( 'ballVertices' )
        # Return the union of two sets
        cmds.sets( newSet2, un=newSet1 )
        # Test whether a list of sets have common members
        cmds.sets( 'ballVertices',ii=newSet1)
        # Test whether the sphere is a member of the set
        cmds.sets('sphere1',im=newSet1)
        # Remove the sphere from a set
        cmds.sets( 'sphere1', rm=newSet1 )
        # Test again whether the sphere is a member of the set
        cmds.sets( 'sphere1', im=newSet1 )
    ```

    ---
    - Args:
        - selectionList: Input item(s).
        - addElement (add): Adds the list of items to the given set.  If some of the items cannot be added to the set because they are in another set which is in the same partition as the set to edit, the command will fail.
        - afterFilters (af): Default state is false. This flag is valid in edit mode only. This flag is for use on sets that are acted on by deformers such as sculpt, lattice, blendShape. The default edit mode is to edit the membership of the group acted on by the
            deformer. If you want to edit the group but not change the membership of the deformer, set the flag to true.
        - channelSetColor (csc): Defines the custom color for the channel set to be shown in the dope sheet. This custom color is used when the channelSetColorIndex is -1.
        - channelSetColorIndex (coi): Defines the index for the color used to show the channel set in the dope sheet. The color is assigned by the UI using the index to cycle through the available colors. A special case is if the index is == -1, then the channelSetColor RGB
            values define the color.
        - clear (cl): An operation which removes all items from the given set making the set empty.
        - color (co): Defines the hilite color of the set. Must be a value in range [-1, 7] (one of the user defined colors).  -1 marks the color has being undefined and therefore not having any affect. Only the vertices of a vertex set will be displayed in this
            color.
        - flatten (fl): An operation that flattens the structure of the given set. That is, any sets contained by the given set will be replaced by its members so that the set no longer contains other sets but contains the other sets' members.
        - forceElement (fe): For use in edit mode only. Forces addition of the items to the set. If the items are in another set which is in the same partition as the given set, the items will be removed from the other set in order to keep the sets in the partition
            mutually exclusive with respect to membership.
        - include: Adds the list of items to the given set.  If some of the items cannot be added to the set, a warning will be issued. This is a less strict version of the -add/addElement operation.
        - remove (rm): Removes the list of items from the given set.
        - text (t): Defines an annotation string to be stored with the set.
        - edit (e): Edit mode flag
    """
