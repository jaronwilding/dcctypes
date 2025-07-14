"""Stub files for Contexts category in Maya commands, command: art3dPaintCtx."""

from typing import Any, overload

@overload #Overload for art3dPaintCtx in ['create']
def art3dPaintCtx(accopacity: bool = ..., afterStrokeCmd: str = ..., alphablendmode: str = ..., attrnames: str = ..., beforeStrokeCmd: str = ..., brushalignment: bool = ..., brushdepth: float = ..., brushfeedback: bool = ..., brushtype: str = ..., clear: bool = ..., dragSlider: str = ..., dynclonemode: bool = ..., exists: bool = ..., expandfilename: bool = ..., extendFillColor: bool = ..., fileformat: str = ..., filetxtaspectratio: float = ..., filetxtsizex: int = ..., filetxtsizey: int = ..., floodOpacity: float = ..., floodall: bool = ..., floodselect: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., keepaspectratio: bool = ..., lastRecorderCmd: str = ..., lastStampName: str = ..., lowerradius: float = ..., makeStroke: int = ..., mappressure: str = ..., name: str = ..., opacity: float = ..., outline: bool = ..., outwhilepaint: bool = ..., paintmode: str = ..., paintoperationtype: str = ..., painttxtattr: str = ..., painttxtattrname: str = ..., pfxScale: float = ..., pfxWidth: float = ..., pickColor: bool = ..., pickValue: bool = ..., playbackCursor: [float, float] = ..., playbackPressure: float = ..., preserveclonesource: bool = ..., pressureMapping1: int = ..., pressureMapping2: int = ..., pressureMapping3: int = ..., pressureMax1: float = ..., pressureMax2: float = ..., pressureMax3: float = ..., pressureMin1: float = ..., pressureMin2: float = ..., pressureMin3: float = ..., profileShapeFile: str = ..., projective: bool = ..., radius: float = ..., record: bool = ..., reflection: bool = ..., reflectionaboutorigin: bool = ..., reflectionaxis: str = ..., resizeratio: float = ..., rgbcolor: [float, float, float] = ..., rgbflood: [float, float, float] = ..., saveTextureOnStroke: bool = ..., saveonstroke: bool = ..., screenRadius: float = ..., selectclonesource: bool = ..., shapeattr: bool = ..., showactive: bool = ..., soloAsDiffuse: bool = ..., stampDepth: float = ..., stampProfile: str = ..., stampSpacing: float = ..., strokesmooth: str = ..., surfaceConformedBrushVertices: bool = ..., tangentOutline: bool = ..., updateEraseTex: bool = ..., usepressure: bool = ..., worldRadius: float = ...) -> None:
    """art3dPaintCtx is undoable, queryable, and editable.
    
    This is a tool context command for 3d Paint tool.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphablendmode (abm): Specifies the blend mode used while painting RGB channel. Currently, we support the following blend modes: "Default" "Lighten" "Darken" "Difference" "Exclusion" "Hard Light" "Soft Light" "Multiply" "Screen" "Overlay" "Constant" Default is
            "Default".
        - attrnames (atn): Name of attributes
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushdepth (bd): Depth of the brush
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - brushtype (brt): Name of the brush type
        - clear (clr): Floods all cvs/vertices to the current value.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - extendFillColor (efc): States if the painted textures will be automatically postprocessed on each stroke to fill in the background color. Default is true.
        - fileformat (eff): Name of the file format
        - filetxtaspectratio (far): Specifies the aspect ration of the texture width and height. Default is 1.
        - filetxtsizex (ftx): Specifies the width of the texture. Default is 256.
        - filetxtsizey (fty): Specifies the height of the texture. Default is 256.
        - floodOpacity (fop): Value of the flood opacity
        - floodall (fal): Turn on to flood everything
        - floodselect (fsl): Should the selected area be flooded?
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keepaspectratio (kar): States if the aspect ratio of the file texture sizes should remain constant. Default is true. boolean.
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
        - painttxtattr (pta): Specifies the attribute on the shader which the user wants to paint. Currently, we support the following attributes: "Color", "Transparency", "Ambient", "Incandescence", "BumpMap", "Diffuse", "Translucence" "Eccentricity" "SpecularColor",
            "Reflectivity", "ReflectedColor", and user-defined float, float3, double, and double3 attributes. Default is "Color".
        - painttxtattrname (ptn): Returns a string with the names of all paintable attributes supported by the Paint Texture Tool.
        - pfxScale (psc): Specifies the scale for Paint Effect brushes.
        - pfxWidth (pwd): Specifies the width for Paint Effect brushes.
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - pressureMapping1 (pm1): First pressure mapping value
        - pressureMapping2 (pm2): Second pressure mapping value
        - pressureMapping3 (pm3): Third pressure mapping value
        - pressureMax1 (px1): First pressure maximum value
        - pressureMax2 (px2): Second pressure maximum value
        - pressureMax3 (px3): Third pressure maximum value
        - pressureMin1 (ps1): First pressure minimum value
        - pressureMin2 (ps2): Second pressure minimum value
        - pressureMin3 (ps3): Third pressure minimum value
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - resizeratio (rr): Specifies the scale by which to resize the current textures.
        - rgbcolor (rgb): Colour value
        - rgbflood (fc): Color of the flood
        - saveTextureOnStroke (sts): States if the original texture will be automatically saved on each stroke. Default is false.
        - saveonstroke (sos): States if the temporary texture will be automatically saved on each stroke. Default is false.
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - shapeattr (spa): States if the attribute to paint is an attribute of the shape and not the shader. Default is false.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - soloAsDiffuse (sod): States if the currently paintable texture will be rendered as as diffuse texture in the viewport. Default is false.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - updateEraseTex (uet): Should the erase texture update?
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
    """
