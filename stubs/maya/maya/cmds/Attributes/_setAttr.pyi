"""Stub files for Attributes category in Maya commands, command: setAttr."""

from typing import Any, overload

@overload #Overload for setAttr in ['create']
def setAttr(attribute Any [Any...]: attribute Any [Any...], alteredValue: bool = ..., caching: bool = ..., capacityHint: int = ..., channelBox: bool = ..., clamp: bool = ..., keyable: bool = ..., lock: bool = ..., size: int = ..., type: str = ...) -> None:
    """setAttr is undoable, queryable, and editable.
    
    Sets the value of a dependency node attribute. No value for the attribute is
    needed when the -l/-k/-s flags are used. The -type flag is only required when
    setting a non-numeric attribute.
    
    For Ufe attributes, the input attribute string should be
    "<ufe_path_string>.<ufe_attribute_name>".
    
    The following chart outlines the syntax of setAttr for non-numeric data types:
    
    * {TYPE} below means any number of values of type TYPE, separated by a space
    * [TYPE] means that the value of type TYPE is optional
    * A|B means that either of A or B may appear
    
    
    In order to run its examples, first execute these commands to create the
    sample attribute types:
    
    
    
    sphere -n node;
    addAttr -ln short2Attr -at short2;
    addAttr -ln short2a -p short2Attr -at short;
    addAttr -ln short2b -p short2Attr -at short;
    addAttr -ln short3Attr -at short3;
    addAttr -ln short3a -p short3Attr -at short;
    addAttr -ln short3b -p short3Attr -at short;
    addAttr -ln short3c -p short3Attr -at short;
    addAttr -ln long2Attr -at long2;
    addAttr -ln long2a -p long2Attr -at long;
    addAttr -ln long2b -p long2Attr -at long;
    addAttr -ln long3Attr -at long3;
    addAttr -ln long3a -p long3Attr -at long;
    addAttr -ln long3b -p long3Attr -at long;
    addAttr -ln long3c -p long3Attr -at long;
    addAttr -ln float2Attr -at float2;
    addAttr -ln float2a -p float2Attr -at "float";
    addAttr -ln float2b -p float2Attr -at "float";
    addAttr -ln float3Attr -at float3;
    addAttr -ln float3a -p float3Attr -at "float";
    addAttr -ln float3b -p float3Attr -at "float";
    addAttr -ln float3c -p float3Attr -at "float";
    addAttr -ln double2Attr -at double2;
    addAttr -ln double2a -p double2Attr -at double;
    addAttr -ln double2b -p double2Attr -at double;
    addAttr -ln double3Attr -at double3;
    addAttr -ln double3a -p double3Attr -at double;
    addAttr -ln double3b -p double3Attr -at double;
    addAttr -ln double3c -p double3Attr -at double;
    addAttr -ln int32ArrayAttr -dt Int32Array;
    addAttr -ln doubleArrayAttr -dt doubleArray;
    addAttr -ln pointArrayAttr -dt pointArray;
    addAttr -ln vectorArrayAttr -dt vectorArray;
    addAttr -ln stringArrayAttr -dt stringArray;
    addAttr -ln stringAttr -dt "string";
    addAttr -ln matrixAttr -dt "matrix";
    addAttr -ln sphereAttr -dt sphere;
    addAttr -ln coneAttr -dt cone;
    addAttr -ln meshAttr -dt mesh;
    addAttr -ln latticeAttr -dt lattice;
    addAttr -ln spectrumRGBAttr -dt spectrumRGB;
    addAttr -ln reflectanceRGBAttr -dt reflectanceRGB;
    addAttr -ln componentListAttr -dt componentList;
    addAttr -ln attrAliasAttr -dt attributeAlias;
    addAttr -ln curveAttr -dt nurbsCurve;
    addAttr -ln surfaceAttr -dt nurbsSurface;
    addAttr -ln trimFaceAttr -dt nurbsTrimface;
    addAttr -ln polyFaceAttr -dt polyFaces;
    
    
    -type short2 |  | Array of two short integers
    ---
    Value Syntax | short short
    Value Meaning | value1 value2
    Mel Example | setAttr node.short2Attr -type short2 1 2;
    Python Example | cmds.setAttr('node.short2Attr',1,2,type='short2')
    
    -type short3 |  | Array of three short integers
    ---
    Value Syntax | short short short
    Value Meaning | value1 value2 value3
    Mel Example | setAttr node.short3Attr -type short3 1 2 3;
    Python Example | cmds.setAttr('node.short3Attr',1,2,3,type='short3')
    
    -type long2 |  | Array of two long integers
    ---
    Value Syntax | long long
    Value Meaning | value1 value2
    Mel Example | setAttr node.long2Attr -type long2 1000000 2000000;
    Python Example | cmds.setAttr('node.long2Attr',1000000,2000000,type='long2')
    
    -type long3 |  | Array of three long integers
    ---
    Value Syntax | long long long
    Value Meaning | value1 value2 value3
    Mel Example | setAttr node.long3Attr -type long3 1000000 2000000 3000000;
    Python Example | cmds.setAttr('node.long3Attr',1000000,2000000,3000000,type='long3')
    
    -type Int32Array |  | Variable length array of long integers
    ---
    Value Syntax | int {int}
    Value Meaning | numberOfArrayValues {arrayValue}
    Mel Example | setAttr node.int32ArrayAttr -type Int32Array 2 12 75;
    Python Example | cmds.setAttr('node.int32ArrayAttr',[2,12,75],type='Int32Array')
    
    -type float2 |  | Array of two floats
    ---
    Value Syntax | float float
    Value Meaning | value1 value2
    Mel Example | setAttr node.float2Attr -type float2 1.1 2.2;
    Python Example | cmds.setAttr('node.float2Attr',1.1,2.2,type='float2')
    
    -type float3 |  | Array of three floats
    ---
    Value Syntax | float float float
    Value Meaning | value1 value2 value3
    Mel Example | setAttr node.float3Attr -type float3 1.1 2.2 3.3;
    Python Example | cmds.setAttr('node.float3Attr',1.1,2.2,3.3,type='float3')
    
    -type double2 |  | Array of two doubles
    ---
    Value Syntax | double double
    Value Meaning | value1 value2
    Mel Example | setAttr node.double2Attr -type double2 1.1 2.2;
    Python Example | cmds.setAttr('node.double2Attr',1.1,2.2,type='double2')
    
    -type double3 |  | Array of three doubles
    ---
    Value Syntax | double double double
    Value Meaning | value1 value2 value3
    Mel Example | setAttr node.double3Attr -type double3 1.1 2.2 3.3;
    Python Example | cmds.setAttr('node.double3Attr',1.1,2.2,3.3,type='double3')
    
    -type doubleArray |  | Variable length array of doubles
    ---
    Value Syntax | int {double}
    Value Meaning | numberOfArrayValues {arrayValue}
    Mel Example | setAttr node.doubleArrayAttr -type doubleArray 2 3.14159 2.782;
    Python Example | cmds.setAttr( "node.doubleArrayAttr", (2, 3.14159, 2.782,), type="doubleArray")
    
    -type matrix |  | 4x4 matrix of doubles
    ---
    Value Syntax | double double double double
    double double double double
    double double double double
    double double double double
    Value Meaning | row1col1 row1col2 row1col3 row1col4
    row2col1 row2col2 row2col3 row2col4
    row3col1 row3col2 row3col3 row3col4
    row4col1 row4col2 row4col3 row4col4
    Alternate Syntax | string double double double
    double double double
    integer
    double double double
    double double double
    double double double
    double double double
    double double double
    double double double
    double double double double
    double double double double
    double double double
    boolean
    Alternate Meaning | "xform" scaleX scaleY scaleZ
    rotateX rotateY rotateZ
    rotationOrder (0=XYZ, 1=YZX, 2=ZXY, 3=XZY, 4=YXZ, 5=ZYX)
    translateX translateY translateZ
    shearXY shearXZ shearYZ
    scalePivotX scalePivotY scalePivotZ
    scaleTranslationX scaleTranslationY scaleTranslationZ
    rotatePivotX rotatePivotY rotatePivotZ
    rotateTranslationX rotateTranslationY rotateTranslationZ
    rotateOrientW rotateOrientX rotateOrientY rotateOrientZ
    jointOrientW jointOrientX jointOrientY jointOrientZ
    inverseParentScaleX inverseParentScaleY inverseParentScaleZ
    compensateForParentScale
    Mel Example | setAttr node.matrixAttr -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2 3 4 1;
    setAttr node.matrixAttr -type "matrix" "xform" 1 1 1 0 0 0 0 2 3 4 0 0 0
    0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 1 0 1 0 1 1 1 0 false;
    Python Example | cmds.setAttr('node.matrixAttr',(1,0,0,0,0,1,0,0,0,0,1,0,2,3,4,1),type='matrix')
    cmds.setAttr('node.matrixAttr','xform',(1,1,1),(0,0,0),0,(2,3,4),(0,0,0),
    (0,0,0),(0,0,0),(0,0,0),(0,1,1),(0,0,1,0),(1,0,1,0),(1,2,3),False,type="matrix")
    
    -type pointArray |  | Variable length array of points
    ---
    Value Syntax | int {double double double double}
    Value Meaning | numberOfArrayValues {xValue yValue zValue wValue}
    Mel Example | setAttr node.pointArrayAttr -type pointArray 2 1 1 1 1 2 2 2 1;
    Python Example | cmds.setAttr('node.pointArrayAttr',2,(1,1,1,1),(2,2,2,1),type='pointArray')
    
    -type vectorArray |  | Variable length array of vectors
    ---
    Value Syntax | int {double double double}
    Value Meaning | numberOfArrayValues {xValue yValue zValue}
    Mel Example | setAttr node.vectorArrayAttr -type vectorArray 2 1 1 1 2 2 2;
    Python Example | cmds.setAttr('node.vectorArrayAttr',2,(1,1,1),(2,2,2),type='vectorArray')
    
    -type "string" |  | Character string
    ---
    Value Syntax | string
    Value Meaning | characterStringValue
    Mel Example | setAttr node.stringAttr -type "string" "blarg";
    Python Example | cmds.setAttr('node.stringAttr',"blarg",type="string")
    
    -type stringArray |  | Variable length array of strings
    ---
    Value Syntax | int {string}
    Value Meaning | numberOfArrayValues {arrayValue}
    Mel Example | setAttr node.stringArrayAttr -type stringArray 3 "a" "b" "c";
    Python Example | cmds.setAttr('node.stringArrayAttr',3,"a","b","c",type='stringArray')
    
    -type sphere |  | Sphere data
    ---
    Value Syntax | double
    Value Meaning | sphereRadius
    Example | setAttr node.sphereAttr -type sphere 5.0;
    
    -type cone |  | Cone data
    ---
    Value Syntax | double double
    Value Meaning | coneAngle coneCap
    Mel Example | setAttr node.coneAttr -type cone 45.0 5.0;
    Python Example | cmds.setAttr('node.coneAttr',45.0,5.0,type='cone')
    
    -type reflectanceRGB |  | Reflectance data
    ---
    Value Syntax | double double double
    Value Meaning | redReflect greenReflect blueReflect
    Mel Example | setAttr node.reflectanceRGBAttr -type reflectanceRGB 0.5 0.5 0.1;
    Python Example | cmds.setAttr('node.reflectanceRGBAttr',0.5,0.5,0.1,type='reflectanceRGB')
    
    -type spectrumRGB |  | Spectrum data
    ---
    Value Syntax | double double double
    Value Meaning | redSpectrum greenSpectrum blueSpectrum
    Mel Example | setAttr node.spectrumRGBAttr -type spectrumRGB 0.5 0.5 0.1;
    Python Example | cmds.setAttr('node.spectrumRGBAttr',0.5,0.5,0.1,type='spectrumRGB')
    
    -type componentList |  | Variable length array of components
    ---
    Value Syntax | int {string}
    Value Meaning | numberOfComponents {componentName}
    Mel Example | setAttr node.componentListAttr -type componentList 3 cv[1] cv[12] cv[3];
    Python Example | cmds.setAttr('node.componentListAttr',3,'cv[1]','cv[12]','cv[3]',type='componentList')
    
    -type attributeAlias |  | String alias data
    ---
    Value Syntax | string string
    Value Meaning | newAlias currentName
    Mel Example | setAttr node.attrAliasAttr -type attributeAlias
    {"GoUp", "translateY", "GoLeft", "translateX"};
    Python Example | cmds.setAttr('node.attrAliasAttr',("GoUp", "translateY",
    "GoLeft", "translateX"),type='attributeAlias')
    
    -type nurbsCurve |  | NURBS curve data
    ---
    Value Syntax | int int int bool int int {double}
    int {double double double}
    Value Meaning | degree spans form isRational dimension knotCount {knotValue}
    cvCount {xCVValue yCVValue [zCVValue] [wCVValue]}
    Mel Example | // degree is the degree of the curve(range 1-7)
    // spans is the number of spans
    // form is open (0), closed (1), periodic (2)
    // isRational is true if the curve CVs contain a rational component
    // dimension is 2 or 3, depending on the dimension of the curve
    // knotCount is the size of the knot list
    // knotValue is a single entry in the knot list
    // cvCount is the number of CVs in the curve
    // xCVValue,yCVValue,[zCVValue] [wCVValue] is a single CV.
    // zCVValue is only present when dimension is 3.
    // wCVValue is only present when isRational is true.
    //
    $curve = `createNode nurbsCurve`;
    setAttr ($curve+".cc") -type nurbsCurve 3 1 0 no 3
    6 0 0 0 1 1 1
    4 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0;
    Python Example | # degree is the degree of the curve(range 1-7)
    # spans is the number of spans
    # form is open (0), closed (1), periodic (2)
    # isRational is true if the curve CVs contain a rational component
    # dimension is 2 or 3, depending on the dimension of the curve
    # knotList is the list of knots
    # next argument is unused and can be set to 0
    # cvCount is the number of CVs in the curve
    # (xCVValue,yCVValue,[zCVValue] [wCVValue]) is a single CV.
    # zCVValue is only present when dimension is 3.
    # wCVValue is only present when isRational is true.
    #
    curve = maya.cmds.createNode("nurbsCurve")
    maya.cmds.setAttr(curve+".cc",
    3, 1, 0, False, 3,
    (0, 0, 0, 1, 1, 1), 0,
    4,
    (-2, 3, 0), (-2, 1, 0), (-2, -1, 0), (-2, -3, 0),
    type="nurbsCurve")
    
    -type nurbsSurface |  | NURBS surface data
    ---
    Value Syntax | int int int int bool
    int {double}
    int {double}
    [string] int {double double double}
    Value Meaning | uDegree vDegree uForm vForm isRational
    uKnotCount {uKnotValue}
    vKnotCount {vKnotValue} ["TRIM"|"NOTRIM"] cvCount {xCVValue yCVValue zCVValue
    [wCVValue]}
    Mel Example | // uDegree is degree of the surface in U direction (range 1-7)
    // vDegree is degree of the surface in V direction (range 1-7)
    // uForm is open (0), closed (1), periodic (2) in U direction
    // vForm is open (0), closed (1), periodic (2) in V direction
    // isRational is true if the surface CVs contain a rational component
    // uKnotCount is the size of the U knot list
    // uKnotValue is a single entry in the U knot list
    // vKnotCount is the size of the V knot list
    // vKnotValue is a single entry in the V knot list
    // If "TRIM" is specified then additional trim information is expected
    // If "NOTRIM" is specified then the surface is not trimmed
    // cvCount is the number of CVs in the surface
    // xCVValue,yCVValue,zCVValue [wCVValue]is a single CV.
    // zCVValue is only present when dimension is 3.
    // wCVValue is only present when isRational is true
    //
    $surface = `createNode nurbsSurface`;
    setAttr ($surface+".cc") -type nurbsSurface 3 3 0 0 no
    6 0 0 0 1 1 1
    6 0 0 0 1 1 1
    16 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0
    -1 3 0 -1 1 0 -1 -1 0 -1 -3 0
    1 3 0 1 1 0 1 -1 0 1 -3 0
    3 3 0 3 1 0 3 -1 0 3 -3 0;
    Python Example | # uDegree is degree of the surface in U direction (range 1-7)
    # vDegree is degree of the surface in V direction (range 1-7)
    # uForm is open (0), closed (1), periodic (2) in U direction
    # vForm is open (0), closed (1), periodic (2) in V direction
    # isRational is true if the surface CVs contain a rational component
    # uKnotList is the list of knots in U
    # next argument is unused and can be set to 0
    # vKnotList is the list of knots in V
    # next argument is unused and can be set to 0
    # If "TRIM" is specified then additional trim information is expected
    # If "NOTRIM" is specified then the surface is not trimmed
    # cvCount is the number of CVs in the surface
    # (xCVValue,yCVValue,zCVValue [wCVValue])is a single CV.
    # zCVValue is only present when dimension is 3.
    # wCVValue is only present when isRational is true
    #
    surface = maya.cmds.createNode("nurbsSurface")
    maya.cmds.setAttr(surface+".cc",
    3, 3, 0, 0, False,
    (0, 0, 0, 1, 1, 1), 0,
    (0, 0, 0, 1, 1, 1), 0,
    16,
    (-2, 3, 0), (-2, 1, 0), (-2, -1, 0), (-2, -3, 0),
    (-1, 3, 0), (-1, 1, 0), (-1, -1, 0), (-1, -3, 0),
    (1, 3, 0), (1, 1, 0), (1, -1, 0), (1, -3, 0),
    (3, 3, 0), (3, 1, 0), (3, -1, 0), (3, -3, 0),
    type="nurbsSurface")
    
    -type nurbsTrimface |  | NURBS trim face data
    ---
    Value Syntax | bool int {int {int {double bool bool} int {bool double}}}
    Value Meaning | flipNormal boundaryCount {boundaryType tedgeCountOnBoundary
    {splineCountOnEdge {edgeTolerance isEdgeReversed geometricContinuity}
    {splineCountOnPedge {isMonotone pedgeTolerance}}}
    Example | // flipNormal if true turns the surface inside out
    // boundaryCount: number of boundaries
    // boundaryType:
    // tedgeCountOnBoundary : number of edges in a boundary
    // splineCountOnEdge : number of splines in an edge in
    // edgeTolerance : tolerance used to build the 3d edge
    // isEdgeReversed : if true, the edge is backwards
    // geometricContinuity : if true, the edge is tangent continuous
    // splineCountOnPedge : number of splines in a 2d edge
    // isMonotone : if true, curvature is monotone
    // pedgeTolerance : tolerance for the 2d edge
    //
    
    
    -type polyFaces |  | Polygon face data
    ---
    Value Syntax | {"f" int {int}}
    {"h" int {int}}
    {"mf" int {int}}
    {"mh" int {int}}
    {"mu" int int {int}}
    {"mc" int int {int}}
    Value Meaning | {"f" faceEdgeCount {edgeIdValue}}
    {"h" holeEdgeCount {edgeIdValue}}
    {"mf" faceUVCount {uvIdValue}}
    {"mh" holeUVCount {uvIdValue}}
    {"mu" uvSet faceUVCount {uvIdValue}}
    {"mc" colorIndex multiColorCount {colorIdValue}}
    
    Example | // This data type (polyFace) is meant to be used in file I/O
    // after setAttrs have been written out for vertex position
    // arrays, edge connectivity arrays (with corresponding start
    // and end vertex descriptions), texture coordinate arrays and
    // color arrays. The reason is that this data type references
    // all of its data through ids created by the former types.
    //
    // "f" specifies the ids of the edges making up a face -
    // negative value if the edge is reversed in the face
    // "h" specifies the ids of the edges making up a hole -
    // negative value if the edge is reversed in the face
    // "mf" specifies the ids of texture coordinates (uvs) for a face.
    // This data type is obsolete as of version 3.0. It is replaced by "mu".
    // "mh" specifies the ids of texture coordinates (uvs) for a hole
    // This data type is obsolete as of version 3.0. It is replaced by "mu".
    // "mu" The first argument refers to the uv set. This is a zero-based
    // integer number. The second argument refers to the number of vertices (n)
    // on the face which have valid uv values. The last n values are the uv
    // ids of the texture coordinates (uvs) for the face. These indices
    // are what used to be represented by the "mf" and "mh" specification.
    // There may be more than one "mu" specification, one for each unique uv set.
    // "mc" specifies the color index values for a face. The first argument
    // is color index. The second argument is the number of color ids to follow.
    // Rest of the arguments are color ids for the face.
    //
    setAttr node.polyFaceAttr -type polyFaces "f" 3 1 2 3 "mc" 0 4 0 1 2 3;
    
    -type mesh |  | Polygonal mesh
    ---
    Value Syntax | {string [int {double double double}]}
    {string [int {double double double}]}
    [{string [int {double double}]}]
    {string [int {double double string}]}
    Value Meaning | "v" [vertexCount {vertexX vertexY vertexZ}]
    "vn" 0
    ["vt" [uvCount {uValue vValue}]]
    "e" [edgeCount {startVertex endVertex "smooth"|"hard"}]
    "face" ["l" edgeLoopCount edgeIndex1...] ]"lt" uvCount uvIndex1...]"
    "face"...
    
    Mel Example | // "v" specifies the vertices of the polygonal mesh
    // "vn"must be set to 0
    // "vt" is optional and specifies a U,V texture coordinate for each vertex
    // "e" specifies the edge connectivity information between vertices
    // "face" specifies face connectivity (edges/UVs) for a single face
    //
    $mesh = `createNode mesh`;
    setAttr ($mesh+".o")
    -type mesh "v" 3 0 0 0 0 1 0 0 0 1
    "vn" 3 1 0 0 1 0 0 1 0 0
    "vt" 3 0 0 0 1 1 0
    "e" 3 0 1 "hard" 1 2 "hard" 2 0 "hard"
    "face" "l" 3 0 1 2 "lt" 3 0 1 2;
    Python Example | # "v" specifies the vertices of the polygonal mesh
    # "vn"must be set to 0
    # "vt" is optional and specifies a U,V texture coordinate for each vertex
    # "e" specifies the edge connectivity information between vertices
    # "face" specifies face connectivity (edges/UVs) for a single face
    #
    mesh = maya.cmds.createNode("mesh")
    maya.cmds.setAttr(mesh+".o",
    "v", 3, (0, 0, 0), (0, 1, 0), (0, 0, 1),
    "vn", 0,
    "vt", 3, (0, 0), (0, 1), (1, 0),
    "e", 3, 0, 1, "hard", 1, 2, "hard", 2, 0, "hard",
    "face", "l", 3, 0, 1, 2, "lt", 3, 0, 1, 2,
    type="mesh")
    
    -type lattice |  | Lattice data
    ---
    Value Syntax | int int int int {double double double}
    Value Meaning | sDivisionCount tDivisionCount uDivisionCount
    pointCount {pointX pointY pointZ}
    Mel Example | // sDivisionCount is the horizontal lattice division count
    // tDivisionCount is the vertical lattice division count
    // uDivisionCount is the depth lattice division count
    // pointCount is the total number of lattice points
    // pointX,pointY,pointZ is one lattice point. The list is
    // specified varying first in S, then in T, last in U so the
    // first two entries are (S=0,T=0,U=0) (s=1,T=0,U=0)
    //
    $lattice = `createNode lattice`;
    setAttr ($lattice+".cc") -type lattice 2 5 2 20
    -2 -2 -2 2 -2 -2 -2 -1 -2 2 -1 -2 -2 0 -2
    2 0 -2 -2 1 -2 2 1 -2 -2 2 -2 2 2 -2
    -2 -2 2 2 -2 2 -2 -1 2 2 -1 2 -2 0 2
    2 0 2 -2 1 2 2 1 2 -2 2 2 2 2 2;
    Python Example | # sDivisionCount is the horizontal lattice division count
    # tDivisionCount is the vertical lattice division count
    # uDivisionCount is the depth lattice division count
    # pointCount is the total number of lattice points
    # (pointX,pointY,pointZ) is one lattice point. The list is
    # specified varying first in S, then in T, last in U so the
    # first two entries are (S=0,T=0,U=0) (s=1,T=0,U=0)
    #
    lattice = maya.cmds.createNode("lattice")
    maya.cmds.setAttr(lattice+".cc",
    2, 5, 2, 20,
    (-2, -2, -2), (2, -2, -2), (-2, -1, -2), (2, -1, -2), (-2, 0, -2),
    (2, 0, -2), (-2, 1, -2), (2, 1, -2), (-2, 2, -2), (2, 2, -2),
    (-2, -2, 2), (2, -2, 2), (-2, -1, 2), (2, -1, 2), (-2, 0, 2),
    (2, 0, 2), (-2, 1, 2), (2, 1, 2), (-2, 2, 2), (2, 2, 2),
    type="lattice")

    Example:
    ```python
        sphere -n node;
        addAttr -ln short2Attr -at short2;
        addAttr -ln short2a -p short2Attr -at short;
        addAttr -ln short2b -p short2Attr -at short;
        addAttr -ln short3Attr -at short3;
        addAttr -ln short3a -p short3Attr -at short;
        addAttr -ln short3b -p short3Attr -at short;
        addAttr -ln short3c -p short3Attr -at short;
        addAttr -ln long2Attr -at long2;
        addAttr -ln long2a -p long2Attr -at long;
        addAttr -ln long2b -p long2Attr -at long;
        addAttr -ln long3Attr -at long3;
        addAttr -ln long3a -p long3Attr -at long;
        addAttr -ln long3b -p long3Attr -at long;
        addAttr -ln long3c -p long3Attr -at long;
        addAttr -ln float2Attr -at float2;
        addAttr -ln float2a -p float2Attr -at "float";
        addAttr -ln float2b -p float2Attr -at "float";
        addAttr -ln float3Attr -at float3;
        addAttr -ln float3a -p float3Attr -at "float";
        addAttr -ln float3b -p float3Attr -at "float";
        addAttr -ln float3c -p float3Attr -at "float";
        addAttr -ln double2Attr -at double2;
        addAttr -ln double2a -p double2Attr -at double;
        addAttr -ln double2b -p double2Attr -at double;
        addAttr -ln double3Attr -at double3;
        addAttr -ln double3a -p double3Attr -at double;
        addAttr -ln double3b -p double3Attr -at double;
        addAttr -ln double3c -p double3Attr -at double;
        addAttr -ln int32ArrayAttr -dt Int32Array;
        addAttr -ln doubleArrayAttr -dt doubleArray;
        addAttr -ln pointArrayAttr -dt pointArray;
        addAttr -ln vectorArrayAttr -dt vectorArray;
        addAttr -ln stringArrayAttr -dt stringArray;
        addAttr -ln stringAttr -dt "string";
        addAttr -ln matrixAttr -dt "matrix";
        addAttr -ln sphereAttr -dt sphere;
        addAttr -ln coneAttr -dt cone;
        addAttr -ln meshAttr -dt mesh;
        addAttr -ln latticeAttr -dt lattice;
        addAttr -ln spectrumRGBAttr -dt spectrumRGB;
        addAttr -ln reflectanceRGBAttr -dt reflectanceRGB;
        addAttr -ln componentListAttr -dt componentList;
        addAttr -ln attrAliasAttr -dt attributeAlias;
        addAttr -ln curveAttr -dt nurbsCurve;
        addAttr -ln surfaceAttr -dt nurbsSurface;
        addAttr -ln trimFaceAttr -dt nurbsTrimface;
        addAttr -ln polyFaceAttr -dt polyFaces;
    ```

    ---
    - Args:
        - attribute Any [Any...]: Input item(s).
        - alteredValue (av): The value is only the current value, which may change in the next evalution (if the attribute has an incoming connection). This flag is only used during file I/O, so that attributes with incoming connections do not have their data
            overwritten during the first evaluation after a file is opened.Not supported for Ufe attributes.
        - caching (ca): Sets the attribute's internal caching on or off. Not all attributes can be defined as caching. Only those attributes that are not defined by default to be cached can be made caching.  As well, multi attribute elements cannot be made
            caching. Caching also affects child attributes for compound attributes.Not supported for Ufe attributes.
        - capacityHint (ch): Used to provide a memory allocation hint to attributes where the -size flag cannot provide enough information. This flag is optional and is primarily intended to be used during file I/O. Only certain attributes make use of this flag, and
            the interpretation of the flag value varies per attribute.Not supported for Ufe attributes.This flag is currently used by (node.attribute):mesh.face - hints the total number of elements in the face edge lists
        - channelBox (cb): Sets the attribute's display in the channelBox on or off. Keyable attributes are always display in the channelBox regardless of the channelBox settting.Not supported for Ufe attributes. The display of Ufe attributes in the Channel Box is
            controlled using thechannelBoxcommand flag-ual/ufeFixedAttrList.
        - clamp (c): For numeric attributes, if the value is outside the range of the attribute, clamp it to the min or max instead of failing.Not supported for Ufe attributes.
        - keyable (k): Sets the attribute's keyable state on or off.Not supported for Ufe attributes.
        - lock (l): Sets the attribute's lock state on or off.
        - size (s): Defines the size of a multi-attribute array. This is only a hint, used to help allocate memory as efficiently as possible.Not supported for Ufe attributes.
        - type (typ): Identifies the type of data.  If the -type flag is not present, a numeric type is assumed.Not supported for Ufe attributes.
    """
