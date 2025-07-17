"""Stub files for General category in Maya commands, command: assembly."""

from typing import Any, overload

@overload #Overload for assembly in ['create']
def assembly(name: str = ..., type: str = ...) -> None:
    """assembly is undoable, queryable, and editable.
    
    Command to register assemblies for the scene assembly framework, to create
    them, and to edit and query them. Assembly nodes are DAG nodes, and are
    therefore shown in the various DAG editors (Outliner, Hypergraph, Node
    Editor). At assembly creation time, the node name defaults to the node type
    name. The assembly command can create any node that is derived from the
    assembly node base class. It also acts as a registry of these types, so that
    various scripting callbacks can be defined and registered with the assembly
    command. These callbacks are invoked by Maya during operations on assembly
    nodes, and can be used to customize behavior.
    
    ## Registering a new assembly type
    
    When defining a new type of assembly derived from the assembly node base
    class, a number of procedures can be defined through the assembly command to
    properly integrate the new assembly node type into Maya. Most of these
    procedures are used to integrate the assembly type with the Maya user
    interface, and are not required for non-interactive scripting use. For more
    information, see the MPxAssembly class description in the Maya API
    documentation. Some of the important procedures that can be registered through
    the assembly command are the following:
    
    listRepTypesProc
    
    Procedure to list the representation types that the new assembly type can create. This allows Maya to query representation types that can be created by an assembly without actually creating an assembly node.
    repTypeLabelProc
    
    Procedure to return a (possibly localized) label which is shown in the user interface for the representation types the assembly can create. The label should be a short, user-friendly, readable description of the representation type.
    createOptionBoxProc
    
    Procedure to populate an option box for creation options for the assembly type. If defined, this procedure will populate an option box that is available for creation of that assembly's type.
    repPreCreateUIProc
    
    Procedure to provide a dialog before representation creation. If defined, will be invoked by Maya so that the user can interactively make choices before the creation of a type of representation for the assembly.
    postCreateUIProc
    
    Procedure to provide a dialog after assembly creation. If defined, will be invoked by Maya so that the user can interactively make choices and apply them to the assembly after its creation.

    Example:
    ```python
        import maya.cmds as cmds
        #Create a default type of assembly and name it MyAssembly.
        #The assembly name is optional.
        #
        cmds.assembly(name='MyAssembly')
        #Create an assembly of type MyAssemblyType and name it MyAssembly.
        #
        cmds.assembly(name='MyAssembly', type='MyAssemblyType')
        #Set the default type to be MyAssemblyType.
        #
        cmds.assembly(edit=True, defaultType='MyAssemblyType')
        #Create a representation of type "MyRepType", on assembly myAssembly, and
        #name it "MyRepName"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='MyRepType',
        repName='MyRepName')
        #Rename representation "MyRepName" to "MyNewRepName" on assembly myAssembly.
        #
        cmds.assembly(myAssembly, edit=True, renameRepresentation='MyRepName',
        repName='MyNewRepName')
        #Create a representation of type "Locator", on assembly myAssembly, name it
        #"myLocator", and add an annotation using the input flag.
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Locator',
        repName="myLocator", input="An Annotation")
        #Create a representation of type "Scene", on assembly myAssembly,
        #using file "/path/to/mayafile.mb"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Scene',
        input="/path/to/mayafile.mb")
        #Delete scene representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="mayafile.mb")
        #Delete locator representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="myLocator")
        #Set the procedure that provides the representation type label for
        #an assembly type.
        #
        cmds.assembly(edit=True, repTypeLabelProc='MyRepTypeLabelQuery', type='MyAssembly')
        #Set the label for the default assembly type.
        #
        cmds.assembly(edit=True, label='My Assembly Type')
        #Set the procedure that provides the representation type list which the
        #default assembly supports.
        #
        cmds.assembly(edit=True, listRepTypesProc='MyRepTypesProc')
        #Set the pre-create UI procedure for a representation type, for a
        #specific type of assembly.
        #
        cmds.assembly(edit=True, repPreCreateUIProc='MyRepresentation', proc='MyPreCreateProcedure', type='MyAssembly')
        #Set the post-create UI procedure for a representation type, for the
        #default assembly type.
        #
        cmds.assembly(edit=True, repPostCreateUIProc='MyRepresentation', proc='MyPostCreateProcedure' )
    ```

    ---
    - Args:
        - name (n): Specify the name of the assembly when creating it.
        - type (typ): Set or query properties for the specified registered assembly type.In query mode, this flag needs a value.
    """
@overload #Overload for assembly in ['create']
def assembly(n: str = ..., typ: str = ...) -> None:
    """assembly is undoable, queryable, and editable.
    
    Command to register assemblies for the scene assembly framework, to create
    them, and to edit and query them. Assembly nodes are DAG nodes, and are
    therefore shown in the various DAG editors (Outliner, Hypergraph, Node
    Editor). At assembly creation time, the node name defaults to the node type
    name. The assembly command can create any node that is derived from the
    assembly node base class. It also acts as a registry of these types, so that
    various scripting callbacks can be defined and registered with the assembly
    command. These callbacks are invoked by Maya during operations on assembly
    nodes, and can be used to customize behavior.
    
    ## Registering a new assembly type
    
    When defining a new type of assembly derived from the assembly node base
    class, a number of procedures can be defined through the assembly command to
    properly integrate the new assembly node type into Maya. Most of these
    procedures are used to integrate the assembly type with the Maya user
    interface, and are not required for non-interactive scripting use. For more
    information, see the MPxAssembly class description in the Maya API
    documentation. Some of the important procedures that can be registered through
    the assembly command are the following:
    
    listRepTypesProc
    
    Procedure to list the representation types that the new assembly type can create. This allows Maya to query representation types that can be created by an assembly without actually creating an assembly node.
    repTypeLabelProc
    
    Procedure to return a (possibly localized) label which is shown in the user interface for the representation types the assembly can create. The label should be a short, user-friendly, readable description of the representation type.
    createOptionBoxProc
    
    Procedure to populate an option box for creation options for the assembly type. If defined, this procedure will populate an option box that is available for creation of that assembly's type.
    repPreCreateUIProc
    
    Procedure to provide a dialog before representation creation. If defined, will be invoked by Maya so that the user can interactively make choices before the creation of a type of representation for the assembly.
    postCreateUIProc
    
    Procedure to provide a dialog after assembly creation. If defined, will be invoked by Maya so that the user can interactively make choices and apply them to the assembly after its creation.

    Example:
    ```python
        import maya.cmds as cmds
        #Create a default type of assembly and name it MyAssembly.
        #The assembly name is optional.
        #
        cmds.assembly(name='MyAssembly')
        #Create an assembly of type MyAssemblyType and name it MyAssembly.
        #
        cmds.assembly(name='MyAssembly', type='MyAssemblyType')
        #Set the default type to be MyAssemblyType.
        #
        cmds.assembly(edit=True, defaultType='MyAssemblyType')
        #Create a representation of type "MyRepType", on assembly myAssembly, and
        #name it "MyRepName"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='MyRepType',
        repName='MyRepName')
        #Rename representation "MyRepName" to "MyNewRepName" on assembly myAssembly.
        #
        cmds.assembly(myAssembly, edit=True, renameRepresentation='MyRepName',
        repName='MyNewRepName')
        #Create a representation of type "Locator", on assembly myAssembly, name it
        #"myLocator", and add an annotation using the input flag.
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Locator',
        repName="myLocator", input="An Annotation")
        #Create a representation of type "Scene", on assembly myAssembly,
        #using file "/path/to/mayafile.mb"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Scene',
        input="/path/to/mayafile.mb")
        #Delete scene representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="mayafile.mb")
        #Delete locator representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="myLocator")
        #Set the procedure that provides the representation type label for
        #an assembly type.
        #
        cmds.assembly(edit=True, repTypeLabelProc='MyRepTypeLabelQuery', type='MyAssembly')
        #Set the label for the default assembly type.
        #
        cmds.assembly(edit=True, label='My Assembly Type')
        #Set the procedure that provides the representation type list which the
        #default assembly supports.
        #
        cmds.assembly(edit=True, listRepTypesProc='MyRepTypesProc')
        #Set the pre-create UI procedure for a representation type, for a
        #specific type of assembly.
        #
        cmds.assembly(edit=True, repPreCreateUIProc='MyRepresentation', proc='MyPreCreateProcedure', type='MyAssembly')
        #Set the post-create UI procedure for a representation type, for the
        #default assembly type.
        #
        cmds.assembly(edit=True, repPostCreateUIProc='MyRepresentation', proc='MyPostCreateProcedure' )
    ```

    ---
    - Args:
        - name (n): Specify the name of the assembly when creating it.
        - type (typ): Set or query properties for the specified registered assembly type.In query mode, this flag needs a value.
    """
