"""Stub files for General category in Maya commands, command: containerTemplate."""

from typing import Any, overload

@overload #Overload for containerTemplate in ['create']
def containerTemplate(addBindingSet: str = ..., addView: str = ..., allKeyable: bool = ..., attribute: str = ..., attributeList: str = ..., baseName: str = ..., bindingSetList: str = ..., childAnchor: bool = ..., delete: bool = ..., expandCompounds: bool = ..., fileName: str = ..., force: bool = ..., fromContainer: str = ..., fromSelection: bool = ..., layoutMode: int = ..., parentAnchor: bool = ..., publishedNodeList: str = ..., removeBindingSet: str = ..., removeView: str = ..., rootTransform: bool = ..., save: bool = ..., searchPath: str = ..., silent: bool = ..., unload: bool = ..., updateBindingSet: str = ..., useHierarchy: bool = ..., viewList: str = ...) -> None:
    """containerTemplate is NOT undoable, queryable, and editable.
    
    A container template is a description of a container's published interface.
    This command provides the ability to create and save a template file for a
    container or load an existing template file. Once a template exists, the user
    can query the template information.

    ---
    - Args:
        - addBindingSet (abs): This argument is used to add a new binding set with the given name to a template. A default binding set will be created. If the binding set already exists, the force flag must be used to replace the existing binding set. When used with the
            fromContainer option, default bindings will be entered based on the current bindings of the designated container. When used without a reference container, the binding set will be made with placeholder entries. The template must be saved
            before the new binding set is permanently stored with the template file.
        - addView (av): This argument is used to add a new view with the given name to a template. By default a view containing a flat list of all template attributes will be created.  The layoutMode flag provides more layout options. The template must be saved
            before the new view is permanently stored with the template file.
        - allKeyable (ak): Used when the fromSelection flag is true and fromContainer is false. If true we will use all keyable attributes to define the template or the view, if false we use the attributes passed in with the attribute flag.
        - attribute (at): If fromSelection is true and allKeyable is false, this attribute name will be used to create an attribute item in the template file.
        - attributeList (al): Used in query mode, returns a list of attributes contained in the template definition.
        - baseName (bn): Used in query mode, returns the base name of the template. The basename is the template name with any package qualifiers stripped off.
        - bindingSetList (bsl): Used in query mode, returns a list of all binding sets defined on the template.
        - childAnchor (can): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only childAnchor published nodes.
        - delete (d): Delete the specified template and its file. All objects that are associated with this template or contained in the same template file will be deleted. To simply unload a template without permanently deleting its file, use unload instead.
        - expandCompounds (ec): This argument is used to determine how compound parent attributes and their children will be added to generated views when both are published to the container. When true, the compound parent and all compound child attributes published to
            the container will be included in the view. When false, only the parent attribute is included in the view. Note: if only the child attributes are published and not the parent, the children will be included in the view, this flag is only
            used in the situation where both parent and child attributes are published to the container. The default value is false.
        - fileName (fn): Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is
            recommended but not required that the filename and template name correspond.
        - force (f): This flag is used with some actions to allow them to proceed with an overwrite or destructive operation. When used with load, it will allow an existing template to be reloaded from a file.  When used in create mode, it will allow an
            existing template to be recreated (for example when using fromContainer argument to regenerate a template).
        - fromContainer (fc): This argument is used in create or edit mode to specify a container node to be used for generating the template contents. In template creation mode, the template definition will be created based on the list of published attributes in the
            specified container. In edit mode, when used with the addNames flag or with no other flag, any published name on the container not present as an attribute on the template will be added to the template. This flag is also used in conjunction
            with flags such as addView.
        - fromSelection (fs): If true, we will use the active selection list to create the template or the view. If allKeyable is also true then we will create the template from all keyable attributes in the selection, otherwise we will create the template using the
            attributes specified with the attribute flag.
        - layoutMode (lm): This argument is used to specify the layout mode when creating a view. Values correspond as follows: 0: layout in flat list (default when not creating view from container) 1: layout grouped by node (default if creating view from container)
            The fromContainer or fromSelection argument is required to provide the reference container or selection for layout modes that require node information.  Note that views can only refer to defined template attributes. This means that when
            using the fromContainer or from Selection flag to add a view to an existing template, only attributes that are defined on both the template and the container or the current selection will be included in the view (i.e. published attributes
            on the container that are not defined in the template will be ignored).
        - parentAnchor (pan): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only parentAnchor published nodes.
        - publishedNodeList (pnl): Used in query mode, returns a list of published nodes contained in the template definition. By default all published nodes on the template will be returned. The list of published nodes can be limited to only include certain types of
            published nodes using one of the childAnchor, parentAnchor or rootTransform flags. If an optional flag is are specified, only nodes of the specified type will be returned.
        - removeBindingSet (rbs): This argument is used to remove the named binding set from the template. The template must be saved before the binding set is permanently removed from the template file.
        - removeView (rv): This argument is used to remove the named view from the template. The template must be saved before the view is permanently removed from the template file.
        - rootTransform (rtn): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only rootTransform published nodes.
        - save (s): Save the specified template to a file. If a filename is specified for the template, the entire file (and all templates associated with it) will be saved. If no file name is specified, a default filename will be assumed, based on the
            template name.
        - searchPath (sp): The template searchPath is an ordered list of all locations that are being searched to locate template files (first location searched to last location searched). The template search path setting is stored in the current workspace and can
            also be set and queried as the file rule entry for 'templates' (see the workspace command for more information). In edit mode, this flag allows the search path setting to be customized. When setting the search path value, the list should
            conform to a path list format expected on the current platform.  This means that paths should be separated by a semicolon (;) on Windows and a colon (:) on Linux and MacOSX. Environment variables can also be used. Additional built-in paths
            may be added automatically by maya to the customized settings. In query mode, this flag returns the current contents of the search path; all paths, both customized and built-in, will be included in the query return value.
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - unload (u): Unload the specified template.  This action will not delete the associated template file if one exists, it merely removes the template definition from the current session.
        - updateBindingSet (ubs): This argument is used to update an existing binding set with new bindings. When used with the fromContainer argument binding set entries with be replaced or merged in the binding set based on the bindings of the designated container. If the
            force flag is used, existing entries in the binding set are replaced with new values. When force is not used, only new entries are merged into the binding set, any existing entries will be left as-is. When used without a reference
            container, the binding set will be updated with placeholder entries. The template must be saved before the new binding set is permanently stored with the template file.
        - useHierarchy (uh): If true, and the fromSelection flag is set, the selection list will expand to include it's hierarchy also.
        - viewList (vl): Used in query mode, returns a list of all views defined on the template.
    """
