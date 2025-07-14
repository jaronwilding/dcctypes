"""Stub files for Contexts category in Maya commands, command: dynParticleCtx."""

from typing import Any, overload

@overload #Overload for dynParticleCtx in ['create']
def dynParticleCtx(string: str, conserve: float = ..., cursorPlacement: bool = ..., exists: bool = ..., grid: bool = ..., gridSpacing: float = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., jitterRadius: float = ..., lowerLeftX: float = ..., lowerLeftY: float = ..., lowerLeftZ: float = ..., name: str = ..., nucleus: bool = ..., numJitters: int = ..., particleName: str = ..., sketch: bool = ..., sketchInterval: int = ..., textPlacement: bool = ..., upperRightX: float = ..., upperRightY: float = ..., upperZ: float = ...) -> None:
    """dynParticleCtx is undoable, queryable, and editable.
    
    The particle context command creates a particle context. The particle context
    provides an interactive means to create particle objects. The particle context
    command also provides an interactive means to set the option values, through
    the Tool Property Sheet, for the "particle" command that the context will
    issue.

    ---
    - Args:
        - string: Input item(s).
        - conserve (c): Conservation of momentum control (between 0 and 1). For smaller values, the field will tend to erase any existing velocity the object has (in other words, will not conserve momentum from frame to frame). A value of 1 (the default)
            corresponds to the true physical law of conservation of momentum.
        - cursorPlacement (cp): Use the cursor to place the lower left and upper right of the grid.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - grid (gr): Create a particle grid.
        - gridSpacing (grs): Spacing between particles in the grid.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jitterRadius (jr): Max radius from the center to place the particle instances.
        - lowerLeftX (llx): Lower left X position of the particle grid.
        - lowerLeftY (lly): Lower left Y position of the particle grid.
        - lowerLeftZ (llz): Lower left Z position of the particle grid.
        - name (n): If this is a tool command, name the tool appropriately.
        - nucleus (nc): If set true then an nParticle is generated with a nucleus node connection. Otherwise a standard particle is created.
        - numJitters (nj): Number of jitters (instances) per particle.
        - particleName (pn): Particle name.
        - sketch (sk): Create particles in sketch mode.
        - sketchInterval (ski): Interval between particles, when in sketch mode.
        - textPlacement (tp): Use the textfields to specify the lower left and upper right of/ the grid.
        - upperRightX (urx): Upper right X position of the particle grid.
        - upperRightY (ury): Upper right Y position of the particle grid.
        - upperZ (urz): Upper right Z position of the particle grid.
    """
@overload #Overload for dynParticleCtx in ['create']
def dynParticleCtx(string: str, c: float = ..., cp: bool = ..., ex: bool = ..., gr: bool = ..., grs: float = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., jr: float = ..., llx: float = ..., lly: float = ..., llz: float = ..., n: str = ..., nc: bool = ..., nj: int = ..., pn: str = ..., sk: bool = ..., ski: int = ..., tp: bool = ..., urx: float = ..., ury: float = ..., urz: float = ...) -> None:
    """dynParticleCtx is undoable, queryable, and editable.
    
    The particle context command creates a particle context. The particle context
    provides an interactive means to create particle objects. The particle context
    command also provides an interactive means to set the option values, through
    the Tool Property Sheet, for the "particle" command that the context will
    issue.

    ---
    - Args:
        - string: Input item(s).
        - conserve (c): Conservation of momentum control (between 0 and 1). For smaller values, the field will tend to erase any existing velocity the object has (in other words, will not conserve momentum from frame to frame). A value of 1 (the default)
            corresponds to the true physical law of conservation of momentum.
        - cursorPlacement (cp): Use the cursor to place the lower left and upper right of the grid.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - grid (gr): Create a particle grid.
        - gridSpacing (grs): Spacing between particles in the grid.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jitterRadius (jr): Max radius from the center to place the particle instances.
        - lowerLeftX (llx): Lower left X position of the particle grid.
        - lowerLeftY (lly): Lower left Y position of the particle grid.
        - lowerLeftZ (llz): Lower left Z position of the particle grid.
        - name (n): If this is a tool command, name the tool appropriately.
        - nucleus (nc): If set true then an nParticle is generated with a nucleus node connection. Otherwise a standard particle is created.
        - numJitters (nj): Number of jitters (instances) per particle.
        - particleName (pn): Particle name.
        - sketch (sk): Create particles in sketch mode.
        - sketchInterval (ski): Interval between particles, when in sketch mode.
        - textPlacement (tp): Use the textfields to specify the lower left and upper right of/ the grid.
        - upperRightX (urx): Upper right X position of the particle grid.
        - upperRightY (ury): Upper right Y position of the particle grid.
        - upperZ (urz): Upper right Z position of the particle grid.
    """
