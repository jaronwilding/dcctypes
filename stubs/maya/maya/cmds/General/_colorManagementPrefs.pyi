"""Stub files for General category in Maya commands, command: colorManagementPrefs."""

from typing import Any, overload

@overload #Overload for colorManagementPrefs in ['create']
def colorManagementPrefs(colorManageAllNodes: bool = ..., exportPolicy: str = ..., inhibitEvents: bool = ..., loadPolicy: str = ..., refresh: bool = ..., restoreDefaults: bool = ...) -> None:
    """colorManagementPrefs is undoable, queryable, and editable.
    
    This command allows querying and editing the color management global data in a
    scene. It also allows for setting the view transform and rendering space which
    automatically configures the color processing in the enabled views.

    Example:
    ```python
        import maya.cmds as cmds
        ws = cmds.colorManagementPrefs(q=True, renderingSpaceName=True)
        cmds.colorManagementPrefs(e=True, viewTransformName="Log")
        renderingSpaces = cmd.colorManagementPrefs(q=True, renderingSpaceNames=True)
        viewingTransforms = cmd.colorManagementPrefs(q=True, viewTransformNames=True)
        cmds.colorManagementPrefs(e=True, configFilePath="/project/local_config.ocio")
    ```

    ---
    - Args:
        - colorManageAllNodes (cma): Adds color management to all input nodes such as file texture nodes
        - exportPolicy (epy): Export the color management parameters to policy file
        - inhibitEvents (ie): Inhibit client-server notifications and event triggers which occur when changing the color management settings.
        - loadPolicy (lpy): Load the color management policy file. This file overides the color management settings.
        - refresh (rfr): Refresh the color management.
        - restoreDefaults (rde): Restore the color management settings to their default value.
    """
@overload #Overload for colorManagementPrefs in ['create']
def colorManagementPrefs(cma: bool = ..., epy: str = ..., ie: bool = ..., lpy: str = ..., rfr: bool = ..., rde: bool = ...) -> None:
    """colorManagementPrefs is undoable, queryable, and editable.
    
    This command allows querying and editing the color management global data in a
    scene. It also allows for setting the view transform and rendering space which
    automatically configures the color processing in the enabled views.

    Example:
    ```python
        import maya.cmds as cmds
        ws = cmds.colorManagementPrefs(q=True, renderingSpaceName=True)
        cmds.colorManagementPrefs(e=True, viewTransformName="Log")
        renderingSpaces = cmd.colorManagementPrefs(q=True, renderingSpaceNames=True)
        viewingTransforms = cmd.colorManagementPrefs(q=True, viewTransformNames=True)
        cmds.colorManagementPrefs(e=True, configFilePath="/project/local_config.ocio")
    ```

    ---
    - Args:
        - colorManageAllNodes (cma): Adds color management to all input nodes such as file texture nodes
        - exportPolicy (epy): Export the color management parameters to policy file
        - inhibitEvents (ie): Inhibit client-server notifications and event triggers which occur when changing the color management settings.
        - loadPolicy (lpy): Load the color management policy file. This file overides the color management settings.
        - refresh (rfr): Refresh the color management.
        - restoreDefaults (rde): Restore the color management settings to their default value.
    """
@overload #Overload for colorManagementPrefs in ['create']
def colorManagementPrefs(colorManageAllNodes: bool = ..., cma: bool = ..., exportPolicy: str = ..., epy: str = ..., inhibitEvents: bool = ..., ie: bool = ..., loadPolicy: str = ..., lpy: str = ..., refresh: bool = ..., rfr: bool = ..., restoreDefaults: bool = ..., rde: bool = ...) -> None:
    """colorManagementPrefs is undoable, queryable, and editable.
    
    This command allows querying and editing the color management global data in a
    scene. It also allows for setting the view transform and rendering space which
    automatically configures the color processing in the enabled views.

    Example:
    ```python
        import maya.cmds as cmds
        ws = cmds.colorManagementPrefs(q=True, renderingSpaceName=True)
        cmds.colorManagementPrefs(e=True, viewTransformName="Log")
        renderingSpaces = cmd.colorManagementPrefs(q=True, renderingSpaceNames=True)
        viewingTransforms = cmd.colorManagementPrefs(q=True, viewTransformNames=True)
        cmds.colorManagementPrefs(e=True, configFilePath="/project/local_config.ocio")
    ```

    ---
    - Args:
        - colorManageAllNodes (cma): Adds color management to all input nodes such as file texture nodes
        - exportPolicy (epy): Export the color management parameters to policy file
        - inhibitEvents (ie): Inhibit client-server notifications and event triggers which occur when changing the color management settings.
        - loadPolicy (lpy): Load the color management policy file. This file overides the color management settings.
        - refresh (rfr): Refresh the color management.
        - restoreDefaults (rde): Restore the color management settings to their default value.
    """
