"""Stub files for Display category in Maya commands, command: weightsColor."""

from typing import Any, overload

@overload #Overload for weightsColor in ['query']
def weightsColor([objects...]: [objects...], colorRamp: str = ..., deformer: str = ..., falseColor: bool = ..., outOfRangeColor: [float, float, float] = ..., rampMaxColor: [float, float, float] = ..., rampMinColor: [float, float, float] = ..., useColorRamp: bool = ..., useMaxMinColor: bool = ..., query: bool = ...) -> list[str]:
    """weightsColor is undoable, queryable, and NOT editable.
    
    Controls the coloring of deformer weights.

    Example:
    ```python
        import maya.cmds as cmds
        # Turn on weight visualization for the cluster1 deformer on pSphere1
        cmds.weightsColor('pSphere1', fc=True, dfm='cluster1')
        # Turn off weight visualization for pSphere1
        cmds.weightsColor('pSphere1', fc=False)
        # Turn of the colorRamp
        cmds.weightsColor(useColorRamp=False)
        # Use a purple min color and green max color
        cmds.weightsColor(umc=True, rmc=(1.0,0.0,1.0), rxc=(0.0,1.0,0.0))
        # Set the outOfRange color for verts outside the deformers subset
        cmds.weightsColor(orc=(0.0,1.0,1.0))
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - colorRamp (cr): Allows a user defined color ramp to be used to map values to colors.
        - deformer (dfm): Specify the deformer that needs to be visualized.
        - falseColor (fc): Enable or disable false color display on the geometry.
        - outOfRangeColor (orc): Defines a special color to be used for the areas outside the deformers subset.
        - rampMaxColor (rxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - rampMinColor (rmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - useColorRamp (ucr): Specifies whether the user defined color ramp should be used to map values from to colors. If this is turned off, the default greyscale feedback will be used.
        - useMaxMinColor (umc): Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        - query (q): Query mode flag
    """
@overload #Overload for weightsColor in ['query']
def weightsColor([objects...]: [objects...], cr: str = ..., dfm: str = ..., fc: bool = ..., orc: [float, float, float] = ..., rxc: [float, float, float] = ..., rmc: [float, float, float] = ..., ucr: bool = ..., umc: bool = ..., q: bool = ...) -> list[str]:
    """weightsColor is undoable, queryable, and NOT editable.
    
    Controls the coloring of deformer weights.

    Example:
    ```python
        import maya.cmds as cmds
        # Turn on weight visualization for the cluster1 deformer on pSphere1
        cmds.weightsColor('pSphere1', fc=True, dfm='cluster1')
        # Turn off weight visualization for pSphere1
        cmds.weightsColor('pSphere1', fc=False)
        # Turn of the colorRamp
        cmds.weightsColor(useColorRamp=False)
        # Use a purple min color and green max color
        cmds.weightsColor(umc=True, rmc=(1.0,0.0,1.0), rxc=(0.0,1.0,0.0))
        # Set the outOfRange color for verts outside the deformers subset
        cmds.weightsColor(orc=(0.0,1.0,1.0))
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - colorRamp (cr): Allows a user defined color ramp to be used to map values to colors.
        - deformer (dfm): Specify the deformer that needs to be visualized.
        - falseColor (fc): Enable or disable false color display on the geometry.
        - outOfRangeColor (orc): Defines a special color to be used for the areas outside the deformers subset.
        - rampMaxColor (rxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - rampMinColor (rmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - useColorRamp (ucr): Specifies whether the user defined color ramp should be used to map values from to colors. If this is turned off, the default greyscale feedback will be used.
        - useMaxMinColor (umc): Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        - query (q): Query mode flag
    """
@overload #Overload for weightsColor in ['query']
def weightsColor([objects...]: [objects...], colorRamp: str = ..., cr: str = ..., deformer: str = ..., dfm: str = ..., falseColor: bool = ..., fc: bool = ..., outOfRangeColor: [float, float, float] = ..., orc: [float, float, float] = ..., rampMaxColor: [float, float, float] = ..., rxc: [float, float, float] = ..., rampMinColor: [float, float, float] = ..., rmc: [float, float, float] = ..., useColorRamp: bool = ..., ucr: bool = ..., useMaxMinColor: bool = ..., umc: bool = ..., query: bool = ..., q: bool = ...) -> list[str]:
    """weightsColor is undoable, queryable, and NOT editable.
    
    Controls the coloring of deformer weights.

    Example:
    ```python
        import maya.cmds as cmds
        # Turn on weight visualization for the cluster1 deformer on pSphere1
        cmds.weightsColor('pSphere1', fc=True, dfm='cluster1')
        # Turn off weight visualization for pSphere1
        cmds.weightsColor('pSphere1', fc=False)
        # Turn of the colorRamp
        cmds.weightsColor(useColorRamp=False)
        # Use a purple min color and green max color
        cmds.weightsColor(umc=True, rmc=(1.0,0.0,1.0), rxc=(0.0,1.0,0.0))
        # Set the outOfRange color for verts outside the deformers subset
        cmds.weightsColor(orc=(0.0,1.0,1.0))
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - colorRamp (cr): Allows a user defined color ramp to be used to map values to colors.
        - deformer (dfm): Specify the deformer that needs to be visualized.
        - falseColor (fc): Enable or disable false color display on the geometry.
        - outOfRangeColor (orc): Defines a special color to be used for the areas outside the deformers subset.
        - rampMaxColor (rxc): Defines a special color to be used when the value is greater than or equal to the maximum value.
        - rampMinColor (rmc): Defines a special color to be used when the value is less than or equal to the minimum value.
        - useColorRamp (ucr): Specifies whether the user defined color ramp should be used to map values from to colors. If this is turned off, the default greyscale feedback will be used.
        - useMaxMinColor (umc): Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        - query (q): Query mode flag
    """
