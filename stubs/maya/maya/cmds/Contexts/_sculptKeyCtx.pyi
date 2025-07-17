"""Stub files for Contexts category in Maya commands, command: sculptKeyCtx."""

from typing import Any, overload

@overload #Overload for sculptKeyCtx in ['create']
def sculptKeyCtx(contextName: contextName, affectsTime: bool = ..., affectsTimeAll: str = ..., brushScaling: int = ..., editingRadius: bool = ..., editingStrength: bool = ..., exists: bool = ..., falloffCurve: str = ..., falloffCurveAll: str = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., minRadius: float = ..., minStrength: float = ..., minStrengthAll: str = ..., mode: int = ..., modeMinStrength: [int, float] = ..., modeStrength: [int, float] = ..., name: str = ..., radius: float = ..., strength: float = ..., strengthAll: str = ...) -> str:
    """sculptKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with a
    sculpt brush. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a sculpt key context in grab mode.
        cmds.sculptKeyCtx('sculptKeyContext', mode=0)
        # Switch to smooth mode and set the sculpt radius to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, mode=1, radius=50)
        # Set the strength for the grab and smooth modes to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, modeStrength=((0,50),(1,50)))
        # Set the strength for all modes to 80.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, strengthAll=(80, 80, 80))
        // Activate affects time option
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, affectsTime=1)
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - affectsTime (at): Specifies whether or not the sculpt tools affect the time as well as the value of the keys.
        - affectsTimeAll (ata): Specifies whether or not the sculpt tools affect the time as well as the value of the keys for all modes.
        - brushScaling (brs): Specifies how the sculpt brush scales relative to the Graph Editor. 1 = no scaling, 2 = scaling based on time, 3 = scaling based on value
        - editingRadius (er): Enables or disables interactive radius scaling.
        - editingStrength (es): Enables or disables interactive strength scaling.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - falloffCurve (fc): Specifies the falloff curve of the sculpting effect.
        - falloffCurveAll (fca): Internal flag used to save/restore falloff curves for all modes.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - minRadius (mr): Specifies the minumum radius the sculpt brush will take due to stylus pressure. Cannot be more than the base brush radius.
        - minStrength (ms): Specifies the minumum strength of sculpting due to stylus pressure. Cannot be more than the base strength.
        - minStrengthAll (msa): Internal flag used to save/restore min strength for all modes.
        - mode (m): Specifies the base sculpt mode. 0 = grab, 1 = smooth 2 = smear 3 = reduce
        - modeMinStrength (mms): Specifies the min strength for the specified mode.
        - modeStrength (mst): Specifies the strength for the specified mode.
        - name (n): If this is a tool command, name the tool appropriately.
        - radius (r): Specifies the radius of the sculpt brush.
        - strength (s): Specifies the strength of the sculpting effect for the current mode. Each mode can have a different strength.
        - strengthAll (sa): Internal flag used to save/restore strength for all modes.
    """
