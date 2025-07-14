"""Stub files for General category in Maya commands, command: bakePartialHistory."""

from typing import Any, overload

@overload #Overload for bakePartialHistory in ['create']
def bakePartialHistory(allShapes: bool = ..., postSmooth: bool = ..., preCache: bool = ..., preDeformers: bool = ..., prePostDeformers: bool = ...) -> str:
    """bakePartialHistory is undoable, queryable, and editable.
    
    This command is used to bake sections of the construction history of a shape
    node when possible. A typical usage would be on a shape that has both
    modelling operations and deformers in its history. Using this command with the
    -prePostDeformers flag will bake the modeling portions of the graph, so that
    only the deformers remain.
    
    Note that not all modeling operations can be baked such that they create
    exactly the same effect after baking. For example, imagine the history
    contains a skinning operation followed by a smooth. Before baking, the smooth
    operation is performed each time the skin deforms, so it will smooth
    differently depending on the output of the skin. When the smooth operation is
    baked into the skinning, the skin will be reweighted based on the smooth
    points to attempt to approximate the original behavior. However, the skin node
    does not perform the smooth operation, it merely performs skinning with the
    newly calculated weights and the result will not be identical to before the
    bake.
    
    In general, modeling operations that occur before deformers can be baked
    precisely. Those which occur after can only be approximated. The -pre and
    -post flags allow you to control whether only the operations before or after
    the deformers are baked.
    
    When the command is used on an object with no deformers, the entire history
    will be deleted.

    ---
    - Args:
        - allShapes (all): Specifies that the bake operation should be performed on all shapes in the entire scene. By default, only selected objects are baked. If this option is specified and there are no shapes in the scene, then this command will do nothing and
            end successfully.
        - postSmooth (nps): Specifies whether or not a smoothing operation should be done on skin vertices. This smoothing is only done on vertices that are found to deviate largely from other vertex values.  The default is false.
        - preCache (pc): Specifies baking of any history operations that occur before the caching operation, including deformers. In query mode, returns a list of the nodes that will be baked.
        - preDeformers (pre): Specifies baking of any modeling operations in the history that occur before the deformers. In query mode, returns a list of the nodes that will be baked.
        - prePostDeformers (ppt): Specifies baking of all modeling operations in the history whether they are before or after the deformers in the history. If neither the -prePostDeformers nor the -preDeformers flag is specified, prePostDeformers will be used as the
            default. In query mode, returns a list of the nodes that will be baked.
    """
@overload #Overload for bakePartialHistory in ['create']
def bakePartialHistory(all: bool = ..., nps: bool = ..., pc: bool = ..., pre: bool = ..., ppt: bool = ...) -> str:
    """bakePartialHistory is undoable, queryable, and editable.
    
    This command is used to bake sections of the construction history of a shape
    node when possible. A typical usage would be on a shape that has both
    modelling operations and deformers in its history. Using this command with the
    -prePostDeformers flag will bake the modeling portions of the graph, so that
    only the deformers remain.
    
    Note that not all modeling operations can be baked such that they create
    exactly the same effect after baking. For example, imagine the history
    contains a skinning operation followed by a smooth. Before baking, the smooth
    operation is performed each time the skin deforms, so it will smooth
    differently depending on the output of the skin. When the smooth operation is
    baked into the skinning, the skin will be reweighted based on the smooth
    points to attempt to approximate the original behavior. However, the skin node
    does not perform the smooth operation, it merely performs skinning with the
    newly calculated weights and the result will not be identical to before the
    bake.
    
    In general, modeling operations that occur before deformers can be baked
    precisely. Those which occur after can only be approximated. The -pre and
    -post flags allow you to control whether only the operations before or after
    the deformers are baked.
    
    When the command is used on an object with no deformers, the entire history
    will be deleted.

    ---
    - Args:
        - allShapes (all): Specifies that the bake operation should be performed on all shapes in the entire scene. By default, only selected objects are baked. If this option is specified and there are no shapes in the scene, then this command will do nothing and
            end successfully.
        - postSmooth (nps): Specifies whether or not a smoothing operation should be done on skin vertices. This smoothing is only done on vertices that are found to deviate largely from other vertex values.  The default is false.
        - preCache (pc): Specifies baking of any history operations that occur before the caching operation, including deformers. In query mode, returns a list of the nodes that will be baked.
        - preDeformers (pre): Specifies baking of any modeling operations in the history that occur before the deformers. In query mode, returns a list of the nodes that will be baked.
        - prePostDeformers (ppt): Specifies baking of all modeling operations in the history whether they are before or after the deformers in the history. If neither the -prePostDeformers nor the -preDeformers flag is specified, prePostDeformers will be used as the
            default. In query mode, returns a list of the nodes that will be baked.
    """
