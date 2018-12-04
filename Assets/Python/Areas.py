from Consts import *

# Peak that change to hills during the game, like Bogota
lPeakExceptions = []

def isReborn(iPlayer):
	return gc.getPlayer(iPlayer).isReborn()
	
def getOrElse(dDictionary, key, default):
	if key in dDictionary: return dDictionary[key]
	return default
	
def getArea(iPlayer, tRectangle, dExceptions, bReborn=None, dChangedRectangle={}, dChangedExceptions={}):
	if bReborn is None: bReborn = isReborn(iPlayer)
	tBL, tTR = tRectangle[iPlayer]
	lExceptions = getOrElse(dExceptions, iPlayer, [])
	
	if bReborn:
		if iPlayer in dChangedRectangle:
			tBL, tTR = dChangedRectangle[iPlayer]
			lExceptions = getOrElse(dChangedExceptions, iPlayer, [])
	
	left, bottom = tBL
	right, top = tTR		
	return [(x, y) for x in range(left, right+1) for y in range(bottom, top+1) if (x, y) not in lExceptions]

def getCapital(iPlayer, bReborn=None):
	if bReborn is None: bReborn = isReborn(iPlayer)
	if bReborn and iPlayer in dChangedCapitals:
		return dChangedCapitals[iPlayer]
	return tCapitals[iPlayer]
	
def getRespawnCapital(iPlayer, bReborn=None):
	if iPlayer in dRespawnCapitals: return dRespawnCapitals[iPlayer]
	return getCapital(iPlayer, bReborn)
	
def getNewCapital(iPlayer, bReborn=None):
	if iPlayer in dNewCapitals: return dNewCapitals[iPlayer]
	return getRespawnCapital(iPlayer, bReborn)
	
def getBirthArea(iPlayer):
	return getArea(iPlayer, tBirthArea, dBirthAreaExceptions)
	
def getBirthRectangle(iPlayer, bExtended = None):
	if bExtended is None: bExtended = isExtendedBirth(iPlayer)
	if iPlayer in dChangedBirthArea and bExtended:
		return dChangedBirthArea[iPlayer]
	return tBirthArea[iPlayer]
	
def getBirthExceptions(iPlayer):
	if iPlayer in dBirthAreaExceptions: return dBirthAreaExceptions[iPlayer]
	return []
	
def getCoreArea(iPlayer, bReborn=None):
	return getArea(iPlayer, tCoreArea, dCoreAreaExceptions, bReborn, dChangedCoreArea, dChangedCoreAreaExceptions)
	
def getNormalArea(iPlayer, bReborn=None):
	return getArea(iPlayer, tNormalArea, dNormalAreaExceptions, bReborn, dChangedNormalArea, dChangedNormalAreaExceptions)

def getBroaderArea(iPlayer, bReborn=None):
	return getArea(iPlayer, tBroaderArea, {}, dChangedBroaderArea)
	
def getRespawnArea(iPlayer):
	if iPlayer in dRespawnArea: return getArea(iPlayer, dRespawnArea, {})
	return getNormalArea(iPlayer)
	
def getRebirthArea(iPlayer):
	if iPlayer in dRebirthArea: return getArea(iPlayer, dRebirthArea, dRebirthAreaExceptions)
	return getBirthArea(iPlayer)
	
def updateCore(iPlayer):
	lCore = getCoreArea(iPlayer)
	for x in range(iWorldX):
		for y in range(iWorldY):
			plot = gc.getMap().plot(x, y)
			if plot.isWater() or (plot.isPeak() and (x, y) not in lPeakExceptions): continue
			plot.setCore(iPlayer, (x, y) in lCore)
			
def isForeignCore(iPlayer, tPlot):
	x, y =  tPlot
	plot = gc.getMap().plot(x, y)
	for iLoopPlayer in range(iNumPlayers):
		if iLoopPlayer == iPlayer: continue
		if plot.isCore(iLoopPlayer):
			return True
	return False
	
def isExtendedBirth(iPlayer):
	if gc.getGame().getActivePlayer() == iPlayer: return False
	
	# add special conditions for extended AI flip zones here
	if iPlayer == iOttomans and pByzantium.isAlive(): return False
	
	return True
			
def init():
	for iPlayer in range(iNumPlayers):
		updateCore(iPlayer)
	
### Capitals ###

