"""Stub files for General category in Maya commands, command: containerBind."""

from typing import Any, overload

@overload #Overload for containerBind in ['create']
def containerBind(allNames: bool = ..., force: bool = ..., preview: bool = ...) -> None:
    """containerBind is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    automated binding operations on the container. A container's published
    interface can be bound using a bindingSet on the associated container
    template.

    Example:
    ```python
        import maya.cmds as cmds
        # query the template binding sets available for this container
        #
        cmds.containerBind(container1, query=1, bindingSetList=1)
        # attempt to bind published names on the container
        # using matching information in the bindingSet specified.
        # By default only unbound names are considered.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings")
        # Attempt to bind all published names on the container
        # using matching information in the bindingSet specified.
        # Previously bound names will only be re-bound if the bindingSet
        # produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1)
        # Forcibly re-bind all published names on the container
        # using matching information in the bindingSet specified.
        # All previously bound names will be unbound and will only
        # be re-bound if the binding set produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1, force=1)
        # preview what the results of a binding operation would be, but do
        # not actually perform it.
        cmds.containerBind(container1, bindingSet="MayaBindings", preview=1, allNames=1, force=1)
    ```

    ---
    - Args:
        - allNames (all): Specifies that all published names on the container should be considered during the binding operation.  By default only unbound published names will be operated on.  Additionally specifying the 'force' option with 'all' will cause all
            previously bound published names to be reset (or unbound) before the binding operation is performed; in the event that there is no appropriate binding found for the published name, it will be left in the unbound state.
        - force (f): This flag is used to force certain operations to proceed that would normally not be performed.
        - preview (p): This flag will provide a preview of the results of a binding operation but will not actually perform it.  A list of publishedName/boundName pairs are returned for each published name that would be affected by the binding action. If the
            binding of a published name will not change as a result of the action it will not be listed. Published names that were bound but will become unbound are also listed, in this case the associated boundName will be indicated by an empty
            string.
    """
@overload #Overload for containerBind in ['create']
def containerBind(all: bool = ..., f: bool = ..., p: bool = ...) -> None:
    """containerBind is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    automated binding operations on the container. A container's published
    interface can be bound using a bindingSet on the associated container
    template.

    Example:
    ```python
        import maya.cmds as cmds
        # query the template binding sets available for this container
        #
        cmds.containerBind(container1, query=1, bindingSetList=1)
        # attempt to bind published names on the container
        # using matching information in the bindingSet specified.
        # By default only unbound names are considered.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings")
        # Attempt to bind all published names on the container
        # using matching information in the bindingSet specified.
        # Previously bound names will only be re-bound if the bindingSet
        # produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1)
        # Forcibly re-bind all published names on the container
        # using matching information in the bindingSet specified.
        # All previously bound names will be unbound and will only
        # be re-bound if the binding set produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1, force=1)
        # preview what the results of a binding operation would be, but do
        # not actually perform it.
        cmds.containerBind(container1, bindingSet="MayaBindings", preview=1, allNames=1, force=1)
    ```

    ---
    - Args:
        - allNames (all): Specifies that all published names on the container should be considered during the binding operation.  By default only unbound published names will be operated on.  Additionally specifying the 'force' option with 'all' will cause all
            previously bound published names to be reset (or unbound) before the binding operation is performed; in the event that there is no appropriate binding found for the published name, it will be left in the unbound state.
        - force (f): This flag is used to force certain operations to proceed that would normally not be performed.
        - preview (p): This flag will provide a preview of the results of a binding operation but will not actually perform it.  A list of publishedName/boundName pairs are returned for each published name that would be affected by the binding action. If the
            binding of a published name will not change as a result of the action it will not be listed. Published names that were bound but will become unbound are also listed, in this case the associated boundName will be indicated by an empty
            string.
    """
@overload #Overload for containerBind in ['create']
def containerBind(allNames: bool = ..., all: bool = ..., force: bool = ..., f: bool = ..., preview: bool = ..., p: bool = ...) -> None:
    """containerBind is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    automated binding operations on the container. A container's published
    interface can be bound using a bindingSet on the associated container
    template.

    Example:
    ```python
        import maya.cmds as cmds
        # query the template binding sets available for this container
        #
        cmds.containerBind(container1, query=1, bindingSetList=1)
        # attempt to bind published names on the container
        # using matching information in the bindingSet specified.
        # By default only unbound names are considered.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings")
        # Attempt to bind all published names on the container
        # using matching information in the bindingSet specified.
        # Previously bound names will only be re-bound if the bindingSet
        # produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1)
        # Forcibly re-bind all published names on the container
        # using matching information in the bindingSet specified.
        # All previously bound names will be unbound and will only
        # be re-bound if the binding set produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1, force=1)
        # preview what the results of a binding operation would be, but do
        # not actually perform it.
        cmds.containerBind(container1, bindingSet="MayaBindings", preview=1, allNames=1, force=1)
    ```

    ---
    - Args:
        - allNames (all): Specifies that all published names on the container should be considered during the binding operation.  By default only unbound published names will be operated on.  Additionally specifying the 'force' option with 'all' will cause all
            previously bound published names to be reset (or unbound) before the binding operation is performed; in the event that there is no appropriate binding found for the published name, it will be left in the unbound state.
        - force (f): This flag is used to force certain operations to proceed that would normally not be performed.
        - preview (p): This flag will provide a preview of the results of a binding operation but will not actually perform it.  A list of publishedName/boundName pairs are returned for each published name that would be affected by the binding action. If the
            binding of a published name will not change as a result of the action it will not be listed. Published names that were bound but will become unbound are also listed, in this case the associated boundName will be indicated by an empty
            string.
    """
