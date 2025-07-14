"""Stub files for Selection category in Maya commands, command: symmetricModelling."""

from typing import Any, overload

@overload #Overload for symmetricModelling in ['create']
def symmetricModelling(about: str = ..., allowPartial: bool = ..., axis: str = ..., preserveSeam: int = ..., reset: bool = ..., seamFalloffCurve: str = ..., seamTolerance: float = ..., symmetry: int = ..., tolerance: float = ..., topoSymmetry: bool = ...) -> None:
    """symmetricModelling is undoable, queryable, and editable.
    
    This command allows you to change the symmetric modelling options.
    
    Symmetric modelling is an option that allows for reflection of basic
    manipulator actions such as move, rotate, and scale.

    ---
    - Args:
        - about (a): Set the space in which symmetry should be calculated (object or world or topo). When queried, returns a string which is the current space being used.
        - allowPartial (ap): Specifies whether partial symmetry should be allowed when enabling topological symmetry.
        - axis (ax): Set the current axis to be reflected over. When queried, returns a string which is the current axis.
        - preserveSeam (ps): Controls whether selection or symmetry should take priority on the plane of symmetry. When queried, returns an int for the option.
        - reset (r): Reset the redo information before starting.
        - seamFalloffCurve (sf): Set the seam's falloff curve, used to control the seam strength within the seam tolerance. The string is a comma separated list of sets of 3 values for each curve point. When queried, returns a string which is the current space being used.
        - seamTolerance (st): Set the seam tolerance used for reflection. When preserveSeam is enabled, this tolerance controls the width of the enforced seam. When queried, returns a float of the seamTolerance.
        - symmetry (s): Set the symmetry option on or off. When queried, returns an int for the option.
        - tolerance (t): Set the tolerance of reflection. When queried, returns a float of the tolerance.
        - topoSymmetry (ts): Enable/disable topological symmetry. When enabled, the supplied component/active list will be used to define the topological symmetry seam. When queried, returns the name of the active topological symmetry object.
    """
@overload #Overload for symmetricModelling in ['create']
def symmetricModelling(a: str = ..., ap: bool = ..., ax: str = ..., ps: int = ..., r: bool = ..., sf: str = ..., st: float = ..., s: int = ..., t: float = ..., ts: bool = ...) -> None:
    """symmetricModelling is undoable, queryable, and editable.
    
    This command allows you to change the symmetric modelling options.
    
    Symmetric modelling is an option that allows for reflection of basic
    manipulator actions such as move, rotate, and scale.

    ---
    - Args:
        - about (a): Set the space in which symmetry should be calculated (object or world or topo). When queried, returns a string which is the current space being used.
        - allowPartial (ap): Specifies whether partial symmetry should be allowed when enabling topological symmetry.
        - axis (ax): Set the current axis to be reflected over. When queried, returns a string which is the current axis.
        - preserveSeam (ps): Controls whether selection or symmetry should take priority on the plane of symmetry. When queried, returns an int for the option.
        - reset (r): Reset the redo information before starting.
        - seamFalloffCurve (sf): Set the seam's falloff curve, used to control the seam strength within the seam tolerance. The string is a comma separated list of sets of 3 values for each curve point. When queried, returns a string which is the current space being used.
        - seamTolerance (st): Set the seam tolerance used for reflection. When preserveSeam is enabled, this tolerance controls the width of the enforced seam. When queried, returns a float of the seamTolerance.
        - symmetry (s): Set the symmetry option on or off. When queried, returns an int for the option.
        - tolerance (t): Set the tolerance of reflection. When queried, returns a float of the tolerance.
        - topoSymmetry (ts): Enable/disable topological symmetry. When enabled, the supplied component/active list will be used to define the topological symmetry seam. When queried, returns the name of the active topological symmetry object.
    """