@overload #Overload for colorManagementPrefs in ['query']
def colorManagementPrefs(cmConfigFileEnabled: bool = ..., cmEnabled: bool = ..., colorManagePots: bool = ..., colorManagedNodes: bool = ..., colorManagementSDKVersion: str = ..., configFilePath: str = ..., configFileVersion: str = ..., defaultInputSpaceName: str = ..., displayName: str = ..., displayNames: bool = ..., equalsToPolicyFile: str = ..., inputSpaceDescription: str = ..., inputSpaceFamilies: str = ..., inputSpaceNames: bool = ..., loadedDefaultInputSpaceName: str = ..., loadedDisplayName: str = ..., loadedOutputTransformName: str = ..., loadedRenderingSpaceName: str = ..., loadedViewName: str = ..., loadedViewTransformName: str = ..., missingColorSpaceNodes: bool = ..., ocioRulesEnabled: bool = ..., ociov2Enabled: bool = ..., outputTarget: str = ..., outputTransformEnabled: bool = ..., outputTransformName: str = ..., outputTransformNames: bool = ..., outputTransformUseColorConversion: bool = ..., outputUseViewTransform: bool = ..., policyFileName: str = ..., renderingSpaceName: str = ..., renderingSpaceNames: bool = ..., viewDisplayNames: str = ..., viewName: str = ..., viewNames: bool = ..., viewTransformName: str = ..., viewTransformNames: bool = ..., query: bool = ...) -> None:
    """colorManagementPrefs is undoable, queryable, and editable.
    
    This command allows querying and editing the color management global data in a
    scene. It also allows for setting the view transform and rendering space which
    automatically configures the color processing in the enabled views.

    Example:
    ```python
        import maya.cmds as cmds
        ws = cmds.colorManagementPrefs(q=True, renderingSpaceName=True)
        cmds.colorManagementPrefs(e=True, viewTransformName="Log")
        renderingSpaces = cmd.colorManagementPrefs(q=True, renderingSpaceNames=True)
        viewingTransforms = cmd.colorManagementPrefs(q=True, viewTransformNames=True)
        cmds.colorManagementPrefs(e=True, configFilePath="/project/local_config.ocio")
    ```

    ---
    - Args:
        - cmConfigFileEnabled (cfe): Turn on or off applying an OCIO configuration file.  If set, the color management configuration set in the preferences is used.
        - cmEnabled (cme): Turn on or off color management in general.  If set, the color management configuration set in the preferences is used.
        - colorManagePots (cmp): Turn on or off color management of color pots in the UI.  If set, colors in color pots are taken to be in rendering space, and are displayed after being transformed by the view transform set in the preferences.
        - colorManagedNodes (cmn): Gets the names of all nodes that apply color management to bring pixels from an input color space to the rendering space. Examples include file texture node.
        - colorManagementSDKVersion (cmv): Obtain the version of the color management SDK used by Maya.
        - configFilePath (cfp): The configuration file to be used, if color management is enabled.
        - configFileVersion (cfv): Obtain the version of the config version.
        - defaultInputSpaceName (din): This flag is obsolete.  See the colorManagementFileRules command for more information.
        - displayName (dn): The display from the (display, view) pair, to be applied by color managed viewers and color managed UI controls.
        - displayNames (dns): Returns the list of available displays.  Used to populate the color management preference UI popup.
        - equalsToPolicyFile (etp): Query if the current loaded policy settings is the same with the settings described in the policy file which is the argument of the command.In query mode, this flag needs a value.
        - inputSpaceDescription (isd): Returns the description for a specific input color space.In query mode, this flag needs a value.
        - inputSpaceFamilies (isf): Returns the list of families for a specific input color space. Used to add submenus when populating the input color spaces UI popup.In query mode, this flag needs a value.
        - inputSpaceNames (iss): Returns the list of available input color spaces. Used to populate the input color spaces UI popup.
        - loadedDefaultInputSpaceName (ldn): This flag is obsolete.
        - loadedDisplayName (ld): Gets the loaded display from the (display, view) pair.  Used by file open, import, and reference to check for missing color spaces or transforms.
        - loadedOutputTransformName (lon): Gets the loaded output transform.  Used by file open, import, and reference to check for missing color spaces or transforms.
        - loadedRenderingSpaceName (lrn): Gets the loaded rendering space.  Used by file open, import, and reference to check for missing color spaces or transforms.
        - loadedViewName (lv): Gets the loaded view from the (display, view) pair.  Used by file open, import, and reference to check for missing color spaces or transforms.
        - loadedViewTransformName (lvn): Gets the loaded view transform.  Used by file open, import, and reference to check for missing color spaces or transforms.
        - missingColorSpaceNodes (mcn): Gets the names of the nodes that have color spaces not defined in the selected transform collection or in the selected config file. Note that an inactive color space is not a missing color space.
        - ocioRulesEnabled (ore): Turn on or off the use of colorspace assignment rules from the OCIO library.
        - ociov2Enabled (oci): Is OCIOv2 the colour management system by default.
        - outputTarget (ott): Indicates to which output the outputTransformEnabled or the outputTransformName flags are to be applied. Valid values are "renderer" or "playblast".In query mode, this flag needs a value.
        - outputTransformEnabled (ote): Turn on or off applying the output transform for out of viewport renders. If set, the output transform set in the preferences is used.
        - outputTransformName (otn): The output transform to be applied for out of viewport renders.  Disables output use view transform mode.
        - outputTransformNames (ots): Returns the list of available output transforms.
        - outputTransformUseColorConversion (otc): Turn on or off selecting the color space conversion for the output color space of viewport renders.  If set, a conversion color space is used; otherwise, a view transform is used.
        - outputUseViewTransform (ovt): Turns use view transform mode on.  In this mode, the output transform is set to match the view transform.  To turn the mode off, set an output transform using the outputTransformName flag.
        - policyFileName (pfn): Set the policy file name
        - renderingSpaceName (rsn): The color space to be used during rendering.  This is the source color space to the viewing transform, for color managed viewers and color managed UI controls, and the destination color space for color managed input pixels.
        - renderingSpaceNames (rss): Returns the list of available rendering spaces.  Used to populate the color management preference UI popup.
        - viewDisplayNames (vds): Returns the list of available views for a specific display. Used to populate the view name list UI for file and image plane nodes.In query mode, this flag needs a value.
        - viewName (vn): The view from the (display, view) pair, to be applied by color managed viewers and color managed UI controls.
        - viewNames (vns): Returns the list of available views from the selected display.  Used to populate the color management preference UI popup.
        - viewTransformName (vtn): The view transform to be applied by color managed viewers and color managed UI controls.
        - viewTransformNames (vts): Returns the list of available view transforms.  Used to populate the color management preference UI popup.
        - query (q): Query mode flag
    """
