"""Stub files for Contexts category in Maya commands, command: artSetPaintCtx."""

from typing import Any, overload

@overload #Overload for artSetPaintCtx in ['create']
def artSetPaintCtx(accopacity: bool = ..., afterStrokeCmd: str = ..., beforeStrokeCmd: str = ..., brushalignment: bool = ..., brushfeedback: bool = ..., clear: bool = ..., dragSlider: str = ..., dynclonemode: bool = ..., exists: bool = ..., expandfilename: bool = ..., exportaspectratio: float = ..., exportfilemode: str = ..., exportfilesizex: int = ..., exportfilesizey: int = ..., exportfiletype: str = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., importfilemode: str = ..., importreassign: bool = ..., lastRecorderCmd: str = ..., lastStampName: str = ..., lowerradius: float = ..., makeStroke: int = ..., mappressure: str = ..., name: str = ..., objectsetnames: str = ..., opacity: float = ..., outline: bool = ..., outwhilepaint: bool = ..., paintmode: str = ..., paintoperationtype: str = ..., pickColor: bool = ..., pickValue: bool = ..., playbackCursor: [float, float] = ..., playbackPressure: float = ..., preserveclonesource: bool = ..., profileShapeFile: str = ..., projective: bool = ..., radius: float = ..., record: bool = ..., reflection: bool = ..., reflectionaboutorigin: bool = ..., reflectionaxis: str = ..., screenRadius: float = ..., selectclonesource: bool = ..., setcolorfeedback: bool = ..., setdisplaycvs: bool = ..., setopertype: str = ..., settomodify: str = ..., showactive: bool = ..., stampDepth: float = ..., stampProfile: str = ..., stampSpacing: float = ..., strokesmooth: str = ..., surfaceConformedBrushVertices: bool = ..., tangentOutline: bool = ..., usepressure: bool = ..., worldRadius: float = ...) -> None:
    """artSetPaintCtx is undoable, queryable, and editable.
    
    This tool allows the user to modify the set membership (add, transfer, remove
    cvs) on nurbs surfaces using Maya Artisan's interface.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
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
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - name (n): If this is a tool command, name the tool appropriately.
        - objectsetnames (osn): Default name of object sets
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
        - setcolorfeedback (scf): Specifies if the color feedback is on or off. C: Default is ON.  Q: When queried, it returns a boolean.
        - setdisplaycvs (dcv): Specifies if the active cvs are displayed. C: Default is ON. Q: When queried, it returns a boolean.
        - setopertype (sot): Specifies the setEdit operation ("add", "transfer", "remove"). C: Default is "add". Q: When queried, it returns a string.
        - settomodify (stm): Specifies the name of the set to modify. Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
    """
@overload #Overload for artSetPaintCtx in ['create']
def artSetPaintCtx(aco: bool = ..., asc: str = ..., bsc: str = ..., bra: bool = ..., brf: bool = ..., clr: bool = ..., dsl: str = ..., dcm: bool = ..., ex: bool = ..., eef: bool = ..., ear: float = ..., efm: str = ..., fsx: int = ..., fsy: int = ..., eft: str = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ifm: str = ..., irm: bool = ..., lrc: str = ..., lsn: str = ..., lr: float = ..., mst: int = ..., mp: str = ..., n: str = ..., osn: str = ..., op: float = ..., o: bool = ..., owp: bool = ..., pm: str = ..., pot: str = ..., pcm: bool = ..., pv: bool = ..., plc: [float, float] = ..., plp: float = ..., pcs: bool = ..., psf: str = ..., prm: bool = ..., r: float = ..., rec: bool = ..., rn: bool = ..., rno: bool = ..., ra: str = ..., scR: float = ..., scs: bool = ..., scf: bool = ..., dcv: bool = ..., sot: str = ..., stm: str = ..., sa: bool = ..., stD: float = ..., stP: str = ..., stS: float = ..., ssm: str = ..., scv: bool = ..., to: bool = ..., up: bool = ..., wlR: float = ...) -> None:
    """artSetPaintCtx is undoable, queryable, and editable.
    
    This tool allows the user to modify the set membership (add, transfer, remove
    cvs) on nurbs surfaces using Maya Artisan's interface.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
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
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - name (n): If this is a tool command, name the tool appropriately.
        - objectsetnames (osn): Default name of object sets
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
        - setcolorfeedback (scf): Specifies if the color feedback is on or off. C: Default is ON.  Q: When queried, it returns a boolean.
        - setdisplaycvs (dcv): Specifies if the active cvs are displayed. C: Default is ON. Q: When queried, it returns a boolean.
        - setopertype (sot): Specifies the setEdit operation ("add", "transfer", "remove"). C: Default is "add". Q: When queried, it returns a string.
        - settomodify (stm): Specifies the name of the set to modify. Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
    """
