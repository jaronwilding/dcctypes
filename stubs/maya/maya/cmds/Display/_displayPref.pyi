"""Stub files for Display category in Maya commands, command: displayPref."""

from typing import Any, overload

@overload #Overload for displayPref in ['create']
def displayPref(activeObjectPivots: bool = ..., defaultFontSize: int = ..., displayAffected: bool = ..., displayGradient: bool = ..., fontSettingMode: int = ..., ghostFrames: [int, int, int] = ..., materialLoadingMode: str = ..., maxTextureResolution: int = ..., purgeExistingTextures: bool = ..., regionOfEffect: bool = ..., shadeTemplates: bool = ..., smallFontSize: int = ..., textureDrawPixel: bool = ..., wireframeOnShadedActive: str = ...) -> None:
    """displayPref is undoable, queryable, and NOT editable.
    
    This command sets/queries the state of global display parameters.

    Example:
    ```python
        import maya.cmds as cmds
        # Turn on the display of affected objects
        cmds.displayPref( displayAffected=True )
        # Query whether affected objects will be displayed
        # in a special color or not.
        cmds.displayPref( q=True, displayAffected=True )
        # Result: 1 #
        # Turn on full wireframes on active shaded objects
        cmds.displayPref( wireframeOnShadedActive='full' )
    ```

    ---
    - Args:
        - activeObjectPivots (aop): Sets the display state for drawing pivots for active objects.
        - defaultFontSize (dfs): Sets the Viewport 2.0 custom default font size, updating the display when in custom mode. Values are limited between size 9 and 24.
        - displayAffected (da): Turns on/off the special coloring of objects that are affected by the objects that are currently in the selection list. If one of the curves in a loft were selected and this feature were turned on, then the lofted surface would be
            highlighted because it is affected by the loft curve.
        - displayGradient (dgr): Set whether to display the background using a colored gradient as opposed to a constant background color.
        - fontSettingMode (fm): Sets the Viewport 2.0 font display size mode, as per the Font Display section in Preferences. Possible values are 0 (default), 1 (medium (from Maya 2010)), 2 (Custom - see smallFontSize/ defaultFontSize)
        - ghostFrames (gf): Obsolete - use the "ghosting" command to set these values.
        - materialLoadingMode (mld): Sets the material loading mode when loading the scene.  Possible values for the string argument are "immediate", "deferred" and "parallel".
        - maxTextureResolution (mtr): Sets the maximum hardware texture resolution to be used when creating hardware textures for display. The maximum will be clamped to the maximum allowable texture determined for the hardware at the time this command is invoked. Use the
            -maxHardwareTextureResolution to retrieve this maximum value. Existing hardware textures are not affected. Only newly created textures will be clamped to this maximum.
        - purgeExistingTextures (pet): Purge any existing hardware textures. This will force a re-evaluation of hardware textures used for display, and thus may take some time to evaluate.
        - regionOfEffect (roe): Turns on/off the display of the region of curves/surfaces that is affected by changes to selected CVs and edit points.
        - shadeTemplates (st): Turns on/off the display of templated surfaces as shaded in shaded display mode. If its off, templated surfaces appear in wireframe.
        - smallFontSize (sfs): Sets the Viewport 2.0 custom small font size, updating the display when in custom mode. Values are limited between size 9 and 12.
        - textureDrawPixel (tdp): Sets the display mode for drawing image planes. True for use of gltexture calls for perspective views. This flag should not normally be needed. Image Planes may display faster on Windows but can result in some display artifacts.
        - wireframeOnShadedActive (wsa): Sets the display state for drawing the wireframe on active shaded objects.  Possible values for the string argument are "full", "reduced" and "none".
    """