@overload #Overload for art3dPaintCtx in ['create']
def art3dPaintCtx(aco: bool = ..., asc: str = ..., abm: str = ..., atn: str = ..., bsc: str = ..., bra: bool = ..., bd: float = ..., brf: bool = ..., brt: str = ..., clr: bool = ..., dsl: str = ..., dcm: bool = ..., ex: bool = ..., eef: bool = ..., efc: bool = ..., eff: str = ..., far: float = ..., ftx: int = ..., fty: int = ..., fop: float = ..., fal: bool = ..., fsl: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., kar: bool = ..., lrc: str = ..., lsn: str = ..., lr: float = ..., mst: int = ..., mp: str = ..., n: str = ..., op: float = ..., o: bool = ..., owp: bool = ..., pm: str = ..., pot: str = ..., pta: str = ..., ptn: str = ..., psc: float = ..., pwd: float = ..., pcm: bool = ..., pv: bool = ..., plc: [float, float] = ..., plp: float = ..., pcs: bool = ..., pm1: int = ..., pm2: int = ..., pm3: int = ..., px1: float = ..., px2: float = ..., px3: float = ..., ps1: float = ..., ps2: float = ..., ps3: float = ..., psf: str = ..., prm: bool = ..., r: float = ..., rec: bool = ..., rn: bool = ..., rno: bool = ..., ra: str = ..., rr: float = ..., rgb: [float, float, float] = ..., fc: [float, float, float] = ..., sts: bool = ..., sos: bool = ..., scR: float = ..., scs: bool = ..., spa: bool = ..., sa: bool = ..., sod: bool = ..., stD: float = ..., stP: str = ..., stS: float = ..., ssm: str = ..., scv: bool = ..., to: bool = ..., uet: bool = ..., up: bool = ..., wlR: float = ...) -> None:
    """art3dPaintCtx is undoable, queryable, and editable.
    
    This is a tool context command for 3d Paint tool.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphablendmode (abm): Specifies the blend mode used while painting RGB channel. Currently, we support the following blend modes: "Default" "Lighten" "Darken" "Difference" "Exclusion" "Hard Light" "Soft Light" "Multiply" "Screen" "Overlay" "Constant" Default is
            "Default".
        - attrnames (atn): Name of attributes
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushdepth (bd): Depth of the brush
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - brushtype (brt): Name of the brush type
        - clear (clr): Floods all cvs/vertices to the current value.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - extendFillColor (efc): States if the painted textures will be automatically postprocessed on each stroke to fill in the background color. Default is true.
        - fileformat (eff): Name of the file format
        - filetxtaspectratio (far): Specifies the aspect ration of the texture width and height. Default is 1.
        - filetxtsizex (ftx): Specifies the width of the texture. Default is 256.
        - filetxtsizey (fty): Specifies the height of the texture. Default is 256.
        - floodOpacity (fop): Value of the flood opacity
        - floodall (fal): Turn on to flood everything
        - floodselect (fsl): Should the selected area be flooded?
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keepaspectratio (kar): States if the aspect ratio of the file texture sizes should remain constant. Default is true. boolean.
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
        - painttxtattr (pta): Specifies the attribute on the shader which the user wants to paint. Currently, we support the following attributes: "Color", "Transparency", "Ambient", "Incandescence", "BumpMap", "Diffuse", "Translucence" "Eccentricity" "SpecularColor",
            "Reflectivity", "ReflectedColor", and user-defined float, float3, double, and double3 attributes. Default is "Color".
        - painttxtattrname (ptn): Returns a string with the names of all paintable attributes supported by the Paint Texture Tool.
        - pfxScale (psc): Specifies the scale for Paint Effect brushes.
        - pfxWidth (pwd): Specifies the width for Paint Effect brushes.
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - pressureMapping1 (pm1): First pressure mapping value
        - pressureMapping2 (pm2): Second pressure mapping value
        - pressureMapping3 (pm3): Third pressure mapping value
        - pressureMax1 (px1): First pressure maximum value
        - pressureMax2 (px2): Second pressure maximum value
        - pressureMax3 (px3): Third pressure maximum value
        - pressureMin1 (ps1): First pressure minimum value
        - pressureMin2 (ps2): Second pressure minimum value
        - pressureMin3 (ps3): Third pressure minimum value
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - resizeratio (rr): Specifies the scale by which to resize the current textures.
        - rgbcolor (rgb): Colour value
        - rgbflood (fc): Color of the flood
        - saveTextureOnStroke (sts): States if the original texture will be automatically saved on each stroke. Default is false.
        - saveonstroke (sos): States if the temporary texture will be automatically saved on each stroke. Default is false.
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - shapeattr (spa): States if the attribute to paint is an attribute of the shape and not the shader. Default is false.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - soloAsDiffuse (sod): States if the currently paintable texture will be rendered as as diffuse texture in the viewport. Default is false.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - updateEraseTex (uet): Should the erase texture update?
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
    """
@overload #Overload for art3dPaintCtx in ['create']
def art3dPaintCtx(accopacity: bool = ..., aco: bool = ..., afterStrokeCmd: str = ..., asc: str = ..., alphablendmode: str = ..., abm: str = ..., attrnames: str = ..., atn: str = ..., beforeStrokeCmd: str = ..., bsc: str = ..., brushalignment: bool = ..., bra: bool = ..., brushdepth: float = ..., bd: float = ..., brushfeedback: bool = ..., brf: bool = ..., brushtype: str = ..., brt: str = ..., clear: bool = ..., clr: bool = ..., dragSlider: str = ..., dsl: str = ..., dynclonemode: bool = ..., dcm: bool = ..., exists: bool = ..., ex: bool = ..., expandfilename: bool = ..., eef: bool = ..., extendFillColor: bool = ..., efc: bool = ..., fileformat: str = ..., eff: str = ..., filetxtaspectratio: float = ..., far: float = ..., filetxtsizex: int = ..., ftx: int = ..., filetxtsizey: int = ..., fty: int = ..., floodOpacity: float = ..., fop: float = ..., floodall: bool = ..., fal: bool = ..., floodselect: bool = ..., fsl: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., keepaspectratio: bool = ..., kar: bool = ..., lastRecorderCmd: str = ..., lrc: str = ..., lastStampName: str = ..., lsn: str = ..., lowerradius: float = ..., lr: float = ..., makeStroke: int = ..., mst: int = ..., mappressure: str = ..., mp: str = ..., name: str = ..., n: str = ..., opacity: float = ..., op: float = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintmode: str = ..., pm: str = ..., paintoperationtype: str = ..., pot: str = ..., painttxtattr: str = ..., pta: str = ..., painttxtattrname: str = ..., ptn: str = ..., pfxScale: float = ..., psc: float = ..., pfxWidth: float = ..., pwd: float = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: [float, float] = ..., plc: [float, float] = ..., playbackPressure: float = ..., plp: float = ..., preserveclonesource: bool = ..., pcs: bool = ..., pressureMapping1: int = ..., pm1: int = ..., pressureMapping2: int = ..., pm2: int = ..., pressureMapping3: int = ..., pm3: int = ..., pressureMax1: float = ..., px1: float = ..., pressureMax2: float = ..., px2: float = ..., pressureMax3: float = ..., px3: float = ..., pressureMin1: float = ..., ps1: float = ..., pressureMin2: float = ..., ps2: float = ..., pressureMin3: float = ..., ps3: float = ..., profileShapeFile: str = ..., psf: str = ..., projective: bool = ..., prm: bool = ..., radius: float = ..., r: float = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: str = ..., ra: str = ..., resizeratio: float = ..., rr: float = ..., rgbcolor: [float, float, float] = ..., rgb: [float, float, float] = ..., rgbflood: [float, float, float] = ..., fc: [float, float, float] = ..., saveTextureOnStroke: bool = ..., sts: bool = ..., saveonstroke: bool = ..., sos: bool = ..., screenRadius: float = ..., scR: float = ..., selectclonesource: bool = ..., scs: bool = ..., shapeattr: bool = ..., spa: bool = ..., showactive: bool = ..., sa: bool = ..., soloAsDiffuse: bool = ..., sod: bool = ..., stampDepth: float = ..., stD: float = ..., stampProfile: str = ..., stP: str = ..., stampSpacing: float = ..., stS: float = ..., strokesmooth: str = ..., ssm: str = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tangentOutline: bool = ..., to: bool = ..., updateEraseTex: bool = ..., uet: bool = ..., usepressure: bool = ..., up: bool = ..., worldRadius: float = ..., wlR: float = ...) -> None:
    """art3dPaintCtx is undoable, queryable, and editable.
    
    This is a tool context command for 3d Paint tool.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphablendmode (abm): Specifies the blend mode used while painting RGB channel. Currently, we support the following blend modes: "Default" "Lighten" "Darken" "Difference" "Exclusion" "Hard Light" "Soft Light" "Multiply" "Screen" "Overlay" "Constant" Default is
            "Default".
        - attrnames (atn): Name of attributes
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushdepth (bd): Depth of the brush
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - brushtype (brt): Name of the brush type
        - clear (clr): Floods all cvs/vertices to the current value.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - extendFillColor (efc): States if the painted textures will be automatically postprocessed on each stroke to fill in the background color. Default is true.
        - fileformat (eff): Name of the file format
        - filetxtaspectratio (far): Specifies the aspect ration of the texture width and height. Default is 1.
        - filetxtsizex (ftx): Specifies the width of the texture. Default is 256.
        - filetxtsizey (fty): Specifies the height of the texture. Default is 256.
        - floodOpacity (fop): Value of the flood opacity
        - floodall (fal): Turn on to flood everything
        - floodselect (fsl): Should the selected area be flooded?
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keepaspectratio (kar): States if the aspect ratio of the file texture sizes should remain constant. Default is true. boolean.
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
        - painttxtattr (pta): Specifies the attribute on the shader which the user wants to paint. Currently, we support the following attributes: "Color", "Transparency", "Ambient", "Incandescence", "BumpMap", "Diffuse", "Translucence" "Eccentricity" "SpecularColor",
            "Reflectivity", "ReflectedColor", and user-defined float, float3, double, and double3 attributes. Default is "Color".
        - painttxtattrname (ptn): Returns a string with the names of all paintable attributes supported by the Paint Texture Tool.
        - pfxScale (psc): Specifies the scale for Paint Effect brushes.
        - pfxWidth (pwd): Specifies the width for Paint Effect brushes.
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - pressureMapping1 (pm1): First pressure mapping value
        - pressureMapping2 (pm2): Second pressure mapping value
        - pressureMapping3 (pm3): Third pressure mapping value
        - pressureMax1 (px1): First pressure maximum value
        - pressureMax2 (px2): Second pressure maximum value
        - pressureMax3 (px3): Third pressure maximum value
        - pressureMin1 (ps1): First pressure minimum value
        - pressureMin2 (ps2): Second pressure minimum value
        - pressureMin3 (ps3): Third pressure minimum value
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - resizeratio (rr): Specifies the scale by which to resize the current textures.
        - rgbcolor (rgb): Colour value
        - rgbflood (fc): Color of the flood
        - saveTextureOnStroke (sts): States if the original texture will be automatically saved on each stroke. Default is false.
        - saveonstroke (sos): States if the temporary texture will be automatically saved on each stroke. Default is false.
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - shapeattr (spa): States if the attribute to paint is an attribute of the shape and not the shader. Default is false.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - soloAsDiffuse (sod): States if the currently paintable texture will be rendered as as diffuse texture in the viewport. Default is false.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - updateEraseTex (uet): Should the erase texture update?
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
    """
