"""Stub files for Display category in Maya commands, command: timeCode."""

from typing import Any, overload

@overload #Overload for timeCode in ['create']
def timeCode(mayaStartFrame: float = ..., productionStartFrame: float = ..., productionStartHour: float = ..., productionStartMinute: float = ..., productionStartSecond: float = ...) -> time:
    """timeCode is undoable, queryable, and editable.
    
    Use this command to query and set the time code information in the file

    ---
    - Args:
        - mayaStartFrame (msf): Sets the Maya start time of the time code, in frames. In query mode, returns the Maya start frame of the time code.
        - productionStartFrame (psf): Sets the production start time of the time code, in terms of frames. In query mode, returns the sub-second frame of production start time.
        - productionStartHour (psh): Sets the production start time of the time code, in terms of hours. In query mode, returns the hour of production start time.
        - productionStartMinute (psm): Sets the production start time of the time code, in terms of minutes. In query mode, returns the minute of production start time.
        - productionStartSecond (pss): Sets the production start time of the time code, in terms of seconds. In query mode, returns the second of production start time.
    """
@overload #Overload for timeCode in ['create']
def timeCode(msf: float = ..., psf: float = ..., psh: float = ..., psm: float = ..., pss: float = ...) -> time:
    """timeCode is undoable, queryable, and editable.
    
    Use this command to query and set the time code information in the file

    ---
    - Args:
        - mayaStartFrame (msf): Sets the Maya start time of the time code, in frames. In query mode, returns the Maya start frame of the time code.
        - productionStartFrame (psf): Sets the production start time of the time code, in terms of frames. In query mode, returns the sub-second frame of production start time.
        - productionStartHour (psh): Sets the production start time of the time code, in terms of hours. In query mode, returns the hour of production start time.
        - productionStartMinute (psm): Sets the production start time of the time code, in terms of minutes. In query mode, returns the minute of production start time.
        - productionStartSecond (pss): Sets the production start time of the time code, in terms of seconds. In query mode, returns the second of production start time.
    """
@overload #Overload for timeCode in ['create']
def timeCode(mayaStartFrame: float = ..., msf: float = ..., productionStartFrame: float = ..., psf: float = ..., productionStartHour: float = ..., psh: float = ..., productionStartMinute: float = ..., psm: float = ..., productionStartSecond: float = ..., pss: float = ...) -> time:
    """timeCode is undoable, queryable, and editable.
    
    Use this command to query and set the time code information in the file

    ---
    - Args:
        - mayaStartFrame (msf): Sets the Maya start time of the time code, in frames. In query mode, returns the Maya start frame of the time code.
        - productionStartFrame (psf): Sets the production start time of the time code, in terms of frames. In query mode, returns the sub-second frame of production start time.
        - productionStartHour (psh): Sets the production start time of the time code, in terms of hours. In query mode, returns the hour of production start time.
        - productionStartMinute (psm): Sets the production start time of the time code, in terms of minutes. In query mode, returns the minute of production start time.
        - productionStartSecond (pss): Sets the production start time of the time code, in terms of seconds. In query mode, returns the second of production start time.
    """
@overload #Overload for timeCode in ['query']
def timeCode(mayaStartFrame: float = ..., productionStartFrame: float = ..., productionStartHour: float = ..., productionStartMinute: float = ..., productionStartSecond: float = ..., query: bool = ...) -> time:
    """timeCode is undoable, queryable, and editable.
    
    Use this command to query and set the time code information in the file

    ---
    - Args:
        - mayaStartFrame (msf): Sets the Maya start time of the time code, in frames. In query mode, returns the Maya start frame of the time code.
        - productionStartFrame (psf): Sets the production start time of the time code, in terms of frames. In query mode, returns the sub-second frame of production start time.
        - productionStartHour (psh): Sets the production start time of the time code, in terms of hours. In query mode, returns the hour of production start time.
        - productionStartMinute (psm): Sets the production start time of the time code, in terms of minutes. In query mode, returns the minute of production start time.
        - productionStartSecond (pss): Sets the production start time of the time code, in terms of seconds. In query mode, returns the second of production start time.
        - query (q): Query mode flag
    """
@overload #Overload for timeCode in ['query']
def timeCode(msf: float = ..., psf: float = ..., psh: float = ..., psm: float = ..., pss: float = ..., q: bool = ...) -> time:
    """timeCode is undoable, queryable, and editable.
    
    Use this command to query and set the time code information in the file

    ---
    - Args:
        - mayaStartFrame (msf): Sets the Maya start time of the time code, in frames. In query mode, returns the Maya start frame of the time code.
        - productionStartFrame (psf): Sets the production start time of the time code, in terms of frames. In query mode, returns the sub-second frame of production start time.
        - productionStartHour (psh): Sets the production start time of the time code, in terms of hours. In query mode, returns the hour of production start time.
        - productionStartMinute (psm): Sets the production start time of the time code, in terms of minutes. In query mode, returns the minute of production start time.
        - productionStartSecond (pss): Sets the production start time of the time code, in terms of seconds. In query mode, returns the second of production start time.
        - query (q): Query mode flag
    """
