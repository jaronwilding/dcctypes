"""Stub files for General category in Maya commands, command: about."""

from typing import Any, overload

@overload #Overload for about in ['create']
def about(apiVersion: bool = ..., application: bool = ..., arm64: bool = ..., batch: bool = ..., buildDirectory: bool = ..., buildVariant: bool = ..., codeset: bool = ..., compositingManager: bool = ..., connected: bool = ..., creativeVersion: bool = ..., ctime: bool = ..., currentDate: bool = ..., currentTime: bool = ..., customVersion: bool = ..., customVersionClient: bool = ..., customVersionMajor: bool = ..., customVersionMinor: bool = ..., customVersionString: bool = ..., cutIdentifier: bool = ..., date: bool = ..., environmentFile: bool = ..., evalVersion: bool = ..., file: bool = ..., fontInfo: bool = ..., helpDataDirectory: bool = ..., installedVersion: bool = ..., ioVersion: bool = ..., irix: bool = ..., is64: bool = ..., languageResources: bool = ..., linux: bool = ..., linux64: bool = ..., liveUpdate: bool = ..., localizedResourceLocation: bool = ..., ltVersion: bool = ..., macOS: bool = ..., macOSASi: bool = ..., macOSppc: bool = ..., macOSx86: bool = ..., majorVersion: bool = ..., minorVersion: bool = ..., ntOS: bool = ..., operatingSystem: bool = ..., operatingSystemVersion: bool = ..., patchVersion: bool = ..., preferences: bool = ..., product: bool = ..., qtVersion: bool = ..., tablet: bool = ..., tabletMode: bool = ..., uiLanguage: bool = ..., uiLanguageForStartup: bool = ..., uiLanguageIsLocalized: bool = ..., uiLocaleLanguage: bool = ..., version: bool = ..., win64: bool = ..., windowManager: bool = ..., windows: bool = ...) -> str:
    """about is undoable, NOT queryable, and NOT editable.
    
    This command displays version information about the application if it is
    executed without flags. If one of the above flags is specified then the
    specified version information is returned.

    ---
    - Args:
        - apiVersion (api): Returns the api version.
        - application (a): Returns the application name string.
        - arm64 (a64): Returns true if the CPU is arm64 based.
        - batch (b): Returns true if application is in batch mode.
        - buildDirectory (bd): Returns the build directory string.
        - buildVariant (bv): Returns the build variant string.
        - codeset (cs): Returns a string identifying the codeset (codepage) of the locale that Maya is running in. Example return values include "UTF-8", "ISO-8859-1", "1252". Note that the codeset values and naming conventions are highly platform dependent.  They
            may differ in format even if they have the same meaning (e.g. "utf8" vs. "UTF-8").
        - compositingManager (cm): On Linux, returns true if there is a compositing manager running; on all other platforms, it always returns true.
        - connected (cnt): Return whether the user is connected or not to the Internet.
        - creativeVersion (cre): Returns true if this is the Maya Creative version of the application.
        - ctime (cti): Returns the current time in the format Wed Jan 02 02:03:55 1980\n\0
        - currentDate (cd): Returns the current date in the format yyyy/mm/dd, e.g. 2003/05/04.
        - currentTime (ct): Returns the current time in the format hh:mm:ss, e.g. 14:27:53.
        - customVersion (cv): Returns true if this is a custom version of Maya.
        - customVersionClient (cvc): Returns the custom client version string for Maya or an empty string if this is not a custom version.
        - customVersionMajor (cvm): Returns the custom major version of Maya or 0 if this is not a custom version.
        - customVersionMinor (cvn): Returns the custom minor version of Maya or 0 if this is not a custom version.
        - customVersionString (cvs): Returns the custom version string for Maya or an empty string if this is not a custom version.
        - cutIdentifier (c): Returns the cut string.
        - date (d): Returns the build date string.
        - environmentFile (env): Returns the location of the application defaults file.
        - evalVersion (ev): This flag is now deprecated. Always returns false, as the eval version is no longer supported.
        - file (f): Returns the file version string.
        - fontInfo (foi): Returns a string of the specifications of the fonts requested, and the specifications of the fonts that are actually being used.
        - helpDataDirectory (hdd): Returns the help data directory.
        - installedVersion (iv): Returns the product version string.
        - ioVersion (io): Returns true if this is the Maya IO version of the application.
        - irix (ir): Returns true if the operating system is Irix. Always false with support for Irix removed.
        - is64 (x64): Returns true if the application is 64 bit.
        - languageResources (lr): Returns a string array of the currently installed language resources. Each string entry consists of three elements delimited with a colon (':'). The first token is the locale code (ISO 639-1 language code followed by ISO 3166-1 country
            code).  The second token is the language name in English. This third token is the alpha-3 code (ISO 639-2).  For example English is represented as "en_US:English:enu".
        - linux (li): Returns true if the operating system is Linux.
        - linux64 (l64): Returns true if the operating system is Linux 64 bit.
        - liveUpdate (lu): This flag is deprecated(2019) and may be removed in future releases of Maya. Returns Autodesk formatted product information.
        - localizedResourceLocation (lrl): Returns the path to the top level of the localized resource directory, if we are running in an alternate language. Returns an empty string if we are running in the default language.
        - ltVersion (lt): Deprecated. Returns true if this is the Maya LT version of the application.
        - macOS (mac): Returns true if the operating system is Macintosh.
        - macOSASi (asi): Returns true if the operating system is an Apple Silicon Mac.
        - macOSppc (ppc): Returns true if the operating system is a PowerPC Macintosh.
        - macOSx86 (x86): Returns true if the operating system is an Intel Macintosh.
        - majorVersion (mjv): Returns the major version of Maya.
        - minorVersion (mnv): Returns the minor version of Maya.
        - ntOS (nt): Returns true if the operating system is Windows.
        - operatingSystem (os): Returns the operating system type. Valid return types are "nt", "win64", "mac", "linux" and "linux64"
        - operatingSystemVersion (osv): Returns the operating system version. on Linux this returns the equivalent of uname -srvm
        - patchVersion (pv): Returns the patch version of Maya.
        - preferences (pd): Returns the location of the preferences directory.
        - product (p): Returns the license product name.
        - qtVersion (qt): Returns Qt version string.
        - tablet (tab): Windows only.  Returns true if the PC is a Tablet PC.
        - tabletMode (tm): Windows 8 (and above) only.  If your device is a Tablet PC, then the convertible mode the device is currently running in.  Returns  either: tablet or laptop (keyboard attached). See thetabletflag.
        - uiLanguage (uil): Returns the language that Maya's running in.  Example return values include "en_US" for English and "ja_JP" for Japanese.
        - uiLanguageForStartup (uis): Returns the language that is used for Maya's next start up. This is read from config file and is rewritten after setting ui language in preference.
        - uiLanguageIsLocalized (uii): Returns true if we are running in an alternate language, not the default (English).
        - uiLocaleLanguage (ull): Returns the language locale of the OS. English is default.
        - version (v): Returns the version string.
        - win64 (w64): Returns true if the operating system is Windows x64 based.
        - windowManager (wm): Returns the name of the Window Manager that is assumed to be running.
        - windows (win): Returns true if the operating system is Windows based.
    """