@overload #Overload for art3dPaintCtx in ['query']
def art3dPaintCtx(accopacity: bool = ..., afterStrokeCmd: str = ..., alphablendmode: str = ..., attrnames: str = ..., beforeStrokeCmd: str = ..., brushalignment: bool = ..., brushdepth: float = ..., brushfeedback: bool = ..., brushtype: str = ..., clear: bool = ..., commonattr: str = ..., dragSlider: str = ..., dynclonemode: bool = ..., expandfilename: bool = ..., extendFillColor: bool = ..., fileformat: str = ..., filetxtaspectratio: float = ..., filetxtsizex: int = ..., filetxtsizey: int = ..., floodOpacity: float = ..., floodall: bool = ..., floodselect: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., keepaspectratio: bool = ..., lastRecorderCmd: str = ..., lastStampName: str = ..., lowerradius: float = ..., makeStroke: int = ..., mappressure: str = ..., opacity: float = ..., outline: bool = ..., outwhilepaint: bool = ..., paintmode: str = ..., paintoperationtype: str = ..., painttxtattr: str = ..., painttxtattrname: str = ..., pfxScale: float = ..., pfxWidth: float = ..., pickColor: bool = ..., pickValue: bool = ..., playbackCursor: [float, float] = ..., playbackPressure: float = ..., preserveclonesource: bool = ..., pressureMapping1: int = ..., pressureMapping2: int = ..., pressureMapping3: int = ..., pressureMax1: float = ..., pressureMax2: float = ..., pressureMax3: float = ..., pressureMin1: float = ..., pressureMin2: float = ..., pressureMin3: float = ..., profileShapeFile: str = ..., projective: bool = ..., radius: float = ..., record: bool = ..., reflection: bool = ..., reflectionaboutorigin: bool = ..., reflectionaxis: str = ..., resizeratio: float = ..., rgbcolor: [float, float, float] = ..., rgbflood: [float, float, float] = ..., saveTextureOnStroke: bool = ..., saveonstroke: bool = ..., screenRadius: float = ..., selectclonesource: bool = ..., shadernames: str = ..., shapeattr: bool = ..., shapenames: str = ..., showactive: bool = ..., soloAsDiffuse: bool = ..., stampDepth: float = ..., stampProfile: str = ..., stampSpacing: float = ..., strokesmooth: str = ..., surfaceConformedBrushVertices: bool = ..., tablet: bool = ..., tangentOutline: bool = ..., textureFilenames: bool = ..., updateEraseTex: bool = ..., usepressure: bool = ..., worldRadius: float = ..., query: bool = ...) -> None:
    """art3dPaintCtx is undoable, queryable, and editable.
    
    This is a tool context command for 3d Paint tool.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphablendmode (abm): Specifies the blend mode used while painting RGB channel. Currently, we support the following blend modes: "Default" "Lighten" "Darken" "Difference" "Exclusion" "Hard Light" "Soft Light" "Multiply" "Screen" "Overlay" "Constant" Default is
            "Default".
        - attrnames (atn): Name of attributes
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushdepth (bd): Depth of the brush
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - brushtype (brt): Name of the brush type
        - clear (clr): Floods all cvs/vertices to the current value.
        - commonattr (cat): Returns a string with the names of all common to all the shaders paintable attributes and supported by the Paint Texture Tool.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - extendFillColor (efc): States if the painted textures will be automatically postprocessed on each stroke to fill in the background color. Default is true.
        - fileformat (eff): Name of the file format
        - filetxtaspectratio (far): Specifies the aspect ration of the texture width and height. Default is 1.
        - filetxtsizex (ftx): Specifies the width of the texture. Default is 256.
        - filetxtsizey (fty): Specifies the height of the texture. Default is 256.
        - floodOpacity (fop): Value of the flood opacity
        - floodall (fal): Turn on to flood everything
        - floodselect (fsl): Should the selected area be flooded?
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keepaspectratio (kar): States if the aspect ratio of the file texture sizes should remain constant. Default is true. boolean.
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
        - painttxtattr (pta): Specifies the attribute on the shader which the user wants to paint. Currently, we support the following attributes: "Color", "Transparency", "Ambient", "Incandescence", "BumpMap", "Diffuse", "Translucence" "Eccentricity" "SpecularColor",
            "Reflectivity", "ReflectedColor", and user-defined float, float3, double, and double3 attributes. Default is "Color".
        - painttxtattrname (ptn): Returns a string with the names of all paintable attributes supported by the Paint Texture Tool.
        - pfxScale (psc): Specifies the scale for Paint Effect brushes.
        - pfxWidth (pwd): Specifies the width for Paint Effect brushes.
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - pressureMapping1 (pm1): First pressure mapping value
        - pressureMapping2 (pm2): Second pressure mapping value
        - pressureMapping3 (pm3): Third pressure mapping value
        - pressureMax1 (px1): First pressure maximum value
        - pressureMax2 (px2): Second pressure maximum value
        - pressureMax3 (px3): Third pressure maximum value
        - pressureMin1 (ps1): First pressure minimum value
        - pressureMin2 (ps2): Second pressure minimum value
        - pressureMin3 (ps3): Third pressure minimum value
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - resizeratio (rr): Specifies the scale by which to resize the current textures.
        - rgbcolor (rgb): Colour value
        - rgbflood (fc): Color of the flood
        - saveTextureOnStroke (sts): States if the original texture will be automatically saved on each stroke. Default is false.
        - saveonstroke (sos): States if the temporary texture will be automatically saved on each stroke. Default is false.
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - shadernames (hnm): Returns a string with the names of all shaders assigned to selected surfaces.
        - shapeattr (spa): States if the attribute to paint is an attribute of the shape and not the shader. Default is false.
        - shapenames (shn): Returns a string with the names of all surfaces which are being painted on.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - soloAsDiffuse (sod): States if the currently paintable texture will be rendered as as diffuse texture in the viewport. Default is false.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tablet (tab): Returns true if the tablet device is present, false if it is absent
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - textureFilenames (tfn): Returns a string array with the names of all the painted file textures.
        - updateEraseTex (uet): Should the erase texture update?
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
        - query (q): Query mode flag
    """