@overload #Overload for containerTemplate in ['create']
def containerTemplate(abs: str = ..., av: str = ..., ak: bool = ..., at: str = ..., al: str = ..., bn: str = ..., bsl: str = ..., can: bool = ..., d: bool = ..., ec: bool = ..., fn: str = ..., f: bool = ..., fc: str = ..., fs: bool = ..., lm: int = ..., pan: bool = ..., pnl: str = ..., rbs: str = ..., rv: str = ..., rtn: bool = ..., s: bool = ..., sp: str = ..., si: bool = ..., u: bool = ..., ubs: str = ..., uh: bool = ..., vl: str = ...) -> None:
    """containerTemplate is NOT undoable, queryable, and editable.
    
    A container template is a description of a container's published interface.
    This command provides the ability to create and save a template file for a
    container or load an existing template file. Once a template exists, the user
    can query the template information.

    ---
    - Args:
        - addBindingSet (abs): This argument is used to add a new binding set with the given name to a template. A default binding set will be created. If the binding set already exists, the force flag must be used to replace the existing binding set. When used with the
            fromContainer option, default bindings will be entered based on the current bindings of the designated container. When used without a reference container, the binding set will be made with placeholder entries. The template must be saved
            before the new binding set is permanently stored with the template file.
        - addView (av): This argument is used to add a new view with the given name to a template. By default a view containing a flat list of all template attributes will be created.  The layoutMode flag provides more layout options. The template must be saved
            before the new view is permanently stored with the template file.
        - allKeyable (ak): Used when the fromSelection flag is true and fromContainer is false. If true we will use all keyable attributes to define the template or the view, if false we use the attributes passed in with the attribute flag.
        - attribute (at): If fromSelection is true and allKeyable is false, this attribute name will be used to create an attribute item in the template file.
        - attributeList (al): Used in query mode, returns a list of attributes contained in the template definition.
        - baseName (bn): Used in query mode, returns the base name of the template. The basename is the template name with any package qualifiers stripped off.
        - bindingSetList (bsl): Used in query mode, returns a list of all binding sets defined on the template.
        - childAnchor (can): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only childAnchor published nodes.
        - delete (d): Delete the specified template and its file. All objects that are associated with this template or contained in the same template file will be deleted. To simply unload a template without permanently deleting its file, use unload instead.
        - expandCompounds (ec): This argument is used to determine how compound parent attributes and their children will be added to generated views when both are published to the container. When true, the compound parent and all compound child attributes published to
            the container will be included in the view. When false, only the parent attribute is included in the view. Note: if only the child attributes are published and not the parent, the children will be included in the view, this flag is only
            used in the situation where both parent and child attributes are published to the container. The default value is false.
        - fileName (fn): Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is
            recommended but not required that the filename and template name correspond.
        - force (f): This flag is used with some actions to allow them to proceed with an overwrite or destructive operation. When used with load, it will allow an existing template to be reloaded from a file.  When used in create mode, it will allow an
            existing template to be recreated (for example when using fromContainer argument to regenerate a template).
        - fromContainer (fc): This argument is used in create or edit mode to specify a container node to be used for generating the template contents. In template creation mode, the template definition will be created based on the list of published attributes in the
            specified container. In edit mode, when used with the addNames flag or with no other flag, any published name on the container not present as an attribute on the template will be added to the template. This flag is also used in conjunction
            with flags such as addView.
        - fromSelection (fs): If true, we will use the active selection list to create the template or the view. If allKeyable is also true then we will create the template from all keyable attributes in the selection, otherwise we will create the template using the
            attributes specified with the attribute flag.
        - layoutMode (lm): This argument is used to specify the layout mode when creating a view. Values correspond as follows: 0: layout in flat list (default when not creating view from container) 1: layout grouped by node (default if creating view from container)
            The fromContainer or fromSelection argument is required to provide the reference container or selection for layout modes that require node information.  Note that views can only refer to defined template attributes. This means that when
            using the fromContainer or from Selection flag to add a view to an existing template, only attributes that are defined on both the template and the container or the current selection will be included in the view (i.e. published attributes
            on the container that are not defined in the template will be ignored).
        - parentAnchor (pan): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only parentAnchor published nodes.
        - publishedNodeList (pnl): Used in query mode, returns a list of published nodes contained in the template definition. By default all published nodes on the template will be returned. The list of published nodes can be limited to only include certain types of
            published nodes using one of the childAnchor, parentAnchor or rootTransform flags. If an optional flag is are specified, only nodes of the specified type will be returned.
        - removeBindingSet (rbs): This argument is used to remove the named binding set from the template. The template must be saved before the binding set is permanently removed from the template file.
        - removeView (rv): This argument is used to remove the named view from the template. The template must be saved before the view is permanently removed from the template file.
        - rootTransform (rtn): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only rootTransform published nodes.
        - save (s): Save the specified template to a file. If a filename is specified for the template, the entire file (and all templates associated with it) will be saved. If no file name is specified, a default filename will be assumed, based on the
            template name.
        - searchPath (sp): The template searchPath is an ordered list of all locations that are being searched to locate template files (first location searched to last location searched). The template search path setting is stored in the current workspace and can
            also be set and queried as the file rule entry for 'templates' (see the workspace command for more information). In edit mode, this flag allows the search path setting to be customized. When setting the search path value, the list should
            conform to a path list format expected on the current platform.  This means that paths should be separated by a semicolon (;) on Windows and a colon (:) on Linux and MacOSX. Environment variables can also be used. Additional built-in paths
            may be added automatically by maya to the customized settings. In query mode, this flag returns the current contents of the search path; all paths, both customized and built-in, will be included in the query return value.
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - unload (u): Unload the specified template.  This action will not delete the associated template file if one exists, it merely removes the template definition from the current session.
        - updateBindingSet (ubs): This argument is used to update an existing binding set with new bindings. When used with the fromContainer argument binding set entries with be replaced or merged in the binding set based on the bindings of the designated container. If the
            force flag is used, existing entries in the binding set are replaced with new values. When force is not used, only new entries are merged into the binding set, any existing entries will be left as-is. When used without a reference
            container, the binding set will be updated with placeholder entries. The template must be saved before the new binding set is permanently stored with the template file.
        - useHierarchy (uh): If true, and the fromSelection flag is set, the selection list will expand to include it's hierarchy also.
        - viewList (vl): Used in query mode, returns a list of all views defined on the template.
    """
