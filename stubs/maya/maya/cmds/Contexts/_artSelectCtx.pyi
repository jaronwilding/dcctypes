"""Stub files for Contexts category in Maya commands, command: artSelectCtx."""

from typing import Any, overload

@overload #Overload for artSelectCtx in ['create']
def artSelectCtx(accopacity: bool = ..., addselection: bool = ..., afterStrokeCmd: str = ..., beforeStrokeCmd: str = ..., brushalignment: bool = ..., brushfeedback: bool = ..., clear: bool = ..., dragSlider: str = ..., dynclonemode: bool = ..., exists: bool = ..., expandfilename: bool = ..., exportaspectratio: float = ..., exportfilemode: str = ..., exportfilesizex: int = ..., exportfilesizey: int = ..., exportfiletype: str = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., importfilemode: str = ..., importreassign: bool = ..., importthreshold: float = ..., lastRecorderCmd: str = ..., lastStampName: str = ..., lowerradius: float = ..., makeStroke: int = ..., mappressure: str = ..., name: str = ..., opacity: float = ..., outline: bool = ..., outwhilepaint: bool = ..., paintmode: str = ..., paintoperationtype: str = ..., pickColor: bool = ..., pickValue: bool = ..., playbackCursor: [float, float] = ..., playbackPressure: float = ..., preserveclonesource: bool = ..., projective: bool = ..., radius: float = ..., record: bool = ..., reflection: bool = ..., reflectionaboutorigin: bool = ..., reflectionaxis: str = ..., screenRadius: float = ..., selectall: bool = ..., selectclonesource: bool = ..., selectop: str = ..., showactive: bool = ..., stampDepth: float = ..., stampProfile: str = ..., stampSpacing: float = ..., strokesmooth: str = ..., surfaceConformedBrushVertices: bool = ..., tangentOutline: bool = ..., toggleall: bool = ..., unselectall: bool = ..., usepressure: bool = ..., worldRadius: float = ...) -> None:
    """artSelectCtx is undoable, queryable, and editable.
    
    This command is used to select/deselect/toggle components on selected surfaces
    using a brush interface (Maya Artisan). Since, it selects components of the
    surface, it only works in the component mode.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new select context, then switch to it
        cmds.artSelectCtx('artSelectCtx1')
        cmds.setToolTo('artSelectCtx1')
        # Set brush's radius to 2.0, lower radius to 0.5
        cmds.artSelectCtx('artSelectCtx1', edit=True, r=2.0, lr=0.5)
    ```

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - addselection (ads): If true, each new stroke adds cvs to the active list. If false, each stroke replaces the previous selection. C: Default is true. Q: When queried, it returns a boole
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - clear (clr): Floods all cvs/vertices to the current value.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - exportaspectratio (ear): Value of aspect ratio for export
        - exportfilemode (efm): Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        - exportfilesizex (fsx): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfilesizey (fsy): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfiletype (eft): Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - importfilemode (ifm): Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        - importreassign (irm): Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        - importthreshold (ift): Specifies the threshold for the import of the attribute maps. C: Default is 0.5.  Q: When queried, it returns a float.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - name (n): If this is a tool command, name the tool appropriately.
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - screenRadius (scR): Brush radius on the screen
        - selectall (sal): Selects all vertices/egdes/faces/uvs.
        - selectclonesource (scs): Toggle on to select the clone source
        - selectop (sop): Specifies the selection operation ("select", "unselect", "toggle"). C: Default is "select". Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - toggleall (tal): Toggle all vertices/egdes/faces/uvs.
        - unselectall (ual): Unselects all vertices/egdes/faces/uvs.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
    """