@overload #Overload for colorManagementPrefs in ['query']
def colorManagementPrefs(cfe: bool = ..., cme: bool = ..., cmp: bool = ..., cmn: bool = ..., cmv: str = ..., cfp: str = ..., cfv: str = ..., din: str = ..., dn: str = ..., dns: bool = ..., etp: str = ..., isd: str = ..., isf: str = ..., iss: bool = ..., ldn: str = ..., ld: str = ..., lon: str = ..., lrn: str = ..., lv: str = ..., lvn: str = ..., mcn: bool = ..., ore: bool = ..., oci: bool = ..., ott: str = ..., ote: bool = ..., otn: str = ..., ots: bool = ..., otc: bool = ..., ovt: bool = ..., pfn: str = ..., rsn: str = ..., rss: bool = ..., vds: str = ..., vn: str = ..., vns: bool = ..., vtn: str = ..., vts: bool = ..., q: bool = ...) -> None:
    """colorManagementPrefs is undoable, queryable, and editable.
    
    This command allows querying and editing the color management global data in a
    scene. It also allows for setting the view transform and rendering space which
    automatically configures the color processing in the enabled views.

    Example:
    ```python
        import maya.cmds as cmds
        ws = cmds.colorManagementPrefs(q=True, renderingSpaceName=True)
        cmds.colorManagementPrefs(e=True, viewTransformName="Log")
        renderingSpaces = cmd.colorManagementPrefs(q=True, renderingSpaceNames=True)
        viewingTransforms = cmd.colorManagementPrefs(q=True, viewTransformNames=True)
        cmds.colorManagementPrefs(e=True, configFilePath="/project/local_config.ocio")
    ```

    ---
    - Args:
        - cmConfigFileEnabled (cfe): Turn on or off applying an OCIO configuration file.  If set, the color management configuration set in the preferences is used.
        - cmEnabled (cme): Turn on or off color management in general.  If set, the color management configuration set in the preferences is used.
        - colorManagePots (cmp): Turn on or off color management of color pots in the UI.  If set, colors in color pots are taken to be in rendering space, and are displayed after being transformed by the view transform set in the preferences.
        - colorManagedNodes (cmn): Gets the names of all nodes that apply color management to bring pixels from an input color space to the rendering space. Examples include file texture node.
        - colorManagementSDKVersion (cmv): Obtain the version of the color management SDK used by Maya.
        - configFilePath (cfp): The configuration file to be used, if color management is enabled.
        - configFileVersion (cfv): Obtain the version of the config version.
        - defaultInputSpaceName (din): This flag is obsolete.  See the colorManagementFileRules command for more information.
        - displayName (dn): The display from the (display, view) pair, to be applied by color managed viewers and color managed UI controls.
        - displayNames (dns): Returns the list of available displays.  Used to populate the color management preference UI popup.
        - equalsToPolicyFile (etp): Query if the current loaded policy settings is the same with the settings described in the policy file which is the argument of the command.In query mode, this flag needs a value.
        - inputSpaceDescription (isd): Returns the description for a specific input color space.In query mode, this flag needs a value.
        - inputSpaceFamilies (isf): Returns the list of families for a specific input color space. Used to add submenus when populating the input color spaces UI popup.In query mode, this flag needs a value.
        - inputSpaceNames (iss): Returns the list of available input color spaces. Used to populate the input color spaces UI popup.
        - loadedDefaultInputSpaceName (ldn): This flag is obsolete.
        - loadedDisplayName (ld): Gets the loaded display from the (display, view) pair.  Used by file open, import, and reference to check for missing color spaces or transforms.
        - loadedOutputTransformName (lon): Gets the loaded output transform.  Used by file open, import, and reference to check for missing color spaces or transforms.
        - loadedRenderingSpaceName (lrn): Gets the loaded rendering space.  Used by file open, import, and reference to check for missing color spaces or transforms.
        - loadedViewName (lv): Gets the loaded view from the (display, view) pair.  Used by file open, import, and reference to check for missing color spaces or transforms.
        - loadedViewTransformName (lvn): Gets the loaded view transform.  Used by file open, import, and reference to check for missing color spaces or transforms.
        - missingColorSpaceNodes (mcn): Gets the names of the nodes that have color spaces not defined in the selected transform collection or in the selected config file. Note that an inactive color space is not a missing color space.
        - ocioRulesEnabled (ore): Turn on or off the use of colorspace assignment rules from the OCIO library.
        - ociov2Enabled (oci): Is OCIOv2 the colour management system by default.
        - outputTarget (ott): Indicates to which output the outputTransformEnabled or the outputTransformName flags are to be applied. Valid values are "renderer" or "playblast".In query mode, this flag needs a value.
        - outputTransformEnabled (ote): Turn on or off applying the output transform for out of viewport renders. If set, the output transform set in the preferences is used.
        - outputTransformName (otn): The output transform to be applied for out of viewport renders.  Disables output use view transform mode.
        - outputTransformNames (ots): Returns the list of available output transforms.
        - outputTransformUseColorConversion (otc): Turn on or off selecting the color space conversion for the output color space of viewport renders.  If set, a conversion color space is used; otherwise, a view transform is used.
        - outputUseViewTransform (ovt): Turns use view transform mode on.  In this mode, the output transform is set to match the view transform.  To turn the mode off, set an output transform using the outputTransformName flag.
        - policyFileName (pfn): Set the policy file name
        - renderingSpaceName (rsn): The color space to be used during rendering.  This is the source color space to the viewing transform, for color managed viewers and color managed UI controls, and the destination color space for color managed input pixels.
        - renderingSpaceNames (rss): Returns the list of available rendering spaces.  Used to populate the color management preference UI popup.
        - viewDisplayNames (vds): Returns the list of available views for a specific display. Used to populate the view name list UI for file and image plane nodes.In query mode, this flag needs a value.
        - viewName (vn): The view from the (display, view) pair, to be applied by color managed viewers and color managed UI controls.
        - viewNames (vns): Returns the list of available views from the selected display.  Used to populate the color management preference UI popup.
        - viewTransformName (vtn): The view transform to be applied by color managed viewers and color managed UI controls.
        - viewTransformNames (vts): Returns the list of available view transforms.  Used to populate the color management preference UI popup.
        - query (q): Query mode flag
    """
