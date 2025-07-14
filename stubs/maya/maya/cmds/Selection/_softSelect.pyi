"""Stub files for Selection category in Maya commands, command: softSelect."""

from typing import Any, overload

@overload #Overload for softSelect in ['create']
def softSelect(compressUndo: int = ..., enableFalseColor: int = ..., softSelectColorCurve: str = ..., softSelectCurve: str = ..., softSelectDistance: float = ..., softSelectEnabled: int = ..., softSelectFalloff: int = ..., softSelectReset: bool = ..., softSelectUVDistance: float = ...) -> None:
    """softSelect is undoable, queryable, and editable.
    
    This command allows you to change the soft modelling options.
    
    Soft modelling is an option that allows for reflection of basic manipulator
    actions such as move, rotate, and scale.

    ---
    - Args:
        - compressUndo (cu): Controls how soft selection settings behave in undo:0 means all changes undo individually1 means all consecutive changes undo as a group2 means only interactive changes undo as a groupWhen queried, returns an int indicating the current undo
            behaviour.
        - enableFalseColor (efc): Set soft select color feedback on or off. When queried, returns an int indicating whether color feedback is currently enabled.
        - softSelectColorCurve (scc): Sets the color ramp used to display false color feedback for soft selected components in the viewport. The color curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is
            represented by 5 successive values: 3 RGB values (the color to use), an input value (the selection weight), and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current color feedback curve.
        - softSelectCurve (ssc): Sets the falloff curve used to calculate selection weights for components within the falloff distance. The curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is represented by 3
            successive values: an output value (the selection weight at this point), an input value (the normalised falloff distance) and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current falloff
            curve.
        - softSelectDistance (ssd): Sets the falloff distance (radius) used for world and object space soft selection. When queried, returns a float indicating the current falloff distance.
        - softSelectEnabled (sse): Sets soft selection based modeling on or off. When queried, returns an int indicating the current state of the option.
        - softSelectFalloff (ssf): Sets the falloff mode:0 for volume based falloff1 for surface based falloff2 for global falloffWhen queried, returns an int indicating the falloff mode.
        - softSelectReset (ssr): Resets soft selection to its default settings.
        - softSelectUVDistance (sud): Sets the falloff distance (radius) used for UV space soft selection. When queried, returns a float indicating the current falloff distance.
    """
@overload #Overload for softSelect in ['create']
def softSelect(cu: int = ..., efc: int = ..., scc: str = ..., ssc: str = ..., ssd: float = ..., sse: int = ..., ssf: int = ..., ssr: bool = ..., sud: float = ...) -> None:
    """softSelect is undoable, queryable, and editable.
    
    This command allows you to change the soft modelling options.
    
    Soft modelling is an option that allows for reflection of basic manipulator
    actions such as move, rotate, and scale.

    ---
    - Args:
        - compressUndo (cu): Controls how soft selection settings behave in undo:0 means all changes undo individually1 means all consecutive changes undo as a group2 means only interactive changes undo as a groupWhen queried, returns an int indicating the current undo
            behaviour.
        - enableFalseColor (efc): Set soft select color feedback on or off. When queried, returns an int indicating whether color feedback is currently enabled.
        - softSelectColorCurve (scc): Sets the color ramp used to display false color feedback for soft selected components in the viewport. The color curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is
            represented by 5 successive values: 3 RGB values (the color to use), an input value (the selection weight), and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current color feedback curve.
        - softSelectCurve (ssc): Sets the falloff curve used to calculate selection weights for components within the falloff distance. The curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is represented by 3
            successive values: an output value (the selection weight at this point), an input value (the normalised falloff distance) and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current falloff
            curve.
        - softSelectDistance (ssd): Sets the falloff distance (radius) used for world and object space soft selection. When queried, returns a float indicating the current falloff distance.
        - softSelectEnabled (sse): Sets soft selection based modeling on or off. When queried, returns an int indicating the current state of the option.
        - softSelectFalloff (ssf): Sets the falloff mode:0 for volume based falloff1 for surface based falloff2 for global falloffWhen queried, returns an int indicating the falloff mode.
        - softSelectReset (ssr): Resets soft selection to its default settings.
        - softSelectUVDistance (sud): Sets the falloff distance (radius) used for UV space soft selection. When queried, returns a float indicating the current falloff distance.
    """
