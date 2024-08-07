# freecad-python generated by Parametrix
# run the script with:
# freecad.cmd myScript.py

import FreeCAD as App
import Part

#print(sys.argv)
outFileName = "rake"
if (len(sys.argv) == 3):
    outFileName = sys.argv[2]
print(f"outFileName: {outFileName}")

def ctr_face_rake_faceCone_Fa0_Ctr0():
	P000 = App.Vector(25.0000, 0.0000, 0)
	P001 = App.Vector(25.0000, 10.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(15.0000, 130.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(13.0069, 129.8339, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(23.0000, 9.9168, 0)
	S003 = Part.LineSegment(P003, P004)
	P005 = App.Vector(23.0000, 0.0000, 0)
	S004 = Part.LineSegment(P004, P005)
	P006 = App.Vector(25.0000, 0.0000, 0)
	S005 = Part.LineSegment(P005, P000)
	aShape = Part.Shape([S000, S001, S002, S003, S004, S005])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_rake_faceCone_Fa0():
	FC000 = ctr_face_rake_faceCone_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def rake_faceCone():
	FA000 = face_rake_faceCone_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_rake_faceConeHollow_Fa0_Ctr0():
	P000 = App.Vector(0.0000, 95.0000, 0)
	P001 = App.Vector(15.9097, 95.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(23.0000, 9.9168, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(23.0000, 4.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(0.0000, 4.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	P005 = App.Vector(0.0000, 95.0000, 0)
	S004 = Part.LineSegment(P004, P000)
	aShape = Part.Shape([S000, S001, S002, S003, S004])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_rake_faceConeHollow_Fa0():
	FC000 = ctr_face_rake_faceConeHollow_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def rake_faceConeHollow():
	FA000 = face_rake_faceConeHollow_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_rake_faceBeam_Fa0_Ctr0():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(15.0000, App.Vector(0.0000, 110.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceBeam_Fa0_Ctr1():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(13.0000, App.Vector(0.0000, 110.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def face_rake_faceBeam_Fa0():
	FC000 = ctr_face_rake_faceBeam_Fa0_Ctr0()
	FC001 = ctr_face_rake_faceBeam_Fa0_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def rake_faceBeam():
	FA000 = face_rake_faceBeam_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_rake_faceBeamHollow_Fa0_Ctr0():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(13.0000, App.Vector(0.0000, 110.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def face_rake_faceBeamHollow_Fa0():
	FC000 = ctr_face_rake_faceBeamHollow_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def rake_faceBeamHollow():
	FA000 = face_rake_faceBeamHollow_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_rake_faceDisc_Fa0_Ctr0():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(25.0000, App.Vector(0.0000, 0.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr1():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(12.0000, App.Vector(0.0000, 0.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr2():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(12.2500, 0.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr3():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(11.8326, 3.1705, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr4():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(10.6088, 6.1250, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr5():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(8.6621, 8.6621, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr6():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(6.1250, 10.6088, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr7():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(3.1705, 11.8326, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr8():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(0.0000, 12.2500, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr9():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(-3.1705, 11.8326, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr10():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(-6.1250, 10.6088, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr11():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(-8.6621, 8.6621, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr12():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(-10.6088, 6.1250, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr13():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(-11.8326, 3.1705, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr14():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(-12.2500, 0.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr15():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(-11.8326, -3.1705, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr16():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(-10.6088, -6.1250, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr17():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(-8.6621, -8.6621, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr18():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(-6.1250, -10.6088, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr19():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(-3.1705, -11.8326, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr20():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(-0.0000, -12.2500, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr21():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(3.1705, -11.8326, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr22():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(6.1250, -10.6088, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr23():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(8.6621, -8.6621, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr24():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(10.6088, -6.1250, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceDisc_Fa0_Ctr25():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(0.1250, App.Vector(11.8326, -3.1705, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def face_rake_faceDisc_Fa0():
	FC000 = ctr_face_rake_faceDisc_Fa0_Ctr0()
	FC001 = ctr_face_rake_faceDisc_Fa0_Ctr1()
	FC002 = ctr_face_rake_faceDisc_Fa0_Ctr2()
	FC003 = ctr_face_rake_faceDisc_Fa0_Ctr3()
	FC004 = ctr_face_rake_faceDisc_Fa0_Ctr4()
	FC005 = ctr_face_rake_faceDisc_Fa0_Ctr5()
	FC006 = ctr_face_rake_faceDisc_Fa0_Ctr6()
	FC007 = ctr_face_rake_faceDisc_Fa0_Ctr7()
	FC008 = ctr_face_rake_faceDisc_Fa0_Ctr8()
	FC009 = ctr_face_rake_faceDisc_Fa0_Ctr9()
	FC010 = ctr_face_rake_faceDisc_Fa0_Ctr10()
	FC011 = ctr_face_rake_faceDisc_Fa0_Ctr11()
	FC012 = ctr_face_rake_faceDisc_Fa0_Ctr12()
	FC013 = ctr_face_rake_faceDisc_Fa0_Ctr13()
	FC014 = ctr_face_rake_faceDisc_Fa0_Ctr14()
	FC015 = ctr_face_rake_faceDisc_Fa0_Ctr15()
	FC016 = ctr_face_rake_faceDisc_Fa0_Ctr16()
	FC017 = ctr_face_rake_faceDisc_Fa0_Ctr17()
	FC018 = ctr_face_rake_faceDisc_Fa0_Ctr18()
	FC019 = ctr_face_rake_faceDisc_Fa0_Ctr19()
	FC020 = ctr_face_rake_faceDisc_Fa0_Ctr20()
	FC021 = ctr_face_rake_faceDisc_Fa0_Ctr21()
	FC022 = ctr_face_rake_faceDisc_Fa0_Ctr22()
	FC023 = ctr_face_rake_faceDisc_Fa0_Ctr23()
	FC024 = ctr_face_rake_faceDisc_Fa0_Ctr24()
	FC025 = ctr_face_rake_faceDisc_Fa0_Ctr25()
	rOneFace = FC000.cut([FC001, FC002, FC003, FC004, FC005, FC006, FC007, FC008, FC009, FC010, FC011, FC012, FC013, FC014, FC015, FC016, FC017, FC018, FC019, FC020, FC021, FC022, FC023, FC024, FC025])
	rOneFace.check()
	return rOneFace

def rake_faceDisc():
	FA000 = face_rake_faceDisc_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_rake_faceHand_Fa0_Ctr0():
	P000 = App.Vector(12.9904, 117.5000, 0)
	P001 = App.Vector(21.6506, 157.5000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(8.6603, 165.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-0.0000, 160.0000, 0)
	P004 = App.Vector(-8.6603, 165.0000, 0)
	S002 = Part.Arc(P002, P003, P004)
	P005 = App.Vector(-21.6506, 157.5000, 0)
	S003 = Part.LineSegment(P004, P005)
	P006 = App.Vector(-12.9904, 117.5000, 0)
	S004 = Part.LineSegment(P005, P006)
	P007 = App.Vector(0.0000, 125.0000, 0)
	P008 = App.Vector(12.9904, 117.5000, 0)
	S005 = Part.Arc(P006, P007, P000)
	aShape = Part.Shape([S000, S001, S002, S003, S004, S005])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_rake_faceHand_Fa0():
	FC000 = ctr_face_rake_faceHand_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def rake_faceHand():
	FA000 = face_rake_faceHand_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_rake_faceWing_Fa0_Ctr0():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(5.0000, App.Vector(0.0000, 0.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_rake_faceWing_Fa0_Ctr1():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(3.0000, App.Vector(0.0000, 0.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def face_rake_faceWing_Fa0():
	FC000 = ctr_face_rake_faceWing_Fa0_Ctr0()
	FC001 = ctr_face_rake_faceWing_Fa0_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def rake_faceWing():
	FA000 = face_rake_faceWing_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_rake_faceWingHollow_Fa0_Ctr0():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(3.0000, App.Vector(0.0000, 0.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def face_rake_faceWingHollow_Fa0():
	FC000 = ctr_face_rake_faceWingHollow_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def rake_faceWingHollow():
	FA000 = face_rake_faceWingHollow_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_rake_faceDoor_Fa0_Ctr0():
	P000 = App.Vector(-9.7830, 12.5000, 0)
	P001 = App.Vector(9.7830, 12.5000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(11.6227, 13.3072, 0)
	P003 = App.Vector(12.2744, 15.2076, 0)
	S001 = Part.Arc(P001, P002, P003)
	P004 = App.Vector(9.3577, 50.2076, 0)
	S002 = Part.LineSegment(P003, P004)
	P005 = App.Vector(8.5591, 51.8397, 0)
	P006 = App.Vector(6.8663, 52.5000, 0)
	S003 = Part.Arc(P004, P005, P006)
	P007 = App.Vector(-6.8663, 52.5000, 0)
	S004 = Part.LineSegment(P006, P007)
	P008 = App.Vector(-8.5591, 51.8397, 0)
	P009 = App.Vector(-9.3577, 50.2076, 0)
	S005 = Part.Arc(P007, P008, P009)
	P010 = App.Vector(-12.2744, 15.2076, 0)
	S006 = Part.LineSegment(P009, P010)
	P011 = App.Vector(-11.6227, 13.3072, 0)
	P012 = App.Vector(-9.7830, 12.5000, 0)
	S007 = Part.Arc(P010, P011, P000)
	aShape = Part.Shape([S000, S001, S002, S003, S004, S005, S006, S007])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_rake_faceDoor_Fa0():
	FC000 = ctr_face_rake_faceDoor_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def rake_faceDoor():
	FA000 = face_rake_faceDoor_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def fex_subpax_rake_cone():
	FIG = rake_faceCone()
	VEX = FIG.revolve(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 360).rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 90)
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, 0.0000, 0.0000))
	return VFP
subpax_rake_cone = fex_subpax_rake_cone()

def fex_subpax_rake_coneHollow():
	FIG = rake_faceConeHollow()
	VEX = FIG.revolve(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 360).rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 90)
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, 0.0000, 0.0000))
	return VFP
subpax_rake_coneHollow = fex_subpax_rake_coneHollow()

def fex_subpax_rake_beam():
	FIG = rake_faceBeam()
	VEX = FIG.extrude(App.Vector(0, 0, 285))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 90.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, 142.5000, 0.0000))
	return VFP
subpax_rake_beam = fex_subpax_rake_beam()

def fex_subpax_rake_beamHollow():
	FIG = rake_faceBeamHollow()
	VEX = FIG.extrude(App.Vector(0, 0, 285))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 90.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, 142.5000, 0.0000))
	return VFP
subpax_rake_beamHollow = fex_subpax_rake_beamHollow()

def fex_subpax_rake_disc():
	FIG = rake_faceDisc()
	VEX = FIG.extrude(App.Vector(0, 0, 2))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, 0.0000, 2.0000))
	return VFP
subpax_rake_disc = fex_subpax_rake_disc()

def fex_subpax_rake_wing_right():
	FIG = rake_faceWing()
	VEX = FIG.extrude(App.Vector(0, 0, 138.513600108457))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), -60.5596)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, 18.9590, 33.2725))
	return VFP
subpax_rake_wing_right = fex_subpax_rake_wing_right()

def fex_subpax_rake_wing_left():
	FIG = rake_faceWing()
	VEX = FIG.extrude(App.Vector(0, 0, 138.513600108457))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 60.5596)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, -18.9590, 33.2725))
	return VFP
subpax_rake_wing_left = fex_subpax_rake_wing_left()

def fex_subpax_rake_wing_hollow_right():
	FIG = rake_faceWingHollow()
	VEX = FIG.extrude(App.Vector(0, 0, 138.513600108457))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), -60.5596)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, 18.9590, 33.2725))
	return VFP
subpax_rake_wing_hollow_right = fex_subpax_rake_wing_hollow_right()

def fex_subpax_rake_wing_hollow_left():
	FIG = rake_faceWingHollow()
	VEX = FIG.extrude(App.Vector(0, 0, 138.513600108457))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 60.5596)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, -18.9590, 33.2725))
	return VFP
subpax_rake_wing_hollow_left = fex_subpax_rake_wing_hollow_left()

def fex_subpax_rake_door():
	FIG = rake_faceDoor()
	VEX = FIG.extrude(App.Vector(0, 0, 50))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 90.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), -90.0000)
	VFP = VR3.translate(App.Vector(0.0000, 0.0000, 0.0000))
	return VFP
subpax_rake_door = fex_subpax_rake_door()

def fex_subpax_rake_hand_0():
	FIG = rake_faceHand()
	VEX = FIG.extrude(App.Vector(0, 0, 13))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 90.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, 142.5000, 0.0000))
	return VFP
subpax_rake_hand_0 = fex_subpax_rake_hand_0()

def fex_subpax_rake_hand_1():
	FIG = rake_faceHand()
	VEX = FIG.extrude(App.Vector(0, 0, 13))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 90.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, 41.5000, 0.0000))
	return VFP
subpax_rake_hand_1 = fex_subpax_rake_hand_1()

def fex_subpax_rake_hand_2():
	FIG = rake_faceHand()
	VEX = FIG.extrude(App.Vector(0, 0, 13))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 90.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, -28.5000, 0.0000))
	return VFP
subpax_rake_hand_2 = fex_subpax_rake_hand_2()

def fex_subpax_rake_hand_3():
	FIG = rake_faceHand()
	VEX = FIG.extrude(App.Vector(0, 0, 13))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 90.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, -129.5000, 0.0000))
	return VFP
subpax_rake_hand_3 = fex_subpax_rake_hand_3()

def fvol_ipax_rake_plus():
	V000 = subpax_rake_cone
	V001 = V000.fuse(subpax_rake_beam)
	V002 = V001.fuse(subpax_rake_disc)
	V003 = V002.fuse(subpax_rake_hand_0)
	V004 = V003.fuse(subpax_rake_hand_1)
	V005 = V004.fuse(subpax_rake_hand_2)
	V006 = V005.fuse(subpax_rake_hand_3)
	V007 = V006.fuse(subpax_rake_wing_right)
	V008 = V007.fuse(subpax_rake_wing_left)
	VFC = V008.removeSplitter()
	return VFC
ipax_rake_plus = fvol_ipax_rake_plus()

def fvol_ipax_rake_hollow():
	V000 = subpax_rake_coneHollow
	V001 = V000.fuse(subpax_rake_beamHollow)
	V002 = V001.fuse(subpax_rake_wing_hollow_right)
	V003 = V002.fuse(subpax_rake_wing_hollow_left)
	V004 = V003.fuse(subpax_rake_door)
	VFC = V004.removeSplitter()
	return VFC
ipax_rake_hollow = fvol_ipax_rake_hollow()

def fvol_pax_rake():
	V000 = ipax_rake_plus
	V001 = V000.cut(ipax_rake_hollow)
	VFC = V001.removeSplitter()
	return VFC
pax_rake = fvol_pax_rake()


pax_rake.check()
#pax_rake.exportBrep(f"{outFileName}.brep")
#pax_rake.exportIges(f"{outFileName}.igs")
#pax_rake.exportStep(f"{outFileName}.stp")
pax_rake.exportStl(f"{outFileName}.stl")