@overload #Overload for colorManagementPrefs in ['query']
def colorManagementPrefs(cmConfigFileEnabled: bool = ..., cfe: bool = ..., cmEnabled: bool = ..., cme: bool = ..., colorManagePots: bool = ..., cmp: bool = ..., colorManagedNodes: bool = ..., cmn: bool = ..., colorManagementSDKVersion: str = ..., cmv: str = ..., configFilePath: str = ..., cfp: str = ..., configFileVersion: str = ..., cfv: str = ..., defaultInputSpaceName: str = ..., din: str = ..., displayName: str = ..., dn: str = ..., displayNames: bool = ..., dns: bool = ..., equalsToPolicyFile: str = ..., etp: str = ..., inputSpaceDescription: str = ..., isd: str = ..., inputSpaceFamilies: str = ..., isf: str = ..., inputSpaceNames: bool = ..., iss: bool = ..., loadedDefaultInputSpaceName: str = ..., ldn: str = ..., loadedDisplayName: str = ..., ld: str = ..., loadedOutputTransformName: str = ..., lon: str = ..., loadedRenderingSpaceName: str = ..., lrn: str = ..., loadedViewName: str = ..., lv: str = ..., loadedViewTransformName: str = ..., lvn: str = ..., missingColorSpaceNodes: bool = ..., mcn: bool = ..., ocioRulesEnabled: bool = ..., ore: bool = ..., ociov2Enabled: bool = ..., oci: bool = ..., outputTarget: str = ..., ott: str = ..., outputTransformEnabled: bool = ..., ote: bool = ..., outputTransformName: str = ..., otn: str = ..., outputTransformNames: bool = ..., ots: bool = ..., outputTransformUseColorConversion: bool = ..., otc: bool = ..., outputUseViewTransform: bool = ..., ovt: bool = ..., policyFileName: str = ..., pfn: str = ..., renderingSpaceName: str = ..., rsn: str = ..., renderingSpaceNames: bool = ..., rss: bool = ..., viewDisplayNames: str = ..., vds: str = ..., viewName: str = ..., vn: str = ..., viewNames: bool = ..., vns: bool = ..., viewTransformName: str = ..., vtn: str = ..., viewTransformNames: bool = ..., vts: bool = ..., query: bool = ..., q: bool = ...) -> None:
    """colorManagementPrefs is undoable, queryable, and editable.
    
    This command allows querying and editing the color management global data in a
    scene. It also allows for setting the view transform and rendering space which
    automatically configures the color processing in the enabled views.

    Example:
    ```python
        import maya.cmds as cmds
        ws = cmds.colorManagementPrefs(q=True, renderingSpaceName=True)
        cmds.colorManagementPrefs(e=True, viewTransformName="Log")
        renderingSpaces = cmd.colorManagementPrefs(q=True, renderingSpaceNames=True)
        viewingTransforms = cmd.colorManagementPrefs(q=True, viewTransformNames=True)
        cmds.colorManagementPrefs(e=True, configFilePath="/project/local_config.ocio")
    ```

    ---
    - Args:
        - cmConfigFileEnabled (cfe): Turn on or off applying an OCIO configuration file.  If set, the color management configuration set in the preferences is used.
        - cmEnabled (cme): Turn on or off color management in general.  If set, the color management configuration set in the preferences is used.
        - colorManagePots (cmp): Turn on or off color management of color pots in the UI.  If set, colors in color pots are taken to be in rendering space, and are displayed after being transformed by the view transform set in the preferences.
        - colorManagedNodes (cmn): Gets the names of all nodes that apply color management to bring pixels from an input color space to the rendering space. Examples include file texture node.
        - colorManagementSDKVersion (cmv): Obtain the version of the color management SDK used by Maya.
        - configFilePath (cfp): The configuration file to be used, if color management is enabled.
        - configFileVersion (cfv): Obtain the version of the config version.
        - defaultInputSpaceName (din): This flag is obsolete.  See the colorManagementFileRules command for more information.
        - displayName (dn): The display from the (display, view) pair, to be applied by color managed viewers and color managed UI controls.
        - displayNames (dns): Returns the list of available displays.  Used to populate the color management preference UI popup.
        - equalsToPolicyFile (etp): Query if the current loaded policy settings is the same with the settings described in the policy file which is the argument of the command.In query mode, this flag needs a value.
        - inputSpaceDescription (isd): Returns the description for a specific input color space.In query mode, this flag needs a value.
        - inputSpaceFamilies (isf): Returns the list of families for a specific input color space. Used to add submenus when populating the input color spaces UI popup.In query mode, this flag needs a value.
        - inputSpaceNames (iss): Returns the list of available input color spaces. Used to populate the input color spaces UI popup.
        - loadedDefaultInputSpaceName (ldn): This flag is obsolete.
        - loadedDisplayName (ld): Gets the loaded display from the (display, view) pair.  Used by file open, import, and reference to check for missing color spaces or transforms.
        - loadedOutputTransformName (lon): Gets the loaded output transform.  Used by file open, import, and reference to check for missing color spaces or transforms.
        - loadedRenderingSpaceName (lrn): Gets the loaded rendering space.  Used by file open, import, and reference to check for missing color spaces or transforms.
        - loadedViewName (lv): Gets the loaded view from the (display, view) pair.  Used by file open, import, and reference to check for missing color spaces or transforms.
        - loadedViewTransformName (lvn): Gets the loaded view transform.  Used by file open, import, and reference to check for missing color spaces or transforms.
        - missingColorSpaceNodes (mcn): Gets the names of the nodes that have color spaces not defined in the selected transform collection or in the selected config file. Note that an inactive color space is not a missing color space.
        - ocioRulesEnabled (ore): Turn on or off the use of colorspace assignment rules from the OCIO library.
        - ociov2Enabled (oci): Is OCIOv2 the colour management system by default.
        - outputTarget (ott): Indicates to which output the outputTransformEnabled or the outputTransformName flags are to be applied. Valid values are "renderer" or "playblast".In query mode, this flag needs a value.
        - outputTransformEnabled (ote): Turn on or off applying the output transform for out of viewport renders. If set, the output transform set in the preferences is used.
        - outputTransformName (otn): The output transform to be applied for out of viewport renders.  Disables output use view transform mode.
        - outputTransformNames (ots): Returns the list of available output transforms.
        - outputTransformUseColorConversion (otc): Turn on or off selecting the color space conversion for the output color space of viewport renders.  If set, a conversion color space is used; otherwise, a view transform is used.
        - outputUseViewTransform (ovt): Turns use view transform mode on.  In this mode, the output transform is set to match the view transform.  To turn the mode off, set an output transform using the outputTransformName flag.
        - policyFileName (pfn): Set the policy file name
        - renderingSpaceName (rsn): The color space to be used during rendering.  This is the source color space to the viewing transform, for color managed viewers and color managed UI controls, and the destination color space for color managed input pixels.
        - renderingSpaceNames (rss): Returns the list of available rendering spaces.  Used to populate the color management preference UI popup.
        - viewDisplayNames (vds): Returns the list of available views for a specific display. Used to populate the view name list UI for file and image plane nodes.In query mode, this flag needs a value.
        - viewName (vn): The view from the (display, view) pair, to be applied by color managed viewers and color managed UI controls.
        - viewNames (vns): Returns the list of available views from the selected display.  Used to populate the color management preference UI popup.
        - viewTransformName (vtn): The view transform to be applied by color managed viewers and color managed UI controls.
        - viewTransformNames (vts): Returns the list of available view transforms.  Used to populate the color management preference UI popup.
        - query (q): Query mode flag
    """