@overload #Overload for softSelect in ['create']
def softSelect(compressUndo: int = ..., cu: int = ..., enableFalseColor: int = ..., efc: int = ..., softSelectColorCurve: str = ..., scc: str = ..., softSelectCurve: str = ..., ssc: str = ..., softSelectDistance: float = ..., ssd: float = ..., softSelectEnabled: int = ..., sse: int = ..., softSelectFalloff: int = ..., ssf: int = ..., softSelectReset: bool = ..., ssr: bool = ..., softSelectUVDistance: float = ..., sud: float = ...) -> None:
    """softSelect is undoable, queryable, and editable.
    
    This command allows you to change the soft modelling options.
    
    Soft modelling is an option that allows for reflection of basic manipulator
    actions such as move, rotate, and scale.

    ---
    - Args:
        - compressUndo (cu): Controls how soft selection settings behave in undo:0 means all changes undo individually1 means all consecutive changes undo as a group2 means only interactive changes undo as a groupWhen queried, returns an int indicating the current undo
            behaviour.
        - enableFalseColor (efc): Set soft select color feedback on or off. When queried, returns an int indicating whether color feedback is currently enabled.
        - softSelectColorCurve (scc): Sets the color ramp used to display false color feedback for soft selected components in the viewport. The color curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is
            represented by 5 successive values: 3 RGB values (the color to use), an input value (the selection weight), and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current color feedback curve.
        - softSelectCurve (ssc): Sets the falloff curve used to calculate selection weights for components within the falloff distance. The curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is represented by 3
            successive values: an output value (the selection weight at this point), an input value (the normalised falloff distance) and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current falloff
            curve.
        - softSelectDistance (ssd): Sets the falloff distance (radius) used for world and object space soft selection. When queried, returns a float indicating the current falloff distance.
        - softSelectEnabled (sse): Sets soft selection based modeling on or off. When queried, returns an int indicating the current state of the option.
        - softSelectFalloff (ssf): Sets the falloff mode:0 for volume based falloff1 for surface based falloff2 for global falloffWhen queried, returns an int indicating the falloff mode.
        - softSelectReset (ssr): Resets soft selection to its default settings.
        - softSelectUVDistance (sud): Sets the falloff distance (radius) used for UV space soft selection. When queried, returns a float indicating the current falloff distance.
    """
@overload #Overload for softSelect in ['query']
def softSelect(compressUndo: int = ..., enableFalseColor: int = ..., softSelectColorCurve: str = ..., softSelectCurve: str = ..., softSelectDistance: float = ..., softSelectEnabled: int = ..., softSelectFalloff: int = ..., softSelectReset: bool = ..., softSelectUVDistance: float = ..., query: bool = ...) -> None:
    """softSelect is undoable, queryable, and editable.
    
    This command allows you to change the soft modelling options.
    
    Soft modelling is an option that allows for reflection of basic manipulator
    actions such as move, rotate, and scale.

    ---
    - Args:
        - compressUndo (cu): Controls how soft selection settings behave in undo:0 means all changes undo individually1 means all consecutive changes undo as a group2 means only interactive changes undo as a groupWhen queried, returns an int indicating the current undo
            behaviour.
        - enableFalseColor (efc): Set soft select color feedback on or off. When queried, returns an int indicating whether color feedback is currently enabled.
        - softSelectColorCurve (scc): Sets the color ramp used to display false color feedback for soft selected components in the viewport. The color curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is
            represented by 5 successive values: 3 RGB values (the color to use), an input value (the selection weight), and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current color feedback curve.
        - softSelectCurve (ssc): Sets the falloff curve used to calculate selection weights for components within the falloff distance. The curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is represented by 3
            successive values: an output value (the selection weight at this point), an input value (the normalised falloff distance) and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current falloff
            curve.
        - softSelectDistance (ssd): Sets the falloff distance (radius) used for world and object space soft selection. When queried, returns a float indicating the current falloff distance.
        - softSelectEnabled (sse): Sets soft selection based modeling on or off. When queried, returns an int indicating the current state of the option.
        - softSelectFalloff (ssf): Sets the falloff mode:0 for volume based falloff1 for surface based falloff2 for global falloffWhen queried, returns an int indicating the falloff mode.
        - softSelectReset (ssr): Resets soft selection to its default settings.
        - softSelectUVDistance (sud): Sets the falloff distance (radius) used for UV space soft selection. When queried, returns a float indicating the current falloff distance.
        - query (q): Query mode flag
    """
