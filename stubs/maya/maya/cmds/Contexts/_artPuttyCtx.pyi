"""Stub files for Contexts category in Maya commands, command: artPuttyCtx."""

from typing import Any, overload

@overload #Overload for artPuttyCtx in ['create']
def artPuttyCtx(accopacity: bool = ..., activeListChangedProc: str = ..., afterStrokeCmd: str = ..., alphaclamp: str = ..., alphaclamplower: float = ..., alphaclampupper: float = ..., autosmooth: bool = ..., beforeStrokeCmd: str = ..., brushStrength: float = ..., brushalignment: bool = ..., brushfeedback: bool = ..., clamp: str = ..., clamplower: float = ..., clampupper: float = ..., clear: bool = ..., collapsecvtol: float = ..., colorAlphaValue: float = ..., colorRGBAValue: [float, float, float, float] = ..., colorRGBValue: [float, float, float] = ..., colorRamp: str = ..., colorfeedback: bool = ..., colorfeedbackOverride: bool = ..., colorrangelower: float = ..., colorrangeupper: float = ..., dataTypeIndex: int = ..., disablelighting: bool = ..., dispdecr: bool = ..., dispincr: bool = ..., dragSlider: str = ..., duringStrokeCmd: str = ..., dynclonemode: bool = ..., erasesrfupd: bool = ..., exists: bool = ..., expandfilename: bool = ..., exportaspectratio: float = ..., exportfilemode: str = ..., exportfilesizex: int = ..., exportfilesizey: int = ..., exportfiletype: str = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., importfilemode: str = ..., importreassign: bool = ..., interactiveUpdate: bool = ..., invertrefvector: bool = ..., lastRecorderCmd: str = ..., lastStampName: str = ..., lowerradius: float = ..., makeStroke: int = ..., mappressure: str = ..., maxdisp: float = ..., maxvalue: float = ..., minvalue: float = ..., mouldtypehead: str = ..., mouldtypemouse: str = ..., mouldtypetail: str = ..., name: str = ..., numericColorRamp: str = ..., numericDisplayColor: [float, float, float] = ..., numericDisplayPrecision: int = ..., numericMaxColor: [float, float, float] = ..., numericMinColor: [float, float, float] = ..., opacity: float = ..., outline: bool = ..., outwhilepaint: bool = ..., paintmode: str = ..., paintoperationtype: str = ..., pickColor: bool = ..., pickValue: bool = ..., playbackCursor: [float, float] = ..., playbackPressure: float = ..., polecv: bool = ..., preserveclonesource: bool = ..., profileShapeFile: str = ..., projective: bool = ..., radius: float = ..., rampMaxColor: [float, float, float] = ..., rampMinColor: [float, float, float] = ..., record: bool = ..., reflection: bool = ..., reflectionaboutorigin: bool = ..., reflectionaxis: str = ..., refsurface: bool = ..., refvector: str = ..., refvectoru: float = ..., refvectorv: float = ..., screenRadius: float = ..., selectclonesource: bool = ..., selectedattroper: str = ..., showactive: bool = ..., smoothiters: int = ..., stampDepth: float = ..., stampProfile: str = ..., stampSpacing: float = ..., stitchcorner: bool = ..., stitchtype: str = ..., strokesmooth: str = ..., surfaceConformedBrushVertices: bool = ..., tangentOutline: bool = ..., toolOffProc: str = ..., toolOnProc: str = ..., updateerasesrf: bool = ..., updaterefsrf: bool = ..., useColorRamp: bool = ..., useMaxMinColor: bool = ..., useNumericColorRamp: bool = ..., useNumericDisplay: bool = ..., usepressure: bool = ..., value: float = ..., whichTool: str = ..., worldRadius: float = ...) -> None:
    """artPuttyCtx is undoable, queryable, and editable.
    
    This is a context command to set the flags on the artAttrContext, which is the
    base context for attribute painting operations. All commands require the name
    of the context as the last argument as this provides the name of the context
    to create, edit or query.
    
    This command is used to modify NURBS surfaces using a brush based interface
    (Maya Artisan). This is accomplished by moving the control vertices (CVs)
    under the brush in the specified direction.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - activeListChangedProc (alp): Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode,
            the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphaclamp (alc): Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both"
            - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - alphaclamplower (acl): Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        - alphaclampupper (acu): Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        - autosmooth (asm): Sets up the auto smoothing option. When the brush is in the smooth mode, adjusting the strength will adjust how fast the surfaces is smoothed out. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushStrength (bs): Sets the strength of the brush. Brush strength is supported by the pinch and slide brushes. In pinch mode, adjusting the strength will adjust how quickly the surface converges on the brush center. In slide mode, the strength scales the
            motion of the brush. C: Default is 1.0.  Q: When queried, it returns a float.
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - clamp (cl): Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" -
            clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - clamplower (cll): Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        - clampupper (clu): Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        - clear (clr): Floods all cvs/vertices to the current value.
        - collapsecvtol (clc): Specifies the tolerance for the collapse cv detection. C: Default is 0.005 cm.  Q: When queried, it returns a float.
        - colorAlphaValue (cl1): The Alpha value of the color.
        - colorRGBAValue (cl4): The RGBA value of the color.
        - colorRGBValue (cl3): The RGB value of the color.
        - colorRamp (cr): Allows a user defined color ramp to be used to map values to colors.
        - colorfeedback (cf): Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorfeedbackOverride (cfo): Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorrangelower (crl): Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        - colorrangeupper (cru): Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        - dataTypeIndex (dti): When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        - disablelighting (dl): If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - dispdecr (dde): Decreases a maximum displacement by 10%.
        - dispincr (din): Increases a maximum displacement by 10%.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - duringStrokeCmd (dsk): The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - erasesrfupd (eut): Toggles the update for the erase surface
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
        - interactiveUpdate (iu): Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When
            queried, it returns a boolean.
        - invertrefvector (irv): Sets the invert of the reference vector option when the reflection is ON. If it is true, the reference vector for the reflected stroke is negated with respect to the original one. C: Default is FALSE. Q: When queried, it returns a boolean.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - maxdisp (md): Defines a maximum displacement ( maxDisp in [0.0..5.0] ). C: Default is 1.0.  Q: When queried, it returns a float.
        - maxvalue (mxv): Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        - minvalue (miv): Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - mouldtypehead (mth): Type of type mould to use
        - mouldtypemouse (mtm): Specifies the putty operations/mode ("push" - pushes CVs along the given direction (see refvector flag), "pull" - pulls CVs along the specified direction, "smooth" - smooths the sculpt, "erase" - erases the paint). C: Default is "push".  Q:
            When queried, it returns a string.
        - mouldtypetail (mtt): Type of eraser mould to use
        - name (n): If this is a tool command, name the tool appropriately.
        - numericColorRamp (ncr): Allows a user defined color ramp to be used to map values to colors for the numeric display.
        - numericDisplayColor (ndc): Defines a color to be used when displaying numeric values.
        - numericDisplayPrecision (ndp): Specifies how many decimal points of precision should be used for the numeric display.
        - numericMaxColor (nxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - numericMinColor (nmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - polecv (pcv): Pull all the pole CVs to the same position.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - rampMaxColor (rxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - rampMinColor (rmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - refsurface (rs): Sets on/off the update of the reference surface. If it is true the reference surface is automatically updated on the per stroke bases. If it is false, the user has to update the reference surface explicitly by pressing the update button
            (see updaterefsrf). C: Default is TRUE.  Q: When queried, it returns a boolean.
        - refvector (rv): Specifies the direction of the push/pull operation ("normal" - sculpt along normals, "firstnormal" - sculpt along the first normal of the stroke, "view" - sculpt along the view direction, "xaxis", "yaxis", "zaxis" - sculpt along a given
            axis directions, "uisoparm", "visoparm" - sculpt along U or V isoparametric lines), "uvvector" - sculpt along an arbitrary vector in UV space. C: Default is "normal".  Q: When queried, it returns a string.
        - refvectoru (rvu): Specifies the U component of the UV vector to be used when -refVector is set to "uvvector".
        - refvectorv (rvv): Specifies the V component of the UV vector to be used when -refVector is set to "uvvector".
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - selectedattroper (sao): Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the
            weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - smoothiters (si): Sets the quality of the smoothing operation (number of iterations). C: Default is 3.  Q: When queried, it returns an int.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - stitchcorner (stc): Sets on/off the stitching corner mode C: Default is "off".  Q: When queried, it returns a boolean.
        - stitchtype (stt): Sets on/off the stitching mode ( "off" - stitching is turned off, "position" - position stitching is done without taking care about the tangent continuity C0, "tan" - C1 continuity is preserved). C: Default is "position".  Q: When queried,
            it returns a string.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - toolOffProc (tfp): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL
            command is returned and this will be an empty string if none is defined.
        - toolOnProc (top): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command
            is returned and this will be an empty string if none is defined.
        - updateerasesrf (ues): Updates the erase surface.
        - updaterefsrf (urs): Updates the reference surface.
        - useColorRamp (ucr): Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        - useMaxMinColor (umc): Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        - useNumericColorRamp (unr): Specifies whether the user defined color ramp should be used to map values from to colors on the numeric display. If this is turned off, the set single numeric color will be used.
        - useNumericDisplay (und): Specifies whether numerical weight values should be displayed next to their associated control points.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - value (val): Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - whichTool (wst): The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last
            when specifying a flag that takes arguments.
        - worldRadius (wlR): Radius in worldspace
    """