@overload #Overload for sculptKeyCtx in ['create']
def sculptKeyCtx(contextName: contextName, at: bool = ..., ata: str = ..., brs: int = ..., er: bool = ..., es: bool = ..., ex: bool = ..., fc: str = ..., fca: str = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., mr: float = ..., ms: float = ..., msa: str = ..., m: int = ..., mms: [int, float] = ..., mst: [int, float] = ..., n: str = ..., r: float = ..., s: float = ..., sa: str = ...) -> str:
    """sculptKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with a
    sculpt brush. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a sculpt key context in grab mode.
        cmds.sculptKeyCtx('sculptKeyContext', mode=0)
        # Switch to smooth mode and set the sculpt radius to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, mode=1, radius=50)
        # Set the strength for the grab and smooth modes to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, modeStrength=((0,50),(1,50)))
        # Set the strength for all modes to 80.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, strengthAll=(80, 80, 80))
        // Activate affects time option
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, affectsTime=1)
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - affectsTime (at): Specifies whether or not the sculpt tools affect the time as well as the value of the keys.
        - affectsTimeAll (ata): Specifies whether or not the sculpt tools affect the time as well as the value of the keys for all modes.
        - brushScaling (brs): Specifies how the sculpt brush scales relative to the Graph Editor. 1 = no scaling, 2 = scaling based on time, 3 = scaling based on value
        - editingRadius (er): Enables or disables interactive radius scaling.
        - editingStrength (es): Enables or disables interactive strength scaling.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - falloffCurve (fc): Specifies the falloff curve of the sculpting effect.
        - falloffCurveAll (fca): Internal flag used to save/restore falloff curves for all modes.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - minRadius (mr): Specifies the minumum radius the sculpt brush will take due to stylus pressure. Cannot be more than the base brush radius.
        - minStrength (ms): Specifies the minumum strength of sculpting due to stylus pressure. Cannot be more than the base strength.
        - minStrengthAll (msa): Internal flag used to save/restore min strength for all modes.
        - mode (m): Specifies the base sculpt mode. 0 = grab, 1 = smooth 2 = smear 3 = reduce
        - modeMinStrength (mms): Specifies the min strength for the specified mode.
        - modeStrength (mst): Specifies the strength for the specified mode.
        - name (n): If this is a tool command, name the tool appropriately.
        - radius (r): Specifies the radius of the sculpt brush.
        - strength (s): Specifies the strength of the sculpting effect for the current mode. Each mode can have a different strength.
        - strengthAll (sa): Internal flag used to save/restore strength for all modes.
    """
@overload #Overload for sculptKeyCtx in ['create']
def sculptKeyCtx(contextName: contextName, affectsTime: bool = ..., at: bool = ..., affectsTimeAll: str = ..., ata: str = ..., brushScaling: int = ..., brs: int = ..., editingRadius: bool = ..., er: bool = ..., editingStrength: bool = ..., es: bool = ..., exists: bool = ..., ex: bool = ..., falloffCurve: str = ..., fc: str = ..., falloffCurveAll: str = ..., fca: str = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., minRadius: float = ..., mr: float = ..., minStrength: float = ..., ms: float = ..., minStrengthAll: str = ..., msa: str = ..., mode: int = ..., m: int = ..., modeMinStrength: [int, float] = ..., mms: [int, float] = ..., modeStrength: [int, float] = ..., mst: [int, float] = ..., name: str = ..., n: str = ..., radius: float = ..., r: float = ..., strength: float = ..., s: float = ..., strengthAll: str = ..., sa: str = ...) -> str:
    """sculptKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with a
    sculpt brush. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a sculpt key context in grab mode.
        cmds.sculptKeyCtx('sculptKeyContext', mode=0)
        # Switch to smooth mode and set the sculpt radius to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, mode=1, radius=50)
        # Set the strength for the grab and smooth modes to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, modeStrength=((0,50),(1,50)))
        # Set the strength for all modes to 80.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, strengthAll=(80, 80, 80))
        // Activate affects time option
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, affectsTime=1)
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - affectsTime (at): Specifies whether or not the sculpt tools affect the time as well as the value of the keys.
        - affectsTimeAll (ata): Specifies whether or not the sculpt tools affect the time as well as the value of the keys for all modes.
        - brushScaling (brs): Specifies how the sculpt brush scales relative to the Graph Editor. 1 = no scaling, 2 = scaling based on time, 3 = scaling based on value
        - editingRadius (er): Enables or disables interactive radius scaling.
        - editingStrength (es): Enables or disables interactive strength scaling.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - falloffCurve (fc): Specifies the falloff curve of the sculpting effect.
        - falloffCurveAll (fca): Internal flag used to save/restore falloff curves for all modes.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - minRadius (mr): Specifies the minumum radius the sculpt brush will take due to stylus pressure. Cannot be more than the base brush radius.
        - minStrength (ms): Specifies the minumum strength of sculpting due to stylus pressure. Cannot be more than the base strength.
        - minStrengthAll (msa): Internal flag used to save/restore min strength for all modes.
        - mode (m): Specifies the base sculpt mode. 0 = grab, 1 = smooth 2 = smear 3 = reduce
        - modeMinStrength (mms): Specifies the min strength for the specified mode.
        - modeStrength (mst): Specifies the strength for the specified mode.
        - name (n): If this is a tool command, name the tool appropriately.
        - radius (r): Specifies the radius of the sculpt brush.
        - strength (s): Specifies the strength of the sculpting effect for the current mode. Each mode can have a different strength.
        - strengthAll (sa): Internal flag used to save/restore strength for all modes.
    """
