"""Stub files for Contexts category in Maya commands, command: propModCtx."""

from typing import Any, overload

@overload #Overload for propModCtx in ['create']
def propModCtx(string: str, animCurve: str = ..., animCurveFalloff: [float, float] = ..., animCurveParam: str = ..., direction: [float, float, float] = ..., exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., linear: float = ..., linearParam: [float, float] = ..., nurbsCurve: str = ..., powerCutoff: float = ..., powerCutoffParam: [float, float] = ..., powerDegree: float = ..., powerDegreeParam: float = ..., script: str = ..., scriptParam: str = ..., type: int = ..., worldspace: bool = ...) -> str:
    """propModCtx is undoable, queryable, and editable.
    
    Controls the proportional move context.

    Example:
    ```python
        import maya.cmds as cmds
        # Edit type of propmod context.
        cmds.propModCtx( 'PropMod', e=True, t=1 )
        # Activate propmod context.
        cmds.setToolTo( 'PropMod' )
        # Change the type and dropoff.
        cmds.propModCtx( 'PropMod', e=True, d=(0, 1, 0) )
    ```

    ---
    - Args:
        - string: Input item(s).
        - animCurve (ac): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds".  The profile of the curve will be used as the profile for propmod function.
        - animCurveFalloff (acf): The profile of the curve will be used as the profile for propmod function in both U and V. This will be scaled in U, V according to the paramters provided. The ratio of the U, V scaling parameters will dictate the footprint of the fuction
            while the curve itself provides the magnitudes.
        - animCurveParam (acp): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds", where 1 second maps to 0.01 units in parametric space.
        - direction (d): Direction along which to compute the distance for the distance based drop-off functions.  The default is (1 1 1)
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - linear (l): If using linear drop-off function, this is its slope.  The default of -0.1 means the point at the locator moves with it and the point 10 units away doesn't move at all.
        - linearParam (lp): If using parametric linear drop-off function, these specify its limits along the U and V directions.
        - nurbsCurve (nc): Name of the nurbs curve to use as a drop-off curve. The closest point distance would be used as the drop off percentage.
        - powerCutoff (pc): If using the power drop-off function, this is its distance cutoff value.  The default is 10.0.
        - powerCutoffParam (pcp): If using the power drop-off function, these specify one of it's limits, 0 for U, and 1 and V.  The default cutoff is 10.0.
        - powerDegree (pd): If using the power drop-off function, this is its degree.  The default is 3.
        - powerDegreeParam (pdp): If using the power drop-off function, this is its degree.  The default is 3.
        - script (s): The name of the script to use to compute the drop-off. The script takes 6 floats as input - first 3 are the position of the move locator, the next 3 the position of the point to be manipulated.  The script should return a drop-off
            coefficient which could be negative or zero.
        - scriptParam (sp): The name of the script to use to compute the drop-off. The script takes 4 floats as input - first 2 are the parametric position of the move locator, the next 2 the parametric position of the point to be manipulated.  The script should
            return a drop-off coefficient which could be negative or zero.
        - type (t): Choose the type for the drop-off function.  Legal values are 1 for linear, 2 for power, 3 for script, 4 for anim curve. The default is 1.
        - worldspace (ws): Set the space in which the tool works. True for world space, false for parametric space.
    """