@overload #Overload for artPuttyCtx in ['create']
def artPuttyCtx(aco: bool = ..., alp: str = ..., asc: str = ..., alc: str = ..., acl: float = ..., acu: float = ..., asm: bool = ..., bsc: str = ..., bs: float = ..., bra: bool = ..., brf: bool = ..., cl: str = ..., cll: float = ..., clu: float = ..., clr: bool = ..., clc: float = ..., cl1: float = ..., cl4: [float, float, float, float] = ..., cl3: [float, float, float] = ..., cr: str = ..., cf: bool = ..., cfo: bool = ..., crl: float = ..., cru: float = ..., dti: int = ..., dl: bool = ..., dde: bool = ..., din: bool = ..., dsl: str = ..., dsk: str = ..., dcm: bool = ..., eut: bool = ..., ex: bool = ..., eef: bool = ..., ear: float = ..., efm: str = ..., fsx: int = ..., fsy: int = ..., eft: str = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ifm: str = ..., irm: bool = ..., iu: bool = ..., irv: bool = ..., lrc: str = ..., lsn: str = ..., lr: float = ..., mst: int = ..., mp: str = ..., md: float = ..., mxv: float = ..., miv: float = ..., mth: str = ..., mtm: str = ..., mtt: str = ..., n: str = ..., ncr: str = ..., ndc: [float, float, float] = ..., ndp: int = ..., nxc: [float, float, float] = ..., nmc: [float, float, float] = ..., op: float = ..., o: bool = ..., owp: bool = ..., pm: str = ..., pot: str = ..., pcm: bool = ..., pv: bool = ..., plc: [float, float] = ..., plp: float = ..., pcv: bool = ..., pcs: bool = ..., psf: str = ..., prm: bool = ..., r: float = ..., rxc: [float, float, float] = ..., rmc: [float, float, float] = ..., rec: bool = ..., rn: bool = ..., rno: bool = ..., ra: str = ..., rs: bool = ..., rv: str = ..., rvu: float = ..., rvv: float = ..., scR: float = ..., scs: bool = ..., sao: str = ..., sa: bool = ..., si: int = ..., stD: float = ..., stP: str = ..., stS: float = ..., stc: bool = ..., stt: str = ..., ssm: str = ..., scv: bool = ..., to: bool = ..., tfp: str = ..., top: str = ..., ues: bool = ..., urs: bool = ..., ucr: bool = ..., umc: bool = ..., unr: bool = ..., und: bool = ..., up: bool = ..., val: float = ..., wst: str = ..., wlR: float = ...) -> None:
    """artPuttyCtx is undoable, queryable, and editable.
    
    This is a context command to set the flags on the artAttrContext, which is the
    base context for attribute painting operations. All commands require the name
    of the context as the last argument as this provides the name of the context
    to create, edit or query.
    
    This command is used to modify NURBS surfaces using a brush based interface
    (Maya Artisan). This is accomplished by moving the control vertices (CVs)
    under the brush in the specified direction.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - activeListChangedProc (alp): Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode,
            the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphaclamp (alc): Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both"
            - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - alphaclamplower (acl): Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        - alphaclampupper (acu): Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        - autosmooth (asm): Sets up the auto smoothing option. When the brush is in the smooth mode, adjusting the strength will adjust how fast the surfaces is smoothed out. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushStrength (bs): Sets the strength of the brush. Brush strength is supported by the pinch and slide brushes. In pinch mode, adjusting the strength will adjust how quickly the surface converges on the brush center. In slide mode, the strength scales the
            motion of the brush. C: Default is 1.0.  Q: When queried, it returns a float.
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - clamp (cl): Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" -
            clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - clamplower (cll): Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        - clampupper (clu): Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        - clear (clr): Floods all cvs/vertices to the current value.
        - collapsecvtol (clc): Specifies the tolerance for the collapse cv detection. C: Default is 0.005 cm.  Q: When queried, it returns a float.
        - colorAlphaValue (cl1): The Alpha value of the color.
        - colorRGBAValue (cl4): The RGBA value of the color.
        - colorRGBValue (cl3): The RGB value of the color.
        - colorRamp (cr): Allows a user defined color ramp to be used to map values to colors.
        - colorfeedback (cf): Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorfeedbackOverride (cfo): Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorrangelower (crl): Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        - colorrangeupper (cru): Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        - dataTypeIndex (dti): When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        - disablelighting (dl): If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - dispdecr (dde): Decreases a maximum displacement by 10%.
        - dispincr (din): Increases a maximum displacement by 10%.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - duringStrokeCmd (dsk): The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - erasesrfupd (eut): Toggles the update for the erase surface
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
        - interactiveUpdate (iu): Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When
            queried, it returns a boolean.
        - invertrefvector (irv): Sets the invert of the reference vector option when the reflection is ON. If it is true, the reference vector for the reflected stroke is negated with respect to the original one. C: Default is FALSE. Q: When queried, it returns a boolean.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - maxdisp (md): Defines a maximum displacement ( maxDisp in [0.0..5.0] ). C: Default is 1.0.  Q: When queried, it returns a float.
        - maxvalue (mxv): Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        - minvalue (miv): Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - mouldtypehead (mth): Type of type mould to use
        - mouldtypemouse (mtm): Specifies the putty operations/mode ("push" - pushes CVs along the given direction (see refvector flag), "pull" - pulls CVs along the specified direction, "smooth" - smooths the sculpt, "erase" - erases the paint). C: Default is "push".  Q:
            When queried, it returns a string.
        - mouldtypetail (mtt): Type of eraser mould to use
        - name (n): If this is a tool command, name the tool appropriately.
        - numericColorRamp (ncr): Allows a user defined color ramp to be used to map values to colors for the numeric display.
        - numericDisplayColor (ndc): Defines a color to be used when displaying numeric values.
        - numericDisplayPrecision (ndp): Specifies how many decimal points of precision should be used for the numeric display.
        - numericMaxColor (nxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - numericMinColor (nmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - polecv (pcv): Pull all the pole CVs to the same position.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - rampMaxColor (rxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - rampMinColor (rmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - refsurface (rs): Sets on/off the update of the reference surface. If it is true the reference surface is automatically updated on the per stroke bases. If it is false, the user has to update the reference surface explicitly by pressing the update button
            (see updaterefsrf). C: Default is TRUE.  Q: When queried, it returns a boolean.
        - refvector (rv): Specifies the direction of the push/pull operation ("normal" - sculpt along normals, "firstnormal" - sculpt along the first normal of the stroke, "view" - sculpt along the view direction, "xaxis", "yaxis", "zaxis" - sculpt along a given
            axis directions, "uisoparm", "visoparm" - sculpt along U or V isoparametric lines), "uvvector" - sculpt along an arbitrary vector in UV space. C: Default is "normal".  Q: When queried, it returns a string.
        - refvectoru (rvu): Specifies the U component of the UV vector to be used when -refVector is set to "uvvector".
        - refvectorv (rvv): Specifies the V component of the UV vector to be used when -refVector is set to "uvvector".
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - selectedattroper (sao): Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the
            weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - smoothiters (si): Sets the quality of the smoothing operation (number of iterations). C: Default is 3.  Q: When queried, it returns an int.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - stitchcorner (stc): Sets on/off the stitching corner mode C: Default is "off".  Q: When queried, it returns a boolean.
        - stitchtype (stt): Sets on/off the stitching mode ( "off" - stitching is turned off, "position" - position stitching is done without taking care about the tangent continuity C0, "tan" - C1 continuity is preserved). C: Default is "position".  Q: When queried,
            it returns a string.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - toolOffProc (tfp): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL
            command is returned and this will be an empty string if none is defined.
        - toolOnProc (top): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command
            is returned and this will be an empty string if none is defined.
        - updateerasesrf (ues): Updates the erase surface.
        - updaterefsrf (urs): Updates the reference surface.
        - useColorRamp (ucr): Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        - useMaxMinColor (umc): Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        - useNumericColorRamp (unr): Specifies whether the user defined color ramp should be used to map values from to colors on the numeric display. If this is turned off, the set single numeric color will be used.
        - useNumericDisplay (und): Specifies whether numerical weight values should be displayed next to their associated control points.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - value (val): Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - whichTool (wst): The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last
            when specifying a flag that takes arguments.
        - worldRadius (wlR): Radius in worldspace
    """