@overload #Overload for artSelectCtx in ['create']
def artSelectCtx(aco: bool = ..., ads: bool = ..., asc: str = ..., bsc: str = ..., bra: bool = ..., brf: bool = ..., clr: bool = ..., dsl: str = ..., dcm: bool = ..., ex: bool = ..., eef: bool = ..., ear: float = ..., efm: str = ..., fsx: int = ..., fsy: int = ..., eft: str = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ifm: str = ..., irm: bool = ..., ift: float = ..., lrc: str = ..., lsn: str = ..., lr: float = ..., mst: int = ..., mp: str = ..., n: str = ..., op: float = ..., o: bool = ..., owp: bool = ..., pm: str = ..., pot: str = ..., pcm: bool = ..., pv: bool = ..., plc: [float, float] = ..., plp: float = ..., pcs: bool = ..., prm: bool = ..., r: float = ..., rec: bool = ..., rn: bool = ..., rno: bool = ..., ra: str = ..., scR: float = ..., sal: bool = ..., scs: bool = ..., sop: str = ..., sa: bool = ..., stD: float = ..., stP: str = ..., stS: float = ..., ssm: str = ..., scv: bool = ..., to: bool = ..., tal: bool = ..., ual: bool = ..., up: bool = ..., wlR: float = ...) -> None:
    """artSelectCtx is undoable, queryable, and editable.
    
    This command is used to select/deselect/toggle components on selected surfaces
    using a brush interface (Maya Artisan). Since, it selects components of the
    surface, it only works in the component mode.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new select context, then switch to it
        cmds.artSelectCtx('artSelectCtx1')
        cmds.setToolTo('artSelectCtx1')
        # Set brush's radius to 2.0, lower radius to 0.5
        cmds.artSelectCtx('artSelectCtx1', edit=True, r=2.0, lr=0.5)
    ```

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - addselection (ads): If true, each new stroke adds cvs to the active list. If false, each stroke replaces the previous selection. C: Default is true. Q: When queried, it returns a boole
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - clear (clr): Floods all cvs/vertices to the current value.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - exportaspectratio (ear): Value of aspect ratio for export
        - exportfilemode (efm): Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        - exportfilesizex (fsx): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfilesizey (fsy): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfiletype (eft): Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - importfilemode (ifm): Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        - importreassign (irm): Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        - importthreshold (ift): Specifies the threshold for the import of the attribute maps. C: Default is 0.5.  Q: When queried, it returns a float.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - name (n): If this is a tool command, name the tool appropriately.
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - screenRadius (scR): Brush radius on the screen
        - selectall (sal): Selects all vertices/egdes/faces/uvs.
        - selectclonesource (scs): Toggle on to select the clone source
        - selectop (sop): Specifies the selection operation ("select", "unselect", "toggle"). C: Default is "select". Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - toggleall (tal): Toggle all vertices/egdes/faces/uvs.
        - unselectall (ual): Unselects all vertices/egdes/faces/uvs.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
    """