@overload #Overload for assembly in ['create']
def assembly(name: str = ..., n: str = ..., type: str = ..., typ: str = ...) -> None:
    """assembly is undoable, queryable, and editable.
    
    Command to register assemblies for the scene assembly framework, to create
    them, and to edit and query them. Assembly nodes are DAG nodes, and are
    therefore shown in the various DAG editors (Outliner, Hypergraph, Node
    Editor). At assembly creation time, the node name defaults to the node type
    name. The assembly command can create any node that is derived from the
    assembly node base class. It also acts as a registry of these types, so that
    various scripting callbacks can be defined and registered with the assembly
    command. These callbacks are invoked by Maya during operations on assembly
    nodes, and can be used to customize behavior.
    
    ## Registering a new assembly type
    
    When defining a new type of assembly derived from the assembly node base
    class, a number of procedures can be defined through the assembly command to
    properly integrate the new assembly node type into Maya. Most of these
    procedures are used to integrate the assembly type with the Maya user
    interface, and are not required for non-interactive scripting use. For more
    information, see the MPxAssembly class description in the Maya API
    documentation. Some of the important procedures that can be registered through
    the assembly command are the following:
    
    listRepTypesProc
    
    Procedure to list the representation types that the new assembly type can create. This allows Maya to query representation types that can be created by an assembly without actually creating an assembly node.
    repTypeLabelProc
    
    Procedure to return a (possibly localized) label which is shown in the user interface for the representation types the assembly can create. The label should be a short, user-friendly, readable description of the representation type.
    createOptionBoxProc
    
    Procedure to populate an option box for creation options for the assembly type. If defined, this procedure will populate an option box that is available for creation of that assembly's type.
    repPreCreateUIProc
    
    Procedure to provide a dialog before representation creation. If defined, will be invoked by Maya so that the user can interactively make choices before the creation of a type of representation for the assembly.
    postCreateUIProc
    
    Procedure to provide a dialog after assembly creation. If defined, will be invoked by Maya so that the user can interactively make choices and apply them to the assembly after its creation.

    Example:
    ```python
        import maya.cmds as cmds
        #Create a default type of assembly and name it MyAssembly.
        #The assembly name is optional.
        #
        cmds.assembly(name='MyAssembly')
        #Create an assembly of type MyAssemblyType and name it MyAssembly.
        #
        cmds.assembly(name='MyAssembly', type='MyAssemblyType')
        #Set the default type to be MyAssemblyType.
        #
        cmds.assembly(edit=True, defaultType='MyAssemblyType')
        #Create a representation of type "MyRepType", on assembly myAssembly, and
        #name it "MyRepName"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='MyRepType',
        repName='MyRepName')
        #Rename representation "MyRepName" to "MyNewRepName" on assembly myAssembly.
        #
        cmds.assembly(myAssembly, edit=True, renameRepresentation='MyRepName',
        repName='MyNewRepName')
        #Create a representation of type "Locator", on assembly myAssembly, name it
        #"myLocator", and add an annotation using the input flag.
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Locator',
        repName="myLocator", input="An Annotation")
        #Create a representation of type "Scene", on assembly myAssembly,
        #using file "/path/to/mayafile.mb"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Scene',
        input="/path/to/mayafile.mb")
        #Delete scene representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="mayafile.mb")
        #Delete locator representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="myLocator")
        #Set the procedure that provides the representation type label for
        #an assembly type.
        #
        cmds.assembly(edit=True, repTypeLabelProc='MyRepTypeLabelQuery', type='MyAssembly')
        #Set the label for the default assembly type.
        #
        cmds.assembly(edit=True, label='My Assembly Type')
        #Set the procedure that provides the representation type list which the
        #default assembly supports.
        #
        cmds.assembly(edit=True, listRepTypesProc='MyRepTypesProc')
        #Set the pre-create UI procedure for a representation type, for a
        #specific type of assembly.
        #
        cmds.assembly(edit=True, repPreCreateUIProc='MyRepresentation', proc='MyPreCreateProcedure', type='MyAssembly')
        #Set the post-create UI procedure for a representation type, for the
        #default assembly type.
        #
        cmds.assembly(edit=True, repPostCreateUIProc='MyRepresentation', proc='MyPostCreateProcedure' )
    ```

    ---
    - Args:
        - name (n): Specify the name of the assembly when creating it.
        - type (typ): Set or query properties for the specified registered assembly type.In query mode, this flag needs a value.
    """