tCapitals = (
(79, 42), # Thebes
(121, 52), # Chang'an
(89, 47), # Babylon
(101, 47), # Harappa
(76, 51), # Athens
(110, 45), # Pataliputra
(84, 47), # Sur
(3, 20), # Tonga
(95, 44), # Persepolis
(68, 53), # Rome
(105, 32), # Thanjavur
(85, 34), # Aksum
(131, 53), # Seoul
(22, 41), # Tikal
(79, 55), # Constantinople
(0, 0), # Kyoto
(0, 0), # Oslo
(0, 0), # Orduqent
(0, 0), # Mecca
(0, 0), # Lhasa
(0, 0), # Palembang
(0, 0), # Cordoba
(0, 0), # Madrid
(0, 0), # Paris
(0, 0), # Angkor
(0, 0), # London
(0, 0), # Cologne
(0, 0), # Moskow
(0, 0), # Timbuktu
(0, 0), # Krakow
(0, 0), # Lisboa
(0, 0), # Cuzco
(0, 0), # Mailand
(0, 0), # Karakorum
(0, 0), # Tenochtitlan
(0, 0), # Delhi
(0, 0), # Sogut
(0, 0), # Ayutthaya
(0, 0), # Mbanza Kongo
(0, 0), # Amsterdam
(0, 0), # Berlin
(0, 0), # Washington
(0, 0), # Buenos Aires
(0, 0), # Rio de Janeiro
(0, 0), # Ottawa
)

dChangedCapitals = {
iChina : (124, 56),	# Beijing
iIndia : (103, 38),	# Delhi
iCarthage : (67, 48),	# Carthage
iPersia : (94, 50),	# Esfahan (Iran)
iTamils : (105, 36),	# Vijayanagara
iMaya : (29, 34),	# Bogota (Colombia)
iKhmer : (0, 0),	# Hanoi
iHolyRome : (0, 0),	# Vienna
}

# new capital locations if changed during the game
dNewCapitals = {
iJapan : (0, 0),	# Tokyo
iVikings : (0, 0),	# Stockholm
iHolyRome : (0, 0),	# Vienna
iItaly : (0, 0),	# Rome
iMongolia : (0, 0),	# Khanbaliq
iOttomans : (0, 0),	# Istanbul
}

# new capital locations on respawn
dRespawnCapitals = {
iEgypt : (79, 42),	# Cairo
iChina :  (124, 56),	# Beijing
iIndia : (0, 0),	# Delhi
iPersia : (0, 0),	# Esfahan
iEthiopia : (0, 0),	# Addis Ababa
iJapan : (0, 0),	# Tokyo
iVikings : (0, 0),	# Stockholm
iTurks: (0, 0), 	# Herat
iIndonesia : (0, 0),	# Jakarta
iMoors : (0, 0),	# Marrakesh
iHolyRome : (0, 0),	# Vienna
iInca : (0, 0),		# Lima
iItaly : (0, 0),	# Rome
iMughals : (0, 0),	# Karachi
iOttomans : (0, 0),	# Istanbul
}

### Birth Area ###

tBirthArea = (
((76, 37),	(81, 45)),	# Egypt
((117, 48),	(129, 56)), 	# China
((86, 47),	(89, 52)),	# Babylonia
((99, 44),	(102, 47)),	# Harappa
((73, 48),	(81, 55)),	# Greece
((105, 42),	(115, 46)),	# India
((82, 47),	(86, 51)),	# Carthage
((2, 19),	(6, 24)),	# Polynesia
((91, 43),	(102, 53)),	# Persia
((66, 50),	(72, 57)),	# Rome
((105, 29),	(109, 36)),	# Tamils
((80, 31),	(85, 37)),	# Ethiopia
((130, 52),	(133, 56)),	# Korea
((20, 41),	(23, 44)),	# Maya
((72, 45),	(86, 56)),	# Byzantium
((0, 0),	(0, 0)),	# Japan
((0, 0),	(0, 0)),	# Vikings
((0, 0), 	(0, 0)),	# Turks
((0, 0),	(0, 0)),	# Arabia
((0, 0),	(0, 0)),	# Tibet
((0, 0),	(0, 0)),	# Indonesia
((0, 0),	(0, 0)),	# Moors
((0, 0),	(0, 0)),	# Spain
((0, 0),	(0, 0)),	# France
((0, 0),	(0, 0)),	# Khmer
((0, 0),	(0, 0)),	# England
((0, 0),	(0, 0)),	# HolyRome
((0, 0),	(0, 0)),	# Russia
((0, 0),	(0, 0)),	# Mali
((0, 0),	(0, 0)),	# Poland
((0, 0),	(0, 0)),	# Portugal
((0, 0),	(0, 0)),	# Inca
((0, 0),	(0, 0)),	# Italy
((0, 0),	(0, 0)),	# Mongolia
((0, 0),	(0, 0)),	# Aztecs
((0, 0),	(0, 0)),	# Mughals
((0, 0),	(0, 0)),	# Ottomans
((0, 0), 	(0, 0)),	# Thailand
((0, 0),	(0, 0)),	# Congo
((0, 0),	(0, 0)),	# Netherlands
((0, 0),	(0, 0)),	# Germany
((0, 0),	(0, 0)),	# America
((0, 0),	(0, 0)),	# Argentina
((0, 0),	(0, 0)),	# Brazil
((0, 0),	(0, 0)),	# Canada
)