@overload #Overload for art3dPaintCtx in ['query']
def art3dPaintCtx(aco: bool = ..., asc: str = ..., abm: str = ..., atn: str = ..., bsc: str = ..., bra: bool = ..., bd: float = ..., brf: bool = ..., brt: str = ..., clr: bool = ..., cat: str = ..., dsl: str = ..., dcm: bool = ..., eef: bool = ..., efc: bool = ..., eff: str = ..., far: float = ..., ftx: int = ..., fty: int = ..., fop: float = ..., fal: bool = ..., fsl: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., kar: bool = ..., lrc: str = ..., lsn: str = ..., lr: float = ..., mst: int = ..., mp: str = ..., op: float = ..., o: bool = ..., owp: bool = ..., pm: str = ..., pot: str = ..., pta: str = ..., ptn: str = ..., psc: float = ..., pwd: float = ..., pcm: bool = ..., pv: bool = ..., plc: [float, float] = ..., plp: float = ..., pcs: bool = ..., pm1: int = ..., pm2: int = ..., pm3: int = ..., px1: float = ..., px2: float = ..., px3: float = ..., ps1: float = ..., ps2: float = ..., ps3: float = ..., psf: str = ..., prm: bool = ..., r: float = ..., rec: bool = ..., rn: bool = ..., rno: bool = ..., ra: str = ..., rr: float = ..., rgb: [float, float, float] = ..., fc: [float, float, float] = ..., sts: bool = ..., sos: bool = ..., scR: float = ..., scs: bool = ..., hnm: str = ..., spa: bool = ..., shn: str = ..., sa: bool = ..., sod: bool = ..., stD: float = ..., stP: str = ..., stS: float = ..., ssm: str = ..., scv: bool = ..., tab: bool = ..., to: bool = ..., tfn: bool = ..., uet: bool = ..., up: bool = ..., wlR: float = ..., q: bool = ...) -> None:
    """art3dPaintCtx is undoable, queryable, and editable.
    
    This is a tool context command for 3d Paint tool.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphablendmode (abm): Specifies the blend mode used while painting RGB channel. Currently, we support the following blend modes: "Default" "Lighten" "Darken" "Difference" "Exclusion" "Hard Light" "Soft Light" "Multiply" "Screen" "Overlay" "Constant" Default is
            "Default".
        - attrnames (atn): Name of attributes
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushdepth (bd): Depth of the brush
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - brushtype (brt): Name of the brush type
        - clear (clr): Floods all cvs/vertices to the current value.
        - commonattr (cat): Returns a string with the names of all common to all the shaders paintable attributes and supported by the Paint Texture Tool.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - extendFillColor (efc): States if the painted textures will be automatically postprocessed on each stroke to fill in the background color. Default is true.
        - fileformat (eff): Name of the file format
        - filetxtaspectratio (far): Specifies the aspect ration of the texture width and height. Default is 1.
        - filetxtsizex (ftx): Specifies the width of the texture. Default is 256.
        - filetxtsizey (fty): Specifies the height of the texture. Default is 256.
        - floodOpacity (fop): Value of the flood opacity
        - floodall (fal): Turn on to flood everything
        - floodselect (fsl): Should the selected area be flooded?
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keepaspectratio (kar): States if the aspect ratio of the file texture sizes should remain constant. Default is true. boolean.
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
        - painttxtattr (pta): Specifies the attribute on the shader which the user wants to paint. Currently, we support the following attributes: "Color", "Transparency", "Ambient", "Incandescence", "BumpMap", "Diffuse", "Translucence" "Eccentricity" "SpecularColor",
            "Reflectivity", "ReflectedColor", and user-defined float, float3, double, and double3 attributes. Default is "Color".
        - painttxtattrname (ptn): Returns a string with the names of all paintable attributes supported by the Paint Texture Tool.
        - pfxScale (psc): Specifies the scale for Paint Effect brushes.
        - pfxWidth (pwd): Specifies the width for Paint Effect brushes.
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - pressureMapping1 (pm1): First pressure mapping value
        - pressureMapping2 (pm2): Second pressure mapping value
        - pressureMapping3 (pm3): Third pressure mapping value
        - pressureMax1 (px1): First pressure maximum value
        - pressureMax2 (px2): Second pressure maximum value
        - pressureMax3 (px3): Third pressure maximum value
        - pressureMin1 (ps1): First pressure minimum value
        - pressureMin2 (ps2): Second pressure minimum value
        - pressureMin3 (ps3): Third pressure minimum value
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - resizeratio (rr): Specifies the scale by which to resize the current textures.
        - rgbcolor (rgb): Colour value
        - rgbflood (fc): Color of the flood
        - saveTextureOnStroke (sts): States if the original texture will be automatically saved on each stroke. Default is false.
        - saveonstroke (sos): States if the temporary texture will be automatically saved on each stroke. Default is false.
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - shadernames (hnm): Returns a string with the names of all shaders assigned to selected surfaces.
        - shapeattr (spa): States if the attribute to paint is an attribute of the shape and not the shader. Default is false.
        - shapenames (shn): Returns a string with the names of all surfaces which are being painted on.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - soloAsDiffuse (sod): States if the currently paintable texture will be rendered as as diffuse texture in the viewport. Default is false.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tablet (tab): Returns true if the tablet device is present, false if it is absent
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - textureFilenames (tfn): Returns a string array with the names of all the painted file textures.
        - updateEraseTex (uet): Should the erase texture update?
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
        - query (q): Query mode flag
    """