@overload #Overload for about in ['create']
def about(api: bool = ..., a: bool = ..., a64: bool = ..., b: bool = ..., bd: bool = ..., bv: bool = ..., cs: bool = ..., cm: bool = ..., cnt: bool = ..., cre: bool = ..., cti: bool = ..., cd: bool = ..., ct: bool = ..., cv: bool = ..., cvc: bool = ..., cvm: bool = ..., cvn: bool = ..., cvs: bool = ..., c: bool = ..., d: bool = ..., env: bool = ..., ev: bool = ..., f: bool = ..., foi: bool = ..., hdd: bool = ..., iv: bool = ..., io: bool = ..., ir: bool = ..., x64: bool = ..., lr: bool = ..., li: bool = ..., l64: bool = ..., lu: bool = ..., lrl: bool = ..., lt: bool = ..., mac: bool = ..., asi: bool = ..., ppc: bool = ..., x86: bool = ..., mjv: bool = ..., mnv: bool = ..., nt: bool = ..., os: bool = ..., osv: bool = ..., pv: bool = ..., pd: bool = ..., p: bool = ..., qt: bool = ..., tab: bool = ..., tm: bool = ..., uil: bool = ..., uis: bool = ..., uii: bool = ..., ull: bool = ..., v: bool = ..., w64: bool = ..., wm: bool = ..., win: bool = ...) -> str:
    """about is undoable, NOT queryable, and NOT editable.
    
    This command displays version information about the application if it is
    executed without flags. If one of the above flags is specified then the
    specified version information is returned.

    ---
    - Args:
        - apiVersion (api): Returns the api version.
        - application (a): Returns the application name string.
        - arm64 (a64): Returns true if the CPU is arm64 based.
        - batch (b): Returns true if application is in batch mode.
        - buildDirectory (bd): Returns the build directory string.
        - buildVariant (bv): Returns the build variant string.
        - codeset (cs): Returns a string identifying the codeset (codepage) of the locale that Maya is running in. Example return values include "UTF-8", "ISO-8859-1", "1252". Note that the codeset values and naming conventions are highly platform dependent.  They
            may differ in format even if they have the same meaning (e.g. "utf8" vs. "UTF-8").
        - compositingManager (cm): On Linux, returns true if there is a compositing manager running; on all other platforms, it always returns true.
        - connected (cnt): Return whether the user is connected or not to the Internet.
        - creativeVersion (cre): Returns true if this is the Maya Creative version of the application.
        - ctime (cti): Returns the current time in the format Wed Jan 02 02:03:55 1980\n\0
        - currentDate (cd): Returns the current date in the format yyyy/mm/dd, e.g. 2003/05/04.
        - currentTime (ct): Returns the current time in the format hh:mm:ss, e.g. 14:27:53.
        - customVersion (cv): Returns true if this is a custom version of Maya.
        - customVersionClient (cvc): Returns the custom client version string for Maya or an empty string if this is not a custom version.
        - customVersionMajor (cvm): Returns the custom major version of Maya or 0 if this is not a custom version.
        - customVersionMinor (cvn): Returns the custom minor version of Maya or 0 if this is not a custom version.
        - customVersionString (cvs): Returns the custom version string for Maya or an empty string if this is not a custom version.
        - cutIdentifier (c): Returns the cut string.
        - date (d): Returns the build date string.
        - environmentFile (env): Returns the location of the application defaults file.
        - evalVersion (ev): This flag is now deprecated. Always returns false, as the eval version is no longer supported.
        - file (f): Returns the file version string.
        - fontInfo (foi): Returns a string of the specifications of the fonts requested, and the specifications of the fonts that are actually being used.
        - helpDataDirectory (hdd): Returns the help data directory.
        - installedVersion (iv): Returns the product version string.
        - ioVersion (io): Returns true if this is the Maya IO version of the application.
        - irix (ir): Returns true if the operating system is Irix. Always false with support for Irix removed.
        - is64 (x64): Returns true if the application is 64 bit.
        - languageResources (lr): Returns a string array of the currently installed language resources. Each string entry consists of three elements delimited with a colon (':'). The first token is the locale code (ISO 639-1 language code followed by ISO 3166-1 country
            code).  The second token is the language name in English. This third token is the alpha-3 code (ISO 639-2).  For example English is represented as "en_US:English:enu".
        - linux (li): Returns true if the operating system is Linux.
        - linux64 (l64): Returns true if the operating system is Linux 64 bit.
        - liveUpdate (lu): This flag is deprecated(2019) and may be removed in future releases of Maya. Returns Autodesk formatted product information.
        - localizedResourceLocation (lrl): Returns the path to the top level of the localized resource directory, if we are running in an alternate language. Returns an empty string if we are running in the default language.
        - ltVersion (lt): Deprecated. Returns true if this is the Maya LT version of the application.
        - macOS (mac): Returns true if the operating system is Macintosh.
        - macOSASi (asi): Returns true if the operating system is an Apple Silicon Mac.
        - macOSppc (ppc): Returns true if the operating system is a PowerPC Macintosh.
        - macOSx86 (x86): Returns true if the operating system is an Intel Macintosh.
        - majorVersion (mjv): Returns the major version of Maya.
        - minorVersion (mnv): Returns the minor version of Maya.
        - ntOS (nt): Returns true if the operating system is Windows.
        - operatingSystem (os): Returns the operating system type. Valid return types are "nt", "win64", "mac", "linux" and "linux64"
        - operatingSystemVersion (osv): Returns the operating system version. on Linux this returns the equivalent of uname -srvm
        - patchVersion (pv): Returns the patch version of Maya.
        - preferences (pd): Returns the location of the preferences directory.
        - product (p): Returns the license product name.
        - qtVersion (qt): Returns Qt version string.
        - tablet (tab): Windows only.  Returns true if the PC is a Tablet PC.
        - tabletMode (tm): Windows 8 (and above) only.  If your device is a Tablet PC, then the convertible mode the device is currently running in.  Returns  either: tablet or laptop (keyboard attached). See thetabletflag.
        - uiLanguage (uil): Returns the language that Maya's running in.  Example return values include "en_US" for English and "ja_JP" for Japanese.
        - uiLanguageForStartup (uis): Returns the language that is used for Maya's next start up. This is read from config file and is rewritten after setting ui language in preference.
        - uiLanguageIsLocalized (uii): Returns true if we are running in an alternate language, not the default (English).
        - uiLocaleLanguage (ull): Returns the language locale of the OS. English is default.
        - version (v): Returns the version string.
        - win64 (w64): Returns true if the operating system is Windows x64 based.
        - windowManager (wm): Returns the name of the Window Manager that is assumed to be running.
        - windows (win): Returns true if the operating system is Windows based.
    """