dChangedBirthArea = {
iPersia :	((86, 44),	(99, 53)),	# includes Assyria and Anatolia
iSpain : 	((0, 0),	(0, 0)),	# includes Catalonia
iInca : 	((0, 0),	(0, 0)),
iMongolia : 	((0, 0),	(0, 0)),	# 6 more west, 1 more south
iOttomans : 	((0, 0), 	(0, 0)), 	# includes Constantinople
iArgentina : 	((0, 0),	(0, 0)),	# includes Chile
}

dBirthAreaExceptions = {
iEgypt : [(78,45), (81, 45), (82, 45)],
iChina : [(128, 56)],
iBabylonia : [(89, 52), (88, 52), (86, 47), (86, 48), (86, 49), (86, 50), (87, 47), (87, 48), (89, 51)],
iHarappa : [(102, 44)],
iGreece : [(73, 55), (74, 55), (75, 55), (76, 55), (81, 53), (81, 54), (81, 55)],
iIndia : [(114, 42), (105, 42), (106, 42), (107, 42), (108, 42), (109, 42), (110, 42), (111, 42), (115, 42), (115, 46)],iRome : [],
iPersia : [(91, 53), (98, 43), (98, 44), (98, 45), (98, 46), (98, 47), (98, 48), (99, 43), (99, 44), (99, 45), (99, 46), (99, 49), (100, 43), (100, 44), (100, 45), (100, 46), (100, 47), (100, 48), (100, 50), (101, 43), (101, 44), (101, 45), (101, 46), (101, 47), (101, 48), (101, 49), (101, 50), (102, 43), (102, 44), (102, 45), (102, 46), (102, 47), (102, 48), (102, 49), (102, 50)],
iEthiopia : [(85, 37), (85, 36)],
iByzantium : [(72, 52), (75, 45), (76, 45), (79, 45), (80, 45)],
iTurks : [],
iArabia : [],
iTibet : [],
iIndonesia : [],
iMoors : [],
iSpain : [],
iFrance : [],
iHolyRome : [],
iRussia : [],
iPoland : [],
iMongolia : [],
iMughals : [],
iOttomans : [],
iNetherlands : [],
iGermany : [],
iAmerica : [],
iArgentina : [],
iBrazil : [],
iCanada : [],
}

### Core Area ###

tCoreArea = (
((78, 39),	(80, 45)),	# Egypt
((117, 48),	(128, 56)),	# China
((86, 47),	(89, 52)),	# Babylonia
((99, 44),	(102, 47)),	# Harappa
((73, 48),	(81, 55)),	# Greece
((105, 42),	(115, 46)),	# India
((84, 47),	(85, 50)), # Phoenicia
((3, 20),	(5, 23)),	# Polynesia
((91, 43),	(102, 53)),	# Persia
((66, 50),	(72, 57)),	# Rome
((105, 29),	(109, 36)),	# Tamils
((80, 31),	(85, 37)),	# Ethiopia
((130, 52),	(133, 56)),	# Korea
((20, 41),	(23, 44)),	# Maya
((73, 50),	(85, 56)),	# Byzantium
((0, 0),	(0, 0)),	# Japan
((0, 0),	(0, 0)),	# Vikings
((0, 0), 	(0, 0)),	# Turks
((0, 0),	(0, 0)),	# Arabia
((0, 0),	(0, 0)),	# Tibet
((0, 0),	(0, 0)),	# Indonesia
((0, 0),	(0, 0)),	# Moors
((0, 0),	(0, 0)),	# Spain
((0, 0),	(0, 0)),	# France
((0, 0),	(0, 0)),	# Khmer
((0, 0),	(0, 0)),	# England
((0, 0),	(0, 0)),	# HolyRome
((0, 0),	(0, 0)),	# Russia
((0, 0),	(0, 0)),	# Mali
((0, 0),	(0, 0)),	# Poland
((0, 0),	(0, 0)),	# Portugal
((0, 0),	(0, 0)),	# Inca
((0, 0),	(0, 0)),	# Italy
((0, 0),	(0, 0)),	# Mongolia
((0, 0),	(0, 0)),	# Aztecs
((0, 0),	(0, 0)),	# Mughals
((0, 0),	(0, 0)),	# Turkey
((0, 0),	(0, 0)),	# Thailand
((0, 0),	(0, 0)),	# Congo
((0, 0),	(0, 0)),	# Netherlands
((0, 0),	(0, 0)),	# Germany
((0, 0),	(0, 0)),	# America
((0, 0),	(0, 0)),	# Argentina
((0, 0),	(0, 0)),	# Brazil
((0, 0),	(0, 0)),	# Canada
)