@overload #Overload for art3dPaintCtx in ['query']
def art3dPaintCtx(accopacity: bool = ..., aco: bool = ..., afterStrokeCmd: str = ..., asc: str = ..., alphablendmode: str = ..., abm: str = ..., attrnames: str = ..., atn: str = ..., beforeStrokeCmd: str = ..., bsc: str = ..., brushalignment: bool = ..., bra: bool = ..., brushdepth: float = ..., bd: float = ..., brushfeedback: bool = ..., brf: bool = ..., brushtype: str = ..., brt: str = ..., clear: bool = ..., clr: bool = ..., commonattr: str = ..., cat: str = ..., dragSlider: str = ..., dsl: str = ..., dynclonemode: bool = ..., dcm: bool = ..., expandfilename: bool = ..., eef: bool = ..., extendFillColor: bool = ..., efc: bool = ..., fileformat: str = ..., eff: str = ..., filetxtaspectratio: float = ..., far: float = ..., filetxtsizex: int = ..., ftx: int = ..., filetxtsizey: int = ..., fty: int = ..., floodOpacity: float = ..., fop: float = ..., floodall: bool = ..., fal: bool = ..., floodselect: bool = ..., fsl: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., keepaspectratio: bool = ..., kar: bool = ..., lastRecorderCmd: str = ..., lrc: str = ..., lastStampName: str = ..., lsn: str = ..., lowerradius: float = ..., lr: float = ..., makeStroke: int = ..., mst: int = ..., mappressure: str = ..., mp: str = ..., opacity: float = ..., op: float = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintmode: str = ..., pm: str = ..., paintoperationtype: str = ..., pot: str = ..., painttxtattr: str = ..., pta: str = ..., painttxtattrname: str = ..., ptn: str = ..., pfxScale: float = ..., psc: float = ..., pfxWidth: float = ..., pwd: float = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: [float, float] = ..., plc: [float, float] = ..., playbackPressure: float = ..., plp: float = ..., preserveclonesource: bool = ..., pcs: bool = ..., pressureMapping1: int = ..., pm1: int = ..., pressureMapping2: int = ..., pm2: int = ..., pressureMapping3: int = ..., pm3: int = ..., pressureMax1: float = ..., px1: float = ..., pressureMax2: float = ..., px2: float = ..., pressureMax3: float = ..., px3: float = ..., pressureMin1: float = ..., ps1: float = ..., pressureMin2: float = ..., ps2: float = ..., pressureMin3: float = ..., ps3: float = ..., profileShapeFile: str = ..., psf: str = ..., projective: bool = ..., prm: bool = ..., radius: float = ..., r: float = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: str = ..., ra: str = ..., resizeratio: float = ..., rr: float = ..., rgbcolor: [float, float, float] = ..., rgb: [float, float, float] = ..., rgbflood: [float, float, float] = ..., fc: [float, float, float] = ..., saveTextureOnStroke: bool = ..., sts: bool = ..., saveonstroke: bool = ..., sos: bool = ..., screenRadius: float = ..., scR: float = ..., selectclonesource: bool = ..., scs: bool = ..., shadernames: str = ..., hnm: str = ..., shapeattr: bool = ..., spa: bool = ..., shapenames: str = ..., shn: str = ..., showactive: bool = ..., sa: bool = ..., soloAsDiffuse: bool = ..., sod: bool = ..., stampDepth: float = ..., stD: float = ..., stampProfile: str = ..., stP: str = ..., stampSpacing: float = ..., stS: float = ..., strokesmooth: str = ..., ssm: str = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tablet: bool = ..., tab: bool = ..., tangentOutline: bool = ..., to: bool = ..., textureFilenames: bool = ..., tfn: bool = ..., updateEraseTex: bool = ..., uet: bool = ..., usepressure: bool = ..., up: bool = ..., worldRadius: float = ..., wlR: float = ..., query: bool = ..., q: bool = ...) -> None:
    """art3dPaintCtx is undoable, queryable, and editable.
    
    This is a tool context command for 3d Paint tool.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphablendmode (abm): Specifies the blend mode used while painting RGB channel. Currently, we support the following blend modes: "Default" "Lighten" "Darken" "Difference" "Exclusion" "Hard Light" "Soft Light" "Multiply" "Screen" "Overlay" "Constant" Default is
            "Default".
        - attrnames (atn): Name of attributes
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushdepth (bd): Depth of the brush
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - brushtype (brt): Name of the brush type
        - clear (clr): Floods all cvs/vertices to the current value.
        - commonattr (cat): Returns a string with the names of all common to all the shaders paintable attributes and supported by the Paint Texture Tool.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - extendFillColor (efc): States if the painted textures will be automatically postprocessed on each stroke to fill in the background color. Default is true.
        - fileformat (eff): Name of the file format
        - filetxtaspectratio (far): Specifies the aspect ration of the texture width and height. Default is 1.
        - filetxtsizex (ftx): Specifies the width of the texture. Default is 256.
        - filetxtsizey (fty): Specifies the height of the texture. Default is 256.
        - floodOpacity (fop): Value of the flood opacity
        - floodall (fal): Turn on to flood everything
        - floodselect (fsl): Should the selected area be flooded?
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keepaspectratio (kar): States if the aspect ratio of the file texture sizes should remain constant. Default is true. boolean.
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
        - painttxtattr (pta): Specifies the attribute on the shader which the user wants to paint. Currently, we support the following attributes: "Color", "Transparency", "Ambient", "Incandescence", "BumpMap", "Diffuse", "Translucence" "Eccentricity" "SpecularColor",
            "Reflectivity", "ReflectedColor", and user-defined float, float3, double, and double3 attributes. Default is "Color".
        - painttxtattrname (ptn): Returns a string with the names of all paintable attributes supported by the Paint Texture Tool.
        - pfxScale (psc): Specifies the scale for Paint Effect brushes.
        - pfxWidth (pwd): Specifies the width for Paint Effect brushes.
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - pressureMapping1 (pm1): First pressure mapping value
        - pressureMapping2 (pm2): Second pressure mapping value
        - pressureMapping3 (pm3): Third pressure mapping value
        - pressureMax1 (px1): First pressure maximum value
        - pressureMax2 (px2): Second pressure maximum value
        - pressureMax3 (px3): Third pressure maximum value
        - pressureMin1 (ps1): First pressure minimum value
        - pressureMin2 (ps2): Second pressure minimum value
        - pressureMin3 (ps3): Third pressure minimum value
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - resizeratio (rr): Specifies the scale by which to resize the current textures.
        - rgbcolor (rgb): Colour value
        - rgbflood (fc): Color of the flood
        - saveTextureOnStroke (sts): States if the original texture will be automatically saved on each stroke. Default is false.
        - saveonstroke (sos): States if the temporary texture will be automatically saved on each stroke. Default is false.
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - shadernames (hnm): Returns a string with the names of all shaders assigned to selected surfaces.
        - shapeattr (spa): States if the attribute to paint is an attribute of the shape and not the shader. Default is false.
        - shapenames (shn): Returns a string with the names of all surfaces which are being painted on.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - soloAsDiffuse (sod): States if the currently paintable texture will be rendered as as diffuse texture in the viewport. Default is false.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tablet (tab): Returns true if the tablet device is present, false if it is absent
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - textureFilenames (tfn): Returns a string array with the names of all the painted file textures.
        - updateEraseTex (uet): Should the erase texture update?
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
        - query (q): Query mode flag
    """