@overload #Overload for displayPref in ['create']
def displayPref(aop: bool = ..., dfs: int = ..., da: bool = ..., dgr: bool = ..., fm: int = ..., gf: [int, int, int] = ..., mld: str = ..., mtr: int = ..., pet: bool = ..., roe: bool = ..., st: bool = ..., sfs: int = ..., tdp: bool = ..., wsa: str = ...) -> None:
    """displayPref is undoable, queryable, and NOT editable.
    
    This command sets/queries the state of global display parameters.

    Example:
    ```python
        import maya.cmds as cmds
        # Turn on the display of affected objects
        cmds.displayPref( displayAffected=True )
        # Query whether affected objects will be displayed
        # in a special color or not.
        cmds.displayPref( q=True, displayAffected=True )
        # Result: 1 #
        # Turn on full wireframes on active shaded objects
        cmds.displayPref( wireframeOnShadedActive='full' )
    ```

    ---
    - Args:
        - activeObjectPivots (aop): Sets the display state for drawing pivots for active objects.
        - defaultFontSize (dfs): Sets the Viewport 2.0 custom default font size, updating the display when in custom mode. Values are limited between size 9 and 24.
        - displayAffected (da): Turns on/off the special coloring of objects that are affected by the objects that are currently in the selection list. If one of the curves in a loft were selected and this feature were turned on, then the lofted surface would be
            highlighted because it is affected by the loft curve.
        - displayGradient (dgr): Set whether to display the background using a colored gradient as opposed to a constant background color.
        - fontSettingMode (fm): Sets the Viewport 2.0 font display size mode, as per the Font Display section in Preferences. Possible values are 0 (default), 1 (medium (from Maya 2010)), 2 (Custom - see smallFontSize/ defaultFontSize)
        - ghostFrames (gf): Obsolete - use the "ghosting" command to set these values.
        - materialLoadingMode (mld): Sets the material loading mode when loading the scene.  Possible values for the string argument are "immediate", "deferred" and "parallel".
        - maxTextureResolution (mtr): Sets the maximum hardware texture resolution to be used when creating hardware textures for display. The maximum will be clamped to the maximum allowable texture determined for the hardware at the time this command is invoked. Use the
            -maxHardwareTextureResolution to retrieve this maximum value. Existing hardware textures are not affected. Only newly created textures will be clamped to this maximum.
        - purgeExistingTextures (pet): Purge any existing hardware textures. This will force a re-evaluation of hardware textures used for display, and thus may take some time to evaluate.
        - regionOfEffect (roe): Turns on/off the display of the region of curves/surfaces that is affected by changes to selected CVs and edit points.
        - shadeTemplates (st): Turns on/off the display of templated surfaces as shaded in shaded display mode. If its off, templated surfaces appear in wireframe.
        - smallFontSize (sfs): Sets the Viewport 2.0 custom small font size, updating the display when in custom mode. Values are limited between size 9 and 12.
        - textureDrawPixel (tdp): Sets the display mode for drawing image planes. True for use of gltexture calls for perspective views. This flag should not normally be needed. Image Planes may display faster on Windows but can result in some display artifacts.
        - wireframeOnShadedActive (wsa): Sets the display state for drawing the wireframe on active shaded objects.  Possible values for the string argument are "full", "reduced" and "none".
    """