dChangedCoreArea = {
iChina :	((117, 48),	(129, 56)),
iGreece : ((74, 48),	(78, 52)),
iIndia : ((103, 38),	(106, 43)),
iPhoenicia : ((61, 45),	(85, 50)),
iMaya : ((26, 29),	(35, 38)),	# Colombia
iByzantium : ((76, 53),	(80, 56)),
iJapan :	((0, 0), 	(0, 0)),
iTurks :	((0, 0), 	(0, 0)),
iArabia :	((0, 0),	(0, 0)),
iMoors :	((0, 0),	(0, 0)),
iSpain :	((0, 0),	(0, 0)),
iKhmer :	((0, 0),	(0, 0)),
iHolyRome :	((0, 0),	(0, 0)),
iItaly :	((0, 0),	(0, 0)),
iMongolia :	((0, 0),	(0, 0)),
iAztecs :	((0, 0),	(0, 0)),	# Mexico
iMughals :	((0, 0),	(0, 0)),
iOttomans :	((0, 0),	(0, 0)),
iGermany :	((0, 0),	(0, 0)),
}

dCoreAreaExceptions = {
iEgypt : [(78, 39), (78, 40)],
iChina : [(117, 50), (117, 52), (117, 53), (117, 55), (117, 56), (118, 56), (122, 48), (123, 48), (123, 49), (123, 50), (124, 49), (124, 50), (124, 51), (125, 48), (125, 49), (125, 50), (125, 51), (126, 49), (126, 50), (126, 51), (126, 52), (127, 48), (127, 49), (127, 50), (127, 51), (127, 52), (128, 48), (128, 49), (128, 51), (128, 52), (128, 56)],
iBabylonia : [(86, 47), (86, 48), (86, 49), (86, 50), (87, 47), (87, 48), (89, 51)],
iHarappa : [(102, 44)],
iGreece : [(73, 55), (74, 55), (75, 55), (76, 55), (81, 53), (81, 54)],
iIndia : [(105, 42), (106, 42), (107, 42), (108, 42), (109, 42), (110, 42), (111, 42), (115, 42), (115, 46)],
iPersia : [(91, 45), (91, 46), (91, 47), (91, 48), (91, 53), (92, 47), (92, 52), (98, 43), (98, 44), (98, 45), (98, 46), (98, 47), (98, 48), (99, 43), (99, 44), (99, 45), (99, 46), (99, 49), (100, 43), (100, 44), (100, 45), (100, 46), (100, 47), (100, 48), (100, 50), (101, 43), (101, 44), (101, 45), (101, 46), (101, 47), (101, 48), (101, 49), (101, 50), (102, 43), (102, 44), (102, 45), (102, 46), (102, 47), (102, 48), (102, 49), (102, 50)],
iRome : [(66, 51), (66, 52), (69, 56)],
iEthiopia : [(80, 31), (80, 32), (80, 33), (80, 34), (80, 35), (80, 37), (81, 31), (82, 31), (83, 35), (83, 37), (84, 35), (84, 36), (84, 37), (85, 35)],
iByzantium : [(84, 51), (85, 50), (85, 51)],
iTurks : [],
iArabia : [],
iTibet : [],
iIndonesia : [],
iSpain : [],
iFrance : [],
iHolyRome : [],
iRussia : [],
iPoland : [],
iMongolia : [],
iMughals : [],
iOttomans : [],
iNetherlands : [],
iGermany : [],
iAmerica : [],
iArgentina : [],
iCanada : [],
}