@overload #Overload for assembly in ['query']
def assembly(active: str = ..., activeLabel: str = ..., canCreate: str = ..., createOptionBoxProc: script = ..., defaultType: str = ..., isAType: str = ..., isTrackingMemberEdits: str = ..., label: str = ..., listRepTypes: bool = ..., listRepTypesProc: script = ..., listRepresentations: bool = ..., listTypes: bool = ..., postCreateUIProc: script = ..., repLabel: str = ..., repNamespace: str = ..., repPostCreateUIProc: str = ..., repPreCreateUIProc: str = ..., repType: str = ..., repTypeLabel: str = ..., repTypeLabelProc: script = ..., type: str = ..., query: bool = ...) -> None:
    """assembly is undoable, queryable, and editable.
    
    Command to register assemblies for the scene assembly framework, to create
    them, and to edit and query them. Assembly nodes are DAG nodes, and are
    therefore shown in the various DAG editors (Outliner, Hypergraph, Node
    Editor). At assembly creation time, the node name defaults to the node type
    name. The assembly command can create any node that is derived from the
    assembly node base class. It also acts as a registry of these types, so that
    various scripting callbacks can be defined and registered with the assembly
    command. These callbacks are invoked by Maya during operations on assembly
    nodes, and can be used to customize behavior.
    
    ## Registering a new assembly type
    
    When defining a new type of assembly derived from the assembly node base
    class, a number of procedures can be defined through the assembly command to
    properly integrate the new assembly node type into Maya. Most of these
    procedures are used to integrate the assembly type with the Maya user
    interface, and are not required for non-interactive scripting use. For more
    information, see the MPxAssembly class description in the Maya API
    documentation. Some of the important procedures that can be registered through
    the assembly command are the following:
    
    listRepTypesProc
    
    Procedure to list the representation types that the new assembly type can create. This allows Maya to query representation types that can be created by an assembly without actually creating an assembly node.
    repTypeLabelProc
    
    Procedure to return a (possibly localized) label which is shown in the user interface for the representation types the assembly can create. The label should be a short, user-friendly, readable description of the representation type.
    createOptionBoxProc
    
    Procedure to populate an option box for creation options for the assembly type. If defined, this procedure will populate an option box that is available for creation of that assembly's type.
    repPreCreateUIProc
    
    Procedure to provide a dialog before representation creation. If defined, will be invoked by Maya so that the user can interactively make choices before the creation of a type of representation for the assembly.
    postCreateUIProc
    
    Procedure to provide a dialog after assembly creation. If defined, will be invoked by Maya so that the user can interactively make choices and apply them to the assembly after its creation.

    Example:
    ```python
        import maya.cmds as cmds
        #Create a default type of assembly and name it MyAssembly.
        #The assembly name is optional.
        #
        cmds.assembly(name='MyAssembly')
        #Create an assembly of type MyAssemblyType and name it MyAssembly.
        #
        cmds.assembly(name='MyAssembly', type='MyAssemblyType')
        #Set the default type to be MyAssemblyType.
        #
        cmds.assembly(edit=True, defaultType='MyAssemblyType')
        #Create a representation of type "MyRepType", on assembly myAssembly, and
        #name it "MyRepName"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='MyRepType',
        repName='MyRepName')
        #Rename representation "MyRepName" to "MyNewRepName" on assembly myAssembly.
        #
        cmds.assembly(myAssembly, edit=True, renameRepresentation='MyRepName',
        repName='MyNewRepName')
        #Create a representation of type "Locator", on assembly myAssembly, name it
        #"myLocator", and add an annotation using the input flag.
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Locator',
        repName="myLocator", input="An Annotation")
        #Create a representation of type "Scene", on assembly myAssembly,
        #using file "/path/to/mayafile.mb"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Scene',
        input="/path/to/mayafile.mb")
        #Delete scene representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="mayafile.mb")
        #Delete locator representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="myLocator")
        #Set the procedure that provides the representation type label for
        #an assembly type.
        #
        cmds.assembly(edit=True, repTypeLabelProc='MyRepTypeLabelQuery', type='MyAssembly')
        #Set the label for the default assembly type.
        #
        cmds.assembly(edit=True, label='My Assembly Type')
        #Set the procedure that provides the representation type list which the
        #default assembly supports.
        #
        cmds.assembly(edit=True, listRepTypesProc='MyRepTypesProc')
        #Set the pre-create UI procedure for a representation type, for a
        #specific type of assembly.
        #
        cmds.assembly(edit=True, repPreCreateUIProc='MyRepresentation', proc='MyPreCreateProcedure', type='MyAssembly')
        #Set the post-create UI procedure for a representation type, for the
        #default assembly type.
        #
        cmds.assembly(edit=True, repPostCreateUIProc='MyRepresentation', proc='MyPostCreateProcedure' )
    ```

    ---
    - Args:
        - active (a): Set the active representation by name, or query the name of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an
            array of strings when multiple assemblies are specified. Using an empty string as name means to inactivate the currently active representation.
        - activeLabel (al): Set the active representation by label, or query the label of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an
            array of strings when multiple assemblies are specified.
        - canCreate (cc): Query the representation types the specific assembly can create.
        - createOptionBoxProc (cob): Set or query the option box menu procedure for a specific assembly type. The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - defaultType (dt): Set or query the default type of assembly.  When the assembly command is used to perform an operation on an assembly type rather than on an assembly object, it will be performed on the default type, unless the -type flag is used to specify
            an explicit assembly type.
        - isAType (isa): Query whether the given object is of an assembly type.
        - isTrackingMemberEdits (ite): Query whether the given object is tracking member edits.
        - label (lbl): Set or query the label for an assembly type. Assembly type is specified with flag "type". If no type specified, the default type is used.
        - listRepTypes (lrt): Query the supported representation types for a given assembly type.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - listRepTypesProc (lrp): Set or query the procedure that provides the representation type list which an assembly type supports.  This procedure takes no argument, and returns a string array of representation types that represents the full set of representation
            types this assembly type can create.  The assembly type for which this procedure applies will be the default type, unless the type flag is used to specify an explicit assembly type.
        - listRepresentations (lr): Query the created representations list for a specific assembly.  The -repType flag can be used to filter the list and return representations for a single representation type.  If the -repType flag is not used, all created representations
            will be returned.
        - listTypes (lt): Query the supported assembly types.
        - postCreateUIProc (aoc): Set or query the UI post-creation procedure for a given assembly type. This procedure will be invoked by Maya immediately after an assembly of the specified type is created from the UI, but not through scripting.  It can be used to invoke a
            dialog, to obtain and set initial parameters on a newly-created assembly.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - repLabel (rl): Query or edit the label of the representation that is the argument to this flag, for a given assembly.  In both query and edit modes, the -repLabel flag specifies the name of the representation.  In edit mode, the -newRepLabel flag must be
            used to specify the new representation label.In query mode, this flag needs a value.
        - repNamespace (rns): Query the representation namespace of this assembly node. The value returned is used by Maya for creating the namespace where nodes created by the activation of a representation will be added. If a name clash occurs when the namespace is
            added to its parent namespace, Maya will update repNamespace with the new name. Two namespaces are involved when dealing with an assembly node: the namespace of the assembly node itself (which this flag does not affect or query), and the
            namespace of its representations. The representation namespace is a child of its assembly node's namespace. The assembly node's namespace is set by its containing assembly, if it is nested, or by the top-level file. Either the assembly
            node's namespace, or the representation namespace, or both, can be the empty string. It should be noted that if the assembly node is nested, the assembly node's namespace will be (by virtue of its nesting) the representation namespace of
            its containing assembly.
        - repPostCreateUIProc (poc): Set or query the UI post-creation procedure for a specific representation type, and for a specific assembly type.  This procedure takes two arguments, the first the DAG path to the assembly, and the second the name of the representation.
            It returns no value.  It will be invoked by Maya immediately after a representation of the specified type is created from the UI, but not through scripting.  It can be used to invoke a dialog, to obtain and set initial parameters on a
            newly-created representation.  The representation type is the argument of this flag. The -proc flag must be used to specify the procedure name.  The assembly type will be the default type, unless the -type flag is used to specify an
            explicit assembly type.In query mode, this flag needs a value.
        - repPreCreateUIProc (pec): Set or query the UI pre-creation procedure for a specific representation type, and for a specific assembly type.  This procedure takes no argument, and returns a string that is passed as an argument to the -input flag when Maya invokes the
            assembly command with the -createRepresentation flag. The representation pre-creation procedure is invoked by Maya immediately before creating a representation of the specified type from the UI, but not through scripting.  It can be used to
            invoke a dialog, to obtain the creation argument for a new representation.  The representation type is the argument of this flag.  The -proc flag must be used to specify the procedure name.  The assembly type will be the default type,
            unless the -type flag is used to specify an explicit assembly type.In query mode, this flag needs a value.
        - repType (rt): Specify a representation type to use as a filter for the -listRepresentations query.  The representation type is the argument to this flag.In query mode, this flag needs a value.
        - repTypeLabel (rtl): Query the label of the specific representation type.In query mode, this flag needs a value.
        - repTypeLabelProc (rtp): Set or query the procedure that provides the representation type label, for a given assembly type.  The procedure takes the representation type as its sole argument, and returns a localized representation type label. The assembly type for
            which this procedure applies will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - type (typ): Set or query properties for the specified registered assembly type.In query mode, this flag needs a value.
        - query (q): Query mode flag
    """