@overload #Overload for sculptKeyCtx in ['query']
def sculptKeyCtx(contextName: contextName, activeMode: int = ..., affectsTime: bool = ..., affectsTimeAll: str = ..., brushScaling: int = ..., falloffCurve: str = ..., falloffCurveAll: str = ..., image1: str = ..., image2: str = ..., image3: str = ..., minRadius: float = ..., minStrength: float = ..., minStrengthAll: str = ..., mode: int = ..., radius: float = ..., reset: bool = ..., strength: float = ..., strengthAll: str = ..., query: bool = ...) -> str:
    """sculptKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with a
    sculpt brush. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a sculpt key context in grab mode.
        cmds.sculptKeyCtx('sculptKeyContext', mode=0)
        # Switch to smooth mode and set the sculpt radius to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, mode=1, radius=50)
        # Set the strength for the grab and smooth modes to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, modeStrength=((0,50),(1,50)))
        # Set the strength for all modes to 80.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, strengthAll=(80, 80, 80))
        // Activate affects time option
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, affectsTime=1)
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - activeMode (am): Used to query the current active sculpt mode. This can differ from the base mode if the user is holding down the shift hotkey to temporarily switch to smooth mode.
        - affectsTime (at): Specifies whether or not the sculpt tools affect the time as well as the value of the keys.
        - affectsTimeAll (ata): Specifies whether or not the sculpt tools affect the time as well as the value of the keys for all modes.
        - brushScaling (brs): Specifies how the sculpt brush scales relative to the Graph Editor. 1 = no scaling, 2 = scaling based on time, 3 = scaling based on value
        - falloffCurve (fc): Specifies the falloff curve of the sculpting effect.
        - falloffCurveAll (fca): Internal flag used to save/restore falloff curves for all modes.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - minRadius (mr): Specifies the minumum radius the sculpt brush will take due to stylus pressure. Cannot be more than the base brush radius.
        - minStrength (ms): Specifies the minumum strength of sculpting due to stylus pressure. Cannot be more than the base strength.
        - minStrengthAll (msa): Internal flag used to save/restore min strength for all modes.
        - mode (m): Specifies the base sculpt mode. 0 = grab, 1 = smooth 2 = smear 3 = reduce
        - radius (r): Specifies the radius of the sculpt brush.
        - reset (rs): Internal flag used to reset current tool mode settings.
        - strength (s): Specifies the strength of the sculpting effect for the current mode. Each mode can have a different strength.
        - strengthAll (sa): Internal flag used to save/restore strength for all modes.
        - query (q): Query mode flag
    """
@overload #Overload for sculptKeyCtx in ['query']
def sculptKeyCtx(contextName: contextName, am: int = ..., at: bool = ..., ata: str = ..., brs: int = ..., fc: str = ..., fca: str = ..., i1: str = ..., i2: str = ..., i3: str = ..., mr: float = ..., ms: float = ..., msa: str = ..., m: int = ..., r: float = ..., rs: bool = ..., s: float = ..., sa: str = ..., q: bool = ...) -> str:
    """sculptKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with a
    sculpt brush. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a sculpt key context in grab mode.
        cmds.sculptKeyCtx('sculptKeyContext', mode=0)
        # Switch to smooth mode and set the sculpt radius to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, mode=1, radius=50)
        # Set the strength for the grab and smooth modes to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, modeStrength=((0,50),(1,50)))
        # Set the strength for all modes to 80.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, strengthAll=(80, 80, 80))
        // Activate affects time option
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, affectsTime=1)
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - activeMode (am): Used to query the current active sculpt mode. This can differ from the base mode if the user is holding down the shift hotkey to temporarily switch to smooth mode.
        - affectsTime (at): Specifies whether or not the sculpt tools affect the time as well as the value of the keys.
        - affectsTimeAll (ata): Specifies whether or not the sculpt tools affect the time as well as the value of the keys for all modes.
        - brushScaling (brs): Specifies how the sculpt brush scales relative to the Graph Editor. 1 = no scaling, 2 = scaling based on time, 3 = scaling based on value
        - falloffCurve (fc): Specifies the falloff curve of the sculpting effect.
        - falloffCurveAll (fca): Internal flag used to save/restore falloff curves for all modes.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - minRadius (mr): Specifies the minumum radius the sculpt brush will take due to stylus pressure. Cannot be more than the base brush radius.
        - minStrength (ms): Specifies the minumum strength of sculpting due to stylus pressure. Cannot be more than the base strength.
        - minStrengthAll (msa): Internal flag used to save/restore min strength for all modes.
        - mode (m): Specifies the base sculpt mode. 0 = grab, 1 = smooth 2 = smear 3 = reduce
        - radius (r): Specifies the radius of the sculpt brush.
        - reset (rs): Internal flag used to reset current tool mode settings.
        - strength (s): Specifies the strength of the sculpting effect for the current mode. Each mode can have a different strength.
        - strengthAll (sa): Internal flag used to save/restore strength for all modes.
        - query (q): Query mode flag
    """