@overload #Overload for colorManagementPrefs in ['edit']
def colorManagementPrefs(cmConfigFileEnabled: bool = ..., cmEnabled: bool = ..., colorManagePots: bool = ..., configFilePath: str = ..., defaultInputSpaceName: str = ..., displayName: str = ..., ocioRulesEnabled: bool = ..., outputTarget: str = ..., outputTransformEnabled: bool = ..., outputTransformName: str = ..., outputTransformUseColorConversion: bool = ..., outputUseViewTransform: bool = ..., policyFileName: str = ..., popupOnError: bool = ..., renderingSpaceName: str = ..., viewName: str = ..., viewTransformName: str = ..., edit: bool = ...) -> None:
    """colorManagementPrefs is undoable, queryable, and editable.
    
    This command allows querying and editing the color management global data in a
    scene. It also allows for setting the view transform and rendering space which
    automatically configures the color processing in the enabled views.

    Example:
    ```python
        import maya.cmds as cmds
        ws = cmds.colorManagementPrefs(q=True, renderingSpaceName=True)
        cmds.colorManagementPrefs(e=True, viewTransformName="Log")
        renderingSpaces = cmd.colorManagementPrefs(q=True, renderingSpaceNames=True)
        viewingTransforms = cmd.colorManagementPrefs(q=True, viewTransformNames=True)
        cmds.colorManagementPrefs(e=True, configFilePath="/project/local_config.ocio")
    ```

    ---
    - Args:
        - cmConfigFileEnabled (cfe): Turn on or off applying an OCIO configuration file.  If set, the color management configuration set in the preferences is used.
        - cmEnabled (cme): Turn on or off color management in general.  If set, the color management configuration set in the preferences is used.
        - colorManagePots (cmp): Turn on or off color management of color pots in the UI.  If set, colors in color pots are taken to be in rendering space, and are displayed after being transformed by the view transform set in the preferences.
        - configFilePath (cfp): The configuration file to be used, if color management is enabled.
        - defaultInputSpaceName (din): This flag is obsolete.  See the colorManagementFileRules command for more information.
        - displayName (dn): The display from the (display, view) pair, to be applied by color managed viewers and color managed UI controls.
        - ocioRulesEnabled (ore): Turn on or off the use of colorspace assignment rules from the OCIO library.
        - outputTarget (ott): Indicates to which output the outputTransformEnabled or the outputTransformName flags are to be applied. Valid values are "renderer" or "playblast".In query mode, this flag needs a value.
        - outputTransformEnabled (ote): Turn on or off applying the output transform for out of viewport renders. If set, the output transform set in the preferences is used.
        - outputTransformName (otn): The output transform to be applied for out of viewport renders.  Disables output use view transform mode.
        - outputTransformUseColorConversion (otc): Turn on or off selecting the color space conversion for the output color space of viewport renders.  If set, a conversion color space is used; otherwise, a view transform is used.
        - outputUseViewTransform (ovt): Turns use view transform mode on.  In this mode, the output transform is set to match the view transform.  To turn the mode off, set an output transform using the outputTransformName flag.
        - policyFileName (pfn): Set the policy file name
        - popupOnError (poe): Turn on or off displaying a modal popup on error (as well as the normal script editor reporting of the error), for this invocation of the command.  Default is off.
        - renderingSpaceName (rsn): The color space to be used during rendering.  This is the source color space to the viewing transform, for color managed viewers and color managed UI controls, and the destination color space for color managed input pixels.
        - viewName (vn): The view from the (display, view) pair, to be applied by color managed viewers and color managed UI controls.
        - viewTransformName (vtn): The view transform to be applied by color managed viewers and color managed UI controls.
        - edit (e): Edit mode flag
    """