@overload #Overload for assembly in ['query']
def assembly(a: str = ..., al: str = ..., cc: str = ..., cob: script = ..., dt: str = ..., isa: str = ..., ite: str = ..., lbl: str = ..., lrt: bool = ..., lrp: script = ..., lr: bool = ..., lt: bool = ..., aoc: script = ..., rl: str = ..., rns: str = ..., poc: str = ..., pec: str = ..., rt: str = ..., rtl: str = ..., rtp: script = ..., typ: str = ..., q: bool = ...) -> None:
    """assembly is undoable, queryable, and editable.
    
    Command to register assemblies for the scene assembly framework, to create
    them, and to edit and query them. Assembly nodes are DAG nodes, and are
    therefore shown in the various DAG editors (Outliner, Hypergraph, Node
    Editor). At assembly creation time, the node name defaults to the node type
    name. The assembly command can create any node that is derived from the
    assembly node base class. It also acts as a registry of these types, so that
    various scripting callbacks can be defined and registered with the assembly
    command. These callbacks are invoked by Maya during operations on assembly
    nodes, and can be used to customize behavior.
    
    ## Registering a new assembly type
    
    When defining a new type of assembly derived from the assembly node base
    class, a number of procedures can be defined through the assembly command to
    properly integrate the new assembly node type into Maya. Most of these
    procedures are used to integrate the assembly type with the Maya user
    interface, and are not required for non-interactive scripting use. For more
    information, see the MPxAssembly class description in the Maya API
    documentation. Some of the important procedures that can be registered through
    the assembly command are the following:
    
    listRepTypesProc
    
    Procedure to list the representation types that the new assembly type can create. This allows Maya to query representation types that can be created by an assembly without actually creating an assembly node.
    repTypeLabelProc
    
    Procedure to return a (possibly localized) label which is shown in the user interface for the representation types the assembly can create. The label should be a short, user-friendly, readable description of the representation type.
    createOptionBoxProc
    
    Procedure to populate an option box for creation options for the assembly type. If defined, this procedure will populate an option box that is available for creation of that assembly's type.
    repPreCreateUIProc
    
    Procedure to provide a dialog before representation creation. If defined, will be invoked by Maya so that the user can interactively make choices before the creation of a type of representation for the assembly.
    postCreateUIProc
    
    Procedure to provide a dialog after assembly creation. If defined, will be invoked by Maya so that the user can interactively make choices and apply them to the assembly after its creation.

    Example:
    ```python
        import maya.cmds as cmds
        #Create a default type of assembly and name it MyAssembly.
        #The assembly name is optional.
        #
        cmds.assembly(name='MyAssembly')
        #Create an assembly of type MyAssemblyType and name it MyAssembly.
        #
        cmds.assembly(name='MyAssembly', type='MyAssemblyType')
        #Set the default type to be MyAssemblyType.
        #
        cmds.assembly(edit=True, defaultType='MyAssemblyType')
        #Create a representation of type "MyRepType", on assembly myAssembly, and
        #name it "MyRepName"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='MyRepType',
        repName='MyRepName')
        #Rename representation "MyRepName" to "MyNewRepName" on assembly myAssembly.
        #
        cmds.assembly(myAssembly, edit=True, renameRepresentation='MyRepName',
        repName='MyNewRepName')
        #Create a representation of type "Locator", on assembly myAssembly, name it
        #"myLocator", and add an annotation using the input flag.
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Locator',
        repName="myLocator", input="An Annotation")
        #Create a representation of type "Scene", on assembly myAssembly,
        #using file "/path/to/mayafile.mb"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Scene',
        input="/path/to/mayafile.mb")
        #Delete scene representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="mayafile.mb")
        #Delete locator representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="myLocator")
        #Set the procedure that provides the representation type label for
        #an assembly type.
        #
        cmds.assembly(edit=True, repTypeLabelProc='MyRepTypeLabelQuery', type='MyAssembly')
        #Set the label for the default assembly type.
        #
        cmds.assembly(edit=True, label='My Assembly Type')
        #Set the procedure that provides the representation type list which the
        #default assembly supports.
        #
        cmds.assembly(edit=True, listRepTypesProc='MyRepTypesProc')
        #Set the pre-create UI procedure for a representation type, for a
        #specific type of assembly.
        #
        cmds.assembly(edit=True, repPreCreateUIProc='MyRepresentation', proc='MyPreCreateProcedure', type='MyAssembly')
        #Set the post-create UI procedure for a representation type, for the
        #default assembly type.
        #
        cmds.assembly(edit=True, repPostCreateUIProc='MyRepresentation', proc='MyPostCreateProcedure' )
    ```

    ---
    - Args:
        - active (a): Set the active representation by name, or query the name of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an
            array of strings when multiple assemblies are specified. Using an empty string as name means to inactivate the currently active representation.
        - activeLabel (al): Set the active representation by label, or query the label of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an
            array of strings when multiple assemblies are specified.
        - canCreate (cc): Query the representation types the specific assembly can create.
        - createOptionBoxProc (cob): Set or query the option box menu procedure for a specific assembly type. The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - defaultType (dt): Set or query the default type of assembly.  When the assembly command is used to perform an operation on an assembly type rather than on an assembly object, it will be performed on the default type, unless the -type flag is used to specify
            an explicit assembly type.
        - isAType (isa): Query whether the given object is of an assembly type.
        - isTrackingMemberEdits (ite): Query whether the given object is tracking member edits.
        - label (lbl): Set or query the label for an assembly type. Assembly type is specified with flag "type". If no type specified, the default type is used.
        - listRepTypes (lrt): Query the supported representation types for a given assembly type.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - listRepTypesProc (lrp): Set or query the procedure that provides the representation type list which an assembly type supports.  This procedure takes no argument, and returns a string array of representation types that represents the full set of representation
            types this assembly type can create.  The assembly type for which this procedure applies will be the default type, unless the type flag is used to specify an explicit assembly type.
        - listRepresentations (lr): Query the created representations list for a specific assembly.  The -repType flag can be used to filter the list and return representations for a single representation type.  If the -repType flag is not used, all created representations
            will be returned.
        - listTypes (lt): Query the supported assembly types.
        - postCreateUIProc (aoc): Set or query the UI post-creation procedure for a given assembly type. This procedure will be invoked by Maya immediately after an assembly of the specified type is created from the UI, but not through scripting.  It can be used to invoke a
            dialog, to obtain and set initial parameters on a newly-created assembly.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - repLabel (rl): Query or edit the label of the representation that is the argument to this flag, for a given assembly.  In both query and edit modes, the -repLabel flag specifies the name of the representation.  In edit mode, the -newRepLabel flag must be
            used to specify the new representation label.In query mode, this flag needs a value.
        - repNamespace (rns): Query the representation namespace of this assembly node. The value returned is used by Maya for creating the namespace where nodes created by the activation of a representation will be added. If a name clash occurs when the namespace is
            added to its parent namespace, Maya will update repNamespace with the new name. Two namespaces are involved when dealing with an assembly node: the namespace of the assembly node itself (which this flag does not affect or query), and the
            namespace of its representations. The representation namespace is a child of its assembly node's namespace. The assembly node's namespace is set by its containing assembly, if it is nested, or by the top-level file. Either the assembly
            node's namespace, or the representation namespace, or both, can be the empty string. It should be noted that if the assembly node is nested, the assembly node's namespace will be (by virtue of its nesting) the representation namespace of
            its containing assembly.
        - repPostCreateUIProc (poc): Set or query the UI post-creation procedure for a specific representation type, and for a specific assembly type.  This procedure takes two arguments, the first the DAG path to the assembly, and the second the name of the representation.
            It returns no value.  It will be invoked by Maya immediately after a representation of the specified type is created from the UI, but not through scripting.  It can be used to invoke a dialog, to obtain and set initial parameters on a
            newly-created representation.  The representation type is the argument of this flag. The -proc flag must be used to specify the procedure name.  The assembly type will be the default type, unless the -type flag is used to specify an
            explicit assembly type.In query mode, this flag needs a value.
        - repPreCreateUIProc (pec): Set or query the UI pre-creation procedure for a specific representation type, and for a specific assembly type.  This procedure takes no argument, and returns a string that is passed as an argument to the -input flag when Maya invokes the
            assembly command with the -createRepresentation flag. The representation pre-creation procedure is invoked by Maya immediately before creating a representation of the specified type from the UI, but not through scripting.  It can be used to
            invoke a dialog, to obtain the creation argument for a new representation.  The representation type is the argument of this flag.  The -proc flag must be used to specify the procedure name.  The assembly type will be the default type,
            unless the -type flag is used to specify an explicit assembly type.In query mode, this flag needs a value.
        - repType (rt): Specify a representation type to use as a filter for the -listRepresentations query.  The representation type is the argument to this flag.In query mode, this flag needs a value.
        - repTypeLabel (rtl): Query the label of the specific representation type.In query mode, this flag needs a value.
        - repTypeLabelProc (rtp): Set or query the procedure that provides the representation type label, for a given assembly type.  The procedure takes the representation type as its sole argument, and returns a localized representation type label. The assembly type for
            which this procedure applies will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - type (typ): Set or query properties for the specified registered assembly type.In query mode, this flag needs a value.
        - query (q): Query mode flag
    """