@overload #Overload for dynParticleCtx in ['create']
def dynParticleCtx(string: str, conserve: float = ..., c: float = ..., cursorPlacement: bool = ..., cp: bool = ..., exists: bool = ..., ex: bool = ..., grid: bool = ..., gr: bool = ..., gridSpacing: float = ..., grs: float = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., jitterRadius: float = ..., jr: float = ..., lowerLeftX: float = ..., llx: float = ..., lowerLeftY: float = ..., lly: float = ..., lowerLeftZ: float = ..., llz: float = ..., name: str = ..., n: str = ..., nucleus: bool = ..., nc: bool = ..., numJitters: int = ..., nj: int = ..., particleName: str = ..., pn: str = ..., sketch: bool = ..., sk: bool = ..., sketchInterval: int = ..., ski: int = ..., textPlacement: bool = ..., tp: bool = ..., upperRightX: float = ..., urx: float = ..., upperRightY: float = ..., ury: float = ..., upperZ: float = ..., urz: float = ...) -> None:
    """dynParticleCtx is undoable, queryable, and editable.
    
    The particle context command creates a particle context. The particle context
    provides an interactive means to create particle objects. The particle context
    command also provides an interactive means to set the option values, through
    the Tool Property Sheet, for the "particle" command that the context will
    issue.

    ---
    - Args:
        - string: Input item(s).
        - conserve (c): Conservation of momentum control (between 0 and 1). For smaller values, the field will tend to erase any existing velocity the object has (in other words, will not conserve momentum from frame to frame). A value of 1 (the default)
            corresponds to the true physical law of conservation of momentum.
        - cursorPlacement (cp): Use the cursor to place the lower left and upper right of the grid.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - grid (gr): Create a particle grid.
        - gridSpacing (grs): Spacing between particles in the grid.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jitterRadius (jr): Max radius from the center to place the particle instances.
        - lowerLeftX (llx): Lower left X position of the particle grid.
        - lowerLeftY (lly): Lower left Y position of the particle grid.
        - lowerLeftZ (llz): Lower left Z position of the particle grid.
        - name (n): If this is a tool command, name the tool appropriately.
        - nucleus (nc): If set true then an nParticle is generated with a nucleus node connection. Otherwise a standard particle is created.
        - numJitters (nj): Number of jitters (instances) per particle.
        - particleName (pn): Particle name.
        - sketch (sk): Create particles in sketch mode.
        - sketchInterval (ski): Interval between particles, when in sketch mode.
        - textPlacement (tp): Use the textfields to specify the lower left and upper right of/ the grid.
        - upperRightX (urx): Upper right X position of the particle grid.
        - upperRightY (ury): Upper right Y position of the particle grid.
        - upperZ (urz): Upper right Z position of the particle grid.
    """
@overload #Overload for dynParticleCtx in ['query']
def dynParticleCtx(string: str, conserve: float = ..., cursorPlacement: bool = ..., grid: bool = ..., gridSpacing: float = ..., image1: str = ..., image2: str = ..., image3: str = ..., jitterRadius: float = ..., lowerLeftX: float = ..., lowerLeftY: float = ..., lowerLeftZ: float = ..., nucleus: bool = ..., numJitters: int = ..., particleName: str = ..., sketch: bool = ..., sketchInterval: int = ..., textPlacement: bool = ..., upperRightX: float = ..., upperRightY: float = ..., upperZ: float = ..., query: bool = ...) -> None:
    """dynParticleCtx is undoable, queryable, and editable.
    
    The particle context command creates a particle context. The particle context
    provides an interactive means to create particle objects. The particle context
    command also provides an interactive means to set the option values, through
    the Tool Property Sheet, for the "particle" command that the context will
    issue.

    ---
    - Args:
        - string: Input item(s).
        - conserve (c): Conservation of momentum control (between 0 and 1). For smaller values, the field will tend to erase any existing velocity the object has (in other words, will not conserve momentum from frame to frame). A value of 1 (the default)
            corresponds to the true physical law of conservation of momentum.
        - cursorPlacement (cp): Use the cursor to place the lower left and upper right of the grid.
        - grid (gr): Create a particle grid.
        - gridSpacing (grs): Spacing between particles in the grid.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jitterRadius (jr): Max radius from the center to place the particle instances.
        - lowerLeftX (llx): Lower left X position of the particle grid.
        - lowerLeftY (lly): Lower left Y position of the particle grid.
        - lowerLeftZ (llz): Lower left Z position of the particle grid.
        - nucleus (nc): If set true then an nParticle is generated with a nucleus node connection. Otherwise a standard particle is created.
        - numJitters (nj): Number of jitters (instances) per particle.
        - particleName (pn): Particle name.
        - sketch (sk): Create particles in sketch mode.
        - sketchInterval (ski): Interval between particles, when in sketch mode.
        - textPlacement (tp): Use the textfields to specify the lower left and upper right of/ the grid.
        - upperRightX (urx): Upper right X position of the particle grid.
        - upperRightY (ury): Upper right Y position of the particle grid.
        - upperZ (urz): Upper right Z position of the particle grid.
        - query (q): Query mode flag
    """