@overload #Overload for artPuttyCtx in ['create']
def artPuttyCtx(accopacity: bool = ..., aco: bool = ..., activeListChangedProc: str = ..., alp: str = ..., afterStrokeCmd: str = ..., asc: str = ..., alphaclamp: str = ..., alc: str = ..., alphaclamplower: float = ..., acl: float = ..., alphaclampupper: float = ..., acu: float = ..., autosmooth: bool = ..., asm: bool = ..., beforeStrokeCmd: str = ..., bsc: str = ..., brushStrength: float = ..., bs: float = ..., brushalignment: bool = ..., bra: bool = ..., brushfeedback: bool = ..., brf: bool = ..., clamp: str = ..., cl: str = ..., clamplower: float = ..., cll: float = ..., clampupper: float = ..., clu: float = ..., clear: bool = ..., clr: bool = ..., collapsecvtol: float = ..., clc: float = ..., colorAlphaValue: float = ..., cl1: float = ..., colorRGBAValue: [float, float, float, float] = ..., cl4: [float, float, float, float] = ..., colorRGBValue: [float, float, float] = ..., cl3: [float, float, float] = ..., colorRamp: str = ..., cr: str = ..., colorfeedback: bool = ..., cf: bool = ..., colorfeedbackOverride: bool = ..., cfo: bool = ..., colorrangelower: float = ..., crl: float = ..., colorrangeupper: float = ..., cru: float = ..., dataTypeIndex: int = ..., dti: int = ..., disablelighting: bool = ..., dl: bool = ..., dispdecr: bool = ..., dde: bool = ..., dispincr: bool = ..., din: bool = ..., dragSlider: str = ..., dsl: str = ..., duringStrokeCmd: str = ..., dsk: str = ..., dynclonemode: bool = ..., dcm: bool = ..., erasesrfupd: bool = ..., eut: bool = ..., exists: bool = ..., ex: bool = ..., expandfilename: bool = ..., eef: bool = ..., exportaspectratio: float = ..., ear: float = ..., exportfilemode: str = ..., efm: str = ..., exportfilesizex: int = ..., fsx: int = ..., exportfilesizey: int = ..., fsy: int = ..., exportfiletype: str = ..., eft: str = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., importfilemode: str = ..., ifm: str = ..., importreassign: bool = ..., irm: bool = ..., interactiveUpdate: bool = ..., iu: bool = ..., invertrefvector: bool = ..., irv: bool = ..., lastRecorderCmd: str = ..., lrc: str = ..., lastStampName: str = ..., lsn: str = ..., lowerradius: float = ..., lr: float = ..., makeStroke: int = ..., mst: int = ..., mappressure: str = ..., mp: str = ..., maxdisp: float = ..., md: float = ..., maxvalue: float = ..., mxv: float = ..., minvalue: float = ..., miv: float = ..., mouldtypehead: str = ..., mth: str = ..., mouldtypemouse: str = ..., mtm: str = ..., mouldtypetail: str = ..., mtt: str = ..., name: str = ..., n: str = ..., numericColorRamp: str = ..., ncr: str = ..., numericDisplayColor: [float, float, float] = ..., ndc: [float, float, float] = ..., numericDisplayPrecision: int = ..., ndp: int = ..., numericMaxColor: [float, float, float] = ..., nxc: [float, float, float] = ..., numericMinColor: [float, float, float] = ..., nmc: [float, float, float] = ..., opacity: float = ..., op: float = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintmode: str = ..., pm: str = ..., paintoperationtype: str = ..., pot: str = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: [float, float] = ..., plc: [float, float] = ..., playbackPressure: float = ..., plp: float = ..., polecv: bool = ..., pcv: bool = ..., preserveclonesource: bool = ..., pcs: bool = ..., profileShapeFile: str = ..., psf: str = ..., projective: bool = ..., prm: bool = ..., radius: float = ..., r: float = ..., rampMaxColor: [float, float, float] = ..., rxc: [float, float, float] = ..., rampMinColor: [float, float, float] = ..., rmc: [float, float, float] = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: str = ..., ra: str = ..., refsurface: bool = ..., rs: bool = ..., refvector: str = ..., rv: str = ..., refvectoru: float = ..., rvu: float = ..., refvectorv: float = ..., rvv: float = ..., screenRadius: float = ..., scR: float = ..., selectclonesource: bool = ..., scs: bool = ..., selectedattroper: str = ..., sao: str = ..., showactive: bool = ..., sa: bool = ..., smoothiters: int = ..., si: int = ..., stampDepth: float = ..., stD: float = ..., stampProfile: str = ..., stP: str = ..., stampSpacing: float = ..., stS: float = ..., stitchcorner: bool = ..., stc: bool = ..., stitchtype: str = ..., stt: str = ..., strokesmooth: str = ..., ssm: str = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tangentOutline: bool = ..., to: bool = ..., toolOffProc: str = ..., tfp: str = ..., toolOnProc: str = ..., top: str = ..., updateerasesrf: bool = ..., ues: bool = ..., updaterefsrf: bool = ..., urs: bool = ..., useColorRamp: bool = ..., ucr: bool = ..., useMaxMinColor: bool = ..., umc: bool = ..., useNumericColorRamp: bool = ..., unr: bool = ..., useNumericDisplay: bool = ..., und: bool = ..., usepressure: bool = ..., up: bool = ..., value: float = ..., val: float = ..., whichTool: str = ..., wst: str = ..., worldRadius: float = ..., wlR: float = ...) -> None:
    """artPuttyCtx is undoable, queryable, and editable.
    
    This is a context command to set the flags on the artAttrContext, which is the
    base context for attribute painting operations. All commands require the name
    of the context as the last argument as this provides the name of the context
    to create, edit or query.
    
    This command is used to modify NURBS surfaces using a brush based interface
    (Maya Artisan). This is accomplished by moving the control vertices (CVs)
    under the brush in the specified direction.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - activeListChangedProc (alp): Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode,
            the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphaclamp (alc): Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both"
            - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - alphaclamplower (acl): Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        - alphaclampupper (acu): Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        - autosmooth (asm): Sets up the auto smoothing option. When the brush is in the smooth mode, adjusting the strength will adjust how fast the surfaces is smoothed out. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushStrength (bs): Sets the strength of the brush. Brush strength is supported by the pinch and slide brushes. In pinch mode, adjusting the strength will adjust how quickly the surface converges on the brush center. In slide mode, the strength scales the
            motion of the brush. C: Default is 1.0.  Q: When queried, it returns a float.
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - clamp (cl): Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" -
            clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - clamplower (cll): Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        - clampupper (clu): Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        - clear (clr): Floods all cvs/vertices to the current value.
        - collapsecvtol (clc): Specifies the tolerance for the collapse cv detection. C: Default is 0.005 cm.  Q: When queried, it returns a float.
        - colorAlphaValue (cl1): The Alpha value of the color.
        - colorRGBAValue (cl4): The RGBA value of the color.
        - colorRGBValue (cl3): The RGB value of the color.
        - colorRamp (cr): Allows a user defined color ramp to be used to map values to colors.
        - colorfeedback (cf): Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorfeedbackOverride (cfo): Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorrangelower (crl): Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        - colorrangeupper (cru): Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        - dataTypeIndex (dti): When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        - disablelighting (dl): If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - dispdecr (dde): Decreases a maximum displacement by 10%.
        - dispincr (din): Increases a maximum displacement by 10%.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - duringStrokeCmd (dsk): The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - erasesrfupd (eut): Toggles the update for the erase surface
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
        - interactiveUpdate (iu): Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When
            queried, it returns a boolean.
        - invertrefvector (irv): Sets the invert of the reference vector option when the reflection is ON. If it is true, the reference vector for the reflected stroke is negated with respect to the original one. C: Default is FALSE. Q: When queried, it returns a boolean.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - maxdisp (md): Defines a maximum displacement ( maxDisp in [0.0..5.0] ). C: Default is 1.0.  Q: When queried, it returns a float.
        - maxvalue (mxv): Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        - minvalue (miv): Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - mouldtypehead (mth): Type of type mould to use
        - mouldtypemouse (mtm): Specifies the putty operations/mode ("push" - pushes CVs along the given direction (see refvector flag), "pull" - pulls CVs along the specified direction, "smooth" - smooths the sculpt, "erase" - erases the paint). C: Default is "push".  Q:
            When queried, it returns a string.
        - mouldtypetail (mtt): Type of eraser mould to use
        - name (n): If this is a tool command, name the tool appropriately.
        - numericColorRamp (ncr): Allows a user defined color ramp to be used to map values to colors for the numeric display.
        - numericDisplayColor (ndc): Defines a color to be used when displaying numeric values.
        - numericDisplayPrecision (ndp): Specifies how many decimal points of precision should be used for the numeric display.
        - numericMaxColor (nxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - numericMinColor (nmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - polecv (pcv): Pull all the pole CVs to the same position.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - rampMaxColor (rxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - rampMinColor (rmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - refsurface (rs): Sets on/off the update of the reference surface. If it is true the reference surface is automatically updated on the per stroke bases. If it is false, the user has to update the reference surface explicitly by pressing the update button
            (see updaterefsrf). C: Default is TRUE.  Q: When queried, it returns a boolean.
        - refvector (rv): Specifies the direction of the push/pull operation ("normal" - sculpt along normals, "firstnormal" - sculpt along the first normal of the stroke, "view" - sculpt along the view direction, "xaxis", "yaxis", "zaxis" - sculpt along a given
            axis directions, "uisoparm", "visoparm" - sculpt along U or V isoparametric lines), "uvvector" - sculpt along an arbitrary vector in UV space. C: Default is "normal".  Q: When queried, it returns a string.
        - refvectoru (rvu): Specifies the U component of the UV vector to be used when -refVector is set to "uvvector".
        - refvectorv (rvv): Specifies the V component of the UV vector to be used when -refVector is set to "uvvector".
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - selectedattroper (sao): Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the
            weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - smoothiters (si): Sets the quality of the smoothing operation (number of iterations). C: Default is 3.  Q: When queried, it returns an int.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - stitchcorner (stc): Sets on/off the stitching corner mode C: Default is "off".  Q: When queried, it returns a boolean.
        - stitchtype (stt): Sets on/off the stitching mode ( "off" - stitching is turned off, "position" - position stitching is done without taking care about the tangent continuity C0, "tan" - C1 continuity is preserved). C: Default is "position".  Q: When queried,
            it returns a string.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - toolOffProc (tfp): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL
            command is returned and this will be an empty string if none is defined.
        - toolOnProc (top): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command
            is returned and this will be an empty string if none is defined.
        - updateerasesrf (ues): Updates the erase surface.
        - updaterefsrf (urs): Updates the reference surface.
        - useColorRamp (ucr): Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        - useMaxMinColor (umc): Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        - useNumericColorRamp (unr): Specifies whether the user defined color ramp should be used to map values from to colors on the numeric display. If this is turned off, the set single numeric color will be used.
        - useNumericDisplay (und): Specifies whether numerical weight values should be displayed next to their associated control points.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - value (val): Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - whichTool (wst): The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last
            when specifying a flag that takes arguments.
        - worldRadius (wlR): Radius in worldspace
    """
@overload #Overload for artPuttyCtx in ['query']
def artPuttyCtx(accopacity: bool = ..., activeListChangedProc: str = ..., afterStrokeCmd: str = ..., alphaclamp: str = ..., alphaclamplower: float = ..., alphaclampupper: float = ..., attrSelected: str = ..., autosmooth: bool = ..., beforeStrokeCmd: str = ..., brushStrength: float = ..., brushalignment: bool = ..., brushfeedback: bool = ..., clamp: str = ..., clamplower: float = ..., clampupper: float = ..., clear: bool = ..., collapsecvtol: float = ..., colorAlphaValue: float = ..., colorRGBAValue: [float, float, float, float] = ..., colorRGBValue: [float, float, float] = ..., colorRamp: str = ..., colorfeedback: bool = ..., colorfeedbackOverride: bool = ..., colorrangelower: float = ..., colorrangeupper: float = ..., dataTypeIndex: int = ..., disablelighting: bool = ..., dispdecr: bool = ..., dispincr: bool = ..., dragSlider: str = ..., duringStrokeCmd: str = ..., dynclonemode: bool = ..., erasesrfupd: bool = ..., expandfilename: bool = ..., exportaspectratio: float = ..., exportfilemode: str = ..., exportfilesizex: int = ..., exportfilesizey: int = ..., exportfiletype: str = ..., image1: str = ..., image2: str = ..., image3: str = ..., importfilemode: str = ..., importreassign: bool = ..., interactiveUpdate: bool = ..., invertrefvector: bool = ..., lastRecorderCmd: str = ..., lastStampName: str = ..., lowerradius: float = ..., makeStroke: int = ..., mappressure: str = ..., maxdisp: float = ..., maxvalue: float = ..., minvalue: float = ..., mouldtypehead: str = ..., mouldtypemouse: str = ..., mouldtypetail: str = ..., numericColorRamp: str = ..., numericDisplayColor: [float, float, float] = ..., numericDisplayPrecision: int = ..., numericMaxColor: [float, float, float] = ..., numericMinColor: [float, float, float] = ..., objattrArray: str = ..., objattrArrayNoMenu: str = ..., opacity: float = ..., outline: bool = ..., outwhilepaint: bool = ..., paintNodeArray: str = ..., paintmode: str = ..., paintoperationtype: str = ..., pickColor: bool = ..., pickValue: bool = ..., playbackCursor: [float, float] = ..., playbackPressure: float = ..., polecv: bool = ..., preserveclonesource: bool = ..., profileShapeFile: str = ..., projective: bool = ..., radius: float = ..., rampMaxColor: [float, float, float] = ..., rampMinColor: [float, float, float] = ..., record: bool = ..., reflection: bool = ..., reflectionaboutorigin: bool = ..., reflectionaxis: str = ..., refsurface: bool = ..., refvector: str = ..., refvectoru: float = ..., refvectorv: float = ..., screenRadius: float = ..., selectclonesource: bool = ..., selectedattroper: str = ..., showactive: bool = ..., smoothiters: int = ..., stampDepth: float = ..., stampProfile: str = ..., stampSpacing: float = ..., stitchcorner: bool = ..., stitchtype: str = ..., strokesmooth: str = ..., surfaceConformedBrushVertices: bool = ..., tablet: bool = ..., tangentOutline: bool = ..., toolOffProc: str = ..., toolOnProc: str = ..., updateerasesrf: bool = ..., updaterefsrf: bool = ..., useColorRamp: bool = ..., useMaxMinColor: bool = ..., useNumericColorRamp: bool = ..., useNumericDisplay: bool = ..., usepressure: bool = ..., value: float = ..., whichTool: str = ..., worldRadius: float = ..., query: bool = ...) -> None:
    """artPuttyCtx is undoable, queryable, and editable.
    
    This is a context command to set the flags on the artAttrContext, which is the
    base context for attribute painting operations. All commands require the name
    of the context as the last argument as this provides the name of the context
    to create, edit or query.
    
    This command is used to modify NURBS surfaces using a brush based interface
    (Maya Artisan). This is accomplished by moving the control vertices (CVs)
    under the brush in the specified direction.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - activeListChangedProc (alp): Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode,
            the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphaclamp (alc): Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both"
            - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - alphaclamplower (acl): Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        - alphaclampupper (acu): Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        - attrSelected (asl): Returns a name of the currently selected attribute. Q: When queried, it returns a string.
        - autosmooth (asm): Sets up the auto smoothing option. When the brush is in the smooth mode, adjusting the strength will adjust how fast the surfaces is smoothed out. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushStrength (bs): Sets the strength of the brush. Brush strength is supported by the pinch and slide brushes. In pinch mode, adjusting the strength will adjust how quickly the surface converges on the brush center. In slide mode, the strength scales the
            motion of the brush. C: Default is 1.0.  Q: When queried, it returns a float.
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - clamp (cl): Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" -
            clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - clamplower (cll): Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        - clampupper (clu): Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        - clear (clr): Floods all cvs/vertices to the current value.
        - collapsecvtol (clc): Specifies the tolerance for the collapse cv detection. C: Default is 0.005 cm.  Q: When queried, it returns a float.
        - colorAlphaValue (cl1): The Alpha value of the color.
        - colorRGBAValue (cl4): The RGBA value of the color.
        - colorRGBValue (cl3): The RGB value of the color.
        - colorRamp (cr): Allows a user defined color ramp to be used to map values to colors.
        - colorfeedback (cf): Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorfeedbackOverride (cfo): Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorrangelower (crl): Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        - colorrangeupper (cru): Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        - dataTypeIndex (dti): When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        - disablelighting (dl): If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - dispdecr (dde): Decreases a maximum displacement by 10%.
        - dispincr (din): Increases a maximum displacement by 10%.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - duringStrokeCmd (dsk): The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - erasesrfupd (eut): Toggles the update for the erase surface
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
        - interactiveUpdate (iu): Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When
            queried, it returns a boolean.
        - invertrefvector (irv): Sets the invert of the reference vector option when the reflection is ON. If it is true, the reference vector for the reflected stroke is negated with respect to the original one. C: Default is FALSE. Q: When queried, it returns a boolean.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - maxdisp (md): Defines a maximum displacement ( maxDisp in [0.0..5.0] ). C: Default is 1.0.  Q: When queried, it returns a float.
        - maxvalue (mxv): Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        - minvalue (miv): Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - mouldtypehead (mth): Type of type mould to use
        - mouldtypemouse (mtm): Specifies the putty operations/mode ("push" - pushes CVs along the given direction (see refvector flag), "pull" - pulls CVs along the specified direction, "smooth" - smooths the sculpt, "erase" - erases the paint). C: Default is "push".  Q:
            When queried, it returns a string.
        - mouldtypetail (mtt): Type of eraser mould to use
        - numericColorRamp (ncr): Allows a user defined color ramp to be used to map values to colors for the numeric display.
        - numericDisplayColor (ndc): Defines a color to be used when displaying numeric values.
        - numericDisplayPrecision (ndp): Specifies how many decimal points of precision should be used for the numeric display.
        - numericMaxColor (nxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - numericMinColor (nmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - objattrArray (oaa): An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.
        - objattrArrayNoMenu (oan): Returns an array of all paintable attributes in their original order. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintNodeArray (pna): An array of paintable nodes. Q: When queried, it returns a string.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - polecv (pcv): Pull all the pole CVs to the same position.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - rampMaxColor (rxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - rampMinColor (rmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - refsurface (rs): Sets on/off the update of the reference surface. If it is true the reference surface is automatically updated on the per stroke bases. If it is false, the user has to update the reference surface explicitly by pressing the update button
            (see updaterefsrf). C: Default is TRUE.  Q: When queried, it returns a boolean.
        - refvector (rv): Specifies the direction of the push/pull operation ("normal" - sculpt along normals, "firstnormal" - sculpt along the first normal of the stroke, "view" - sculpt along the view direction, "xaxis", "yaxis", "zaxis" - sculpt along a given
            axis directions, "uisoparm", "visoparm" - sculpt along U or V isoparametric lines), "uvvector" - sculpt along an arbitrary vector in UV space. C: Default is "normal".  Q: When queried, it returns a string.
        - refvectoru (rvu): Specifies the U component of the UV vector to be used when -refVector is set to "uvvector".
        - refvectorv (rvv): Specifies the V component of the UV vector to be used when -refVector is set to "uvvector".
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - selectedattroper (sao): Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the
            weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - smoothiters (si): Sets the quality of the smoothing operation (number of iterations). C: Default is 3.  Q: When queried, it returns an int.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - stitchcorner (stc): Sets on/off the stitching corner mode C: Default is "off".  Q: When queried, it returns a boolean.
        - stitchtype (stt): Sets on/off the stitching mode ( "off" - stitching is turned off, "position" - position stitching is done without taking care about the tangent continuity C0, "tan" - C1 continuity is preserved). C: Default is "position".  Q: When queried,
            it returns a string.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tablet (tab): Returns true if the tablet device is present, false if it is absent
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - toolOffProc (tfp): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL
            command is returned and this will be an empty string if none is defined.
        - toolOnProc (top): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command
            is returned and this will be an empty string if none is defined.
        - updateerasesrf (ues): Updates the erase surface.
        - updaterefsrf (urs): Updates the reference surface.
        - useColorRamp (ucr): Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        - useMaxMinColor (umc): Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        - useNumericColorRamp (unr): Specifies whether the user defined color ramp should be used to map values from to colors on the numeric display. If this is turned off, the set single numeric color will be used.
        - useNumericDisplay (und): Specifies whether numerical weight values should be displayed next to their associated control points.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - value (val): Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - whichTool (wst): The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last
            when specifying a flag that takes arguments.
        - worldRadius (wlR): Radius in worldspace
        - query (q): Query mode flag
    """
