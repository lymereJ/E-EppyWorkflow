from pint import UnitRegistry
from eppy import modeleditor
from eppy.modeleditor import IDF

def EffectiveLeakageArea(idf_file,EffectiveLeakageArea):
	ureg = UnitRegistry()
	ELAObjects = idf_file.idfobjects["AIRFLOWNETWORK:MULTIZONE:SURFACE:EFFECTIVELEAKAGEAREA"]
	for i in range(0,len(ELAObjects)):
		EffectiveLeakageArea = float(EffectiveLeakageArea)*ureg.foot**2
		EffectiveLeakageArea = EffectiveLeakageArea.to(ureg.meter**2)
		ELAObjects[i].Effective_Leakage_Area = EffectiveLeakageArea.magnitude

if __name__ == '__main':
	EffectiveLeakageArea(idf_file,EffectiveLeakageArea)