@overload #Overload for propModCtx in ['create']
def propModCtx(string: str, ac: str = ..., acf: [float, float] = ..., acp: str = ..., d: [float, float, float] = ..., ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., l: float = ..., lp: [float, float] = ..., nc: str = ..., pc: float = ..., pcp: [float, float] = ..., pd: float = ..., pdp: float = ..., s: str = ..., sp: str = ..., t: int = ..., ws: bool = ...) -> str:
    """propModCtx is undoable, queryable, and editable.
    
    Controls the proportional move context.

    Example:
    ```python
        import maya.cmds as cmds
        # Edit type of propmod context.
        cmds.propModCtx( 'PropMod', e=True, t=1 )
        # Activate propmod context.
        cmds.setToolTo( 'PropMod' )
        # Change the type and dropoff.
        cmds.propModCtx( 'PropMod', e=True, d=(0, 1, 0) )
    ```

    ---
    - Args:
        - string: Input item(s).
        - animCurve (ac): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds".  The profile of the curve will be used as the profile for propmod function.
        - animCurveFalloff (acf): The profile of the curve will be used as the profile for propmod function in both U and V. This will be scaled in U, V according to the paramters provided. The ratio of the U, V scaling parameters will dictate the footprint of the fuction
            while the curve itself provides the magnitudes.
        - animCurveParam (acp): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds", where 1 second maps to 0.01 units in parametric space.
        - direction (d): Direction along which to compute the distance for the distance based drop-off functions.  The default is (1 1 1)
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - linear (l): If using linear drop-off function, this is its slope.  The default of -0.1 means the point at the locator moves with it and the point 10 units away doesn't move at all.
        - linearParam (lp): If using parametric linear drop-off function, these specify its limits along the U and V directions.
        - nurbsCurve (nc): Name of the nurbs curve to use as a drop-off curve. The closest point distance would be used as the drop off percentage.
        - powerCutoff (pc): If using the power drop-off function, this is its distance cutoff value.  The default is 10.0.
        - powerCutoffParam (pcp): If using the power drop-off function, these specify one of it's limits, 0 for U, and 1 and V.  The default cutoff is 10.0.
        - powerDegree (pd): If using the power drop-off function, this is its degree.  The default is 3.
        - powerDegreeParam (pdp): If using the power drop-off function, this is its degree.  The default is 3.
        - script (s): The name of the script to use to compute the drop-off. The script takes 6 floats as input - first 3 are the position of the move locator, the next 3 the position of the point to be manipulated.  The script should return a drop-off
            coefficient which could be negative or zero.
        - scriptParam (sp): The name of the script to use to compute the drop-off. The script takes 4 floats as input - first 2 are the parametric position of the move locator, the next 2 the parametric position of the point to be manipulated.  The script should
            return a drop-off coefficient which could be negative or zero.
        - type (t): Choose the type for the drop-off function.  Legal values are 1 for linear, 2 for power, 3 for script, 4 for anim curve. The default is 1.
        - worldspace (ws): Set the space in which the tool works. True for world space, false for parametric space.
    """
@overload #Overload for propModCtx in ['create']
def propModCtx(string: str, animCurve: str = ..., ac: str = ..., animCurveFalloff: [float, float] = ..., acf: [float, float] = ..., animCurveParam: str = ..., acp: str = ..., direction: [float, float, float] = ..., d: [float, float, float] = ..., exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., linear: float = ..., l: float = ..., linearParam: [float, float] = ..., lp: [float, float] = ..., nurbsCurve: str = ..., nc: str = ..., powerCutoff: float = ..., pc: float = ..., powerCutoffParam: [float, float] = ..., pcp: [float, float] = ..., powerDegree: float = ..., pd: float = ..., powerDegreeParam: float = ..., pdp: float = ..., script: str = ..., s: str = ..., scriptParam: str = ..., sp: str = ..., type: int = ..., t: int = ..., worldspace: bool = ..., ws: bool = ...) -> str:
    """propModCtx is undoable, queryable, and editable.
    
    Controls the proportional move context.

    Example:
    ```python
        import maya.cmds as cmds
        # Edit type of propmod context.
        cmds.propModCtx( 'PropMod', e=True, t=1 )
        # Activate propmod context.
        cmds.setToolTo( 'PropMod' )
        # Change the type and dropoff.
        cmds.propModCtx( 'PropMod', e=True, d=(0, 1, 0) )
    ```

    ---
    - Args:
        - string: Input item(s).
        - animCurve (ac): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds".  The profile of the curve will be used as the profile for propmod function.
        - animCurveFalloff (acf): The profile of the curve will be used as the profile for propmod function in both U and V. This will be scaled in U, V according to the paramters provided. The ratio of the U, V scaling parameters will dictate the footprint of the fuction
            while the curve itself provides the magnitudes.
        - animCurveParam (acp): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds", where 1 second maps to 0.01 units in parametric space.
        - direction (d): Direction along which to compute the distance for the distance based drop-off functions.  The default is (1 1 1)
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - linear (l): If using linear drop-off function, this is its slope.  The default of -0.1 means the point at the locator moves with it and the point 10 units away doesn't move at all.
        - linearParam (lp): If using parametric linear drop-off function, these specify its limits along the U and V directions.
        - nurbsCurve (nc): Name of the nurbs curve to use as a drop-off curve. The closest point distance would be used as the drop off percentage.
        - powerCutoff (pc): If using the power drop-off function, this is its distance cutoff value.  The default is 10.0.
        - powerCutoffParam (pcp): If using the power drop-off function, these specify one of it's limits, 0 for U, and 1 and V.  The default cutoff is 10.0.
        - powerDegree (pd): If using the power drop-off function, this is its degree.  The default is 3.
        - powerDegreeParam (pdp): If using the power drop-off function, this is its degree.  The default is 3.
        - script (s): The name of the script to use to compute the drop-off. The script takes 6 floats as input - first 3 are the position of the move locator, the next 3 the position of the point to be manipulated.  The script should return a drop-off
            coefficient which could be negative or zero.
        - scriptParam (sp): The name of the script to use to compute the drop-off. The script takes 4 floats as input - first 2 are the parametric position of the move locator, the next 2 the parametric position of the point to be manipulated.  The script should
            return a drop-off coefficient which could be negative or zero.
        - type (t): Choose the type for the drop-off function.  Legal values are 1 for linear, 2 for power, 3 for script, 4 for anim curve. The default is 1.
        - worldspace (ws): Set the space in which the tool works. True for world space, false for parametric space.
    """