dChangedCoreAreaExceptions = {
iChina : [(117, 50), (117, 52), (117, 53), (117, 55), (117, 56), (118, 56), (128, 56)],
iPhoenicia : [(61, 45), (62, 45), (63, 45), (63, 46), (64, 45), (64, 46), (65, 45), (65, 46), (66, 45), (69, 49), (70, 45), (70, 48), (70, 49), (71, 50), (74, 50), (75, 45), (75, 50), (76, 45), (77, 48), (78, 48), (79, 45), (80, 45), (82, 48), (83, 45), (83, 49), (84, 45), (84, 46), (85, 45), (85, 46)],
iMaya : [(31, 29), (31, 30), (31, 31), (31, 32), (32, 29), (32, 30), (32, 31), (32, 32), (32, 33), (33, 29), (33, 30), (33, 31), (33, 32), (33, 33), (33, 34), (34, 29), (34, 30), (34, 31), (34, 32), (34, 33), (35, 29), (35, 30), (35, 31), (35, 32), (35, 34), (35, 35)], # Colombia
iByzantium : [(76, 55), (76, 56), (77, 56)],
iArabia : [],
iKhmer:	[],
iMoors : [],
iSpain : [],
iHolyRome : [],
iItaly : [],
iMongolia : [],
iMughals : [],
iOttomans : [],
iGermany : [],
}

### Normal Area ###

tNormalArea = (
((75, 36),	(82, 45)),	# Egypt
((0, 0),	(0, 0)),	# China
((0, 0),	(0, 0)),	# Babylonia
((0, 0),	(0, 0)), 	# Harappa
((0, 0),	(0, 0)),	# Greece
((0, 0),	(0, 0)),	# India
((0, 0),	(0, 0)),	# Carthage
((0, 0),	(0, 0)),	# Polynesia
((0, 0),	(0, 0)),	# Persia
((0, 0),	(0, 0)),	# Rome
((0, 0),	(0, 0)),	# Tamils
((0, 0),	(0, 0)),	# Ethiopia
((0, 0),	(0, 0)),	# Korea
((0, 0),	(0, 0)),	# Maya
((0, 0),	(0, 0)),	# Byzantium
((0, 0),	(0, 0)),	# Japan
((0, 0),	(0, 0)),	# Vikings
((0, 0), 	(0, 0)),	# Turks
((0, 0),	(0, 0)),	# Arabia
((0, 0),	(0, 0)),	# Tibet
((0, 0),	(0, 0)),	# Indonesia
((0, 0),	(0, 0)),	# Moors
((0, 0),	(0, 0)),	# Spain
((0, 0),	(0, 0)),	# France
((0, 0),	(0, 0)),	# Khmer
((0, 0),	(0, 0)),	# England
((0, 0),	(0, 0)),	# HolyRome
((0, 0),	(0, 0)),	# Russia
((0, 0),	(0, 0)),	# Mali
((0, 0),	(0, 0)),	# Poland
((0, 0),	(0, 0)),	# Portugal
((0, 0),	(0, 0)),	# Inca
((0, 0),	(0, 0)),	# Italy
((0, 0),	(0, 0)),	# Mongolia
((0, 0),	(0, 0)),	# Aztecs
((0, 0),	(0, 0)),	# Mughals
((0, 0),	(0, 0)),	# Ottomans
((0, 0),	(0, 0)),	# Thailand
((0, 0),	(0, 0)),	# Congo
((0, 0),	(0, 0)),	# Netherlands
((0, 0),	(0, 0)),	# Germany
((0, 0),	(0, 0)),	# America
((0, 0),	(0, 0)),	# Argentina
((0, 0),	(0, 0)),	# Brazil
((0, 0),	(0, 0)),	# Canada
)

dChangedNormalArea = {
iIndia : 	((0, 0),	(0, 0)),
iCarthage :	((0, 0),	(0, 0)),
iMaya : 	((0, 0),	(0, 0)),	# Colombia
iArabia : 	((0, 0),	(0, 0)),
iKhmer : 	((0, 0),	(0, 0)),
iHolyRome : 	((0, 0),	(0, 0)),
}