@overload #Overload for assembly in ['query']
def assembly(active: str = ..., a: str = ..., activeLabel: str = ..., al: str = ..., canCreate: str = ..., cc: str = ..., createOptionBoxProc: script = ..., cob: script = ..., defaultType: str = ..., dt: str = ..., isAType: str = ..., isa: str = ..., isTrackingMemberEdits: str = ..., ite: str = ..., label: str = ..., lbl: str = ..., listRepTypes: bool = ..., lrt: bool = ..., listRepTypesProc: script = ..., lrp: script = ..., listRepresentations: bool = ..., lr: bool = ..., listTypes: bool = ..., lt: bool = ..., postCreateUIProc: script = ..., aoc: script = ..., repLabel: str = ..., rl: str = ..., repNamespace: str = ..., rns: str = ..., repPostCreateUIProc: str = ..., poc: str = ..., repPreCreateUIProc: str = ..., pec: str = ..., repType: str = ..., rt: str = ..., repTypeLabel: str = ..., rtl: str = ..., repTypeLabelProc: script = ..., rtp: script = ..., type: str = ..., typ: str = ..., query: bool = ..., q: bool = ...) -> None:
    """assembly is undoable, queryable, and editable.
    
    Command to register assemblies for the scene assembly framework, to create
    them, and to edit and query them. Assembly nodes are DAG nodes, and are
    therefore shown in the various DAG editors (Outliner, Hypergraph, Node
    Editor). At assembly creation time, the node name defaults to the node type
    name. The assembly command can create any node that is derived from the
    assembly node base class. It also acts as a registry of these types, so that
    various scripting callbacks can be defined and registered with the assembly
    command. These callbacks are invoked by Maya during operations on assembly
    nodes, and can be used to customize behavior.
    
    ## Registering a new assembly type
    
    When defining a new type of assembly derived from the assembly node base
    class, a number of procedures can be defined through the assembly command to
    properly integrate the new assembly node type into Maya. Most of these
    procedures are used to integrate the assembly type with the Maya user
    interface, and are not required for non-interactive scripting use. For more
    information, see the MPxAssembly class description in the Maya API
    documentation. Some of the important procedures that can be registered through
    the assembly command are the following:
    
    listRepTypesProc
    
    Procedure to list the representation types that the new assembly type can create. This allows Maya to query representation types that can be created by an assembly without actually creating an assembly node.
    repTypeLabelProc
    
    Procedure to return a (possibly localized) label which is shown in the user interface for the representation types the assembly can create. The label should be a short, user-friendly, readable description of the representation type.
    createOptionBoxProc
    
    Procedure to populate an option box for creation options for the assembly type. If defined, this procedure will populate an option box that is available for creation of that assembly's type.
    repPreCreateUIProc
    
    Procedure to provide a dialog before representation creation. If defined, will be invoked by Maya so that the user can interactively make choices before the creation of a type of representation for the assembly.
    postCreateUIProc
    
    Procedure to provide a dialog after assembly creation. If defined, will be invoked by Maya so that the user can interactively make choices and apply them to the assembly after its creation.

    Example:
    ```python
        import maya.cmds as cmds
        #Create a default type of assembly and name it MyAssembly.
        #The assembly name is optional.
        #
        cmds.assembly(name='MyAssembly')
        #Create an assembly of type MyAssemblyType and name it MyAssembly.
        #
        cmds.assembly(name='MyAssembly', type='MyAssemblyType')
        #Set the default type to be MyAssemblyType.
        #
        cmds.assembly(edit=True, defaultType='MyAssemblyType')
        #Create a representation of type "MyRepType", on assembly myAssembly, and
        #name it "MyRepName"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='MyRepType',
        repName='MyRepName')
        #Rename representation "MyRepName" to "MyNewRepName" on assembly myAssembly.
        #
        cmds.assembly(myAssembly, edit=True, renameRepresentation='MyRepName',
        repName='MyNewRepName')
        #Create a representation of type "Locator", on assembly myAssembly, name it
        #"myLocator", and add an annotation using the input flag.
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Locator',
        repName="myLocator", input="An Annotation")
        #Create a representation of type "Scene", on assembly myAssembly,
        #using file "/path/to/mayafile.mb"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Scene',
        input="/path/to/mayafile.mb")
        #Delete scene representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="mayafile.mb")
        #Delete locator representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="myLocator")
        #Set the procedure that provides the representation type label for
        #an assembly type.
        #
        cmds.assembly(edit=True, repTypeLabelProc='MyRepTypeLabelQuery', type='MyAssembly')
        #Set the label for the default assembly type.
        #
        cmds.assembly(edit=True, label='My Assembly Type')
        #Set the procedure that provides the representation type list which the
        #default assembly supports.
        #
        cmds.assembly(edit=True, listRepTypesProc='MyRepTypesProc')
        #Set the pre-create UI procedure for a representation type, for a
        #specific type of assembly.
        #
        cmds.assembly(edit=True, repPreCreateUIProc='MyRepresentation', proc='MyPreCreateProcedure', type='MyAssembly')
        #Set the post-create UI procedure for a representation type, for the
        #default assembly type.
        #
        cmds.assembly(edit=True, repPostCreateUIProc='MyRepresentation', proc='MyPostCreateProcedure' )
    ```

    ---
    - Args:
        - active (a): Set the active representation by name, or query the name of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an
            array of strings when multiple assemblies are specified. Using an empty string as name means to inactivate the currently active representation.
        - activeLabel (al): Set the active representation by label, or query the label of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an
            array of strings when multiple assemblies are specified.
        - canCreate (cc): Query the representation types the specific assembly can create.
        - createOptionBoxProc (cob): Set or query the option box menu procedure for a specific assembly type. The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - defaultType (dt): Set or query the default type of assembly.  When the assembly command is used to perform an operation on an assembly type rather than on an assembly object, it will be performed on the default type, unless the -type flag is used to specify
            an explicit assembly type.
        - isAType (isa): Query whether the given object is of an assembly type.
        - isTrackingMemberEdits (ite): Query whether the given object is tracking member edits.
        - label (lbl): Set or query the label for an assembly type. Assembly type is specified with flag "type". If no type specified, the default type is used.
        - listRepTypes (lrt): Query the supported representation types for a given assembly type.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - listRepTypesProc (lrp): Set or query the procedure that provides the representation type list which an assembly type supports.  This procedure takes no argument, and returns a string array of representation types that represents the full set of representation
            types this assembly type can create.  The assembly type for which this procedure applies will be the default type, unless the type flag is used to specify an explicit assembly type.
        - listRepresentations (lr): Query the created representations list for a specific assembly.  The -repType flag can be used to filter the list and return representations for a single representation type.  If the -repType flag is not used, all created representations
            will be returned.
        - listTypes (lt): Query the supported assembly types.
        - postCreateUIProc (aoc): Set or query the UI post-creation procedure for a given assembly type. This procedure will be invoked by Maya immediately after an assembly of the specified type is created from the UI, but not through scripting.  It can be used to invoke a
            dialog, to obtain and set initial parameters on a newly-created assembly.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - repLabel (rl): Query or edit the label of the representation that is the argument to this flag, for a given assembly.  In both query and edit modes, the -repLabel flag specifies the name of the representation.  In edit mode, the -newRepLabel flag must be
            used to specify the new representation label.In query mode, this flag needs a value.
        - repNamespace (rns): Query the representation namespace of this assembly node. The value returned is used by Maya for creating the namespace where nodes created by the activation of a representation will be added. If a name clash occurs when the namespace is
            added to its parent namespace, Maya will update repNamespace with the new name. Two namespaces are involved when dealing with an assembly node: the namespace of the assembly node itself (which this flag does not affect or query), and the
            namespace of its representations. The representation namespace is a child of its assembly node's namespace. The assembly node's namespace is set by its containing assembly, if it is nested, or by the top-level file. Either the assembly
            node's namespace, or the representation namespace, or both, can be the empty string. It should be noted that if the assembly node is nested, the assembly node's namespace will be (by virtue of its nesting) the representation namespace of
            its containing assembly.
        - repPostCreateUIProc (poc): Set or query the UI post-creation procedure for a specific representation type, and for a specific assembly type.  This procedure takes two arguments, the first the DAG path to the assembly, and the second the name of the representation.
            It returns no value.  It will be invoked by Maya immediately after a representation of the specified type is created from the UI, but not through scripting.  It can be used to invoke a dialog, to obtain and set initial parameters on a
            newly-created representation.  The representation type is the argument of this flag. The -proc flag must be used to specify the procedure name.  The assembly type will be the default type, unless the -type flag is used to specify an
            explicit assembly type.In query mode, this flag needs a value.
        - repPreCreateUIProc (pec): Set or query the UI pre-creation procedure for a specific representation type, and for a specific assembly type.  This procedure takes no argument, and returns a string that is passed as an argument to the -input flag when Maya invokes the
            assembly command with the -createRepresentation flag. The representation pre-creation procedure is invoked by Maya immediately before creating a representation of the specified type from the UI, but not through scripting.  It can be used to
            invoke a dialog, to obtain the creation argument for a new representation.  The representation type is the argument of this flag.  The -proc flag must be used to specify the procedure name.  The assembly type will be the default type,
            unless the -type flag is used to specify an explicit assembly type.In query mode, this flag needs a value.
        - repType (rt): Specify a representation type to use as a filter for the -listRepresentations query.  The representation type is the argument to this flag.In query mode, this flag needs a value.
        - repTypeLabel (rtl): Query the label of the specific representation type.In query mode, this flag needs a value.
        - repTypeLabelProc (rtp): Set or query the procedure that provides the representation type label, for a given assembly type.  The procedure takes the representation type as its sole argument, and returns a localized representation type label. The assembly type for
            which this procedure applies will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - type (typ): Set or query properties for the specified registered assembly type.In query mode, this flag needs a value.
        - query (q): Query mode flag
    """