@overload #Overload for sculptKeyCtx in ['query']
def sculptKeyCtx(contextName: contextName, activeMode: int = ..., am: int = ..., affectsTime: bool = ..., at: bool = ..., affectsTimeAll: str = ..., ata: str = ..., brushScaling: int = ..., brs: int = ..., falloffCurve: str = ..., fc: str = ..., falloffCurveAll: str = ..., fca: str = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., minRadius: float = ..., mr: float = ..., minStrength: float = ..., ms: float = ..., minStrengthAll: str = ..., msa: str = ..., mode: int = ..., m: int = ..., radius: float = ..., r: float = ..., reset: bool = ..., rs: bool = ..., strength: float = ..., s: float = ..., strengthAll: str = ..., sa: str = ..., query: bool = ..., q: bool = ...) -> str:
    """sculptKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with a
    sculpt brush. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a sculpt key context in grab mode.
        cmds.sculptKeyCtx('sculptKeyContext', mode=0)
        # Switch to smooth mode and set the sculpt radius to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, mode=1, radius=50)
        # Set the strength for the grab and smooth modes to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, modeStrength=((0,50),(1,50)))
        # Set the strength for all modes to 80.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, strengthAll=(80, 80, 80))
        // Activate affects time option
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, affectsTime=1)
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - activeMode (am): Used to query the current active sculpt mode. This can differ from the base mode if the user is holding down the shift hotkey to temporarily switch to smooth mode.
        - affectsTime (at): Specifies whether or not the sculpt tools affect the time as well as the value of the keys.
        - affectsTimeAll (ata): Specifies whether or not the sculpt tools affect the time as well as the value of the keys for all modes.
        - brushScaling (brs): Specifies how the sculpt brush scales relative to the Graph Editor. 1 = no scaling, 2 = scaling based on time, 3 = scaling based on value
        - falloffCurve (fc): Specifies the falloff curve of the sculpting effect.
        - falloffCurveAll (fca): Internal flag used to save/restore falloff curves for all modes.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - minRadius (mr): Specifies the minumum radius the sculpt brush will take due to stylus pressure. Cannot be more than the base brush radius.
        - minStrength (ms): Specifies the minumum strength of sculpting due to stylus pressure. Cannot be more than the base strength.
        - minStrengthAll (msa): Internal flag used to save/restore min strength for all modes.
        - mode (m): Specifies the base sculpt mode. 0 = grab, 1 = smooth 2 = smear 3 = reduce
        - radius (r): Specifies the radius of the sculpt brush.
        - reset (rs): Internal flag used to reset current tool mode settings.
        - strength (s): Specifies the strength of the sculpting effect for the current mode. Each mode can have a different strength.
        - strengthAll (sa): Internal flag used to save/restore strength for all modes.
        - query (q): Query mode flag
    """