@overload #Overload for artPuttyCtx in ['query']
def artPuttyCtx(aco: bool = ..., alp: str = ..., asc: str = ..., alc: str = ..., acl: float = ..., acu: float = ..., asl: str = ..., asm: bool = ..., bsc: str = ..., bs: float = ..., bra: bool = ..., brf: bool = ..., cl: str = ..., cll: float = ..., clu: float = ..., clr: bool = ..., clc: float = ..., cl1: float = ..., cl4: [float, float, float, float] = ..., cl3: [float, float, float] = ..., cr: str = ..., cf: bool = ..., cfo: bool = ..., crl: float = ..., cru: float = ..., dti: int = ..., dl: bool = ..., dde: bool = ..., din: bool = ..., dsl: str = ..., dsk: str = ..., dcm: bool = ..., eut: bool = ..., eef: bool = ..., ear: float = ..., efm: str = ..., fsx: int = ..., fsy: int = ..., eft: str = ..., i1: str = ..., i2: str = ..., i3: str = ..., ifm: str = ..., irm: bool = ..., iu: bool = ..., irv: bool = ..., lrc: str = ..., lsn: str = ..., lr: float = ..., mst: int = ..., mp: str = ..., md: float = ..., mxv: float = ..., miv: float = ..., mth: str = ..., mtm: str = ..., mtt: str = ..., ncr: str = ..., ndc: [float, float, float] = ..., ndp: int = ..., nxc: [float, float, float] = ..., nmc: [float, float, float] = ..., oaa: str = ..., oan: str = ..., op: float = ..., o: bool = ..., owp: bool = ..., pna: str = ..., pm: str = ..., pot: str = ..., pcm: bool = ..., pv: bool = ..., plc: [float, float] = ..., plp: float = ..., pcv: bool = ..., pcs: bool = ..., psf: str = ..., prm: bool = ..., r: float = ..., rxc: [float, float, float] = ..., rmc: [float, float, float] = ..., rec: bool = ..., rn: bool = ..., rno: bool = ..., ra: str = ..., rs: bool = ..., rv: str = ..., rvu: float = ..., rvv: float = ..., scR: float = ..., scs: bool = ..., sao: str = ..., sa: bool = ..., si: int = ..., stD: float = ..., stP: str = ..., stS: float = ..., stc: bool = ..., stt: str = ..., ssm: str = ..., scv: bool = ..., tab: bool = ..., to: bool = ..., tfp: str = ..., top: str = ..., ues: bool = ..., urs: bool = ..., ucr: bool = ..., umc: bool = ..., unr: bool = ..., und: bool = ..., up: bool = ..., val: float = ..., wst: str = ..., wlR: float = ..., q: bool = ...) -> None:
    """artPuttyCtx is undoable, queryable, and editable.
    
    This is a context command to set the flags on the artAttrContext, which is the
    base context for attribute painting operations. All commands require the name
    of the context as the last argument as this provides the name of the context
    to create, edit or query.
    
    This command is used to modify NURBS surfaces using a brush based interface
    (Maya Artisan). This is accomplished by moving the control vertices (CVs)
    under the brush in the specified direction.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - activeListChangedProc (alp): Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode,
            the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphaclamp (alc): Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both"
            - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - alphaclamplower (acl): Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        - alphaclampupper (acu): Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        - attrSelected (asl): Returns a name of the currently selected attribute. Q: When queried, it returns a string.
        - autosmooth (asm): Sets up the auto smoothing option. When the brush is in the smooth mode, adjusting the strength will adjust how fast the surfaces is smoothed out. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushStrength (bs): Sets the strength of the brush. Brush strength is supported by the pinch and slide brushes. In pinch mode, adjusting the strength will adjust how quickly the surface converges on the brush center. In slide mode, the strength scales the
            motion of the brush. C: Default is 1.0.  Q: When queried, it returns a float.
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - clamp (cl): Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" -
            clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - clamplower (cll): Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        - clampupper (clu): Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        - clear (clr): Floods all cvs/vertices to the current value.
        - collapsecvtol (clc): Specifies the tolerance for the collapse cv detection. C: Default is 0.005 cm.  Q: When queried, it returns a float.
        - colorAlphaValue (cl1): The Alpha value of the color.
        - colorRGBAValue (cl4): The RGBA value of the color.
        - colorRGBValue (cl3): The RGB value of the color.
        - colorRamp (cr): Allows a user defined color ramp to be used to map values to colors.
        - colorfeedback (cf): Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorfeedbackOverride (cfo): Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorrangelower (crl): Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        - colorrangeupper (cru): Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        - dataTypeIndex (dti): When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        - disablelighting (dl): If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - dispdecr (dde): Decreases a maximum displacement by 10%.
        - dispincr (din): Increases a maximum displacement by 10%.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - duringStrokeCmd (dsk): The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - erasesrfupd (eut): Toggles the update for the erase surface
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
        - interactiveUpdate (iu): Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When
            queried, it returns a boolean.
        - invertrefvector (irv): Sets the invert of the reference vector option when the reflection is ON. If it is true, the reference vector for the reflected stroke is negated with respect to the original one. C: Default is FALSE. Q: When queried, it returns a boolean.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - maxdisp (md): Defines a maximum displacement ( maxDisp in [0.0..5.0] ). C: Default is 1.0.  Q: When queried, it returns a float.
        - maxvalue (mxv): Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        - minvalue (miv): Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - mouldtypehead (mth): Type of type mould to use
        - mouldtypemouse (mtm): Specifies the putty operations/mode ("push" - pushes CVs along the given direction (see refvector flag), "pull" - pulls CVs along the specified direction, "smooth" - smooths the sculpt, "erase" - erases the paint). C: Default is "push".  Q:
            When queried, it returns a string.
        - mouldtypetail (mtt): Type of eraser mould to use
        - numericColorRamp (ncr): Allows a user defined color ramp to be used to map values to colors for the numeric display.
        - numericDisplayColor (ndc): Defines a color to be used when displaying numeric values.
        - numericDisplayPrecision (ndp): Specifies how many decimal points of precision should be used for the numeric display.
        - numericMaxColor (nxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - numericMinColor (nmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - objattrArray (oaa): An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.
        - objattrArrayNoMenu (oan): Returns an array of all paintable attributes in their original order. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintNodeArray (pna): An array of paintable nodes. Q: When queried, it returns a string.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - polecv (pcv): Pull all the pole CVs to the same position.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - rampMaxColor (rxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - rampMinColor (rmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - refsurface (rs): Sets on/off the update of the reference surface. If it is true the reference surface is automatically updated on the per stroke bases. If it is false, the user has to update the reference surface explicitly by pressing the update button
            (see updaterefsrf). C: Default is TRUE.  Q: When queried, it returns a boolean.
        - refvector (rv): Specifies the direction of the push/pull operation ("normal" - sculpt along normals, "firstnormal" - sculpt along the first normal of the stroke, "view" - sculpt along the view direction, "xaxis", "yaxis", "zaxis" - sculpt along a given
            axis directions, "uisoparm", "visoparm" - sculpt along U or V isoparametric lines), "uvvector" - sculpt along an arbitrary vector in UV space. C: Default is "normal".  Q: When queried, it returns a string.
        - refvectoru (rvu): Specifies the U component of the UV vector to be used when -refVector is set to "uvvector".
        - refvectorv (rvv): Specifies the V component of the UV vector to be used when -refVector is set to "uvvector".
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - selectedattroper (sao): Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the
            weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - smoothiters (si): Sets the quality of the smoothing operation (number of iterations). C: Default is 3.  Q: When queried, it returns an int.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - stitchcorner (stc): Sets on/off the stitching corner mode C: Default is "off".  Q: When queried, it returns a boolean.
        - stitchtype (stt): Sets on/off the stitching mode ( "off" - stitching is turned off, "position" - position stitching is done without taking care about the tangent continuity C0, "tan" - C1 continuity is preserved). C: Default is "position".  Q: When queried,
            it returns a string.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tablet (tab): Returns true if the tablet device is present, false if it is absent
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - toolOffProc (tfp): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL
            command is returned and this will be an empty string if none is defined.
        - toolOnProc (top): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command
            is returned and this will be an empty string if none is defined.
        - updateerasesrf (ues): Updates the erase surface.
        - updaterefsrf (urs): Updates the reference surface.
        - useColorRamp (ucr): Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        - useMaxMinColor (umc): Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        - useNumericColorRamp (unr): Specifies whether the user defined color ramp should be used to map values from to colors on the numeric display. If this is turned off, the set single numeric color will be used.
        - useNumericDisplay (und): Specifies whether numerical weight values should be displayed next to their associated control points.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - value (val): Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - whichTool (wst): The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last
            when specifying a flag that takes arguments.
        - worldRadius (wlR): Radius in worldspace
        - query (q): Query mode flag
    """