@overload #Overload for containerBind in ['query']
def containerBind(bindingSet: str = ..., bindingSetConditions: bool = ..., bindingSetList: bool = ..., query: bool = ...) -> None:
    """containerBind is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    automated binding operations on the container. A container's published
    interface can be bound using a bindingSet on the associated container
    template.

    Example:
    ```python
        import maya.cmds as cmds
        # query the template binding sets available for this container
        #
        cmds.containerBind(container1, query=1, bindingSetList=1)
        # attempt to bind published names on the container
        # using matching information in the bindingSet specified.
        # By default only unbound names are considered.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings")
        # Attempt to bind all published names on the container
        # using matching information in the bindingSet specified.
        # Previously bound names will only be re-bound if the bindingSet
        # produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1)
        # Forcibly re-bind all published names on the container
        # using matching information in the bindingSet specified.
        # All previously bound names will be unbound and will only
        # be re-bound if the binding set produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1, force=1)
        # preview what the results of a binding operation would be, but do
        # not actually perform it.
        cmds.containerBind(container1, bindingSet="MayaBindings", preview=1, allNames=1, force=1)
    ```

    ---
    - Args:
        - bindingSet (bs): Specifies the name of the template binding set to use for the bind or query operation. This flag is not available in query mode.In query mode, this flag needs a value.
        - bindingSetConditions (bsc): Used in query mode, returns a list of binding set condition entries from the specified template binding set.  The list returned is composed of of all published name / condition string pairs for each entry in the binding set. This flag
            returns all entries in the associated binding set and does not take into account the validity of each entry with respect to the container's list of published names, bound or unbound state, etc.
        - bindingSetList (bsl): Used in query mode, returns a list of available binding sets that are defined on the associated container template.
        - query (q): Query mode flag
    """
@overload #Overload for containerBind in ['query']
def containerBind(bs: str = ..., bsc: bool = ..., bsl: bool = ..., q: bool = ...) -> None:
    """containerBind is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    automated binding operations on the container. A container's published
    interface can be bound using a bindingSet on the associated container
    template.

    Example:
    ```python
        import maya.cmds as cmds
        # query the template binding sets available for this container
        #
        cmds.containerBind(container1, query=1, bindingSetList=1)
        # attempt to bind published names on the container
        # using matching information in the bindingSet specified.
        # By default only unbound names are considered.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings")
        # Attempt to bind all published names on the container
        # using matching information in the bindingSet specified.
        # Previously bound names will only be re-bound if the bindingSet
        # produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1)
        # Forcibly re-bind all published names on the container
        # using matching information in the bindingSet specified.
        # All previously bound names will be unbound and will only
        # be re-bound if the binding set produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1, force=1)
        # preview what the results of a binding operation would be, but do
        # not actually perform it.
        cmds.containerBind(container1, bindingSet="MayaBindings", preview=1, allNames=1, force=1)
    ```

    ---
    - Args:
        - bindingSet (bs): Specifies the name of the template binding set to use for the bind or query operation. This flag is not available in query mode.In query mode, this flag needs a value.
        - bindingSetConditions (bsc): Used in query mode, returns a list of binding set condition entries from the specified template binding set.  The list returned is composed of of all published name / condition string pairs for each entry in the binding set. This flag
            returns all entries in the associated binding set and does not take into account the validity of each entry with respect to the container's list of published names, bound or unbound state, etc.
        - bindingSetList (bsl): Used in query mode, returns a list of available binding sets that are defined on the associated container template.
        - query (q): Query mode flag
    """