@overload #Overload for containerTemplate in ['create']
def containerTemplate(addBindingSet: str = ..., abs: str = ..., addView: str = ..., av: str = ..., allKeyable: bool = ..., ak: bool = ..., attribute: str = ..., at: str = ..., attributeList: str = ..., al: str = ..., baseName: str = ..., bn: str = ..., bindingSetList: str = ..., bsl: str = ..., childAnchor: bool = ..., can: bool = ..., delete: bool = ..., d: bool = ..., expandCompounds: bool = ..., ec: bool = ..., fileName: str = ..., fn: str = ..., force: bool = ..., f: bool = ..., fromContainer: str = ..., fc: str = ..., fromSelection: bool = ..., fs: bool = ..., layoutMode: int = ..., lm: int = ..., parentAnchor: bool = ..., pan: bool = ..., publishedNodeList: str = ..., pnl: str = ..., removeBindingSet: str = ..., rbs: str = ..., removeView: str = ..., rv: str = ..., rootTransform: bool = ..., rtn: bool = ..., save: bool = ..., s: bool = ..., searchPath: str = ..., sp: str = ..., silent: bool = ..., si: bool = ..., unload: bool = ..., u: bool = ..., updateBindingSet: str = ..., ubs: str = ..., useHierarchy: bool = ..., uh: bool = ..., viewList: str = ..., vl: str = ...) -> None:
    """containerTemplate is NOT undoable, queryable, and editable.
    
    A container template is a description of a container's published interface.
    This command provides the ability to create and save a template file for a
    container or load an existing template file. Once a template exists, the user
    can query the template information.

    ---
    - Args:
        - addBindingSet (abs): This argument is used to add a new binding set with the given name to a template. A default binding set will be created. If the binding set already exists, the force flag must be used to replace the existing binding set. When used with the
            fromContainer option, default bindings will be entered based on the current bindings of the designated container. When used without a reference container, the binding set will be made with placeholder entries. The template must be saved
            before the new binding set is permanently stored with the template file.
        - addView (av): This argument is used to add a new view with the given name to a template. By default a view containing a flat list of all template attributes will be created.  The layoutMode flag provides more layout options. The template must be saved
            before the new view is permanently stored with the template file.
        - allKeyable (ak): Used when the fromSelection flag is true and fromContainer is false. If true we will use all keyable attributes to define the template or the view, if false we use the attributes passed in with the attribute flag.
        - attribute (at): If fromSelection is true and allKeyable is false, this attribute name will be used to create an attribute item in the template file.
        - attributeList (al): Used in query mode, returns a list of attributes contained in the template definition.
        - baseName (bn): Used in query mode, returns the base name of the template. The basename is the template name with any package qualifiers stripped off.
        - bindingSetList (bsl): Used in query mode, returns a list of all binding sets defined on the template.
        - childAnchor (can): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only childAnchor published nodes.
        - delete (d): Delete the specified template and its file. All objects that are associated with this template or contained in the same template file will be deleted. To simply unload a template without permanently deleting its file, use unload instead.
        - expandCompounds (ec): This argument is used to determine how compound parent attributes and their children will be added to generated views when both are published to the container. When true, the compound parent and all compound child attributes published to
            the container will be included in the view. When false, only the parent attribute is included in the view. Note: if only the child attributes are published and not the parent, the children will be included in the view, this flag is only
            used in the situation where both parent and child attributes are published to the container. The default value is false.
        - fileName (fn): Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is
            recommended but not required that the filename and template name correspond.
        - force (f): This flag is used with some actions to allow them to proceed with an overwrite or destructive operation. When used with load, it will allow an existing template to be reloaded from a file.  When used in create mode, it will allow an
            existing template to be recreated (for example when using fromContainer argument to regenerate a template).
        - fromContainer (fc): This argument is used in create or edit mode to specify a container node to be used for generating the template contents. In template creation mode, the template definition will be created based on the list of published attributes in the
            specified container. In edit mode, when used with the addNames flag or with no other flag, any published name on the container not present as an attribute on the template will be added to the template. This flag is also used in conjunction
            with flags such as addView.
        - fromSelection (fs): If true, we will use the active selection list to create the template or the view. If allKeyable is also true then we will create the template from all keyable attributes in the selection, otherwise we will create the template using the
            attributes specified with the attribute flag.
        - layoutMode (lm): This argument is used to specify the layout mode when creating a view. Values correspond as follows: 0: layout in flat list (default when not creating view from container) 1: layout grouped by node (default if creating view from container)
            The fromContainer or fromSelection argument is required to provide the reference container or selection for layout modes that require node information.  Note that views can only refer to defined template attributes. This means that when
            using the fromContainer or from Selection flag to add a view to an existing template, only attributes that are defined on both the template and the container or the current selection will be included in the view (i.e. published attributes
            on the container that are not defined in the template will be ignored).
        - parentAnchor (pan): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only parentAnchor published nodes.
        - publishedNodeList (pnl): Used in query mode, returns a list of published nodes contained in the template definition. By default all published nodes on the template will be returned. The list of published nodes can be limited to only include certain types of
            published nodes using one of the childAnchor, parentAnchor or rootTransform flags. If an optional flag is are specified, only nodes of the specified type will be returned.
        - removeBindingSet (rbs): This argument is used to remove the named binding set from the template. The template must be saved before the binding set is permanently removed from the template file.
        - removeView (rv): This argument is used to remove the named view from the template. The template must be saved before the view is permanently removed from the template file.
        - rootTransform (rtn): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only rootTransform published nodes.
        - save (s): Save the specified template to a file. If a filename is specified for the template, the entire file (and all templates associated with it) will be saved. If no file name is specified, a default filename will be assumed, based on the
            template name.
        - searchPath (sp): The template searchPath is an ordered list of all locations that are being searched to locate template files (first location searched to last location searched). The template search path setting is stored in the current workspace and can
            also be set and queried as the file rule entry for 'templates' (see the workspace command for more information). In edit mode, this flag allows the search path setting to be customized. When setting the search path value, the list should
            conform to a path list format expected on the current platform.  This means that paths should be separated by a semicolon (;) on Windows and a colon (:) on Linux and MacOSX. Environment variables can also be used. Additional built-in paths
            may be added automatically by maya to the customized settings. In query mode, this flag returns the current contents of the search path; all paths, both customized and built-in, will be included in the query return value.
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - unload (u): Unload the specified template.  This action will not delete the associated template file if one exists, it merely removes the template definition from the current session.
        - updateBindingSet (ubs): This argument is used to update an existing binding set with new bindings. When used with the fromContainer argument binding set entries with be replaced or merged in the binding set based on the bindings of the designated container. If the
            force flag is used, existing entries in the binding set are replaced with new values. When force is not used, only new entries are merged into the binding set, any existing entries will be left as-is. When used without a reference
            container, the binding set will be updated with placeholder entries. The template must be saved before the new binding set is permanently stored with the template file.
        - useHierarchy (uh): If true, and the fromSelection flag is set, the selection list will expand to include it's hierarchy also.
        - viewList (vl): Used in query mode, returns a list of all views defined on the template.
    """