@overload #Overload for dynParticleCtx in ['query']
def dynParticleCtx(string: str, c: float = ..., cp: bool = ..., gr: bool = ..., grs: float = ..., i1: str = ..., i2: str = ..., i3: str = ..., jr: float = ..., llx: float = ..., lly: float = ..., llz: float = ..., nc: bool = ..., nj: int = ..., pn: str = ..., sk: bool = ..., ski: int = ..., tp: bool = ..., urx: float = ..., ury: float = ..., urz: float = ..., q: bool = ...) -> None:
    """dynParticleCtx is undoable, queryable, and editable.
    
    The particle context command creates a particle context. The particle context
    provides an interactive means to create particle objects. The particle context
    command also provides an interactive means to set the option values, through
    the Tool Property Sheet, for the "particle" command that the context will
    issue.

    ---
    - Args:
        - string: Input item(s).
        - conserve (c): Conservation of momentum control (between 0 and 1). For smaller values, the field will tend to erase any existing velocity the object has (in other words, will not conserve momentum from frame to frame). A value of 1 (the default)
            corresponds to the true physical law of conservation of momentum.
        - cursorPlacement (cp): Use the cursor to place the lower left and upper right of the grid.
        - grid (gr): Create a particle grid.
        - gridSpacing (grs): Spacing between particles in the grid.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jitterRadius (jr): Max radius from the center to place the particle instances.
        - lowerLeftX (llx): Lower left X position of the particle grid.
        - lowerLeftY (lly): Lower left Y position of the particle grid.
        - lowerLeftZ (llz): Lower left Z position of the particle grid.
        - nucleus (nc): If set true then an nParticle is generated with a nucleus node connection. Otherwise a standard particle is created.
        - numJitters (nj): Number of jitters (instances) per particle.
        - particleName (pn): Particle name.
        - sketch (sk): Create particles in sketch mode.
        - sketchInterval (ski): Interval between particles, when in sketch mode.
        - textPlacement (tp): Use the textfields to specify the lower left and upper right of/ the grid.
        - upperRightX (urx): Upper right X position of the particle grid.
        - upperRightY (ury): Upper right Y position of the particle grid.
        - upperZ (urz): Upper right Z position of the particle grid.
        - query (q): Query mode flag
    """