@overload #Overload for bakePartialHistory in ['create']
def bakePartialHistory(allShapes: bool = ..., all: bool = ..., postSmooth: bool = ..., nps: bool = ..., preCache: bool = ..., pc: bool = ..., preDeformers: bool = ..., pre: bool = ..., prePostDeformers: bool = ..., ppt: bool = ...) -> str:
    """bakePartialHistory is undoable, queryable, and editable.
    
    This command is used to bake sections of the construction history of a shape
    node when possible. A typical usage would be on a shape that has both
    modelling operations and deformers in its history. Using this command with the
    -prePostDeformers flag will bake the modeling portions of the graph, so that
    only the deformers remain.
    
    Note that not all modeling operations can be baked such that they create
    exactly the same effect after baking. For example, imagine the history
    contains a skinning operation followed by a smooth. Before baking, the smooth
    operation is performed each time the skin deforms, so it will smooth
    differently depending on the output of the skin. When the smooth operation is
    baked into the skinning, the skin will be reweighted based on the smooth
    points to attempt to approximate the original behavior. However, the skin node
    does not perform the smooth operation, it merely performs skinning with the
    newly calculated weights and the result will not be identical to before the
    bake.
    
    In general, modeling operations that occur before deformers can be baked
    precisely. Those which occur after can only be approximated. The -pre and
    -post flags allow you to control whether only the operations before or after
    the deformers are baked.
    
    When the command is used on an object with no deformers, the entire history
    will be deleted.

    ---
    - Args:
        - allShapes (all): Specifies that the bake operation should be performed on all shapes in the entire scene. By default, only selected objects are baked. If this option is specified and there are no shapes in the scene, then this command will do nothing and
            end successfully.
        - postSmooth (nps): Specifies whether or not a smoothing operation should be done on skin vertices. This smoothing is only done on vertices that are found to deviate largely from other vertex values.  The default is false.
        - preCache (pc): Specifies baking of any history operations that occur before the caching operation, including deformers. In query mode, returns a list of the nodes that will be baked.
        - preDeformers (pre): Specifies baking of any modeling operations in the history that occur before the deformers. In query mode, returns a list of the nodes that will be baked.
        - prePostDeformers (ppt): Specifies baking of all modeling operations in the history whether they are before or after the deformers in the history. If neither the -prePostDeformers nor the -preDeformers flag is specified, prePostDeformers will be used as the
            default. In query mode, returns a list of the nodes that will be baked.
    """
@overload #Overload for bakePartialHistory in ['query']
def bakePartialHistory(allShapes: bool = ..., postSmooth: bool = ..., preCache: bool = ..., preDeformers: bool = ..., prePostDeformers: bool = ..., query: bool = ...) -> str:
    """bakePartialHistory is undoable, queryable, and editable.
    
    This command is used to bake sections of the construction history of a shape
    node when possible. A typical usage would be on a shape that has both
    modelling operations and deformers in its history. Using this command with the
    -prePostDeformers flag will bake the modeling portions of the graph, so that
    only the deformers remain.
    
    Note that not all modeling operations can be baked such that they create
    exactly the same effect after baking. For example, imagine the history
    contains a skinning operation followed by a smooth. Before baking, the smooth
    operation is performed each time the skin deforms, so it will smooth
    differently depending on the output of the skin. When the smooth operation is
    baked into the skinning, the skin will be reweighted based on the smooth
    points to attempt to approximate the original behavior. However, the skin node
    does not perform the smooth operation, it merely performs skinning with the
    newly calculated weights and the result will not be identical to before the
    bake.
    
    In general, modeling operations that occur before deformers can be baked
    precisely. Those which occur after can only be approximated. The -pre and
    -post flags allow you to control whether only the operations before or after
    the deformers are baked.
    
    When the command is used on an object with no deformers, the entire history
    will be deleted.

    ---
    - Args:
        - allShapes (all): Specifies that the bake operation should be performed on all shapes in the entire scene. By default, only selected objects are baked. If this option is specified and there are no shapes in the scene, then this command will do nothing and
            end successfully.
        - postSmooth (nps): Specifies whether or not a smoothing operation should be done on skin vertices. This smoothing is only done on vertices that are found to deviate largely from other vertex values.  The default is false.
        - preCache (pc): Specifies baking of any history operations that occur before the caching operation, including deformers. In query mode, returns a list of the nodes that will be baked.
        - preDeformers (pre): Specifies baking of any modeling operations in the history that occur before the deformers. In query mode, returns a list of the nodes that will be baked.
        - prePostDeformers (ppt): Specifies baking of all modeling operations in the history whether they are before or after the deformers in the history. If neither the -prePostDeformers nor the -preDeformers flag is specified, prePostDeformers will be used as the
            default. In query mode, returns a list of the nodes that will be baked.
        - query (q): Query mode flag
    """