@overload #Overload for softSelect in ['query']
def softSelect(cu: int = ..., efc: int = ..., scc: str = ..., ssc: str = ..., ssd: float = ..., sse: int = ..., ssf: int = ..., ssr: bool = ..., sud: float = ..., q: bool = ...) -> None:
    """softSelect is undoable, queryable, and editable.
    
    This command allows you to change the soft modelling options.
    
    Soft modelling is an option that allows for reflection of basic manipulator
    actions such as move, rotate, and scale.

    ---
    - Args:
        - compressUndo (cu): Controls how soft selection settings behave in undo:0 means all changes undo individually1 means all consecutive changes undo as a group2 means only interactive changes undo as a groupWhen queried, returns an int indicating the current undo
            behaviour.
        - enableFalseColor (efc): Set soft select color feedback on or off. When queried, returns an int indicating whether color feedback is currently enabled.
        - softSelectColorCurve (scc): Sets the color ramp used to display false color feedback for soft selected components in the viewport. The color curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is
            represented by 5 successive values: 3 RGB values (the color to use), an input value (the selection weight), and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current color feedback curve.
        - softSelectCurve (ssc): Sets the falloff curve used to calculate selection weights for components within the falloff distance. The curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is represented by 3
            successive values: an output value (the selection weight at this point), an input value (the normalised falloff distance) and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current falloff
            curve.
        - softSelectDistance (ssd): Sets the falloff distance (radius) used for world and object space soft selection. When queried, returns a float indicating the current falloff distance.
        - softSelectEnabled (sse): Sets soft selection based modeling on or off. When queried, returns an int indicating the current state of the option.
        - softSelectFalloff (ssf): Sets the falloff mode:0 for volume based falloff1 for surface based falloff2 for global falloffWhen queried, returns an int indicating the falloff mode.
        - softSelectReset (ssr): Resets soft selection to its default settings.
        - softSelectUVDistance (sud): Sets the falloff distance (radius) used for UV space soft selection. When queried, returns a float indicating the current falloff distance.
        - query (q): Query mode flag
    """