@overload #Overload for displayPref in ['create']
def displayPref(activeObjectPivots: bool = ..., aop: bool = ..., defaultFontSize: int = ..., dfs: int = ..., displayAffected: bool = ..., da: bool = ..., displayGradient: bool = ..., dgr: bool = ..., fontSettingMode: int = ..., fm: int = ..., ghostFrames: [int, int, int] = ..., gf: [int, int, int] = ..., materialLoadingMode: str = ..., mld: str = ..., maxTextureResolution: int = ..., mtr: int = ..., purgeExistingTextures: bool = ..., pet: bool = ..., regionOfEffect: bool = ..., roe: bool = ..., shadeTemplates: bool = ..., st: bool = ..., smallFontSize: int = ..., sfs: int = ..., textureDrawPixel: bool = ..., tdp: bool = ..., wireframeOnShadedActive: str = ..., wsa: str = ...) -> None:
    """displayPref is undoable, queryable, and NOT editable.
    
    This command sets/queries the state of global display parameters.

    Example:
    ```python
        import maya.cmds as cmds
        # Turn on the display of affected objects
        cmds.displayPref( displayAffected=True )
        # Query whether affected objects will be displayed
        # in a special color or not.
        cmds.displayPref( q=True, displayAffected=True )
        # Result: 1 #
        # Turn on full wireframes on active shaded objects
        cmds.displayPref( wireframeOnShadedActive='full' )
    ```

    ---
    - Args:
        - activeObjectPivots (aop): Sets the display state for drawing pivots for active objects.
        - defaultFontSize (dfs): Sets the Viewport 2.0 custom default font size, updating the display when in custom mode. Values are limited between size 9 and 24.
        - displayAffected (da): Turns on/off the special coloring of objects that are affected by the objects that are currently in the selection list. If one of the curves in a loft were selected and this feature were turned on, then the lofted surface would be
            highlighted because it is affected by the loft curve.
        - displayGradient (dgr): Set whether to display the background using a colored gradient as opposed to a constant background color.
        - fontSettingMode (fm): Sets the Viewport 2.0 font display size mode, as per the Font Display section in Preferences. Possible values are 0 (default), 1 (medium (from Maya 2010)), 2 (Custom - see smallFontSize/ defaultFontSize)
        - ghostFrames (gf): Obsolete - use the "ghosting" command to set these values.
        - materialLoadingMode (mld): Sets the material loading mode when loading the scene.  Possible values for the string argument are "immediate", "deferred" and "parallel".
        - maxTextureResolution (mtr): Sets the maximum hardware texture resolution to be used when creating hardware textures for display. The maximum will be clamped to the maximum allowable texture determined for the hardware at the time this command is invoked. Use the
            -maxHardwareTextureResolution to retrieve this maximum value. Existing hardware textures are not affected. Only newly created textures will be clamped to this maximum.
        - purgeExistingTextures (pet): Purge any existing hardware textures. This will force a re-evaluation of hardware textures used for display, and thus may take some time to evaluate.
        - regionOfEffect (roe): Turns on/off the display of the region of curves/surfaces that is affected by changes to selected CVs and edit points.
        - shadeTemplates (st): Turns on/off the display of templated surfaces as shaded in shaded display mode. If its off, templated surfaces appear in wireframe.
        - smallFontSize (sfs): Sets the Viewport 2.0 custom small font size, updating the display when in custom mode. Values are limited between size 9 and 12.
        - textureDrawPixel (tdp): Sets the display mode for drawing image planes. True for use of gltexture calls for perspective views. This flag should not normally be needed. Image Planes may display faster on Windows but can result in some display artifacts.
        - wireframeOnShadedActive (wsa): Sets the display state for drawing the wireframe on active shaded objects.  Possible values for the string argument are "full", "reduced" and "none".
    """
@overload #Overload for displayPref in ['query']
def displayPref(activeObjectPivots: bool = ..., defaultFontSize: int = ..., displayAffected: bool = ..., displayGradient: bool = ..., fontSettingMode: int = ..., ghostFrames: [int, int, int] = ..., materialLoadingMode: str = ..., maxHardwareTextureResolution: bool = ..., maxTextureResolution: int = ..., regionOfEffect: bool = ..., shadeTemplates: bool = ..., smallFontSize: int = ..., textureDrawPixel: bool = ..., wireframeOnShadedActive: str = ..., query: bool = ...) -> None:
    """displayPref is undoable, queryable, and NOT editable.
    
    This command sets/queries the state of global display parameters.

    Example:
    ```python
        import maya.cmds as cmds
        # Turn on the display of affected objects
        cmds.displayPref( displayAffected=True )
        # Query whether affected objects will be displayed
        # in a special color or not.
        cmds.displayPref( q=True, displayAffected=True )
        # Result: 1 #
        # Turn on full wireframes on active shaded objects
        cmds.displayPref( wireframeOnShadedActive='full' )
    ```

    ---
    - Args:
        - activeObjectPivots (aop): Sets the display state for drawing pivots for active objects.
        - defaultFontSize (dfs): Sets the Viewport 2.0 custom default font size, updating the display when in custom mode. Values are limited between size 9 and 24.
        - displayAffected (da): Turns on/off the special coloring of objects that are affected by the objects that are currently in the selection list. If one of the curves in a loft were selected and this feature were turned on, then the lofted surface would be
            highlighted because it is affected by the loft curve.
        - displayGradient (dgr): Set whether to display the background using a colored gradient as opposed to a constant background color.
        - fontSettingMode (fm): Sets the Viewport 2.0 font display size mode, as per the Font Display section in Preferences. Possible values are 0 (default), 1 (medium (from Maya 2010)), 2 (Custom - see smallFontSize/ defaultFontSize)
        - ghostFrames (gf): Obsolete - use the "ghosting" command to set these values.
        - materialLoadingMode (mld): Sets the material loading mode when loading the scene.  Possible values for the string argument are "immediate", "deferred" and "parallel".
        - maxHardwareTextureResolution (mhr): Query the maximum allowable hardware texture resolution available on the current video card. This maximum can vary between different video cards and different operating systems.
        - maxTextureResolution (mtr): Sets the maximum hardware texture resolution to be used when creating hardware textures for display. The maximum will be clamped to the maximum allowable texture determined for the hardware at the time this command is invoked. Use the
            -maxHardwareTextureResolution to retrieve this maximum value. Existing hardware textures are not affected. Only newly created textures will be clamped to this maximum.
        - regionOfEffect (roe): Turns on/off the display of the region of curves/surfaces that is affected by changes to selected CVs and edit points.
        - shadeTemplates (st): Turns on/off the display of templated surfaces as shaded in shaded display mode. If its off, templated surfaces appear in wireframe.
        - smallFontSize (sfs): Sets the Viewport 2.0 custom small font size, updating the display when in custom mode. Values are limited between size 9 and 12.
        - textureDrawPixel (tdp): Sets the display mode for drawing image planes. True for use of gltexture calls for perspective views. This flag should not normally be needed. Image Planes may display faster on Windows but can result in some display artifacts.
        - wireframeOnShadedActive (wsa): Sets the display state for drawing the wireframe on active shaded objects.  Possible values for the string argument are "full", "reduced" and "none".
        - query (q): Query mode flag
    """