@overload #Overload for about in ['create']
def about(apiVersion: bool = ..., api: bool = ..., application: bool = ..., a: bool = ..., arm64: bool = ..., a64: bool = ..., batch: bool = ..., b: bool = ..., buildDirectory: bool = ..., bd: bool = ..., buildVariant: bool = ..., bv: bool = ..., codeset: bool = ..., cs: bool = ..., compositingManager: bool = ..., cm: bool = ..., connected: bool = ..., cnt: bool = ..., creativeVersion: bool = ..., cre: bool = ..., ctime: bool = ..., cti: bool = ..., currentDate: bool = ..., cd: bool = ..., currentTime: bool = ..., ct: bool = ..., customVersion: bool = ..., cv: bool = ..., customVersionClient: bool = ..., cvc: bool = ..., customVersionMajor: bool = ..., cvm: bool = ..., customVersionMinor: bool = ..., cvn: bool = ..., customVersionString: bool = ..., cvs: bool = ..., cutIdentifier: bool = ..., c: bool = ..., date: bool = ..., d: bool = ..., environmentFile: bool = ..., env: bool = ..., evalVersion: bool = ..., ev: bool = ..., file: bool = ..., f: bool = ..., fontInfo: bool = ..., foi: bool = ..., helpDataDirectory: bool = ..., hdd: bool = ..., installedVersion: bool = ..., iv: bool = ..., ioVersion: bool = ..., io: bool = ..., irix: bool = ..., ir: bool = ..., is64: bool = ..., x64: bool = ..., languageResources: bool = ..., lr: bool = ..., linux: bool = ..., li: bool = ..., linux64: bool = ..., l64: bool = ..., liveUpdate: bool = ..., lu: bool = ..., localizedResourceLocation: bool = ..., lrl: bool = ..., ltVersion: bool = ..., lt: bool = ..., macOS: bool = ..., mac: bool = ..., macOSASi: bool = ..., asi: bool = ..., macOSppc: bool = ..., ppc: bool = ..., macOSx86: bool = ..., x86: bool = ..., majorVersion: bool = ..., mjv: bool = ..., minorVersion: bool = ..., mnv: bool = ..., ntOS: bool = ..., nt: bool = ..., operatingSystem: bool = ..., os: bool = ..., operatingSystemVersion: bool = ..., osv: bool = ..., patchVersion: bool = ..., pv: bool = ..., preferences: bool = ..., pd: bool = ..., product: bool = ..., p: bool = ..., qtVersion: bool = ..., qt: bool = ..., tablet: bool = ..., tab: bool = ..., tabletMode: bool = ..., tm: bool = ..., uiLanguage: bool = ..., uil: bool = ..., uiLanguageForStartup: bool = ..., uis: bool = ..., uiLanguageIsLocalized: bool = ..., uii: bool = ..., uiLocaleLanguage: bool = ..., ull: bool = ..., version: bool = ..., v: bool = ..., win64: bool = ..., w64: bool = ..., windowManager: bool = ..., wm: bool = ..., windows: bool = ..., win: bool = ...) -> str:
    """about is undoable, NOT queryable, and NOT editable.
    
    This command displays version information about the application if it is
    executed without flags. If one of the above flags is specified then the
    specified version information is returned.

    ---
    - Args:
        - apiVersion (api): Returns the api version.
        - application (a): Returns the application name string.
        - arm64 (a64): Returns true if the CPU is arm64 based.
        - batch (b): Returns true if application is in batch mode.
        - buildDirectory (bd): Returns the build directory string.
        - buildVariant (bv): Returns the build variant string.
        - codeset (cs): Returns a string identifying the codeset (codepage) of the locale that Maya is running in. Example return values include "UTF-8", "ISO-8859-1", "1252". Note that the codeset values and naming conventions are highly platform dependent.  They
            may differ in format even if they have the same meaning (e.g. "utf8" vs. "UTF-8").
        - compositingManager (cm): On Linux, returns true if there is a compositing manager running; on all other platforms, it always returns true.
        - connected (cnt): Return whether the user is connected or not to the Internet.
        - creativeVersion (cre): Returns true if this is the Maya Creative version of the application.
        - ctime (cti): Returns the current time in the format Wed Jan 02 02:03:55 1980\n\0
        - currentDate (cd): Returns the current date in the format yyyy/mm/dd, e.g. 2003/05/04.
        - currentTime (ct): Returns the current time in the format hh:mm:ss, e.g. 14:27:53.
        - customVersion (cv): Returns true if this is a custom version of Maya.
        - customVersionClient (cvc): Returns the custom client version string for Maya or an empty string if this is not a custom version.
        - customVersionMajor (cvm): Returns the custom major version of Maya or 0 if this is not a custom version.
        - customVersionMinor (cvn): Returns the custom minor version of Maya or 0 if this is not a custom version.
        - customVersionString (cvs): Returns the custom version string for Maya or an empty string if this is not a custom version.
        - cutIdentifier (c): Returns the cut string.
        - date (d): Returns the build date string.
        - environmentFile (env): Returns the location of the application defaults file.
        - evalVersion (ev): This flag is now deprecated. Always returns false, as the eval version is no longer supported.
        - file (f): Returns the file version string.
        - fontInfo (foi): Returns a string of the specifications of the fonts requested, and the specifications of the fonts that are actually being used.
        - helpDataDirectory (hdd): Returns the help data directory.
        - installedVersion (iv): Returns the product version string.
        - ioVersion (io): Returns true if this is the Maya IO version of the application.
        - irix (ir): Returns true if the operating system is Irix. Always false with support for Irix removed.
        - is64 (x64): Returns true if the application is 64 bit.
        - languageResources (lr): Returns a string array of the currently installed language resources. Each string entry consists of three elements delimited with a colon (':'). The first token is the locale code (ISO 639-1 language code followed by ISO 3166-1 country
            code).  The second token is the language name in English. This third token is the alpha-3 code (ISO 639-2).  For example English is represented as "en_US:English:enu".
        - linux (li): Returns true if the operating system is Linux.
        - linux64 (l64): Returns true if the operating system is Linux 64 bit.
        - liveUpdate (lu): This flag is deprecated(2019) and may be removed in future releases of Maya. Returns Autodesk formatted product information.
        - localizedResourceLocation (lrl): Returns the path to the top level of the localized resource directory, if we are running in an alternate language. Returns an empty string if we are running in the default language.
        - ltVersion (lt): Deprecated. Returns true if this is the Maya LT version of the application.
        - macOS (mac): Returns true if the operating system is Macintosh.
        - macOSASi (asi): Returns true if the operating system is an Apple Silicon Mac.
        - macOSppc (ppc): Returns true if the operating system is a PowerPC Macintosh.
        - macOSx86 (x86): Returns true if the operating system is an Intel Macintosh.
        - majorVersion (mjv): Returns the major version of Maya.
        - minorVersion (mnv): Returns the minor version of Maya.
        - ntOS (nt): Returns true if the operating system is Windows.
        - operatingSystem (os): Returns the operating system type. Valid return types are "nt", "win64", "mac", "linux" and "linux64"
        - operatingSystemVersion (osv): Returns the operating system version. on Linux this returns the equivalent of uname -srvm
        - patchVersion (pv): Returns the patch version of Maya.
        - preferences (pd): Returns the location of the preferences directory.
        - product (p): Returns the license product name.
        - qtVersion (qt): Returns Qt version string.
        - tablet (tab): Windows only.  Returns true if the PC is a Tablet PC.
        - tabletMode (tm): Windows 8 (and above) only.  If your device is a Tablet PC, then the convertible mode the device is currently running in.  Returns  either: tablet or laptop (keyboard attached). See thetabletflag.
        - uiLanguage (uil): Returns the language that Maya's running in.  Example return values include "en_US" for English and "ja_JP" for Japanese.
        - uiLanguageForStartup (uis): Returns the language that is used for Maya's next start up. This is read from config file and is rewritten after setting ui language in preference.
        - uiLanguageIsLocalized (uii): Returns true if we are running in an alternate language, not the default (English).
        - uiLocaleLanguage (ull): Returns the language locale of the OS. English is default.
        - version (v): Returns the version string.
        - win64 (w64): Returns true if the operating system is Windows x64 based.
        - windowManager (wm): Returns the name of the Window Manager that is assumed to be running.
        - windows (win): Returns true if the operating system is Windows based.
    """
