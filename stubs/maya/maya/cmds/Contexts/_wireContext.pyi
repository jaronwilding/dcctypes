"""Stub files for Contexts category in Maya commands, command: wireContext."""

from typing import Any, overload

@overload #Overload for wireContext in ['create']
def wireContext(string: str, crossingEffect: linear = ..., deformationOrder: str = ..., dropoffDistance: linear = ..., envelope: linear = ..., exclusive: bool = ..., exclusivePartition: str = ..., exists: bool = ..., groupWithBase: bool = ..., history: bool = ..., holder: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., localInfluence: linear = ..., name: str = ...) -> str:
    """wireContext is undoable, queryable, and editable.
    
    This command creates a tool that can be used to create a wire deformer.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wireContext( 'wireCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - crossingEffect (ce): Set the amount of convolution filter effect. Varies from fully convolved at 0 to a simple additive effect at 1. Default is 0.
        - deformationOrder (do): Set the appropriate flag that determines the position in in the deformation hierarchy.
        - dropoffDistance (dds): Set the dropoff Distance for the wires.
        - envelope (en): Set the envelope value for the deformer. Default is 1.0
        - exclusive (exc): Set exclusive mode on or off.
        - exclusivePartition (ep): Set the name of an exclusive partition.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - groupWithBase (gw): Groups the wire with the base wire so that they can easily be moved together to create a ripple effect. Default is false.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - holder (ho): Controls whether the user can specify holders for the wires from the wire context. A holder is a curve that you can use to limit the wire's deformation region. Default is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localInfluence (li): Set the amount of local influence a wire has with respect to other wires. Default is 0.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for wireContext in ['create']
def wireContext(string: str, ce: linear = ..., do: str = ..., dds: linear = ..., en: linear = ..., exc: bool = ..., ep: str = ..., ex: bool = ..., gw: bool = ..., ch: bool = ..., ho: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., li: linear = ..., n: str = ...) -> str:
    """wireContext is undoable, queryable, and editable.
    
    This command creates a tool that can be used to create a wire deformer.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wireContext( 'wireCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - crossingEffect (ce): Set the amount of convolution filter effect. Varies from fully convolved at 0 to a simple additive effect at 1. Default is 0.
        - deformationOrder (do): Set the appropriate flag that determines the position in in the deformation hierarchy.
        - dropoffDistance (dds): Set the dropoff Distance for the wires.
        - envelope (en): Set the envelope value for the deformer. Default is 1.0
        - exclusive (exc): Set exclusive mode on or off.
        - exclusivePartition (ep): Set the name of an exclusive partition.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - groupWithBase (gw): Groups the wire with the base wire so that they can easily be moved together to create a ripple effect. Default is false.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - holder (ho): Controls whether the user can specify holders for the wires from the wire context. A holder is a curve that you can use to limit the wire's deformation region. Default is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localInfluence (li): Set the amount of local influence a wire has with respect to other wires. Default is 0.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for wireContext in ['create']
def wireContext(string: str, crossingEffect: linear = ..., ce: linear = ..., deformationOrder: str = ..., do: str = ..., dropoffDistance: linear = ..., dds: linear = ..., envelope: linear = ..., en: linear = ..., exclusive: bool = ..., exc: bool = ..., exclusivePartition: str = ..., ep: str = ..., exists: bool = ..., ex: bool = ..., groupWithBase: bool = ..., gw: bool = ..., history: bool = ..., ch: bool = ..., holder: bool = ..., ho: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., localInfluence: linear = ..., li: linear = ..., name: str = ..., n: str = ...) -> str:
    """wireContext is undoable, queryable, and editable.
    
    This command creates a tool that can be used to create a wire deformer.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wireContext( 'wireCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - crossingEffect (ce): Set the amount of convolution filter effect. Varies from fully convolved at 0 to a simple additive effect at 1. Default is 0.
        - deformationOrder (do): Set the appropriate flag that determines the position in in the deformation hierarchy.
        - dropoffDistance (dds): Set the dropoff Distance for the wires.
        - envelope (en): Set the envelope value for the deformer. Default is 1.0
        - exclusive (exc): Set exclusive mode on or off.
        - exclusivePartition (ep): Set the name of an exclusive partition.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - groupWithBase (gw): Groups the wire with the base wire so that they can easily be moved together to create a ripple effect. Default is false.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - holder (ho): Controls whether the user can specify holders for the wires from the wire context. A holder is a curve that you can use to limit the wire's deformation region. Default is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localInfluence (li): Set the amount of local influence a wire has with respect to other wires. Default is 0.
        - name (n): If this is a tool command, name the tool appropriately.
    """
@overload #Overload for wireContext in ['query']
def wireContext(string: str, crossingEffect: linear = ..., deformationOrder: str = ..., dropoffDistance: linear = ..., envelope: linear = ..., exclusive: bool = ..., exclusivePartition: str = ..., groupWithBase: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., localInfluence: linear = ..., query: bool = ...) -> str:
    """wireContext is undoable, queryable, and editable.
    
    This command creates a tool that can be used to create a wire deformer.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wireContext( 'wireCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - crossingEffect (ce): Set the amount of convolution filter effect. Varies from fully convolved at 0 to a simple additive effect at 1. Default is 0.
        - deformationOrder (do): Set the appropriate flag that determines the position in in the deformation hierarchy.
        - dropoffDistance (dds): Set the dropoff Distance for the wires.
        - envelope (en): Set the envelope value for the deformer. Default is 1.0
        - exclusive (exc): Set exclusive mode on or off.
        - exclusivePartition (ep): Set the name of an exclusive partition.
        - groupWithBase (gw): Groups the wire with the base wire so that they can easily be moved together to create a ripple effect. Default is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localInfluence (li): Set the amount of local influence a wire has with respect to other wires. Default is 0.
        - query (q): Query mode flag
    """
@overload #Overload for wireContext in ['query']
def wireContext(string: str, ce: linear = ..., do: str = ..., dds: linear = ..., en: linear = ..., exc: bool = ..., ep: str = ..., gw: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., li: linear = ..., q: bool = ...) -> str:
    """wireContext is undoable, queryable, and editable.
    
    This command creates a tool that can be used to create a wire deformer.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wireContext( 'wireCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - crossingEffect (ce): Set the amount of convolution filter effect. Varies from fully convolved at 0 to a simple additive effect at 1. Default is 0.
        - deformationOrder (do): Set the appropriate flag that determines the position in in the deformation hierarchy.
        - dropoffDistance (dds): Set the dropoff Distance for the wires.
        - envelope (en): Set the envelope value for the deformer. Default is 1.0
        - exclusive (exc): Set exclusive mode on or off.
        - exclusivePartition (ep): Set the name of an exclusive partition.
        - groupWithBase (gw): Groups the wire with the base wire so that they can easily be moved together to create a ripple effect. Default is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localInfluence (li): Set the amount of local influence a wire has with respect to other wires. Default is 0.
        - query (q): Query mode flag
    """
@overload #Overload for wireContext in ['query']
def wireContext(string: str, crossingEffect: linear = ..., ce: linear = ..., deformationOrder: str = ..., do: str = ..., dropoffDistance: linear = ..., dds: linear = ..., envelope: linear = ..., en: linear = ..., exclusive: bool = ..., exc: bool = ..., exclusivePartition: str = ..., ep: str = ..., groupWithBase: bool = ..., gw: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., localInfluence: linear = ..., li: linear = ..., query: bool = ..., q: bool = ...) -> str:
    """wireContext is undoable, queryable, and editable.
    
    This command creates a tool that can be used to create a wire deformer.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wireContext( 'wireCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - crossingEffect (ce): Set the amount of convolution filter effect. Varies from fully convolved at 0 to a simple additive effect at 1. Default is 0.
        - deformationOrder (do): Set the appropriate flag that determines the position in in the deformation hierarchy.
        - dropoffDistance (dds): Set the dropoff Distance for the wires.
        - envelope (en): Set the envelope value for the deformer. Default is 1.0
        - exclusive (exc): Set exclusive mode on or off.
        - exclusivePartition (ep): Set the name of an exclusive partition.
        - groupWithBase (gw): Groups the wire with the base wire so that they can easily be moved together to create a ripple effect. Default is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localInfluence (li): Set the amount of local influence a wire has with respect to other wires. Default is 0.
        - query (q): Query mode flag
    """
@overload #Overload for wireContext in ['edit']
def wireContext(string: str, crossingEffect: linear = ..., deformationOrder: str = ..., dropoffDistance: linear = ..., envelope: linear = ..., exclusive: bool = ..., exclusivePartition: str = ..., groupWithBase: bool = ..., holder: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., localInfluence: linear = ..., edit: bool = ...) -> str:
    """wireContext is undoable, queryable, and editable.
    
    This command creates a tool that can be used to create a wire deformer.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wireContext( 'wireCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - crossingEffect (ce): Set the amount of convolution filter effect. Varies from fully convolved at 0 to a simple additive effect at 1. Default is 0.
        - deformationOrder (do): Set the appropriate flag that determines the position in in the deformation hierarchy.
        - dropoffDistance (dds): Set the dropoff Distance for the wires.
        - envelope (en): Set the envelope value for the deformer. Default is 1.0
        - exclusive (exc): Set exclusive mode on or off.
        - exclusivePartition (ep): Set the name of an exclusive partition.
        - groupWithBase (gw): Groups the wire with the base wire so that they can easily be moved together to create a ripple effect. Default is false.
        - holder (ho): Controls whether the user can specify holders for the wires from the wire context. A holder is a curve that you can use to limit the wire's deformation region. Default is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localInfluence (li): Set the amount of local influence a wire has with respect to other wires. Default is 0.
        - edit (e): Edit mode flag
    """
@overload #Overload for wireContext in ['edit']
def wireContext(string: str, ce: linear = ..., do: str = ..., dds: linear = ..., en: linear = ..., exc: bool = ..., ep: str = ..., gw: bool = ..., ho: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., li: linear = ..., e: bool = ...) -> str:
    """wireContext is undoable, queryable, and editable.
    
    This command creates a tool that can be used to create a wire deformer.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wireContext( 'wireCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - crossingEffect (ce): Set the amount of convolution filter effect. Varies from fully convolved at 0 to a simple additive effect at 1. Default is 0.
        - deformationOrder (do): Set the appropriate flag that determines the position in in the deformation hierarchy.
        - dropoffDistance (dds): Set the dropoff Distance for the wires.
        - envelope (en): Set the envelope value for the deformer. Default is 1.0
        - exclusive (exc): Set exclusive mode on or off.
        - exclusivePartition (ep): Set the name of an exclusive partition.
        - groupWithBase (gw): Groups the wire with the base wire so that they can easily be moved together to create a ripple effect. Default is false.
        - holder (ho): Controls whether the user can specify holders for the wires from the wire context. A holder is a curve that you can use to limit the wire's deformation region. Default is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localInfluence (li): Set the amount of local influence a wire has with respect to other wires. Default is 0.
        - edit (e): Edit mode flag
    """
@overload #Overload for wireContext in ['edit']
def wireContext(string: str, crossingEffect: linear = ..., ce: linear = ..., deformationOrder: str = ..., do: str = ..., dropoffDistance: linear = ..., dds: linear = ..., envelope: linear = ..., en: linear = ..., exclusive: bool = ..., exc: bool = ..., exclusivePartition: str = ..., ep: str = ..., groupWithBase: bool = ..., gw: bool = ..., holder: bool = ..., ho: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., localInfluence: linear = ..., li: linear = ..., edit: bool = ..., e: bool = ...) -> str:
    """wireContext is undoable, queryable, and editable.
    
    This command creates a tool that can be used to create a wire deformer.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.wireContext( 'wireCtx' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - crossingEffect (ce): Set the amount of convolution filter effect. Varies from fully convolved at 0 to a simple additive effect at 1. Default is 0.
        - deformationOrder (do): Set the appropriate flag that determines the position in in the deformation hierarchy.
        - dropoffDistance (dds): Set the dropoff Distance for the wires.
        - envelope (en): Set the envelope value for the deformer. Default is 1.0
        - exclusive (exc): Set exclusive mode on or off.
        - exclusivePartition (ep): Set the name of an exclusive partition.
        - groupWithBase (gw): Groups the wire with the base wire so that they can easily be moved together to create a ripple effect. Default is false.
        - holder (ho): Controls whether the user can specify holders for the wires from the wire context. A holder is a curve that you can use to limit the wire's deformation region. Default is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - localInfluence (li): Set the amount of local influence a wire has with respect to other wires. Default is 0.
        - edit (e): Edit mode flag
    """