@overload #Overload for artSelectCtx in ['create']
def artSelectCtx(accopacity: bool = ..., aco: bool = ..., addselection: bool = ..., ads: bool = ..., afterStrokeCmd: str = ..., asc: str = ..., beforeStrokeCmd: str = ..., bsc: str = ..., brushalignment: bool = ..., bra: bool = ..., brushfeedback: bool = ..., brf: bool = ..., clear: bool = ..., clr: bool = ..., dragSlider: str = ..., dsl: str = ..., dynclonemode: bool = ..., dcm: bool = ..., exists: bool = ..., ex: bool = ..., expandfilename: bool = ..., eef: bool = ..., exportaspectratio: float = ..., ear: float = ..., exportfilemode: str = ..., efm: str = ..., exportfilesizex: int = ..., fsx: int = ..., exportfilesizey: int = ..., fsy: int = ..., exportfiletype: str = ..., eft: str = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., importfilemode: str = ..., ifm: str = ..., importreassign: bool = ..., irm: bool = ..., importthreshold: float = ..., ift: float = ..., lastRecorderCmd: str = ..., lrc: str = ..., lastStampName: str = ..., lsn: str = ..., lowerradius: float = ..., lr: float = ..., makeStroke: int = ..., mst: int = ..., mappressure: str = ..., mp: str = ..., name: str = ..., n: str = ..., opacity: float = ..., op: float = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintmode: str = ..., pm: str = ..., paintoperationtype: str = ..., pot: str = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: [float, float] = ..., plc: [float, float] = ..., playbackPressure: float = ..., plp: float = ..., preserveclonesource: bool = ..., pcs: bool = ..., projective: bool = ..., prm: bool = ..., radius: float = ..., r: float = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: str = ..., ra: str = ..., screenRadius: float = ..., scR: float = ..., selectall: bool = ..., sal: bool = ..., selectclonesource: bool = ..., scs: bool = ..., selectop: str = ..., sop: str = ..., showactive: bool = ..., sa: bool = ..., stampDepth: float = ..., stD: float = ..., stampProfile: str = ..., stP: str = ..., stampSpacing: float = ..., stS: float = ..., strokesmooth: str = ..., ssm: str = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tangentOutline: bool = ..., to: bool = ..., toggleall: bool = ..., tal: bool = ..., unselectall: bool = ..., ual: bool = ..., usepressure: bool = ..., up: bool = ..., worldRadius: float = ..., wlR: float = ...) -> None:
    """artSelectCtx is undoable, queryable, and editable.
    
    This command is used to select/deselect/toggle components on selected surfaces
    using a brush interface (Maya Artisan). Since, it selects components of the
    surface, it only works in the component mode.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new select context, then switch to it
        cmds.artSelectCtx('artSelectCtx1')
        cmds.setToolTo('artSelectCtx1')
        # Set brush's radius to 2.0, lower radius to 0.5
        cmds.artSelectCtx('artSelectCtx1', edit=True, r=2.0, lr=0.5)
    ```

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - addselection (ads): If true, each new stroke adds cvs to the active list. If false, each stroke replaces the previous selection. C: Default is true. Q: When queried, it returns a boole
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - clear (clr): Floods all cvs/vertices to the current value.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - exportaspectratio (ear): Value of aspect ratio for export
        - exportfilemode (efm): Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        - exportfilesizex (fsx): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfilesizey (fsy): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfiletype (eft): Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - importfilemode (ifm): Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        - importreassign (irm): Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        - importthreshold (ift): Specifies the threshold for the import of the attribute maps. C: Default is 0.5.  Q: When queried, it returns a float.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - name (n): If this is a tool command, name the tool appropriately.
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - screenRadius (scR): Brush radius on the screen
        - selectall (sal): Selects all vertices/egdes/faces/uvs.
        - selectclonesource (scs): Toggle on to select the clone source
        - selectop (sop): Specifies the selection operation ("select", "unselect", "toggle"). C: Default is "select". Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - toggleall (tal): Toggle all vertices/egdes/faces/uvs.
        - unselectall (ual): Unselects all vertices/egdes/faces/uvs.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
    """