@overload #Overload for colorManagementPrefs in ['edit']
def colorManagementPrefs(cfe: bool = ..., cme: bool = ..., cmp: bool = ..., cfp: str = ..., din: str = ..., dn: str = ..., ore: bool = ..., ott: str = ..., ote: bool = ..., otn: str = ..., otc: bool = ..., ovt: bool = ..., pfn: str = ..., poe: bool = ..., rsn: str = ..., vn: str = ..., vtn: str = ..., e: bool = ...) -> None:
    """colorManagementPrefs is undoable, queryable, and editable.
    
    This command allows querying and editing the color management global data in a
    scene. It also allows for setting the view transform and rendering space which
    automatically configures the color processing in the enabled views.

    Example:
    ```python
        import maya.cmds as cmds
        ws = cmds.colorManagementPrefs(q=True, renderingSpaceName=True)
        cmds.colorManagementPrefs(e=True, viewTransformName="Log")
        renderingSpaces = cmd.colorManagementPrefs(q=True, renderingSpaceNames=True)
        viewingTransforms = cmd.colorManagementPrefs(q=True, viewTransformNames=True)
        cmds.colorManagementPrefs(e=True, configFilePath="/project/local_config.ocio")
    ```

    ---
    - Args:
        - cmConfigFileEnabled (cfe): Turn on or off applying an OCIO configuration file.  If set, the color management configuration set in the preferences is used.
        - cmEnabled (cme): Turn on or off color management in general.  If set, the color management configuration set in the preferences is used.
        - colorManagePots (cmp): Turn on or off color management of color pots in the UI.  If set, colors in color pots are taken to be in rendering space, and are displayed after being transformed by the view transform set in the preferences.
        - configFilePath (cfp): The configuration file to be used, if color management is enabled.
        - defaultInputSpaceName (din): This flag is obsolete.  See the colorManagementFileRules command for more information.
        - displayName (dn): The display from the (display, view) pair, to be applied by color managed viewers and color managed UI controls.
        - ocioRulesEnabled (ore): Turn on or off the use of colorspace assignment rules from the OCIO library.
        - outputTarget (ott): Indicates to which output the outputTransformEnabled or the outputTransformName flags are to be applied. Valid values are "renderer" or "playblast".In query mode, this flag needs a value.
        - outputTransformEnabled (ote): Turn on or off applying the output transform for out of viewport renders. If set, the output transform set in the preferences is used.
        - outputTransformName (otn): The output transform to be applied for out of viewport renders.  Disables output use view transform mode.
        - outputTransformUseColorConversion (otc): Turn on or off selecting the color space conversion for the output color space of viewport renders.  If set, a conversion color space is used; otherwise, a view transform is used.
        - outputUseViewTransform (ovt): Turns use view transform mode on.  In this mode, the output transform is set to match the view transform.  To turn the mode off, set an output transform using the outputTransformName flag.
        - policyFileName (pfn): Set the policy file name
        - popupOnError (poe): Turn on or off displaying a modal popup on error (as well as the normal script editor reporting of the error), for this invocation of the command.  Default is off.
        - renderingSpaceName (rsn): The color space to be used during rendering.  This is the source color space to the viewing transform, for color managed viewers and color managed UI controls, and the destination color space for color managed input pixels.
        - viewName (vn): The view from the (display, view) pair, to be applied by color managed viewers and color managed UI controls.
        - viewTransformName (vtn): The view transform to be applied by color managed viewers and color managed UI controls.
        - edit (e): Edit mode flag
    """