@overload #Overload for setAttr in ['create']
def setAttr(attribute Any [Any...]: attribute Any [Any...], av: bool = ..., ca: bool = ..., ch: int = ..., cb: bool = ..., c: bool = ..., k: bool = ..., l: bool = ..., s: int = ..., typ: str = ...) -> None:
    """setAttr is undoable, queryable, and editable.
    
    Sets the value of a dependency node attribute. No value for the attribute is
    needed when the -l/-k/-s flags are used. The -type flag is only required when
    setting a non-numeric attribute.
    
    For Ufe attributes, the input attribute string should be
    "<ufe_path_string>.<ufe_attribute_name>".
    
    The following chart outlines the syntax of setAttr for non-numeric data types:
    
    * {TYPE} below means any number of values of type TYPE, separated by a space
    * [TYPE] means that the value of type TYPE is optional
    * A|B means that either of A or B may appear
    
    
    In order to run its examples, first execute these commands to create the
    sample attribute types:
    
    
    
    sphere -n node;
    addAttr -ln short2Attr -at short2;
    addAttr -ln short2a -p short2Attr -at short;
    addAttr -ln short2b -p short2Attr -at short;
    addAttr -ln short3Attr -at short3;
    addAttr -ln short3a -p short3Attr -at short;
    addAttr -ln short3b -p short3Attr -at short;
    addAttr -ln short3c -p short3Attr -at short;
    addAttr -ln long2Attr -at long2;
    addAttr -ln long2a -p long2Attr -at long;
    addAttr -ln long2b -p long2Attr -at long;
    addAttr -ln long3Attr -at long3;
    addAttr -ln long3a -p long3Attr -at long;
    addAttr -ln long3b -p long3Attr -at long;
    addAttr -ln long3c -p long3Attr -at long;
    addAttr -ln float2Attr -at float2;
    addAttr -ln float2a -p float2Attr -at "float";
    addAttr -ln float2b -p float2Attr -at "float";
    addAttr -ln float3Attr -at float3;
    addAttr -ln float3a -p float3Attr -at "float";
    addAttr -ln float3b -p float3Attr -at "float";
    addAttr -ln float3c -p float3Attr -at "float";
    addAttr -ln double2Attr -at double2;
    addAttr -ln double2a -p double2Attr -at double;
    addAttr -ln double2b -p double2Attr -at double;
    addAttr -ln double3Attr -at double3;
    addAttr -ln double3a -p double3Attr -at double;
    addAttr -ln double3b -p double3Attr -at double;
    addAttr -ln double3c -p double3Attr -at double;
    addAttr -ln int32ArrayAttr -dt Int32Array;
    addAttr -ln doubleArrayAttr -dt doubleArray;
    addAttr -ln pointArrayAttr -dt pointArray;
    addAttr -ln vectorArrayAttr -dt vectorArray;
    addAttr -ln stringArrayAttr -dt stringArray;
    addAttr -ln stringAttr -dt "string";
    addAttr -ln matrixAttr -dt "matrix";
    addAttr -ln sphereAttr -dt sphere;
    addAttr -ln coneAttr -dt cone;
    addAttr -ln meshAttr -dt mesh;
    addAttr -ln latticeAttr -dt lattice;
    addAttr -ln spectrumRGBAttr -dt spectrumRGB;
    addAttr -ln reflectanceRGBAttr -dt reflectanceRGB;
    addAttr -ln componentListAttr -dt componentList;
    addAttr -ln attrAliasAttr -dt attributeAlias;
    addAttr -ln curveAttr -dt nurbsCurve;
    addAttr -ln surfaceAttr -dt nurbsSurface;
    addAttr -ln trimFaceAttr -dt nurbsTrimface;
    addAttr -ln polyFaceAttr -dt polyFaces;
    
    
    -type short2 |  | Array of two short integers
    ---
    Value Syntax | short short
    Value Meaning | value1 value2
    Mel Example | setAttr node.short2Attr -type short2 1 2;
    Python Example | cmds.setAttr('node.short2Attr',1,2,type='short2')
    
    -type short3 |  | Array of three short integers
    ---
    Value Syntax | short short short
    Value Meaning | value1 value2 value3
    Mel Example | setAttr node.short3Attr -type short3 1 2 3;
    Python Example | cmds.setAttr('node.short3Attr',1,2,3,type='short3')
    
    -type long2 |  | Array of two long integers
    ---
    Value Syntax | long long
    Value Meaning | value1 value2
    Mel Example | setAttr node.long2Attr -type long2 1000000 2000000;
    Python Example | cmds.setAttr('node.long2Attr',1000000,2000000,type='long2')
    
    -type long3 |  | Array of three long integers
    ---
    Value Syntax | long long long
    Value Meaning | value1 value2 value3
    Mel Example | setAttr node.long3Attr -type long3 1000000 2000000 3000000;
    Python Example | cmds.setAttr('node.long3Attr',1000000,2000000,3000000,type='long3')
    
    -type Int32Array |  | Variable length array of long integers
    ---
    Value Syntax | int {int}
    Value Meaning | numberOfArrayValues {arrayValue}
    Mel Example | setAttr node.int32ArrayAttr -type Int32Array 2 12 75;
    Python Example | cmds.setAttr('node.int32ArrayAttr',[2,12,75],type='Int32Array')
    
    -type float2 |  | Array of two floats
    ---
    Value Syntax | float float
    Value Meaning | value1 value2
    Mel Example | setAttr node.float2Attr -type float2 1.1 2.2;
    Python Example | cmds.setAttr('node.float2Attr',1.1,2.2,type='float2')
    
    -type float3 |  | Array of three floats
    ---
    Value Syntax | float float float
    Value Meaning | value1 value2 value3
    Mel Example | setAttr node.float3Attr -type float3 1.1 2.2 3.3;
    Python Example | cmds.setAttr('node.float3Attr',1.1,2.2,3.3,type='float3')
    
    -type double2 |  | Array of two doubles
    ---
    Value Syntax | double double
    Value Meaning | value1 value2
    Mel Example | setAttr node.double2Attr -type double2 1.1 2.2;
    Python Example | cmds.setAttr('node.double2Attr',1.1,2.2,type='double2')
    
    -type double3 |  | Array of three doubles
    ---
    Value Syntax | double double double
    Value Meaning | value1 value2 value3
    Mel Example | setAttr node.double3Attr -type double3 1.1 2.2 3.3;
    Python Example | cmds.setAttr('node.double3Attr',1.1,2.2,3.3,type='double3')
    
    -type doubleArray |  | Variable length array of doubles
    ---
    Value Syntax | int {double}
    Value Meaning | numberOfArrayValues {arrayValue}
    Mel Example | setAttr node.doubleArrayAttr -type doubleArray 2 3.14159 2.782;
    Python Example | cmds.setAttr( "node.doubleArrayAttr", (2, 3.14159, 2.782,), type="doubleArray")
    
    -type matrix |  | 4x4 matrix of doubles
    ---
    Value Syntax | double double double double
    double double double double
    double double double double
    double double double double
    Value Meaning | row1col1 row1col2 row1col3 row1col4
    row2col1 row2col2 row2col3 row2col4
    row3col1 row3col2 row3col3 row3col4
    row4col1 row4col2 row4col3 row4col4
    Alternate Syntax | string double double double
    double double double
    integer
    double double double
    double double double
    double double double
    double double double
    double double double
    double double double
    double double double double
    double double double double
    double double double
    boolean
    Alternate Meaning | "xform" scaleX scaleY scaleZ
    rotateX rotateY rotateZ
    rotationOrder (0=XYZ, 1=YZX, 2=ZXY, 3=XZY, 4=YXZ, 5=ZYX)
    translateX translateY translateZ
    shearXY shearXZ shearYZ
    scalePivotX scalePivotY scalePivotZ
    scaleTranslationX scaleTranslationY scaleTranslationZ
    rotatePivotX rotatePivotY rotatePivotZ
    rotateTranslationX rotateTranslationY rotateTranslationZ
    rotateOrientW rotateOrientX rotateOrientY rotateOrientZ
    jointOrientW jointOrientX jointOrientY jointOrientZ
    inverseParentScaleX inverseParentScaleY inverseParentScaleZ
    compensateForParentScale
    Mel Example | setAttr node.matrixAttr -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2 3 4 1;
    setAttr node.matrixAttr -type "matrix" "xform" 1 1 1 0 0 0 0 2 3 4 0 0 0
    0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 1 0 1 0 1 1 1 0 false;
    Python Example | cmds.setAttr('node.matrixAttr',(1,0,0,0,0,1,0,0,0,0,1,0,2,3,4,1),type='matrix')
    cmds.setAttr('node.matrixAttr','xform',(1,1,1),(0,0,0),0,(2,3,4),(0,0,0),
    (0,0,0),(0,0,0),(0,0,0),(0,1,1),(0,0,1,0),(1,0,1,0),(1,2,3),False,type="matrix")
    
    -type pointArray |  | Variable length array of points
    ---
    Value Syntax | int {double double double double}
    Value Meaning | numberOfArrayValues {xValue yValue zValue wValue}
    Mel Example | setAttr node.pointArrayAttr -type pointArray 2 1 1 1 1 2 2 2 1;
    Python Example | cmds.setAttr('node.pointArrayAttr',2,(1,1,1,1),(2,2,2,1),type='pointArray')
    
    -type vectorArray |  | Variable length array of vectors
    ---
    Value Syntax | int {double double double}
    Value Meaning | numberOfArrayValues {xValue yValue zValue}
    Mel Example | setAttr node.vectorArrayAttr -type vectorArray 2 1 1 1 2 2 2;
    Python Example | cmds.setAttr('node.vectorArrayAttr',2,(1,1,1),(2,2,2),type='vectorArray')
    
    -type "string" |  | Character string
    ---
    Value Syntax | string
    Value Meaning | characterStringValue
    Mel Example | setAttr node.stringAttr -type "string" "blarg";
    Python Example | cmds.setAttr('node.stringAttr',"blarg",type="string")
    
    -type stringArray |  | Variable length array of strings
    ---
    Value Syntax | int {string}
    Value Meaning | numberOfArrayValues {arrayValue}
    Mel Example | setAttr node.stringArrayAttr -type stringArray 3 "a" "b" "c";
    Python Example | cmds.setAttr('node.stringArrayAttr',3,"a","b","c",type='stringArray')
    
    -type sphere |  | Sphere data
    ---
    Value Syntax | double
    Value Meaning | sphereRadius
    Example | setAttr node.sphereAttr -type sphere 5.0;
    
    -type cone |  | Cone data
    ---
    Value Syntax | double double
    Value Meaning | coneAngle coneCap
    Mel Example | setAttr node.coneAttr -type cone 45.0 5.0;
    Python Example | cmds.setAttr('node.coneAttr',45.0,5.0,type='cone')
    
    -type reflectanceRGB |  | Reflectance data
    ---
    Value Syntax | double double double
    Value Meaning | redReflect greenReflect blueReflect
    Mel Example | setAttr node.reflectanceRGBAttr -type reflectanceRGB 0.5 0.5 0.1;
    Python Example | cmds.setAttr('node.reflectanceRGBAttr',0.5,0.5,0.1,type='reflectanceRGB')
    
    -type spectrumRGB |  | Spectrum data
    ---
    Value Syntax | double double double
    Value Meaning | redSpectrum greenSpectrum blueSpectrum
    Mel Example | setAttr node.spectrumRGBAttr -type spectrumRGB 0.5 0.5 0.1;
    Python Example | cmds.setAttr('node.spectrumRGBAttr',0.5,0.5,0.1,type='spectrumRGB')
    
    -type componentList |  | Variable length array of components
    ---
    Value Syntax | int {string}
    Value Meaning | numberOfComponents {componentName}
    Mel Example | setAttr node.componentListAttr -type componentList 3 cv[1] cv[12] cv[3];
    Python Example | cmds.setAttr('node.componentListAttr',3,'cv[1]','cv[12]','cv[3]',type='componentList')
    
    -type attributeAlias |  | String alias data
    ---
    Value Syntax | string string
    Value Meaning | newAlias currentName
    Mel Example | setAttr node.attrAliasAttr -type attributeAlias
    {"GoUp", "translateY", "GoLeft", "translateX"};
    Python Example | cmds.setAttr('node.attrAliasAttr',("GoUp", "translateY",
    "GoLeft", "translateX"),type='attributeAlias')
    
    -type nurbsCurve |  | NURBS curve data
    ---
    Value Syntax | int int int bool int int {double}
    int {double double double}
    Value Meaning | degree spans form isRational dimension knotCount {knotValue}
    cvCount {xCVValue yCVValue [zCVValue] [wCVValue]}
    Mel Example | // degree is the degree of the curve(range 1-7)
    // spans is the number of spans
    // form is open (0), closed (1), periodic (2)
    // isRational is true if the curve CVs contain a rational component
    // dimension is 2 or 3, depending on the dimension of the curve
    // knotCount is the size of the knot list
    // knotValue is a single entry in the knot list
    // cvCount is the number of CVs in the curve
    // xCVValue,yCVValue,[zCVValue] [wCVValue] is a single CV.
    // zCVValue is only present when dimension is 3.
    // wCVValue is only present when isRational is true.
    //
    $curve = `createNode nurbsCurve`;
    setAttr ($curve+".cc") -type nurbsCurve 3 1 0 no 3
    6 0 0 0 1 1 1
    4 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0;
    Python Example | # degree is the degree of the curve(range 1-7)
    # spans is the number of spans
    # form is open (0), closed (1), periodic (2)
    # isRational is true if the curve CVs contain a rational component
    # dimension is 2 or 3, depending on the dimension of the curve
    # knotList is the list of knots
    # next argument is unused and can be set to 0
    # cvCount is the number of CVs in the curve
    # (xCVValue,yCVValue,[zCVValue] [wCVValue]) is a single CV.
    # zCVValue is only present when dimension is 3.
    # wCVValue is only present when isRational is true.
    #
    curve = maya.cmds.createNode("nurbsCurve")
    maya.cmds.setAttr(curve+".cc",
    3, 1, 0, False, 3,
    (0, 0, 0, 1, 1, 1), 0,
    4,
    (-2, 3, 0), (-2, 1, 0), (-2, -1, 0), (-2, -3, 0),
    type="nurbsCurve")
    
    -type nurbsSurface |  | NURBS surface data
    ---
    Value Syntax | int int int int bool
    int {double}
    int {double}
    [string] int {double double double}
    Value Meaning | uDegree vDegree uForm vForm isRational
    uKnotCount {uKnotValue}
    vKnotCount {vKnotValue} ["TRIM"|"NOTRIM"] cvCount {xCVValue yCVValue zCVValue
    [wCVValue]}
    Mel Example | // uDegree is degree of the surface in U direction (range 1-7)
    // vDegree is degree of the surface in V direction (range 1-7)
    // uForm is open (0), closed (1), periodic (2) in U direction
    // vForm is open (0), closed (1), periodic (2) in V direction
    // isRational is true if the surface CVs contain a rational component
    // uKnotCount is the size of the U knot list
    // uKnotValue is a single entry in the U knot list
    // vKnotCount is the size of the V knot list
    // vKnotValue is a single entry in the V knot list
    // If "TRIM" is specified then additional trim information is expected
    // If "NOTRIM" is specified then the surface is not trimmed
    // cvCount is the number of CVs in the surface
    // xCVValue,yCVValue,zCVValue [wCVValue]is a single CV.
    // zCVValue is only present when dimension is 3.
    // wCVValue is only present when isRational is true
    //
    $surface = `createNode nurbsSurface`;
    setAttr ($surface+".cc") -type nurbsSurface 3 3 0 0 no
    6 0 0 0 1 1 1
    6 0 0 0 1 1 1
    16 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0
    -1 3 0 -1 1 0 -1 -1 0 -1 -3 0
    1 3 0 1 1 0 1 -1 0 1 -3 0
    3 3 0 3 1 0 3 -1 0 3 -3 0;
    Python Example | # uDegree is degree of the surface in U direction (range 1-7)
    # vDegree is degree of the surface in V direction (range 1-7)
    # uForm is open (0), closed (1), periodic (2) in U direction
    # vForm is open (0), closed (1), periodic (2) in V direction
    # isRational is true if the surface CVs contain a rational component
    # uKnotList is the list of knots in U
    # next argument is unused and can be set to 0
    # vKnotList is the list of knots in V
    # next argument is unused and can be set to 0
    # If "TRIM" is specified then additional trim information is expected
    # If "NOTRIM" is specified then the surface is not trimmed
    # cvCount is the number of CVs in the surface
    # (xCVValue,yCVValue,zCVValue [wCVValue])is a single CV.
    # zCVValue is only present when dimension is 3.
    # wCVValue is only present when isRational is true
    #
    surface = maya.cmds.createNode("nurbsSurface")
    maya.cmds.setAttr(surface+".cc",
    3, 3, 0, 0, False,
    (0, 0, 0, 1, 1, 1), 0,
    (0, 0, 0, 1, 1, 1), 0,
    16,
    (-2, 3, 0), (-2, 1, 0), (-2, -1, 0), (-2, -3, 0),
    (-1, 3, 0), (-1, 1, 0), (-1, -1, 0), (-1, -3, 0),
    (1, 3, 0), (1, 1, 0), (1, -1, 0), (1, -3, 0),
    (3, 3, 0), (3, 1, 0), (3, -1, 0), (3, -3, 0),
    type="nurbsSurface")
    
    -type nurbsTrimface |  | NURBS trim face data
    ---
    Value Syntax | bool int {int {int {double bool bool} int {bool double}}}
    Value Meaning | flipNormal boundaryCount {boundaryType tedgeCountOnBoundary
    {splineCountOnEdge {edgeTolerance isEdgeReversed geometricContinuity}
    {splineCountOnPedge {isMonotone pedgeTolerance}}}
    Example | // flipNormal if true turns the surface inside out
    // boundaryCount: number of boundaries
    // boundaryType:
    // tedgeCountOnBoundary : number of edges in a boundary
    // splineCountOnEdge : number of splines in an edge in
    // edgeTolerance : tolerance used to build the 3d edge
    // isEdgeReversed : if true, the edge is backwards
    // geometricContinuity : if true, the edge is tangent continuous
    // splineCountOnPedge : number of splines in a 2d edge
    // isMonotone : if true, curvature is monotone
    // pedgeTolerance : tolerance for the 2d edge
    //
    
    
    -type polyFaces |  | Polygon face data
    ---
    Value Syntax | {"f" int {int}}
    {"h" int {int}}
    {"mf" int {int}}
    {"mh" int {int}}
    {"mu" int int {int}}
    {"mc" int int {int}}
    Value Meaning | {"f" faceEdgeCount {edgeIdValue}}
    {"h" holeEdgeCount {edgeIdValue}}
    {"mf" faceUVCount {uvIdValue}}
    {"mh" holeUVCount {uvIdValue}}
    {"mu" uvSet faceUVCount {uvIdValue}}
    {"mc" colorIndex multiColorCount {colorIdValue}}
    
    Example | // This data type (polyFace) is meant to be used in file I/O
    // after setAttrs have been written out for vertex position
    // arrays, edge connectivity arrays (with corresponding start
    // and end vertex descriptions), texture coordinate arrays and
    // color arrays. The reason is that this data type references
    // all of its data through ids created by the former types.
    //
    // "f" specifies the ids of the edges making up a face -
    // negative value if the edge is reversed in the face
    // "h" specifies the ids of the edges making up a hole -
    // negative value if the edge is reversed in the face
    // "mf" specifies the ids of texture coordinates (uvs) for a face.
    // This data type is obsolete as of version 3.0. It is replaced by "mu".
    // "mh" specifies the ids of texture coordinates (uvs) for a hole
    // This data type is obsolete as of version 3.0. It is replaced by "mu".
    // "mu" The first argument refers to the uv set. This is a zero-based
    // integer number. The second argument refers to the number of vertices (n)
    // on the face which have valid uv values. The last n values are the uv
    // ids of the texture coordinates (uvs) for the face. These indices
    // are what used to be represented by the "mf" and "mh" specification.
    // There may be more than one "mu" specification, one for each unique uv set.
    // "mc" specifies the color index values for a face. The first argument
    // is color index. The second argument is the number of color ids to follow.
    // Rest of the arguments are color ids for the face.
    //
    setAttr node.polyFaceAttr -type polyFaces "f" 3 1 2 3 "mc" 0 4 0 1 2 3;
    
    -type mesh |  | Polygonal mesh
    ---
    Value Syntax | {string [int {double double double}]}
    {string [int {double double double}]}
    [{string [int {double double}]}]
    {string [int {double double string}]}
    Value Meaning | "v" [vertexCount {vertexX vertexY vertexZ}]
    "vn" 0
    ["vt" [uvCount {uValue vValue}]]
    "e" [edgeCount {startVertex endVertex "smooth"|"hard"}]
    "face" ["l" edgeLoopCount edgeIndex1...] ]"lt" uvCount uvIndex1...]"
    "face"...
    
    Mel Example | // "v" specifies the vertices of the polygonal mesh
    // "vn"must be set to 0
    // "vt" is optional and specifies a U,V texture coordinate for each vertex
    // "e" specifies the edge connectivity information between vertices
    // "face" specifies face connectivity (edges/UVs) for a single face
    //
    $mesh = `createNode mesh`;
    setAttr ($mesh+".o")
    -type mesh "v" 3 0 0 0 0 1 0 0 0 1
    "vn" 3 1 0 0 1 0 0 1 0 0
    "vt" 3 0 0 0 1 1 0
    "e" 3 0 1 "hard" 1 2 "hard" 2 0 "hard"
    "face" "l" 3 0 1 2 "lt" 3 0 1 2;
    Python Example | # "v" specifies the vertices of the polygonal mesh
    # "vn"must be set to 0
    # "vt" is optional and specifies a U,V texture coordinate for each vertex
    # "e" specifies the edge connectivity information between vertices
    # "face" specifies face connectivity (edges/UVs) for a single face
    #
    mesh = maya.cmds.createNode("mesh")
    maya.cmds.setAttr(mesh+".o",
    "v", 3, (0, 0, 0), (0, 1, 0), (0, 0, 1),
    "vn", 0,
    "vt", 3, (0, 0), (0, 1), (1, 0),
    "e", 3, 0, 1, "hard", 1, 2, "hard", 2, 0, "hard",
    "face", "l", 3, 0, 1, 2, "lt", 3, 0, 1, 2,
    type="mesh")
    
    -type lattice |  | Lattice data
    ---
    Value Syntax | int int int int {double double double}
    Value Meaning | sDivisionCount tDivisionCount uDivisionCount
    pointCount {pointX pointY pointZ}
    Mel Example | // sDivisionCount is the horizontal lattice division count
    // tDivisionCount is the vertical lattice division count
    // uDivisionCount is the depth lattice division count
    // pointCount is the total number of lattice points
    // pointX,pointY,pointZ is one lattice point. The list is
    // specified varying first in S, then in T, last in U so the
    // first two entries are (S=0,T=0,U=0) (s=1,T=0,U=0)
    //
    $lattice = `createNode lattice`;
    setAttr ($lattice+".cc") -type lattice 2 5 2 20
    -2 -2 -2 2 -2 -2 -2 -1 -2 2 -1 -2 -2 0 -2
    2 0 -2 -2 1 -2 2 1 -2 -2 2 -2 2 2 -2
    -2 -2 2 2 -2 2 -2 -1 2 2 -1 2 -2 0 2
    2 0 2 -2 1 2 2 1 2 -2 2 2 2 2 2;
    Python Example | # sDivisionCount is the horizontal lattice division count
    # tDivisionCount is the vertical lattice division count
    # uDivisionCount is the depth lattice division count
    # pointCount is the total number of lattice points
    # (pointX,pointY,pointZ) is one lattice point. The list is
    # specified varying first in S, then in T, last in U so the
    # first two entries are (S=0,T=0,U=0) (s=1,T=0,U=0)
    #
    lattice = maya.cmds.createNode("lattice")
    maya.cmds.setAttr(lattice+".cc",
    2, 5, 2, 20,
    (-2, -2, -2), (2, -2, -2), (-2, -1, -2), (2, -1, -2), (-2, 0, -2),
    (2, 0, -2), (-2, 1, -2), (2, 1, -2), (-2, 2, -2), (2, 2, -2),
    (-2, -2, 2), (2, -2, 2), (-2, -1, 2), (2, -1, 2), (-2, 0, 2),
    (2, 0, 2), (-2, 1, 2), (2, 1, 2), (-2, 2, 2), (2, 2, 2),
    type="lattice")

    Example:
    ```python
        sphere -n node;
        addAttr -ln short2Attr -at short2;
        addAttr -ln short2a -p short2Attr -at short;
        addAttr -ln short2b -p short2Attr -at short;
        addAttr -ln short3Attr -at short3;
        addAttr -ln short3a -p short3Attr -at short;
        addAttr -ln short3b -p short3Attr -at short;
        addAttr -ln short3c -p short3Attr -at short;
        addAttr -ln long2Attr -at long2;
        addAttr -ln long2a -p long2Attr -at long;
        addAttr -ln long2b -p long2Attr -at long;
        addAttr -ln long3Attr -at long3;
        addAttr -ln long3a -p long3Attr -at long;
        addAttr -ln long3b -p long3Attr -at long;
        addAttr -ln long3c -p long3Attr -at long;
        addAttr -ln float2Attr -at float2;
        addAttr -ln float2a -p float2Attr -at "float";
        addAttr -ln float2b -p float2Attr -at "float";
        addAttr -ln float3Attr -at float3;
        addAttr -ln float3a -p float3Attr -at "float";
        addAttr -ln float3b -p float3Attr -at "float";
        addAttr -ln float3c -p float3Attr -at "float";
        addAttr -ln double2Attr -at double2;
        addAttr -ln double2a -p double2Attr -at double;
        addAttr -ln double2b -p double2Attr -at double;
        addAttr -ln double3Attr -at double3;
        addAttr -ln double3a -p double3Attr -at double;
        addAttr -ln double3b -p double3Attr -at double;
        addAttr -ln double3c -p double3Attr -at double;
        addAttr -ln int32ArrayAttr -dt Int32Array;
        addAttr -ln doubleArrayAttr -dt doubleArray;
        addAttr -ln pointArrayAttr -dt pointArray;
        addAttr -ln vectorArrayAttr -dt vectorArray;
        addAttr -ln stringArrayAttr -dt stringArray;
        addAttr -ln stringAttr -dt "string";
        addAttr -ln matrixAttr -dt "matrix";
        addAttr -ln sphereAttr -dt sphere;
        addAttr -ln coneAttr -dt cone;
        addAttr -ln meshAttr -dt mesh;
        addAttr -ln latticeAttr -dt lattice;
        addAttr -ln spectrumRGBAttr -dt spectrumRGB;
        addAttr -ln reflectanceRGBAttr -dt reflectanceRGB;
        addAttr -ln componentListAttr -dt componentList;
        addAttr -ln attrAliasAttr -dt attributeAlias;
        addAttr -ln curveAttr -dt nurbsCurve;
        addAttr -ln surfaceAttr -dt nurbsSurface;
        addAttr -ln trimFaceAttr -dt nurbsTrimface;
        addAttr -ln polyFaceAttr -dt polyFaces;
    ```

    ---
    - Args:
        - attribute Any [Any...]: Input item(s).
        - alteredValue (av): The value is only the current value, which may change in the next evalution (if the attribute has an incoming connection). This flag is only used during file I/O, so that attributes with incoming connections do not have their data
            overwritten during the first evaluation after a file is opened.Not supported for Ufe attributes.
        - caching (ca): Sets the attribute's internal caching on or off. Not all attributes can be defined as caching. Only those attributes that are not defined by default to be cached can be made caching.  As well, multi attribute elements cannot be made
            caching. Caching also affects child attributes for compound attributes.Not supported for Ufe attributes.
        - capacityHint (ch): Used to provide a memory allocation hint to attributes where the -size flag cannot provide enough information. This flag is optional and is primarily intended to be used during file I/O. Only certain attributes make use of this flag, and
            the interpretation of the flag value varies per attribute.Not supported for Ufe attributes.This flag is currently used by (node.attribute):mesh.face - hints the total number of elements in the face edge lists
        - channelBox (cb): Sets the attribute's display in the channelBox on or off. Keyable attributes are always display in the channelBox regardless of the channelBox settting.Not supported for Ufe attributes. The display of Ufe attributes in the Channel Box is
            controlled using thechannelBoxcommand flag-ual/ufeFixedAttrList.
        - clamp (c): For numeric attributes, if the value is outside the range of the attribute, clamp it to the min or max instead of failing.Not supported for Ufe attributes.
        - keyable (k): Sets the attribute's keyable state on or off.Not supported for Ufe attributes.
        - lock (l): Sets the attribute's lock state on or off.
        - size (s): Defines the size of a multi-attribute array. This is only a hint, used to help allocate memory as efficiently as possible.Not supported for Ufe attributes.
        - type (typ): Identifies the type of data.  If the -type flag is not present, a numeric type is assumed.Not supported for Ufe attributes.
    """