@overload #Overload for displayPref in ['query']
def displayPref(aop: bool = ..., dfs: int = ..., da: bool = ..., dgr: bool = ..., fm: int = ..., gf: [int, int, int] = ..., mld: str = ..., mhr: bool = ..., mtr: int = ..., roe: bool = ..., st: bool = ..., sfs: int = ..., tdp: bool = ..., wsa: str = ..., q: bool = ...) -> None:
    """displayPref is undoable, queryable, and NOT editable.
    
    This command sets/queries the state of global display parameters.

    Example:
    ```python
        import maya.cmds as cmds
        # Turn on the display of affected objects
        cmds.displayPref( displayAffected=True )
        # Query whether affected objects will be displayed
        # in a special color or not.
        cmds.displayPref( q=True, displayAffected=True )
        # Result: 1 #
        # Turn on full wireframes on active shaded objects
        cmds.displayPref( wireframeOnShadedActive='full' )
    ```

    ---
    - Args:
        - activeObjectPivots (aop): Sets the display state for drawing pivots for active objects.
        - defaultFontSize (dfs): Sets the Viewport 2.0 custom default font size, updating the display when in custom mode. Values are limited between size 9 and 24.
        - displayAffected (da): Turns on/off the special coloring of objects that are affected by the objects that are currently in the selection list. If one of the curves in a loft were selected and this feature were turned on, then the lofted surface would be
            highlighted because it is affected by the loft curve.
        - displayGradient (dgr): Set whether to display the background using a colored gradient as opposed to a constant background color.
        - fontSettingMode (fm): Sets the Viewport 2.0 font display size mode, as per the Font Display section in Preferences. Possible values are 0 (default), 1 (medium (from Maya 2010)), 2 (Custom - see smallFontSize/ defaultFontSize)
        - ghostFrames (gf): Obsolete - use the "ghosting" command to set these values.
        - materialLoadingMode (mld): Sets the material loading mode when loading the scene.  Possible values for the string argument are "immediate", "deferred" and "parallel".
        - maxHardwareTextureResolution (mhr): Query the maximum allowable hardware texture resolution available on the current video card. This maximum can vary between different video cards and different operating systems.
        - maxTextureResolution (mtr): Sets the maximum hardware texture resolution to be used when creating hardware textures for display. The maximum will be clamped to the maximum allowable texture determined for the hardware at the time this command is invoked. Use the
            -maxHardwareTextureResolution to retrieve this maximum value. Existing hardware textures are not affected. Only newly created textures will be clamped to this maximum.
        - regionOfEffect (roe): Turns on/off the display of the region of curves/surfaces that is affected by changes to selected CVs and edit points.
        - shadeTemplates (st): Turns on/off the display of templated surfaces as shaded in shaded display mode. If its off, templated surfaces appear in wireframe.
        - smallFontSize (sfs): Sets the Viewport 2.0 custom small font size, updating the display when in custom mode. Values are limited between size 9 and 12.
        - textureDrawPixel (tdp): Sets the display mode for drawing image planes. True for use of gltexture calls for perspective views. This flag should not normally be needed. Image Planes may display faster on Windows but can result in some display artifacts.
        - wireframeOnShadedActive (wsa): Sets the display state for drawing the wireframe on active shaded objects.  Possible values for the string argument are "full", "reduced" and "none".
        - query (q): Query mode flag
    """