@overload #Overload for artPuttyCtx in ['query']
def artPuttyCtx(accopacity: bool = ..., aco: bool = ..., activeListChangedProc: str = ..., alp: str = ..., afterStrokeCmd: str = ..., asc: str = ..., alphaclamp: str = ..., alc: str = ..., alphaclamplower: float = ..., acl: float = ..., alphaclampupper: float = ..., acu: float = ..., attrSelected: str = ..., asl: str = ..., autosmooth: bool = ..., asm: bool = ..., beforeStrokeCmd: str = ..., bsc: str = ..., brushStrength: float = ..., bs: float = ..., brushalignment: bool = ..., bra: bool = ..., brushfeedback: bool = ..., brf: bool = ..., clamp: str = ..., cl: str = ..., clamplower: float = ..., cll: float = ..., clampupper: float = ..., clu: float = ..., clear: bool = ..., clr: bool = ..., collapsecvtol: float = ..., clc: float = ..., colorAlphaValue: float = ..., cl1: float = ..., colorRGBAValue: [float, float, float, float] = ..., cl4: [float, float, float, float] = ..., colorRGBValue: [float, float, float] = ..., cl3: [float, float, float] = ..., colorRamp: str = ..., cr: str = ..., colorfeedback: bool = ..., cf: bool = ..., colorfeedbackOverride: bool = ..., cfo: bool = ..., colorrangelower: float = ..., crl: float = ..., colorrangeupper: float = ..., cru: float = ..., dataTypeIndex: int = ..., dti: int = ..., disablelighting: bool = ..., dl: bool = ..., dispdecr: bool = ..., dde: bool = ..., dispincr: bool = ..., din: bool = ..., dragSlider: str = ..., dsl: str = ..., duringStrokeCmd: str = ..., dsk: str = ..., dynclonemode: bool = ..., dcm: bool = ..., erasesrfupd: bool = ..., eut: bool = ..., expandfilename: bool = ..., eef: bool = ..., exportaspectratio: float = ..., ear: float = ..., exportfilemode: str = ..., efm: str = ..., exportfilesizex: int = ..., fsx: int = ..., exportfilesizey: int = ..., fsy: int = ..., exportfiletype: str = ..., eft: str = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., importfilemode: str = ..., ifm: str = ..., importreassign: bool = ..., irm: bool = ..., interactiveUpdate: bool = ..., iu: bool = ..., invertrefvector: bool = ..., irv: bool = ..., lastRecorderCmd: str = ..., lrc: str = ..., lastStampName: str = ..., lsn: str = ..., lowerradius: float = ..., lr: float = ..., makeStroke: int = ..., mst: int = ..., mappressure: str = ..., mp: str = ..., maxdisp: float = ..., md: float = ..., maxvalue: float = ..., mxv: float = ..., minvalue: float = ..., miv: float = ..., mouldtypehead: str = ..., mth: str = ..., mouldtypemouse: str = ..., mtm: str = ..., mouldtypetail: str = ..., mtt: str = ..., numericColorRamp: str = ..., ncr: str = ..., numericDisplayColor: [float, float, float] = ..., ndc: [float, float, float] = ..., numericDisplayPrecision: int = ..., ndp: int = ..., numericMaxColor: [float, float, float] = ..., nxc: [float, float, float] = ..., numericMinColor: [float, float, float] = ..., nmc: [float, float, float] = ..., objattrArray: str = ..., oaa: str = ..., objattrArrayNoMenu: str = ..., oan: str = ..., opacity: float = ..., op: float = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintNodeArray: str = ..., pna: str = ..., paintmode: str = ..., pm: str = ..., paintoperationtype: str = ..., pot: str = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: [float, float] = ..., plc: [float, float] = ..., playbackPressure: float = ..., plp: float = ..., polecv: bool = ..., pcv: bool = ..., preserveclonesource: bool = ..., pcs: bool = ..., profileShapeFile: str = ..., psf: str = ..., projective: bool = ..., prm: bool = ..., radius: float = ..., r: float = ..., rampMaxColor: [float, float, float] = ..., rxc: [float, float, float] = ..., rampMinColor: [float, float, float] = ..., rmc: [float, float, float] = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: str = ..., ra: str = ..., refsurface: bool = ..., rs: bool = ..., refvector: str = ..., rv: str = ..., refvectoru: float = ..., rvu: float = ..., refvectorv: float = ..., rvv: float = ..., screenRadius: float = ..., scR: float = ..., selectclonesource: bool = ..., scs: bool = ..., selectedattroper: str = ..., sao: str = ..., showactive: bool = ..., sa: bool = ..., smoothiters: int = ..., si: int = ..., stampDepth: float = ..., stD: float = ..., stampProfile: str = ..., stP: str = ..., stampSpacing: float = ..., stS: float = ..., stitchcorner: bool = ..., stc: bool = ..., stitchtype: str = ..., stt: str = ..., strokesmooth: str = ..., ssm: str = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tablet: bool = ..., tab: bool = ..., tangentOutline: bool = ..., to: bool = ..., toolOffProc: str = ..., tfp: str = ..., toolOnProc: str = ..., top: str = ..., updateerasesrf: bool = ..., ues: bool = ..., updaterefsrf: bool = ..., urs: bool = ..., useColorRamp: bool = ..., ucr: bool = ..., useMaxMinColor: bool = ..., umc: bool = ..., useNumericColorRamp: bool = ..., unr: bool = ..., useNumericDisplay: bool = ..., und: bool = ..., usepressure: bool = ..., up: bool = ..., value: float = ..., val: float = ..., whichTool: str = ..., wst: str = ..., worldRadius: float = ..., wlR: float = ..., query: bool = ..., q: bool = ...) -> None:
    """artPuttyCtx is undoable, queryable, and editable.
    
    This is a context command to set the flags on the artAttrContext, which is the
    base context for attribute painting operations. All commands require the name
    of the context as the last argument as this provides the name of the context
    to create, edit or query.
    
    This command is used to modify NURBS surfaces using a brush based interface
    (Maya Artisan). This is accomplished by moving the control vertices (CVs)
    under the brush in the specified direction.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - activeListChangedProc (alp): Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode,
            the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphaclamp (alc): Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both"
            - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - alphaclamplower (acl): Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        - alphaclampupper (acu): Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        - attrSelected (asl): Returns a name of the currently selected attribute. Q: When queried, it returns a string.
        - autosmooth (asm): Sets up the auto smoothing option. When the brush is in the smooth mode, adjusting the strength will adjust how fast the surfaces is smoothed out. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushStrength (bs): Sets the strength of the brush. Brush strength is supported by the pinch and slide brushes. In pinch mode, adjusting the strength will adjust how quickly the surface converges on the brush center. In slide mode, the strength scales the
            motion of the brush. C: Default is 1.0.  Q: When queried, it returns a float.
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - clamp (cl): Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" -
            clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - clamplower (cll): Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        - clampupper (clu): Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        - clear (clr): Floods all cvs/vertices to the current value.
        - collapsecvtol (clc): Specifies the tolerance for the collapse cv detection. C: Default is 0.005 cm.  Q: When queried, it returns a float.
        - colorAlphaValue (cl1): The Alpha value of the color.
        - colorRGBAValue (cl4): The RGBA value of the color.
        - colorRGBValue (cl3): The RGB value of the color.
        - colorRamp (cr): Allows a user defined color ramp to be used to map values to colors.
        - colorfeedback (cf): Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorfeedbackOverride (cfo): Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorrangelower (crl): Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        - colorrangeupper (cru): Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        - dataTypeIndex (dti): When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        - disablelighting (dl): If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - dispdecr (dde): Decreases a maximum displacement by 10%.
        - dispincr (din): Increases a maximum displacement by 10%.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - duringStrokeCmd (dsk): The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - erasesrfupd (eut): Toggles the update for the erase surface
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
        - interactiveUpdate (iu): Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When
            queried, it returns a boolean.
        - invertrefvector (irv): Sets the invert of the reference vector option when the reflection is ON. If it is true, the reference vector for the reflected stroke is negated with respect to the original one. C: Default is FALSE. Q: When queried, it returns a boolean.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - maxdisp (md): Defines a maximum displacement ( maxDisp in [0.0..5.0] ). C: Default is 1.0.  Q: When queried, it returns a float.
        - maxvalue (mxv): Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        - minvalue (miv): Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - mouldtypehead (mth): Type of type mould to use
        - mouldtypemouse (mtm): Specifies the putty operations/mode ("push" - pushes CVs along the given direction (see refvector flag), "pull" - pulls CVs along the specified direction, "smooth" - smooths the sculpt, "erase" - erases the paint). C: Default is "push".  Q:
            When queried, it returns a string.
        - mouldtypetail (mtt): Type of eraser mould to use
        - numericColorRamp (ncr): Allows a user defined color ramp to be used to map values to colors for the numeric display.
        - numericDisplayColor (ndc): Defines a color to be used when displaying numeric values.
        - numericDisplayPrecision (ndp): Specifies how many decimal points of precision should be used for the numeric display.
        - numericMaxColor (nxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - numericMinColor (nmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - objattrArray (oaa): An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.
        - objattrArrayNoMenu (oan): Returns an array of all paintable attributes in their original order. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintNodeArray (pna): An array of paintable nodes. Q: When queried, it returns a string.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - polecv (pcv): Pull all the pole CVs to the same position.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - rampMaxColor (rxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - rampMinColor (rmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - refsurface (rs): Sets on/off the update of the reference surface. If it is true the reference surface is automatically updated on the per stroke bases. If it is false, the user has to update the reference surface explicitly by pressing the update button
            (see updaterefsrf). C: Default is TRUE.  Q: When queried, it returns a boolean.
        - refvector (rv): Specifies the direction of the push/pull operation ("normal" - sculpt along normals, "firstnormal" - sculpt along the first normal of the stroke, "view" - sculpt along the view direction, "xaxis", "yaxis", "zaxis" - sculpt along a given
            axis directions, "uisoparm", "visoparm" - sculpt along U or V isoparametric lines), "uvvector" - sculpt along an arbitrary vector in UV space. C: Default is "normal".  Q: When queried, it returns a string.
        - refvectoru (rvu): Specifies the U component of the UV vector to be used when -refVector is set to "uvvector".
        - refvectorv (rvv): Specifies the V component of the UV vector to be used when -refVector is set to "uvvector".
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - selectedattroper (sao): Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the
            weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - smoothiters (si): Sets the quality of the smoothing operation (number of iterations). C: Default is 3.  Q: When queried, it returns an int.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - stitchcorner (stc): Sets on/off the stitching corner mode C: Default is "off".  Q: When queried, it returns a boolean.
        - stitchtype (stt): Sets on/off the stitching mode ( "off" - stitching is turned off, "position" - position stitching is done without taking care about the tangent continuity C0, "tan" - C1 continuity is preserved). C: Default is "position".  Q: When queried,
            it returns a string.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tablet (tab): Returns true if the tablet device is present, false if it is absent
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - toolOffProc (tfp): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL
            command is returned and this will be an empty string if none is defined.
        - toolOnProc (top): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command
            is returned and this will be an empty string if none is defined.
        - updateerasesrf (ues): Updates the erase surface.
        - updaterefsrf (urs): Updates the reference surface.
        - useColorRamp (ucr): Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        - useMaxMinColor (umc): Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        - useNumericColorRamp (unr): Specifies whether the user defined color ramp should be used to map values from to colors on the numeric display. If this is turned off, the set single numeric color will be used.
        - useNumericDisplay (und): Specifies whether numerical weight values should be displayed next to their associated control points.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - value (val): Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - whichTool (wst): The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last
            when specifying a flag that takes arguments.
        - worldRadius (wlR): Radius in worldspace
        - query (q): Query mode flag
    """