@overload #Overload for bakePartialHistory in ['query']
def bakePartialHistory(all: bool = ..., nps: bool = ..., pc: bool = ..., pre: bool = ..., ppt: bool = ..., q: bool = ...) -> str:
    """bakePartialHistory is undoable, queryable, and editable.
    
    This command is used to bake sections of the construction history of a shape
    node when possible. A typical usage would be on a shape that has both
    modelling operations and deformers in its history. Using this command with the
    -prePostDeformers flag will bake the modeling portions of the graph, so that
    only the deformers remain.
    
    Note that not all modeling operations can be baked such that they create
    exactly the same effect after baking. For example, imagine the history
    contains a skinning operation followed by a smooth. Before baking, the smooth
    operation is performed each time the skin deforms, so it will smooth
    differently depending on the output of the skin. When the smooth operation is
    baked into the skinning, the skin will be reweighted based on the smooth
    points to attempt to approximate the original behavior. However, the skin node
    does not perform the smooth operation, it merely performs skinning with the
    newly calculated weights and the result will not be identical to before the
    bake.
    
    In general, modeling operations that occur before deformers can be baked
    precisely. Those which occur after can only be approximated. The -pre and
    -post flags allow you to control whether only the operations before or after
    the deformers are baked.
    
    When the command is used on an object with no deformers, the entire history
    will be deleted.

    ---
    - Args:
        - allShapes (all): Specifies that the bake operation should be performed on all shapes in the entire scene. By default, only selected objects are baked. If this option is specified and there are no shapes in the scene, then this command will do nothing and
            end successfully.
        - postSmooth (nps): Specifies whether or not a smoothing operation should be done on skin vertices. This smoothing is only done on vertices that are found to deviate largely from other vertex values.  The default is false.
        - preCache (pc): Specifies baking of any history operations that occur before the caching operation, including deformers. In query mode, returns a list of the nodes that will be baked.
        - preDeformers (pre): Specifies baking of any modeling operations in the history that occur before the deformers. In query mode, returns a list of the nodes that will be baked.
        - prePostDeformers (ppt): Specifies baking of all modeling operations in the history whether they are before or after the deformers in the history. If neither the -prePostDeformers nor the -preDeformers flag is specified, prePostDeformers will be used as the
            default. In query mode, returns a list of the nodes that will be baked.
        - query (q): Query mode flag
    """