@overload #Overload for sculptKeyCtx in ['edit']
def sculptKeyCtx(contextName: contextName, affectsTime: bool = ..., affectsTimeAll: str = ..., brushScaling: int = ..., editingRadius: bool = ..., editingStrength: bool = ..., falloffCurve: str = ..., falloffCurveAll: str = ..., image1: str = ..., image2: str = ..., image3: str = ..., minRadius: float = ..., minStrength: float = ..., minStrengthAll: str = ..., mode: int = ..., modeMinStrength: [int, float] = ..., modeStrength: [int, float] = ..., radius: float = ..., reset: bool = ..., strength: float = ..., strengthAll: str = ..., edit: bool = ...) -> str:
    """sculptKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with a
    sculpt brush. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a sculpt key context in grab mode.
        cmds.sculptKeyCtx('sculptKeyContext', mode=0)
        # Switch to smooth mode and set the sculpt radius to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, mode=1, radius=50)
        # Set the strength for the grab and smooth modes to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, modeStrength=((0,50),(1,50)))
        # Set the strength for all modes to 80.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, strengthAll=(80, 80, 80))
        // Activate affects time option
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, affectsTime=1)
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - affectsTime (at): Specifies whether or not the sculpt tools affect the time as well as the value of the keys.
        - affectsTimeAll (ata): Specifies whether or not the sculpt tools affect the time as well as the value of the keys for all modes.
        - brushScaling (brs): Specifies how the sculpt brush scales relative to the Graph Editor. 1 = no scaling, 2 = scaling based on time, 3 = scaling based on value
        - editingRadius (er): Enables or disables interactive radius scaling.
        - editingStrength (es): Enables or disables interactive strength scaling.
        - falloffCurve (fc): Specifies the falloff curve of the sculpting effect.
        - falloffCurveAll (fca): Internal flag used to save/restore falloff curves for all modes.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - minRadius (mr): Specifies the minumum radius the sculpt brush will take due to stylus pressure. Cannot be more than the base brush radius.
        - minStrength (ms): Specifies the minumum strength of sculpting due to stylus pressure. Cannot be more than the base strength.
        - minStrengthAll (msa): Internal flag used to save/restore min strength for all modes.
        - mode (m): Specifies the base sculpt mode. 0 = grab, 1 = smooth 2 = smear 3 = reduce
        - modeMinStrength (mms): Specifies the min strength for the specified mode.
        - modeStrength (mst): Specifies the strength for the specified mode.
        - radius (r): Specifies the radius of the sculpt brush.
        - reset (rs): Internal flag used to reset current tool mode settings.
        - strength (s): Specifies the strength of the sculpting effect for the current mode. Each mode can have a different strength.
        - strengthAll (sa): Internal flag used to save/restore strength for all modes.
        - edit (e): Edit mode flag
    """
@overload #Overload for sculptKeyCtx in ['edit']
def sculptKeyCtx(contextName: contextName, at: bool = ..., ata: str = ..., brs: int = ..., er: bool = ..., es: bool = ..., fc: str = ..., fca: str = ..., i1: str = ..., i2: str = ..., i3: str = ..., mr: float = ..., ms: float = ..., msa: str = ..., m: int = ..., mms: [int, float] = ..., mst: [int, float] = ..., r: float = ..., rs: bool = ..., s: float = ..., sa: str = ..., e: bool = ...) -> str:
    """sculptKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with a
    sculpt brush. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a sculpt key context in grab mode.
        cmds.sculptKeyCtx('sculptKeyContext', mode=0)
        # Switch to smooth mode and set the sculpt radius to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, mode=1, radius=50)
        # Set the strength for the grab and smooth modes to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, modeStrength=((0,50),(1,50)))
        # Set the strength for all modes to 80.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, strengthAll=(80, 80, 80))
        // Activate affects time option
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, affectsTime=1)
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - affectsTime (at): Specifies whether or not the sculpt tools affect the time as well as the value of the keys.
        - affectsTimeAll (ata): Specifies whether or not the sculpt tools affect the time as well as the value of the keys for all modes.
        - brushScaling (brs): Specifies how the sculpt brush scales relative to the Graph Editor. 1 = no scaling, 2 = scaling based on time, 3 = scaling based on value
        - editingRadius (er): Enables or disables interactive radius scaling.
        - editingStrength (es): Enables or disables interactive strength scaling.
        - falloffCurve (fc): Specifies the falloff curve of the sculpting effect.
        - falloffCurveAll (fca): Internal flag used to save/restore falloff curves for all modes.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - minRadius (mr): Specifies the minumum radius the sculpt brush will take due to stylus pressure. Cannot be more than the base brush radius.
        - minStrength (ms): Specifies the minumum strength of sculpting due to stylus pressure. Cannot be more than the base strength.
        - minStrengthAll (msa): Internal flag used to save/restore min strength for all modes.
        - mode (m): Specifies the base sculpt mode. 0 = grab, 1 = smooth 2 = smear 3 = reduce
        - modeMinStrength (mms): Specifies the min strength for the specified mode.
        - modeStrength (mst): Specifies the strength for the specified mode.
        - radius (r): Specifies the radius of the sculpt brush.
        - reset (rs): Internal flag used to reset current tool mode settings.
        - strength (s): Specifies the strength of the sculpting effect for the current mode. Each mode can have a different strength.
        - strengthAll (sa): Internal flag used to save/restore strength for all modes.
        - edit (e): Edit mode flag
    """