@overload #Overload for softSelect in ['query']
def softSelect(compressUndo: int = ..., cu: int = ..., enableFalseColor: int = ..., efc: int = ..., softSelectColorCurve: str = ..., scc: str = ..., softSelectCurve: str = ..., ssc: str = ..., softSelectDistance: float = ..., ssd: float = ..., softSelectEnabled: int = ..., sse: int = ..., softSelectFalloff: int = ..., ssf: int = ..., softSelectReset: bool = ..., ssr: bool = ..., softSelectUVDistance: float = ..., sud: float = ..., query: bool = ..., q: bool = ...) -> None:
    """softSelect is undoable, queryable, and editable.
    
    This command allows you to change the soft modelling options.
    
    Soft modelling is an option that allows for reflection of basic manipulator
    actions such as move, rotate, and scale.

    ---
    - Args:
        - compressUndo (cu): Controls how soft selection settings behave in undo:0 means all changes undo individually1 means all consecutive changes undo as a group2 means only interactive changes undo as a groupWhen queried, returns an int indicating the current undo
            behaviour.
        - enableFalseColor (efc): Set soft select color feedback on or off. When queried, returns an int indicating whether color feedback is currently enabled.
        - softSelectColorCurve (scc): Sets the color ramp used to display false color feedback for soft selected components in the viewport. The color curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is
            represented by 5 successive values: 3 RGB values (the color to use), an input value (the selection weight), and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current color feedback curve.
        - softSelectCurve (ssc): Sets the falloff curve used to calculate selection weights for components within the falloff distance. The curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is represented by 3
            successive values: an output value (the selection weight at this point), an input value (the normalised falloff distance) and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current falloff
            curve.
        - softSelectDistance (ssd): Sets the falloff distance (radius) used for world and object space soft selection. When queried, returns a float indicating the current falloff distance.
        - softSelectEnabled (sse): Sets soft selection based modeling on or off. When queried, returns an int indicating the current state of the option.
        - softSelectFalloff (ssf): Sets the falloff mode:0 for volume based falloff1 for surface based falloff2 for global falloffWhen queried, returns an int indicating the falloff mode.
        - softSelectReset (ssr): Resets soft selection to its default settings.
        - softSelectUVDistance (sud): Sets the falloff distance (radius) used for UV space soft selection. When queried, returns a float indicating the current falloff distance.
        - query (q): Query mode flag
    """
@overload #Overload for softSelect in ['edit']
def softSelect(compressUndo: int = ..., enableFalseColor: int = ..., softSelectColorCurve: str = ..., softSelectCurve: str = ..., softSelectDistance: float = ..., softSelectEnabled: int = ..., softSelectFalloff: int = ..., softSelectReset: bool = ..., softSelectUVDistance: float = ..., edit: bool = ...) -> None:
    """softSelect is undoable, queryable, and editable.
    
    This command allows you to change the soft modelling options.
    
    Soft modelling is an option that allows for reflection of basic manipulator
    actions such as move, rotate, and scale.

    ---
    - Args:
        - compressUndo (cu): Controls how soft selection settings behave in undo:0 means all changes undo individually1 means all consecutive changes undo as a group2 means only interactive changes undo as a groupWhen queried, returns an int indicating the current undo
            behaviour.
        - enableFalseColor (efc): Set soft select color feedback on or off. When queried, returns an int indicating whether color feedback is currently enabled.
        - softSelectColorCurve (scc): Sets the color ramp used to display false color feedback for soft selected components in the viewport. The color curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is
            represented by 5 successive values: 3 RGB values (the color to use), an input value (the selection weight), and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current color feedback curve.
        - softSelectCurve (ssc): Sets the falloff curve used to calculate selection weights for components within the falloff distance. The curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is represented by 3
            successive values: an output value (the selection weight at this point), an input value (the normalised falloff distance) and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current falloff
            curve.
        - softSelectDistance (ssd): Sets the falloff distance (radius) used for world and object space soft selection. When queried, returns a float indicating the current falloff distance.
        - softSelectEnabled (sse): Sets soft selection based modeling on or off. When queried, returns an int indicating the current state of the option.
        - softSelectFalloff (ssf): Sets the falloff mode:0 for volume based falloff1 for surface based falloff2 for global falloffWhen queried, returns an int indicating the falloff mode.
        - softSelectReset (ssr): Resets soft selection to its default settings.
        - softSelectUVDistance (sud): Sets the falloff distance (radius) used for UV space soft selection. When queried, returns a float indicating the current falloff distance.
        - edit (e): Edit mode flag
    """