@overload #Overload for assembly in ['edit']
def assembly(active: str = ..., activeLabel: str = ..., createOptionBoxProc: script = ..., createRepresentation: str = ..., defaultType: str = ..., deleteRepresentation: str = ..., deregister: str = ..., input: str = ..., label: str = ..., listRepTypesProc: script = ..., newRepLabel: str = ..., postCreateUIProc: script = ..., proc: script = ..., renameRepresentation: str = ..., repLabel: str = ..., repName: str = ..., repPostCreateUIProc: str = ..., repPreCreateUIProc: str = ..., repTypeLabelProc: script = ..., type: str = ..., edit: bool = ...) -> None:
    """assembly is undoable, queryable, and editable.
    
    Command to register assemblies for the scene assembly framework, to create
    them, and to edit and query them. Assembly nodes are DAG nodes, and are
    therefore shown in the various DAG editors (Outliner, Hypergraph, Node
    Editor). At assembly creation time, the node name defaults to the node type
    name. The assembly command can create any node that is derived from the
    assembly node base class. It also acts as a registry of these types, so that
    various scripting callbacks can be defined and registered with the assembly
    command. These callbacks are invoked by Maya during operations on assembly
    nodes, and can be used to customize behavior.
    
    ## Registering a new assembly type
    
    When defining a new type of assembly derived from the assembly node base
    class, a number of procedures can be defined through the assembly command to
    properly integrate the new assembly node type into Maya. Most of these
    procedures are used to integrate the assembly type with the Maya user
    interface, and are not required for non-interactive scripting use. For more
    information, see the MPxAssembly class description in the Maya API
    documentation. Some of the important procedures that can be registered through
    the assembly command are the following:
    
    listRepTypesProc
    
    Procedure to list the representation types that the new assembly type can create. This allows Maya to query representation types that can be created by an assembly without actually creating an assembly node.
    repTypeLabelProc
    
    Procedure to return a (possibly localized) label which is shown in the user interface for the representation types the assembly can create. The label should be a short, user-friendly, readable description of the representation type.
    createOptionBoxProc
    
    Procedure to populate an option box for creation options for the assembly type. If defined, this procedure will populate an option box that is available for creation of that assembly's type.
    repPreCreateUIProc
    
    Procedure to provide a dialog before representation creation. If defined, will be invoked by Maya so that the user can interactively make choices before the creation of a type of representation for the assembly.
    postCreateUIProc
    
    Procedure to provide a dialog after assembly creation. If defined, will be invoked by Maya so that the user can interactively make choices and apply them to the assembly after its creation.

    Example:
    ```python
        import maya.cmds as cmds
        #Create a default type of assembly and name it MyAssembly.
        #The assembly name is optional.
        #
        cmds.assembly(name='MyAssembly')
        #Create an assembly of type MyAssemblyType and name it MyAssembly.
        #
        cmds.assembly(name='MyAssembly', type='MyAssemblyType')
        #Set the default type to be MyAssemblyType.
        #
        cmds.assembly(edit=True, defaultType='MyAssemblyType')
        #Create a representation of type "MyRepType", on assembly myAssembly, and
        #name it "MyRepName"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='MyRepType',
        repName='MyRepName')
        #Rename representation "MyRepName" to "MyNewRepName" on assembly myAssembly.
        #
        cmds.assembly(myAssembly, edit=True, renameRepresentation='MyRepName',
        repName='MyNewRepName')
        #Create a representation of type "Locator", on assembly myAssembly, name it
        #"myLocator", and add an annotation using the input flag.
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Locator',
        repName="myLocator", input="An Annotation")
        #Create a representation of type "Scene", on assembly myAssembly,
        #using file "/path/to/mayafile.mb"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Scene',
        input="/path/to/mayafile.mb")
        #Delete scene representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="mayafile.mb")
        #Delete locator representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="myLocator")
        #Set the procedure that provides the representation type label for
        #an assembly type.
        #
        cmds.assembly(edit=True, repTypeLabelProc='MyRepTypeLabelQuery', type='MyAssembly')
        #Set the label for the default assembly type.
        #
        cmds.assembly(edit=True, label='My Assembly Type')
        #Set the procedure that provides the representation type list which the
        #default assembly supports.
        #
        cmds.assembly(edit=True, listRepTypesProc='MyRepTypesProc')
        #Set the pre-create UI procedure for a representation type, for a
        #specific type of assembly.
        #
        cmds.assembly(edit=True, repPreCreateUIProc='MyRepresentation', proc='MyPreCreateProcedure', type='MyAssembly')
        #Set the post-create UI procedure for a representation type, for the
        #default assembly type.
        #
        cmds.assembly(edit=True, repPostCreateUIProc='MyRepresentation', proc='MyPostCreateProcedure' )
    ```

    ---
    - Args:
        - active (a): Set the active representation by name, or query the name of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an
            array of strings when multiple assemblies are specified. Using an empty string as name means to inactivate the currently active representation.
        - activeLabel (al): Set the active representation by label, or query the label of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an
            array of strings when multiple assemblies are specified.
        - createOptionBoxProc (cob): Set or query the option box menu procedure for a specific assembly type. The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - createRepresentation (cr): Create and add a specific type of representation for an assembly. If the representation type needs additional parameters, they must be specified using the "input" flag. For example, the Maya scene assembly reference implementation Cache and
            Scene representations need an input file.
        - defaultType (dt): Set or query the default type of assembly.  When the assembly command is used to perform an operation on an assembly type rather than on an assembly object, it will be performed on the default type, unless the -type flag is used to specify
            an explicit assembly type.
        - deleteRepresentation (dr): Delete a specific representation from an assembly.
        - deregister (d): Deregister a registered assembly type. If the deregistered type is the default type, the default type will be set to the empty string.
        - input: Specify the additional parameters of representation creation procedure when creating a representation. This flag must be used with createRepresentation flag.
        - label (lbl): Set or query the label for an assembly type. Assembly type is specified with flag "type". If no type specified, the default type is used.
        - listRepTypesProc (lrp): Set or query the procedure that provides the representation type list which an assembly type supports.  This procedure takes no argument, and returns a string array of representation types that represents the full set of representation
            types this assembly type can create.  The assembly type for which this procedure applies will be the default type, unless the type flag is used to specify an explicit assembly type.
        - newRepLabel (nrl): Specify the representation label to set on representation label edit.
        - postCreateUIProc (aoc): Set or query the UI post-creation procedure for a given assembly type. This procedure will be invoked by Maya immediately after an assembly of the specified type is created from the UI, but not through scripting.  It can be used to invoke a
            dialog, to obtain and set initial parameters on a newly-created assembly.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - proc (prc): Specify the procedure when setting the representation UI post- or pre-creation procedure, for a given assembly type.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - renameRepresentation (rnr): Renames the representation that is the argument to this flag.  The repName flag must be used to provide the new name.
        - repLabel (rl): Query or edit the label of the representation that is the argument to this flag, for a given assembly.  In both query and edit modes, the -repLabel flag specifies the name of the representation.  In edit mode, the -newRepLabel flag must be
            used to specify the new representation label.In query mode, this flag needs a value.
        - repName (rnm): Specify the representation name to set on representation creation or rename. This flag is optional with the createRepresentation flag: if omitted, the assembly will name the representation.  It is mandatory with the renameRepresentation
            flag.
        - repPostCreateUIProc (poc): Set or query the UI post-creation procedure for a specific representation type, and for a specific assembly type.  This procedure takes two arguments, the first the DAG path to the assembly, and the second the name of the representation.
            It returns no value.  It will be invoked by Maya immediately after a representation of the specified type is created from the UI, but not through scripting.  It can be used to invoke a dialog, to obtain and set initial parameters on a
            newly-created representation.  The representation type is the argument of this flag. The -proc flag must be used to specify the procedure name.  The assembly type will be the default type, unless the -type flag is used to specify an
            explicit assembly type.In query mode, this flag needs a value.
        - repPreCreateUIProc (pec): Set or query the UI pre-creation procedure for a specific representation type, and for a specific assembly type.  This procedure takes no argument, and returns a string that is passed as an argument to the -input flag when Maya invokes the
            assembly command with the -createRepresentation flag. The representation pre-creation procedure is invoked by Maya immediately before creating a representation of the specified type from the UI, but not through scripting.  It can be used to
            invoke a dialog, to obtain the creation argument for a new representation.  The representation type is the argument of this flag.  The -proc flag must be used to specify the procedure name.  The assembly type will be the default type,
            unless the -type flag is used to specify an explicit assembly type.In query mode, this flag needs a value.
        - repTypeLabelProc (rtp): Set or query the procedure that provides the representation type label, for a given assembly type.  The procedure takes the representation type as its sole argument, and returns a localized representation type label. The assembly type for
            which this procedure applies will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - type (typ): Set or query properties for the specified registered assembly type.In query mode, this flag needs a value.
        - edit (e): Edit mode flag
    """