@overload #Overload for bakePartialHistory in ['query']
def bakePartialHistory(allShapes: bool = ..., all: bool = ..., postSmooth: bool = ..., nps: bool = ..., preCache: bool = ..., pc: bool = ..., preDeformers: bool = ..., pre: bool = ..., prePostDeformers: bool = ..., ppt: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """bakePartialHistory is undoable, queryable, and editable.
    
    This command is used to bake sections of the construction history of a shape
    node when possible. A typical usage would be on a shape that has both
    modelling operations and deformers in its history. Using this command with the
    -prePostDeformers flag will bake the modeling portions of the graph, so that
    only the deformers remain.
    
    Note that not all modeling operations can be baked such that they create
    exactly the same effect after baking. For example, imagine the history
    contains a skinning operation followed by a smooth. Before baking, the smooth
    operation is performed each time the skin deforms, so it will smooth
    differently depending on the output of the skin. When the smooth operation is
    baked into the skinning, the skin will be reweighted based on the smooth
    points to attempt to approximate the original behavior. However, the skin node
    does not perform the smooth operation, it merely performs skinning with the
    newly calculated weights and the result will not be identical to before the
    bake.
    
    In general, modeling operations that occur before deformers can be baked
    precisely. Those which occur after can only be approximated. The -pre and
    -post flags allow you to control whether only the operations before or after
    the deformers are baked.
    
    When the command is used on an object with no deformers, the entire history
    will be deleted.

    ---
    - Args:
        - allShapes (all): Specifies that the bake operation should be performed on all shapes in the entire scene. By default, only selected objects are baked. If this option is specified and there are no shapes in the scene, then this command will do nothing and
            end successfully.
        - postSmooth (nps): Specifies whether or not a smoothing operation should be done on skin vertices. This smoothing is only done on vertices that are found to deviate largely from other vertex values.  The default is false.
        - preCache (pc): Specifies baking of any history operations that occur before the caching operation, including deformers. In query mode, returns a list of the nodes that will be baked.
        - preDeformers (pre): Specifies baking of any modeling operations in the history that occur before the deformers. In query mode, returns a list of the nodes that will be baked.
        - prePostDeformers (ppt): Specifies baking of all modeling operations in the history whether they are before or after the deformers in the history. If neither the -prePostDeformers nor the -preDeformers flag is specified, prePostDeformers will be used as the
            default. In query mode, returns a list of the nodes that will be baked.
        - query (q): Query mode flag
    """
@overload #Overload for bakePartialHistory in ['edit']
def bakePartialHistory(allShapes: bool = ..., postSmooth: bool = ..., preCache: bool = ..., preDeformers: bool = ..., prePostDeformers: bool = ..., edit: bool = ...) -> str:
    """bakePartialHistory is undoable, queryable, and editable.
    
    This command is used to bake sections of the construction history of a shape
    node when possible. A typical usage would be on a shape that has both
    modelling operations and deformers in its history. Using this command with the
    -prePostDeformers flag will bake the modeling portions of the graph, so that
    only the deformers remain.
    
    Note that not all modeling operations can be baked such that they create
    exactly the same effect after baking. For example, imagine the history
    contains a skinning operation followed by a smooth. Before baking, the smooth
    operation is performed each time the skin deforms, so it will smooth
    differently depending on the output of the skin. When the smooth operation is
    baked into the skinning, the skin will be reweighted based on the smooth
    points to attempt to approximate the original behavior. However, the skin node
    does not perform the smooth operation, it merely performs skinning with the
    newly calculated weights and the result will not be identical to before the
    bake.
    
    In general, modeling operations that occur before deformers can be baked
    precisely. Those which occur after can only be approximated. The -pre and
    -post flags allow you to control whether only the operations before or after
    the deformers are baked.
    
    When the command is used on an object with no deformers, the entire history
    will be deleted.

    ---
    - Args:
        - allShapes (all): Specifies that the bake operation should be performed on all shapes in the entire scene. By default, only selected objects are baked. If this option is specified and there are no shapes in the scene, then this command will do nothing and
            end successfully.
        - postSmooth (nps): Specifies whether or not a smoothing operation should be done on skin vertices. This smoothing is only done on vertices that are found to deviate largely from other vertex values.  The default is false.
        - preCache (pc): Specifies baking of any history operations that occur before the caching operation, including deformers. In query mode, returns a list of the nodes that will be baked.
        - preDeformers (pre): Specifies baking of any modeling operations in the history that occur before the deformers. In query mode, returns a list of the nodes that will be baked.
        - prePostDeformers (ppt): Specifies baking of all modeling operations in the history whether they are before or after the deformers in the history. If neither the -prePostDeformers nor the -preDeformers flag is specified, prePostDeformers will be used as the
            default. In query mode, returns a list of the nodes that will be baked.
        - edit (e): Edit mode flag
    """
@overload #Overload for bakePartialHistory in ['edit']
def bakePartialHistory(all: bool = ..., nps: bool = ..., pc: bool = ..., pre: bool = ..., ppt: bool = ..., e: bool = ...) -> str:
    """bakePartialHistory is undoable, queryable, and editable.
    
    This command is used to bake sections of the construction history of a shape
    node when possible. A typical usage would be on a shape that has both
    modelling operations and deformers in its history. Using this command with the
    -prePostDeformers flag will bake the modeling portions of the graph, so that
    only the deformers remain.
    
    Note that not all modeling operations can be baked such that they create
    exactly the same effect after baking. For example, imagine the history
    contains a skinning operation followed by a smooth. Before baking, the smooth
    operation is performed each time the skin deforms, so it will smooth
    differently depending on the output of the skin. When the smooth operation is
    baked into the skinning, the skin will be reweighted based on the smooth
    points to attempt to approximate the original behavior. However, the skin node
    does not perform the smooth operation, it merely performs skinning with the
    newly calculated weights and the result will not be identical to before the
    bake.
    
    In general, modeling operations that occur before deformers can be baked
    precisely. Those which occur after can only be approximated. The -pre and
    -post flags allow you to control whether only the operations before or after
    the deformers are baked.
    
    When the command is used on an object with no deformers, the entire history
    will be deleted.

    ---
    - Args:
        - allShapes (all): Specifies that the bake operation should be performed on all shapes in the entire scene. By default, only selected objects are baked. If this option is specified and there are no shapes in the scene, then this command will do nothing and
            end successfully.
        - postSmooth (nps): Specifies whether or not a smoothing operation should be done on skin vertices. This smoothing is only done on vertices that are found to deviate largely from other vertex values.  The default is false.
        - preCache (pc): Specifies baking of any history operations that occur before the caching operation, including deformers. In query mode, returns a list of the nodes that will be baked.
        - preDeformers (pre): Specifies baking of any modeling operations in the history that occur before the deformers. In query mode, returns a list of the nodes that will be baked.
        - prePostDeformers (ppt): Specifies baking of all modeling operations in the history whether they are before or after the deformers in the history. If neither the -prePostDeformers nor the -preDeformers flag is specified, prePostDeformers will be used as the
            default. In query mode, returns a list of the nodes that will be baked.
        - edit (e): Edit mode flag
    """
@overload #Overload for bakePartialHistory in ['edit']
def bakePartialHistory(allShapes: bool = ..., all: bool = ..., postSmooth: bool = ..., nps: bool = ..., preCache: bool = ..., pc: bool = ..., preDeformers: bool = ..., pre: bool = ..., prePostDeformers: bool = ..., ppt: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """bakePartialHistory is undoable, queryable, and editable.
    
    This command is used to bake sections of the construction history of a shape
    node when possible. A typical usage would be on a shape that has both
    modelling operations and deformers in its history. Using this command with the
    -prePostDeformers flag will bake the modeling portions of the graph, so that
    only the deformers remain.
    
    Note that not all modeling operations can be baked such that they create
    exactly the same effect after baking. For example, imagine the history
    contains a skinning operation followed by a smooth. Before baking, the smooth
    operation is performed each time the skin deforms, so it will smooth
    differently depending on the output of the skin. When the smooth operation is
    baked into the skinning, the skin will be reweighted based on the smooth
    points to attempt to approximate the original behavior. However, the skin node
    does not perform the smooth operation, it merely performs skinning with the
    newly calculated weights and the result will not be identical to before the
    bake.
    
    In general, modeling operations that occur before deformers can be baked
    precisely. Those which occur after can only be approximated. The -pre and
    -post flags allow you to control whether only the operations before or after
    the deformers are baked.
    
    When the command is used on an object with no deformers, the entire history
    will be deleted.

    ---
    - Args:
        - allShapes (all): Specifies that the bake operation should be performed on all shapes in the entire scene. By default, only selected objects are baked. If this option is specified and there are no shapes in the scene, then this command will do nothing and
            end successfully.
        - postSmooth (nps): Specifies whether or not a smoothing operation should be done on skin vertices. This smoothing is only done on vertices that are found to deviate largely from other vertex values.  The default is false.
        - preCache (pc): Specifies baking of any history operations that occur before the caching operation, including deformers. In query mode, returns a list of the nodes that will be baked.
        - preDeformers (pre): Specifies baking of any modeling operations in the history that occur before the deformers. In query mode, returns a list of the nodes that will be baked.
        - prePostDeformers (ppt): Specifies baking of all modeling operations in the history whether they are before or after the deformers in the history. If neither the -prePostDeformers nor the -preDeformers flag is specified, prePostDeformers will be used as the
            default. In query mode, returns a list of the nodes that will be baked.
        - edit (e): Edit mode flag
    """