@overload #Overload for dynParticleCtx in ['query']
def dynParticleCtx(string: str, conserve: float = ..., c: float = ..., cursorPlacement: bool = ..., cp: bool = ..., grid: bool = ..., gr: bool = ..., gridSpacing: float = ..., grs: float = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., jitterRadius: float = ..., jr: float = ..., lowerLeftX: float = ..., llx: float = ..., lowerLeftY: float = ..., lly: float = ..., lowerLeftZ: float = ..., llz: float = ..., nucleus: bool = ..., nc: bool = ..., numJitters: int = ..., nj: int = ..., particleName: str = ..., pn: str = ..., sketch: bool = ..., sk: bool = ..., sketchInterval: int = ..., ski: int = ..., textPlacement: bool = ..., tp: bool = ..., upperRightX: float = ..., urx: float = ..., upperRightY: float = ..., ury: float = ..., upperZ: float = ..., urz: float = ..., query: bool = ..., q: bool = ...) -> None:
    """dynParticleCtx is undoable, queryable, and editable.
    
    The particle context command creates a particle context. The particle context
    provides an interactive means to create particle objects. The particle context
    command also provides an interactive means to set the option values, through
    the Tool Property Sheet, for the "particle" command that the context will
    issue.

    ---
    - Args:
        - string: Input item(s).
        - conserve (c): Conservation of momentum control (between 0 and 1). For smaller values, the field will tend to erase any existing velocity the object has (in other words, will not conserve momentum from frame to frame). A value of 1 (the default)
            corresponds to the true physical law of conservation of momentum.
        - cursorPlacement (cp): Use the cursor to place the lower left and upper right of the grid.
        - grid (gr): Create a particle grid.
        - gridSpacing (grs): Spacing between particles in the grid.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jitterRadius (jr): Max radius from the center to place the particle instances.
        - lowerLeftX (llx): Lower left X position of the particle grid.
        - lowerLeftY (lly): Lower left Y position of the particle grid.
        - lowerLeftZ (llz): Lower left Z position of the particle grid.
        - nucleus (nc): If set true then an nParticle is generated with a nucleus node connection. Otherwise a standard particle is created.
        - numJitters (nj): Number of jitters (instances) per particle.
        - particleName (pn): Particle name.
        - sketch (sk): Create particles in sketch mode.
        - sketchInterval (ski): Interval between particles, when in sketch mode.
        - textPlacement (tp): Use the textfields to specify the lower left and upper right of/ the grid.
        - upperRightX (urx): Upper right X position of the particle grid.
        - upperRightY (ury): Upper right Y position of the particle grid.
        - upperZ (urz): Upper right Z position of the particle grid.
        - query (q): Query mode flag
    """
@overload #Overload for dynParticleCtx in ['edit']
def dynParticleCtx(string: str, conserve: float = ..., cursorPlacement: bool = ..., grid: bool = ..., gridSpacing: float = ..., image1: str = ..., image2: str = ..., image3: str = ..., jitterRadius: float = ..., lowerLeftX: float = ..., lowerLeftY: float = ..., lowerLeftZ: float = ..., nucleus: bool = ..., numJitters: int = ..., particleName: str = ..., sketch: bool = ..., sketchInterval: int = ..., textPlacement: bool = ..., upperRightX: float = ..., upperRightY: float = ..., upperZ: float = ..., edit: bool = ...) -> None:
    """dynParticleCtx is undoable, queryable, and editable.
    
    The particle context command creates a particle context. The particle context
    provides an interactive means to create particle objects. The particle context
    command also provides an interactive means to set the option values, through
    the Tool Property Sheet, for the "particle" command that the context will
    issue.

    ---
    - Args:
        - string: Input item(s).
        - conserve (c): Conservation of momentum control (between 0 and 1). For smaller values, the field will tend to erase any existing velocity the object has (in other words, will not conserve momentum from frame to frame). A value of 1 (the default)
            corresponds to the true physical law of conservation of momentum.
        - cursorPlacement (cp): Use the cursor to place the lower left and upper right of the grid.
        - grid (gr): Create a particle grid.
        - gridSpacing (grs): Spacing between particles in the grid.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jitterRadius (jr): Max radius from the center to place the particle instances.
        - lowerLeftX (llx): Lower left X position of the particle grid.
        - lowerLeftY (lly): Lower left Y position of the particle grid.
        - lowerLeftZ (llz): Lower left Z position of the particle grid.
        - nucleus (nc): If set true then an nParticle is generated with a nucleus node connection. Otherwise a standard particle is created.
        - numJitters (nj): Number of jitters (instances) per particle.
        - particleName (pn): Particle name.
        - sketch (sk): Create particles in sketch mode.
        - sketchInterval (ski): Interval between particles, when in sketch mode.
        - textPlacement (tp): Use the textfields to specify the lower left and upper right of/ the grid.
        - upperRightX (urx): Upper right X position of the particle grid.
        - upperRightY (ury): Upper right Y position of the particle grid.
        - upperZ (urz): Upper right Z position of the particle grid.
        - edit (e): Edit mode flag
    """