@overload #Overload for symmetricModelling in ['create']
def symmetricModelling(about: str = ..., a: str = ..., allowPartial: bool = ..., ap: bool = ..., axis: str = ..., ax: str = ..., preserveSeam: int = ..., ps: int = ..., reset: bool = ..., r: bool = ..., seamFalloffCurve: str = ..., sf: str = ..., seamTolerance: float = ..., st: float = ..., symmetry: int = ..., s: int = ..., tolerance: float = ..., t: float = ..., topoSymmetry: bool = ..., ts: bool = ...) -> None:
    """symmetricModelling is undoable, queryable, and editable.
    
    This command allows you to change the symmetric modelling options.
    
    Symmetric modelling is an option that allows for reflection of basic
    manipulator actions such as move, rotate, and scale.

    ---
    - Args:
        - about (a): Set the space in which symmetry should be calculated (object or world or topo). When queried, returns a string which is the current space being used.
        - allowPartial (ap): Specifies whether partial symmetry should be allowed when enabling topological symmetry.
        - axis (ax): Set the current axis to be reflected over. When queried, returns a string which is the current axis.
        - preserveSeam (ps): Controls whether selection or symmetry should take priority on the plane of symmetry. When queried, returns an int for the option.
        - reset (r): Reset the redo information before starting.
        - seamFalloffCurve (sf): Set the seam's falloff curve, used to control the seam strength within the seam tolerance. The string is a comma separated list of sets of 3 values for each curve point. When queried, returns a string which is the current space being used.
        - seamTolerance (st): Set the seam tolerance used for reflection. When preserveSeam is enabled, this tolerance controls the width of the enforced seam. When queried, returns a float of the seamTolerance.
        - symmetry (s): Set the symmetry option on or off. When queried, returns an int for the option.
        - tolerance (t): Set the tolerance of reflection. When queried, returns a float of the tolerance.
        - topoSymmetry (ts): Enable/disable topological symmetry. When enabled, the supplied component/active list will be used to define the topological symmetry seam. When queried, returns the name of the active topological symmetry object.
    """
@overload #Overload for symmetricModelling in ['query']
def symmetricModelling(about: str = ..., allowPartial: bool = ..., axis: str = ..., preserveSeam: int = ..., reset: bool = ..., seamFalloffCurve: str = ..., seamTolerance: float = ..., symmetry: int = ..., tolerance: float = ..., topoSymmetry: bool = ..., query: bool = ...) -> None:
    """symmetricModelling is undoable, queryable, and editable.
    
    This command allows you to change the symmetric modelling options.
    
    Symmetric modelling is an option that allows for reflection of basic
    manipulator actions such as move, rotate, and scale.

    ---
    - Args:
        - about (a): Set the space in which symmetry should be calculated (object or world or topo). When queried, returns a string which is the current space being used.
        - allowPartial (ap): Specifies whether partial symmetry should be allowed when enabling topological symmetry.
        - axis (ax): Set the current axis to be reflected over. When queried, returns a string which is the current axis.
        - preserveSeam (ps): Controls whether selection or symmetry should take priority on the plane of symmetry. When queried, returns an int for the option.
        - reset (r): Reset the redo information before starting.
        - seamFalloffCurve (sf): Set the seam's falloff curve, used to control the seam strength within the seam tolerance. The string is a comma separated list of sets of 3 values for each curve point. When queried, returns a string which is the current space being used.
        - seamTolerance (st): Set the seam tolerance used for reflection. When preserveSeam is enabled, this tolerance controls the width of the enforced seam. When queried, returns a float of the seamTolerance.
        - symmetry (s): Set the symmetry option on or off. When queried, returns an int for the option.
        - tolerance (t): Set the tolerance of reflection. When queried, returns a float of the tolerance.
        - topoSymmetry (ts): Enable/disable topological symmetry. When enabled, the supplied component/active list will be used to define the topological symmetry seam. When queried, returns the name of the active topological symmetry object.
        - query (q): Query mode flag
    """
@overload #Overload for symmetricModelling in ['query']
def symmetricModelling(a: str = ..., ap: bool = ..., ax: str = ..., ps: int = ..., r: bool = ..., sf: str = ..., st: float = ..., s: int = ..., t: float = ..., ts: bool = ..., q: bool = ...) -> None:
    """symmetricModelling is undoable, queryable, and editable.
    
    This command allows you to change the symmetric modelling options.
    
    Symmetric modelling is an option that allows for reflection of basic
    manipulator actions such as move, rotate, and scale.

    ---
    - Args:
        - about (a): Set the space in which symmetry should be calculated (object or world or topo). When queried, returns a string which is the current space being used.
        - allowPartial (ap): Specifies whether partial symmetry should be allowed when enabling topological symmetry.
        - axis (ax): Set the current axis to be reflected over. When queried, returns a string which is the current axis.
        - preserveSeam (ps): Controls whether selection or symmetry should take priority on the plane of symmetry. When queried, returns an int for the option.
        - reset (r): Reset the redo information before starting.
        - seamFalloffCurve (sf): Set the seam's falloff curve, used to control the seam strength within the seam tolerance. The string is a comma separated list of sets of 3 values for each curve point. When queried, returns a string which is the current space being used.
        - seamTolerance (st): Set the seam tolerance used for reflection. When preserveSeam is enabled, this tolerance controls the width of the enforced seam. When queried, returns a float of the seamTolerance.
        - symmetry (s): Set the symmetry option on or off. When queried, returns an int for the option.
        - tolerance (t): Set the tolerance of reflection. When queried, returns a float of the tolerance.
        - topoSymmetry (ts): Enable/disable topological symmetry. When enabled, the supplied component/active list will be used to define the topological symmetry seam. When queried, returns the name of the active topological symmetry object.
        - query (q): Query mode flag
    """