@overload #Overload for assembly in ['edit']
def assembly(a: str = ..., al: str = ..., cob: script = ..., cr: str = ..., dt: str = ..., dr: str = ..., d: str = ..., lbl: str = ..., lrp: script = ..., nrl: str = ..., aoc: script = ..., prc: script = ..., rnr: str = ..., rl: str = ..., rnm: str = ..., poc: str = ..., pec: str = ..., rtp: script = ..., typ: str = ..., e: bool = ...) -> None:
    """assembly is undoable, queryable, and editable.
    
    Command to register assemblies for the scene assembly framework, to create
    them, and to edit and query them. Assembly nodes are DAG nodes, and are
    therefore shown in the various DAG editors (Outliner, Hypergraph, Node
    Editor). At assembly creation time, the node name defaults to the node type
    name. The assembly command can create any node that is derived from the
    assembly node base class. It also acts as a registry of these types, so that
    various scripting callbacks can be defined and registered with the assembly
    command. These callbacks are invoked by Maya during operations on assembly
    nodes, and can be used to customize behavior.
    
    ## Registering a new assembly type
    
    When defining a new type of assembly derived from the assembly node base
    class, a number of procedures can be defined through the assembly command to
    properly integrate the new assembly node type into Maya. Most of these
    procedures are used to integrate the assembly type with the Maya user
    interface, and are not required for non-interactive scripting use. For more
    information, see the MPxAssembly class description in the Maya API
    documentation. Some of the important procedures that can be registered through
    the assembly command are the following:
    
    listRepTypesProc
    
    Procedure to list the representation types that the new assembly type can create. This allows Maya to query representation types that can be created by an assembly without actually creating an assembly node.
    repTypeLabelProc
    
    Procedure to return a (possibly localized) label which is shown in the user interface for the representation types the assembly can create. The label should be a short, user-friendly, readable description of the representation type.
    createOptionBoxProc
    
    Procedure to populate an option box for creation options for the assembly type. If defined, this procedure will populate an option box that is available for creation of that assembly's type.
    repPreCreateUIProc
    
    Procedure to provide a dialog before representation creation. If defined, will be invoked by Maya so that the user can interactively make choices before the creation of a type of representation for the assembly.
    postCreateUIProc
    
    Procedure to provide a dialog after assembly creation. If defined, will be invoked by Maya so that the user can interactively make choices and apply them to the assembly after its creation.

    Example:
    ```python
        import maya.cmds as cmds
        #Create a default type of assembly and name it MyAssembly.
        #The assembly name is optional.
        #
        cmds.assembly(name='MyAssembly')
        #Create an assembly of type MyAssemblyType and name it MyAssembly.
        #
        cmds.assembly(name='MyAssembly', type='MyAssemblyType')
        #Set the default type to be MyAssemblyType.
        #
        cmds.assembly(edit=True, defaultType='MyAssemblyType')
        #Create a representation of type "MyRepType", on assembly myAssembly, and
        #name it "MyRepName"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='MyRepType',
        repName='MyRepName')
        #Rename representation "MyRepName" to "MyNewRepName" on assembly myAssembly.
        #
        cmds.assembly(myAssembly, edit=True, renameRepresentation='MyRepName',
        repName='MyNewRepName')
        #Create a representation of type "Locator", on assembly myAssembly, name it
        #"myLocator", and add an annotation using the input flag.
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Locator',
        repName="myLocator", input="An Annotation")
        #Create a representation of type "Scene", on assembly myAssembly,
        #using file "/path/to/mayafile.mb"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Scene',
        input="/path/to/mayafile.mb")
        #Delete scene representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="mayafile.mb")
        #Delete locator representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="myLocator")
        #Set the procedure that provides the representation type label for
        #an assembly type.
        #
        cmds.assembly(edit=True, repTypeLabelProc='MyRepTypeLabelQuery', type='MyAssembly')
        #Set the label for the default assembly type.
        #
        cmds.assembly(edit=True, label='My Assembly Type')
        #Set the procedure that provides the representation type list which the
        #default assembly supports.
        #
        cmds.assembly(edit=True, listRepTypesProc='MyRepTypesProc')
        #Set the pre-create UI procedure for a representation type, for a
        #specific type of assembly.
        #
        cmds.assembly(edit=True, repPreCreateUIProc='MyRepresentation', proc='MyPreCreateProcedure', type='MyAssembly')
        #Set the post-create UI procedure for a representation type, for the
        #default assembly type.
        #
        cmds.assembly(edit=True, repPostCreateUIProc='MyRepresentation', proc='MyPostCreateProcedure' )
    ```

    ---
    - Args:
        - active (a): Set the active representation by name, or query the name of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an
            array of strings when multiple assemblies are specified. Using an empty string as name means to inactivate the currently active representation.
        - activeLabel (al): Set the active representation by label, or query the label of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an
            array of strings when multiple assemblies are specified.
        - createOptionBoxProc (cob): Set or query the option box menu procedure for a specific assembly type. The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - createRepresentation (cr): Create and add a specific type of representation for an assembly. If the representation type needs additional parameters, they must be specified using the "input" flag. For example, the Maya scene assembly reference implementation Cache and
            Scene representations need an input file.
        - defaultType (dt): Set or query the default type of assembly.  When the assembly command is used to perform an operation on an assembly type rather than on an assembly object, it will be performed on the default type, unless the -type flag is used to specify
            an explicit assembly type.
        - deleteRepresentation (dr): Delete a specific representation from an assembly.
        - deregister (d): Deregister a registered assembly type. If the deregistered type is the default type, the default type will be set to the empty string.
        - input: Specify the additional parameters of representation creation procedure when creating a representation. This flag must be used with createRepresentation flag.
        - label (lbl): Set or query the label for an assembly type. Assembly type is specified with flag "type". If no type specified, the default type is used.
        - listRepTypesProc (lrp): Set or query the procedure that provides the representation type list which an assembly type supports.  This procedure takes no argument, and returns a string array of representation types that represents the full set of representation
            types this assembly type can create.  The assembly type for which this procedure applies will be the default type, unless the type flag is used to specify an explicit assembly type.
        - newRepLabel (nrl): Specify the representation label to set on representation label edit.
        - postCreateUIProc (aoc): Set or query the UI post-creation procedure for a given assembly type. This procedure will be invoked by Maya immediately after an assembly of the specified type is created from the UI, but not through scripting.  It can be used to invoke a
            dialog, to obtain and set initial parameters on a newly-created assembly.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - proc (prc): Specify the procedure when setting the representation UI post- or pre-creation procedure, for a given assembly type.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - renameRepresentation (rnr): Renames the representation that is the argument to this flag.  The repName flag must be used to provide the new name.
        - repLabel (rl): Query or edit the label of the representation that is the argument to this flag, for a given assembly.  In both query and edit modes, the -repLabel flag specifies the name of the representation.  In edit mode, the -newRepLabel flag must be
            used to specify the new representation label.In query mode, this flag needs a value.
        - repName (rnm): Specify the representation name to set on representation creation or rename. This flag is optional with the createRepresentation flag: if omitted, the assembly will name the representation.  It is mandatory with the renameRepresentation
            flag.
        - repPostCreateUIProc (poc): Set or query the UI post-creation procedure for a specific representation type, and for a specific assembly type.  This procedure takes two arguments, the first the DAG path to the assembly, and the second the name of the representation.
            It returns no value.  It will be invoked by Maya immediately after a representation of the specified type is created from the UI, but not through scripting.  It can be used to invoke a dialog, to obtain and set initial parameters on a
            newly-created representation.  The representation type is the argument of this flag. The -proc flag must be used to specify the procedure name.  The assembly type will be the default type, unless the -type flag is used to specify an
            explicit assembly type.In query mode, this flag needs a value.
        - repPreCreateUIProc (pec): Set or query the UI pre-creation procedure for a specific representation type, and for a specific assembly type.  This procedure takes no argument, and returns a string that is passed as an argument to the -input flag when Maya invokes the
            assembly command with the -createRepresentation flag. The representation pre-creation procedure is invoked by Maya immediately before creating a representation of the specified type from the UI, but not through scripting.  It can be used to
            invoke a dialog, to obtain the creation argument for a new representation.  The representation type is the argument of this flag.  The -proc flag must be used to specify the procedure name.  The assembly type will be the default type,
            unless the -type flag is used to specify an explicit assembly type.In query mode, this flag needs a value.
        - repTypeLabelProc (rtp): Set or query the procedure that provides the representation type label, for a given assembly type.  The procedure takes the representation type as its sole argument, and returns a localized representation type label. The assembly type for
            which this procedure applies will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - type (typ): Set or query properties for the specified registered assembly type.In query mode, this flag needs a value.
        - edit (e): Edit mode flag
    """