@overload #Overload for artPuttyCtx in ['edit']
def artPuttyCtx(accopacity: bool = ..., activeListChangedProc: str = ..., afterStrokeCmd: str = ..., alphaclamp: str = ..., alphaclamplower: float = ..., alphaclampupper: float = ..., autosmooth: bool = ..., beforeStrokeCmd: str = ..., brushStrength: float = ..., brushalignment: bool = ..., brushfeedback: bool = ..., clamp: str = ..., clamplower: float = ..., clampupper: float = ..., clear: bool = ..., collapsecvtol: float = ..., colorAlphaValue: float = ..., colorRGBAValue: [float, float, float, float] = ..., colorRGBValue: [float, float, float] = ..., colorRamp: str = ..., colorfeedback: bool = ..., colorfeedbackOverride: bool = ..., colorrangelower: float = ..., colorrangeupper: float = ..., dataTypeIndex: int = ..., disablelighting: bool = ..., dispdecr: bool = ..., dispincr: bool = ..., dragSlider: str = ..., duringStrokeCmd: str = ..., dynclonemode: bool = ..., erasesrfupd: bool = ..., expandfilename: bool = ..., exportaspectratio: float = ..., exportfilemode: str = ..., exportfilesave: str = ..., exportfilesizex: int = ..., exportfilesizey: int = ..., exportfiletype: str = ..., filterNodes: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., importfileload: str = ..., importfilemode: str = ..., importreassign: bool = ..., interactiveUpdate: bool = ..., invertrefvector: bool = ..., lastRecorderCmd: str = ..., lastStampName: str = ..., lowerradius: float = ..., makeStroke: int = ..., mappressure: str = ..., maxdisp: float = ..., maxvalue: float = ..., minvalue: float = ..., mouldtypehead: str = ..., mouldtypemouse: str = ..., mouldtypetail: str = ..., numericColorRamp: str = ..., numericDisplayColor: [float, float, float] = ..., numericDisplayPrecision: int = ..., numericMaxColor: [float, float, float] = ..., numericMinColor: [float, float, float] = ..., opacity: float = ..., outline: bool = ..., outwhilepaint: bool = ..., paintattrselected: str = ..., paintmode: str = ..., paintoperationtype: str = ..., pickColor: bool = ..., pickValue: bool = ..., playbackCursor: [float, float] = ..., playbackPressure: float = ..., polecv: bool = ..., preserveclonesource: bool = ..., profileShapeFile: str = ..., projective: bool = ..., radius: float = ..., rampMaxColor: [float, float, float] = ..., rampMinColor: [float, float, float] = ..., record: bool = ..., reflection: bool = ..., reflectionaboutorigin: bool = ..., reflectionaxis: str = ..., refsurface: bool = ..., refvector: str = ..., refvectoru: float = ..., refvectorv: float = ..., screenRadius: float = ..., selectclonesource: bool = ..., selectedattroper: str = ..., showactive: bool = ..., smoothiters: int = ..., stampDepth: float = ..., stampProfile: str = ..., stampSpacing: float = ..., stitchcorner: bool = ..., stitchedgeflood: bool = ..., stitchtype: str = ..., strokesmooth: str = ..., surfaceConformedBrushVertices: bool = ..., tangentOutline: bool = ..., toolOffProc: str = ..., toolOnProc: str = ..., updateerasesrf: bool = ..., updaterefsrf: bool = ..., useColorRamp: bool = ..., useMaxMinColor: bool = ..., useNumericColorRamp: bool = ..., useNumericDisplay: bool = ..., usepressure: bool = ..., value: float = ..., whichTool: str = ..., worldRadius: float = ..., edit: bool = ...) -> None:
    """artPuttyCtx is undoable, queryable, and editable.
    
    This is a context command to set the flags on the artAttrContext, which is the
    base context for attribute painting operations. All commands require the name
    of the context as the last argument as this provides the name of the context
    to create, edit or query.
    
    This command is used to modify NURBS surfaces using a brush based interface
    (Maya Artisan). This is accomplished by moving the control vertices (CVs)
    under the brush in the specified direction.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - activeListChangedProc (alp): Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode,
            the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphaclamp (alc): Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both"
            - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - alphaclamplower (acl): Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        - alphaclampupper (acu): Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        - autosmooth (asm): Sets up the auto smoothing option. When the brush is in the smooth mode, adjusting the strength will adjust how fast the surfaces is smoothed out. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushStrength (bs): Sets the strength of the brush. Brush strength is supported by the pinch and slide brushes. In pinch mode, adjusting the strength will adjust how quickly the surface converges on the brush center. In slide mode, the strength scales the
            motion of the brush. C: Default is 1.0.  Q: When queried, it returns a float.
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - clamp (cl): Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" -
            clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - clamplower (cll): Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        - clampupper (clu): Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        - clear (clr): Floods all cvs/vertices to the current value.
        - collapsecvtol (clc): Specifies the tolerance for the collapse cv detection. C: Default is 0.005 cm.  Q: When queried, it returns a float.
        - colorAlphaValue (cl1): The Alpha value of the color.
        - colorRGBAValue (cl4): The RGBA value of the color.
        - colorRGBValue (cl3): The RGB value of the color.
        - colorRamp (cr): Allows a user defined color ramp to be used to map values to colors.
        - colorfeedback (cf): Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorfeedbackOverride (cfo): Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorrangelower (crl): Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        - colorrangeupper (cru): Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        - dataTypeIndex (dti): When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        - disablelighting (dl): If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - dispdecr (dde): Decreases a maximum displacement by 10%.
        - dispincr (din): Increases a maximum displacement by 10%.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - duringStrokeCmd (dsk): The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - erasesrfupd (eut): Toggles the update for the erase surface
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - exportaspectratio (ear): Value of aspect ratio for export
        - exportfilemode (efm): Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        - exportfilesave (esf): Exports the attribute map and saves to a specified file.
        - exportfilesizex (fsx): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfilesizey (fsy): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfiletype (eft): Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        - filterNodes (fon): Sets the node filter.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - importfileload (ifl): Load the attribute map a specified file.
        - importfilemode (ifm): Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        - importreassign (irm): Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        - interactiveUpdate (iu): Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When
            queried, it returns a boolean.
        - invertrefvector (irv): Sets the invert of the reference vector option when the reflection is ON. If it is true, the reference vector for the reflected stroke is negated with respect to the original one. C: Default is FALSE. Q: When queried, it returns a boolean.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - maxdisp (md): Defines a maximum displacement ( maxDisp in [0.0..5.0] ). C: Default is 1.0.  Q: When queried, it returns a float.
        - maxvalue (mxv): Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        - minvalue (miv): Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - mouldtypehead (mth): Type of type mould to use
        - mouldtypemouse (mtm): Specifies the putty operations/mode ("push" - pushes CVs along the given direction (see refvector flag), "pull" - pulls CVs along the specified direction, "smooth" - smooths the sculpt, "erase" - erases the paint). C: Default is "push".  Q:
            When queried, it returns a string.
        - mouldtypetail (mtt): Type of eraser mould to use
        - numericColorRamp (ncr): Allows a user defined color ramp to be used to map values to colors for the numeric display.
        - numericDisplayColor (ndc): Defines a color to be used when displaying numeric values.
        - numericDisplayPrecision (ndp): Specifies how many decimal points of precision should be used for the numeric display.
        - numericMaxColor (nxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - numericMinColor (nmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintattrselected (pas): An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - polecv (pcv): Pull all the pole CVs to the same position.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - rampMaxColor (rxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - rampMinColor (rmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - refsurface (rs): Sets on/off the update of the reference surface. If it is true the reference surface is automatically updated on the per stroke bases. If it is false, the user has to update the reference surface explicitly by pressing the update button
            (see updaterefsrf). C: Default is TRUE.  Q: When queried, it returns a boolean.
        - refvector (rv): Specifies the direction of the push/pull operation ("normal" - sculpt along normals, "firstnormal" - sculpt along the first normal of the stroke, "view" - sculpt along the view direction, "xaxis", "yaxis", "zaxis" - sculpt along a given
            axis directions, "uisoparm", "visoparm" - sculpt along U or V isoparametric lines), "uvvector" - sculpt along an arbitrary vector in UV space. C: Default is "normal".  Q: When queried, it returns a string.
        - refvectoru (rvu): Specifies the U component of the UV vector to be used when -refVector is set to "uvvector".
        - refvectorv (rvv): Specifies the V component of the UV vector to be used when -refVector is set to "uvvector".
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - selectedattroper (sao): Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the
            weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - smoothiters (si): Sets the quality of the smoothing operation (number of iterations). C: Default is 3.  Q: When queried, it returns an int.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - stitchcorner (stc): Sets on/off the stitching corner mode C: Default is "off".  Q: When queried, it returns a boolean.
        - stitchedgeflood (sef): Triggers postprocessing stitching edge procedure.
        - stitchtype (stt): Sets on/off the stitching mode ( "off" - stitching is turned off, "position" - position stitching is done without taking care about the tangent continuity C0, "tan" - C1 continuity is preserved). C: Default is "position".  Q: When queried,
            it returns a string.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - toolOffProc (tfp): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL
            command is returned and this will be an empty string if none is defined.
        - toolOnProc (top): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command
            is returned and this will be an empty string if none is defined.
        - updateerasesrf (ues): Updates the erase surface.
        - updaterefsrf (urs): Updates the reference surface.
        - useColorRamp (ucr): Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        - useMaxMinColor (umc): Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        - useNumericColorRamp (unr): Specifies whether the user defined color ramp should be used to map values from to colors on the numeric display. If this is turned off, the set single numeric color will be used.
        - useNumericDisplay (und): Specifies whether numerical weight values should be displayed next to their associated control points.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - value (val): Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - whichTool (wst): The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last
            when specifying a flag that takes arguments.
        - worldRadius (wlR): Radius in worldspace
        - edit (e): Edit mode flag
    """