@overload #Overload for containerTemplate in ['query']
def containerTemplate(addBindingSet: str = ..., addView: str = ..., allKeyable: bool = ..., attribute: str = ..., attributeList: str = ..., baseName: str = ..., bindingSetList: str = ..., childAnchor: bool = ..., exists: bool = ..., expandCompounds: bool = ..., fileName: str = ..., fromSelection: bool = ..., matchFile: str = ..., matchName: str = ..., parentAnchor: bool = ..., publishedNodeList: str = ..., removeBindingSet: str = ..., removeView: str = ..., rootTransform: bool = ..., searchPath: str = ..., silent: bool = ..., templateList: str = ..., updateBindingSet: str = ..., useHierarchy: bool = ..., viewList: str = ..., query: bool = ...) -> None:
    """containerTemplate is NOT undoable, queryable, and editable.
    
    A container template is a description of a container's published interface.
    This command provides the ability to create and save a template file for a
    container or load an existing template file. Once a template exists, the user
    can query the template information.

    ---
    - Args:
        - addBindingSet (abs): This argument is used to add a new binding set with the given name to a template. A default binding set will be created. If the binding set already exists, the force flag must be used to replace the existing binding set. When used with the
            fromContainer option, default bindings will be entered based on the current bindings of the designated container. When used without a reference container, the binding set will be made with placeholder entries. The template must be saved
            before the new binding set is permanently stored with the template file.
        - addView (av): This argument is used to add a new view with the given name to a template. By default a view containing a flat list of all template attributes will be created.  The layoutMode flag provides more layout options. The template must be saved
            before the new view is permanently stored with the template file.
        - allKeyable (ak): Used when the fromSelection flag is true and fromContainer is false. If true we will use all keyable attributes to define the template or the view, if false we use the attributes passed in with the attribute flag.
        - attribute (at): If fromSelection is true and allKeyable is false, this attribute name will be used to create an attribute item in the template file.
        - attributeList (al): Used in query mode, returns a list of attributes contained in the template definition.
        - baseName (bn): Used in query mode, returns the base name of the template. The basename is the template name with any package qualifiers stripped off.
        - bindingSetList (bsl): Used in query mode, returns a list of all binding sets defined on the template.
        - childAnchor (can): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only childAnchor published nodes.
        - exists (ex): Returns true or false depending upon whether the specified template exists. When used with the matchFile argument, the query will return true if the template exists and the filename it was loaded from matches the filename given.
        - expandCompounds (ec): This argument is used to determine how compound parent attributes and their children will be added to generated views when both are published to the container. When true, the compound parent and all compound child attributes published to
            the container will be included in the view. When false, only the parent attribute is included in the view. Note: if only the child attributes are published and not the parent, the children will be included in the view, this flag is only
            used in the situation where both parent and child attributes are published to the container. The default value is false.
        - fileName (fn): Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is
            recommended but not required that the filename and template name correspond.
        - fromSelection (fs): If true, we will use the active selection list to create the template or the view. If allKeyable is also true then we will create the template from all keyable attributes in the selection, otherwise we will create the template using the
            attributes specified with the attribute flag.
        - matchFile (mf): Used in query mode in conjunction with other flags this flag specifies an optional file name that is to be matched as part of the query operation.In query mode, this flag needs a value.
        - matchName (mn): Used in query mode in conjunction with other flags this flag specifies an optional template name that is to be matched as part of the query operation. The base template name is used for matching, any template with the same basename will be
            matched even across different packages.In query mode, this flag needs a value.
        - parentAnchor (pan): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only parentAnchor published nodes.
        - publishedNodeList (pnl): Used in query mode, returns a list of published nodes contained in the template definition. By default all published nodes on the template will be returned. The list of published nodes can be limited to only include certain types of
            published nodes using one of the childAnchor, parentAnchor or rootTransform flags. If an optional flag is are specified, only nodes of the specified type will be returned.
        - removeBindingSet (rbs): This argument is used to remove the named binding set from the template. The template must be saved before the binding set is permanently removed from the template file.
        - removeView (rv): This argument is used to remove the named view from the template. The template must be saved before the view is permanently removed from the template file.
        - rootTransform (rtn): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only rootTransform published nodes.
        - searchPath (sp): The template searchPath is an ordered list of all locations that are being searched to locate template files (first location searched to last location searched). The template search path setting is stored in the current workspace and can
            also be set and queried as the file rule entry for 'templates' (see the workspace command for more information). In edit mode, this flag allows the search path setting to be customized. When setting the search path value, the list should
            conform to a path list format expected on the current platform.  This means that paths should be separated by a semicolon (;) on Windows and a colon (:) on Linux and MacOSX. Environment variables can also be used. Additional built-in paths
            may be added automatically by maya to the customized settings. In query mode, this flag returns the current contents of the search path; all paths, both customized and built-in, will be included in the query return value.
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - templateList (tl): Used in query mode, returns a list of all loaded templates. This query can be used with optional matchFile and matchName flags. When used with the matchFile flag, the list of templates will be restricted to those associated with the
            specified file.  When used with the matchName flag, the list of templates will be restricted to those matching the specified template name.
        - updateBindingSet (ubs): This argument is used to update an existing binding set with new bindings. When used with the fromContainer argument binding set entries with be replaced or merged in the binding set based on the bindings of the designated container. If the
            force flag is used, existing entries in the binding set are replaced with new values. When force is not used, only new entries are merged into the binding set, any existing entries will be left as-is. When used without a reference
            container, the binding set will be updated with placeholder entries. The template must be saved before the new binding set is permanently stored with the template file.
        - useHierarchy (uh): If true, and the fromSelection flag is set, the selection list will expand to include it's hierarchy also.
        - viewList (vl): Used in query mode, returns a list of all views defined on the template.
        - query (q): Query mode flag
    """