@overload #Overload for artSelectCtx in ['query']
def artSelectCtx(accopacity: bool = ..., addselection: bool = ..., afterStrokeCmd: str = ..., beforeStrokeCmd: str = ..., brushalignment: bool = ..., brushfeedback: bool = ..., dynclonemode: bool = ..., exportaspectratio: float = ..., exportfilemode: str = ..., exportfilesizex: int = ..., exportfilesizey: int = ..., exportfiletype: str = ..., image1: str = ..., image2: str = ..., image3: str = ..., importfilemode: str = ..., importreassign: bool = ..., importthreshold: float = ..., lastRecorderCmd: str = ..., lastStampName: str = ..., lowerradius: float = ..., makeStroke: int = ..., mappressure: str = ..., opacity: float = ..., outline: bool = ..., outwhilepaint: bool = ..., paintmode: str = ..., paintoperationtype: str = ..., pickColor: bool = ..., pickValue: bool = ..., playbackCursor: [float, float] = ..., playbackPressure: float = ..., preserveclonesource: bool = ..., profileShapeFile: str = ..., projective: bool = ..., radius: float = ..., record: bool = ..., reflection: bool = ..., reflectionaboutorigin: bool = ..., reflectionaxis: str = ..., screenRadius: float = ..., selectclonesource: bool = ..., selectop: str = ..., showactive: bool = ..., stampDepth: float = ..., stampProfile: str = ..., stampSpacing: float = ..., strokesmooth: str = ..., surfaceConformedBrushVertices: bool = ..., tablet: bool = ..., tangentOutline: bool = ..., usepressure: bool = ..., worldRadius: float = ..., query: bool = ...) -> None:
    """artSelectCtx is undoable, queryable, and editable.
    
    This command is used to select/deselect/toggle components on selected surfaces
    using a brush interface (Maya Artisan). Since, it selects components of the
    surface, it only works in the component mode.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new select context, then switch to it
        cmds.artSelectCtx('artSelectCtx1')
        cmds.setToolTo('artSelectCtx1')
        # Set brush's radius to 2.0, lower radius to 0.5
        cmds.artSelectCtx('artSelectCtx1', edit=True, r=2.0, lr=0.5)
    ```

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - addselection (ads): If true, each new stroke adds cvs to the active list. If false, each stroke replaces the previous selection. C: Default is true. Q: When queried, it returns a boole
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - exportaspectratio (ear): Value of aspect ratio for export
        - exportfilemode (efm): Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        - exportfilesizex (fsx): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfilesizey (fsy): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfiletype (eft): Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - importfilemode (ifm): Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        - importreassign (irm): Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        - importthreshold (ift): Specifies the threshold for the import of the attribute maps. C: Default is 0.5.  Q: When queried, it returns a float.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - selectop (sop): Specifies the selection operation ("select", "unselect", "toggle"). C: Default is "select". Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tablet (tab): Returns true if the tablet device is present, false if it is absent
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
        - query (q): Query mode flag
    """
@overload #Overload for artSelectCtx in ['query']
def artSelectCtx(aco: bool = ..., ads: bool = ..., asc: str = ..., bsc: str = ..., bra: bool = ..., brf: bool = ..., dcm: bool = ..., ear: float = ..., efm: str = ..., fsx: int = ..., fsy: int = ..., eft: str = ..., i1: str = ..., i2: str = ..., i3: str = ..., ifm: str = ..., irm: bool = ..., ift: float = ..., lrc: str = ..., lsn: str = ..., lr: float = ..., mst: int = ..., mp: str = ..., op: float = ..., o: bool = ..., owp: bool = ..., pm: str = ..., pot: str = ..., pcm: bool = ..., pv: bool = ..., plc: [float, float] = ..., plp: float = ..., pcs: bool = ..., psf: str = ..., prm: bool = ..., r: float = ..., rec: bool = ..., rn: bool = ..., rno: bool = ..., ra: str = ..., scR: float = ..., scs: bool = ..., sop: str = ..., sa: bool = ..., stD: float = ..., stP: str = ..., stS: float = ..., ssm: str = ..., scv: bool = ..., tab: bool = ..., to: bool = ..., up: bool = ..., wlR: float = ..., q: bool = ...) -> None:
    """artSelectCtx is undoable, queryable, and editable.
    
    This command is used to select/deselect/toggle components on selected surfaces
    using a brush interface (Maya Artisan). Since, it selects components of the
    surface, it only works in the component mode.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new select context, then switch to it
        cmds.artSelectCtx('artSelectCtx1')
        cmds.setToolTo('artSelectCtx1')
        # Set brush's radius to 2.0, lower radius to 0.5
        cmds.artSelectCtx('artSelectCtx1', edit=True, r=2.0, lr=0.5)
    ```

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - addselection (ads): If true, each new stroke adds cvs to the active list. If false, each stroke replaces the previous selection. C: Default is true. Q: When queried, it returns a boole
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - exportaspectratio (ear): Value of aspect ratio for export
        - exportfilemode (efm): Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        - exportfilesizex (fsx): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfilesizey (fsy): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfiletype (eft): Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - importfilemode (ifm): Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        - importreassign (irm): Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        - importthreshold (ift): Specifies the threshold for the import of the attribute maps. C: Default is 0.5.  Q: When queried, it returns a float.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - selectop (sop): Specifies the selection operation ("select", "unselect", "toggle"). C: Default is "select". Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tablet (tab): Returns true if the tablet device is present, false if it is absent
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
        - query (q): Query mode flag
    """
