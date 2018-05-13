from Consts import *
from RFCUtils import utils

def getModifier(iPlayer, iModifier):
	iCivilization = gc.getPlayer(iPlayer).getCivilizationType()
	if iCivilization in lOrder:
		return tModifiers[iModifier][lOrder.index(iCivilization)]
	return tDefaults[iModifier]

def getAdjustedModifier(iPlayer, iModifier):
	if utils.getScenario() > i3000BC and iPlayer < iVikings:
		if iModifier in dLateScenarioModifiers:
			return getModifier(iPlayer, iModifier) * dLateScenarioModifiers[iModifier] / 100
	return getModifier(iPlayer, iModifier)

def setModifier(iPlayer, iModifier, iNewValue):
	gc.getPlayer(iPlayer).setModifier(iModifier, iNewValue)

def changeModifier(iPlayer, iModifier, iChange):
	setModifier(iPlayer, iModifier, gc.getPlayer(iPlayer).getModifier(iModifier) + iChange)

def adjustModifier(iPlayer, iModifier, iPercent):
	setModifier(iPlayer, iModifier, gc.getPlayer(iPlayer).getModifier(iModifier) * iPercent / 100)

def adjustModifiers(iPlayer):
	for iModifier in dLateScenarioModifiers:
		adjustModifier(iPlayer, iModifier, dLateScenarioModifiers[iModifier])

def adjustInflationModifier(iPlayer):
	adjustModifier(iPlayer, iModifierInflationRate, dLateScenarioModifiers[iModifierInflationRate])

def updateModifier(iPlayer, iModifier):
	setModifier(iPlayer, iModifier, getModifier(iPlayer, iModifier))

def updateModifiers(iPlayer):
	for iModifier in range(iNumModifiers):
		updateModifier(iPlayer, iModifier)

def init():
	for iPlayer in range(iNumTotalPlayersB):
		updateModifiers(iPlayer)

		if utils.getScenario() > i3000BC and iPlayer < iVikings:
			adjustModifiers(iPlayer)


### Modifier types ###

iNumModifiers = 13
(iModifierCulture, iModifierUnitUpkeep, iModifierResearchCost, iModifierDistanceMaintenance, iModifierCitiesMaintenance,
iModifierCivicUpkeep, iModifierHealth, iModifierUnitCost, iModifierWonderCost, iModifierBuildingCost,
iModifierInflationRate, iModifierGreatPeopleThreshold, iModifierGrowthThreshold) = range(iNumModifiers)

### Sequence of spawns ###

lOrder = [iCivEgypt, iCivChina, iCivBabylonia, iCivAssyria, iCivHarappa, iCivHittite, iCivGreece, iCivIndia, iCivCarthage, iCivPolynesia, iCivPersia, iCivRome, iCivEthiopia, iCivTeotihuacan, iCivVietnam, iCivKorea, iCivMaya, iCivByzantium, iCivJapan, iCivVikings, iCivTurks, iCivArabia, iCivTibet, iCivIndonesia, iCivMoors, iCivSpain, iCivFrance, iCivKhmer, iCivTamils, iCivEngland, iCivHolyRome, iCivRussia, iCivPhilippines, iCivSwahili, iCivMamluks, iCivMali, iCivPoland, iCivPortugal, iCivInca, iCivItaly, iCivMongols, iCivAztecs, iCivMughals, iCivOttomans, iCivThailand, iCivCongo, iCivIran, iCivSweden, iCivNetherlands, iCivManchuria, iCivGermany, iCivAmerica, iCivArgentina, iCivMexico, iCivColombia, iCivBrazil, iCivAustralia, iCivBoers, iCivCanada, iCivIsrael, iCivIndependent, iCivIndependent2, iCivNative, iCivCeltia, iCivBarbarian]

### Modifiers (by civilization!) ###

# 							  EGY CHI BAB ASY HAR HTT GRE IND CAR PLY PER ROM ETH TEO VIE KOR MAY BYZ JAP VIK TUR ARA TIB INO MOO SPA FRA KHM TAM ENG HRE RUS PHI SWA MAM MAL POL POR INC ITA MON AZT MUG OTT THA CON IRA SWE NET MAN GER AME ARG MEX COL BRA AUS BOE CAN ISR		IND IND NAT CEL BAR 

tCulture =					(  90, 80, 80, 80, 80,100,100, 80,100,100,100,100,110,120,100, 90,100,100,100,110,120,130,110,120,120,120,125,125,160,130,150,130,120,130,130,130,110,147,140,150,135,140,125,150,130,130,135,140,165,140,150,140,130,140,140,140,140,140,140,140,		 20, 20, 20, 50, 30 )