@overload #Overload for assembly in ['edit']
def assembly(active: str = ..., a: str = ..., activeLabel: str = ..., al: str = ..., createOptionBoxProc: script = ..., cob: script = ..., createRepresentation: str = ..., cr: str = ..., defaultType: str = ..., dt: str = ..., deleteRepresentation: str = ..., dr: str = ..., deregister: str = ..., d: str = ..., input: str = ..., label: str = ..., lbl: str = ..., listRepTypesProc: script = ..., lrp: script = ..., newRepLabel: str = ..., nrl: str = ..., postCreateUIProc: script = ..., aoc: script = ..., proc: script = ..., prc: script = ..., renameRepresentation: str = ..., rnr: str = ..., repLabel: str = ..., rl: str = ..., repName: str = ..., rnm: str = ..., repPostCreateUIProc: str = ..., poc: str = ..., repPreCreateUIProc: str = ..., pec: str = ..., repTypeLabelProc: script = ..., rtp: script = ..., type: str = ..., typ: str = ..., edit: bool = ..., e: bool = ...) -> None:
    """assembly is undoable, queryable, and editable.
    
    Command to register assemblies for the scene assembly framework, to create
    them, and to edit and query them. Assembly nodes are DAG nodes, and are
    therefore shown in the various DAG editors (Outliner, Hypergraph, Node
    Editor). At assembly creation time, the node name defaults to the node type
    name. The assembly command can create any node that is derived from the
    assembly node base class. It also acts as a registry of these types, so that
    various scripting callbacks can be defined and registered with the assembly
    command. These callbacks are invoked by Maya during operations on assembly
    nodes, and can be used to customize behavior.
    
    ## Registering a new assembly type
    
    When defining a new type of assembly derived from the assembly node base
    class, a number of procedures can be defined through the assembly command to
    properly integrate the new assembly node type into Maya. Most of these
    procedures are used to integrate the assembly type with the Maya user
    interface, and are not required for non-interactive scripting use. For more
    information, see the MPxAssembly class description in the Maya API
    documentation. Some of the important procedures that can be registered through
    the assembly command are the following:
    
    listRepTypesProc
    
    Procedure to list the representation types that the new assembly type can create. This allows Maya to query representation types that can be created by an assembly without actually creating an assembly node.
    repTypeLabelProc
    
    Procedure to return a (possibly localized) label which is shown in the user interface for the representation types the assembly can create. The label should be a short, user-friendly, readable description of the representation type.
    createOptionBoxProc
    
    Procedure to populate an option box for creation options for the assembly type. If defined, this procedure will populate an option box that is available for creation of that assembly's type.
    repPreCreateUIProc
    
    Procedure to provide a dialog before representation creation. If defined, will be invoked by Maya so that the user can interactively make choices before the creation of a type of representation for the assembly.
    postCreateUIProc
    
    Procedure to provide a dialog after assembly creation. If defined, will be invoked by Maya so that the user can interactively make choices and apply them to the assembly after its creation.

    Example:
    ```python
        import maya.cmds as cmds
        #Create a default type of assembly and name it MyAssembly.
        #The assembly name is optional.
        #
        cmds.assembly(name='MyAssembly')
        #Create an assembly of type MyAssemblyType and name it MyAssembly.
        #
        cmds.assembly(name='MyAssembly', type='MyAssemblyType')
        #Set the default type to be MyAssemblyType.
        #
        cmds.assembly(edit=True, defaultType='MyAssemblyType')
        #Create a representation of type "MyRepType", on assembly myAssembly, and
        #name it "MyRepName"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='MyRepType',
        repName='MyRepName')
        #Rename representation "MyRepName" to "MyNewRepName" on assembly myAssembly.
        #
        cmds.assembly(myAssembly, edit=True, renameRepresentation='MyRepName',
        repName='MyNewRepName')
        #Create a representation of type "Locator", on assembly myAssembly, name it
        #"myLocator", and add an annotation using the input flag.
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Locator',
        repName="myLocator", input="An Annotation")
        #Create a representation of type "Scene", on assembly myAssembly,
        #using file "/path/to/mayafile.mb"
        #
        cmds.assembly(myAssembly, edit=True, createRepresentation='Scene',
        input="/path/to/mayafile.mb")
        #Delete scene representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="mayafile.mb")
        #Delete locator representation from assembly myAssembly
        cmds.assembly(myAssembly, edit=True, deleteRepresentation="myLocator")
        #Set the procedure that provides the representation type label for
        #an assembly type.
        #
        cmds.assembly(edit=True, repTypeLabelProc='MyRepTypeLabelQuery', type='MyAssembly')
        #Set the label for the default assembly type.
        #
        cmds.assembly(edit=True, label='My Assembly Type')
        #Set the procedure that provides the representation type list which the
        #default assembly supports.
        #
        cmds.assembly(edit=True, listRepTypesProc='MyRepTypesProc')
        #Set the pre-create UI procedure for a representation type, for a
        #specific type of assembly.
        #
        cmds.assembly(edit=True, repPreCreateUIProc='MyRepresentation', proc='MyPreCreateProcedure', type='MyAssembly')
        #Set the post-create UI procedure for a representation type, for the
        #default assembly type.
        #
        cmds.assembly(edit=True, repPostCreateUIProc='MyRepresentation', proc='MyPostCreateProcedure' )
    ```

    ---
    - Args:
        - active (a): Set the active representation by name, or query the name of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an
            array of strings when multiple assemblies are specified. Using an empty string as name means to inactivate the currently active representation.
        - activeLabel (al): Set the active representation by label, or query the label of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an
            array of strings when multiple assemblies are specified.
        - createOptionBoxProc (cob): Set or query the option box menu procedure for a specific assembly type. The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - createRepresentation (cr): Create and add a specific type of representation for an assembly. If the representation type needs additional parameters, they must be specified using the "input" flag. For example, the Maya scene assembly reference implementation Cache and
            Scene representations need an input file.
        - defaultType (dt): Set or query the default type of assembly.  When the assembly command is used to perform an operation on an assembly type rather than on an assembly object, it will be performed on the default type, unless the -type flag is used to specify
            an explicit assembly type.
        - deleteRepresentation (dr): Delete a specific representation from an assembly.
        - deregister (d): Deregister a registered assembly type. If the deregistered type is the default type, the default type will be set to the empty string.
        - input: Specify the additional parameters of representation creation procedure when creating a representation. This flag must be used with createRepresentation flag.
        - label (lbl): Set or query the label for an assembly type. Assembly type is specified with flag "type". If no type specified, the default type is used.
        - listRepTypesProc (lrp): Set or query the procedure that provides the representation type list which an assembly type supports.  This procedure takes no argument, and returns a string array of representation types that represents the full set of representation
            types this assembly type can create.  The assembly type for which this procedure applies will be the default type, unless the type flag is used to specify an explicit assembly type.
        - newRepLabel (nrl): Specify the representation label to set on representation label edit.
        - postCreateUIProc (aoc): Set or query the UI post-creation procedure for a given assembly type. This procedure will be invoked by Maya immediately after an assembly of the specified type is created from the UI, but not through scripting.  It can be used to invoke a
            dialog, to obtain and set initial parameters on a newly-created assembly.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - proc (prc): Specify the procedure when setting the representation UI post- or pre-creation procedure, for a given assembly type.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - renameRepresentation (rnr): Renames the representation that is the argument to this flag.  The repName flag must be used to provide the new name.
        - repLabel (rl): Query or edit the label of the representation that is the argument to this flag, for a given assembly.  In both query and edit modes, the -repLabel flag specifies the name of the representation.  In edit mode, the -newRepLabel flag must be
            used to specify the new representation label.In query mode, this flag needs a value.
        - repName (rnm): Specify the representation name to set on representation creation or rename. This flag is optional with the createRepresentation flag: if omitted, the assembly will name the representation.  It is mandatory with the renameRepresentation
            flag.
        - repPostCreateUIProc (poc): Set or query the UI post-creation procedure for a specific representation type, and for a specific assembly type.  This procedure takes two arguments, the first the DAG path to the assembly, and the second the name of the representation.
            It returns no value.  It will be invoked by Maya immediately after a representation of the specified type is created from the UI, but not through scripting.  It can be used to invoke a dialog, to obtain and set initial parameters on a
            newly-created representation.  The representation type is the argument of this flag. The -proc flag must be used to specify the procedure name.  The assembly type will be the default type, unless the -type flag is used to specify an
            explicit assembly type.In query mode, this flag needs a value.
        - repPreCreateUIProc (pec): Set or query the UI pre-creation procedure for a specific representation type, and for a specific assembly type.  This procedure takes no argument, and returns a string that is passed as an argument to the -input flag when Maya invokes the
            assembly command with the -createRepresentation flag. The representation pre-creation procedure is invoked by Maya immediately before creating a representation of the specified type from the UI, but not through scripting.  It can be used to
            invoke a dialog, to obtain the creation argument for a new representation.  The representation type is the argument of this flag.  The -proc flag must be used to specify the procedure name.  The assembly type will be the default type,
            unless the -type flag is used to specify an explicit assembly type.In query mode, this flag needs a value.
        - repTypeLabelProc (rtp): Set or query the procedure that provides the representation type label, for a given assembly type.  The procedure takes the representation type as its sole argument, and returns a localized representation type label. The assembly type for
            which this procedure applies will be the default type, unless the -type flag is used to specify an explicit assembly type.
        - type (typ): Set or query properties for the specified registered assembly type.In query mode, this flag needs a value.
        - edit (e): Edit mode flag
    """