@overload #Overload for setAttr in ['create']
def setAttr(attribute Any [Any...]: attribute Any [Any...], alteredValue: bool = ..., av: bool = ..., caching: bool = ..., ca: bool = ..., capacityHint: int = ..., ch: int = ..., channelBox: bool = ..., cb: bool = ..., clamp: bool = ..., c: bool = ..., keyable: bool = ..., k: bool = ..., lock: bool = ..., l: bool = ..., size: int = ..., s: int = ..., type: str = ..., typ: str = ...) -> None:
    """setAttr is undoable, queryable, and editable.
    
    Sets the value of a dependency node attribute. No value for the attribute is
    needed when the -l/-k/-s flags are used. The -type flag is only required when
    setting a non-numeric attribute.
    
    For Ufe attributes, the input attribute string should be
    "<ufe_path_string>.<ufe_attribute_name>".
    
    The following chart outlines the syntax of setAttr for non-numeric data types:
    
    * {TYPE} below means any number of values of type TYPE, separated by a space
    * [TYPE] means that the value of type TYPE is optional
    * A|B means that either of A or B may appear
    
    
    In order to run its examples, first execute these commands to create the
    sample attribute types:
    
    
    
    sphere -n node;
    addAttr -ln short2Attr -at short2;
    addAttr -ln short2a -p short2Attr -at short;
    addAttr -ln short2b -p short2Attr -at short;
    addAttr -ln short3Attr -at short3;
    addAttr -ln short3a -p short3Attr -at short;
    addAttr -ln short3b -p short3Attr -at short;
    addAttr -ln short3c -p short3Attr -at short;
    addAttr -ln long2Attr -at long2;
    addAttr -ln long2a -p long2Attr -at long;
    addAttr -ln long2b -p long2Attr -at long;
    addAttr -ln long3Attr -at long3;
    addAttr -ln long3a -p long3Attr -at long;
    addAttr -ln long3b -p long3Attr -at long;
    addAttr -ln long3c -p long3Attr -at long;
    addAttr -ln float2Attr -at float2;
    addAttr -ln float2a -p float2Attr -at "float";
    addAttr -ln float2b -p float2Attr -at "float";
    addAttr -ln float3Attr -at float3;
    addAttr -ln float3a -p float3Attr -at "float";
    addAttr -ln float3b -p float3Attr -at "float";
    addAttr -ln float3c -p float3Attr -at "float";
    addAttr -ln double2Attr -at double2;
    addAttr -ln double2a -p double2Attr -at double;
    addAttr -ln double2b -p double2Attr -at double;
    addAttr -ln double3Attr -at double3;
    addAttr -ln double3a -p double3Attr -at double;
    addAttr -ln double3b -p double3Attr -at double;
    addAttr -ln double3c -p double3Attr -at double;
    addAttr -ln int32ArrayAttr -dt Int32Array;
    addAttr -ln doubleArrayAttr -dt doubleArray;
    addAttr -ln pointArrayAttr -dt pointArray;
    addAttr -ln vectorArrayAttr -dt vectorArray;
    addAttr -ln stringArrayAttr -dt stringArray;
    addAttr -ln stringAttr -dt "string";
    addAttr -ln matrixAttr -dt "matrix";
    addAttr -ln sphereAttr -dt sphere;
    addAttr -ln coneAttr -dt cone;
    addAttr -ln meshAttr -dt mesh;
    addAttr -ln latticeAttr -dt lattice;
    addAttr -ln spectrumRGBAttr -dt spectrumRGB;
    addAttr -ln reflectanceRGBAttr -dt reflectanceRGB;
    addAttr -ln componentListAttr -dt componentList;
    addAttr -ln attrAliasAttr -dt attributeAlias;
    addAttr -ln curveAttr -dt nurbsCurve;
    addAttr -ln surfaceAttr -dt nurbsSurface;
    addAttr -ln trimFaceAttr -dt nurbsTrimface;
    addAttr -ln polyFaceAttr -dt polyFaces;
    
    
    -type short2 |  | Array of two short integers
    ---
    Value Syntax | short short
    Value Meaning | value1 value2
    Mel Example | setAttr node.short2Attr -type short2 1 2;
    Python Example | cmds.setAttr('node.short2Attr',1,2,type='short2')
    
    -type short3 |  | Array of three short integers
    ---
    Value Syntax | short short short
    Value Meaning | value1 value2 value3
    Mel Example | setAttr node.short3Attr -type short3 1 2 3;
    Python Example | cmds.setAttr('node.short3Attr',1,2,3,type='short3')
    
    -type long2 |  | Array of two long integers
    ---
    Value Syntax | long long
    Value Meaning | value1 value2
    Mel Example | setAttr node.long2Attr -type long2 1000000 2000000;
    Python Example | cmds.setAttr('node.long2Attr',1000000,2000000,type='long2')
    
    -type long3 |  | Array of three long integers
    ---
    Value Syntax | long long long
    Value Meaning | value1 value2 value3
    Mel Example | setAttr node.long3Attr -type long3 1000000 2000000 3000000;
    Python Example | cmds.setAttr('node.long3Attr',1000000,2000000,3000000,type='long3')
    
    -type Int32Array |  | Variable length array of long integers
    ---
    Value Syntax | int {int}
    Value Meaning | numberOfArrayValues {arrayValue}
    Mel Example | setAttr node.int32ArrayAttr -type Int32Array 2 12 75;
    Python Example | cmds.setAttr('node.int32ArrayAttr',[2,12,75],type='Int32Array')
    
    -type float2 |  | Array of two floats
    ---
    Value Syntax | float float
    Value Meaning | value1 value2
    Mel Example | setAttr node.float2Attr -type float2 1.1 2.2;
    Python Example | cmds.setAttr('node.float2Attr',1.1,2.2,type='float2')
    
    -type float3 |  | Array of three floats
    ---
    Value Syntax | float float float
    Value Meaning | value1 value2 value3
    Mel Example | setAttr node.float3Attr -type float3 1.1 2.2 3.3;
    Python Example | cmds.setAttr('node.float3Attr',1.1,2.2,3.3,type='float3')
    
    -type double2 |  | Array of two doubles
    ---
    Value Syntax | double double
    Value Meaning | value1 value2
    Mel Example | setAttr node.double2Attr -type double2 1.1 2.2;
    Python Example | cmds.setAttr('node.double2Attr',1.1,2.2,type='double2')
    
    -type double3 |  | Array of three doubles
    ---
    Value Syntax | double double double
    Value Meaning | value1 value2 value3
    Mel Example | setAttr node.double3Attr -type double3 1.1 2.2 3.3;
    Python Example | cmds.setAttr('node.double3Attr',1.1,2.2,3.3,type='double3')
    
    -type doubleArray |  | Variable length array of doubles
    ---
    Value Syntax | int {double}
    Value Meaning | numberOfArrayValues {arrayValue}
    Mel Example | setAttr node.doubleArrayAttr -type doubleArray 2 3.14159 2.782;
    Python Example | cmds.setAttr( "node.doubleArrayAttr", (2, 3.14159, 2.782,), type="doubleArray")
    
    -type matrix |  | 4x4 matrix of doubles
    ---
    Value Syntax | double double double double
    double double double double
    double double double double
    double double double double
    Value Meaning | row1col1 row1col2 row1col3 row1col4
    row2col1 row2col2 row2col3 row2col4
    row3col1 row3col2 row3col3 row3col4
    row4col1 row4col2 row4col3 row4col4
    Alternate Syntax | string double double double
    double double double
    integer
    double double double
    double double double
    double double double
    double double double
    double double double
    double double double
    double double double double
    double double double double
    double double double
    boolean
    Alternate Meaning | "xform" scaleX scaleY scaleZ
    rotateX rotateY rotateZ
    rotationOrder (0=XYZ, 1=YZX, 2=ZXY, 3=XZY, 4=YXZ, 5=ZYX)
    translateX translateY translateZ
    shearXY shearXZ shearYZ
    scalePivotX scalePivotY scalePivotZ
    scaleTranslationX scaleTranslationY scaleTranslationZ
    rotatePivotX rotatePivotY rotatePivotZ
    rotateTranslationX rotateTranslationY rotateTranslationZ
    rotateOrientW rotateOrientX rotateOrientY rotateOrientZ
    jointOrientW jointOrientX jointOrientY jointOrientZ
    inverseParentScaleX inverseParentScaleY inverseParentScaleZ
    compensateForParentScale
    Mel Example | setAttr node.matrixAttr -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2 3 4 1;
    setAttr node.matrixAttr -type "matrix" "xform" 1 1 1 0 0 0 0 2 3 4 0 0 0
    0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 1 0 1 0 1 1 1 0 false;
    Python Example | cmds.setAttr('node.matrixAttr',(1,0,0,0,0,1,0,0,0,0,1,0,2,3,4,1),type='matrix')
    cmds.setAttr('node.matrixAttr','xform',(1,1,1),(0,0,0),0,(2,3,4),(0,0,0),
    (0,0,0),(0,0,0),(0,0,0),(0,1,1),(0,0,1,0),(1,0,1,0),(1,2,3),False,type="matrix")
    
    -type pointArray |  | Variable length array of points
    ---
    Value Syntax | int {double double double double}
    Value Meaning | numberOfArrayValues {xValue yValue zValue wValue}
    Mel Example | setAttr node.pointArrayAttr -type pointArray 2 1 1 1 1 2 2 2 1;
    Python Example | cmds.setAttr('node.pointArrayAttr',2,(1,1,1,1),(2,2,2,1),type='pointArray')
    
    -type vectorArray |  | Variable length array of vectors
    ---
    Value Syntax | int {double double double}
    Value Meaning | numberOfArrayValues {xValue yValue zValue}
    Mel Example | setAttr node.vectorArrayAttr -type vectorArray 2 1 1 1 2 2 2;
    Python Example | cmds.setAttr('node.vectorArrayAttr',2,(1,1,1),(2,2,2),type='vectorArray')
    
    -type "string" |  | Character string
    ---
    Value Syntax | string
    Value Meaning | characterStringValue
    Mel Example | setAttr node.stringAttr -type "string" "blarg";
    Python Example | cmds.setAttr('node.stringAttr',"blarg",type="string")
    
    -type stringArray |  | Variable length array of strings
    ---
    Value Syntax | int {string}
    Value Meaning | numberOfArrayValues {arrayValue}
    Mel Example | setAttr node.stringArrayAttr -type stringArray 3 "a" "b" "c";
    Python Example | cmds.setAttr('node.stringArrayAttr',3,"a","b","c",type='stringArray')
    
    -type sphere |  | Sphere data
    ---
    Value Syntax | double
    Value Meaning | sphereRadius
    Example | setAttr node.sphereAttr -type sphere 5.0;
    
    -type cone |  | Cone data
    ---
    Value Syntax | double double
    Value Meaning | coneAngle coneCap
    Mel Example | setAttr node.coneAttr -type cone 45.0 5.0;
    Python Example | cmds.setAttr('node.coneAttr',45.0,5.0,type='cone')
    
    -type reflectanceRGB |  | Reflectance data
    ---
    Value Syntax | double double double
    Value Meaning | redReflect greenReflect blueReflect
    Mel Example | setAttr node.reflectanceRGBAttr -type reflectanceRGB 0.5 0.5 0.1;
    Python Example | cmds.setAttr('node.reflectanceRGBAttr',0.5,0.5,0.1,type='reflectanceRGB')
    
    -type spectrumRGB |  | Spectrum data
    ---
    Value Syntax | double double double
    Value Meaning | redSpectrum greenSpectrum blueSpectrum
    Mel Example | setAttr node.spectrumRGBAttr -type spectrumRGB 0.5 0.5 0.1;
    Python Example | cmds.setAttr('node.spectrumRGBAttr',0.5,0.5,0.1,type='spectrumRGB')
    
    -type componentList |  | Variable length array of components
    ---
    Value Syntax | int {string}
    Value Meaning | numberOfComponents {componentName}
    Mel Example | setAttr node.componentListAttr -type componentList 3 cv[1] cv[12] cv[3];
    Python Example | cmds.setAttr('node.componentListAttr',3,'cv[1]','cv[12]','cv[3]',type='componentList')
    
    -type attributeAlias |  | String alias data
    ---
    Value Syntax | string string
    Value Meaning | newAlias currentName
    Mel Example | setAttr node.attrAliasAttr -type attributeAlias
    {"GoUp", "translateY", "GoLeft", "translateX"};
    Python Example | cmds.setAttr('node.attrAliasAttr',("GoUp", "translateY",
    "GoLeft", "translateX"),type='attributeAlias')
    
    -type nurbsCurve |  | NURBS curve data
    ---
    Value Syntax | int int int bool int int {double}
    int {double double double}
    Value Meaning | degree spans form isRational dimension knotCount {knotValue}
    cvCount {xCVValue yCVValue [zCVValue] [wCVValue]}
    Mel Example | // degree is the degree of the curve(range 1-7)
    // spans is the number of spans
    // form is open (0), closed (1), periodic (2)
    // isRational is true if the curve CVs contain a rational component
    // dimension is 2 or 3, depending on the dimension of the curve
    // knotCount is the size of the knot list
    // knotValue is a single entry in the knot list
    // cvCount is the number of CVs in the curve
    // xCVValue,yCVValue,[zCVValue] [wCVValue] is a single CV.
    // zCVValue is only present when dimension is 3.
    // wCVValue is only present when isRational is true.
    //
    $curve = `createNode nurbsCurve`;
    setAttr ($curve+".cc") -type nurbsCurve 3 1 0 no 3
    6 0 0 0 1 1 1
    4 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0;
    Python Example | # degree is the degree of the curve(range 1-7)
    # spans is the number of spans
    # form is open (0), closed (1), periodic (2)
    # isRational is true if the curve CVs contain a rational component
    # dimension is 2 or 3, depending on the dimension of the curve
    # knotList is the list of knots
    # next argument is unused and can be set to 0
    # cvCount is the number of CVs in the curve
    # (xCVValue,yCVValue,[zCVValue] [wCVValue]) is a single CV.
    # zCVValue is only present when dimension is 3.
    # wCVValue is only present when isRational is true.
    #
    curve = maya.cmds.createNode("nurbsCurve")
    maya.cmds.setAttr(curve+".cc",
    3, 1, 0, False, 3,
    (0, 0, 0, 1, 1, 1), 0,
    4,
    (-2, 3, 0), (-2, 1, 0), (-2, -1, 0), (-2, -3, 0),
    type="nurbsCurve")
    
    -type nurbsSurface |  | NURBS surface data
    ---
    Value Syntax | int int int int bool
    int {double}
    int {double}
    [string] int {double double double}
    Value Meaning | uDegree vDegree uForm vForm isRational
    uKnotCount {uKnotValue}
    vKnotCount {vKnotValue} ["TRIM"|"NOTRIM"] cvCount {xCVValue yCVValue zCVValue
    [wCVValue]}
    Mel Example | // uDegree is degree of the surface in U direction (range 1-7)
    // vDegree is degree of the surface in V direction (range 1-7)
    // uForm is open (0), closed (1), periodic (2) in U direction
    // vForm is open (0), closed (1), periodic (2) in V direction
    // isRational is true if the surface CVs contain a rational component
    // uKnotCount is the size of the U knot list
    // uKnotValue is a single entry in the U knot list
    // vKnotCount is the size of the V knot list
    // vKnotValue is a single entry in the V knot list
    // If "TRIM" is specified then additional trim information is expected
    // If "NOTRIM" is specified then the surface is not trimmed
    // cvCount is the number of CVs in the surface
    // xCVValue,yCVValue,zCVValue [wCVValue]is a single CV.
    // zCVValue is only present when dimension is 3.
    // wCVValue is only present when isRational is true
    //
    $surface = `createNode nurbsSurface`;
    setAttr ($surface+".cc") -type nurbsSurface 3 3 0 0 no
    6 0 0 0 1 1 1
    6 0 0 0 1 1 1
    16 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0
    -1 3 0 -1 1 0 -1 -1 0 -1 -3 0
    1 3 0 1 1 0 1 -1 0 1 -3 0
    3 3 0 3 1 0 3 -1 0 3 -3 0;
    Python Example | # uDegree is degree of the surface in U direction (range 1-7)
    # vDegree is degree of the surface in V direction (range 1-7)
    # uForm is open (0), closed (1), periodic (2) in U direction
    # vForm is open (0), closed (1), periodic (2) in V direction
    # isRational is true if the surface CVs contain a rational component
    # uKnotList is the list of knots in U
    # next argument is unused and can be set to 0
    # vKnotList is the list of knots in V
    # next argument is unused and can be set to 0
    # If "TRIM" is specified then additional trim information is expected
    # If "NOTRIM" is specified then the surface is not trimmed
    # cvCount is the number of CVs in the surface
    # (xCVValue,yCVValue,zCVValue [wCVValue])is a single CV.
    # zCVValue is only present when dimension is 3.
    # wCVValue is only present when isRational is true
    #
    surface = maya.cmds.createNode("nurbsSurface")
    maya.cmds.setAttr(surface+".cc",
    3, 3, 0, 0, False,
    (0, 0, 0, 1, 1, 1), 0,
    (0, 0, 0, 1, 1, 1), 0,
    16,
    (-2, 3, 0), (-2, 1, 0), (-2, -1, 0), (-2, -3, 0),
    (-1, 3, 0), (-1, 1, 0), (-1, -1, 0), (-1, -3, 0),
    (1, 3, 0), (1, 1, 0), (1, -1, 0), (1, -3, 0),
    (3, 3, 0), (3, 1, 0), (3, -1, 0), (3, -3, 0),
    type="nurbsSurface")
    
    -type nurbsTrimface |  | NURBS trim face data
    ---
    Value Syntax | bool int {int {int {double bool bool} int {bool double}}}
    Value Meaning | flipNormal boundaryCount {boundaryType tedgeCountOnBoundary
    {splineCountOnEdge {edgeTolerance isEdgeReversed geometricContinuity}
    {splineCountOnPedge {isMonotone pedgeTolerance}}}
    Example | // flipNormal if true turns the surface inside out
    // boundaryCount: number of boundaries
    // boundaryType:
    // tedgeCountOnBoundary : number of edges in a boundary
    // splineCountOnEdge : number of splines in an edge in
    // edgeTolerance : tolerance used to build the 3d edge
    // isEdgeReversed : if true, the edge is backwards
    // geometricContinuity : if true, the edge is tangent continuous
    // splineCountOnPedge : number of splines in a 2d edge
    // isMonotone : if true, curvature is monotone
    // pedgeTolerance : tolerance for the 2d edge
    //
    
    
    -type polyFaces |  | Polygon face data
    ---
    Value Syntax | {"f" int {int}}
    {"h" int {int}}
    {"mf" int {int}}
    {"mh" int {int}}
    {"mu" int int {int}}
    {"mc" int int {int}}
    Value Meaning | {"f" faceEdgeCount {edgeIdValue}}
    {"h" holeEdgeCount {edgeIdValue}}
    {"mf" faceUVCount {uvIdValue}}
    {"mh" holeUVCount {uvIdValue}}
    {"mu" uvSet faceUVCount {uvIdValue}}
    {"mc" colorIndex multiColorCount {colorIdValue}}
    
    Example | // This data type (polyFace) is meant to be used in file I/O
    // after setAttrs have been written out for vertex position
    // arrays, edge connectivity arrays (with corresponding start
    // and end vertex descriptions), texture coordinate arrays and
    // color arrays. The reason is that this data type references
    // all of its data through ids created by the former types.
    //
    // "f" specifies the ids of the edges making up a face -
    // negative value if the edge is reversed in the face
    // "h" specifies the ids of the edges making up a hole -
    // negative value if the edge is reversed in the face
    // "mf" specifies the ids of texture coordinates (uvs) for a face.
    // This data type is obsolete as of version 3.0. It is replaced by "mu".
    // "mh" specifies the ids of texture coordinates (uvs) for a hole
    // This data type is obsolete as of version 3.0. It is replaced by "mu".
    // "mu" The first argument refers to the uv set. This is a zero-based
    // integer number. The second argument refers to the number of vertices (n)
    // on the face which have valid uv values. The last n values are the uv
    // ids of the texture coordinates (uvs) for the face. These indices
    // are what used to be represented by the "mf" and "mh" specification.
    // There may be more than one "mu" specification, one for each unique uv set.
    // "mc" specifies the color index values for a face. The first argument
    // is color index. The second argument is the number of color ids to follow.
    // Rest of the arguments are color ids for the face.
    //
    setAttr node.polyFaceAttr -type polyFaces "f" 3 1 2 3 "mc" 0 4 0 1 2 3;
    
    -type mesh |  | Polygonal mesh
    ---
    Value Syntax | {string [int {double double double}]}
    {string [int {double double double}]}
    [{string [int {double double}]}]
    {string [int {double double string}]}
    Value Meaning | "v" [vertexCount {vertexX vertexY vertexZ}]
    "vn" 0
    ["vt" [uvCount {uValue vValue}]]
    "e" [edgeCount {startVertex endVertex "smooth"|"hard"}]
    "face" ["l" edgeLoopCount edgeIndex1...] ]"lt" uvCount uvIndex1...]"
    "face"...
    
    Mel Example | // "v" specifies the vertices of the polygonal mesh
    // "vn"must be set to 0
    // "vt" is optional and specifies a U,V texture coordinate for each vertex
    // "e" specifies the edge connectivity information between vertices
    // "face" specifies face connectivity (edges/UVs) for a single face
    //
    $mesh = `createNode mesh`;
    setAttr ($mesh+".o")
    -type mesh "v" 3 0 0 0 0 1 0 0 0 1
    "vn" 3 1 0 0 1 0 0 1 0 0
    "vt" 3 0 0 0 1 1 0
    "e" 3 0 1 "hard" 1 2 "hard" 2 0 "hard"
    "face" "l" 3 0 1 2 "lt" 3 0 1 2;
    Python Example | # "v" specifies the vertices of the polygonal mesh
    # "vn"must be set to 0
    # "vt" is optional and specifies a U,V texture coordinate for each vertex
    # "e" specifies the edge connectivity information between vertices
    # "face" specifies face connectivity (edges/UVs) for a single face
    #
    mesh = maya.cmds.createNode("mesh")
    maya.cmds.setAttr(mesh+".o",
    "v", 3, (0, 0, 0), (0, 1, 0), (0, 0, 1),
    "vn", 0,
    "vt", 3, (0, 0), (0, 1), (1, 0),
    "e", 3, 0, 1, "hard", 1, 2, "hard", 2, 0, "hard",
    "face", "l", 3, 0, 1, 2, "lt", 3, 0, 1, 2,
    type="mesh")
    
    -type lattice |  | Lattice data
    ---
    Value Syntax | int int int int {double double double}
    Value Meaning | sDivisionCount tDivisionCount uDivisionCount
    pointCount {pointX pointY pointZ}
    Mel Example | // sDivisionCount is the horizontal lattice division count
    // tDivisionCount is the vertical lattice division count
    // uDivisionCount is the depth lattice division count
    // pointCount is the total number of lattice points
    // pointX,pointY,pointZ is one lattice point. The list is
    // specified varying first in S, then in T, last in U so the
    // first two entries are (S=0,T=0,U=0) (s=1,T=0,U=0)
    //
    $lattice = `createNode lattice`;
    setAttr ($lattice+".cc") -type lattice 2 5 2 20
    -2 -2 -2 2 -2 -2 -2 -1 -2 2 -1 -2 -2 0 -2
    2 0 -2 -2 1 -2 2 1 -2 -2 2 -2 2 2 -2
    -2 -2 2 2 -2 2 -2 -1 2 2 -1 2 -2 0 2
    2 0 2 -2 1 2 2 1 2 -2 2 2 2 2 2;
    Python Example | # sDivisionCount is the horizontal lattice division count
    # tDivisionCount is the vertical lattice division count
    # uDivisionCount is the depth lattice division count
    # pointCount is the total number of lattice points
    # (pointX,pointY,pointZ) is one lattice point. The list is
    # specified varying first in S, then in T, last in U so the
    # first two entries are (S=0,T=0,U=0) (s=1,T=0,U=0)
    #
    lattice = maya.cmds.createNode("lattice")
    maya.cmds.setAttr(lattice+".cc",
    2, 5, 2, 20,
    (-2, -2, -2), (2, -2, -2), (-2, -1, -2), (2, -1, -2), (-2, 0, -2),
    (2, 0, -2), (-2, 1, -2), (2, 1, -2), (-2, 2, -2), (2, 2, -2),
    (-2, -2, 2), (2, -2, 2), (-2, -1, 2), (2, -1, 2), (-2, 0, 2),
    (2, 0, 2), (-2, 1, 2), (2, 1, 2), (-2, 2, 2), (2, 2, 2),
    type="lattice")

    Example:
    ```python
        sphere -n node;
        addAttr -ln short2Attr -at short2;
        addAttr -ln short2a -p short2Attr -at short;
        addAttr -ln short2b -p short2Attr -at short;
        addAttr -ln short3Attr -at short3;
        addAttr -ln short3a -p short3Attr -at short;
        addAttr -ln short3b -p short3Attr -at short;
        addAttr -ln short3c -p short3Attr -at short;
        addAttr -ln long2Attr -at long2;
        addAttr -ln long2a -p long2Attr -at long;
        addAttr -ln long2b -p long2Attr -at long;
        addAttr -ln long3Attr -at long3;
        addAttr -ln long3a -p long3Attr -at long;
        addAttr -ln long3b -p long3Attr -at long;
        addAttr -ln long3c -p long3Attr -at long;
        addAttr -ln float2Attr -at float2;
        addAttr -ln float2a -p float2Attr -at "float";
        addAttr -ln float2b -p float2Attr -at "float";
        addAttr -ln float3Attr -at float3;
        addAttr -ln float3a -p float3Attr -at "float";
        addAttr -ln float3b -p float3Attr -at "float";
        addAttr -ln float3c -p float3Attr -at "float";
        addAttr -ln double2Attr -at double2;
        addAttr -ln double2a -p double2Attr -at double;
        addAttr -ln double2b -p double2Attr -at double;
        addAttr -ln double3Attr -at double3;
        addAttr -ln double3a -p double3Attr -at double;
        addAttr -ln double3b -p double3Attr -at double;
        addAttr -ln double3c -p double3Attr -at double;
        addAttr -ln int32ArrayAttr -dt Int32Array;
        addAttr -ln doubleArrayAttr -dt doubleArray;
        addAttr -ln pointArrayAttr -dt pointArray;
        addAttr -ln vectorArrayAttr -dt vectorArray;
        addAttr -ln stringArrayAttr -dt stringArray;
        addAttr -ln stringAttr -dt "string";
        addAttr -ln matrixAttr -dt "matrix";
        addAttr -ln sphereAttr -dt sphere;
        addAttr -ln coneAttr -dt cone;
        addAttr -ln meshAttr -dt mesh;
        addAttr -ln latticeAttr -dt lattice;
        addAttr -ln spectrumRGBAttr -dt spectrumRGB;
        addAttr -ln reflectanceRGBAttr -dt reflectanceRGB;
        addAttr -ln componentListAttr -dt componentList;
        addAttr -ln attrAliasAttr -dt attributeAlias;
        addAttr -ln curveAttr -dt nurbsCurve;
        addAttr -ln surfaceAttr -dt nurbsSurface;
        addAttr -ln trimFaceAttr -dt nurbsTrimface;
        addAttr -ln polyFaceAttr -dt polyFaces;
    ```

    ---
    - Args:
        - attribute Any [Any...]: Input item(s).
        - alteredValue (av): The value is only the current value, which may change in the next evalution (if the attribute has an incoming connection). This flag is only used during file I/O, so that attributes with incoming connections do not have their data
            overwritten during the first evaluation after a file is opened.Not supported for Ufe attributes.
        - caching (ca): Sets the attribute's internal caching on or off. Not all attributes can be defined as caching. Only those attributes that are not defined by default to be cached can be made caching.  As well, multi attribute elements cannot be made
            caching. Caching also affects child attributes for compound attributes.Not supported for Ufe attributes.
        - capacityHint (ch): Used to provide a memory allocation hint to attributes where the -size flag cannot provide enough information. This flag is optional and is primarily intended to be used during file I/O. Only certain attributes make use of this flag, and
            the interpretation of the flag value varies per attribute.Not supported for Ufe attributes.This flag is currently used by (node.attribute):mesh.face - hints the total number of elements in the face edge lists
        - channelBox (cb): Sets the attribute's display in the channelBox on or off. Keyable attributes are always display in the channelBox regardless of the channelBox settting.Not supported for Ufe attributes. The display of Ufe attributes in the Channel Box is
            controlled using thechannelBoxcommand flag-ual/ufeFixedAttrList.
        - clamp (c): For numeric attributes, if the value is outside the range of the attribute, clamp it to the min or max instead of failing.Not supported for Ufe attributes.
        - keyable (k): Sets the attribute's keyable state on or off.Not supported for Ufe attributes.
        - lock (l): Sets the attribute's lock state on or off.
        - size (s): Defines the size of a multi-attribute array. This is only a hint, used to help allocate memory as efficiently as possible.Not supported for Ufe attributes.
        - type (typ): Identifies the type of data.  If the -type flag is not present, a numeric type is assumed.Not supported for Ufe attributes.
    """