@overload #Overload for artSetPaintCtx in ['create']
def artSetPaintCtx(accopacity: bool = ..., aco: bool = ..., afterStrokeCmd: str = ..., asc: str = ..., beforeStrokeCmd: str = ..., bsc: str = ..., brushalignment: bool = ..., bra: bool = ..., brushfeedback: bool = ..., brf: bool = ..., clear: bool = ..., clr: bool = ..., dragSlider: str = ..., dsl: str = ..., dynclonemode: bool = ..., dcm: bool = ..., exists: bool = ..., ex: bool = ..., expandfilename: bool = ..., eef: bool = ..., exportaspectratio: float = ..., ear: float = ..., exportfilemode: str = ..., efm: str = ..., exportfilesizex: int = ..., fsx: int = ..., exportfilesizey: int = ..., fsy: int = ..., exportfiletype: str = ..., eft: str = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., importfilemode: str = ..., ifm: str = ..., importreassign: bool = ..., irm: bool = ..., lastRecorderCmd: str = ..., lrc: str = ..., lastStampName: str = ..., lsn: str = ..., lowerradius: float = ..., lr: float = ..., makeStroke: int = ..., mst: int = ..., mappressure: str = ..., mp: str = ..., name: str = ..., n: str = ..., objectsetnames: str = ..., osn: str = ..., opacity: float = ..., op: float = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintmode: str = ..., pm: str = ..., paintoperationtype: str = ..., pot: str = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: [float, float] = ..., plc: [float, float] = ..., playbackPressure: float = ..., plp: float = ..., preserveclonesource: bool = ..., pcs: bool = ..., profileShapeFile: str = ..., psf: str = ..., projective: bool = ..., prm: bool = ..., radius: float = ..., r: float = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: str = ..., ra: str = ..., screenRadius: float = ..., scR: float = ..., selectclonesource: bool = ..., scs: bool = ..., setcolorfeedback: bool = ..., scf: bool = ..., setdisplaycvs: bool = ..., dcv: bool = ..., setopertype: str = ..., sot: str = ..., settomodify: str = ..., stm: str = ..., showactive: bool = ..., sa: bool = ..., stampDepth: float = ..., stD: float = ..., stampProfile: str = ..., stP: str = ..., stampSpacing: float = ..., stS: float = ..., strokesmooth: str = ..., ssm: str = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tangentOutline: bool = ..., to: bool = ..., usepressure: bool = ..., up: bool = ..., worldRadius: float = ..., wlR: float = ...) -> None:
    """artSetPaintCtx is undoable, queryable, and editable.
    
    This tool allows the user to modify the set membership (add, transfer, remove
    cvs) on nurbs surfaces using Maya Artisan's interface.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
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
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - name (n): If this is a tool command, name the tool appropriately.
        - objectsetnames (osn): Default name of object sets
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
        - setcolorfeedback (scf): Specifies if the color feedback is on or off. C: Default is ON.  Q: When queried, it returns a boolean.
        - setdisplaycvs (dcv): Specifies if the active cvs are displayed. C: Default is ON. Q: When queried, it returns a boolean.
        - setopertype (sot): Specifies the setEdit operation ("add", "transfer", "remove"). C: Default is "add". Q: When queried, it returns a string.
        - settomodify (stm): Specifies the name of the set to modify. Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
    """