@overload #Overload for art3dPaintCtx in ['edit']
def art3dPaintCtx(accopacity: bool = ..., afterStrokeCmd: str = ..., alphablendmode: str = ..., assigntxt: bool = ..., attrnames: str = ..., beforeStrokeCmd: str = ..., brushalignment: bool = ..., brushdepth: float = ..., brushfeedback: bool = ..., brushtype: str = ..., clear: bool = ..., dragSlider: str = ..., dynclonemode: bool = ..., expandfilename: bool = ..., extendFillColor: bool = ..., fileformat: str = ..., filetxtaspectratio: float = ..., filetxtsizex: int = ..., filetxtsizey: int = ..., floodOpacity: float = ..., floodall: bool = ..., floodselect: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., keepaspectratio: bool = ..., lastRecorderCmd: str = ..., lastStampName: str = ..., lowerradius: float = ..., makeStroke: int = ..., mappressure: str = ..., opacity: float = ..., outline: bool = ..., outwhilepaint: bool = ..., paintmode: str = ..., paintoperationtype: str = ..., painttxtattr: str = ..., painttxtattrname: str = ..., pfxScale: float = ..., pfxWidth: float = ..., pickColor: bool = ..., pickValue: bool = ..., playbackCursor: [float, float] = ..., playbackPressure: float = ..., preserveclonesource: bool = ..., pressureMapping1: int = ..., pressureMapping2: int = ..., pressureMapping3: int = ..., pressureMax1: float = ..., pressureMax2: float = ..., pressureMax3: float = ..., pressureMin1: float = ..., pressureMin2: float = ..., pressureMin3: float = ..., profileShapeFile: str = ..., projective: bool = ..., radius: float = ..., record: bool = ..., reflection: bool = ..., reflectionaboutorigin: bool = ..., reflectionaxis: str = ..., reloadtexfile: bool = ..., resizeratio: float = ..., resizetxt: bool = ..., rgbcolor: [float, float, float] = ..., rgbflood: [float, float, float] = ..., saveTextureOnStroke: bool = ..., saveonstroke: bool = ..., savetexture: bool = ..., screenRadius: float = ..., selectclonesource: bool = ..., shapeattr: bool = ..., showactive: bool = ..., soloAsDiffuse: bool = ..., stampDepth: float = ..., stampProfile: str = ..., stampSpacing: float = ..., strokesmooth: str = ..., surfaceConformedBrushVertices: bool = ..., tangentOutline: bool = ..., updateEraseTex: bool = ..., usepressure: bool = ..., worldRadius: float = ..., edit: bool = ...) -> None:
    """art3dPaintCtx is undoable, queryable, and editable.
    
    This is a tool context command for 3d Paint tool.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphablendmode (abm): Specifies the blend mode used while painting RGB channel. Currently, we support the following blend modes: "Default" "Lighten" "Darken" "Difference" "Exclusion" "Hard Light" "Soft Light" "Multiply" "Screen" "Overlay" "Constant" Default is
            "Default".
        - assigntxt (ast): Sends a request to the tool to allocate and assign file textures to the specified attibute on the selected shaders.
        - attrnames (atn): Name of attributes
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushdepth (bd): Depth of the brush
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - brushtype (brt): Name of the brush type
        - clear (clr): Floods all cvs/vertices to the current value.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - extendFillColor (efc): States if the painted textures will be automatically postprocessed on each stroke to fill in the background color. Default is true.
        - fileformat (eff): Name of the file format
        - filetxtaspectratio (far): Specifies the aspect ration of the texture width and height. Default is 1.
        - filetxtsizex (ftx): Specifies the width of the texture. Default is 256.
        - filetxtsizey (fty): Specifies the height of the texture. Default is 256.
        - floodOpacity (fop): Value of the flood opacity
        - floodall (fal): Turn on to flood everything
        - floodselect (fsl): Should the selected area be flooded?
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keepaspectratio (kar): States if the aspect ratio of the file texture sizes should remain constant. Default is true. boolean.
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
        - painttxtattr (pta): Specifies the attribute on the shader which the user wants to paint. Currently, we support the following attributes: "Color", "Transparency", "Ambient", "Incandescence", "BumpMap", "Diffuse", "Translucence" "Eccentricity" "SpecularColor",
            "Reflectivity", "ReflectedColor", and user-defined float, float3, double, and double3 attributes. Default is "Color".
        - painttxtattrname (ptn): Returns a string with the names of all paintable attributes supported by the Paint Texture Tool.
        - pfxScale (psc): Specifies the scale for Paint Effect brushes.
        - pfxWidth (pwd): Specifies the width for Paint Effect brushes.
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - pressureMapping1 (pm1): First pressure mapping value
        - pressureMapping2 (pm2): Second pressure mapping value
        - pressureMapping3 (pm3): Third pressure mapping value
        - pressureMax1 (px1): First pressure maximum value
        - pressureMax2 (px2): Second pressure maximum value
        - pressureMax3 (px3): Third pressure maximum value
        - pressureMin1 (ps1): First pressure minimum value
        - pressureMin2 (ps2): Second pressure minimum value
        - pressureMin3 (ps3): Third pressure minimum value
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - reloadtexfile (rtf): Sends a request to the tool to reload the texture from the disc.
        - resizeratio (rr): Specifies the scale by which to resize the current textures.
        - resizetxt (rft): Sends a request to the tool to resize all the currently in use textures.
        - rgbcolor (rgb): Colour value
        - rgbflood (fc): Color of the flood
        - saveTextureOnStroke (sts): States if the original texture will be automatically saved on each stroke. Default is false.
        - saveonstroke (sos): States if the temporary texture will be automatically saved on each stroke. Default is false.
        - savetexture (stx): Sends a request to the tool to save the texture to the disc.
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - shapeattr (spa): States if the attribute to paint is an attribute of the shape and not the shader. Default is false.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - soloAsDiffuse (sod): States if the currently paintable texture will be rendered as as diffuse texture in the viewport. Default is false.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - updateEraseTex (uet): Should the erase texture update?
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
        - edit (e): Edit mode flag
    """