@overload #Overload for sculptKeyCtx in ['edit']
def sculptKeyCtx(contextName: contextName, affectsTime: bool = ..., at: bool = ..., affectsTimeAll: str = ..., ata: str = ..., brushScaling: int = ..., brs: int = ..., editingRadius: bool = ..., er: bool = ..., editingStrength: bool = ..., es: bool = ..., falloffCurve: str = ..., fc: str = ..., falloffCurveAll: str = ..., fca: str = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., minRadius: float = ..., mr: float = ..., minStrength: float = ..., ms: float = ..., minStrengthAll: str = ..., msa: str = ..., mode: int = ..., m: int = ..., modeMinStrength: [int, float] = ..., mms: [int, float] = ..., modeStrength: [int, float] = ..., mst: [int, float] = ..., radius: float = ..., r: float = ..., reset: bool = ..., rs: bool = ..., strength: float = ..., s: float = ..., strengthAll: str = ..., sa: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """sculptKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with a
    sculpt brush. This context only works in the graph editor.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a sculpt key context in grab mode.
        cmds.sculptKeyCtx('sculptKeyContext', mode=0)
        # Switch to smooth mode and set the sculpt radius to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, mode=1, radius=50)
        # Set the strength for the grab and smooth modes to 50.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, modeStrength=((0,50),(1,50)))
        # Set the strength for all modes to 80.
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, strengthAll=(80, 80, 80))
        // Activate affects time option
        cmds.sculptKeyCtx('sculptKeyContext', edit=True, affectsTime=1)
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - affectsTime (at): Specifies whether or not the sculpt tools affect the time as well as the value of the keys.
        - affectsTimeAll (ata): Specifies whether or not the sculpt tools affect the time as well as the value of the keys for all modes.
        - brushScaling (brs): Specifies how the sculpt brush scales relative to the Graph Editor. 1 = no scaling, 2 = scaling based on time, 3 = scaling based on value
        - editingRadius (er): Enables or disables interactive radius scaling.
        - editingStrength (es): Enables or disables interactive strength scaling.
        - falloffCurve (fc): Specifies the falloff curve of the sculpting effect.
        - falloffCurveAll (fca): Internal flag used to save/restore falloff curves for all modes.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - minRadius (mr): Specifies the minumum radius the sculpt brush will take due to stylus pressure. Cannot be more than the base brush radius.
        - minStrength (ms): Specifies the minumum strength of sculpting due to stylus pressure. Cannot be more than the base strength.
        - minStrengthAll (msa): Internal flag used to save/restore min strength for all modes.
        - mode (m): Specifies the base sculpt mode. 0 = grab, 1 = smooth 2 = smear 3 = reduce
        - modeMinStrength (mms): Specifies the min strength for the specified mode.
        - modeStrength (mst): Specifies the strength for the specified mode.
        - radius (r): Specifies the radius of the sculpt brush.
        - reset (rs): Internal flag used to reset current tool mode settings.
        - strength (s): Specifies the strength of the sculpting effect for the current mode. Each mode can have a different strength.
        - strengthAll (sa): Internal flag used to save/restore strength for all modes.
        - edit (e): Edit mode flag
    """