@overload #Overload for artPuttyCtx in ['edit']
def artPuttyCtx(aco: bool = ..., alp: str = ..., asc: str = ..., alc: str = ..., acl: float = ..., acu: float = ..., asm: bool = ..., bsc: str = ..., bs: float = ..., bra: bool = ..., brf: bool = ..., cl: str = ..., cll: float = ..., clu: float = ..., clr: bool = ..., clc: float = ..., cl1: float = ..., cl4: [float, float, float, float] = ..., cl3: [float, float, float] = ..., cr: str = ..., cf: bool = ..., cfo: bool = ..., crl: float = ..., cru: float = ..., dti: int = ..., dl: bool = ..., dde: bool = ..., din: bool = ..., dsl: str = ..., dsk: str = ..., dcm: bool = ..., eut: bool = ..., eef: bool = ..., ear: float = ..., efm: str = ..., esf: str = ..., fsx: int = ..., fsy: int = ..., eft: str = ..., fon: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ifl: str = ..., ifm: str = ..., irm: bool = ..., iu: bool = ..., irv: bool = ..., lrc: str = ..., lsn: str = ..., lr: float = ..., mst: int = ..., mp: str = ..., md: float = ..., mxv: float = ..., miv: float = ..., mth: str = ..., mtm: str = ..., mtt: str = ..., ncr: str = ..., ndc: [float, float, float] = ..., ndp: int = ..., nxc: [float, float, float] = ..., nmc: [float, float, float] = ..., op: float = ..., o: bool = ..., owp: bool = ..., pas: str = ..., pm: str = ..., pot: str = ..., pcm: bool = ..., pv: bool = ..., plc: [float, float] = ..., plp: float = ..., pcv: bool = ..., pcs: bool = ..., psf: str = ..., prm: bool = ..., r: float = ..., rxc: [float, float, float] = ..., rmc: [float, float, float] = ..., rec: bool = ..., rn: bool = ..., rno: bool = ..., ra: str = ..., rs: bool = ..., rv: str = ..., rvu: float = ..., rvv: float = ..., scR: float = ..., scs: bool = ..., sao: str = ..., sa: bool = ..., si: int = ..., stD: float = ..., stP: str = ..., stS: float = ..., stc: bool = ..., sef: bool = ..., stt: str = ..., ssm: str = ..., scv: bool = ..., to: bool = ..., tfp: str = ..., top: str = ..., ues: bool = ..., urs: bool = ..., ucr: bool = ..., umc: bool = ..., unr: bool = ..., und: bool = ..., up: bool = ..., val: float = ..., wst: str = ..., wlR: float = ..., e: bool = ...) -> None:
    """artPuttyCtx is undoable, queryable, and editable.
    
    This is a context command to set the flags on the artAttrContext, which is the
    base context for attribute painting operations. All commands require the name
    of the context as the last argument as this provides the name of the context
    to create, edit or query.
    
    This command is used to modify NURBS surfaces using a brush based interface
    (Maya Artisan). This is accomplished by moving the control vertices (CVs)
    under the brush in the specified direction.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - activeListChangedProc (alp): Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode,
            the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphaclamp (alc): Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both"
            - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - alphaclamplower (acl): Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        - alphaclampupper (acu): Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        - autosmooth (asm): Sets up the auto smoothing option. When the brush is in the smooth mode, adjusting the strength will adjust how fast the surfaces is smoothed out. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushStrength (bs): Sets the strength of the brush. Brush strength is supported by the pinch and slide brushes. In pinch mode, adjusting the strength will adjust how quickly the surface converges on the brush center. In slide mode, the strength scales the
            motion of the brush. C: Default is 1.0.  Q: When queried, it returns a float.
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - clamp (cl): Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" -
            clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - clamplower (cll): Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        - clampupper (clu): Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        - clear (clr): Floods all cvs/vertices to the current value.
        - collapsecvtol (clc): Specifies the tolerance for the collapse cv detection. C: Default is 0.005 cm.  Q: When queried, it returns a float.
        - colorAlphaValue (cl1): The Alpha value of the color.
        - colorRGBAValue (cl4): The RGBA value of the color.
        - colorRGBValue (cl3): The RGB value of the color.
        - colorRamp (cr): Allows a user defined color ramp to be used to map values to colors.
        - colorfeedback (cf): Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorfeedbackOverride (cfo): Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorrangelower (crl): Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        - colorrangeupper (cru): Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        - dataTypeIndex (dti): When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        - disablelighting (dl): If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - dispdecr (dde): Decreases a maximum displacement by 10%.
        - dispincr (din): Increases a maximum displacement by 10%.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - duringStrokeCmd (dsk): The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - erasesrfupd (eut): Toggles the update for the erase surface
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - exportaspectratio (ear): Value of aspect ratio for export
        - exportfilemode (efm): Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        - exportfilesave (esf): Exports the attribute map and saves to a specified file.
        - exportfilesizex (fsx): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfilesizey (fsy): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfiletype (eft): Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        - filterNodes (fon): Sets the node filter.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - importfileload (ifl): Load the attribute map a specified file.
        - importfilemode (ifm): Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        - importreassign (irm): Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        - interactiveUpdate (iu): Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When
            queried, it returns a boolean.
        - invertrefvector (irv): Sets the invert of the reference vector option when the reflection is ON. If it is true, the reference vector for the reflected stroke is negated with respect to the original one. C: Default is FALSE. Q: When queried, it returns a boolean.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - maxdisp (md): Defines a maximum displacement ( maxDisp in [0.0..5.0] ). C: Default is 1.0.  Q: When queried, it returns a float.
        - maxvalue (mxv): Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        - minvalue (miv): Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - mouldtypehead (mth): Type of type mould to use
        - mouldtypemouse (mtm): Specifies the putty operations/mode ("push" - pushes CVs along the given direction (see refvector flag), "pull" - pulls CVs along the specified direction, "smooth" - smooths the sculpt, "erase" - erases the paint). C: Default is "push".  Q:
            When queried, it returns a string.
        - mouldtypetail (mtt): Type of eraser mould to use
        - numericColorRamp (ncr): Allows a user defined color ramp to be used to map values to colors for the numeric display.
        - numericDisplayColor (ndc): Defines a color to be used when displaying numeric values.
        - numericDisplayPrecision (ndp): Specifies how many decimal points of precision should be used for the numeric display.
        - numericMaxColor (nxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - numericMinColor (nmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintattrselected (pas): An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - polecv (pcv): Pull all the pole CVs to the same position.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - rampMaxColor (rxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - rampMinColor (rmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - refsurface (rs): Sets on/off the update of the reference surface. If it is true the reference surface is automatically updated on the per stroke bases. If it is false, the user has to update the reference surface explicitly by pressing the update button
            (see updaterefsrf). C: Default is TRUE.  Q: When queried, it returns a boolean.
        - refvector (rv): Specifies the direction of the push/pull operation ("normal" - sculpt along normals, "firstnormal" - sculpt along the first normal of the stroke, "view" - sculpt along the view direction, "xaxis", "yaxis", "zaxis" - sculpt along a given
            axis directions, "uisoparm", "visoparm" - sculpt along U or V isoparametric lines), "uvvector" - sculpt along an arbitrary vector in UV space. C: Default is "normal".  Q: When queried, it returns a string.
        - refvectoru (rvu): Specifies the U component of the UV vector to be used when -refVector is set to "uvvector".
        - refvectorv (rvv): Specifies the V component of the UV vector to be used when -refVector is set to "uvvector".
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - selectedattroper (sao): Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the
            weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - smoothiters (si): Sets the quality of the smoothing operation (number of iterations). C: Default is 3.  Q: When queried, it returns an int.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - stitchcorner (stc): Sets on/off the stitching corner mode C: Default is "off".  Q: When queried, it returns a boolean.
        - stitchedgeflood (sef): Triggers postprocessing stitching edge procedure.
        - stitchtype (stt): Sets on/off the stitching mode ( "off" - stitching is turned off, "position" - position stitching is done without taking care about the tangent continuity C0, "tan" - C1 continuity is preserved). C: Default is "position".  Q: When queried,
            it returns a string.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - toolOffProc (tfp): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL
            command is returned and this will be an empty string if none is defined.
        - toolOnProc (top): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command
            is returned and this will be an empty string if none is defined.
        - updateerasesrf (ues): Updates the erase surface.
        - updaterefsrf (urs): Updates the reference surface.
        - useColorRamp (ucr): Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        - useMaxMinColor (umc): Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        - useNumericColorRamp (unr): Specifies whether the user defined color ramp should be used to map values from to colors on the numeric display. If this is turned off, the set single numeric color will be used.
        - useNumericDisplay (und): Specifies whether numerical weight values should be displayed next to their associated control points.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - value (val): Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - whichTool (wst): The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last
            when specifying a flag that takes arguments.
        - worldRadius (wlR): Radius in worldspace
        - edit (e): Edit mode flag
    """