@overload #Overload for displayPref in ['query']
def displayPref(activeObjectPivots: bool = ..., aop: bool = ..., defaultFontSize: int = ..., dfs: int = ..., displayAffected: bool = ..., da: bool = ..., displayGradient: bool = ..., dgr: bool = ..., fontSettingMode: int = ..., fm: int = ..., ghostFrames: [int, int, int] = ..., gf: [int, int, int] = ..., materialLoadingMode: str = ..., mld: str = ..., maxHardwareTextureResolution: bool = ..., mhr: bool = ..., maxTextureResolution: int = ..., mtr: int = ..., regionOfEffect: bool = ..., roe: bool = ..., shadeTemplates: bool = ..., st: bool = ..., smallFontSize: int = ..., sfs: int = ..., textureDrawPixel: bool = ..., tdp: bool = ..., wireframeOnShadedActive: str = ..., wsa: str = ..., query: bool = ..., q: bool = ...) -> None:
    """displayPref is undoable, queryable, and NOT editable.
    
    This command sets/queries the state of global display parameters.

    Example:
    ```python
        import maya.cmds as cmds
        # Turn on the display of affected objects
        cmds.displayPref( displayAffected=True )
        # Query whether affected objects will be displayed
        # in a special color or not.
        cmds.displayPref( q=True, displayAffected=True )
        # Result: 1 #
        # Turn on full wireframes on active shaded objects
        cmds.displayPref( wireframeOnShadedActive='full' )
    ```

    ---
    - Args:
        - activeObjectPivots (aop): Sets the display state for drawing pivots for active objects.
        - defaultFontSize (dfs): Sets the Viewport 2.0 custom default font size, updating the display when in custom mode. Values are limited between size 9 and 24.
        - displayAffected (da): Turns on/off the special coloring of objects that are affected by the objects that are currently in the selection list. If one of the curves in a loft were selected and this feature were turned on, then the lofted surface would be
            highlighted because it is affected by the loft curve.
        - displayGradient (dgr): Set whether to display the background using a colored gradient as opposed to a constant background color.
        - fontSettingMode (fm): Sets the Viewport 2.0 font display size mode, as per the Font Display section in Preferences. Possible values are 0 (default), 1 (medium (from Maya 2010)), 2 (Custom - see smallFontSize/ defaultFontSize)
        - ghostFrames (gf): Obsolete - use the "ghosting" command to set these values.
        - materialLoadingMode (mld): Sets the material loading mode when loading the scene.  Possible values for the string argument are "immediate", "deferred" and "parallel".
        - maxHardwareTextureResolution (mhr): Query the maximum allowable hardware texture resolution available on the current video card. This maximum can vary between different video cards and different operating systems.
        - maxTextureResolution (mtr): Sets the maximum hardware texture resolution to be used when creating hardware textures for display. The maximum will be clamped to the maximum allowable texture determined for the hardware at the time this command is invoked. Use the
            -maxHardwareTextureResolution to retrieve this maximum value. Existing hardware textures are not affected. Only newly created textures will be clamped to this maximum.
        - regionOfEffect (roe): Turns on/off the display of the region of curves/surfaces that is affected by changes to selected CVs and edit points.
        - shadeTemplates (st): Turns on/off the display of templated surfaces as shaded in shaded display mode. If its off, templated surfaces appear in wireframe.
        - smallFontSize (sfs): Sets the Viewport 2.0 custom small font size, updating the display when in custom mode. Values are limited between size 9 and 12.
        - textureDrawPixel (tdp): Sets the display mode for drawing image planes. True for use of gltexture calls for perspective views. This flag should not normally be needed. Image Planes may display faster on Windows but can result in some display artifacts.
        - wireframeOnShadedActive (wsa): Sets the display state for drawing the wireframe on active shaded objects.  Possible values for the string argument are "full", "reduced" and "none".
        - query (q): Query mode flag
    """