@overload #Overload for containerTemplate in ['query']
def containerTemplate(abs: str = ..., av: str = ..., ak: bool = ..., at: str = ..., al: str = ..., bn: str = ..., bsl: str = ..., can: bool = ..., ex: bool = ..., ec: bool = ..., fn: str = ..., fs: bool = ..., mf: str = ..., mn: str = ..., pan: bool = ..., pnl: str = ..., rbs: str = ..., rv: str = ..., rtn: bool = ..., sp: str = ..., si: bool = ..., tl: str = ..., ubs: str = ..., uh: bool = ..., vl: str = ..., q: bool = ...) -> None:
    """containerTemplate is NOT undoable, queryable, and editable.
    
    A container template is a description of a container's published interface.
    This command provides the ability to create and save a template file for a
    container or load an existing template file. Once a template exists, the user
    can query the template information.

    ---
    - Args:
        - addBindingSet (abs): This argument is used to add a new binding set with the given name to a template. A default binding set will be created. If the binding set already exists, the force flag must be used to replace the existing binding set. When used with the
            fromContainer option, default bindings will be entered based on the current bindings of the designated container. When used without a reference container, the binding set will be made with placeholder entries. The template must be saved
            before the new binding set is permanently stored with the template file.
        - addView (av): This argument is used to add a new view with the given name to a template. By default a view containing a flat list of all template attributes will be created.  The layoutMode flag provides more layout options. The template must be saved
            before the new view is permanently stored with the template file.
        - allKeyable (ak): Used when the fromSelection flag is true and fromContainer is false. If true we will use all keyable attributes to define the template or the view, if false we use the attributes passed in with the attribute flag.
        - attribute (at): If fromSelection is true and allKeyable is false, this attribute name will be used to create an attribute item in the template file.
        - attributeList (al): Used in query mode, returns a list of attributes contained in the template definition.
        - baseName (bn): Used in query mode, returns the base name of the template. The basename is the template name with any package qualifiers stripped off.
        - bindingSetList (bsl): Used in query mode, returns a list of all binding sets defined on the template.
        - childAnchor (can): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only childAnchor published nodes.
        - exists (ex): Returns true or false depending upon whether the specified template exists. When used with the matchFile argument, the query will return true if the template exists and the filename it was loaded from matches the filename given.
        - expandCompounds (ec): This argument is used to determine how compound parent attributes and their children will be added to generated views when both are published to the container. When true, the compound parent and all compound child attributes published to
            the container will be included in the view. When false, only the parent attribute is included in the view. Note: if only the child attributes are published and not the parent, the children will be included in the view, this flag is only
            used in the situation where both parent and child attributes are published to the container. The default value is false.
        - fileName (fn): Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is
            recommended but not required that the filename and template name correspond.
        - fromSelection (fs): If true, we will use the active selection list to create the template or the view. If allKeyable is also true then we will create the template from all keyable attributes in the selection, otherwise we will create the template using the
            attributes specified with the attribute flag.
        - matchFile (mf): Used in query mode in conjunction with other flags this flag specifies an optional file name that is to be matched as part of the query operation.In query mode, this flag needs a value.
        - matchName (mn): Used in query mode in conjunction with other flags this flag specifies an optional template name that is to be matched as part of the query operation. The base template name is used for matching, any template with the same basename will be
            matched even across different packages.In query mode, this flag needs a value.
        - parentAnchor (pan): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only parentAnchor published nodes.
        - publishedNodeList (pnl): Used in query mode, returns a list of published nodes contained in the template definition. By default all published nodes on the template will be returned. The list of published nodes can be limited to only include certain types of
            published nodes using one of the childAnchor, parentAnchor or rootTransform flags. If an optional flag is are specified, only nodes of the specified type will be returned.
        - removeBindingSet (rbs): This argument is used to remove the named binding set from the template. The template must be saved before the binding set is permanently removed from the template file.
        - removeView (rv): This argument is used to remove the named view from the template. The template must be saved before the view is permanently removed from the template file.
        - rootTransform (rtn): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only rootTransform published nodes.
        - searchPath (sp): The template searchPath is an ordered list of all locations that are being searched to locate template files (first location searched to last location searched). The template search path setting is stored in the current workspace and can
            also be set and queried as the file rule entry for 'templates' (see the workspace command for more information). In edit mode, this flag allows the search path setting to be customized. When setting the search path value, the list should
            conform to a path list format expected on the current platform.  This means that paths should be separated by a semicolon (;) on Windows and a colon (:) on Linux and MacOSX. Environment variables can also be used. Additional built-in paths
            may be added automatically by maya to the customized settings. In query mode, this flag returns the current contents of the search path; all paths, both customized and built-in, will be included in the query return value.
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - templateList (tl): Used in query mode, returns a list of all loaded templates. This query can be used with optional matchFile and matchName flags. When used with the matchFile flag, the list of templates will be restricted to those associated with the
            specified file.  When used with the matchName flag, the list of templates will be restricted to those matching the specified template name.
        - updateBindingSet (ubs): This argument is used to update an existing binding set with new bindings. When used with the fromContainer argument binding set entries with be replaced or merged in the binding set based on the bindings of the designated container. If the
            force flag is used, existing entries in the binding set are replaced with new values. When force is not used, only new entries are merged into the binding set, any existing entries will be left as-is. When used without a reference
            container, the binding set will be updated with placeholder entries. The template must be saved before the new binding set is permanently stored with the template file.
        - useHierarchy (uh): If true, and the fromSelection flag is set, the selection list will expand to include it's hierarchy also.
        - viewList (vl): Used in query mode, returns a list of all views defined on the template.
        - query (q): Query mode flag
    """