@overload #Overload for artSelectCtx in ['query']
def artSelectCtx(accopacity: bool = ..., aco: bool = ..., addselection: bool = ..., ads: bool = ..., afterStrokeCmd: str = ..., asc: str = ..., beforeStrokeCmd: str = ..., bsc: str = ..., brushalignment: bool = ..., bra: bool = ..., brushfeedback: bool = ..., brf: bool = ..., dynclonemode: bool = ..., dcm: bool = ..., exportaspectratio: float = ..., ear: float = ..., exportfilemode: str = ..., efm: str = ..., exportfilesizex: int = ..., fsx: int = ..., exportfilesizey: int = ..., fsy: int = ..., exportfiletype: str = ..., eft: str = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., importfilemode: str = ..., ifm: str = ..., importreassign: bool = ..., irm: bool = ..., importthreshold: float = ..., ift: float = ..., lastRecorderCmd: str = ..., lrc: str = ..., lastStampName: str = ..., lsn: str = ..., lowerradius: float = ..., lr: float = ..., makeStroke: int = ..., mst: int = ..., mappressure: str = ..., mp: str = ..., opacity: float = ..., op: float = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintmode: str = ..., pm: str = ..., paintoperationtype: str = ..., pot: str = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: [float, float] = ..., plc: [float, float] = ..., playbackPressure: float = ..., plp: float = ..., preserveclonesource: bool = ..., pcs: bool = ..., profileShapeFile: str = ..., psf: str = ..., projective: bool = ..., prm: bool = ..., radius: float = ..., r: float = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: str = ..., ra: str = ..., screenRadius: float = ..., scR: float = ..., selectclonesource: bool = ..., scs: bool = ..., selectop: str = ..., sop: str = ..., showactive: bool = ..., sa: bool = ..., stampDepth: float = ..., stD: float = ..., stampProfile: str = ..., stP: str = ..., stampSpacing: float = ..., stS: float = ..., strokesmooth: str = ..., ssm: str = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tablet: bool = ..., tab: bool = ..., tangentOutline: bool = ..., to: bool = ..., usepressure: bool = ..., up: bool = ..., worldRadius: float = ..., wlR: float = ..., query: bool = ..., q: bool = ...) -> None:
    """artSelectCtx is undoable, queryable, and editable.
    
    This command is used to select/deselect/toggle components on selected surfaces
    using a brush interface (Maya Artisan). Since, it selects components of the
    surface, it only works in the component mode.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new select context, then switch to it
        cmds.artSelectCtx('artSelectCtx1')
        cmds.setToolTo('artSelectCtx1')
        # Set brush's radius to 2.0, lower radius to 0.5
        cmds.artSelectCtx('artSelectCtx1', edit=True, r=2.0, lr=0.5)
    ```

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - addselection (ads): If true, each new stroke adds cvs to the active list. If false, each stroke replaces the previous selection. C: Default is true. Q: When queried, it returns a boole
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - exportaspectratio (ear): Value of aspect ratio for export
        - exportfilemode (efm): Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        - exportfilesizex (fsx): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfilesizey (fsy): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfiletype (eft): Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - importfilemode (ifm): Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        - importreassign (irm): Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        - importthreshold (ift): Specifies the threshold for the import of the attribute maps. C: Default is 0.5.  Q: When queried, it returns a float.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - selectop (sop): Specifies the selection operation ("select", "unselect", "toggle"). C: Default is "select". Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tablet (tab): Returns true if the tablet device is present, false if it is absent
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
        - query (q): Query mode flag
    """