@overload #Overload for propModCtx in ['query']
def propModCtx(string: str, animCurve: str = ..., animCurveFalloff: [float, float] = ..., animCurveParam: str = ..., direction: [float, float, float] = ..., image1: str = ..., image2: str = ..., image3: str = ..., linear: float = ..., linearParam: [float, float] = ..., nurbsCurve: str = ..., powerCutoff: float = ..., powerCutoffParam: [float, float] = ..., powerDegree: float = ..., powerDegreeParam: float = ..., script: str = ..., scriptParam: str = ..., type: int = ..., worldspace: bool = ..., query: bool = ...) -> str:
    """propModCtx is undoable, queryable, and editable.
    
    Controls the proportional move context.

    Example:
    ```python
        import maya.cmds as cmds
        # Edit type of propmod context.
        cmds.propModCtx( 'PropMod', e=True, t=1 )
        # Activate propmod context.
        cmds.setToolTo( 'PropMod' )
        # Change the type and dropoff.
        cmds.propModCtx( 'PropMod', e=True, d=(0, 1, 0) )
    ```

    ---
    - Args:
        - string: Input item(s).
        - animCurve (ac): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds".  The profile of the curve will be used as the profile for propmod function.
        - animCurveFalloff (acf): The profile of the curve will be used as the profile for propmod function in both U and V. This will be scaled in U, V according to the paramters provided. The ratio of the U, V scaling parameters will dictate the footprint of the fuction
            while the curve itself provides the magnitudes.
        - animCurveParam (acp): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds", where 1 second maps to 0.01 units in parametric space.
        - direction (d): Direction along which to compute the distance for the distance based drop-off functions.  The default is (1 1 1)
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - linear (l): If using linear drop-off function, this is its slope.  The default of -0.1 means the point at the locator moves with it and the point 10 units away doesn't move at all.
        - linearParam (lp): If using parametric linear drop-off function, these specify its limits along the U and V directions.
        - nurbsCurve (nc): Name of the nurbs curve to use as a drop-off curve. The closest point distance would be used as the drop off percentage.
        - powerCutoff (pc): If using the power drop-off function, this is its distance cutoff value.  The default is 10.0.
        - powerCutoffParam (pcp): If using the power drop-off function, these specify one of it's limits, 0 for U, and 1 and V.  The default cutoff is 10.0.
        - powerDegree (pd): If using the power drop-off function, this is its degree.  The default is 3.
        - powerDegreeParam (pdp): If using the power drop-off function, this is its degree.  The default is 3.
        - script (s): The name of the script to use to compute the drop-off. The script takes 6 floats as input - first 3 are the position of the move locator, the next 3 the position of the point to be manipulated.  The script should return a drop-off
            coefficient which could be negative or zero.
        - scriptParam (sp): The name of the script to use to compute the drop-off. The script takes 4 floats as input - first 2 are the parametric position of the move locator, the next 2 the parametric position of the point to be manipulated.  The script should
            return a drop-off coefficient which could be negative or zero.
        - type (t): Choose the type for the drop-off function.  Legal values are 1 for linear, 2 for power, 3 for script, 4 for anim curve. The default is 1.
        - worldspace (ws): Set the space in which the tool works. True for world space, false for parametric space.
        - query (q): Query mode flag
    """
