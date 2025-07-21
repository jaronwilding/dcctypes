"""Stub files for Display category in Maya commands, command: currentUnit."""

from typing import overload

# [CREATE] Angle Overloads

@overload
def currentUnit(angle: str = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - angle (a): Set the current angular unit. Valid strings are: [`deg` | `degree` | `rad` | `radian`]. Returns the current angular unit as a string.
    """

@overload
def currentUnit(a: str = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - angle (a): Set the current angular unit. Valid strings are: [`deg` | `degree` | `rad` | `radian`]. Returns the current angular unit as a string.
    """

@overload
def currentUnit(angle: str = ..., a: str = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - angle (a): Set the current angular unit. Valid strings are: [`deg` | `degree` | `rad` | `radian`]. Returns the current angular unit as a string.
    """

# [CREATE] Linear Overloads

@overload
def currentUnit(linear: str = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - linear (l): Set the current linear unit. Valid strings are: [`mm` | `millimeter` | `cm` | `centimeter` | `m` | `meter` | `km` | `kilometer` | `in` | `inch`
            | `ft` | `foot` | `yd` | `yard` | `mi` | `mile`]. Returns the current linear unit as a string.
    """

@overload
def currentUnit(l: str = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - linear (l): Set the current linear unit. Valid strings are: [`mm` | `millimeter` | `cm` | `centimeter` | `m` | `meter` | `km` | `kilometer` | `in` | `inch`
            | `ft` | `foot` | `yd` | `yard` | `mi` | `mile`]. Returns the current linear unit as a string.
    """

@overload
def currentUnit(linear: str = ..., l: str = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - linear (l): Set the current linear unit. Valid strings are: [`mm` | `millimeter` | `cm` | `centimeter` | `m` | `meter` | `km` | `kilometer` | `in` | `inch`
            | `ft` | `foot` | `yd` | `yard` | `mi` | `mile`]. Returns the current linear unit as a string.
    """

# [CREATE] Time Overloads

@overload
def currentUnit(time: str = ..., updateAnimation: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - time (t): Set the current time unit. Valid strings are: [`hour` | `min` | `sec` | `millisec` | `game` | `film` | `pal` | `ntsc` | `show` | `palf` | `ntscf` |
            `23.976fps` | `29.97fps` | `29.97df` | `47.952fps` | `59.94fps` | `44100fps` | `48000fps`]. Returns the current time unit as a string.
        - updateAnimation (ua): An edit only flag. When specified in conjunction with the `-time` flag indicates that times for keys are not updated. By default when the
            current time unit is changed, the times for keys are modified so that playback timing is preserved. For example a key set a frame 12film is changed to frame 15ntsc
            when the current time unit is changed to `ntsc`, since they both represent a key at a time of 0.5 seconds.
            Specifying -updateAnimation false would leave the key at frame 12ntsc. Default is -updateAnimation true.
    """

@overload
def currentUnit(t: str = ..., ua: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - time (t): Set the current time unit. Valid strings are: [`hour` | `min` | `sec` | `millisec` | `game` | `film` | `pal` | `ntsc` | `show` | `palf` | `ntscf` |
            `23.976fps` | `29.97fps` | `29.97df` | `47.952fps` | `59.94fps` | `44100fps` | `48000fps`]. Returns the current time unit as a string.
        - updateAnimation (ua): An edit only flag. When specified in conjunction with the `-time` flag indicates that times for keys are not updated. By default when the
            current time unit is changed, the times for keys are modified so that playback timing is preserved. For example a key set a frame 12film is changed to frame 15ntsc
            when the current time unit is changed to `ntsc`, since they both represent a key at a time of 0.5 seconds.
            Specifying -updateAnimation false would leave the key at frame 12ntsc. Default is -updateAnimation true.
    """

@overload
def currentUnit(time: str = ..., t: str = ..., updateAnimation: bool = ..., ua: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - time (t): Set the current time unit. Valid strings are: [`hour` | `min` | `sec` | `millisec` | `game` | `film` | `pal` | `ntsc` | `show` | `palf` | `ntscf` |
            `23.976fps` | `29.97fps` | `29.97df` | `47.952fps` | `59.94fps` | `44100fps` | `48000fps`]. Returns the current time unit as a string.
        - updateAnimation (ua): An edit only flag. When specified in conjunction with the `-time` flag indicates that times for keys are not updated. By default when the
            current time unit is changed, the times for keys are modified so that playback timing is preserved. For example a key set a frame 12film is changed to frame 15ntsc
            when the current time unit is changed to `ntsc`, since they both represent a key at a time of 0.5 seconds.
            Specifying -updateAnimation false would leave the key at frame 12ntsc. Default is -updateAnimation true.
    """

# [CREATE] Update Animation Overloads

@overload
def currentUnit(updateAnimation: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - updateAnimation (ua): An edit only flag. When specified in conjunction with the `-time` flag indicates that times for keys are not updated. By default when the
            current time unit is changed, the times for keys are modified so that playback timing is preserved. For example a key set a frame 12film is changed to frame 15ntsc
            when the current time unit is changed to `ntsc`, since they both represent a key at a time of 0.5 seconds.
            Specifying -updateAnimation false would leave the key at frame 12ntsc. Default is -updateAnimation true.
    """

@overload
def currentUnit(ua: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - updateAnimation (ua): An edit only flag. When specified in conjunction with the `-time` flag indicates that times for keys are not updated. By default when the
            current time unit is changed, the times for keys are modified so that playback timing is preserved. For example a key set a frame 12film is changed to frame 15ntsc
            when the current time unit is changed to `ntsc`, since they both represent a key at a time of 0.5 seconds.
            Specifying -updateAnimation false would leave the key at frame 12ntsc. Default is -updateAnimation true.
    """

@overload
def currentUnit(updateAnimation: bool = ..., ua: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - updateAnimation (ua): An edit only flag. When specified in conjunction with the `-time` flag indicates that times for keys are not updated. By default when the
            current time unit is changed, the times for keys are modified so that playback timing is preserved. For example a key set a frame 12film is changed to frame 15ntsc
            when the current time unit is changed to `ntsc`, since they both represent a key at a time of 0.5 seconds.
            Specifying -updateAnimation false would leave the key at frame 12ntsc. Default is -updateAnimation true.
    """

# [CREATE] Default Overloads

@overload
def currentUnit(angle: str = ..., linear: str = ..., time: str = ..., updateAnimation: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - angle (a): Set the current angular unit. Valid strings are: [`deg` | `degree` | `rad` | `radian`].
        - linear (l): Set the current linear unit. Valid strings are: [`mm` | `millimeter` | `cm` | `centimeter` | `m` | `meter` | `km` | `kilometer` | `in` | `inch`
            | `ft` | `foot` | `yd` | `yard` | `mi` | `mile`].
        - time (t): Set the current time unit. Valid strings are: [`hour` | `min` | `sec` | `millisec` | `game` | `film` | `pal` | `ntsc` | `show` | `palf` | `ntscf` |
            `23.976fps` | `29.97fps` | `29.97df` | `47.952fps` | `59.94fps` | `44100fps` | `48000fps`].
        - updateAnimation (ua): An edit only flag. When specified in conjunction with the `-time` flag indicates that times for keys are not updated. By default when the
            current time unit is changed, the times for keys are modified so that playback timing is preserved. For example a key set a frame 12film is changed to frame 15ntsc
            when the current time unit is changed to `ntsc`, since they both represent a key at a time of 0.5 seconds.
            Specifying -updateAnimation false would leave the key at frame 12ntsc. Default is -updateAnimation true.
    """

@overload
def currentUnit(a: str = ..., l: str = ..., t: str = ..., ua: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - angle (a): Set the current angular unit. Valid strings are: [`deg` | `degree` | `rad` | `radian`].
        - linear (l): Set the current linear unit. Valid strings are: [`mm` | `millimeter` | `cm` | `centimeter` | `m` | `meter` | `km` | `kilometer` | `in` | `inch`
            | `ft` | `foot` | `yd` | `yard` | `mi` | `mile`].
        - time (t): Set the current time unit. Valid strings are: [`hour` | `min` | `sec` | `millisec` | `game` | `film` | `pal` | `ntsc` | `show` | `palf` | `ntscf` |
            `23.976fps` | `29.97fps` | `29.97df` | `47.952fps` | `59.94fps` | `44100fps` | `48000fps`].
        - updateAnimation (ua): An edit only flag. When specified in conjunction with the `-time` flag indicates that times for keys are not updated. By default when the
            current time unit is changed, the times for keys are modified so that playback timing is preserved. For example a key set a frame 12film is changed to frame 15ntsc
            when the current time unit is changed to `ntsc`, since they both represent a key at a time of 0.5 seconds.
            Specifying -updateAnimation false would leave the key at frame 12ntsc. Default is -updateAnimation true.
    """

@overload
def currentUnit(angle: str = ..., a: str = ..., linear: str = ..., l: str = ..., time: str = ..., t: str = ..., updateAnimation: bool = ..., ua: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - angle (a): Set the current angular unit. Valid strings are: [`deg` | `degree` | `rad` | `radian`].
        - linear (l): Set the current linear unit. Valid strings are: [`mm` | `millimeter` | `cm` | `centimeter` | `m` | `meter` | `km` | `kilometer` | `in` | `inch`
            | `ft` | `foot` | `yd` | `yard` | `mi` | `mile`].
        - time (t): Set the current time unit. Valid strings are: [`hour` | `min` | `sec` | `millisec` | `game` | `film` | `pal` | `ntsc` | `show` | `palf` | `ntscf` |
            `23.976fps` | `29.97fps` | `29.97df` | `47.952fps` | `59.94fps` | `44100fps` | `48000fps`].
        - updateAnimation (ua): An edit only flag. When specified in conjunction with the `-time` flag indicates that times for keys are not updated. By default when the
            current time unit is changed, the times for keys are modified so that playback timing is preserved. For example a key set a frame 12film is changed to frame 15ntsc
            when the current time unit is changed to `ntsc`, since they both represent a key at a time of 0.5 seconds.
            Specifying -updateAnimation false would leave the key at frame 12ntsc. Default is -updateAnimation true.
    """

# [QUERY] Angle and Full Name Overloads

@overload
def currentUnit(angle: str = ..., fullName: bool = ..., query: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - angle (a): Returns a string which is the current angular unit: [`deg` | `degree` | `rad` | `radian`].
        - fullName (f): A query only flag. When specified in conjunction with any of the `-linear`/`-angle`/`-time` flags, will return the long form of the unit. For example,
            `mm` and `millimeter` are the same unit, but the former is the short form of the unit name, and the latter is the long form of the unit name.
        - query (q): Query mode flag
    """

@overload
def currentUnit(a: str = ..., f: bool = ..., q: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - angle (a): Returns a string which is the current angular unit: [`deg` | `degree` | `rad` | `radian`].
        - fullName (f): A query only flag. When specified in conjunction with any of the `-linear`/`-angle`/`-time` flags, will return the long form of the unit. For example,
            `mm` and `millimeter` are the same unit, but the former is the short form of the unit name, and the latter is the long form of the unit name.
        - query (q): Query mode flag
    """

@overload
def currentUnit(angle: str = ..., a: str = ..., fullName: bool = ..., f: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - angle (a): Returns a string which is the current angular unit: [`deg` | `degree` | `rad` | `radian`].
        - fullName (f): A query only flag. When specified in conjunction with any of the `-linear`/`-angle`/`-time` flags, will return the long form of the unit. For example,
            `mm` and `millimeter` are the same unit, but the former is the short form of the unit name, and the latter is the long form of the unit name.
        - query (q): Query mode flag
    """

# [QUERY] Linear and Full Name Overloads

@overload
def currentUnit(fullName: bool = ..., linear: str = ..., query: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - fullName (f): A query only flag. When specified in conjunction with any of the `-linear`/`-angle`/`-time` flags, will return the long form of the unit. For example,
            `mm` and `millimeter` are the same unit, but the former is the short form of the unit name, and the latter is the long form of the unit name.
        - linear (l): Returns a string which is the current linear unit: [`mm` | `millimeter` | `cm` | `centimeter` | `m` | `meter` | `km` | `kilometer` | `in` | `inch` |
            `ft` | `foot` | `yd` | `yard` | `mi` | `mile`]
        - query (q): Query mode flag
    """

@overload
def currentUnit(f: bool = ..., l: str = ..., q: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - fullName (f): A query only flag. When specified in conjunction with any of the `-linear`/`-angle`/`-time` flags, will return the long form of the unit. For example,
            `mm` and `millimeter` are the same unit, but the former is the short form of the unit name, and the latter is the long form of the unit name.
        - linear (l): Returns a string which is the current linear unit: [`mm` | `millimeter` | `cm` | `centimeter` | `m` | `meter` | `km` | `kilometer` | `in` | `inch` |
            `ft` | `foot` | `yd` | `yard` | `mi` | `mile`]
        - query (q): Query mode flag
    """

@overload
def currentUnit(fullName: bool = ..., f: str = ..., linear: str = ..., l: str = ..., query: bool = ..., q: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - fullName (f): A query only flag. When specified in conjunction with any of the `-linear`/`-angle`/`-time` flags, will return the long form of the unit. For example,
            `mm` and `millimeter` are the same unit, but the former is the short form of the unit name, and the latter is the long form of the unit name.
        - linear (l): Returns a string which is the current linear unit: [`mm` | `millimeter` | `cm` | `centimeter` | `m` | `meter` | `km` | `kilometer` | `in` | `inch` |
            `ft` | `foot` | `yd` | `yard` | `mi` | `mile`]
        - query (q): Query mode flag
    """

# [QUERY] Time Overloads

@overload
def currentUnit(time: str = ..., query: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - time (t): Returns a string which is the current time unit. Note that there is no long form for any of the time units. The non-seconds based time units are
            interpreted as the following frames per second: `15 fps`, `film`: `24 fps`, `pal`: `25 fps`, `ntsc`: `30 fps`, `show`: `48 fps`, `palf`: `50 fps`, `ntscf`: `60 fps`
        - query (q): Query mode flag
    """

@overload
def currentUnit(t: str = ..., q: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - time (t): Returns a string which is the current time unit. Note that there is no long form for any of the time units. The non-seconds based time units are
            interpreted as the following frames per second: `15 fps`, `film`: `24 fps`, `pal`: `25 fps`, `ntsc`: `30 fps`, `show`: `48 fps`, `palf`: `50 fps`, `ntscf`: `60 fps`
        - query (q): Query mode flag
    """

@overload
def currentUnit(time: str = ..., t: str = ..., query: bool = ..., q: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - time (t): Returns a string which is the current time unit. Note that there is no long form for any of the time units. The non-seconds based time units are
            interpreted as the following frames per second: `15 fps`, `film`: `24 fps`, `pal`: `25 fps`, `ntsc`: `30 fps`, `show`: `48 fps`, `palf`: `50 fps`, `ntscf`: `60 fps`
        - query (q): Query mode flag
    """

# [QUERY] Default Overloads

@overload
def currentUnit(angle: str = ..., fullName: bool = ..., linear: str = ..., time: str = ..., query: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - angle (a): Returns a string which is the current angular unit: [`deg` | `degree` | `rad` | `radian`].
        - fullName (f): A query only flag. When specified in conjunction with any of the `-linear`/`-angle`/`-time` flags, will return the long form of the unit. For example,
            `mm` and `millimeter` are the same unit, but the former is the short form of the unit name, and the latter is the long form of the unit name.
        - linear (l): Returns a string which is the current linear unit: [`mm` | `millimeter` | `cm` | `centimeter` | `m` | `meter` | `km` | `kilometer` | `in` | `inch` |
            `ft` | `foot` | `yd` | `yard` | `mi` | `mile`]
        - time (t): Returns a string which is the current time unit. Note that there is no long form for any of the time units. The non-seconds based time units are
            interpreted as the following frames per second: `15 fps`, `film`: `24 fps`, `pal`: `25 fps`, `ntsc`: `30 fps`, `show`: `48 fps`, `palf`: `50 fps`, `ntscf`: `60 fps`
        - query (q): Query mode flag
    """

@overload
def currentUnit(a: str = ..., f: bool = ..., l: str = ..., t: str = ..., q: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - angle (a): Returns a string which is the current angular unit: [`deg` | `degree` | `rad` | `radian`].
        - fullName (f): A query only flag. When specified in conjunction with any of the `-linear`/`-angle`/`-time` flags, will return the long form of the unit. For example,
            `mm` and `millimeter` are the same unit, but the former is the short form of the unit name, and the latter is the long form of the unit name.
        - linear (l): Returns a string which is the current linear unit: [`mm` | `millimeter` | `cm` | `centimeter` | `m` | `meter` | `km` | `kilometer` | `in` | `inch` |
            `ft` | `foot` | `yd` | `yard` | `mi` | `mile`]
        - time (t): Returns a string which is the current time unit. Note that there is no long form for any of the time units. The non-seconds based time units are
            interpreted as the following frames per second: `15 fps`, `film`: `24 fps`, `pal`: `25 fps`, `ntsc`: `30 fps`, `show`: `48 fps`, `palf`: `50 fps`, `ntscf`: `60 fps`
        - query (q): Query mode flag
    """

@overload
def currentUnit(angle: str = ..., a: str = ..., fullName: bool = ..., f: bool = ..., linear: str = ..., l: str = ..., time: str = ..., t: str = ..., query: bool = ..., q: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.

    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.

    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    ```python
    move 5 -2 3;
    sphere -radius 4;
    ```

    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    ```python
    currentTime 6;
    ```

    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.

    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    ```python
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    ```

    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Examples:
    ```python
    import maya.cmds as cmds

    # What is the current linear unit?
    cmds.currentUnit( query=True, linear=True )

    # What is the current angular unit in its long name form?
    cmds.currentUnit( fullName=True, query=True, angle=True )

    # Change the current time unit to ntsc
    cmds.currentUnit( time='ntsc' )

    # Change the current linear unit to inches
    cmds.currentUnit( linear='in' )

    ```

    ---
    - Args:
        - angle (a): Returns a string which is the current angular unit: [`deg` | `degree` | `rad` | `radian`].
        - fullName (f): A query only flag. When specified in conjunction with any of the `-linear`/`-angle`/`-time` flags, will return the long form of the unit. For example,
            `mm` and `millimeter` are the same unit, but the former is the short form of the unit name, and the latter is the long form of the unit name.
        - linear (l): Returns a string which is the current linear unit: [`mm` | `millimeter` | `cm` | `centimeter` | `m` | `meter` | `km` | `kilometer` | `in` | `inch` |
            `ft` | `foot` | `yd` | `yard` | `mi` | `mile`]
        - time (t): Returns a string which is the current time unit. Note that there is no long form for any of the time units. The non-seconds based time units are
            interpreted as the following frames per second: `15 fps`, `film`: `24 fps`, `pal`: `25 fps`, `ntsc`: `30 fps`, `show`: `48 fps`, `palf`: `50 fps`, `ntscf`: `60 fps`
        - query (q): Query mode flag
    """