@overload #Overload for artSelectCtx in ['edit']
def artSelectCtx(accopacity: bool = ..., addselection: bool = ..., afterStrokeCmd: str = ..., beforeStrokeCmd: str = ..., brushalignment: bool = ..., brushfeedback: bool = ..., clear: bool = ..., dragSlider: str = ..., dynclonemode: bool = ..., expandfilename: bool = ..., exportaspectratio: float = ..., exportfilemode: str = ..., exportfilesave: str = ..., exportfilesizex: int = ..., exportfilesizey: int = ..., exportfiletype: str = ..., image1: str = ..., image2: str = ..., image3: str = ..., importfileload: str = ..., importfilemode: str = ..., importreassign: bool = ..., importthreshold: float = ..., lastRecorderCmd: str = ..., lastStampName: str = ..., lowerradius: float = ..., makeStroke: int = ..., mappressure: str = ..., opacity: float = ..., outline: bool = ..., outwhilepaint: bool = ..., paintmode: str = ..., paintoperationtype: str = ..., pickColor: bool = ..., pickValue: bool = ..., playbackCursor: [float, float] = ..., playbackPressure: float = ..., preserveclonesource: bool = ..., profileShapeFile: str = ..., projective: bool = ..., radius: float = ..., record: bool = ..., reflection: bool = ..., reflectionaboutorigin: bool = ..., reflectionaxis: str = ..., screenRadius: float = ..., selectall: bool = ..., selectclonesource: bool = ..., selectop: str = ..., showactive: bool = ..., stampDepth: float = ..., stampProfile: str = ..., stampSpacing: float = ..., strokesmooth: str = ..., surfaceConformedBrushVertices: bool = ..., tangentOutline: bool = ..., toggleall: bool = ..., unselectall: bool = ..., usepressure: bool = ..., worldRadius: float = ..., edit: bool = ...) -> None:
    """artSelectCtx is undoable, queryable, and editable.
    
    This command is used to select/deselect/toggle components on selected surfaces
    using a brush interface (Maya Artisan). Since, it selects components of the
    surface, it only works in the component mode.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new select context, then switch to it
        cmds.artSelectCtx('artSelectCtx1')
        cmds.setToolTo('artSelectCtx1')
        # Set brush's radius to 2.0, lower radius to 0.5
        cmds.artSelectCtx('artSelectCtx1', edit=True, r=2.0, lr=0.5)
    ```

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - addselection (ads): If true, each new stroke adds cvs to the active list. If false, each stroke replaces the previous selection. C: Default is true. Q: When queried, it returns a boole
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - clear (clr): Floods all cvs/vertices to the current value.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - exportaspectratio (ear): Value of aspect ratio for export
        - exportfilemode (efm): Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        - exportfilesave (esf): Exports the attribute map and saves to a specified file.
        - exportfilesizex (fsx): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfilesizey (fsy): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfiletype (eft): Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - importfileload (ifl): Load the attribute map a specified file.
        - importfilemode (ifm): Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        - importreassign (irm): Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        - importthreshold (ift): Specifies the threshold for the import of the attribute maps. C: Default is 0.5.  Q: When queried, it returns a float.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - screenRadius (scR): Brush radius on the screen
        - selectall (sal): Selects all vertices/egdes/faces/uvs.
        - selectclonesource (scs): Toggle on to select the clone source
        - selectop (sop): Specifies the selection operation ("select", "unselect", "toggle"). C: Default is "select". Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - toggleall (tal): Toggle all vertices/egdes/faces/uvs.
        - unselectall (ual): Unselects all vertices/egdes/faces/uvs.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
        - edit (e): Edit mode flag
    """