dNormalAreaExceptions = {
iChina : [],
iBabylonia : [],
iHarappa : [],
iGreece : [],
iIndia : [],
iPolynesia : [],
iPersia : [],
iRome : [],
iEthiopia : [],
iByzantium : [],
iJapan : [],
iVikings : [],
iTurks : [],
iArabia : [],
iSpain : [],
iTibet : [],
iIndonesia : [],
iMoors : [],
iSpain : [],
iFrance : [],
iKhmer:	[],
iHolyRome : [],
iRussia : [],
iPoland : [],
iInca : [],
iItaly : [],
iMongolia : [],
iMughals : [],
iOttomans : [],
iThailand : [],
iNetherlands : [],
iGermany : [],
iAmerica : [],
iArgentina : [],
iBrazil : [],
iCanada : [],
}

dChangedNormalAreaExceptions = {
iMaya : [], # Colombia
iArabia : [],
iKhmer:	[],
iHolyRome : [],
}

### Broader Area ###

tBroaderArea = (
((0, 0),	(0, 0)),	# Egypt
((0, 0),	(0, 0)),	# China
((0, 0),	(0, 0)),	# Babylonia
((0, 0),	(0, 0)),	# Harappa
((0, 0),	(0, 0)),	# Greece
((0, 0),	(0, 0)),	# India
((0, 0),	(0, 0)),	# Carthage
((0, 0),	(0, 0)),	# Polynesia
((0, 0),	(0, 0)),	# Persia
((0, 0),	(0, 0)),	# Rome
((0, 0),	(0, 0)),	# Tamils
((0, 0),	(0, 0)),	# Ethiopia
((0, 0),	(0, 0)),	# Korea
((0, 0),	(0, 0)),	# Maya
((0, 0),	(0, 0)),	# Byzantium
((0, 0),	(0, 0)),	# Japan
((0, 0),	(0, 0)),	# Vikings
((0, 0), 	(0, 0)),	# Turks
((0, 0),	(0, 0)),	# Arabia
((0, 0),	(0, 0)),	# Tibet
((0, 0),	(0, 0)),	# Indonesia
((0, 0),	(0, 0)),	# Moors
((0, 0),	(0, 0)),	# Spain
((0, 0),	(0, 0)),	# France
((0, 0),	(0, 0)),	# Khmer
((0, 0),	(0, 0)),	# England
((0, 0),	(0, 0)),	# Holy Rome
((0, 0),	(0, 0)),	# Russia
((0, 0),	(0, 0)),	# Mali
((0, 0),	(0, 0)),	# Poland
((0, 0),	(0, 0)),	# Portugal
((0, 0),	(0, 0)),	# Inca
((0, 0),	(0, 0)),	# Italy
((0, 0),	(0, 0)),	# Mongolia
((0, 0),	(0, 0)),	# Aztecs
((0, 0),	(0, 0)),	# Mughals
((0, 0),	(0, 0)),	# Ottomans
((0, 0),	(0, 0)),	# Thailand
((0, 0),	(0, 0)),	# Congo
((0, 0),	(0, 0)),	# Netherlands
((0, 0),	(0, 0)),	# Germany
((0, 0),	(0, 0)),	# America
((0, 0),	(0, 0)),	# Argentina
((0, 0),	(0, 0)),	# Brazil
((0, 0),	(0, 0)),	# Canada
)

dChangedBroaderArea = {
iCarthage :	((0, 0),	(0, 0)), 	# Carthage
iMaya :		((0, 0),	(0, 0)),	# Colombia
iByzantium :	((0, 0),	(0, 0)),
iHolyRome :	((0, 0),	(0, 0)),
iMughals :	((0, 0),	(0, 0)),
}

### Respawn area ###

dRespawnArea = {
iEgypt :	((74, 37), 	(83, 47)),
iChina :	((117, 44),	(129, 56)),
iIndia :	((103, 36),	(115, 47)),
iByzantium :	((74, 50),	(80, 56)),
iMoors :	((0, 0),	(0, 0)),
iInca :		((0, 0),	(0, 0)),
iMughals :	((0, 0),	(0, 0)),
}

dRespawnAreaExceptions = {
iIndia : [],
iMoors : [],
iInca : [],
}

### Rebirth area ###

dRebirthPlot = {
iPersia : (94, 50),	# Esfahan (Iran)
iMaya : (29, 34),		# Bogota (Colombia)
iAztecs : (0, 0),	# Mexico City (Mexico)
}

dRebirthArea = {
iPersia :	((91, 44),	(100, 50)),	# Iran
iMaya : ((25, 29),	(35, 38)),	# Colombia
iAztecs :	((0, 0),	(0, 0)),	# Mexico
}

dRebirthAreaExceptions = {
iAztecs : [],
}