@overload #Overload for symmetricModelling in ['query']
def symmetricModelling(about: str = ..., a: str = ..., allowPartial: bool = ..., ap: bool = ..., axis: str = ..., ax: str = ..., preserveSeam: int = ..., ps: int = ..., reset: bool = ..., r: bool = ..., seamFalloffCurve: str = ..., sf: str = ..., seamTolerance: float = ..., st: float = ..., symmetry: int = ..., s: int = ..., tolerance: float = ..., t: float = ..., topoSymmetry: bool = ..., ts: bool = ..., query: bool = ..., q: bool = ...) -> None:
    """symmetricModelling is undoable, queryable, and editable.
    
    This command allows you to change the symmetric modelling options.
    
    Symmetric modelling is an option that allows for reflection of basic
    manipulator actions such as move, rotate, and scale.

    ---
    - Args:
        - about (a): Set the space in which symmetry should be calculated (object or world or topo). When queried, returns a string which is the current space being used.
        - allowPartial (ap): Specifies whether partial symmetry should be allowed when enabling topological symmetry.
        - axis (ax): Set the current axis to be reflected over. When queried, returns a string which is the current axis.
        - preserveSeam (ps): Controls whether selection or symmetry should take priority on the plane of symmetry. When queried, returns an int for the option.
        - reset (r): Reset the redo information before starting.
        - seamFalloffCurve (sf): Set the seam's falloff curve, used to control the seam strength within the seam tolerance. The string is a comma separated list of sets of 3 values for each curve point. When queried, returns a string which is the current space being used.
        - seamTolerance (st): Set the seam tolerance used for reflection. When preserveSeam is enabled, this tolerance controls the width of the enforced seam. When queried, returns a float of the seamTolerance.
        - symmetry (s): Set the symmetry option on or off. When queried, returns an int for the option.
        - tolerance (t): Set the tolerance of reflection. When queried, returns a float of the tolerance.
        - topoSymmetry (ts): Enable/disable topological symmetry. When enabled, the supplied component/active list will be used to define the topological symmetry seam. When queried, returns the name of the active topological symmetry object.
        - query (q): Query mode flag
    """
@overload #Overload for symmetricModelling in ['edit']
def symmetricModelling(about: str = ..., allowPartial: bool = ..., axis: str = ..., preserveSeam: int = ..., reset: bool = ..., seamFalloffCurve: str = ..., seamTolerance: float = ..., symmetry: int = ..., tolerance: float = ..., topoSymmetry: bool = ..., edit: bool = ...) -> None:
    """symmetricModelling is undoable, queryable, and editable.
    
    This command allows you to change the symmetric modelling options.
    
    Symmetric modelling is an option that allows for reflection of basic
    manipulator actions such as move, rotate, and scale.

    ---
    - Args:
        - about (a): Set the space in which symmetry should be calculated (object or world or topo). When queried, returns a string which is the current space being used.
        - allowPartial (ap): Specifies whether partial symmetry should be allowed when enabling topological symmetry.
        - axis (ax): Set the current axis to be reflected over. When queried, returns a string which is the current axis.
        - preserveSeam (ps): Controls whether selection or symmetry should take priority on the plane of symmetry. When queried, returns an int for the option.
        - reset (r): Reset the redo information before starting.
        - seamFalloffCurve (sf): Set the seam's falloff curve, used to control the seam strength within the seam tolerance. The string is a comma separated list of sets of 3 values for each curve point. When queried, returns a string which is the current space being used.
        - seamTolerance (st): Set the seam tolerance used for reflection. When preserveSeam is enabled, this tolerance controls the width of the enforced seam. When queried, returns a float of the seamTolerance.
        - symmetry (s): Set the symmetry option on or off. When queried, returns an int for the option.
        - tolerance (t): Set the tolerance of reflection. When queried, returns a float of the tolerance.
        - topoSymmetry (ts): Enable/disable topological symmetry. When enabled, the supplied component/active list will be used to define the topological symmetry seam. When queried, returns the name of the active topological symmetry object.
        - edit (e): Edit mode flag
    """