@overload #Overload for artSelectCtx in ['edit']
def artSelectCtx(aco: bool = ..., ads: bool = ..., asc: str = ..., bsc: str = ..., bra: bool = ..., brf: bool = ..., clr: bool = ..., dsl: str = ..., dcm: bool = ..., eef: bool = ..., ear: float = ..., efm: str = ..., esf: str = ..., fsx: int = ..., fsy: int = ..., eft: str = ..., i1: str = ..., i2: str = ..., i3: str = ..., ifl: str = ..., ifm: str = ..., irm: bool = ..., ift: float = ..., lrc: str = ..., lsn: str = ..., lr: float = ..., mst: int = ..., mp: str = ..., op: float = ..., o: bool = ..., owp: bool = ..., pm: str = ..., pot: str = ..., pcm: bool = ..., pv: bool = ..., plc: [float, float] = ..., plp: float = ..., pcs: bool = ..., psf: str = ..., prm: bool = ..., r: float = ..., rec: bool = ..., rn: bool = ..., rno: bool = ..., ra: str = ..., scR: float = ..., sal: bool = ..., scs: bool = ..., sop: str = ..., sa: bool = ..., stD: float = ..., stP: str = ..., stS: float = ..., ssm: str = ..., scv: bool = ..., to: bool = ..., tal: bool = ..., ual: bool = ..., up: bool = ..., wlR: float = ..., e: bool = ...) -> None:
    """artSelectCtx is undoable, queryable, and editable.
    
    This command is used to select/deselect/toggle components on selected surfaces
    using a brush interface (Maya Artisan). Since, it selects components of the
    surface, it only works in the component mode.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new select context, then switch to it
        cmds.artSelectCtx('artSelectCtx1')
        cmds.setToolTo('artSelectCtx1')
        # Set brush's radius to 2.0, lower radius to 0.5
        cmds.artSelectCtx('artSelectCtx1', edit=True, r=2.0, lr=0.5)
    ```

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - addselection (ads): If true, each new stroke adds cvs to the active list. If false, each stroke replaces the previous selection. C: Default is true. Q: When queried, it returns a boole
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - clear (clr): Floods all cvs/vertices to the current value.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - exportaspectratio (ear): Value of aspect ratio for export
        - exportfilemode (efm): Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        - exportfilesave (esf): Exports the attribute map and saves to a specified file.
        - exportfilesizex (fsx): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfilesizey (fsy): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfiletype (eft): Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - importfileload (ifl): Load the attribute map a specified file.
        - importfilemode (ifm): Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        - importreassign (irm): Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        - importthreshold (ift): Specifies the threshold for the import of the attribute maps. C: Default is 0.5.  Q: When queried, it returns a float.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - screenRadius (scR): Brush radius on the screen
        - selectall (sal): Selects all vertices/egdes/faces/uvs.
        - selectclonesource (scs): Toggle on to select the clone source
        - selectop (sop): Specifies the selection operation ("select", "unselect", "toggle"). C: Default is "select". Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - toggleall (tal): Toggle all vertices/egdes/faces/uvs.
        - unselectall (ual): Unselects all vertices/egdes/faces/uvs.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
        - edit (e): Edit mode flag
    """
