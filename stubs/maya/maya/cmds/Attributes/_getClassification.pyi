"""Stub files for Attributes category in Maya commands, command: getClassification."""

from typing import Any, overload

@overload #Overload for getClassification in ['create']
def getClassification(string: str, satisfies: str = ...) -> list[str]:
    """getClassification is undoable, NOT queryable, and NOT editable.
    
    Returns the classification string for a given node type.
    
    Classification strings look like file pathnames ("shader/reflective" or
    "texture/2D", for example). Multiple classifications can be combined into a
    single compound classification string by joining the individual
    classifications with ':'. For example, the classification string
    "shader/reflective:texture/2D" means that the node is both a reflective shader
    and a 2D texture.
    
    The classification string is used to determine how rendering nodes are
    categorized in various UI, such as the Create Render Node and HyperShade
    windows:
    
    Category| Classification String
    ---|---
    2D Textures| "texture/2d"
    3D Textures| "texture/3d"
    Env Textures| "texture/environment"
    Surface Materials| "shader/surface"
    Volumetric Materials| "shader/volume"
    Displacement Materials| "shader/displacement"
    Lights| "light"
    General Utilities| "utility/general"
    Math Utilities| "math"
    Color Utilities| "utility/color
    Particle Utilities| "utility/particle"
    Image Planes| "imageplane"
    Glow| "postprocess/opticalFX"
    
    The classification string is also used to determine how Viewport 2.0 will
    interpret the node.
    
    Category| Classification String
    ---|---
    Geometry| "drawdb/geometry"
    Transform| "drawdb/geometry/transform"
    Sub-Scene Object| "drawdb/subscene"
    Shader| "drawdb/shader"
    Surface Shader| "drawdb/shader/surface"

    ---
    - Args:
        - string: Input item(s).
        - satisfies (sat): Returns true if the given node type's classification satisfies the classification string which is passed with the flag.A non-compound classification string A is said to satisfy a non-compound classification string B if A is a
            subclassification of B (for example, "shaders/reflective" satisfies "shaders").A compound classification string A satisfies a compound classification string B iff:every component of A satisfies at least one component of B andevery component
            of B is satisfied by at least one component of AHence, "shader/reflective/phong:texture" satisfies "shader:texture", but "shader/reflective/phong" does not satisfy "shader:texture".
    """
@overload #Overload for getClassification in ['create']
def getClassification(string: str, sat: str = ...) -> list[str]:
    """getClassification is undoable, NOT queryable, and NOT editable.
    
    Returns the classification string for a given node type.
    
    Classification strings look like file pathnames ("shader/reflective" or
    "texture/2D", for example). Multiple classifications can be combined into a
    single compound classification string by joining the individual
    classifications with ':'. For example, the classification string
    "shader/reflective:texture/2D" means that the node is both a reflective shader
    and a 2D texture.
    
    The classification string is used to determine how rendering nodes are
    categorized in various UI, such as the Create Render Node and HyperShade
    windows:
    
    Category| Classification String
    ---|---
    2D Textures| "texture/2d"
    3D Textures| "texture/3d"
    Env Textures| "texture/environment"
    Surface Materials| "shader/surface"
    Volumetric Materials| "shader/volume"
    Displacement Materials| "shader/displacement"
    Lights| "light"
    General Utilities| "utility/general"
    Math Utilities| "math"
    Color Utilities| "utility/color
    Particle Utilities| "utility/particle"
    Image Planes| "imageplane"
    Glow| "postprocess/opticalFX"
    
    The classification string is also used to determine how Viewport 2.0 will
    interpret the node.
    
    Category| Classification String
    ---|---
    Geometry| "drawdb/geometry"
    Transform| "drawdb/geometry/transform"
    Sub-Scene Object| "drawdb/subscene"
    Shader| "drawdb/shader"
    Surface Shader| "drawdb/shader/surface"

    ---
    - Args:
        - string: Input item(s).
        - satisfies (sat): Returns true if the given node type's classification satisfies the classification string which is passed with the flag.A non-compound classification string A is said to satisfy a non-compound classification string B if A is a
            subclassification of B (for example, "shaders/reflective" satisfies "shaders").A compound classification string A satisfies a compound classification string B iff:every component of A satisfies at least one component of B andevery component
            of B is satisfied by at least one component of AHence, "shader/reflective/phong:texture" satisfies "shader:texture", but "shader/reflective/phong" does not satisfy "shader:texture".
    """
@overload #Overload for getClassification in ['create']
def getClassification(string: str, satisfies: str = ..., sat: str = ...) -> list[str]:
    """getClassification is undoable, NOT queryable, and NOT editable.
    
    Returns the classification string for a given node type.
    
    Classification strings look like file pathnames ("shader/reflective" or
    "texture/2D", for example). Multiple classifications can be combined into a
    single compound classification string by joining the individual
    classifications with ':'. For example, the classification string
    "shader/reflective:texture/2D" means that the node is both a reflective shader
    and a 2D texture.
    
    The classification string is used to determine how rendering nodes are
    categorized in various UI, such as the Create Render Node and HyperShade
    windows:
    
    Category| Classification String
    ---|---
    2D Textures| "texture/2d"
    3D Textures| "texture/3d"
    Env Textures| "texture/environment"
    Surface Materials| "shader/surface"
    Volumetric Materials| "shader/volume"
    Displacement Materials| "shader/displacement"
    Lights| "light"
    General Utilities| "utility/general"
    Math Utilities| "math"
    Color Utilities| "utility/color
    Particle Utilities| "utility/particle"
    Image Planes| "imageplane"
    Glow| "postprocess/opticalFX"
    
    The classification string is also used to determine how Viewport 2.0 will
    interpret the node.
    
    Category| Classification String
    ---|---
    Geometry| "drawdb/geometry"
    Transform| "drawdb/geometry/transform"
    Sub-Scene Object| "drawdb/subscene"
    Shader| "drawdb/shader"
    Surface Shader| "drawdb/shader/surface"

    ---
    - Args:
        - string: Input item(s).
        - satisfies (sat): Returns true if the given node type's classification satisfies the classification string which is passed with the flag.A non-compound classification string A is said to satisfy a non-compound classification string B if A is a
            subclassification of B (for example, "shaders/reflective" satisfies "shaders").A compound classification string A satisfies a compound classification string B iff:every component of A satisfies at least one component of B andevery component
            of B is satisfied by at least one component of AHence, "shader/reflective/phong:texture" satisfies "shader:texture", but "shader/reflective/phong" does not satisfy "shader:texture".
    """