@overload #Overload for containerTemplate in ['query']
def containerTemplate(addBindingSet: str = ..., abs: str = ..., addView: str = ..., av: str = ..., allKeyable: bool = ..., ak: bool = ..., attribute: str = ..., at: str = ..., attributeList: str = ..., al: str = ..., baseName: str = ..., bn: str = ..., bindingSetList: str = ..., bsl: str = ..., childAnchor: bool = ..., can: bool = ..., exists: bool = ..., ex: bool = ..., expandCompounds: bool = ..., ec: bool = ..., fileName: str = ..., fn: str = ..., fromSelection: bool = ..., fs: bool = ..., matchFile: str = ..., mf: str = ..., matchName: str = ..., mn: str = ..., parentAnchor: bool = ..., pan: bool = ..., publishedNodeList: str = ..., pnl: str = ..., removeBindingSet: str = ..., rbs: str = ..., removeView: str = ..., rv: str = ..., rootTransform: bool = ..., rtn: bool = ..., searchPath: str = ..., sp: str = ..., silent: bool = ..., si: bool = ..., templateList: str = ..., tl: str = ..., updateBindingSet: str = ..., ubs: str = ..., useHierarchy: bool = ..., uh: bool = ..., viewList: str = ..., vl: str = ..., query: bool = ..., q: bool = ...) -> None:
    """containerTemplate is NOT undoable, queryable, and editable.
    
    A container template is a description of a container's published interface.
    This command provides the ability to create and save a template file for a
    container or load an existing template file. Once a template exists, the user
    can query the template information.

    ---
    - Args:
        - addBindingSet (abs): This argument is used to add a new binding set with the given name to a template. A default binding set will be created. If the binding set already exists, the force flag must be used to replace the existing binding set. When used with the
            fromContainer option, default bindings will be entered based on the current bindings of the designated container. When used without a reference container, the binding set will be made with placeholder entries. The template must be saved
            before the new binding set is permanently stored with the template file.
        - addView (av): This argument is used to add a new view with the given name to a template. By default a view containing a flat list of all template attributes will be created.  The layoutMode flag provides more layout options. The template must be saved
            before the new view is permanently stored with the template file.
        - allKeyable (ak): Used when the fromSelection flag is true and fromContainer is false. If true we will use all keyable attributes to define the template or the view, if false we use the attributes passed in with the attribute flag.
        - attribute (at): If fromSelection is true and allKeyable is false, this attribute name will be used to create an attribute item in the template file.
        - attributeList (al): Used in query mode, returns a list of attributes contained in the template definition.
        - baseName (bn): Used in query mode, returns the base name of the template. The basename is the template name with any package qualifiers stripped off.
        - bindingSetList (bsl): Used in query mode, returns a list of all binding sets defined on the template.
        - childAnchor (can): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only childAnchor published nodes.
        - exists (ex): Returns true or false depending upon whether the specified template exists. When used with the matchFile argument, the query will return true if the template exists and the filename it was loaded from matches the filename given.
        - expandCompounds (ec): This argument is used to determine how compound parent attributes and their children will be added to generated views when both are published to the container. When true, the compound parent and all compound child attributes published to
            the container will be included in the view. When false, only the parent attribute is included in the view. Note: if only the child attributes are published and not the parent, the children will be included in the view, this flag is only
            used in the situation where both parent and child attributes are published to the container. The default value is false.
        - fileName (fn): Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is
            recommended but not required that the filename and template name correspond.
        - fromSelection (fs): If true, we will use the active selection list to create the template or the view. If allKeyable is also true then we will create the template from all keyable attributes in the selection, otherwise we will create the template using the
            attributes specified with the attribute flag.
        - matchFile (mf): Used in query mode in conjunction with other flags this flag specifies an optional file name that is to be matched as part of the query operation.In query mode, this flag needs a value.
        - matchName (mn): Used in query mode in conjunction with other flags this flag specifies an optional template name that is to be matched as part of the query operation. The base template name is used for matching, any template with the same basename will be
            matched even across different packages.In query mode, this flag needs a value.
        - parentAnchor (pan): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only parentAnchor published nodes.
        - publishedNodeList (pnl): Used in query mode, returns a list of published nodes contained in the template definition. By default all published nodes on the template will be returned. The list of published nodes can be limited to only include certain types of
            published nodes using one of the childAnchor, parentAnchor or rootTransform flags. If an optional flag is are specified, only nodes of the specified type will be returned.
        - removeBindingSet (rbs): This argument is used to remove the named binding set from the template. The template must be saved before the binding set is permanently removed from the template file.
        - removeView (rv): This argument is used to remove the named view from the template. The template must be saved before the view is permanently removed from the template file.
        - rootTransform (rtn): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only rootTransform published nodes.
        - searchPath (sp): The template searchPath is an ordered list of all locations that are being searched to locate template files (first location searched to last location searched). The template search path setting is stored in the current workspace and can
            also be set and queried as the file rule entry for 'templates' (see the workspace command for more information). In edit mode, this flag allows the search path setting to be customized. When setting the search path value, the list should
            conform to a path list format expected on the current platform.  This means that paths should be separated by a semicolon (;) on Windows and a colon (:) on Linux and MacOSX. Environment variables can also be used. Additional built-in paths
            may be added automatically by maya to the customized settings. In query mode, this flag returns the current contents of the search path; all paths, both customized and built-in, will be included in the query return value.
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - templateList (tl): Used in query mode, returns a list of all loaded templates. This query can be used with optional matchFile and matchName flags. When used with the matchFile flag, the list of templates will be restricted to those associated with the
            specified file.  When used with the matchName flag, the list of templates will be restricted to those matching the specified template name.
        - updateBindingSet (ubs): This argument is used to update an existing binding set with new bindings. When used with the fromContainer argument binding set entries with be replaced or merged in the binding set based on the bindings of the designated container. If the
            force flag is used, existing entries in the binding set are replaced with new values. When force is not used, only new entries are merged into the binding set, any existing entries will be left as-is. When used without a reference
            container, the binding set will be updated with placeholder entries. The template must be saved before the new binding set is permanently stored with the template file.
        - useHierarchy (uh): If true, and the fromSelection flag is set, the selection list will expand to include it's hierarchy also.
        - viewList (vl): Used in query mode, returns a list of all views defined on the template.
        - query (q): Query mode flag
    """