@overload #Overload for art3dPaintCtx in ['edit']
def art3dPaintCtx(aco: bool = ..., asc: str = ..., abm: str = ..., ast: bool = ..., atn: str = ..., bsc: str = ..., bra: bool = ..., bd: float = ..., brf: bool = ..., brt: str = ..., clr: bool = ..., dsl: str = ..., dcm: bool = ..., eef: bool = ..., efc: bool = ..., eff: str = ..., far: float = ..., ftx: int = ..., fty: int = ..., fop: float = ..., fal: bool = ..., fsl: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., kar: bool = ..., lrc: str = ..., lsn: str = ..., lr: float = ..., mst: int = ..., mp: str = ..., op: float = ..., o: bool = ..., owp: bool = ..., pm: str = ..., pot: str = ..., pta: str = ..., ptn: str = ..., psc: float = ..., pwd: float = ..., pcm: bool = ..., pv: bool = ..., plc: [float, float] = ..., plp: float = ..., pcs: bool = ..., pm1: int = ..., pm2: int = ..., pm3: int = ..., px1: float = ..., px2: float = ..., px3: float = ..., ps1: float = ..., ps2: float = ..., ps3: float = ..., psf: str = ..., prm: bool = ..., r: float = ..., rec: bool = ..., rn: bool = ..., rno: bool = ..., ra: str = ..., rtf: bool = ..., rr: float = ..., rft: bool = ..., rgb: [float, float, float] = ..., fc: [float, float, float] = ..., sts: bool = ..., sos: bool = ..., stx: bool = ..., scR: float = ..., scs: bool = ..., spa: bool = ..., sa: bool = ..., sod: bool = ..., stD: float = ..., stP: str = ..., stS: float = ..., ssm: str = ..., scv: bool = ..., to: bool = ..., uet: bool = ..., up: bool = ..., wlR: float = ..., e: bool = ...) -> None:
    """art3dPaintCtx is undoable, queryable, and editable.
    
    This is a tool context command for 3d Paint tool.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphablendmode (abm): Specifies the blend mode used while painting RGB channel. Currently, we support the following blend modes: "Default" "Lighten" "Darken" "Difference" "Exclusion" "Hard Light" "Soft Light" "Multiply" "Screen" "Overlay" "Constant" Default is
            "Default".
        - assigntxt (ast): Sends a request to the tool to allocate and assign file textures to the specified attibute on the selected shaders.
        - attrnames (atn): Name of attributes
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushdepth (bd): Depth of the brush
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - brushtype (brt): Name of the brush type
        - clear (clr): Floods all cvs/vertices to the current value.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - extendFillColor (efc): States if the painted textures will be automatically postprocessed on each stroke to fill in the background color. Default is true.
        - fileformat (eff): Name of the file format
        - filetxtaspectratio (far): Specifies the aspect ration of the texture width and height. Default is 1.
        - filetxtsizex (ftx): Specifies the width of the texture. Default is 256.
        - filetxtsizey (fty): Specifies the height of the texture. Default is 256.
        - floodOpacity (fop): Value of the flood opacity
        - floodall (fal): Turn on to flood everything
        - floodselect (fsl): Should the selected area be flooded?
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keepaspectratio (kar): States if the aspect ratio of the file texture sizes should remain constant. Default is true. boolean.
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
        - painttxtattr (pta): Specifies the attribute on the shader which the user wants to paint. Currently, we support the following attributes: "Color", "Transparency", "Ambient", "Incandescence", "BumpMap", "Diffuse", "Translucence" "Eccentricity" "SpecularColor",
            "Reflectivity", "ReflectedColor", and user-defined float, float3, double, and double3 attributes. Default is "Color".
        - painttxtattrname (ptn): Returns a string with the names of all paintable attributes supported by the Paint Texture Tool.
        - pfxScale (psc): Specifies the scale for Paint Effect brushes.
        - pfxWidth (pwd): Specifies the width for Paint Effect brushes.
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - pressureMapping1 (pm1): First pressure mapping value
        - pressureMapping2 (pm2): Second pressure mapping value
        - pressureMapping3 (pm3): Third pressure mapping value
        - pressureMax1 (px1): First pressure maximum value
        - pressureMax2 (px2): Second pressure maximum value
        - pressureMax3 (px3): Third pressure maximum value
        - pressureMin1 (ps1): First pressure minimum value
        - pressureMin2 (ps2): Second pressure minimum value
        - pressureMin3 (ps3): Third pressure minimum value
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - reloadtexfile (rtf): Sends a request to the tool to reload the texture from the disc.
        - resizeratio (rr): Specifies the scale by which to resize the current textures.
        - resizetxt (rft): Sends a request to the tool to resize all the currently in use textures.
        - rgbcolor (rgb): Colour value
        - rgbflood (fc): Color of the flood
        - saveTextureOnStroke (sts): States if the original texture will be automatically saved on each stroke. Default is false.
        - saveonstroke (sos): States if the temporary texture will be automatically saved on each stroke. Default is false.
        - savetexture (stx): Sends a request to the tool to save the texture to the disc.
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - shapeattr (spa): States if the attribute to paint is an attribute of the shape and not the shader. Default is false.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - soloAsDiffuse (sod): States if the currently paintable texture will be rendered as as diffuse texture in the viewport. Default is false.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - updateEraseTex (uet): Should the erase texture update?
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
        - edit (e): Edit mode flag
    """