@overload #Overload for colorManagementPrefs in ['edit']
def colorManagementPrefs(cmConfigFileEnabled: bool = ..., cfe: bool = ..., cmEnabled: bool = ..., cme: bool = ..., colorManagePots: bool = ..., cmp: bool = ..., configFilePath: str = ..., cfp: str = ..., defaultInputSpaceName: str = ..., din: str = ..., displayName: str = ..., dn: str = ..., ocioRulesEnabled: bool = ..., ore: bool = ..., outputTarget: str = ..., ott: str = ..., outputTransformEnabled: bool = ..., ote: bool = ..., outputTransformName: str = ..., otn: str = ..., outputTransformUseColorConversion: bool = ..., otc: bool = ..., outputUseViewTransform: bool = ..., ovt: bool = ..., policyFileName: str = ..., pfn: str = ..., popupOnError: bool = ..., poe: bool = ..., renderingSpaceName: str = ..., rsn: str = ..., viewName: str = ..., vn: str = ..., viewTransformName: str = ..., vtn: str = ..., edit: bool = ..., e: bool = ...) -> None:
    """colorManagementPrefs is undoable, queryable, and editable.
    
    This command allows querying and editing the color management global data in a
    scene. It also allows for setting the view transform and rendering space which
    automatically configures the color processing in the enabled views.

    Example:
    ```python
        import maya.cmds as cmds
        ws = cmds.colorManagementPrefs(q=True, renderingSpaceName=True)
        cmds.colorManagementPrefs(e=True, viewTransformName="Log")
        renderingSpaces = cmd.colorManagementPrefs(q=True, renderingSpaceNames=True)
        viewingTransforms = cmd.colorManagementPrefs(q=True, viewTransformNames=True)
        cmds.colorManagementPrefs(e=True, configFilePath="/project/local_config.ocio")
    ```

    ---
    - Args:
        - cmConfigFileEnabled (cfe): Turn on or off applying an OCIO configuration file.  If set, the color management configuration set in the preferences is used.
        - cmEnabled (cme): Turn on or off color management in general.  If set, the color management configuration set in the preferences is used.
        - colorManagePots (cmp): Turn on or off color management of color pots in the UI.  If set, colors in color pots are taken to be in rendering space, and are displayed after being transformed by the view transform set in the preferences.
        - configFilePath (cfp): The configuration file to be used, if color management is enabled.
        - defaultInputSpaceName (din): This flag is obsolete.  See the colorManagementFileRules command for more information.
        - displayName (dn): The display from the (display, view) pair, to be applied by color managed viewers and color managed UI controls.
        - ocioRulesEnabled (ore): Turn on or off the use of colorspace assignment rules from the OCIO library.
        - outputTarget (ott): Indicates to which output the outputTransformEnabled or the outputTransformName flags are to be applied. Valid values are "renderer" or "playblast".In query mode, this flag needs a value.
        - outputTransformEnabled (ote): Turn on or off applying the output transform for out of viewport renders. If set, the output transform set in the preferences is used.
        - outputTransformName (otn): The output transform to be applied for out of viewport renders.  Disables output use view transform mode.
        - outputTransformUseColorConversion (otc): Turn on or off selecting the color space conversion for the output color space of viewport renders.  If set, a conversion color space is used; otherwise, a view transform is used.
        - outputUseViewTransform (ovt): Turns use view transform mode on.  In this mode, the output transform is set to match the view transform.  To turn the mode off, set an output transform using the outputTransformName flag.
        - policyFileName (pfn): Set the policy file name
        - popupOnError (poe): Turn on or off displaying a modal popup on error (as well as the normal script editor reporting of the error), for this invocation of the command.  Default is off.
        - renderingSpaceName (rsn): The color space to be used during rendering.  This is the source color space to the viewing transform, for color managed viewers and color managed UI controls, and the destination color space for color managed input pixels.
        - viewName (vn): The view from the (display, view) pair, to be applied by color managed viewers and color managed UI controls.
        - viewTransformName (vtn): The view transform to be applied by color managed viewers and color managed UI controls.
        - edit (e): Edit mode flag
    """