tUnitUpkeep = 				( 110,120,120,110,200,110,110,135,115,100,100,110,100,120,100,115,105,110,110,105,100, 90,120,110, 90,100,110,110,100,100,100,100,100,100,100,100,100,100,100,100, 75, 90,110,120, 90, 90, 90, 90, 90, 90, 75, 80, 80, 90, 90, 80, 80, 80, 75, 75,		  0,  0,100,100,100 )
tResearchCost = 			(  90,120,110, 90,120, 90, 90, 90, 90, 90, 90, 90, 90,110,110, 90,120,125, 85, 90,120, 85, 85, 90, 90,100, 90, 80, 80, 80,100, 85,100,100, 90,110, 80, 85, 80, 70, 90, 85,120,120,100, 85, 90, 80, 80,100, 75, 75, 70, 90, 90, 90, 75, 80, 70, 70,		110,110,110,350,110 )
tDistanceMaintenance =		(  80,120, 90,110,120, 90, 90,120, 60, 50, 80, 70, 95,120,110,100, 70,100, 80, 95, 60, 70, 90,120, 80, 80, 80, 55, 60, 55, 70, 70, 65, 80, 80, 80, 90, 75, 60, 70, 75, 70,100,110, 80, 80, 80, 60, 70, 70, 60, 60, 50, 70, 70, 80, 60, 80, 70, 70,		 20, 20, 20, 20, 20 )
tCitiesMaintenance =		( 110,120,110, 90,125,110,125,150,120,100, 70, 60,100,120,110,115, 75,115, 80,110, 90, 75,110,120,100,100, 70, 50, 70, 70, 75, 60, 90, 90, 90, 90, 75, 80, 80, 80, 75, 85,100,120,100, 90, 80, 70, 75, 70, 70, 50, 70, 85, 85, 80, 70, 70, 60, 60,		 30, 30, 30, 30, 30 )
tCivicUpkeep = 				( 110,110,110,110,130,110,110,140, 70, 80, 70, 75, 80, 90, 80, 80, 80, 80, 90, 80,110, 80, 90, 80,100,100, 90, 75, 80, 70, 70, 80, 80, 80, 80, 80, 70, 80, 60, 60, 60, 60, 90, 90, 80, 80, 70, 60, 70, 70, 50, 50, 70, 70, 75, 75, 70, 75, 75, 75,	 	 70, 70, 70, 70, 70 )
tHealth = 					(   2,  1,  1,  1,  0,  1,  3,  1,  3,  3,  3,  3,  2,  2,  3,  3,  3,  3,  3,  2,  2,  3,  2,  3,  3,  3,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  3,  2,  3,  3,  4,  4,  4,  4,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,		  0,  0,  0,  0,  0 )

tUnitCost = 				( 110,130,110,110,200,110,110,120, 90,100, 70,100, 85,100, 90, 90, 90,105,115, 90,100, 85,100,110, 90,105,100, 90, 90,100, 90, 90, 90, 90, 90, 90, 80, 90,100,110, 80,100,100,100, 90, 70, 90, 90, 90, 90, 90, 75, 85, 80, 85, 85, 85, 85, 85, 85,		600,600,150,150,140 )
tWonderCost = 				(  80,100, 80, 80,300, 80, 80,100, 90,100, 85,100,100, 90,100,100,100, 90,110,100,120, 90, 90,100, 90, 80, 85, 90, 70, 90,100,100, 90, 90, 70, 90,100, 90, 80, 80, 90, 80, 80, 90, 90,100, 85, 90,100,100, 90, 70, 70, 90, 90, 90, 80, 90, 80, 80,		150,150,150,100,100 )
tBuildingCost = 			( 110,120,110,110,100,100,100,110, 90, 50,110, 90, 70,100, 90,100,100, 90,110,100,100, 90,100, 80,100, 90, 90, 90, 85, 90, 85, 90, 80, 80, 90, 80, 80, 85, 70, 80, 80, 80, 85, 80, 80, 80, 80, 80, 80, 75, 70, 70, 70, 80, 80, 75, 70, 80, 75, 80,		100,100,150,100,100 )
tInflationRate = 			( 130,120,130,110,150,130,130,140,130,130,130,130,110, 85,120,130, 80,125,120, 80, 90, 70, 85,100,100, 90, 85, 90, 75, 70, 70, 75,100,115, 75,115, 70, 80, 80, 85, 90, 80,100,100, 75, 75, 75, 85, 75, 90, 70, 65, 60, 65, 65, 60, 60, 60, 60, 60,		 95, 95, 95, 95, 95 )
tGreatPeopleThreshold =		( 140,140,140,140,140,140,110,125,120,120,110,110,110, 85,110,110, 90,100,120,110, 90, 90, 80, 85, 90, 90, 75, 75, 70, 75, 80, 80, 80, 80, 80, 80, 80, 75, 70, 65, 70, 70, 75, 80, 80, 85, 70, 80, 70, 70, 65, 65, 70, 80, 80, 80, 75, 80, 75, 75,		100,100,100,100,100 )
tGrowthThreshold =			( 150,120,150,150,150,130,130,150,120,120,130,120,110, 80,110,100,110,110, 80,110, 80, 80, 80, 80, 80, 80, 80, 80, 80, 70, 80, 80, 80, 75, 75, 75, 80, 80, 70, 70, 75, 70, 70, 70, 75, 75, 70, 75, 75, 65, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70,		125,125,125,125,125 )

tModifiers = (tCulture, tUnitUpkeep, tResearchCost, tDistanceMaintenance, tCitiesMaintenance, tCivicUpkeep, tHealth, tUnitCost, tWonderCost, tBuildingCost, tInflationRate, tGreatPeopleThreshold, tGrowthThreshold)

tDefaults = (100, 100, 100, 100, 100, 100, 2, 100, 100, 100, 100, 100, 100)

dLateScenarioModifiers = {
iModifierUnitUpkeep : 90,
iModifierDistanceMaintenance : 85,
iModifierCitiesMaintenance : 80,
iModifierCivicUpkeep : 90,
iModifierInflationRate : 85,
iModifierGreatPeopleThreshold : 85,
iModifierGrowthThreshold : 80,
}