@overload #Overload for artSelectCtx in ['edit']
def artSelectCtx(accopacity: bool = ..., aco: bool = ..., addselection: bool = ..., ads: bool = ..., afterStrokeCmd: str = ..., asc: str = ..., beforeStrokeCmd: str = ..., bsc: str = ..., brushalignment: bool = ..., bra: bool = ..., brushfeedback: bool = ..., brf: bool = ..., clear: bool = ..., clr: bool = ..., dragSlider: str = ..., dsl: str = ..., dynclonemode: bool = ..., dcm: bool = ..., expandfilename: bool = ..., eef: bool = ..., exportaspectratio: float = ..., ear: float = ..., exportfilemode: str = ..., efm: str = ..., exportfilesave: str = ..., esf: str = ..., exportfilesizex: int = ..., fsx: int = ..., exportfilesizey: int = ..., fsy: int = ..., exportfiletype: str = ..., eft: str = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., importfileload: str = ..., ifl: str = ..., importfilemode: str = ..., ifm: str = ..., importreassign: bool = ..., irm: bool = ..., importthreshold: float = ..., ift: float = ..., lastRecorderCmd: str = ..., lrc: str = ..., lastStampName: str = ..., lsn: str = ..., lowerradius: float = ..., lr: float = ..., makeStroke: int = ..., mst: int = ..., mappressure: str = ..., mp: str = ..., opacity: float = ..., op: float = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintmode: str = ..., pm: str = ..., paintoperationtype: str = ..., pot: str = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: [float, float] = ..., plc: [float, float] = ..., playbackPressure: float = ..., plp: float = ..., preserveclonesource: bool = ..., pcs: bool = ..., profileShapeFile: str = ..., psf: str = ..., projective: bool = ..., prm: bool = ..., radius: float = ..., r: float = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: str = ..., ra: str = ..., screenRadius: float = ..., scR: float = ..., selectall: bool = ..., sal: bool = ..., selectclonesource: bool = ..., scs: bool = ..., selectop: str = ..., sop: str = ..., showactive: bool = ..., sa: bool = ..., stampDepth: float = ..., stD: float = ..., stampProfile: str = ..., stP: str = ..., stampSpacing: float = ..., stS: float = ..., strokesmooth: str = ..., ssm: str = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tangentOutline: bool = ..., to: bool = ..., toggleall: bool = ..., tal: bool = ..., unselectall: bool = ..., ual: bool = ..., usepressure: bool = ..., up: bool = ..., worldRadius: float = ..., wlR: float = ..., edit: bool = ..., e: bool = ...) -> None:
    """artSelectCtx is undoable, queryable, and editable.
    
    This command is used to select/deselect/toggle components on selected surfaces
    using a brush interface (Maya Artisan). Since, it selects components of the
    surface, it only works in the component mode.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a new select context, then switch to it
        cmds.artSelectCtx('artSelectCtx1')
        cmds.setToolTo('artSelectCtx1')
        # Set brush's radius to 2.0, lower radius to 0.5
        cmds.artSelectCtx('artSelectCtx1', edit=True, r=2.0, lr=0.5)
    ```

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - addselection (ads): If true, each new stroke adds cvs to the active list. If false, each stroke replaces the previous selection. C: Default is true. Q: When queried, it returns a boole
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - clear (clr): Floods all cvs/vertices to the current value.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - exportaspectratio (ear): Value of aspect ratio for export
        - exportfilemode (efm): Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        - exportfilesave (esf): Exports the attribute map and saves to a specified file.
        - exportfilesizex (fsx): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfilesizey (fsy): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfiletype (eft): Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - importfileload (ifl): Load the attribute map a specified file.
        - importfilemode (ifm): Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        - importreassign (irm): Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        - importthreshold (ift): Specifies the threshold for the import of the attribute maps. C: Default is 0.5.  Q: When queried, it returns a float.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - screenRadius (scR): Brush radius on the screen
        - selectall (sal): Selects all vertices/egdes/faces/uvs.
        - selectclonesource (scs): Toggle on to select the clone source
        - selectop (sop): Specifies the selection operation ("select", "unselect", "toggle"). C: Default is "select". Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - toggleall (tal): Toggle all vertices/egdes/faces/uvs.
        - unselectall (ual): Unselects all vertices/egdes/faces/uvs.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
        - edit (e): Edit mode flag
    """