@overload #Overload for containerTemplate in ['edit']
def containerTemplate(addBindingSet: str = ..., addNames: bool = ..., addView: str = ..., allKeyable: bool = ..., attribute: str = ..., attributeList: str = ..., baseName: str = ..., bindingSetList: str = ..., childAnchor: bool = ..., expandCompounds: bool = ..., fileName: str = ..., fromSelection: bool = ..., parentAnchor: bool = ..., publishedNodeList: str = ..., removeBindingSet: str = ..., removeView: str = ..., rootTransform: bool = ..., searchPath: str = ..., silent: bool = ..., updateBindingSet: str = ..., useHierarchy: bool = ..., viewList: str = ..., edit: bool = ...) -> None:
    """containerTemplate is NOT undoable, queryable, and editable.
    
    A container template is a description of a container's published interface.
    This command provides the ability to create and save a template file for a
    container or load an existing template file. Once a template exists, the user
    can query the template information.

    ---
    - Args:
        - addBindingSet (abs): This argument is used to add a new binding set with the given name to a template. A default binding set will be created. If the binding set already exists, the force flag must be used to replace the existing binding set. When used with the
            fromContainer option, default bindings will be entered based on the current bindings of the designated container. When used without a reference container, the binding set will be made with placeholder entries. The template must be saved
            before the new binding set is permanently stored with the template file.
        - addNames (an): In edit mode, when used with the fromContainer flag, any published name on the container not present as an attribute on the template will be added to the template.
        - addView (av): This argument is used to add a new view with the given name to a template. By default a view containing a flat list of all template attributes will be created.  The layoutMode flag provides more layout options. The template must be saved
            before the new view is permanently stored with the template file.
        - allKeyable (ak): Used when the fromSelection flag is true and fromContainer is false. If true we will use all keyable attributes to define the template or the view, if false we use the attributes passed in with the attribute flag.
        - attribute (at): If fromSelection is true and allKeyable is false, this attribute name will be used to create an attribute item in the template file.
        - attributeList (al): Used in query mode, returns a list of attributes contained in the template definition.
        - baseName (bn): Used in query mode, returns the base name of the template. The basename is the template name with any package qualifiers stripped off.
        - bindingSetList (bsl): Used in query mode, returns a list of all binding sets defined on the template.
        - childAnchor (can): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only childAnchor published nodes.
        - expandCompounds (ec): This argument is used to determine how compound parent attributes and their children will be added to generated views when both are published to the container. When true, the compound parent and all compound child attributes published to
            the container will be included in the view. When false, only the parent attribute is included in the view. Note: if only the child attributes are published and not the parent, the children will be included in the view, this flag is only
            used in the situation where both parent and child attributes are published to the container. The default value is false.
        - fileName (fn): Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is
            recommended but not required that the filename and template name correspond.
        - fromSelection (fs): If true, we will use the active selection list to create the template or the view. If allKeyable is also true then we will create the template from all keyable attributes in the selection, otherwise we will create the template using the
            attributes specified with the attribute flag.
        - parentAnchor (pan): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only parentAnchor published nodes.
        - publishedNodeList (pnl): Used in query mode, returns a list of published nodes contained in the template definition. By default all published nodes on the template will be returned. The list of published nodes can be limited to only include certain types of
            published nodes using one of the childAnchor, parentAnchor or rootTransform flags. If an optional flag is are specified, only nodes of the specified type will be returned.
        - removeBindingSet (rbs): This argument is used to remove the named binding set from the template. The template must be saved before the binding set is permanently removed from the template file.
        - removeView (rv): This argument is used to remove the named view from the template. The template must be saved before the view is permanently removed from the template file.
        - rootTransform (rtn): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only rootTransform published nodes.
        - searchPath (sp): The template searchPath is an ordered list of all locations that are being searched to locate template files (first location searched to last location searched). The template search path setting is stored in the current workspace and can
            also be set and queried as the file rule entry for 'templates' (see the workspace command for more information). In edit mode, this flag allows the search path setting to be customized. When setting the search path value, the list should
            conform to a path list format expected on the current platform.  This means that paths should be separated by a semicolon (;) on Windows and a colon (:) on Linux and MacOSX. Environment variables can also be used. Additional built-in paths
            may be added automatically by maya to the customized settings. In query mode, this flag returns the current contents of the search path; all paths, both customized and built-in, will be included in the query return value.
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - updateBindingSet (ubs): This argument is used to update an existing binding set with new bindings. When used with the fromContainer argument binding set entries with be replaced or merged in the binding set based on the bindings of the designated container. If the
            force flag is used, existing entries in the binding set are replaced with new values. When force is not used, only new entries are merged into the binding set, any existing entries will be left as-is. When used without a reference
            container, the binding set will be updated with placeholder entries. The template must be saved before the new binding set is permanently stored with the template file.
        - useHierarchy (uh): If true, and the fromSelection flag is set, the selection list will expand to include it's hierarchy also.
        - viewList (vl): Used in query mode, returns a list of all views defined on the template.
        - edit (e): Edit mode flag
    """
@overload #Overload for containerTemplate in ['edit']
def containerTemplate(abs: str = ..., an: bool = ..., av: str = ..., ak: bool = ..., at: str = ..., al: str = ..., bn: str = ..., bsl: str = ..., can: bool = ..., ec: bool = ..., fn: str = ..., fs: bool = ..., pan: bool = ..., pnl: str = ..., rbs: str = ..., rv: str = ..., rtn: bool = ..., sp: str = ..., si: bool = ..., ubs: str = ..., uh: bool = ..., vl: str = ..., e: bool = ...) -> None:
    """containerTemplate is NOT undoable, queryable, and editable.
    
    A container template is a description of a container's published interface.
    This command provides the ability to create and save a template file for a
    container or load an existing template file. Once a template exists, the user
    can query the template information.

    ---
    - Args:
        - addBindingSet (abs): This argument is used to add a new binding set with the given name to a template. A default binding set will be created. If the binding set already exists, the force flag must be used to replace the existing binding set. When used with the
            fromContainer option, default bindings will be entered based on the current bindings of the designated container. When used without a reference container, the binding set will be made with placeholder entries. The template must be saved
            before the new binding set is permanently stored with the template file.
        - addNames (an): In edit mode, when used with the fromContainer flag, any published name on the container not present as an attribute on the template will be added to the template.
        - addView (av): This argument is used to add a new view with the given name to a template. By default a view containing a flat list of all template attributes will be created.  The layoutMode flag provides more layout options. The template must be saved
            before the new view is permanently stored with the template file.
        - allKeyable (ak): Used when the fromSelection flag is true and fromContainer is false. If true we will use all keyable attributes to define the template or the view, if false we use the attributes passed in with the attribute flag.
        - attribute (at): If fromSelection is true and allKeyable is false, this attribute name will be used to create an attribute item in the template file.
        - attributeList (al): Used in query mode, returns a list of attributes contained in the template definition.
        - baseName (bn): Used in query mode, returns the base name of the template. The basename is the template name with any package qualifiers stripped off.
        - bindingSetList (bsl): Used in query mode, returns a list of all binding sets defined on the template.
        - childAnchor (can): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only childAnchor published nodes.
        - expandCompounds (ec): This argument is used to determine how compound parent attributes and their children will be added to generated views when both are published to the container. When true, the compound parent and all compound child attributes published to
            the container will be included in the view. When false, only the parent attribute is included in the view. Note: if only the child attributes are published and not the parent, the children will be included in the view, this flag is only
            used in the situation where both parent and child attributes are published to the container. The default value is false.
        - fileName (fn): Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is
            recommended but not required that the filename and template name correspond.
        - fromSelection (fs): If true, we will use the active selection list to create the template or the view. If allKeyable is also true then we will create the template from all keyable attributes in the selection, otherwise we will create the template using the
            attributes specified with the attribute flag.
        - parentAnchor (pan): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only parentAnchor published nodes.
        - publishedNodeList (pnl): Used in query mode, returns a list of published nodes contained in the template definition. By default all published nodes on the template will be returned. The list of published nodes can be limited to only include certain types of
            published nodes using one of the childAnchor, parentAnchor or rootTransform flags. If an optional flag is are specified, only nodes of the specified type will be returned.
        - removeBindingSet (rbs): This argument is used to remove the named binding set from the template. The template must be saved before the binding set is permanently removed from the template file.
        - removeView (rv): This argument is used to remove the named view from the template. The template must be saved before the view is permanently removed from the template file.
        - rootTransform (rtn): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only rootTransform published nodes.
        - searchPath (sp): The template searchPath is an ordered list of all locations that are being searched to locate template files (first location searched to last location searched). The template search path setting is stored in the current workspace and can
            also be set and queried as the file rule entry for 'templates' (see the workspace command for more information). In edit mode, this flag allows the search path setting to be customized. When setting the search path value, the list should
            conform to a path list format expected on the current platform.  This means that paths should be separated by a semicolon (;) on Windows and a colon (:) on Linux and MacOSX. Environment variables can also be used. Additional built-in paths
            may be added automatically by maya to the customized settings. In query mode, this flag returns the current contents of the search path; all paths, both customized and built-in, will be included in the query return value.
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - updateBindingSet (ubs): This argument is used to update an existing binding set with new bindings. When used with the fromContainer argument binding set entries with be replaced or merged in the binding set based on the bindings of the designated container. If the
            force flag is used, existing entries in the binding set are replaced with new values. When force is not used, only new entries are merged into the binding set, any existing entries will be left as-is. When used without a reference
            container, the binding set will be updated with placeholder entries. The template must be saved before the new binding set is permanently stored with the template file.
        - useHierarchy (uh): If true, and the fromSelection flag is set, the selection list will expand to include it's hierarchy also.
        - viewList (vl): Used in query mode, returns a list of all views defined on the template.
        - edit (e): Edit mode flag
    """