@overload #Overload for propModCtx in ['query']
def propModCtx(string: str, ac: str = ..., acf: [float, float] = ..., acp: str = ..., d: [float, float, float] = ..., i1: str = ..., i2: str = ..., i3: str = ..., l: float = ..., lp: [float, float] = ..., nc: str = ..., pc: float = ..., pcp: [float, float] = ..., pd: float = ..., pdp: float = ..., s: str = ..., sp: str = ..., t: int = ..., ws: bool = ..., q: bool = ...) -> str:
    """propModCtx is undoable, queryable, and editable.
    
    Controls the proportional move context.

    Example:
    ```python
        import maya.cmds as cmds
        # Edit type of propmod context.
        cmds.propModCtx( 'PropMod', e=True, t=1 )
        # Activate propmod context.
        cmds.setToolTo( 'PropMod' )
        # Change the type and dropoff.
        cmds.propModCtx( 'PropMod', e=True, d=(0, 1, 0) )
    ```

    ---
    - Args:
        - string: Input item(s).
        - animCurve (ac): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds".  The profile of the curve will be used as the profile for propmod function.
        - animCurveFalloff (acf): The profile of the curve will be used as the profile for propmod function in both U and V. This will be scaled in U, V according to the paramters provided. The ratio of the U, V scaling parameters will dictate the footprint of the fuction
            while the curve itself provides the magnitudes.
        - animCurveParam (acp): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds", where 1 second maps to 0.01 units in parametric space.
        - direction (d): Direction along which to compute the distance for the distance based drop-off functions.  The default is (1 1 1)
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - linear (l): If using linear drop-off function, this is its slope.  The default of -0.1 means the point at the locator moves with it and the point 10 units away doesn't move at all.
        - linearParam (lp): If using parametric linear drop-off function, these specify its limits along the U and V directions.
        - nurbsCurve (nc): Name of the nurbs curve to use as a drop-off curve. The closest point distance would be used as the drop off percentage.
        - powerCutoff (pc): If using the power drop-off function, this is its distance cutoff value.  The default is 10.0.
        - powerCutoffParam (pcp): If using the power drop-off function, these specify one of it's limits, 0 for U, and 1 and V.  The default cutoff is 10.0.
        - powerDegree (pd): If using the power drop-off function, this is its degree.  The default is 3.
        - powerDegreeParam (pdp): If using the power drop-off function, this is its degree.  The default is 3.
        - script (s): The name of the script to use to compute the drop-off. The script takes 6 floats as input - first 3 are the position of the move locator, the next 3 the position of the point to be manipulated.  The script should return a drop-off
            coefficient which could be negative or zero.
        - scriptParam (sp): The name of the script to use to compute the drop-off. The script takes 4 floats as input - first 2 are the parametric position of the move locator, the next 2 the parametric position of the point to be manipulated.  The script should
            return a drop-off coefficient which could be negative or zero.
        - type (t): Choose the type for the drop-off function.  Legal values are 1 for linear, 2 for power, 3 for script, 4 for anim curve. The default is 1.
        - worldspace (ws): Set the space in which the tool works. True for world space, false for parametric space.
        - query (q): Query mode flag
    """