@overload #Overload for timeCode in ['query']
def timeCode(mayaStartFrame: float = ..., msf: float = ..., productionStartFrame: float = ..., psf: float = ..., productionStartHour: float = ..., psh: float = ..., productionStartMinute: float = ..., psm: float = ..., productionStartSecond: float = ..., pss: float = ..., query: bool = ..., q: bool = ...) -> time:
    """timeCode is undoable, queryable, and editable.
    
    Use this command to query and set the time code information in the file

    ---
    - Args:
        - mayaStartFrame (msf): Sets the Maya start time of the time code, in frames. In query mode, returns the Maya start frame of the time code.
        - productionStartFrame (psf): Sets the production start time of the time code, in terms of frames. In query mode, returns the sub-second frame of production start time.
        - productionStartHour (psh): Sets the production start time of the time code, in terms of hours. In query mode, returns the hour of production start time.
        - productionStartMinute (psm): Sets the production start time of the time code, in terms of minutes. In query mode, returns the minute of production start time.
        - productionStartSecond (pss): Sets the production start time of the time code, in terms of seconds. In query mode, returns the second of production start time.
        - query (q): Query mode flag
    """
@overload #Overload for timeCode in ['edit']
def timeCode(mayaStartFrame: float = ..., productionStartFrame: float = ..., productionStartHour: float = ..., productionStartMinute: float = ..., productionStartSecond: float = ..., edit: bool = ...) -> time:
    """timeCode is undoable, queryable, and editable.
    
    Use this command to query and set the time code information in the file

    ---
    - Args:
        - mayaStartFrame (msf): Sets the Maya start time of the time code, in frames. In query mode, returns the Maya start frame of the time code.
        - productionStartFrame (psf): Sets the production start time of the time code, in terms of frames. In query mode, returns the sub-second frame of production start time.
        - productionStartHour (psh): Sets the production start time of the time code, in terms of hours. In query mode, returns the hour of production start time.
        - productionStartMinute (psm): Sets the production start time of the time code, in terms of minutes. In query mode, returns the minute of production start time.
        - productionStartSecond (pss): Sets the production start time of the time code, in terms of seconds. In query mode, returns the second of production start time.
        - edit (e): Edit mode flag
    """
@overload #Overload for timeCode in ['edit']
def timeCode(msf: float = ..., psf: float = ..., psh: float = ..., psm: float = ..., pss: float = ..., e: bool = ...) -> time:
    """timeCode is undoable, queryable, and editable.
    
    Use this command to query and set the time code information in the file

    ---
    - Args:
        - mayaStartFrame (msf): Sets the Maya start time of the time code, in frames. In query mode, returns the Maya start frame of the time code.
        - productionStartFrame (psf): Sets the production start time of the time code, in terms of frames. In query mode, returns the sub-second frame of production start time.
        - productionStartHour (psh): Sets the production start time of the time code, in terms of hours. In query mode, returns the hour of production start time.
        - productionStartMinute (psm): Sets the production start time of the time code, in terms of minutes. In query mode, returns the minute of production start time.
        - productionStartSecond (pss): Sets the production start time of the time code, in terms of seconds. In query mode, returns the second of production start time.
        - edit (e): Edit mode flag
    """
@overload #Overload for timeCode in ['edit']
def timeCode(mayaStartFrame: float = ..., msf: float = ..., productionStartFrame: float = ..., psf: float = ..., productionStartHour: float = ..., psh: float = ..., productionStartMinute: float = ..., psm: float = ..., productionStartSecond: float = ..., pss: float = ..., edit: bool = ..., e: bool = ...) -> time:
    """timeCode is undoable, queryable, and editable.
    
    Use this command to query and set the time code information in the file

    ---
    - Args:
        - mayaStartFrame (msf): Sets the Maya start time of the time code, in frames. In query mode, returns the Maya start frame of the time code.
        - productionStartFrame (psf): Sets the production start time of the time code, in terms of frames. In query mode, returns the sub-second frame of production start time.
        - productionStartHour (psh): Sets the production start time of the time code, in terms of hours. In query mode, returns the hour of production start time.
        - productionStartMinute (psm): Sets the production start time of the time code, in terms of minutes. In query mode, returns the minute of production start time.
        - productionStartSecond (pss): Sets the production start time of the time code, in terms of seconds. In query mode, returns the second of production start time.
        - edit (e): Edit mode flag
    """