@overload #Overload for artSetPaintCtx in ['query']
def artSetPaintCtx(accopacity: bool = ..., afterStrokeCmd: str = ..., beforeStrokeCmd: str = ..., brushalignment: bool = ..., brushfeedback: bool = ..., clear: bool = ..., dragSlider: str = ..., dynclonemode: bool = ..., expandfilename: bool = ..., exportaspectratio: float = ..., exportfilemode: str = ..., exportfilesizex: int = ..., exportfilesizey: int = ..., exportfiletype: str = ..., image1: str = ..., image2: str = ..., image3: str = ..., importfilemode: str = ..., importreassign: bool = ..., lastRecorderCmd: str = ..., lastStampName: str = ..., lowerradius: float = ..., makeStroke: int = ..., mappressure: str = ..., objectsetnames: str = ..., opacity: float = ..., outline: bool = ..., outwhilepaint: bool = ..., paintmode: str = ..., paintoperationtype: str = ..., pickColor: bool = ..., pickValue: bool = ..., playbackCursor: [float, float] = ..., playbackPressure: float = ..., preserveclonesource: bool = ..., profileShapeFile: str = ..., projective: bool = ..., radius: float = ..., record: bool = ..., reflection: bool = ..., reflectionaboutorigin: bool = ..., reflectionaxis: str = ..., screenRadius: float = ..., selectclonesource: bool = ..., setcolorfeedback: bool = ..., setdisplaycvs: bool = ..., setopertype: str = ..., settomodify: str = ..., showactive: bool = ..., stampDepth: float = ..., stampProfile: str = ..., stampSpacing: float = ..., strokesmooth: str = ..., surfaceConformedBrushVertices: bool = ..., tablet: bool = ..., tangentOutline: bool = ..., usepressure: bool = ..., worldRadius: float = ..., query: bool = ...) -> None:
    """artSetPaintCtx is undoable, queryable, and editable.
    
    This tool allows the user to modify the set membership (add, transfer, remove
    cvs) on nurbs surfaces using Maya Artisan's interface.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
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
        - exportfilesizex (fsx): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfilesizey (fsy): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfiletype (eft): Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - importfilemode (ifm): Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        - importreassign (irm): Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - objectsetnames (osn): Default name of object sets
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
        - setcolorfeedback (scf): Specifies if the color feedback is on or off. C: Default is ON.  Q: When queried, it returns a boolean.
        - setdisplaycvs (dcv): Specifies if the active cvs are displayed. C: Default is ON. Q: When queried, it returns a boolean.
        - setopertype (sot): Specifies the setEdit operation ("add", "transfer", "remove"). C: Default is "add". Q: When queried, it returns a string.
        - settomodify (stm): Specifies the name of the set to modify. Q: When queried, it returns a string.
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
@overload #Overload for artSetPaintCtx in ['query']
def artSetPaintCtx(aco: bool = ..., asc: str = ..., bsc: str = ..., bra: bool = ..., brf: bool = ..., clr: bool = ..., dsl: str = ..., dcm: bool = ..., eef: bool = ..., ear: float = ..., efm: str = ..., fsx: int = ..., fsy: int = ..., eft: str = ..., i1: str = ..., i2: str = ..., i3: str = ..., ifm: str = ..., irm: bool = ..., lrc: str = ..., lsn: str = ..., lr: float = ..., mst: int = ..., mp: str = ..., osn: str = ..., op: float = ..., o: bool = ..., owp: bool = ..., pm: str = ..., pot: str = ..., pcm: bool = ..., pv: bool = ..., plc: [float, float] = ..., plp: float = ..., pcs: bool = ..., psf: str = ..., prm: bool = ..., r: float = ..., rec: bool = ..., rn: bool = ..., rno: bool = ..., ra: str = ..., scR: float = ..., scs: bool = ..., scf: bool = ..., dcv: bool = ..., sot: str = ..., stm: str = ..., sa: bool = ..., stD: float = ..., stP: str = ..., stS: float = ..., ssm: str = ..., scv: bool = ..., tab: bool = ..., to: bool = ..., up: bool = ..., wlR: float = ..., q: bool = ...) -> None:
    """artSetPaintCtx is undoable, queryable, and editable.
    
    This tool allows the user to modify the set membership (add, transfer, remove
    cvs) on nurbs surfaces using Maya Artisan's interface.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
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
        - exportfilesizex (fsx): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfilesizey (fsy): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfiletype (eft): Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - importfilemode (ifm): Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        - importreassign (irm): Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - objectsetnames (osn): Default name of object sets
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
        - setcolorfeedback (scf): Specifies if the color feedback is on or off. C: Default is ON.  Q: When queried, it returns a boolean.
        - setdisplaycvs (dcv): Specifies if the active cvs are displayed. C: Default is ON. Q: When queried, it returns a boolean.
        - setopertype (sot): Specifies the setEdit operation ("add", "transfer", "remove"). C: Default is "add". Q: When queried, it returns a string.
        - settomodify (stm): Specifies the name of the set to modify. Q: When queried, it returns a string.
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
@overload #Overload for artSetPaintCtx in ['query']
def artSetPaintCtx(accopacity: bool = ..., aco: bool = ..., afterStrokeCmd: str = ..., asc: str = ..., beforeStrokeCmd: str = ..., bsc: str = ..., brushalignment: bool = ..., bra: bool = ..., brushfeedback: bool = ..., brf: bool = ..., clear: bool = ..., clr: bool = ..., dragSlider: str = ..., dsl: str = ..., dynclonemode: bool = ..., dcm: bool = ..., expandfilename: bool = ..., eef: bool = ..., exportaspectratio: float = ..., ear: float = ..., exportfilemode: str = ..., efm: str = ..., exportfilesizex: int = ..., fsx: int = ..., exportfilesizey: int = ..., fsy: int = ..., exportfiletype: str = ..., eft: str = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., importfilemode: str = ..., ifm: str = ..., importreassign: bool = ..., irm: bool = ..., lastRecorderCmd: str = ..., lrc: str = ..., lastStampName: str = ..., lsn: str = ..., lowerradius: float = ..., lr: float = ..., makeStroke: int = ..., mst: int = ..., mappressure: str = ..., mp: str = ..., objectsetnames: str = ..., osn: str = ..., opacity: float = ..., op: float = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintmode: str = ..., pm: str = ..., paintoperationtype: str = ..., pot: str = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: [float, float] = ..., plc: [float, float] = ..., playbackPressure: float = ..., plp: float = ..., preserveclonesource: bool = ..., pcs: bool = ..., profileShapeFile: str = ..., psf: str = ..., projective: bool = ..., prm: bool = ..., radius: float = ..., r: float = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: str = ..., ra: str = ..., screenRadius: float = ..., scR: float = ..., selectclonesource: bool = ..., scs: bool = ..., setcolorfeedback: bool = ..., scf: bool = ..., setdisplaycvs: bool = ..., dcv: bool = ..., setopertype: str = ..., sot: str = ..., settomodify: str = ..., stm: str = ..., showactive: bool = ..., sa: bool = ..., stampDepth: float = ..., stD: float = ..., stampProfile: str = ..., stP: str = ..., stampSpacing: float = ..., stS: float = ..., strokesmooth: str = ..., ssm: str = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tablet: bool = ..., tab: bool = ..., tangentOutline: bool = ..., to: bool = ..., usepressure: bool = ..., up: bool = ..., worldRadius: float = ..., wlR: float = ..., query: bool = ..., q: bool = ...) -> None:
    """artSetPaintCtx is undoable, queryable, and editable.
    
    This tool allows the user to modify the set membership (add, transfer, remove
    cvs) on nurbs surfaces using Maya Artisan's interface.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
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
        - exportfilesizex (fsx): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfilesizey (fsy): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfiletype (eft): Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - importfilemode (ifm): Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        - importreassign (irm): Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - objectsetnames (osn): Default name of object sets
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
        - setcolorfeedback (scf): Specifies if the color feedback is on or off. C: Default is ON.  Q: When queried, it returns a boolean.
        - setdisplaycvs (dcv): Specifies if the active cvs are displayed. C: Default is ON. Q: When queried, it returns a boolean.
        - setopertype (sot): Specifies the setEdit operation ("add", "transfer", "remove"). C: Default is "add". Q: When queried, it returns a string.
        - settomodify (stm): Specifies the name of the set to modify. Q: When queried, it returns a string.
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
@overload #Overload for artSetPaintCtx in ['edit']
def artSetPaintCtx(accopacity: bool = ..., afterStrokeCmd: str = ..., beforeStrokeCmd: str = ..., brushalignment: bool = ..., brushfeedback: bool = ..., clear: bool = ..., dragSlider: str = ..., dynclonemode: bool = ..., expandfilename: bool = ..., exportaspectratio: float = ..., exportfilemode: str = ..., exportfilesave: str = ..., exportfilesizex: int = ..., exportfilesizey: int = ..., exportfiletype: str = ..., image1: str = ..., image2: str = ..., image3: str = ..., importfileload: str = ..., importfilemode: str = ..., importreassign: bool = ..., lastRecorderCmd: str = ..., lastStampName: str = ..., lowerradius: float = ..., makeStroke: int = ..., mappressure: str = ..., objectsetnames: str = ..., opacity: float = ..., outline: bool = ..., outwhilepaint: bool = ..., paintmode: str = ..., paintoperationtype: str = ..., pickColor: bool = ..., pickValue: bool = ..., playbackCursor: [float, float] = ..., playbackPressure: float = ..., preserveclonesource: bool = ..., profileShapeFile: str = ..., projective: bool = ..., radius: float = ..., record: bool = ..., reflection: bool = ..., reflectionaboutorigin: bool = ..., reflectionaxis: str = ..., screenRadius: float = ..., selectclonesource: bool = ..., setcolorfeedback: bool = ..., setdisplaycvs: bool = ..., setopertype: str = ..., settomodify: str = ..., showactive: bool = ..., stampDepth: float = ..., stampProfile: str = ..., stampSpacing: float = ..., strokesmooth: str = ..., surfaceConformedBrushVertices: bool = ..., tangentOutline: bool = ..., usepressure: bool = ..., worldRadius: float = ..., edit: bool = ...) -> None:
    """artSetPaintCtx is undoable, queryable, and editable.
    
    This tool allows the user to modify the set membership (add, transfer, remove
    cvs) on nurbs surfaces using Maya Artisan's interface.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
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
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - objectsetnames (osn): Default name of object sets
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
        - setcolorfeedback (scf): Specifies if the color feedback is on or off. C: Default is ON.  Q: When queried, it returns a boolean.
        - setdisplaycvs (dcv): Specifies if the active cvs are displayed. C: Default is ON. Q: When queried, it returns a boolean.
        - setopertype (sot): Specifies the setEdit operation ("add", "transfer", "remove"). C: Default is "add". Q: When queried, it returns a string.
        - settomodify (stm): Specifies the name of the set to modify. Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
        - edit (e): Edit mode flag
    """
@overload #Overload for artSetPaintCtx in ['edit']
def artSetPaintCtx(aco: bool = ..., asc: str = ..., bsc: str = ..., bra: bool = ..., brf: bool = ..., clr: bool = ..., dsl: str = ..., dcm: bool = ..., eef: bool = ..., ear: float = ..., efm: str = ..., esf: str = ..., fsx: int = ..., fsy: int = ..., eft: str = ..., i1: str = ..., i2: str = ..., i3: str = ..., ifl: str = ..., ifm: str = ..., irm: bool = ..., lrc: str = ..., lsn: str = ..., lr: float = ..., mst: int = ..., mp: str = ..., osn: str = ..., op: float = ..., o: bool = ..., owp: bool = ..., pm: str = ..., pot: str = ..., pcm: bool = ..., pv: bool = ..., plc: [float, float] = ..., plp: float = ..., pcs: bool = ..., psf: str = ..., prm: bool = ..., r: float = ..., rec: bool = ..., rn: bool = ..., rno: bool = ..., ra: str = ..., scR: float = ..., scs: bool = ..., scf: bool = ..., dcv: bool = ..., sot: str = ..., stm: str = ..., sa: bool = ..., stD: float = ..., stP: str = ..., stS: float = ..., ssm: str = ..., scv: bool = ..., to: bool = ..., up: bool = ..., wlR: float = ..., e: bool = ...) -> None:
    """artSetPaintCtx is undoable, queryable, and editable.
    
    This tool allows the user to modify the set membership (add, transfer, remove
    cvs) on nurbs surfaces using Maya Artisan's interface.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
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
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - objectsetnames (osn): Default name of object sets
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
        - setcolorfeedback (scf): Specifies if the color feedback is on or off. C: Default is ON.  Q: When queried, it returns a boolean.
        - setdisplaycvs (dcv): Specifies if the active cvs are displayed. C: Default is ON. Q: When queried, it returns a boolean.
        - setopertype (sot): Specifies the setEdit operation ("add", "transfer", "remove"). C: Default is "add". Q: When queried, it returns a string.
        - settomodify (stm): Specifies the name of the set to modify. Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
        - edit (e): Edit mode flag
    """
@overload #Overload for artSetPaintCtx in ['edit']
def artSetPaintCtx(accopacity: bool = ..., aco: bool = ..., afterStrokeCmd: str = ..., asc: str = ..., beforeStrokeCmd: str = ..., bsc: str = ..., brushalignment: bool = ..., bra: bool = ..., brushfeedback: bool = ..., brf: bool = ..., clear: bool = ..., clr: bool = ..., dragSlider: str = ..., dsl: str = ..., dynclonemode: bool = ..., dcm: bool = ..., expandfilename: bool = ..., eef: bool = ..., exportaspectratio: float = ..., ear: float = ..., exportfilemode: str = ..., efm: str = ..., exportfilesave: str = ..., esf: str = ..., exportfilesizex: int = ..., fsx: int = ..., exportfilesizey: int = ..., fsy: int = ..., exportfiletype: str = ..., eft: str = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., importfileload: str = ..., ifl: str = ..., importfilemode: str = ..., ifm: str = ..., importreassign: bool = ..., irm: bool = ..., lastRecorderCmd: str = ..., lrc: str = ..., lastStampName: str = ..., lsn: str = ..., lowerradius: float = ..., lr: float = ..., makeStroke: int = ..., mst: int = ..., mappressure: str = ..., mp: str = ..., objectsetnames: str = ..., osn: str = ..., opacity: float = ..., op: float = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintmode: str = ..., pm: str = ..., paintoperationtype: str = ..., pot: str = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: [float, float] = ..., plc: [float, float] = ..., playbackPressure: float = ..., plp: float = ..., preserveclonesource: bool = ..., pcs: bool = ..., profileShapeFile: str = ..., psf: str = ..., projective: bool = ..., prm: bool = ..., radius: float = ..., r: float = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: str = ..., ra: str = ..., screenRadius: float = ..., scR: float = ..., selectclonesource: bool = ..., scs: bool = ..., setcolorfeedback: bool = ..., scf: bool = ..., setdisplaycvs: bool = ..., dcv: bool = ..., setopertype: str = ..., sot: str = ..., settomodify: str = ..., stm: str = ..., showactive: bool = ..., sa: bool = ..., stampDepth: float = ..., stD: float = ..., stampProfile: str = ..., stP: str = ..., stampSpacing: float = ..., stS: float = ..., strokesmooth: str = ..., ssm: str = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tangentOutline: bool = ..., to: bool = ..., usepressure: bool = ..., up: bool = ..., worldRadius: float = ..., wlR: float = ..., edit: bool = ..., e: bool = ...) -> None:
    """artSetPaintCtx is undoable, queryable, and editable.
    
    This tool allows the user to modify the set membership (add, transfer, remove
    cvs) on nurbs surfaces using Maya Artisan's interface.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
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
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - objectsetnames (osn): Default name of object sets
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
        - setcolorfeedback (scf): Specifies if the color feedback is on or off. C: Default is ON.  Q: When queried, it returns a boolean.
        - setdisplaycvs (dcv): Specifies if the active cvs are displayed. C: Default is ON. Q: When queried, it returns a boolean.
        - setopertype (sot): Specifies the setEdit operation ("add", "transfer", "remove"). C: Default is "add". Q: When queried, it returns a string.
        - settomodify (stm): Specifies the name of the set to modify. Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
        - edit (e): Edit mode flag
    """