@overload #Overload for propModCtx in ['query']
def propModCtx(string: str, animCurve: str = ..., ac: str = ..., animCurveFalloff: [float, float] = ..., acf: [float, float] = ..., animCurveParam: str = ..., acp: str = ..., direction: [float, float, float] = ..., d: [float, float, float] = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., linear: float = ..., l: float = ..., linearParam: [float, float] = ..., lp: [float, float] = ..., nurbsCurve: str = ..., nc: str = ..., powerCutoff: float = ..., pc: float = ..., powerCutoffParam: [float, float] = ..., pcp: [float, float] = ..., powerDegree: float = ..., pd: float = ..., powerDegreeParam: float = ..., pdp: float = ..., script: str = ..., s: str = ..., scriptParam: str = ..., sp: str = ..., type: int = ..., t: int = ..., worldspace: bool = ..., ws: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """propModCtx is undoable, queryable, and editable.
    
    Controls the proportional move context.

    Example:
    ```python
        import maya.cmds as cmds
        # Edit type of propmod context.
        cmds.propModCtx( 'PropMod', e=True, t=1 )
        # Activate propmod context.
        cmds.setToolTo( 'PropMod' )
        # Change the type and dropoff.
        cmds.propModCtx( 'PropMod', e=True, d=(0, 1, 0) )
    ```

    ---
    - Args:
        - string: Input item(s).
        - animCurve (ac): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds".  The profile of the curve will be used as the profile for propmod function.
        - animCurveFalloff (acf): The profile of the curve will be used as the profile for propmod function in both U and V. This will be scaled in U, V according to the paramters provided. The ratio of the U, V scaling parameters will dictate the footprint of the fuction
            while the curve itself provides the magnitudes.
        - animCurveParam (acp): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds", where 1 second maps to 0.01 units in parametric space.
        - direction (d): Direction along which to compute the distance for the distance based drop-off functions.  The default is (1 1 1)
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - linear (l): If using linear drop-off function, this is its slope.  The default of -0.1 means the point at the locator moves with it and the point 10 units away doesn't move at all.
        - linearParam (lp): If using parametric linear drop-off function, these specify its limits along the U and V directions.
        - nurbsCurve (nc): Name of the nurbs curve to use as a drop-off curve. The closest point distance would be used as the drop off percentage.
        - powerCutoff (pc): If using the power drop-off function, this is its distance cutoff value.  The default is 10.0.
        - powerCutoffParam (pcp): If using the power drop-off function, these specify one of it's limits, 0 for U, and 1 and V.  The default cutoff is 10.0.
        - powerDegree (pd): If using the power drop-off function, this is its degree.  The default is 3.
        - powerDegreeParam (pdp): If using the power drop-off function, this is its degree.  The default is 3.
        - script (s): The name of the script to use to compute the drop-off. The script takes 6 floats as input - first 3 are the position of the move locator, the next 3 the position of the point to be manipulated.  The script should return a drop-off
            coefficient which could be negative or zero.
        - scriptParam (sp): The name of the script to use to compute the drop-off. The script takes 4 floats as input - first 2 are the parametric position of the move locator, the next 2 the parametric position of the point to be manipulated.  The script should
            return a drop-off coefficient which could be negative or zero.
        - type (t): Choose the type for the drop-off function.  Legal values are 1 for linear, 2 for power, 3 for script, 4 for anim curve. The default is 1.
        - worldspace (ws): Set the space in which the tool works. True for world space, false for parametric space.
        - query (q): Query mode flag
    """
@overload #Overload for propModCtx in ['edit']
def propModCtx(string: str, animCurve: str = ..., animCurveFalloff: [float, float] = ..., animCurveParam: str = ..., direction: [float, float, float] = ..., image1: str = ..., image2: str = ..., image3: str = ..., linear: float = ..., linearParam: [float, float] = ..., nurbsCurve: str = ..., powerCutoff: float = ..., powerCutoffParam: [float, float] = ..., powerDegree: float = ..., powerDegreeParam: float = ..., script: str = ..., scriptParam: str = ..., type: int = ..., worldspace: bool = ..., edit: bool = ...) -> str:
    """propModCtx is undoable, queryable, and editable.
    
    Controls the proportional move context.

    Example:
    ```python
        import maya.cmds as cmds
        # Edit type of propmod context.
        cmds.propModCtx( 'PropMod', e=True, t=1 )
        # Activate propmod context.
        cmds.setToolTo( 'PropMod' )
        # Change the type and dropoff.
        cmds.propModCtx( 'PropMod', e=True, d=(0, 1, 0) )
    ```

    ---
    - Args:
        - string: Input item(s).
        - animCurve (ac): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds".  The profile of the curve will be used as the profile for propmod function.
        - animCurveFalloff (acf): The profile of the curve will be used as the profile for propmod function in both U and V. This will be scaled in U, V according to the paramters provided. The ratio of the U, V scaling parameters will dictate the footprint of the fuction
            while the curve itself provides the magnitudes.
        - animCurveParam (acp): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds", where 1 second maps to 0.01 units in parametric space.
        - direction (d): Direction along which to compute the distance for the distance based drop-off functions.  The default is (1 1 1)
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - linear (l): If using linear drop-off function, this is its slope.  The default of -0.1 means the point at the locator moves with it and the point 10 units away doesn't move at all.
        - linearParam (lp): If using parametric linear drop-off function, these specify its limits along the U and V directions.
        - nurbsCurve (nc): Name of the nurbs curve to use as a drop-off curve. The closest point distance would be used as the drop off percentage.
        - powerCutoff (pc): If using the power drop-off function, this is its distance cutoff value.  The default is 10.0.
        - powerCutoffParam (pcp): If using the power drop-off function, these specify one of it's limits, 0 for U, and 1 and V.  The default cutoff is 10.0.
        - powerDegree (pd): If using the power drop-off function, this is its degree.  The default is 3.
        - powerDegreeParam (pdp): If using the power drop-off function, this is its degree.  The default is 3.
        - script (s): The name of the script to use to compute the drop-off. The script takes 6 floats as input - first 3 are the position of the move locator, the next 3 the position of the point to be manipulated.  The script should return a drop-off
            coefficient which could be negative or zero.
        - scriptParam (sp): The name of the script to use to compute the drop-off. The script takes 4 floats as input - first 2 are the parametric position of the move locator, the next 2 the parametric position of the point to be manipulated.  The script should
            return a drop-off coefficient which could be negative or zero.
        - type (t): Choose the type for the drop-off function.  Legal values are 1 for linear, 2 for power, 3 for script, 4 for anim curve. The default is 1.
        - worldspace (ws): Set the space in which the tool works. True for world space, false for parametric space.
        - edit (e): Edit mode flag
    """
@overload #Overload for propModCtx in ['edit']
def propModCtx(string: str, ac: str = ..., acf: [float, float] = ..., acp: str = ..., d: [float, float, float] = ..., i1: str = ..., i2: str = ..., i3: str = ..., l: float = ..., lp: [float, float] = ..., nc: str = ..., pc: float = ..., pcp: [float, float] = ..., pd: float = ..., pdp: float = ..., s: str = ..., sp: str = ..., t: int = ..., ws: bool = ..., e: bool = ...) -> str:
    """propModCtx is undoable, queryable, and editable.
    
    Controls the proportional move context.

    Example:
    ```python
        import maya.cmds as cmds
        # Edit type of propmod context.
        cmds.propModCtx( 'PropMod', e=True, t=1 )
        # Activate propmod context.
        cmds.setToolTo( 'PropMod' )
        # Change the type and dropoff.
        cmds.propModCtx( 'PropMod', e=True, d=(0, 1, 0) )
    ```

    ---
    - Args:
        - string: Input item(s).
        - animCurve (ac): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds".  The profile of the curve will be used as the profile for propmod function.
        - animCurveFalloff (acf): The profile of the curve will be used as the profile for propmod function in both U and V. This will be scaled in U, V according to the paramters provided. The ratio of the U, V scaling parameters will dictate the footprint of the fuction
            while the curve itself provides the magnitudes.
        - animCurveParam (acp): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds", where 1 second maps to 0.01 units in parametric space.
        - direction (d): Direction along which to compute the distance for the distance based drop-off functions.  The default is (1 1 1)
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - linear (l): If using linear drop-off function, this is its slope.  The default of -0.1 means the point at the locator moves with it and the point 10 units away doesn't move at all.
        - linearParam (lp): If using parametric linear drop-off function, these specify its limits along the U and V directions.
        - nurbsCurve (nc): Name of the nurbs curve to use as a drop-off curve. The closest point distance would be used as the drop off percentage.
        - powerCutoff (pc): If using the power drop-off function, this is its distance cutoff value.  The default is 10.0.
        - powerCutoffParam (pcp): If using the power drop-off function, these specify one of it's limits, 0 for U, and 1 and V.  The default cutoff is 10.0.
        - powerDegree (pd): If using the power drop-off function, this is its degree.  The default is 3.
        - powerDegreeParam (pdp): If using the power drop-off function, this is its degree.  The default is 3.
        - script (s): The name of the script to use to compute the drop-off. The script takes 6 floats as input - first 3 are the position of the move locator, the next 3 the position of the point to be manipulated.  The script should return a drop-off
            coefficient which could be negative or zero.
        - scriptParam (sp): The name of the script to use to compute the drop-off. The script takes 4 floats as input - first 2 are the parametric position of the move locator, the next 2 the parametric position of the point to be manipulated.  The script should
            return a drop-off coefficient which could be negative or zero.
        - type (t): Choose the type for the drop-off function.  Legal values are 1 for linear, 2 for power, 3 for script, 4 for anim curve. The default is 1.
        - worldspace (ws): Set the space in which the tool works. True for world space, false for parametric space.
        - edit (e): Edit mode flag
    """
@overload #Overload for propModCtx in ['edit']
def propModCtx(string: str, animCurve: str = ..., ac: str = ..., animCurveFalloff: [float, float] = ..., acf: [float, float] = ..., animCurveParam: str = ..., acp: str = ..., direction: [float, float, float] = ..., d: [float, float, float] = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., linear: float = ..., l: float = ..., linearParam: [float, float] = ..., lp: [float, float] = ..., nurbsCurve: str = ..., nc: str = ..., powerCutoff: float = ..., pc: float = ..., powerCutoffParam: [float, float] = ..., pcp: [float, float] = ..., powerDegree: float = ..., pd: float = ..., powerDegreeParam: float = ..., pdp: float = ..., script: str = ..., s: str = ..., scriptParam: str = ..., sp: str = ..., type: int = ..., t: int = ..., worldspace: bool = ..., ws: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """propModCtx is undoable, queryable, and editable.
    
    Controls the proportional move context.

    Example:
    ```python
        import maya.cmds as cmds
        # Edit type of propmod context.
        cmds.propModCtx( 'PropMod', e=True, t=1 )
        # Activate propmod context.
        cmds.setToolTo( 'PropMod' )
        # Change the type and dropoff.
        cmds.propModCtx( 'PropMod', e=True, d=(0, 1, 0) )
    ```

    ---
    - Args:
        - string: Input item(s).
        - animCurve (ac): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds".  The profile of the curve will be used as the profile for propmod function.
        - animCurveFalloff (acf): The profile of the curve will be used as the profile for propmod function in both U and V. This will be scaled in U, V according to the paramters provided. The ratio of the U, V scaling parameters will dictate the footprint of the fuction
            while the curve itself provides the magnitudes.
        - animCurveParam (acp): Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds", where 1 second maps to 0.01 units in parametric space.
        - direction (d): Direction along which to compute the distance for the distance based drop-off functions.  The default is (1 1 1)
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - linear (l): If using linear drop-off function, this is its slope.  The default of -0.1 means the point at the locator moves with it and the point 10 units away doesn't move at all.
        - linearParam (lp): If using parametric linear drop-off function, these specify its limits along the U and V directions.
        - nurbsCurve (nc): Name of the nurbs curve to use as a drop-off curve. The closest point distance would be used as the drop off percentage.
        - powerCutoff (pc): If using the power drop-off function, this is its distance cutoff value.  The default is 10.0.
        - powerCutoffParam (pcp): If using the power drop-off function, these specify one of it's limits, 0 for U, and 1 and V.  The default cutoff is 10.0.
        - powerDegree (pd): If using the power drop-off function, this is its degree.  The default is 3.
        - powerDegreeParam (pdp): If using the power drop-off function, this is its degree.  The default is 3.
        - script (s): The name of the script to use to compute the drop-off. The script takes 6 floats as input - first 3 are the position of the move locator, the next 3 the position of the point to be manipulated.  The script should return a drop-off
            coefficient which could be negative or zero.
        - scriptParam (sp): The name of the script to use to compute the drop-off. The script takes 4 floats as input - first 2 are the parametric position of the move locator, the next 2 the parametric position of the point to be manipulated.  The script should
            return a drop-off coefficient which could be negative or zero.
        - type (t): Choose the type for the drop-off function.  Legal values are 1 for linear, 2 for power, 3 for script, 4 for anim curve. The default is 1.
        - worldspace (ws): Set the space in which the tool works. True for world space, false for parametric space.
        - edit (e): Edit mode flag
    """