@overload #Overload for containerTemplate in ['edit']
def containerTemplate(addBindingSet: str = ..., abs: str = ..., addNames: bool = ..., an: bool = ..., addView: str = ..., av: str = ..., allKeyable: bool = ..., ak: bool = ..., attribute: str = ..., at: str = ..., attributeList: str = ..., al: str = ..., baseName: str = ..., bn: str = ..., bindingSetList: str = ..., bsl: str = ..., childAnchor: bool = ..., can: bool = ..., expandCompounds: bool = ..., ec: bool = ..., fileName: str = ..., fn: str = ..., fromSelection: bool = ..., fs: bool = ..., parentAnchor: bool = ..., pan: bool = ..., publishedNodeList: str = ..., pnl: str = ..., removeBindingSet: str = ..., rbs: str = ..., removeView: str = ..., rv: str = ..., rootTransform: bool = ..., rtn: bool = ..., searchPath: str = ..., sp: str = ..., silent: bool = ..., si: bool = ..., updateBindingSet: str = ..., ubs: str = ..., useHierarchy: bool = ..., uh: bool = ..., viewList: str = ..., vl: str = ..., edit: bool = ..., e: bool = ...) -> None:
    """containerTemplate is NOT undoable, queryable, and editable.
    
    A container template is a description of a container's published interface.
    This command provides the ability to create and save a template file for a
    container or load an existing template file. Once a template exists, the user
    can query the template information.

    ---
    - Args:
        - addBindingSet (abs): This argument is used to add a new binding set with the given name to a template. A default binding set will be created. If the binding set already exists, the force flag must be used to replace the existing binding set. When used with the
            fromContainer option, default bindings will be entered based on the current bindings of the designated container. When used without a reference container, the binding set will be made with placeholder entries. The template must be saved
            before the new binding set is permanently stored with the template file.
        - addNames (an): In edit mode, when used with the fromContainer flag, any published name on the container not present as an attribute on the template will be added to the template.
        - addView (av): This argument is used to add a new view with the given name to a template. By default a view containing a flat list of all template attributes will be created.  The layoutMode flag provides more layout options. The template must be saved
            before the new view is permanently stored with the template file.
        - allKeyable (ak): Used when the fromSelection flag is true and fromContainer is false. If true we will use all keyable attributes to define the template or the view, if false we use the attributes passed in with the attribute flag.
        - attribute (at): If fromSelection is true and allKeyable is false, this attribute name will be used to create an attribute item in the template file.
        - attributeList (al): Used in query mode, returns a list of attributes contained in the template definition.
        - baseName (bn): Used in query mode, returns the base name of the template. The basename is the template name with any package qualifiers stripped off.
        - bindingSetList (bsl): Used in query mode, returns a list of all binding sets defined on the template.
        - childAnchor (can): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only childAnchor published nodes.
        - expandCompounds (ec): This argument is used to determine how compound parent attributes and their children will be added to generated views when both are published to the container. When true, the compound parent and all compound child attributes published to
            the container will be included in the view. When false, only the parent attribute is included in the view. Note: if only the child attributes are published and not the parent, the children will be included in the view, this flag is only
            used in the situation where both parent and child attributes are published to the container. The default value is false.
        - fileName (fn): Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is
            recommended but not required that the filename and template name correspond.
        - fromSelection (fs): If true, we will use the active selection list to create the template or the view. If allKeyable is also true then we will create the template from all keyable attributes in the selection, otherwise we will create the template using the
            attributes specified with the attribute flag.
        - parentAnchor (pan): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only parentAnchor published nodes.
        - publishedNodeList (pnl): Used in query mode, returns a list of published nodes contained in the template definition. By default all published nodes on the template will be returned. The list of published nodes can be limited to only include certain types of
            published nodes using one of the childAnchor, parentAnchor or rootTransform flags. If an optional flag is are specified, only nodes of the specified type will be returned.
        - removeBindingSet (rbs): This argument is used to remove the named binding set from the template. The template must be saved before the binding set is permanently removed from the template file.
        - removeView (rv): This argument is used to remove the named view from the template. The template must be saved before the view is permanently removed from the template file.
        - rootTransform (rtn): This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only rootTransform published nodes.
        - searchPath (sp): The template searchPath is an ordered list of all locations that are being searched to locate template files (first location searched to last location searched). The template search path setting is stored in the current workspace and can
            also be set and queried as the file rule entry for 'templates' (see the workspace command for more information). In edit mode, this flag allows the search path setting to be customized. When setting the search path value, the list should
            conform to a path list format expected on the current platform.  This means that paths should be separated by a semicolon (;) on Windows and a colon (:) on Linux and MacOSX. Environment variables can also be used. Additional built-in paths
            may be added automatically by maya to the customized settings. In query mode, this flag returns the current contents of the search path; all paths, both customized and built-in, will be included in the query return value.
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - updateBindingSet (ubs): This argument is used to update an existing binding set with new bindings. When used with the fromContainer argument binding set entries with be replaced or merged in the binding set based on the bindings of the designated container. If the
            force flag is used, existing entries in the binding set are replaced with new values. When force is not used, only new entries are merged into the binding set, any existing entries will be left as-is. When used without a reference
            container, the binding set will be updated with placeholder entries. The template must be saved before the new binding set is permanently stored with the template file.
        - useHierarchy (uh): If true, and the fromSelection flag is set, the selection list will expand to include it's hierarchy also.
        - viewList (vl): Used in query mode, returns a list of all views defined on the template.
        - edit (e): Edit mode flag
    """