@overload #Overload for dynParticleCtx in ['edit']
def dynParticleCtx(string: str, c: float = ..., cp: bool = ..., gr: bool = ..., grs: float = ..., i1: str = ..., i2: str = ..., i3: str = ..., jr: float = ..., llx: float = ..., lly: float = ..., llz: float = ..., nc: bool = ..., nj: int = ..., pn: str = ..., sk: bool = ..., ski: int = ..., tp: bool = ..., urx: float = ..., ury: float = ..., urz: float = ..., e: bool = ...) -> None:
    """dynParticleCtx is undoable, queryable, and editable.
    
    The particle context command creates a particle context. The particle context
    provides an interactive means to create particle objects. The particle context
    command also provides an interactive means to set the option values, through
    the Tool Property Sheet, for the "particle" command that the context will
    issue.

    ---
    - Args:
        - string: Input item(s).
        - conserve (c): Conservation of momentum control (between 0 and 1). For smaller values, the field will tend to erase any existing velocity the object has (in other words, will not conserve momentum from frame to frame). A value of 1 (the default)
            corresponds to the true physical law of conservation of momentum.
        - cursorPlacement (cp): Use the cursor to place the lower left and upper right of the grid.
        - grid (gr): Create a particle grid.
        - gridSpacing (grs): Spacing between particles in the grid.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jitterRadius (jr): Max radius from the center to place the particle instances.
        - lowerLeftX (llx): Lower left X position of the particle grid.
        - lowerLeftY (lly): Lower left Y position of the particle grid.
        - lowerLeftZ (llz): Lower left Z position of the particle grid.
        - nucleus (nc): If set true then an nParticle is generated with a nucleus node connection. Otherwise a standard particle is created.
        - numJitters (nj): Number of jitters (instances) per particle.
        - particleName (pn): Particle name.
        - sketch (sk): Create particles in sketch mode.
        - sketchInterval (ski): Interval between particles, when in sketch mode.
        - textPlacement (tp): Use the textfields to specify the lower left and upper right of/ the grid.
        - upperRightX (urx): Upper right X position of the particle grid.
        - upperRightY (ury): Upper right Y position of the particle grid.
        - upperZ (urz): Upper right Z position of the particle grid.
        - edit (e): Edit mode flag
    """
@overload #Overload for dynParticleCtx in ['edit']
def dynParticleCtx(string: str, conserve: float = ..., c: float = ..., cursorPlacement: bool = ..., cp: bool = ..., grid: bool = ..., gr: bool = ..., gridSpacing: float = ..., grs: float = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., jitterRadius: float = ..., jr: float = ..., lowerLeftX: float = ..., llx: float = ..., lowerLeftY: float = ..., lly: float = ..., lowerLeftZ: float = ..., llz: float = ..., nucleus: bool = ..., nc: bool = ..., numJitters: int = ..., nj: int = ..., particleName: str = ..., pn: str = ..., sketch: bool = ..., sk: bool = ..., sketchInterval: int = ..., ski: int = ..., textPlacement: bool = ..., tp: bool = ..., upperRightX: float = ..., urx: float = ..., upperRightY: float = ..., ury: float = ..., upperZ: float = ..., urz: float = ..., edit: bool = ..., e: bool = ...) -> None:
    """dynParticleCtx is undoable, queryable, and editable.
    
    The particle context command creates a particle context. The particle context
    provides an interactive means to create particle objects. The particle context
    command also provides an interactive means to set the option values, through
    the Tool Property Sheet, for the "particle" command that the context will
    issue.

    ---
    - Args:
        - string: Input item(s).
        - conserve (c): Conservation of momentum control (between 0 and 1). For smaller values, the field will tend to erase any existing velocity the object has (in other words, will not conserve momentum from frame to frame). A value of 1 (the default)
            corresponds to the true physical law of conservation of momentum.
        - cursorPlacement (cp): Use the cursor to place the lower left and upper right of the grid.
        - grid (gr): Create a particle grid.
        - gridSpacing (grs): Spacing between particles in the grid.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jitterRadius (jr): Max radius from the center to place the particle instances.
        - lowerLeftX (llx): Lower left X position of the particle grid.
        - lowerLeftY (lly): Lower left Y position of the particle grid.
        - lowerLeftZ (llz): Lower left Z position of the particle grid.
        - nucleus (nc): If set true then an nParticle is generated with a nucleus node connection. Otherwise a standard particle is created.
        - numJitters (nj): Number of jitters (instances) per particle.
        - particleName (pn): Particle name.
        - sketch (sk): Create particles in sketch mode.
        - sketchInterval (ski): Interval between particles, when in sketch mode.
        - textPlacement (tp): Use the textfields to specify the lower left and upper right of/ the grid.
        - upperRightX (urx): Upper right X position of the particle grid.
        - upperRightY (ury): Upper right Y position of the particle grid.
        - upperZ (urz): Upper right Z position of the particle grid.
        - edit (e): Edit mode flag
    """