@overload #Overload for softSelect in ['edit']
def softSelect(cu: int = ..., efc: int = ..., scc: str = ..., ssc: str = ..., ssd: float = ..., sse: int = ..., ssf: int = ..., ssr: bool = ..., sud: float = ..., e: bool = ...) -> None:
    """softSelect is undoable, queryable, and editable.
    
    This command allows you to change the soft modelling options.
    
    Soft modelling is an option that allows for reflection of basic manipulator
    actions such as move, rotate, and scale.

    ---
    - Args:
        - compressUndo (cu): Controls how soft selection settings behave in undo:0 means all changes undo individually1 means all consecutive changes undo as a group2 means only interactive changes undo as a groupWhen queried, returns an int indicating the current undo
            behaviour.
        - enableFalseColor (efc): Set soft select color feedback on or off. When queried, returns an int indicating whether color feedback is currently enabled.
        - softSelectColorCurve (scc): Sets the color ramp used to display false color feedback for soft selected components in the viewport. The color curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is
            represented by 5 successive values: 3 RGB values (the color to use), an input value (the selection weight), and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current color feedback curve.
        - softSelectCurve (ssc): Sets the falloff curve used to calculate selection weights for components within the falloff distance. The curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is represented by 3
            successive values: an output value (the selection weight at this point), an input value (the normalised falloff distance) and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current falloff
            curve.
        - softSelectDistance (ssd): Sets the falloff distance (radius) used for world and object space soft selection. When queried, returns a float indicating the current falloff distance.
        - softSelectEnabled (sse): Sets soft selection based modeling on or off. When queried, returns an int indicating the current state of the option.
        - softSelectFalloff (ssf): Sets the falloff mode:0 for volume based falloff1 for surface based falloff2 for global falloffWhen queried, returns an int indicating the falloff mode.
        - softSelectReset (ssr): Resets soft selection to its default settings.
        - softSelectUVDistance (sud): Sets the falloff distance (radius) used for UV space soft selection. When queried, returns a float indicating the current falloff distance.
        - edit (e): Edit mode flag
    """
@overload #Overload for softSelect in ['edit']
def softSelect(compressUndo: int = ..., cu: int = ..., enableFalseColor: int = ..., efc: int = ..., softSelectColorCurve: str = ..., scc: str = ..., softSelectCurve: str = ..., ssc: str = ..., softSelectDistance: float = ..., ssd: float = ..., softSelectEnabled: int = ..., sse: int = ..., softSelectFalloff: int = ..., ssf: int = ..., softSelectReset: bool = ..., ssr: bool = ..., softSelectUVDistance: float = ..., sud: float = ..., edit: bool = ..., e: bool = ...) -> None:
    """softSelect is undoable, queryable, and editable.
    
    This command allows you to change the soft modelling options.
    
    Soft modelling is an option that allows for reflection of basic manipulator
    actions such as move, rotate, and scale.

    ---
    - Args:
        - compressUndo (cu): Controls how soft selection settings behave in undo:0 means all changes undo individually1 means all consecutive changes undo as a group2 means only interactive changes undo as a groupWhen queried, returns an int indicating the current undo
            behaviour.
        - enableFalseColor (efc): Set soft select color feedback on or off. When queried, returns an int indicating whether color feedback is currently enabled.
        - softSelectColorCurve (scc): Sets the color ramp used to display false color feedback for soft selected components in the viewport. The color curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is
            represented by 5 successive values: 3 RGB values (the color to use), an input value (the selection weight), and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current color feedback curve.
        - softSelectCurve (ssc): Sets the falloff curve used to calculate selection weights for components within the falloff distance. The curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is represented by 3
            successive values: an output value (the selection weight at this point), an input value (the normalised falloff distance) and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current falloff
            curve.
        - softSelectDistance (ssd): Sets the falloff distance (radius) used for world and object space soft selection. When queried, returns a float indicating the current falloff distance.
        - softSelectEnabled (sse): Sets soft selection based modeling on or off. When queried, returns an int indicating the current state of the option.
        - softSelectFalloff (ssf): Sets the falloff mode:0 for volume based falloff1 for surface based falloff2 for global falloffWhen queried, returns an int indicating the falloff mode.
        - softSelectReset (ssr): Resets soft selection to its default settings.
        - softSelectUVDistance (sud): Sets the falloff distance (radius) used for UV space soft selection. When queried, returns a float indicating the current falloff distance.
        - edit (e): Edit mode flag
    """