@overload #Overload for artPuttyCtx in ['edit']
def artPuttyCtx(accopacity: bool = ..., aco: bool = ..., activeListChangedProc: str = ..., alp: str = ..., afterStrokeCmd: str = ..., asc: str = ..., alphaclamp: str = ..., alc: str = ..., alphaclamplower: float = ..., acl: float = ..., alphaclampupper: float = ..., acu: float = ..., autosmooth: bool = ..., asm: bool = ..., beforeStrokeCmd: str = ..., bsc: str = ..., brushStrength: float = ..., bs: float = ..., brushalignment: bool = ..., bra: bool = ..., brushfeedback: bool = ..., brf: bool = ..., clamp: str = ..., cl: str = ..., clamplower: float = ..., cll: float = ..., clampupper: float = ..., clu: float = ..., clear: bool = ..., clr: bool = ..., collapsecvtol: float = ..., clc: float = ..., colorAlphaValue: float = ..., cl1: float = ..., colorRGBAValue: [float, float, float, float] = ..., cl4: [float, float, float, float] = ..., colorRGBValue: [float, float, float] = ..., cl3: [float, float, float] = ..., colorRamp: str = ..., cr: str = ..., colorfeedback: bool = ..., cf: bool = ..., colorfeedbackOverride: bool = ..., cfo: bool = ..., colorrangelower: float = ..., crl: float = ..., colorrangeupper: float = ..., cru: float = ..., dataTypeIndex: int = ..., dti: int = ..., disablelighting: bool = ..., dl: bool = ..., dispdecr: bool = ..., dde: bool = ..., dispincr: bool = ..., din: bool = ..., dragSlider: str = ..., dsl: str = ..., duringStrokeCmd: str = ..., dsk: str = ..., dynclonemode: bool = ..., dcm: bool = ..., erasesrfupd: bool = ..., eut: bool = ..., expandfilename: bool = ..., eef: bool = ..., exportaspectratio: float = ..., ear: float = ..., exportfilemode: str = ..., efm: str = ..., exportfilesave: str = ..., esf: str = ..., exportfilesizex: int = ..., fsx: int = ..., exportfilesizey: int = ..., fsy: int = ..., exportfiletype: str = ..., eft: str = ..., filterNodes: bool = ..., fon: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., importfileload: str = ..., ifl: str = ..., importfilemode: str = ..., ifm: str = ..., importreassign: bool = ..., irm: bool = ..., interactiveUpdate: bool = ..., iu: bool = ..., invertrefvector: bool = ..., irv: bool = ..., lastRecorderCmd: str = ..., lrc: str = ..., lastStampName: str = ..., lsn: str = ..., lowerradius: float = ..., lr: float = ..., makeStroke: int = ..., mst: int = ..., mappressure: str = ..., mp: str = ..., maxdisp: float = ..., md: float = ..., maxvalue: float = ..., mxv: float = ..., minvalue: float = ..., miv: float = ..., mouldtypehead: str = ..., mth: str = ..., mouldtypemouse: str = ..., mtm: str = ..., mouldtypetail: str = ..., mtt: str = ..., numericColorRamp: str = ..., ncr: str = ..., numericDisplayColor: [float, float, float] = ..., ndc: [float, float, float] = ..., numericDisplayPrecision: int = ..., ndp: int = ..., numericMaxColor: [float, float, float] = ..., nxc: [float, float, float] = ..., numericMinColor: [float, float, float] = ..., nmc: [float, float, float] = ..., opacity: float = ..., op: float = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintattrselected: str = ..., pas: str = ..., paintmode: str = ..., pm: str = ..., paintoperationtype: str = ..., pot: str = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: [float, float] = ..., plc: [float, float] = ..., playbackPressure: float = ..., plp: float = ..., polecv: bool = ..., pcv: bool = ..., preserveclonesource: bool = ..., pcs: bool = ..., profileShapeFile: str = ..., psf: str = ..., projective: bool = ..., prm: bool = ..., radius: float = ..., r: float = ..., rampMaxColor: [float, float, float] = ..., rxc: [float, float, float] = ..., rampMinColor: [float, float, float] = ..., rmc: [float, float, float] = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: str = ..., ra: str = ..., refsurface: bool = ..., rs: bool = ..., refvector: str = ..., rv: str = ..., refvectoru: float = ..., rvu: float = ..., refvectorv: float = ..., rvv: float = ..., screenRadius: float = ..., scR: float = ..., selectclonesource: bool = ..., scs: bool = ..., selectedattroper: str = ..., sao: str = ..., showactive: bool = ..., sa: bool = ..., smoothiters: int = ..., si: int = ..., stampDepth: float = ..., stD: float = ..., stampProfile: str = ..., stP: str = ..., stampSpacing: float = ..., stS: float = ..., stitchcorner: bool = ..., stc: bool = ..., stitchedgeflood: bool = ..., sef: bool = ..., stitchtype: str = ..., stt: str = ..., strokesmooth: str = ..., ssm: str = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tangentOutline: bool = ..., to: bool = ..., toolOffProc: str = ..., tfp: str = ..., toolOnProc: str = ..., top: str = ..., updateerasesrf: bool = ..., ues: bool = ..., updaterefsrf: bool = ..., urs: bool = ..., useColorRamp: bool = ..., ucr: bool = ..., useMaxMinColor: bool = ..., umc: bool = ..., useNumericColorRamp: bool = ..., unr: bool = ..., useNumericDisplay: bool = ..., und: bool = ..., usepressure: bool = ..., up: bool = ..., value: float = ..., val: float = ..., whichTool: str = ..., wst: str = ..., worldRadius: float = ..., wlR: float = ..., edit: bool = ..., e: bool = ...) -> None:
    """artPuttyCtx is undoable, queryable, and editable.
    
    This is a context command to set the flags on the artAttrContext, which is the
    base context for attribute painting operations. All commands require the name
    of the context as the last argument as this provides the name of the context
    to create, edit or query.
    
    This command is used to modify NURBS surfaces using a brush based interface
    (Maya Artisan). This is accomplished by moving the control vertices (CVs)
    under the brush in the specified direction.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - activeListChangedProc (alp): Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode,
            the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphaclamp (alc): Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both"
            - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - alphaclamplower (acl): Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        - alphaclampupper (acu): Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        - autosmooth (asm): Sets up the auto smoothing option. When the brush is in the smooth mode, adjusting the strength will adjust how fast the surfaces is smoothed out. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushStrength (bs): Sets the strength of the brush. Brush strength is supported by the pinch and slide brushes. In pinch mode, adjusting the strength will adjust how quickly the surface converges on the brush center. In slide mode, the strength scales the
            motion of the brush. C: Default is 1.0.  Q: When queried, it returns a float.
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - clamp (cl): Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" -
            clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        - clamplower (cll): Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        - clampupper (clu): Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        - clear (clr): Floods all cvs/vertices to the current value.
        - collapsecvtol (clc): Specifies the tolerance for the collapse cv detection. C: Default is 0.005 cm.  Q: When queried, it returns a float.
        - colorAlphaValue (cl1): The Alpha value of the color.
        - colorRGBAValue (cl4): The RGBA value of the color.
        - colorRGBValue (cl3): The RGB value of the color.
        - colorRamp (cr): Allows a user defined color ramp to be used to map values to colors.
        - colorfeedback (cf): Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorfeedbackOverride (cfo): Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - colorrangelower (crl): Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        - colorrangeupper (cru): Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        - dataTypeIndex (dti): When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        - disablelighting (dl): If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        - dispdecr (dde): Decreases a maximum displacement by 10%.
        - dispincr (din): Increases a maximum displacement by 10%.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - duringStrokeCmd (dsk): The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - erasesrfupd (eut): Toggles the update for the erase surface
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - exportaspectratio (ear): Value of aspect ratio for export
        - exportfilemode (efm): Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        - exportfilesave (esf): Exports the attribute map and saves to a specified file.
        - exportfilesizex (fsx): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfilesizey (fsy): Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        - exportfiletype (eft): Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        - filterNodes (fon): Sets the node filter.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - importfileload (ifl): Load the attribute map a specified file.
        - importfilemode (ifm): Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        - importreassign (irm): Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        - interactiveUpdate (iu): Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When
            queried, it returns a boolean.
        - invertrefvector (irv): Sets the invert of the reference vector option when the reflection is ON. If it is true, the reference vector for the reflected stroke is negated with respect to the original one. C: Default is FALSE. Q: When queried, it returns a boolean.
        - lastRecorderCmd (lrc): Value of last recorded command.
        - lastStampName (lsn): Value of the last stamp name.
        - lowerradius (lr): Sets the lower size of the brush (only apply on tablet).
        - makeStroke (mst): Stroke point values.
        - mappressure (mp): Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity
            and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        - maxdisp (md): Defines a maximum displacement ( maxDisp in [0.0..5.0] ). C: Default is 1.0.  Q: When queried, it returns a float.
        - maxvalue (mxv): Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        - minvalue (miv): Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - mouldtypehead (mth): Type of type mould to use
        - mouldtypemouse (mtm): Specifies the putty operations/mode ("push" - pushes CVs along the given direction (see refvector flag), "pull" - pulls CVs along the specified direction, "smooth" - smooths the sculpt, "erase" - erases the paint). C: Default is "push".  Q:
            When queried, it returns a string.
        - mouldtypetail (mtt): Type of eraser mould to use
        - numericColorRamp (ncr): Allows a user defined color ramp to be used to map values to colors for the numeric display.
        - numericDisplayColor (ndc): Defines a color to be used when displaying numeric values.
        - numericDisplayPrecision (ndp): Specifies how many decimal points of precision should be used for the numeric display.
        - numericMaxColor (nxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - numericMinColor (nmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - opacity (op): Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        - outline (o): Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - outwhilepaint (owp): Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        - paintattrselected (pas): An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.
        - paintmode (pm): Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        - paintoperationtype (pot): Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - polecv (pcv): Pull all the pole CVs to the same position.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - rampMaxColor (rxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - rampMinColor (rmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - refsurface (rs): Sets on/off the update of the reference surface. If it is true the reference surface is automatically updated on the per stroke bases. If it is false, the user has to update the reference surface explicitly by pressing the update button
            (see updaterefsrf). C: Default is TRUE.  Q: When queried, it returns a boolean.
        - refvector (rv): Specifies the direction of the push/pull operation ("normal" - sculpt along normals, "firstnormal" - sculpt along the first normal of the stroke, "view" - sculpt along the view direction, "xaxis", "yaxis", "zaxis" - sculpt along a given
            axis directions, "uisoparm", "visoparm" - sculpt along U or V isoparametric lines), "uvvector" - sculpt along an arbitrary vector in UV space. C: Default is "normal".  Q: When queried, it returns a string.
        - refvectoru (rvu): Specifies the U component of the UV vector to be used when -refVector is set to "uvvector".
        - refvectorv (rvv): Specifies the V component of the UV vector to be used when -refVector is set to "uvvector".
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - selectedattroper (sao): Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the
            weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - smoothiters (si): Sets the quality of the smoothing operation (number of iterations). C: Default is 3.  Q: When queried, it returns an int.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - stitchcorner (stc): Sets on/off the stitching corner mode C: Default is "off".  Q: When queried, it returns a boolean.
        - stitchedgeflood (sef): Triggers postprocessing stitching edge procedure.
        - stitchtype (stt): Sets on/off the stitching mode ( "off" - stitching is turned off, "position" - position stitching is done without taking care about the tangent continuity C0, "tan" - C1 continuity is preserved). C: Default is "position".  Q: When queried,
            it returns a string.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - toolOffProc (tfp): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL
            command is returned and this will be an empty string if none is defined.
        - toolOnProc (top): Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires
            special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command
            is returned and this will be an empty string if none is defined.
        - updateerasesrf (ues): Updates the erase surface.
        - updaterefsrf (urs): Updates the reference surface.
        - useColorRamp (ucr): Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        - useMaxMinColor (umc): Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        - useNumericColorRamp (unr): Specifies whether the user defined color ramp should be used to map values from to colors on the numeric display. If this is turned off, the set single numeric color will be used.
        - useNumericDisplay (und): Specifies whether numerical weight values should be displayed next to their associated control points.
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - value (val): Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        - whichTool (wst): The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last
            when specifying a flag that takes arguments.
        - worldRadius (wlR): Radius in worldspace
        - edit (e): Edit mode flag
    """