@overload #Overload for art3dPaintCtx in ['edit']
def art3dPaintCtx(accopacity: bool = ..., aco: bool = ..., afterStrokeCmd: str = ..., asc: str = ..., alphablendmode: str = ..., abm: str = ..., assigntxt: bool = ..., ast: bool = ..., attrnames: str = ..., atn: str = ..., beforeStrokeCmd: str = ..., bsc: str = ..., brushalignment: bool = ..., bra: bool = ..., brushdepth: float = ..., bd: float = ..., brushfeedback: bool = ..., brf: bool = ..., brushtype: str = ..., brt: str = ..., clear: bool = ..., clr: bool = ..., dragSlider: str = ..., dsl: str = ..., dynclonemode: bool = ..., dcm: bool = ..., expandfilename: bool = ..., eef: bool = ..., extendFillColor: bool = ..., efc: bool = ..., fileformat: str = ..., eff: str = ..., filetxtaspectratio: float = ..., far: float = ..., filetxtsizex: int = ..., ftx: int = ..., filetxtsizey: int = ..., fty: int = ..., floodOpacity: float = ..., fop: float = ..., floodall: bool = ..., fal: bool = ..., floodselect: bool = ..., fsl: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., keepaspectratio: bool = ..., kar: bool = ..., lastRecorderCmd: str = ..., lrc: str = ..., lastStampName: str = ..., lsn: str = ..., lowerradius: float = ..., lr: float = ..., makeStroke: int = ..., mst: int = ..., mappressure: str = ..., mp: str = ..., opacity: float = ..., op: float = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintmode: str = ..., pm: str = ..., paintoperationtype: str = ..., pot: str = ..., painttxtattr: str = ..., pta: str = ..., painttxtattrname: str = ..., ptn: str = ..., pfxScale: float = ..., psc: float = ..., pfxWidth: float = ..., pwd: float = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: [float, float] = ..., plc: [float, float] = ..., playbackPressure: float = ..., plp: float = ..., preserveclonesource: bool = ..., pcs: bool = ..., pressureMapping1: int = ..., pm1: int = ..., pressureMapping2: int = ..., pm2: int = ..., pressureMapping3: int = ..., pm3: int = ..., pressureMax1: float = ..., px1: float = ..., pressureMax2: float = ..., px2: float = ..., pressureMax3: float = ..., px3: float = ..., pressureMin1: float = ..., ps1: float = ..., pressureMin2: float = ..., ps2: float = ..., pressureMin3: float = ..., ps3: float = ..., profileShapeFile: str = ..., psf: str = ..., projective: bool = ..., prm: bool = ..., radius: float = ..., r: float = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: str = ..., ra: str = ..., reloadtexfile: bool = ..., rtf: bool = ..., resizeratio: float = ..., rr: float = ..., resizetxt: bool = ..., rft: bool = ..., rgbcolor: [float, float, float] = ..., rgb: [float, float, float] = ..., rgbflood: [float, float, float] = ..., fc: [float, float, float] = ..., saveTextureOnStroke: bool = ..., sts: bool = ..., saveonstroke: bool = ..., sos: bool = ..., savetexture: bool = ..., stx: bool = ..., screenRadius: float = ..., scR: float = ..., selectclonesource: bool = ..., scs: bool = ..., shapeattr: bool = ..., spa: bool = ..., showactive: bool = ..., sa: bool = ..., soloAsDiffuse: bool = ..., sod: bool = ..., stampDepth: float = ..., stD: float = ..., stampProfile: str = ..., stP: str = ..., stampSpacing: float = ..., stS: float = ..., strokesmooth: str = ..., ssm: str = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tangentOutline: bool = ..., to: bool = ..., updateEraseTex: bool = ..., uet: bool = ..., usepressure: bool = ..., up: bool = ..., worldRadius: float = ..., wlR: float = ..., edit: bool = ..., e: bool = ...) -> None:
    """art3dPaintCtx is undoable, queryable, and editable.
    
    This is a tool context command for 3d Paint tool.

    ---
    - Args:
        - accopacity (aco): Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        - afterStrokeCmd (asc): The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - alphablendmode (abm): Specifies the blend mode used while painting RGB channel. Currently, we support the following blend modes: "Default" "Lighten" "Darken" "Difference" "Exclusion" "Hard Light" "Soft Light" "Multiply" "Screen" "Overlay" "Constant" Default is
            "Default".
        - assigntxt (ast): Sends a request to the tool to allocate and assign file textures to the specified attibute on the selected shaders.
        - attrnames (atn): Name of attributes
        - beforeStrokeCmd (bsc): The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        - brushalignment (bra): Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        - brushdepth (bd): Depth of the brush
        - brushfeedback (brf): Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        - brushtype (brt): Name of the brush type
        - clear (clr): Floods all cvs/vertices to the current value.
        - dragSlider (dsl): Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
            Default is "none".
        - dynclonemode (dcm): Enable or disable dynamic clone mode.
        - expandfilename (eef): If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        - extendFillColor (efc): States if the painted textures will be automatically postprocessed on each stroke to fill in the background color. Default is true.
        - fileformat (eff): Name of the file format
        - filetxtaspectratio (far): Specifies the aspect ration of the texture width and height. Default is 1.
        - filetxtsizex (ftx): Specifies the width of the texture. Default is 256.
        - filetxtsizey (fty): Specifies the height of the texture. Default is 256.
        - floodOpacity (fop): Value of the flood opacity
        - floodall (fal): Turn on to flood everything
        - floodselect (fsl): Should the selected area be flooded?
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keepaspectratio (kar): States if the aspect ratio of the file texture sizes should remain constant. Default is true. boolean.
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
        - painttxtattr (pta): Specifies the attribute on the shader which the user wants to paint. Currently, we support the following attributes: "Color", "Transparency", "Ambient", "Incandescence", "BumpMap", "Diffuse", "Translucence" "Eccentricity" "SpecularColor",
            "Reflectivity", "ReflectedColor", and user-defined float, float3, double, and double3 attributes. Default is "Color".
        - painttxtattrname (ptn): Returns a string with the names of all paintable attributes supported by the Paint Texture Tool.
        - pfxScale (psc): Specifies the scale for Paint Effect brushes.
        - pfxWidth (pwd): Specifies the width for Paint Effect brushes.
        - pickColor (pcm): Set pick color mode on or off
        - pickValue (pv): Toggle for picking
        - playbackCursor (plc): Values for the playback cursor.
        - playbackPressure (plp): Valus for the playback pressure.
        - preserveclonesource (pcs): Whether or not to preserve a clone source.
        - pressureMapping1 (pm1): First pressure mapping value
        - pressureMapping2 (pm2): Second pressure mapping value
        - pressureMapping3 (pm3): Third pressure mapping value
        - pressureMax1 (px1): First pressure maximum value
        - pressureMax2 (px2): Second pressure maximum value
        - pressureMax3 (px3): Third pressure maximum value
        - pressureMin1 (ps1): First pressure minimum value
        - pressureMin2 (ps2): Second pressure minimum value
        - pressureMin3 (ps3): Third pressure minimum value
        - profileShapeFile (psf): Passes a name of the image file for the stamp shape profile.
        - projective (prm): Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - radius (r): Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        - record (rec): Toggle on for recording.
        - reflection (rn): Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        - reflectionaboutorigin (rno): Toggle on to reflect about the origin
        - reflectionaxis (ra): Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        - reloadtexfile (rtf): Sends a request to the tool to reload the texture from the disc.
        - resizeratio (rr): Specifies the scale by which to resize the current textures.
        - resizetxt (rft): Sends a request to the tool to resize all the currently in use textures.
        - rgbcolor (rgb): Colour value
        - rgbflood (fc): Color of the flood
        - saveTextureOnStroke (sts): States if the original texture will be automatically saved on each stroke. Default is false.
        - saveonstroke (sos): States if the temporary texture will be automatically saved on each stroke. Default is false.
        - savetexture (stx): Sends a request to the tool to save the texture to the disc.
        - screenRadius (scR): Brush radius on the screen
        - selectclonesource (scs): Toggle on to select the clone source
        - shapeattr (spa): States if the attribute to paint is an attribute of the shape and not the shader. Default is false.
        - showactive (sa): Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        - soloAsDiffuse (sod): States if the currently paintable texture will be rendered as as diffuse texture in the viewport. Default is false.
        - stampDepth (stD): Depth of the stamps
        - stampProfile (stP): Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        - stampSpacing (stS): Specifies the stamp spacing. Default is 1.0.
        - strokesmooth (ssm): Stroke smoothing type name
        - surfaceConformedBrushVertices (scv): Enables/disables the the display of the effective brush area as affected vertices.
        - tangentOutline (to): Enables/disables the display of the brush circle tangent to the surface.
        - updateEraseTex (uet): Should the erase texture update?
        - usepressure (up): Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        - worldRadius (wlR): Radius in worldspace
        - edit (e): Edit mode flag
    """
