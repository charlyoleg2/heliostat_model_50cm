# freecad-python generated by Parametrix
# run the script with:
# freecad.cmd myScript.py

import FreeCAD as App
import Part

#print(sys.argv)
outFileName = "swing"
if (len(sys.argv) == 3):
    outFileName = sys.argv[2]
print(f"outFileName: {outFileName}")

def ctr_face_swing_faceSide_Fa0_Ctr0():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(10.0000, App.Vector(0.0000, 0.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_swing_faceSide_Fa0_Ctr1():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(8.0000, App.Vector(0.0000, 0.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def face_swing_faceSide_Fa0():
	FC000 = ctr_face_swing_faceSide_Fa0_Ctr0()
	FC001 = ctr_face_swing_faceSide_Fa0_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceSide_Fa1_Ctr0():
	P000 = App.Vector(-160.0000, 7.0000, 0)
	P001 = App.Vector(-152.0000, 7.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-152.0000, 17.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-160.0000, 17.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-160.0000, 7.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_swing_faceSide_Fa1_Ctr1():
	P000 = App.Vector(-158.0000, 9.0000, 0)
	P001 = App.Vector(-154.0000, 9.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-154.0000, 15.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-158.0000, 15.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-158.0000, 9.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceSide_Fa1():
	FC000 = ctr_face_swing_faceSide_Fa1_Ctr0()
	FC001 = ctr_face_swing_faceSide_Fa1_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceSide_Fa2_Ctr0():
	P000 = App.Vector(-88.0000, 7.0000, 0)
	P001 = App.Vector(-80.0000, 7.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-80.0000, 17.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-88.0000, 17.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-88.0000, 7.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_swing_faceSide_Fa2_Ctr1():
	P000 = App.Vector(-86.0000, 9.0000, 0)
	P001 = App.Vector(-82.0000, 9.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-82.0000, 15.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-86.0000, 15.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-86.0000, 9.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceSide_Fa2():
	FC000 = ctr_face_swing_faceSide_Fa2_Ctr0()
	FC001 = ctr_face_swing_faceSide_Fa2_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceSide_Fa3_Ctr0():
	P000 = App.Vector(80.0000, 7.0000, 0)
	P001 = App.Vector(88.0000, 7.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(88.0000, 17.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(80.0000, 17.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(80.0000, 7.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_swing_faceSide_Fa3_Ctr1():
	P000 = App.Vector(82.0000, 9.0000, 0)
	P001 = App.Vector(86.0000, 9.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(86.0000, 15.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(82.0000, 15.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(82.0000, 9.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceSide_Fa3():
	FC000 = ctr_face_swing_faceSide_Fa3_Ctr0()
	FC001 = ctr_face_swing_faceSide_Fa3_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceSide_Fa4_Ctr0():
	P000 = App.Vector(152.0000, 7.0000, 0)
	P001 = App.Vector(160.0000, 7.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(160.0000, 17.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(152.0000, 17.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(152.0000, 7.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_swing_faceSide_Fa4_Ctr1():
	P000 = App.Vector(154.0000, 9.0000, 0)
	P001 = App.Vector(158.0000, 9.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(158.0000, 15.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(154.0000, 15.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(154.0000, 9.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceSide_Fa4():
	FC000 = ctr_face_swing_faceSide_Fa4_Ctr0()
	FC001 = ctr_face_swing_faceSide_Fa4_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def swing_faceSide():
	FA000 = face_swing_faceSide_Fa0()
	FA001 = face_swing_faceSide_Fa1()
	FA002 = face_swing_faceSide_Fa2()
	FA003 = face_swing_faceSide_Fa3()
	FA004 = face_swing_faceSide_Fa4()
	rOneFig = FA000.fuse([FA001, FA002, FA003, FA004])
	rOneFig.check()
	return rOneFig

def ctr_face_swing_faceFace_Fa0_Ctr0():
	P000 = App.Vector(-170.0000, 17.0000, 0)
	P001 = App.Vector(-162.0000, 17.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-162.0000, 27.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-170.0000, 27.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-170.0000, 17.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_swing_faceFace_Fa0_Ctr1():
	P000 = App.Vector(-168.0000, 19.0000, 0)
	P001 = App.Vector(-164.0000, 19.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-164.0000, 25.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-168.0000, 25.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-168.0000, 19.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceFace_Fa0():
	FC000 = ctr_face_swing_faceFace_Fa0_Ctr0()
	FC001 = ctr_face_swing_faceFace_Fa0_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceFace_Fa1_Ctr0():
	P000 = App.Vector(162.0000, 17.0000, 0)
	P001 = App.Vector(170.0000, 17.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(170.0000, 27.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(162.0000, 27.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(162.0000, 17.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_swing_faceFace_Fa1_Ctr1():
	P000 = App.Vector(164.0000, 19.0000, 0)
	P001 = App.Vector(168.0000, 19.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(168.0000, 25.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(164.0000, 25.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(164.0000, 19.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceFace_Fa1():
	FC000 = ctr_face_swing_faceFace_Fa1_Ctr0()
	FC001 = ctr_face_swing_faceFace_Fa1_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceFace_Fa2_Ctr0():
	P000 = App.Vector(-156.0000, 17.0000, 0)
	P001 = App.Vector(-148.0000, 17.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-148.0000, 27.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-156.0000, 27.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-156.0000, 17.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_swing_faceFace_Fa2_Ctr1():
	P000 = App.Vector(-154.0000, 19.0000, 0)
	P001 = App.Vector(-150.0000, 19.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-150.0000, 25.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-154.0000, 25.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-154.0000, 19.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceFace_Fa2():
	FC000 = ctr_face_swing_faceFace_Fa2_Ctr0()
	FC001 = ctr_face_swing_faceFace_Fa2_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceFace_Fa3_Ctr0():
	P000 = App.Vector(-134.0000, 17.0000, 0)
	P001 = App.Vector(-126.0000, 17.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-126.0000, 27.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-134.0000, 27.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-134.0000, 17.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_swing_faceFace_Fa3_Ctr1():
	P000 = App.Vector(-132.0000, 19.0000, 0)
	P001 = App.Vector(-128.0000, 19.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-128.0000, 25.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-132.0000, 25.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-132.0000, 19.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceFace_Fa3():
	FC000 = ctr_face_swing_faceFace_Fa3_Ctr0()
	FC001 = ctr_face_swing_faceFace_Fa3_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceFace_Fa4_Ctr0():
	P000 = App.Vector(-82.0000, 17.0000, 0)
	P001 = App.Vector(-74.0000, 17.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-74.0000, 27.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-82.0000, 27.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-82.0000, 17.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_swing_faceFace_Fa4_Ctr1():
	P000 = App.Vector(-80.0000, 19.0000, 0)
	P001 = App.Vector(-76.0000, 19.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-76.0000, 25.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-80.0000, 25.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-80.0000, 19.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceFace_Fa4():
	FC000 = ctr_face_swing_faceFace_Fa4_Ctr0()
	FC001 = ctr_face_swing_faceFace_Fa4_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceFace_Fa5_Ctr0():
	P000 = App.Vector(-60.0000, 17.0000, 0)
	P001 = App.Vector(-52.0000, 17.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-52.0000, 27.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-60.0000, 27.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-60.0000, 17.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_swing_faceFace_Fa5_Ctr1():
	P000 = App.Vector(-58.0000, 19.0000, 0)
	P001 = App.Vector(-54.0000, 19.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-54.0000, 25.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-58.0000, 25.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-58.0000, 19.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceFace_Fa5():
	FC000 = ctr_face_swing_faceFace_Fa5_Ctr0()
	FC001 = ctr_face_swing_faceFace_Fa5_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceFace_Fa6_Ctr0():
	P000 = App.Vector(52.0000, 17.0000, 0)
	P001 = App.Vector(60.0000, 17.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(60.0000, 27.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(52.0000, 27.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(52.0000, 17.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_swing_faceFace_Fa6_Ctr1():
	P000 = App.Vector(54.0000, 19.0000, 0)
	P001 = App.Vector(58.0000, 19.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(58.0000, 25.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(54.0000, 25.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(54.0000, 19.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceFace_Fa6():
	FC000 = ctr_face_swing_faceFace_Fa6_Ctr0()
	FC001 = ctr_face_swing_faceFace_Fa6_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceFace_Fa7_Ctr0():
	P000 = App.Vector(74.0000, 17.0000, 0)
	P001 = App.Vector(82.0000, 17.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(82.0000, 27.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(74.0000, 27.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(74.0000, 17.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_swing_faceFace_Fa7_Ctr1():
	P000 = App.Vector(76.0000, 19.0000, 0)
	P001 = App.Vector(80.0000, 19.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(80.0000, 25.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(76.0000, 25.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(76.0000, 19.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceFace_Fa7():
	FC000 = ctr_face_swing_faceFace_Fa7_Ctr0()
	FC001 = ctr_face_swing_faceFace_Fa7_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceFace_Fa8_Ctr0():
	P000 = App.Vector(126.0000, 17.0000, 0)
	P001 = App.Vector(134.0000, 17.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(134.0000, 27.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(126.0000, 27.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(126.0000, 17.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_swing_faceFace_Fa8_Ctr1():
	P000 = App.Vector(128.0000, 19.0000, 0)
	P001 = App.Vector(132.0000, 19.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(132.0000, 25.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(128.0000, 25.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(128.0000, 19.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceFace_Fa8():
	FC000 = ctr_face_swing_faceFace_Fa8_Ctr0()
	FC001 = ctr_face_swing_faceFace_Fa8_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceFace_Fa9_Ctr0():
	P000 = App.Vector(148.0000, 17.0000, 0)
	P001 = App.Vector(156.0000, 17.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(156.0000, 27.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(148.0000, 27.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(148.0000, 17.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_swing_faceFace_Fa9_Ctr1():
	P000 = App.Vector(150.0000, 19.0000, 0)
	P001 = App.Vector(154.0000, 19.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(154.0000, 25.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(150.0000, 25.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(150.0000, 19.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceFace_Fa9():
	FC000 = ctr_face_swing_faceFace_Fa9_Ctr0()
	FC001 = ctr_face_swing_faceFace_Fa9_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def swing_faceFace():
	FA000 = face_swing_faceFace_Fa0()
	FA001 = face_swing_faceFace_Fa1()
	FA002 = face_swing_faceFace_Fa2()
	FA003 = face_swing_faceFace_Fa3()
	FA004 = face_swing_faceFace_Fa4()
	FA005 = face_swing_faceFace_Fa5()
	FA006 = face_swing_faceFace_Fa6()
	FA007 = face_swing_faceFace_Fa7()
	FA008 = face_swing_faceFace_Fa8()
	FA009 = face_swing_faceFace_Fa9()
	rOneFig = FA000.fuse([FA001, FA002, FA003, FA004, FA005, FA006, FA007, FA008, FA009])
	rOneFig.check()
	return rOneFig

def swing_faceTop():
	rOneFig = undefined
	rOneFig.check()
	return rOneFig

def ctr_face_swing_faceButtress_Fa0_Ctr0():
	P000 = App.Vector(-80.0000, 17.0000, 0)
	P001 = App.Vector(-51.3254, 17.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-50.0442, 16.8331, 0)
	P003 = App.Vector(-48.8486, 16.3435, 0)
	S001 = Part.Arc(P001, P002, P003)
	P004 = App.Vector(-4.9535, -8.6869, 0)
	S002 = Part.LineSegment(P003, P004)
	P005 = App.Vector(-0.0000, -10.0000, 0)
	P006 = App.Vector(4.9535, -8.6869, 0)
	S003 = Part.Arc(P004, P005, P006)
	P007 = App.Vector(48.8486, 16.3435, 0)
	S004 = Part.LineSegment(P006, P007)
	P008 = App.Vector(50.0442, 16.8331, 0)
	P009 = App.Vector(51.3254, 17.0000, 0)
	S005 = Part.Arc(P007, P008, P009)
	P010 = App.Vector(80.0000, 17.0000, 0)
	S006 = Part.LineSegment(P009, P010)
	P011 = App.Vector(80.0000, 19.0000, 0)
	S007 = Part.LineSegment(P010, P011)
	P012 = App.Vector(-80.0000, 19.0000, 0)
	S008 = Part.LineSegment(P011, P012)
	P013 = App.Vector(-80.0000, 17.0000, 0)
	S009 = Part.LineSegment(P012, P013)
	aShape = Part.Shape([S000, S001, S002, S003, S004, S005, S006, S007, S008, S009])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_swing_faceButtress_Fa0_Ctr1():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(8.0000, App.Vector(0.0000, 0.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def face_swing_faceButtress_Fa0():
	FC000 = ctr_face_swing_faceButtress_Fa0_Ctr0()
	FC001 = ctr_face_swing_faceButtress_Fa0_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def swing_faceButtress():
	FA000 = face_swing_faceButtress_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_swing_faceTopWithRods_Fa0_Ctr0():
	P000 = App.Vector(-170.0000, -160.0000, 0)
	P001 = App.Vector(-162.0000, -160.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-162.0000, 160.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-170.0000, 160.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-170.0000, -160.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceTopWithRods_Fa0():
	FC000 = ctr_face_swing_faceTopWithRods_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceTopWithRods_Fa1_Ctr0():
	P000 = App.Vector(162.0000, -160.0000, 0)
	P001 = App.Vector(170.0000, -160.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(170.0000, 160.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(162.0000, 160.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(162.0000, -160.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceTopWithRods_Fa1():
	FC000 = ctr_face_swing_faceTopWithRods_Fa1_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceTopWithRods_Fa2_Ctr0():
	P000 = App.Vector(-156.0000, -160.0000, 0)
	P001 = App.Vector(-148.0000, -160.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-148.0000, 160.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-156.0000, 160.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-156.0000, -160.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceTopWithRods_Fa2():
	FC000 = ctr_face_swing_faceTopWithRods_Fa2_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceTopWithRods_Fa3_Ctr0():
	P000 = App.Vector(-134.0000, -160.0000, 0)
	P001 = App.Vector(-126.0000, -160.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-126.0000, 160.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-134.0000, 160.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-134.0000, -160.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceTopWithRods_Fa3():
	FC000 = ctr_face_swing_faceTopWithRods_Fa3_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceTopWithRods_Fa4_Ctr0():
	P000 = App.Vector(-82.0000, -160.0000, 0)
	P001 = App.Vector(-74.0000, -160.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-74.0000, 160.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-82.0000, 160.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-82.0000, -160.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceTopWithRods_Fa4():
	FC000 = ctr_face_swing_faceTopWithRods_Fa4_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceTopWithRods_Fa5_Ctr0():
	P000 = App.Vector(-60.0000, -160.0000, 0)
	P001 = App.Vector(-52.0000, -160.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-52.0000, 160.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-60.0000, 160.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-60.0000, -160.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceTopWithRods_Fa5():
	FC000 = ctr_face_swing_faceTopWithRods_Fa5_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceTopWithRods_Fa6_Ctr0():
	P000 = App.Vector(52.0000, -160.0000, 0)
	P001 = App.Vector(60.0000, -160.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(60.0000, 160.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(52.0000, 160.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(52.0000, -160.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceTopWithRods_Fa6():
	FC000 = ctr_face_swing_faceTopWithRods_Fa6_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceTopWithRods_Fa7_Ctr0():
	P000 = App.Vector(74.0000, -160.0000, 0)
	P001 = App.Vector(82.0000, -160.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(82.0000, 160.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(74.0000, 160.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(74.0000, -160.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceTopWithRods_Fa7():
	FC000 = ctr_face_swing_faceTopWithRods_Fa7_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceTopWithRods_Fa8_Ctr0():
	P000 = App.Vector(126.0000, -160.0000, 0)
	P001 = App.Vector(134.0000, -160.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(134.0000, 160.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(126.0000, 160.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(126.0000, -160.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceTopWithRods_Fa8():
	FC000 = ctr_face_swing_faceTopWithRods_Fa8_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceTopWithRods_Fa9_Ctr0():
	P000 = App.Vector(148.0000, -160.0000, 0)
	P001 = App.Vector(156.0000, -160.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(156.0000, 160.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(148.0000, 160.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(148.0000, -160.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceTopWithRods_Fa9():
	FC000 = ctr_face_swing_faceTopWithRods_Fa9_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceTopWithRods_Fa10_Ctr0():
	P000 = App.Vector(-170.0000, -160.0000, 0)
	P001 = App.Vector(170.0000, -160.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(170.0000, -152.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-170.0000, -152.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-170.0000, -160.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceTopWithRods_Fa10():
	FC000 = ctr_face_swing_faceTopWithRods_Fa10_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceTopWithRods_Fa11_Ctr0():
	P000 = App.Vector(-170.0000, -88.0000, 0)
	P001 = App.Vector(170.0000, -88.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(170.0000, -80.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-170.0000, -80.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-170.0000, -88.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceTopWithRods_Fa11():
	FC000 = ctr_face_swing_faceTopWithRods_Fa11_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceTopWithRods_Fa12_Ctr0():
	P000 = App.Vector(-170.0000, 80.0000, 0)
	P001 = App.Vector(170.0000, 80.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(170.0000, 88.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-170.0000, 88.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-170.0000, 80.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceTopWithRods_Fa12():
	FC000 = ctr_face_swing_faceTopWithRods_Fa12_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceTopWithRods_Fa13_Ctr0():
	P000 = App.Vector(-170.0000, 152.0000, 0)
	P001 = App.Vector(170.0000, 152.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(170.0000, 160.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-170.0000, 160.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-170.0000, 152.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceTopWithRods_Fa13():
	FC000 = ctr_face_swing_faceTopWithRods_Fa13_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_swing_faceTopWithRods_Fa14_Ctr0():
	P000 = App.Vector(-170.0000, -10.0000, 0)
	P001 = App.Vector(170.0000, -10.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(170.0000, 10.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-170.0000, 10.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-170.0000, -10.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_swing_faceTopWithRods_Fa14():
	FC000 = ctr_face_swing_faceTopWithRods_Fa14_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def swing_faceTopWithRods():
	FA000 = face_swing_faceTopWithRods_Fa0()
	FA001 = face_swing_faceTopWithRods_Fa1()
	FA002 = face_swing_faceTopWithRods_Fa2()
	FA003 = face_swing_faceTopWithRods_Fa3()
	FA004 = face_swing_faceTopWithRods_Fa4()
	FA005 = face_swing_faceTopWithRods_Fa5()
	FA006 = face_swing_faceTopWithRods_Fa6()
	FA007 = face_swing_faceTopWithRods_Fa7()
	FA008 = face_swing_faceTopWithRods_Fa8()
	FA009 = face_swing_faceTopWithRods_Fa9()
	FA010 = face_swing_faceTopWithRods_Fa10()
	FA011 = face_swing_faceTopWithRods_Fa11()
	FA012 = face_swing_faceTopWithRods_Fa12()
	FA013 = face_swing_faceTopWithRods_Fa13()
	FA014 = face_swing_faceTopWithRods_Fa14()
	rOneFig = FA000.fuse([FA001, FA002, FA003, FA004, FA005, FA006, FA007, FA008, FA009, FA010, FA011, FA012, FA013, FA014])
	rOneFig.check()
	return rOneFig

def fex_subpax_swing_side():
	FIG = swing_faceSide()
	VEX = FIG.extrude(App.Vector(0, 0, 340))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0)
	VFP = VR3.translate(App.Vector(0, 0, -170))
	return VFP
subpax_swing_side = fex_subpax_swing_side()

def fex_subpax_swing_face():
	FIG = swing_faceFace()
	VEX = FIG.extrude(App.Vector(0, 0, 320))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 90)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0)
	VFP = VR3.translate(App.Vector(-160, 0, 0))
	return VFP
subpax_swing_face = fex_subpax_swing_face()

def fex_subpax_swing_buttress_0():
	FIG = swing_faceButtress()
	VEX = FIG.extrude(App.Vector(0, 0, 8))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0)
	VFP = VR3.translate(App.Vector(0, 0, -170))
	return VFP
subpax_swing_buttress_0 = fex_subpax_swing_buttress_0()

def fex_subpax_swing_buttress_1():
	FIG = swing_faceButtress()
	VEX = FIG.extrude(App.Vector(0, 0, 8))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0)
	VFP = VR3.translate(App.Vector(0, 0, 162))
	return VFP
subpax_swing_buttress_1 = fex_subpax_swing_buttress_1()

def fex_subpax_swing_buttress_2():
	FIG = swing_faceButtress()
	VEX = FIG.extrude(App.Vector(0, 0, 8))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0)
	VFP = VR3.translate(App.Vector(0, 0, -156))
	return VFP
subpax_swing_buttress_2 = fex_subpax_swing_buttress_2()

def fex_subpax_swing_buttress_3():
	FIG = swing_faceButtress()
	VEX = FIG.extrude(App.Vector(0, 0, 8))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0)
	VFP = VR3.translate(App.Vector(0, 0, -134))
	return VFP
subpax_swing_buttress_3 = fex_subpax_swing_buttress_3()

def fex_subpax_swing_buttress_4():
	FIG = swing_faceButtress()
	VEX = FIG.extrude(App.Vector(0, 0, 8))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0)
	VFP = VR3.translate(App.Vector(0, 0, -82))
	return VFP
subpax_swing_buttress_4 = fex_subpax_swing_buttress_4()

def fex_subpax_swing_buttress_5():
	FIG = swing_faceButtress()
	VEX = FIG.extrude(App.Vector(0, 0, 8))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0)
	VFP = VR3.translate(App.Vector(0, 0, -60))
	return VFP
subpax_swing_buttress_5 = fex_subpax_swing_buttress_5()

def fex_subpax_swing_buttress_6():
	FIG = swing_faceButtress()
	VEX = FIG.extrude(App.Vector(0, 0, 8))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0)
	VFP = VR3.translate(App.Vector(0, 0, 52))
	return VFP
subpax_swing_buttress_6 = fex_subpax_swing_buttress_6()

def fex_subpax_swing_buttress_7():
	FIG = swing_faceButtress()
	VEX = FIG.extrude(App.Vector(0, 0, 8))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0)
	VFP = VR3.translate(App.Vector(0, 0, 74))
	return VFP
subpax_swing_buttress_7 = fex_subpax_swing_buttress_7()

def fex_subpax_swing_buttress_8():
	FIG = swing_faceButtress()
	VEX = FIG.extrude(App.Vector(0, 0, 8))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0)
	VFP = VR3.translate(App.Vector(0, 0, 126))
	return VFP
subpax_swing_buttress_8 = fex_subpax_swing_buttress_8()

def fex_subpax_swing_buttress_9():
	FIG = swing_faceButtress()
	VEX = FIG.extrude(App.Vector(0, 0, 8))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0)
	VFP = VR3.translate(App.Vector(0, 0, 148))
	return VFP
subpax_swing_buttress_9 = fex_subpax_swing_buttress_9()

pax_swing = subpax_swing_side.fuse([subpax_swing_face, subpax_swing_buttress_0, subpax_swing_buttress_1, subpax_swing_buttress_2, subpax_swing_buttress_3, subpax_swing_buttress_4, subpax_swing_buttress_5, subpax_swing_buttress_6, subpax_swing_buttress_7, subpax_swing_buttress_8, subpax_swing_buttress_9])

pax_swing.check()
#pax_swing.exportBrep(f"{outFileName}.brep")
#pax_swing.exportIges(f"{outFileName}.igs")
#pax_swing.exportStep(f"{outFileName}.stp")
pax_swing.exportStl(f"{outFileName}.stl")