@overload #Overload for containerBind in ['query']
def containerBind(bindingSet: str = ..., bs: str = ..., bindingSetConditions: bool = ..., bsc: bool = ..., bindingSetList: bool = ..., bsl: bool = ..., query: bool = ..., q: bool = ...) -> None:
    """containerBind is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    automated binding operations on the container. A container's published
    interface can be bound using a bindingSet on the associated container
    template.

    Example:
    ```python
        import maya.cmds as cmds
        # query the template binding sets available for this container
        #
        cmds.containerBind(container1, query=1, bindingSetList=1)
        # attempt to bind published names on the container
        # using matching information in the bindingSet specified.
        # By default only unbound names are considered.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings")
        # Attempt to bind all published names on the container
        # using matching information in the bindingSet specified.
        # Previously bound names will only be re-bound if the bindingSet
        # produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1)
        # Forcibly re-bind all published names on the container
        # using matching information in the bindingSet specified.
        # All previously bound names will be unbound and will only
        # be re-bound if the binding set produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1, force=1)
        # preview what the results of a binding operation would be, but do
        # not actually perform it.
        cmds.containerBind(container1, bindingSet="MayaBindings", preview=1, allNames=1, force=1)
    ```

    ---
    - Args:
        - bindingSet (bs): Specifies the name of the template binding set to use for the bind or query operation. This flag is not available in query mode.In query mode, this flag needs a value.
        - bindingSetConditions (bsc): Used in query mode, returns a list of binding set condition entries from the specified template binding set.  The list returned is composed of of all published name / condition string pairs for each entry in the binding set. This flag
            returns all entries in the associated binding set and does not take into account the validity of each entry with respect to the container's list of published names, bound or unbound state, etc.
        - bindingSetList (bsl): Used in query mode, returns a list of available binding sets that are defined on the associated container template.
        - query (q): Query mode flag
    """
@overload #Overload for containerBind in ['edit']
def containerBind(bindingSetList: bool = ..., edit: bool = ...) -> None:
    """containerBind is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    automated binding operations on the container. A container's published
    interface can be bound using a bindingSet on the associated container
    template.

    Example:
    ```python
        import maya.cmds as cmds
        # query the template binding sets available for this container
        #
        cmds.containerBind(container1, query=1, bindingSetList=1)
        # attempt to bind published names on the container
        # using matching information in the bindingSet specified.
        # By default only unbound names are considered.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings")
        # Attempt to bind all published names on the container
        # using matching information in the bindingSet specified.
        # Previously bound names will only be re-bound if the bindingSet
        # produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1)
        # Forcibly re-bind all published names on the container
        # using matching information in the bindingSet specified.
        # All previously bound names will be unbound and will only
        # be re-bound if the binding set produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1, force=1)
        # preview what the results of a binding operation would be, but do
        # not actually perform it.
        cmds.containerBind(container1, bindingSet="MayaBindings", preview=1, allNames=1, force=1)
    ```

    ---
    - Args:
        - bindingSetList (bsl): Used in query mode, returns a list of available binding sets that are defined on the associated container template.
        - edit (e): Edit mode flag
    """
@overload #Overload for containerBind in ['edit']
def containerBind(bsl: bool = ..., e: bool = ...) -> None:
    """containerBind is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    automated binding operations on the container. A container's published
    interface can be bound using a bindingSet on the associated container
    template.

    Example:
    ```python
        import maya.cmds as cmds
        # query the template binding sets available for this container
        #
        cmds.containerBind(container1, query=1, bindingSetList=1)
        # attempt to bind published names on the container
        # using matching information in the bindingSet specified.
        # By default only unbound names are considered.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings")
        # Attempt to bind all published names on the container
        # using matching information in the bindingSet specified.
        # Previously bound names will only be re-bound if the bindingSet
        # produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1)
        # Forcibly re-bind all published names on the container
        # using matching information in the bindingSet specified.
        # All previously bound names will be unbound and will only
        # be re-bound if the binding set produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1, force=1)
        # preview what the results of a binding operation would be, but do
        # not actually perform it.
        cmds.containerBind(container1, bindingSet="MayaBindings", preview=1, allNames=1, force=1)
    ```

    ---
    - Args:
        - bindingSetList (bsl): Used in query mode, returns a list of available binding sets that are defined on the associated container template.
        - edit (e): Edit mode flag
    """
@overload #Overload for containerBind in ['edit']
def containerBind(bindingSetList: bool = ..., bsl: bool = ..., edit: bool = ..., e: bool = ...) -> None:
    """containerBind is undoable, queryable, and editable.
    
    This is an accessory command to the container command which is used for some
    automated binding operations on the container. A container's published
    interface can be bound using a bindingSet on the associated container
    template.

    Example:
    ```python
        import maya.cmds as cmds
        # query the template binding sets available for this container
        #
        cmds.containerBind(container1, query=1, bindingSetList=1)
        # attempt to bind published names on the container
        # using matching information in the bindingSet specified.
        # By default only unbound names are considered.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings")
        # Attempt to bind all published names on the container
        # using matching information in the bindingSet specified.
        # Previously bound names will only be re-bound if the bindingSet
        # produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1)
        # Forcibly re-bind all published names on the container
        # using matching information in the bindingSet specified.
        # All previously bound names will be unbound and will only
        # be re-bound if the binding set produces an appropriate match.
        #
        cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1, force=1)
        # preview what the results of a binding operation would be, but do
        # not actually perform it.
        cmds.containerBind(container1, bindingSet="MayaBindings", preview=1, allNames=1, force=1)
    ```

    ---
    - Args:
        - bindingSetList (bsl): Used in query mode, returns a list of available binding sets that are defined on the associated container template.
        - edit (e): Edit mode flag
    """
