"""Stub files for Display category in Maya commands, command: currentUnit."""

from typing import Any, overload

@overload #Overload for currentUnit in ['create']
def currentUnit(angle: str = ..., linear: str = ..., time: str = ..., updateAnimation: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.
    
    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.
    
    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    
    
    
    move 5 -2 3;
    sphere -radius 4;
    
    
    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    
    
    
    currentTime 6;
    
    
    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.
    
    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    
    
    
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    
    
    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Args:
        - angle (a): Set the current angular unit. Valid strings are:[deg | degree | rad | radian]When queried, returns a string which is the current angular unit
        - linear (l): Set the current linear unit. Valid strings are:[mm | millimeter | cm | centimeter | m | meter | km | kilometer | in | inch | ft | foot | yd | yard | mi | mile]When queried, returns a string which is the current linear unit
        - time (t): Set the current time unit. Valid strings are:[hour | min | sec | millisec | game | film | pal | ntsc | show | palf | ntscf | 23.976fps | 29.97fps | 29.97df | 47.952fps | 59.94fps | 44100fps | 48000fps]When queried, returns a string which is
            the current time unitNote that there is no long form for any of the time units. The non-seconds based time units are interpreted as the following frames per second:game: 15 fpsfilm: 24 fpspal: 25 fpsntsc: 30 fpsshow: 48 fpspalf: 50
            fpsntscf: 60 fps
        - updateAnimation (ua): An edit only flag.  When specified in conjunction with the -time flag indicates that times for keys are not updated.  By default when the current time unit is changed, the times for keys are modified so that playback timing is preserved.
            For example a key set a frame 12film is changed to frame 15ntsc when the current time unit is changed to ntsc, since they both represent a key at a time of 0.5 seconds.  Specifying -updateAnimation false would leave the key at frame 12ntsc.
            Default is -updateAnimation true.
    """
@overload #Overload for currentUnit in ['create']
def currentUnit(a: str = ..., l: str = ..., t: str = ..., ua: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.
    
    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.
    
    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    
    
    
    move 5 -2 3;
    sphere -radius 4;
    
    
    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    
    
    
    currentTime 6;
    
    
    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.
    
    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    
    
    
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    
    
    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Args:
        - angle (a): Set the current angular unit. Valid strings are:[deg | degree | rad | radian]When queried, returns a string which is the current angular unit
        - linear (l): Set the current linear unit. Valid strings are:[mm | millimeter | cm | centimeter | m | meter | km | kilometer | in | inch | ft | foot | yd | yard | mi | mile]When queried, returns a string which is the current linear unit
        - time (t): Set the current time unit. Valid strings are:[hour | min | sec | millisec | game | film | pal | ntsc | show | palf | ntscf | 23.976fps | 29.97fps | 29.97df | 47.952fps | 59.94fps | 44100fps | 48000fps]When queried, returns a string which is
            the current time unitNote that there is no long form for any of the time units. The non-seconds based time units are interpreted as the following frames per second:game: 15 fpsfilm: 24 fpspal: 25 fpsntsc: 30 fpsshow: 48 fpspalf: 50
            fpsntscf: 60 fps
        - updateAnimation (ua): An edit only flag.  When specified in conjunction with the -time flag indicates that times for keys are not updated.  By default when the current time unit is changed, the times for keys are modified so that playback timing is preserved.
            For example a key set a frame 12film is changed to frame 15ntsc when the current time unit is changed to ntsc, since they both represent a key at a time of 0.5 seconds.  Specifying -updateAnimation false would leave the key at frame 12ntsc.
            Default is -updateAnimation true.
    """
@overload #Overload for currentUnit in ['create']
def currentUnit(angle: str = ..., a: str = ..., linear: str = ..., l: str = ..., time: str = ..., t: str = ..., updateAnimation: bool = ..., ua: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.
    
    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.
    
    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    
    
    
    move 5 -2 3;
    sphere -radius 4;
    
    
    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    
    
    
    currentTime 6;
    
    
    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.
    
    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    
    
    
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    
    
    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Args:
        - angle (a): Set the current angular unit. Valid strings are:[deg | degree | rad | radian]When queried, returns a string which is the current angular unit
        - linear (l): Set the current linear unit. Valid strings are:[mm | millimeter | cm | centimeter | m | meter | km | kilometer | in | inch | ft | foot | yd | yard | mi | mile]When queried, returns a string which is the current linear unit
        - time (t): Set the current time unit. Valid strings are:[hour | min | sec | millisec | game | film | pal | ntsc | show | palf | ntscf | 23.976fps | 29.97fps | 29.97df | 47.952fps | 59.94fps | 44100fps | 48000fps]When queried, returns a string which is
            the current time unitNote that there is no long form for any of the time units. The non-seconds based time units are interpreted as the following frames per second:game: 15 fpsfilm: 24 fpspal: 25 fpsntsc: 30 fpsshow: 48 fpspalf: 50
            fpsntscf: 60 fps
        - updateAnimation (ua): An edit only flag.  When specified in conjunction with the -time flag indicates that times for keys are not updated.  By default when the current time unit is changed, the times for keys are modified so that playback timing is preserved.
            For example a key set a frame 12film is changed to frame 15ntsc when the current time unit is changed to ntsc, since they both represent a key at a time of 0.5 seconds.  Specifying -updateAnimation false would leave the key at frame 12ntsc.
            Default is -updateAnimation true.
    """
@overload #Overload for currentUnit in ['query']
def currentUnit(angle: str = ..., fullName: bool = ..., linear: str = ..., time: str = ..., query: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.
    
    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.
    
    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    
    
    
    move 5 -2 3;
    sphere -radius 4;
    
    
    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    
    
    
    currentTime 6;
    
    
    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.
    
    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    
    
    
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    
    
    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Args:
        - angle (a): Set the current angular unit. Valid strings are:[deg | degree | rad | radian]When queried, returns a string which is the current angular unit
        - fullName (f): A query only flag. When specified in conjunction with any of the -linear/-angle/-time flags, will return the long form of the unit. For example,mmandmillimeterare the same unit, but the former is the short form of the unit name, and the
            latter is the long form of the unit name.
        - linear (l): Set the current linear unit. Valid strings are:[mm | millimeter | cm | centimeter | m | meter | km | kilometer | in | inch | ft | foot | yd | yard | mi | mile]When queried, returns a string which is the current linear unit
        - time (t): Set the current time unit. Valid strings are:[hour | min | sec | millisec | game | film | pal | ntsc | show | palf | ntscf | 23.976fps | 29.97fps | 29.97df | 47.952fps | 59.94fps | 44100fps | 48000fps]When queried, returns a string which is
            the current time unitNote that there is no long form for any of the time units. The non-seconds based time units are interpreted as the following frames per second:game: 15 fpsfilm: 24 fpspal: 25 fpsntsc: 30 fpsshow: 48 fpspalf: 50
            fpsntscf: 60 fps
        - query (q): Query mode flag
    """
@overload #Overload for currentUnit in ['query']
def currentUnit(a: str = ..., f: bool = ..., l: str = ..., t: str = ..., q: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.
    
    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.
    
    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    
    
    
    move 5 -2 3;
    sphere -radius 4;
    
    
    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    
    
    
    currentTime 6;
    
    
    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.
    
    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    
    
    
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    
    
    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Args:
        - angle (a): Set the current angular unit. Valid strings are:[deg | degree | rad | radian]When queried, returns a string which is the current angular unit
        - fullName (f): A query only flag. When specified in conjunction with any of the -linear/-angle/-time flags, will return the long form of the unit. For example,mmandmillimeterare the same unit, but the former is the short form of the unit name, and the
            latter is the long form of the unit name.
        - linear (l): Set the current linear unit. Valid strings are:[mm | millimeter | cm | centimeter | m | meter | km | kilometer | in | inch | ft | foot | yd | yard | mi | mile]When queried, returns a string which is the current linear unit
        - time (t): Set the current time unit. Valid strings are:[hour | min | sec | millisec | game | film | pal | ntsc | show | palf | ntscf | 23.976fps | 29.97fps | 29.97df | 47.952fps | 59.94fps | 44100fps | 48000fps]When queried, returns a string which is
            the current time unitNote that there is no long form for any of the time units. The non-seconds based time units are interpreted as the following frames per second:game: 15 fpsfilm: 24 fpspal: 25 fpsntsc: 30 fpsshow: 48 fpspalf: 50
            fpsntscf: 60 fps
        - query (q): Query mode flag
    """
@overload #Overload for currentUnit in ['query']
def currentUnit(angle: str = ..., a: str = ..., fullName: bool = ..., f: bool = ..., linear: str = ..., l: str = ..., time: str = ..., t: str = ..., query: bool = ..., q: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.
    
    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.
    
    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    
    
    
    move 5 -2 3;
    sphere -radius 4;
    
    
    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    
    
    
    currentTime 6;
    
    
    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.
    
    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    
    
    
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    
    
    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Args:
        - angle (a): Set the current angular unit. Valid strings are:[deg | degree | rad | radian]When queried, returns a string which is the current angular unit
        - fullName (f): A query only flag. When specified in conjunction with any of the -linear/-angle/-time flags, will return the long form of the unit. For example,mmandmillimeterare the same unit, but the former is the short form of the unit name, and the
            latter is the long form of the unit name.
        - linear (l): Set the current linear unit. Valid strings are:[mm | millimeter | cm | centimeter | m | meter | km | kilometer | in | inch | ft | foot | yd | yard | mi | mile]When queried, returns a string which is the current linear unit
        - time (t): Set the current time unit. Valid strings are:[hour | min | sec | millisec | game | film | pal | ntsc | show | palf | ntscf | 23.976fps | 29.97fps | 29.97df | 47.952fps | 59.94fps | 44100fps | 48000fps]When queried, returns a string which is
            the current time unitNote that there is no long form for any of the time units. The non-seconds based time units are interpreted as the following frames per second:game: 15 fpsfilm: 24 fpspal: 25 fpsntsc: 30 fpsshow: 48 fpspalf: 50
            fpsntscf: 60 fps
        - query (q): Query mode flag
    """
@overload #Overload for currentUnit in ['edit']
def currentUnit(angle: str = ..., linear: str = ..., time: str = ..., edit: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.
    
    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.
    
    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    
    
    
    move 5 -2 3;
    sphere -radius 4;
    
    
    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    
    
    
    currentTime 6;
    
    
    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.
    
    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    
    
    
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    
    
    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Args:
        - angle (a): Set the current angular unit. Valid strings are:[deg | degree | rad | radian]When queried, returns a string which is the current angular unit
        - linear (l): Set the current linear unit. Valid strings are:[mm | millimeter | cm | centimeter | m | meter | km | kilometer | in | inch | ft | foot | yd | yard | mi | mile]When queried, returns a string which is the current linear unit
        - time (t): Set the current time unit. Valid strings are:[hour | min | sec | millisec | game | film | pal | ntsc | show | palf | ntscf | 23.976fps | 29.97fps | 29.97df | 47.952fps | 59.94fps | 44100fps | 48000fps]When queried, returns a string which is
            the current time unitNote that there is no long form for any of the time units. The non-seconds based time units are interpreted as the following frames per second:game: 15 fpsfilm: 24 fpspal: 25 fpsntsc: 30 fpsshow: 48 fpspalf: 50
            fpsntscf: 60 fps
        - edit (e): Edit mode flag
    """
@overload #Overload for currentUnit in ['edit']
def currentUnit(a: str = ..., l: str = ..., t: str = ..., e: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.
    
    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.
    
    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    
    
    
    move 5 -2 3;
    sphere -radius 4;
    
    
    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    
    
    
    currentTime 6;
    
    
    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.
    
    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    
    
    
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    
    
    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Args:
        - angle (a): Set the current angular unit. Valid strings are:[deg | degree | rad | radian]When queried, returns a string which is the current angular unit
        - linear (l): Set the current linear unit. Valid strings are:[mm | millimeter | cm | centimeter | m | meter | km | kilometer | in | inch | ft | foot | yd | yard | mi | mile]When queried, returns a string which is the current linear unit
        - time (t): Set the current time unit. Valid strings are:[hour | min | sec | millisec | game | film | pal | ntsc | show | palf | ntscf | 23.976fps | 29.97fps | 29.97df | 47.952fps | 59.94fps | 44100fps | 48000fps]When queried, returns a string which is
            the current time unitNote that there is no long form for any of the time units. The non-seconds based time units are interpreted as the following frames per second:game: 15 fpsfilm: 24 fpspal: 25 fpsntsc: 30 fpsshow: 48 fpspalf: 50
            fpsntscf: 60 fps
        - edit (e): Edit mode flag
    """
@overload #Overload for currentUnit in ['edit']
def currentUnit(angle: str = ..., a: str = ..., linear: str = ..., l: str = ..., time: str = ..., t: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """currentUnit is undoable, queryable, and NOT editable.
    
    This command allows you to change the units in which you will work in Maya.
    There are three types of units: linear, angular and time.
    
    The current unit affects how all commands in Maya interpret their numeric
    values. For example, if the current linear unit is cm, then the command:
    
    
    
    move 5 -2 3;
    sphere -radius 4;
    
    
    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
    sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
    per second), then the command:
    
    
    
    currentTime 6;
    
    
    will be interpreted as setting the current time to frame 6 in the Film unit,
    which is 6/24 or 0.25 seconds.
    
    You can always override the unit of a particular numeric value to a command be
    specifying it one the command. For example, using the above examples:
    
    
    
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    
    
    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
    create a sphere of radius 4 inches, and change the current time to 6 frames in
    the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
    unit.

    ---
    - Args:
        - angle (a): Set the current angular unit. Valid strings are:[deg | degree | rad | radian]When queried, returns a string which is the current angular unit
        - linear (l): Set the current linear unit. Valid strings are:[mm | millimeter | cm | centimeter | m | meter | km | kilometer | in | inch | ft | foot | yd | yard | mi | mile]When queried, returns a string which is the current linear unit
        - time (t): Set the current time unit. Valid strings are:[hour | min | sec | millisec | game | film | pal | ntsc | show | palf | ntscf | 23.976fps | 29.97fps | 29.97df | 47.952fps | 59.94fps | 44100fps | 48000fps]When queried, returns a string which is
            the current time unitNote that there is no long form for any of the time units. The non-seconds based time units are interpreted as the following frames per second:game: 15 fpsfilm: 24 fpspal: 25 fpsntsc: 30 fpsshow: 48 fpspalf: 50
            fpsntscf: 60 fps
        - edit (e): Edit mode flag
    """