@overload #Overload for symmetricModelling in ['edit']
def symmetricModelling(a: str = ..., ap: bool = ..., ax: str = ..., ps: int = ..., r: bool = ..., sf: str = ..., st: float = ..., s: int = ..., t: float = ..., ts: bool = ..., e: bool = ...) -> None:
    """symmetricModelling is undoable, queryable, and editable.
    
    This command allows you to change the symmetric modelling options.
    
    Symmetric modelling is an option that allows for reflection of basic
    manipulator actions such as move, rotate, and scale.

    ---
    - Args:
        - about (a): Set the space in which symmetry should be calculated (object or world or topo). When queried, returns a string which is the current space being used.
        - allowPartial (ap): Specifies whether partial symmetry should be allowed when enabling topological symmetry.
        - axis (ax): Set the current axis to be reflected over. When queried, returns a string which is the current axis.
        - preserveSeam (ps): Controls whether selection or symmetry should take priority on the plane of symmetry. When queried, returns an int for the option.
        - reset (r): Reset the redo information before starting.
        - seamFalloffCurve (sf): Set the seam's falloff curve, used to control the seam strength within the seam tolerance. The string is a comma separated list of sets of 3 values for each curve point. When queried, returns a string which is the current space being used.
        - seamTolerance (st): Set the seam tolerance used for reflection. When preserveSeam is enabled, this tolerance controls the width of the enforced seam. When queried, returns a float of the seamTolerance.
        - symmetry (s): Set the symmetry option on or off. When queried, returns an int for the option.
        - tolerance (t): Set the tolerance of reflection. When queried, returns a float of the tolerance.
        - topoSymmetry (ts): Enable/disable topological symmetry. When enabled, the supplied component/active list will be used to define the topological symmetry seam. When queried, returns the name of the active topological symmetry object.
        - edit (e): Edit mode flag
    """
@overload #Overload for symmetricModelling in ['edit']
def symmetricModelling(about: str = ..., a: str = ..., allowPartial: bool = ..., ap: bool = ..., axis: str = ..., ax: str = ..., preserveSeam: int = ..., ps: int = ..., reset: bool = ..., r: bool = ..., seamFalloffCurve: str = ..., sf: str = ..., seamTolerance: float = ..., st: float = ..., symmetry: int = ..., s: int = ..., tolerance: float = ..., t: float = ..., topoSymmetry: bool = ..., ts: bool = ..., edit: bool = ..., e: bool = ...) -> None:
    """symmetricModelling is undoable, queryable, and editable.
    
    This command allows you to change the symmetric modelling options.
    
    Symmetric modelling is an option that allows for reflection of basic
    manipulator actions such as move, rotate, and scale.

    ---
    - Args:
        - about (a): Set the space in which symmetry should be calculated (object or world or topo). When queried, returns a string which is the current space being used.
        - allowPartial (ap): Specifies whether partial symmetry should be allowed when enabling topological symmetry.
        - axis (ax): Set the current axis to be reflected over. When queried, returns a string which is the current axis.
        - preserveSeam (ps): Controls whether selection or symmetry should take priority on the plane of symmetry. When queried, returns an int for the option.
        - reset (r): Reset the redo information before starting.
        - seamFalloffCurve (sf): Set the seam's falloff curve, used to control the seam strength within the seam tolerance. The string is a comma separated list of sets of 3 values for each curve point. When queried, returns a string which is the current space being used.
        - seamTolerance (st): Set the seam tolerance used for reflection. When preserveSeam is enabled, this tolerance controls the width of the enforced seam. When queried, returns a float of the seamTolerance.
        - symmetry (s): Set the symmetry option on or off. When queried, returns an int for the option.
        - tolerance (t): Set the tolerance of reflection. When queried, returns a float of the tolerance.
        - topoSymmetry (ts): Enable/disable topological symmetry. When enabled, the supplied component/active list will be used to define the topological symmetry seam. When queried, returns the name of the active topological symmetry object.
        - edit (e): Edit mode flag
    """
