# coding: utf-8

from CvPythonExtensions import *
import CvUtil
import PyHelpers
from Consts import *
import Victory as vic
from StoredData import data
from RFCUtils import utils
import CityNameManager as cnm
import Areas

### Constants ###

gc = CyGlobalContext()
localText = CyTranslator()

encoding = "utf-8"

tBrazilTL = (32, 14)
tBrazilBR = (43, 30)
tNCAmericaTL = (3, 33)
tNCAmericaBR = (37, 63)

tBritainTL = (48, 53)
tBritainBR = (54, 60)

tEuropeanRussiaTL = (68, 50)
tEuropeanRussiaBR = (80, 62)
tEuropeanRussiaExceptions = ((68, 59), (68, 60), (68, 61), (68, 62))

tKhazariaTL = (71, 46)
tKhazariaBR = (79, 53)
tAnatoliaTL = (69, 41)
tAnatoliaBR = (75, 45)
iTurkicEastWestBorder = 89

### Setup methods ###

def findCapitalLocations(dCapitals):
	dLocations = {}
	for iPlayer in dCapitals:
		for sCapital in dCapitals[iPlayer]:
			dLocations[sCapital] = cnm.findLocations(iPlayer, sCapital)
	return dLocations

### Dictionaries with text keys

dDefaultInsertNames = {
	iVikings : "TXT_KEY_CIV_VIKINGS_SCANDINAVIA",
	iKhmer : "TXT_KEY_CIV_KHMER_KAMPUCHEA",
	iNetherlands : "TXT_KEY_CIV_NETHERLANDS_ARTICLE",
	iTamils : "TXT_KEY_CIV_TAMILS_TAMIL_NADU",
	iMaya : "TXT_KEY_CIV_MAYA_YUCATAN",
	iThailand : "TXT_KEY_CIV_THAILAND_SIAM",
	iMoors : "TXT_KEY_CIV_MOORS_MOROCCO",
	iMughals : "TXT_KEY_CIV_MUGHALS_DELHI",
	iHarappa : "TXT_KEY_CIV_HARAPPA_INDUS",
	iBoers : "TXT_KEY_CIV_BOER_SOUTH_AFRICA",
}

dDefaultInsertAdjectives = {
	iVikings : "TXT_KEY_CIV_VIKINGS_SCANDINAVIAN",
	iKhmer : "TXT_KEY_CIV_KHMER_KAMPUCHEAN",
	iThailand : "TXT_KEY_CIV_THAILAND_SIAMESE",
	iMoors : "TXT_KEY_CIV_MOORS_MOROCCAN",
}

dSpecificVassalTitles = {
	iEgypt : {
		iPhoenicia : "TXT_KEY_CIV_EGYPTIAN_PHOENICIA",
		iEthiopia : "TXT_KEY_CIV_EGYPTIAN_ETHIOPIA",
	},
	iBabylonia : {
		iPhoenicia : "TXT_KEY_ADJECTIVE_TITLE",
	},
	iChina : {
		iKorea : "TXT_KEY_CIV_CHINESE_KOREA",
		iTurks : "TXT_KEY_CIV_CHINESE_TURKS",
		iMongolia : "TXT_KEY_CIV_CHINESE_MONGOLIA",
	},
	iGreece : {
		iIndia : "TXT_KEY_CIV_GREEK_INDIA",
		iEgypt : "TXT_KEY_CIV_GREEK_EGYPT",
		iPersia : "TXT_KEY_CIV_GREEK_PERSIA",
		iRome : "TXT_KEY_CIV_GREEK_ROME",
	},
	iIndia : {
		iAztecs: "TXT_KEY_CIV_INDIAN_AZTECS",
	},
	iPersia : {
		iEgypt : "TXT_KEY_CIV_PERSIAN_EGYPT",
		iIndia : "TXT_KEY_CIV_PERSIAN_INDIA",
		iBabylonia : "TXT_KEY_CIV_PERSIAN_BABYLONIA",
		iGreece : "TXT_KEY_CIV_PERSIAN_GREECE",
		iEthiopia : "TXT_KEY_CIV_PERSIAN_ETHIOPIA",
		iArabia : "TXT_KEY_CIV_PERSIAN_ARABIA",
		iMongolia : "TXT_KEY_CIV_PERSIAN_MONGOLIA",
	},
	iJapan : {
		iChina : "TXT_KEY_CIV_JAPANESE_CHINA",
		iIndia : "TXT_KEY_CIV_JAPANESE_INDIA",
		iKorea : "TXT_KEY_CIV_JAPANESE_KOREA",
		iMongolia : "TXT_KEY_CIV_JAPANESE_MONGOLIA",
	},
	iByzantium : {
		iEgypt : "TXT_KEY_CIV_BYZANTINE_EGYPT",
		iBabylonia : "TXT_KEY_CIV_BYZANTINE_BABYLONIA",
		iGreece : "TXT_KEY_CIV_BYZANTINE_GREECE",
		iPhoenicia : "TXT_KEY_CIV_BYZANTINE_CARTHAGE",
		iPersia : "TXT_KEY_CIV_BYZANTINE_PERSIA",
		iRome : "TXT_KEY_CIV_BYZANTINE_ROME",
		iSpain : "TXT_KEY_CIV_BYZANTINE_SPAIN",
		iMamluks : "TXT_KEY_CIV_BYZANTINE_EGYPT",
	},
	iVikings : {
		iEngland : "TXT_KEY_CIV_VIKING_ENGLAND",
		iRussia : "TXT_KEY_CIV_VIKING_RUSSIA",
	},
	iArabia : {
		iOttomans : "TXT_KEY_CIV_ARABIAN_OTTOMANS",
		iMughals : "TXT_KEY_CIV_ARABIAN_MUGHALS",
		iIsrael : "TXT_KEY_CIV_ARABIAN_ISRAEL",
	},
	iMoors : {
		iArabia : "TXT_KEY_CIV_MOORISH_ARABIA",
		iMali : "TXT_KEY_CIV_MOORISH_MALI",
	},
	iSpain : {
		iPhoenicia : "TXT_KEY_CIV_SPANISH_CARTHAGE",
		iEthiopia : "TXT_KEY_CIV_SPANISH_ETHIOPIA",
		iMaya : "TXT_KEY_CIV_SPANISH_MAYA",
		iByzantium : "TXT_KEY_CIV_SPANISH_BYZANTIUM",
		iIndonesia : "TXT_KEY_CIV_SPANISH_INDONESIA",
		iMoors : "TXT_KEY_CIV_SPANISH_MOORS",
		iFrance : "TXT_KEY_CIV_SPANISH_FRANCE",
		iNetherlands : "TXT_KEY_ADJECTIVE_TITLE",
		iMali : "TXT_KEY_CIV_SPANISH_MALI",
		iPortugal : "TXT_KEY_CIV_SPANISH_PORTUGAL",
		iAmerica : "TXT_KEY_CIV_SPANISH_AMERICA",
		iArgentina : "TXT_KEY_CIV_SPANISH_ARGENTINA",
	},
	iFrance : {
		iEgypt : "TXT_KEY_MANDATE_OF",
		iBabylonia : "TXT_KEY_CIV_FRENCH_BABYLONIA",
		iGreece : "TXT_KEY_CIV_FRANCE_DEPARTEMENTS_OF",
		iPersia : "TXT_KEY_MANDATE_OF",
		iPhoenicia : "TXT_KEY_CIV_FRENCH_PHOENICIA",
		iItaly : "TXT_KEY_CIV_FRENCH_ITALY",
		iEthiopia : "TXT_KEY_CIV_FRENCH_ETHIOPIA",
		iByzantium : "TXT_KEY_CIV_FRENCH_BYZANTIUM",
		iVikings : "TXT_KEY_CIV_FRANCE_DEPARTEMENTS_OF",
		iArabia : "TXT_KEY_MANDATE_OF",
		iEngland : "TXT_KEY_CIV_FRENCH_ENGLAND",
		iSpain : "TXT_KEY_CIV_FRENCH_SPAIN",
		iHolyRome : "TXT_KEY_CIV_FRENCH_HOLY_ROME",
		iRussia : "TXT_KEY_CIV_FRANCE_DEPARTEMENTS_OF",
		iPoland : "TXT_KEY_CIV_FRENCH_POLAND",
		iNetherlands : "TXT_KEY_CIV_FRENCH_NETHERLANDS",
		iMamluks : "TXT_KEY_MANDATE_OF",
		iMali : "TXT_KEY_CIV_FRENCH_MALI",
		iPortugal : "TXT_KEY_CIV_FRANCE_DEPARTEMENTS_OF",
		iInca : "TXT_KEY_CIV_FRENCH_INCA",
		iAztecs : "TXT_KEY_CIV_FRENCH_AZTECS",
		iMughals : "TXT_KEY_MANDATE_OF",
		iCongo : "TXT_KEY_ADJECTIVE_TITLE",
		iOttomans : "TXT_KEY_MANDATE_OF",
		iAmerica : "TXT_KEY_CIV_FRENCH_AMERICA",
		iIsrael : "TXT_KEY_CIV_FRENCH_ISRAEL",
	},
	iEngland : {
		iEgypt : "TXT_KEY_MANDATE_OF",
		iIndia : "TXT_KEY_CIV_ENGLISH_INDIA",
		iBabylonia : "TXT_KEY_CIV_ENGLISH_BABYLONIA",
		iPersia : "TXT_KEY_MANDATE_OF",
		iPhoenicia : "TXT_KEY_CIV_ENGLISH_PHOENICIA",
		iEthiopia : "TXT_KEY_CIV_ENGLISH_ETHIOPIA",
		iMaya : "TXT_KEY_CIV_ENGLISH_MAYA",
		iByzantium : "TXT_KEY_CIV_ENGLISH_BYZANTIUM",
		iVikings : "TXT_KEY_CIV_ENGLISH_VIKINGS",
		iArabia : "TXT_KEY_MANDATE_OF",
		iIndonesia : "TXT_KEY_CIV_ENGLISH_INDONESIA",
		iFrance : "TXT_KEY_CIV_ENGLISH_FRANCE",
		iHolyRome : "TXT_KEY_CIV_ENGLISH_HOLY_ROME",
		iGermany : "TXT_KEY_CIV_ENGLISH_GERMANY",
		iNetherlands : "TXT_KEY_CIV_ENGLISH_NETHERLANDS",
		iMamluks : "TXT_KEY_MANDATE_OF",
		iMali : "TXT_KEY_CIV_ENGLISH_MALI",
		iOttomans : "TXT_KEY_MANDATE_OF",
		iAmerica : "TXT_KEY_CIV_ENGLISH_AMERICA",
		iIsrael : "TXT_KEY_CIV_ENGLISH_ISRAEL",
	},
	iHolyRome : {
		iItaly : "TXT_KEY_CIV_HOLY_ROMAN_ITALY",
		iFrance : "TXT_KEY_CIV_HOLY_ROMAN_FRANCE",
		iNetherlands : "TXT_KEY_CIV_HOLY_ROMAN_NETHERLANDS",
		iByzantium : "TXT_KEY_CIV_HOLY_ROMAN_BYZANTIUM",
		iPoland : "TXT_KEY_CIV_HOLY_ROMAN_POLAND",
	},
	iRussia : {
		iTurks : "TXT_KEY_ADJECTIVE_TITLE",
		iPoland : "TXT_KEY_CIV_RUSSIAN_POLAND",
		iAmerica : "TXT_KEY_ADJECTIVE_TITLE",
	},
	iNetherlands : {
		iIndonesia : "TXT_KEY_CIV_DUTCH_INDONESIA",
		iMali : "TXT_KEY_CIV_DUTCH_MALI",
		iEthiopia : "TXT_KEY_CIV_DUTCH_ETHIOPIA",
		iCongo : "TXT_KEY_CIV_DUTCH_CONGO",
		iAmerica : "TXT_KEY_CIV_DUTCH_AMERICA",
		iBrazil : "TXT_KEY_CIV_DUTCH_BRAZIL",
	},
	iPortugal : {
		iIndia : "TXT_KEY_CIV_PORTUGUESE_INDIA",
		iIndonesia : "TXT_KEY_CIV_PORTUGUESE_INDIA",
		iMali : "TXT_KEY_CIV_PORTUGUESE_MALI",
		iCongo : "TXT_KEY_CIV_PORTUGUESE_CONGO",
		iBrazil : "TXT_KEY_CIV_PORTUGUESE_BRAZIL",
	},
	iMongolia : {
		iEgypt : "TXT_KEY_CIV_MONGOL_ILKHANATE",
		iChina : "TXT_KEY_CIV_MONGOL_CHINA",
		iBabylonia : "TXT_KEY_CIV_MONGOL_BABYLONIA",
		iGreece : "TXT_KEY_CIV_MONGOL_ILKHANATE",
		iPersia : "TXT_KEY_CIV_MONGOL_ILKHANATE",
		iPhoenicia : "TXT_KEY_CIV_MONGOL_PHOENICIA",
		iRome : "TXT_KEY_CIV_MONGOL_ILKHANATE",
		iByzantium : "TXT_KEY_CIV_MONGOL_BYZANTIUM",
		iRussia : "TXT_KEY_CIV_MONGOL_RUSSIA",
		iOttomans : "TXT_KEY_CIV_MONGOL_OTTOMANS",
		iMughals : "TXT_KEY_CIV_MONGOL_MUGHALS",
		iMamluks : "TXT_KEY_CIV_MONGOL_ILKHANATE",
	},
	iMughals : {
		iIndia : "TXT_KEY_CIV_MUGHAL_INDIA",
	},
	iOttomans : {
		iEgypt : "TXT_KEY_CIV_OTTOMAN_EGYPT",
		iBabylonia : "TXT_KEY_CIV_OTTOMAN_BABYLONIA",
		iPersia : "TXT_KEY_CIV_OTTOMAN_PERSIA",
		iGreece : "TXT_KEY_CIV_OTTOMAN_GREECE",
		iPhoenicia : "TXT_KEY_CIV_OTTOMAN_PHOENICIA",
		iEthiopia : "TXT_KEY_CIV_OTTOMAN_ETHIOPIA",
		iByzantium : "TXT_KEY_CIV_OTTOMAN_BYZANTIUM",
		iArabia : "TXT_KEY_CIV_OTTOMAN_ARABIA",
		iIndonesia : "TXT_KEY_CIV_OTTOMAN_INDONESIA",
		iRussia : "TXT_KEY_CIV_OTTOMAN_RUSSIA",
		iMamluks : "TXT_KEY_CIV_TURKISH_EGYPT",
		iIsrael : "TXT_KEY_CIV_OTTOMAN_ISRAEL",
	},
	iGermany : {
		iHolyRome : "TXT_KEY_CIV_GERMAN_HOLY_ROME",
		iMali : "TXT_KEY_CIV_GERMAN_MALI",
		iEthiopia : "TXT_KEY_CIV_GERMAN_ETHIOPIA",
		iPoland : "TXT_KEY_CIV_GERMAN_POLAND",
	},
	iAmerica : {
		iEngland : "TXT_KEY_CIV_AMERICAN_ENGLAND",
		iJapan : "TXT_KEY_CIV_AMERICAN_JAPAN",
		iGermany : "TXT_KEY_CIV_AMERICAN_GERMANY",
		iAztecs : "TXT_KEY_CIV_AMERICAN_MEXICO",
		iMaya : "TXT_KEY_CIV_AMERICAN_MAYA",
		iKorea : "TXT_KEY_CIV_AMERICAN_KOREA",
	},
	iBrazil : {
		iArgentina : "TXT_KEY_CIV_BRAZILIAN_ARGENTINA",
	},
	iBoers	: {
		iEngland : "TXT_KEY_CIV_BOER_ENGLAND",
		iNetherlands : "TXT_KEY_CIV_BOER_NETHERLANDS",
	}
}

dMasterTitles = {
	iChina : "TXT_KEY_CIV_CHINESE_VASSAL",
	iIndia : "TXT_KEY_CIV_INDIAN_VASSAL",
	iPersia : "TXT_KEY_CIV_PERSIAN_VASSAL",
	iRome : "TXT_KEY_CIV_ROMAN_VASSAL",
	iJapan : "TXT_KEY_CIV_JAPANESE_VASSAL",
	iByzantium : "TXT_KEY_CIV_BYZANTINE_VASSAL",
	iTurks : "TXT_KEY_CIV_TURKIC_VASSAL",
	iArabia : "TXT_KEY_CIV_ARABIAN_VASSAL",
	iTibet : "TXT_KEY_CIV_TIBETAN_VASSAL",
	iIndonesia : "TXT_KEY_CIV_INDONESIAN_VASSAL",
	iMoors : "TXT_KEY_CIV_ARABIAN_VASSAL",
	iSpain : "TXT_KEY_CIV_SPANISH_VASSAL",
	iFrance : "TXT_KEY_ADJECTIVE_TITLE",
	iEngland : "TXT_KEY_CIV_ENGLISH_VASSAL",
	iRussia : "TXT_KEY_CIV_RUSSIAN_VASSAL",
	iNetherlands : "TXT_KEY_ADJECTIVE_TITLE",
	iPortugal : "TXT_KEY_ADJECTIVE_TITLE",
	iMongolia : "TXT_KEY_CIV_MONGOL_VASSAL",
	iMughals : "TXT_KEY_CIV_MUGHAL_VASSAL",
	iOttomans : "TXT_KEY_CIV_OTTOMAN_VASSAL",
	iThailand : "TXT_KEY_CIV_THAI_VASSAL",
}

dCommunistVassalTitlesGeneric = {
	iRussia : "TXT_KEY_CIV_RUSSIA_SOVIET",
}

dCommunistVassalTitles = {
	iRussia : {
		iChina : "TXT_KEY_CIV_RUSSIA_SOVIET_REPUBLIC_ADJECTIVE",
		iTurks : "TXT_KEY_CIV_RUSSIA_SOVIET_TURKS",
		iJapan : "TXT_KEY_CIV_RUSSIA_SOVIET_JAPAN",
		iOttomans : "TXT_KEY_CIV_RUSSIA_SOVIET_OTTOMANS",
		iGermany : "TXT_KEY_CIV_RUSSIA_SOVIET_GERMANY",
	},
}

dFascistVassalTitlesGeneric = {
	iGermany : "TXT_KEY_ADJECTIVE_TITLE"
}

dFascistVassalTitles = {
	iGermany : {
		iEgypt : "TXT_KEY_CIV_GERMANY_REICHSPROTEKTORAT",
		iChina : "TXT_KEY_CIV_GERMANY_REICHSKOMMISSARIAT",
		iGreece : "TXT_KEY_CIV_GERMANY_NAZI_GREECE",
		iPhoenicia : "TXT_KEY_CIV_GERMANY_REICHSKOMMISSARIAT",
		iRome : "TXT_KEY_CIV_GERMANY_REICHSPROTEKTORAT",
		iEthiopia : "TXT_KEY_CIV_GERMANY_NAZI_ETHIOPIA",
		iByzantium : "TXT_KEY_CIV_GERMANY_NAZI_BYZANTIUM",
		iSpain : "TXT_KEY_CIV_GERMANY_REICHSKOMMISSARIAT",
		iFrance : "TXT_KEY_CIV_GERMANY_NAZI_FRANCE",
		iEngland : "TXT_KEY_CIV_GERMANY_REICHSKOMMISSARIAT",
		iHolyRome : "TXT_KEY_CIV_GERMANY_NAZI_HOLY_ROME",
		iRussia : "TXT_KEY_CIV_GERMANY_NAZI_RUSSIA",
		iNetherlands : "TXT_KEY_CIV_GERMANY_NAZI_NETHERLANDS",
		iMamluks : "TXT_KEY_CIV_GERMANY_REICHSPROTEKTORAT",
		iMali : "TXT_KEY_CIV_GERMANY_NAZI_MALI",
		iPoland : "TXT_KEY_CIV_GERMANY_NAZI_POLAND",
		iPortugal : "TXT_KEY_CIV_GERMANY_REICHSKOMMISSARIAT",
		iMughals : "TXT_KEY_CIV_GERMANY_NAZI_MUGHALS",
		iOttomans : "TXT_KEY_CIV_GERMANY_REICHSKOMMISSARIAT",
		iCanada : "TXT_KEY_CIV_GERMANY_NAZI_CANADA",
	},
}

dForeignAdjectives = {
	iChina : {
		iEgypt : "TXT_KEY_CIV_CHINESE_ADJECTIVE_EGYPT",
		iIndia : "TXT_KEY_CIV_CHINESE_ADJECTIVE_INDIA",
		iBabylonia : "TXT_KEY_CIV_CHINESE_ADJECTIVE_BABYLONIA",
		iPersia : "TXT_KEY_CIV_CHINESE_ADJECTIVE_PERSIA",
		iRome : "TXT_KEY_CIV_CHINESE_ADJECTIVE_ROME",
		iJapan : "TXT_KEY_CIV_CHINESE_ADJECTIVE_JAPAN",
		iKorea : "TXT_KEY_CIV_CHINESE_ADJECTIVE_KOREA",
		iByzantium : "TXT_KEY_CIV_CHINESE_ADJECTIVE_BYZANTIUM",
		iArabia : "TXT_KEY_CIV_CHINESE_ADJECTIVE_ARABIA",
		iKhmer : "TXT_KEY_CIV_CHINESE_ADJECTIVE_KHMER",
		iIndonesia : "TXT_KEY_CIV_CHINESE_ADJECTIVE_INDONESIA",
		iMongolia : "TXT_KEY_CIV_CHINESE_ADJECTIVE_MONGOLIA",
		iOttomans : "TXT_KEY_CIV_CHINESE_ADJECTIVE_OTTOMANS",
		iTibet : "TXT_KEY_CIV_CHINESE_ADJECTIVE_TIBET",
		iVietnam : "TXT_KEY_CIV_CHINESE_ADJECTIVE_VIETNAM",
		iMamluks : "TXT_KEY_CIV_CHINESE_ADJECTIVE_EGYPT",
	},
}

dForeignNames = {
	iGreece : {
		iTurks : "TXT_KEY_CIV_GREEK_NAME_TURKS",
	},
	iPersia : {
		iByzantium : "TXT_KEY_CIV_PERSIAN_NAME_BYZANTIUM",
		iTurks : "TXT_KEY_CIV_PERSIAN_NAME_TURKS",
		iIndonesia : "TXT_KEY_CIV_PERSIAN_NAME_INDONESIA",
	},
	iRome : {
		iEgypt : "TXT_KEY_CIV_ROMAN_NAME_EGYPT",
		iChina : "TXT_KEY_CIV_ROMAN_NAME_CHINA",
		iBabylonia : "TXT_KEY_CIV_ROMAN_NAME_BABYLONIA",
		iGreece : "TXT_KEY_CIV_ROMAN_NAME_GREECE",
		iPersia : "TXT_KEY_CIV_ROMAN_NAME_PERSIA",
		iPhoenicia : "TXT_KEY_CIV_ROMAN_NAME_PHOENICIA",
		iEthiopia : "TXT_KEY_CIV_ROMAN_NAME_ETHIOPIA",
		iByzantium : "TXT_KEY_CIV_ROMAN_NAME_BYZANTIUM",
		iVikings : "TXT_KEY_CIV_ROMAN_NAME_VIKINGS",
		iTurks : "TXT_KEY_CIV_ROMAN_NAME_TURKS",
		iKhmer : "TXT_KEY_CIV_ROMAN_NAME_KHMER",
		iSpain : "TXT_KEY_CIV_ROMAN_NAME_SPAIN",
		iFrance : "TXT_KEY_CIV_ROMAN_NAME_FRANCE",
		iEngland : "TXT_KEY_CIV_ROMAN_NAME_ENGLAND",
		iHolyRome : "TXT_KEY_CIV_ROMAN_NAME_HOLY_ROME",
		iGermany : "TXT_KEY_CIV_ROMAN_NAME_GERMANY",
		iRussia : "TXT_KEY_CIV_ROMAN_NAME_RUSSIA",
		iNetherlands : "TXT_KEY_CIV_ROMAN_NAME_NETHERLANDS",
		iMali : "TXT_KEY_CIV_ROMAN_NAME_MALI",
		iPortugal : "TXT_KEY_CIV_ROMAN_NAME_PORTUGAL",
		iMongolia : "TXT_KEY_CIV_ROMAN_NAME_MONGOLIA",
		iOttomans : "TXT_KEY_CIV_ROMAN_NAME_OTTOMANS",
		iThailand : "TXT_KEY_CIV_ROMAN_NAME_THAILAND",
		iMamluks : "TXT_KEY_CIV_ROMAN_NAME_EGYPT",
	},
	iArabia : {
		iEgypt : "TXT_KEY_CIV_ARABIAN_NAME_EGYPT",
		iBabylonia : "TXT_KEY_CIV_ARABIAN_NAME_BABYLONIA",
		iPersia : "TXT_KEY_CIV_ARABIAN_NAME_PERSIA",
		iPhoenicia : "TXT_KEY_CIV_ARABIAN_NAME_CARTHAGE",
		iRome : "TXT_KEY_CIV_ARABIAN_NAME_ROME",
		iEthiopia : "TXT_KEY_CIV_ARABIAN_NAME_ETHIOPIA",
		iByzantium : "TXT_KEY_CIV_ARABIAN_NAME_BYZANTIUM",
		iTurks : "TXT_KEY_CIV_ARABIAN_NAME_TURKS",
		iArabia : "TXT_KEY_CIV_ARABIAN_NAME_ARABIA",
		iIndonesia : "TXT_KEY_CIV_ARABIAN_NAME_INDONESIA",
		iMoors : "TXT_KEY_CIV_ARABIAN_NAME_MOORS",
		iSpain : "TXT_KEY_CIV_ARABIAN_NAME_SPAIN",
		iPortugal : "TXT_KEY_CIV_ARABIAN_NAME_PORTUGAL",
		iMamluks : "TXT_KEY_CIV_ARABIAN_NAME_EGYPT",
	},
	iTibet : {
		iChina : "TXT_KEY_CIV_TIBETAN_NAME_CHINA",
		iIndia : "TXT_KEY_CIV_TIBETAN_NAME_INDIA",
		iTurks : "TXT_KEY_CIV_TIBETAN_NAME_TURKS",
		iMongolia : "TXT_KEY_CIV_TIBETAN_NAME_MONGOLIA",
	},
	iMoors : {
		iEgypt : "TXT_KEY_CIV_ARABIAN_NAME_EGYPT",
		iBabylonia : "TXT_KEY_CIV_ARABIAN_NAME_BABYLONIA",
		iPersia : "TXT_KEY_CIV_ARABIAN_NAME_PERSIA",
		iPhoenicia : "TXT_KEY_CIV_ARABIAN_NAME_CARTHAGE",
		iRome : "TXT_KEY_CIV_ARABIAN_NAME_ROME",
		iEthiopia : "TXT_KEY_CIV_ARABIAN_NAME_ETHIOPIA",
		iByzantium : "TXT_KEY_CIV_ARABIAN_NAME_BYZANTIUM",
		iArabia : "TXT_KEY_CIV_ARABIAN_NAME_ARABIA",
		iMoors : "TXT_KEY_CIV_ARABIAN_NAME_MOORS",
		iSpain : "TXT_KEY_CIV_ARABIAN_NAME_SPAIN",
		iPortugal : "TXT_KEY_CIV_ARABIAN_NAME_PORTUGAL",
		iMamluks : "TXT_KEY_CIV_ARABIAN_NAME_EGYPT",
	},
	iSpain : {
		iKhmer : "TXT_KEY_CIV_SPANISH_NAME_KHMER",
		iAztecs : "TXT_KEY_CIV_SPANISH_NAME_AZTECS",
		iMughals : "TXT_KEY_CIV_SPANISH_NAME_MUGHALS",
	},
	iFrance : {
		iKhmer : "TXT_KEY_CIV_FRENCH_NAME_KHMER",
		iMughals : "TXT_KEY_CIV_FRENCH_NAME_MUGHALS",
		iVietnam : "TXT_KEY_CIV_FRENCH_NAME_VIETNAM",
	},
	iEngland : {
		iKhmer : "TXT_KEY_CIV_ENGLISH_NAME_KHMER",
		iMughals : "TXT_KEY_CIV_ENGLISH_NAME_MUGHALS",
	},
	iRussia : {
		iPersia : "TXT_KEY_CIV_RUSSIAN_NAME_PERSIA",
	},
	iMongolia : {
		iTurks : "TXT_KEY_CIV_MONGOL_NAME_TURKS"
	},
	iGermany : {
		iMoors : "TXT_KEY_CIV_GERMAN_NAME_MOORS",
	},
}

lMonarchyOf = [iEthiopia, iKorea]
lMonarchyAdj = [iChina, iIndia, iRome]
lDuchy = [iHolyRome, iPoland, iRussia]

lRepublicOf = [iEgypt, iIndia, iChina, iPersia, iJapan, iEthiopia, iKorea, iVikings, iTurks, iTibet, iIndonesia, iKhmer, iHolyRome, iMali, iPoland, iMughals, iOttomans, iThailand, iPhilippines, iVietnam, iMamluks]

lRepublicAdj = [iBabylonia, iRome, iMoors, iSpain, iFrance, iPortugal, iInca, iItaly, iAztecs, iArgentina, iAustralia]

lSocialistRepublicOf = [iMoors, iHolyRome, iBrazil, iVikings]
lSocialistRepublicAdj = [iPersia, iTurks, iItaly, iAztecs, iArgentina]

lPeoplesRepublicOf = [iIndia, iChina, iPolynesia, iJapan, iTibet, iIndonesia, iMali, iPoland, iMughals, iThailand, iCongo]
lPeoplesRepublicAdj = [iTamils, iByzantium, iMongolia]

lIslamicRepublicOf = [iIndia, iPersia, iMali, iMughals]

lCityStatesStart = [iRome, iCarthage, iGreece, iIndia, iMaya, iAztecs]

dEmpireThreshold = {
	iBabylonia : 2,
	iCarthage : 4,
	iIndonesia : 4,
	iTeotihuacan : 3,
	iKorea : 4,
	iRussia : 8,
	iHolyRome : 3,
	iGermany : 4,
	iItaly : 4,
	iInca : 3,
	iMongolia : 6,
	iPoland : 3,
	iMoors : 3,
	iTibet : 3,
	iPolynesia : 3,
	iTamils : 3,
	iSwahili : 4,
}

lChristianity = [iCatholicism, iOrthodoxy, iProtestantism]

lRespawnNameChanges = [iEgypt, iHolyRome, iInca, iAztecs, iMali]
lVassalNameChanges = [iInca, iAztecs, iMughals]
lChristianityNameChanges = [iInca, iAztecs]

lRebirths = [iAztecs, iMaya, iPersia]
lColonies = [iMali, iEthiopia, iCongo, iAztecs, iInca, iMaya]

dNameChanges = {
	iPhoenicia : "TXT_KEY_CIV_CARTHAGE_SHORT_DESC",
	iAztecs : "TXT_KEY_CIV_MEXICO_SHORT_DESC",
	iInca : "TXT_KEY_CIV_PERU_SHORT_DESC",
	iHolyRome : "TXT_KEY_CIV_AUSTRIA_SHORT_DESC",
	iMali : "TXT_KEY_CIV_SONGHAI_SHORT_DESC",
	iMughals : "TXT_KEY_CIV_PAKISTAN_SHORT_DESC",
	iMoors : "TXT_KEY_CIV_MOROCCO_SHORT_DESC",
}

dAdjectiveChanges = {
	iPhoenicia : "TXT_KEY_CIV_CARTHAGE_ADJECTIVE",
	iAztecs : "TXT_KEY_CIV_MEXICO_ADJECTIVE",
	iInca : "TXT_KEY_CIV_PERU_ADJECTIVE",
	iHolyRome : "TXT_KEY_CIV_AUSTRIA_ADJECTIVE",
	iMali : "TXT_KEY_CIV_SONGHAI_ADJECTIVE",
	iMughals : "TXT_KEY_CIV_PAKISTAN_ADJECTIVE",
	iMoors : "TXT_KEY_CIV_MOROCCO_ADJECTIVE",
}

dCapitals = {
	iPolynesia : ["Kaua'i", "O'ahu", "Maui", "Manu'a", "Niue"],
	iBabylonia : ["Ninua", "Kalhu", "Akkad"],
	iTeotihuacan : ["Tollan"],
	iPhoenicia : ['Sur', 'Sydwn', 'Carthage'],
	iByzantium : ["Dyrrachion", "Athena", "Konstantinoupolis"],
	iVikings : ["Oslo", "Nidaros", "Roskilde", "Stockholm", "Kalmar"],
	iKhmer : ["Pagan", "Dali", "Angkor", "Hanoi"],
	iHolyRome : ["Buda"],
	iRussia : ["Moskva", "Kiev"],
	iItaly : ["Fiorenza", "Roma"],
	iTamils : ["Madurai", "Thiruvananthapuram", "Cochin", "Kozhikode"],
	iArabia : ["Dimashq"],
	iSpain : ["La Paz", "Barcelona", "Valencia"],
	iPoland : ["Kowno", "Medvegalis", "Wilno", "Ryga"],
	iNetherlands : ["Brussels", "Antwerpen"],
	iPhilippines : ["Tondo", "Butuan"],
	iBoers : ["Pretoria", "Johannesburg", "Pietermaritzburg", "Durban"],
}

dCapitalLocations = findCapitalLocations(dCapitals)

dStartingLeaders = [
# 3000 BC
{
	iEgypt : iRamesses,
	iIndia : iAsoka,
	iChina : iQinShiHuang,
	iBabylonia : iSargon,
	iAssyria : iAshurbanipal,
	iHarappa : iVatavelli,
	iGreece : iPericles,
	iPersia : iCyrus,
	iCarthage : iHiram,
	iPolynesia : iAhoeitu,
	iRome : iJuliusCaesar,
	iJapan : iOdaNobunaga,
	iTamils : iRajendra,
	iEthiopia : iZaraYaqob,
	iTeotihuacan : iAtlatlCauac,
	iVietnam : iTrung,
	iKorea : iWangKon,
	iByzantium : iJustinian,
	iVikings : iRagnar,
	iTurks : iBumin,
	iArabia : iHarun,
	iTibet : iSongtsen,
	iKhmer : iSuryavarman,
	iIndonesia : iDharmasetu,
	iMoors : iRahman,
	iSpain : iIsabella,
	iFrance : iCharlemagne,
	iEngland : iAlfred,
	iHolyRome : iBarbarossa,
	iRussia : iIvan,
	iNetherlands : iWillemVanOranje,
	iPhilippines : iLapuLapu,
	iSwahili : iShirazi,
	iMamluks : iSaladin,
	iMali : iMansaMusa,
	iPoland : iCasimir,
	iPortugal : iAfonso,
	iInca : iHuaynaCapac,
	iItaly : iLorenzo,
	iMongolia : iGenghisKhan,
	iAztecs : iMontezuma,
	iMughals : iTughluq,
	iOttomans : iMehmed,
	iThailand : iNaresuan,
	iCongo : iMbemba,
	iSweden : iGustavVasa,
	iManchuria : iKangxi,
	iGermany : iFrederick,
	iAmerica : iWashington,
	iAustralia : iCurtin,
	iArgentina : iSanMartin,
	iBrazil : iPedro,
	iBoers : iKruger,
	iCanada : iMacDonald,
	iIsrael : iBenGurion,
},
# 600 AD
{
	iChina : iTaizong,
	iPersia : iKhosrow,
	iRome : iAugustus,
	iIndia : iChandragupta
},
# 1700 AD
{
	iChina : iHongwu,
	iIndia : iShahuji,
	iPersia : iAbbas,
	iVietnam : iHoChiMinh,
	iJapan : iOdaNobunaga,
	iVikings : iChristian,
	iSpain : iPhilip,
	iFrance : iLouis,
	iEngland : iVictoria,
	iHolyRome : iFrancis,
	iRussia : iPeter,
	iSweden : iKarl,
	iNetherlands : iWilliam,
	iPoland : iSobieski,
	iPortugal : iJoao,
	iMughals : iAkbar,
	iOttomans : iSuleiman,
	iGermany : iFrederick,
}]

### Event handlers

def setup():
	iScenario = utils.getScenario()

	if iScenario == i600AD:
		data.players[iChina].iAnarchyTurns += 3

	elif iScenario == i1700AD:
		# data.players[iEgypt].iResurrections += 1
		
		for iPlayer in [iMoors]:
			nameChange(iPlayer)
			adjectiveChange(iPlayer)

	for iPlayer in range(iNumPlayers):
		setDesc(iPlayer, peoplesName(iPlayer))

		if gc.getPlayer(iPlayer).getNumCities() > 0:
			checkName(iPlayer)

		setLeader(iPlayer, startingLeader(iPlayer))

		Areas.updateCore(iPlayer, [])

def onCivRespawn(iPlayer, tOriginalOwners):
	data.players[iPlayer].iResurrections += 1

	if iPlayer in lRespawnNameChanges:
		nameChange(iPlayer)
		adjectiveChange(iPlayer)

		checkShortAdjectiveCapitalLeaderCore(iPlayer)

	setDesc(iPlayer, defaultTitle(iPlayer))
	checkName(iPlayer)
	checkLeader(iPlayer)
	checkShortAdjectiveCapitalLeaderCore(iPlayer)

def onVassalState(iMaster, iVassal):
	if iVassal in lVassalNameChanges:
		if iVassal == iMughals and iMaster not in lCivGroups[0]: return

		data.players[iVassal].iResurrections += 1
		nameChange(iVassal)
		adjectiveChange(iVassal)

	checkName(iVassal)

	#checkShortAdjectiveCapitalLeaderCore(iMaster)

def onPlayerChangeStateReligion(iPlayer, iReligion):
	if iPlayer in lChristianityNameChanges and iReligion in lChristianity:
		data.players[iPlayer].iResurrections += 1
		nameChange(iPlayer)
		adjectiveChange(iPlayer)

	checkName(iPlayer)

	checkShortAdjectiveCapitalLeaderCore(iPlayer)

def onRevolution(iPlayer):
	data.players[iPlayer].iAnarchyTurns += 1
	
	if iPlayer == iMughals and isRepublic(iPlayer):
		nameChange(iPlayer)
	
	checkName(iPlayer)
	
	for iLoopPlayer in range(iNumPlayers):
		if gc.getTeam(iLoopPlayer).isVassal(iPlayer):
			checkName(iLoopPlayer)

	checkShortAdjectiveCapitalLeaderCore(iPlayer)
	
def onCityAcquired(iPreviousOwner, iNewOwner):
	checkName(iPreviousOwner)
	checkName(iNewOwner)
	checkShortAdjectiveCapitalLeaderCore(iPreviousOwner)
	checkShortAdjectiveCapitalLeaderCore(iNewOwner)
	
def onCityRazed(iOwner):
	checkName(iOwner)
	checkShortAdjectiveCapitalLeaderCore(iOwner)
	
def onCityBuilt(iOwner):
	checkName(iOwner)
	checkShortAdjectiveCapitalLeaderCore(iOwner)

def onTechAcquired(iPlayer, iTech):
	iEra = gc.getTechInfo(iTech).getEra()

	#if iPlayer == iVikings:
	#	if iEra == iRenaissance:
	#		if isCapital(iPlayer, ["Stockholm", "Kalmar"]):
	#			setShort(iVikings, text("TXT_KEY_CIV_SWEDEN_SHORT_DESC"))
	#			setAdjective(iVikings, text("TXT_KEY_CIV_SWEDEN_ADJECTIVE"))
			
	#		elif isCapital(iPlayer, ["Oslo", "Nidaros"]):
	#			setShort(iVikings, text("TXT_KEY_CIV_NORWAY_SHORT_DESC"))
	#			setAdjective(iVikings, text("TXT_KEY_CIV_NORWAY_ADJECTIVE"))
			
	#		elif isCapital(iPlayer, ["Roskilde"]):
	#			setShort(iVikings, text("TXT_KEY_CIV_DENMARK_SHORT_DESC"))
	#			setAdjective(iVikings, text("TXT_KEY_CIV_DENMARK_ADJECTIVE"))
				
	#if iPlayer == iMoors:
	#	if iEra == iIndustrial:
	#		capital = gc.getPlayer(iPlayer).getCapitalCity()
			
	#		if capital and capital.getRegionID() != rIberia:
	#			nameChange(iPlayer)
	#			adjectiveChange(iPlayer)
	#		else:
	#			setShort(iPlayer, short(iPlayer))
	#			setAdjective(iPlayer, civAdjective(iPlayer))

	checkName(iPlayer)

	checkShortAdjectiveCapitalLeaderCore(iPlayer)

def onPalaceMoved(iPlayer):
	capital = gc.getPlayer(iPlayer).getCapitalCity()
	iEra = gc.getPlayer(iPlayer).getCurrentEra()

	if iPlayer == iPhoenicia:
		if capital.getRegionID() not in [rMesopotamia, rAnatolia]:
			nameChange(iPlayer)
			adjectiveChange(iPlayer)
		else:
			setShort(iPlayer, short(iPlayer))
			setAdjective(iPlayer, civAdjective(iPlayer))
			
	#elif iPlayer == iVikings:
	#	if iEra >= iRenaissance:
	#		if isCapital(iPlayer, ["Stockholm", "Kalmar"]):
	#			setShort(iVikings, text("TXT_KEY_CIV_SWEDEN_SHORT_DESC"))
	#			setAdjective(iVikings, text("TXT_KEY_CIV_SWEDEN_ADJECTIVE"))
			
	#		elif isCapital(iPlayer, ["Oslo", "Nidaros"]):
	#			setShort(iVikings, text("TXT_KEY_CIV_NORWAY_SHORT_DESC"))
	#			setAdjective(iVikings, text("TXT_KEY_CIV_NORWAY_ADJECTIVE"))
			
	#		elif isCapital(iPlayer, ["Roskilde"]):
	#			setShort(iVikings, text("TXT_KEY_CIV_DENMARK_SHORT_DESC"))
	#			setAdjective(iVikings, text("TXT_KEY_CIV_DENMARK_ADJECTIVE"))
				
	#elif iPlayer == iMoors:
	#	if iEra >= iIndustrial:
	#		if capital.getRegionID() != rIberia:
	#			nameChange(iPlayer)
	#			adjectiveChange(iPlayer)
	#		else:
	#			setShort(iPlayer, short(iPlayer))
	#			setAdjective(iPlayer, civAdjective(iPlayer))

	checkName(iPlayer)

	checkShortAdjectiveCapitalLeaderCore(iPlayer)
	
def onReligionFounded(iPlayer):
	checkName(iPlayer)
	checkShortAdjectiveCapitalLeaderCore(iPlayer)

def checkTurn(iGameTurn):
	for iPlayer in range(iNumPlayers):
		checkName(iPlayer)
		checkLeader(iPlayer)
	
	#checkShortAdjectiveCapitalLeaderCore(iPlayer)

def checkName(iPlayer):
	if not gc.getPlayer(iPlayer).isAlive(): return
	if iPlayer >= iNumPlayers: return
	if gc.getPlayer(iPlayer).getNumCities() == 0: return
	setDesc(iPlayer, desc(iPlayer, title(iPlayer)))

def checkLeader(iPlayer):
	if not gc.getPlayer(iPlayer).isAlive(): return
	if iPlayer >= iNumPlayers: return
	#setLeader(iPlayer, getPolityLeader(iPlayer))
	setLeaderName(iPlayer, leaderName(iPlayer))

### Setter methods for player object ###

def setDesc(iPlayer, sName):
	try:
		gc.getPlayer(iPlayer).setCivDescription(sName)
	except:
		pass

def setShort(iPlayer, sShort):
	gc.getPlayer(iPlayer).setCivShortDescription(sShort)

def setAdjective(iPlayer, sAdj):
	gc.getPlayer(iPlayer).setCivAdjective(sAdj)

def setLeader(iPlayer, iLeader):
	if not iLeader: return
	if gc.getPlayer(iPlayer).getLeader() == iLeader: return
	gc.getPlayer(iPlayer).setLeader(iLeader)

def setLeaderName(iPlayer, sName):
	if not sName: return
	if gc.getLeaderHeadInfo(gc.getPlayer(iPlayer).getLeader()).getText() != sName:
		gc.getPlayer(iPlayer).setLeaderName(sName)

### Utility methods ###

def getOrElse(dDictionary, iPlayer, sDefault=None):
	if iPlayer in dDictionary: return dDictionary[iPlayer]
	return sDefault

def key(iPlayer, sSuffix):
	if sSuffix: sSuffix = "_" + sSuffix
	return "TXT_KEY_CIV_" + short(iPlayer).replace(" ", "_").upper() + sSuffix

def text(sTextKey, tInput=()):
	return localText.getText(sTextKey.encode(encoding), tInput)

def desc(iPlayer, sTextKey=str("%s1")):
	if isVassal(iPlayer): return text(sTextKey, (name(iPlayer), adjective(iPlayer), name(iPlayer, True), adjective(iPlayer, True)))

	return text(sTextKey, (name(iPlayer), adjective(iPlayer)))

def short(iPlayer):
	return gc.getPlayer(iPlayer).getCivilizationShortDescription(0)

def civAdjective(iPlayer):
	return gc.getPlayer(iPlayer).getCivilizationAdjective(0)

def capitalName(iPlayer):
	capital = gc.getPlayer(iPlayer).getCapitalCity()
	if capital:
		sCapitalName = cnm.getRenameName(iEngland, capital.getName())
		if sCapitalName: return sCapitalName
		else: return capital.getName()

	return short(iPlayer)

def nameChange(iPlayer):
	if iPlayer in dNameChanges:
		setShort(iPlayer, text(dNameChanges[iPlayer]))

def adjectiveChange(iPlayer):
	if iPlayer in dAdjectiveChanges:
		setAdjective(iPlayer, text(dAdjectiveChanges[iPlayer]))

def getColumn(iPlayer):
	lTechs = [gc.getTechInfo(iTech).getGridX() for iTech in range(iNumTechs) if gc.getTeam(iPlayer).isHasTech(iTech)]
	if not lTechs: return 0
	return max(lTechs)

### Utility methods for civilization status ###

def getCivics(iPlayer):
	pPlayer = gc.getPlayer(iPlayer)
	return (pPlayer.getCivics(i) for i in range(6))

def isCommunist(iPlayer):
	iGovernment, iLegitimacy, iSociety, iEconomy, _, _ = getCivics(iPlayer)

	if iLegitimacy == iVassalage: return False

	if iEconomy == iCentralPlanning: return True

	if iGovernment == iStateParty and iSociety != iTotalitarianism and iEconomy not in [iMerchantTrade, iFreeEnterprise]: return True

	return False

def isFascist(iPlayer):
	iGovernment, _, iSociety, _, _, _ = getCivics(iPlayer)

	if iSociety == iTotalitarianism: return True

	if iGovernment == iStateParty: return True

	return False

def isRepublic(iPlayer):
	iGovernment, iLegitimacy, _, _, _, _ = getCivics(iPlayer)

	if iGovernment == iDemocracy: return True

	if iGovernment in [iDespotism, iRepublic, iElective] and iLegitimacy == iConstitution: return True

	return False

def isCityStates(iPlayer):
	iGovernment, iLegitimacy, _, _, _, _ = getCivics(iPlayer)
	
	if iGovernment == iRepublic: return True
	
	if iLegitimacy not in [iAuthority, iCitizenship, iCentralism]: return False
	
	if iGovernment in [iElective, iDemocracy]: return True

	if iGovernment == iChiefdom and iPlayer in lCityStatesStart: return True

	return False


def isGrandDuchy(iPlayer):
	iGovernment, iLegitimacy, _, _, _, _ = getCivics(iPlayer)
	
	if iGovernment == iElective: return True
	
	return False

def isMonarchy(iPlayer):
	return not (isCommunist(iPlayer) or isFascist(iPlayer) or isRepublic(iPlayer) or isCityStates(iPlayer) or isGrandDuchy(iPlayer))

def isVassal(iPlayer):
	return utils.isAVassal(iPlayer)

def isCapitulated(iPlayer):
	return isVassal(iPlayer) and gc.getTeam(iPlayer).isCapitulated()

def getMaster(iPlayer):
	return utils.getMaster(iPlayer)


def isColonialEmpire(iPlayer):
	iGameTurn = gc.getGame().getGameTurn()
	pPlayer = gc.getPlayer(iPlayer)
	tPlayer = gc.getTeam(pPlayer.getTeam())
	iCivicGovernment, iCivicLegitimacy, iCivicSociety, iCivicEconomy, iCivicReligion, iCivicTerritory = getCivics(iPlayer)
	iNumCities = pPlayer.getNumCities()
	bReborn = pPlayer.isReborn()
	iReligion = pPlayer.getStateReligion()
	capital = gc.getPlayer(iPlayer).getCapitalCity()
	tCapitalCoords = capitalCoords(iPlayer)
	bAnarchy = pPlayer.isAnarchy()
	bCityStates = isCityStates(iPlayer)
	bTheocracy = (iCivicReligion == iTheocracy)
	bResurrected = data.players[iPlayer].iResurrections > 0
	bCapitulated = isCapitulated(iPlayer)
	iAnarchyTurns = data.players[iPlayer].iAnarchyTurns
	iEra = pPlayer.getCurrentEra()
	iGameEra = gc.getGame().getCurrentEra()
	bWar = isAtWar(iPlayer)
	bCityState = (iNumCities == 1)
	
	coreRegion = capital.getRegionID()
	coreContinent = utils.getContinent(coreRegion)
	iColonies = 0
	for city in utils.getCityList(iPlayer):
		cityRegion = city.getRegionID()
		if iEra <= iClassical:
			return True
		else:
			if utils.getContinent(cityRegion) != coreContinent:

				iColonies = iColonies + 1
	return iColonies > iNumCities - iColonies

def isEmpire(iPlayer):
	return gc.getPlayer(iPlayer).getNumCities() > getEmpireThreshold(iPlayer)

def getEmpireThreshold(iPlayer):
	if iPlayer in dEmpireThreshold: return dEmpireThreshold[iPlayer]

	if gc.getPlayer(iPlayer).isReborn():
		if iPlayer == iPersia: return 4
	
	iGameTurn = gc.getGame().getGameTurn()
	pPlayer = gc.getPlayer(iPlayer)
	tPlayer = gc.getTeam(pPlayer.getTeam())
	iCivicGovernment, iCivicLegitimacy, iCivicSociety, iCivicEconomy, iCivicReligion, iCivicTerritory = getCivics(iPlayer)
	iNumCities = pPlayer.getNumCities()
	bReborn = pPlayer.isReborn()
	iReligion = pPlayer.getStateReligion()
	capital = gc.getPlayer(iPlayer).getCapitalCity()
	tCapitalCoords = capitalCoords(iPlayer)
	bAnarchy = pPlayer.isAnarchy()
	bCityStates = isCityStates(iPlayer)
	bTheocracy = (iCivicReligion == iTheocracy)
	bResurrected = data.players[iPlayer].iResurrections > 0
	bCapitulated = isCapitulated(iPlayer)
	iAnarchyTurns = data.players[iPlayer].iAnarchyTurns
	iEra = pPlayer.getCurrentEra()
	iGameEra = gc.getGame().getCurrentEra()
	bWar = isAtWar(iPlayer)
	bCityState = (iNumCities == 1)
	

	return 3 + iEra

def isAtWar(iPlayer):
	for iTarget in range(iNumPlayers):
		if gc.getTeam(iPlayer).isAtWar(iTarget) and gc.getPlayer(iTarget).isAlive():
			return True
	return False

def isCapital(iPlayer, lNames):
	capital = gc.getPlayer(iPlayer).getCapitalCity()
	if not capital: return False

	tLocation = (capital.getX(), capital.getY())

	for sName in lNames:
		if tLocation in dCapitalLocations[sName]:
			return True

	return False

def countAreaCities(tTL, tBR, tExceptions=()):
	return len(utils.getAreaCities(utils.getPlotList(tTL, tBR, tExceptions)))

def countPlayerAreaCities(iPlayer, tTL, tBR, tExceptions=()):
	return len(utils.getAreaCitiesCiv(iPlayer, utils.getPlotList(tTL, tBR, tExceptions)))

def isAreaControlled(iPlayer, tTL, tBR, iMinCities=1, tExceptions=()):
	iTotalCities = countAreaCities(tTL, tBR, tExceptions)
	iPlayerCities = countPlayerAreaCities(iPlayer, tTL, tBR, tExceptions)

	if iPlayerCities < iTotalCities: return False
	if iPlayerCities < iMinCities: return False

	return True

def capitalCoords(iPlayer):
	capital = gc.getPlayer(iPlayer).getCapitalCity()
	if capital: return (capital.getX(), capital.getY())

	return (-1, -1)

def controlsHolyCity(iPlayer, iReligion):
	holyCity = gc.getGame().getHolyCity(iReligion)
	if holyCity and holyCity.getOwner() == iPlayer: return True

	return False

def controlsCity(iPlayer, tPlot):
	x, y = tPlot
	plot = gc.getMap().plot(x, y)

	return plot.isCity() and plot.getPlotCity().getOwner() == iPlayer

### Naming methods ###

def name(iPlayer, bIgnoreVassal = False):
	if isCapitulated(iPlayer) and not bIgnoreVassal:
		sVassalName = vassalName(iPlayer, getMaster(iPlayer))
		if sVassalName: return sVassalName

	sName = getPolityTitleName(iPlayer)
	if sName:
		return sName

	if isCommunist(iPlayer) or isFascist(iPlayer) or isRepublic(iPlayer):
		sRepublicName = republicName(iPlayer)
		if sRepublicName: return sRepublicName

	sSpecificName = specificName(iPlayer)
	if sSpecificName: return sSpecificName

	sDefaultInsertName = getOrElse(dDefaultInsertNames, iPlayer)
	if sDefaultInsertName: return sDefaultInsertName

	return short(iPlayer)

def vassalName(iPlayer, iMaster):
	if iMaster == iRome and short(iPlayer) == "Carthage":
		return "TXT_KEY_CIV_ROMAN_NAME_CARTHAGE"

	if iPlayer == iNetherlands: return short(iPlayer)

	if gc.getPlayer(iPlayer).isReborn(): return short(iPlayer)

	sSpecificName = getOrElse(getOrElse(dForeignNames, iMaster, {}), iPlayer)
	if sSpecificName: return sSpecificName

	return None

def republicName(iPlayer):
	if iPlayer in [iMoors, iEngland]: return None

	if iPlayer == iInca and data.players[iPlayer].iResurrections > 0: return None

	if iPlayer == iNetherlands and isCommunist(iPlayer): return "TXT_KEY_CIV_NETHERLANDS_ARTICLE"
	
	if iPlayer == iBoers: return "TXT_KEY_CIV_BOER_SOUTH_AFRICA"
	
	if iPlayer == iTurks: return "TXT_KEY_CIV_TURKS_UZBEKISTAN"

	return short(iPlayer)

def peoplesName(iPlayer):
	return desc(iPlayer, key(iPlayer, "PEOPLES"))

def specificName(iPlayer):
	iGameTurn = gc.getGame().getGameTurn()
	pPlayer = gc.getPlayer(iPlayer)
	tPlayer = gc.getTeam(pPlayer.getTeam())
	iCivicGovernment, iCivicLegitimacy, iCivicSociety, iCivicEconomy, iCivicReligion, iCivicTerritory = getCivics(iPlayer)

	iNumCities = pPlayer.getNumCities()
	if iNumCities == 0: return short(iPlayer)

	bReborn = pPlayer.isReborn()
	iReligion = pPlayer.getStateReligion()
	capital = gc.getPlayer(iPlayer).getCapitalCity()
	tCapitalCoords = capitalCoords(iPlayer)
	bAnarchy = pPlayer.isAnarchy()
	bEmpire = isEmpire(iPlayer)
	bCityStates = isCityStates(iPlayer)
	bTheocracy = (iCivicReligion == iTheocracy)
	bResurrected = data.players[iPlayer].iResurrections > 0
	bCapitulated = isCapitulated(iPlayer)
	iAnarchyTurns = data.players[iPlayer].iAnarchyTurns
	iEra = pPlayer.getCurrentEra()
	iGameEra = gc.getGame().getCurrentEra()
	bWar = isAtWar(iPlayer)

	if iPlayer == iChina:
		if bEmpire:
			# if iEra >= iIndustrial or utils.getScenario() == i1700AD:
				# return "TXT_KEY_CIV_CHINA_QING"

			if iEra == iRenaissance and iGameTurn >= getTurnForYear(1400):
				return "TXT_KEY_CIV_CHINA_MING"

	elif iPlayer == iBabylonia:
		if isCapital(iPlayer, ["Ninua", "Kalhu"]):
			return "TXT_KEY_CIV_BABYLONIA_ASSYRIA"

		if gc.getPlayer(iPlayer).getCapitalCity().getName() == "Akkad":
			return "TXT_KEY_CIV_BABYLONIA_AKKADIA"

	if iPlayer == iHittite:
		if bResurrected:
			return "TXT_KEY_CIV_LYDIAN_SHORT_DESC"
		return "TXT_KEY_CIV_HITTITE_SHORT_DESC"
		
	elif iPlayer == iGreece:
		if iCivicGovernment == iMonarchy and bEmpire and iEra == iClassical:
			return "TXT_KEY_CIV_GREECE_MACEDONIA"

	elif iPlayer == iPolynesia:
		if isCapital(iPlayer, ["Kaua'i", "O'ahu", "Maui"]):
			return "TXT_KEY_CIV_POLYNESIA_HAWAII"

		if isCapital(iPlayer, ["Manu'a"]):
			return "TXT_KEY_CIV_POLYNESIA_SAMOA"

		if isCapital(iPlayer, ["Niue"]):
			return "TXT_KEY_CIV_POLYNESIA_NIUE"

		return "TXT_KEY_CIV_POLYNESIA_TONGA"

	elif iPlayer == iTamils:
		if iEra >= iRenaissance:
			return "TXT_KEY_CIV_TAMILS_MYSORE"

		if iEra >= iMedieval:
			return "TXT_KEY_CIV_TAMILS_VIJAYANAGARA"

	elif iPlayer == iEthiopia:
		if iEra < iMedieval:
			return gc.getPlayer(iPlayer).getCapitalCity().getName()

	elif iPlayer == iVietnam:
		if iEra >= iDigital:
			return "TXT_KEY_CIV_VIETNAM_SHORT_DESC"
		
		if iEra >= iIndustrial:
			return "TXT_KEY_CIV_VIETNAM_VIET_NAM"
			
		if iEra >= iMedieval:
			return "TXT_KEY_CIV_VIETNAM_DAI_VIET"
			
		return "TXT_KEY_CIV_VIETNAM_AU_LAC"

	elif iPlayer == iKorea:
		if capital.getY() > 46:
			if iEra == iClassical:
				return "TXT_KEY_CIV_KOREA_GOGURYEO"
					
			if iEra <= iMedieval:
				return "TXT_KEY_CIV_KOREA_GORYEO"
		else:
			if iEra == iClassical:
				return "TXT_KEY_CIV_KOREA_GOJOSEON"
					
			if iEra <= iMedieval:
				return "TXT_KEY_CIV_KOREA_JOSEON"

	elif iPlayer == iTeotihuacan:
		if not isCapital(iPlayer, ["Tollan"]):
				return capitalName(iPlayer)
				
		if iGameTurn >= getTurnForYear(800):
			return "TXT_KEY_CIV_TEOTIHUACAN_TULA"

	elif iPlayer == iByzantium:
		if iReligion == iIslam:
			return "TXT_KEY_CIV_BYZANTIUM_RUM"

		if not bEmpire:
			if isCapital(iPlayer, ["Dyrrachion"]):
				return "TXT_KEY_CIV_BYZANTIUM_EPIRUS"

			if isCapital(iPlayer, ["Athena"]):
				return "TXT_KEY_CIV_BYZANTIUM_MOREA"

			if not isCapital(iPlayer, ["Konstantinoupolis"]):
				return capitalName(iPlayer)

	#elif iPlayer == iVikings:	
	#	if bEmpire:
	#		if not isCapital(iPlayer, ["Stockholm", "Kalmar"]) or iEra > iRenaissance:
	#			return "TXT_KEY_CIV_VIKINGS_DENMARK_NORWAY"
	
	#	if isCapital(iPlayer, ["Oslo", "Nidaros"]):
	#		return "TXT_KEY_CIV_VIKINGS_NORWAY"
			
	#	if isCapital(iPlayer, ["Stockholm", "Kalmar"]):
	#		return "TXT_KEY_CIV_VIKINGS_SWEDEN"
			
	#	if isCapital(iPlayer, ["Roskilde"]):
	#		return "TXT_KEY_CIV_VIKINGS_DENMARK"
			
	#	return "TXT_KEY_CIV_VIKINGS_SCANDINAVIA"

	#elif iPlayer == iArabia:
	#	if bResurrected:
	#		return "TXT_KEY_CIV_ARABIA_SAUDI"

	elif iPlayer == iTurks:
		if utils.isPlotInArea(tCapitalCoords, tKhazariaTL, tKhazariaTL):
			return "TXT_KEY_CIV_TURKS_KHAZARIA"
	
		if utils.isPlotInArea(tCapitalCoords, tAnatoliaTL, tAnatoliaBR):
			return "TXT_KEY_CIV_TURKS_RUM"
			
		if iEra >= iRenaissance:
			if bEmpire:
				return "TXT_KEY_CIV_TURKS_UZBEKISTAN"
				
			return capitalName(iPlayer)
			
	elif iPlayer == iKhmer:
		if isCapital(iPlayer, ["Pagan"]):
			return "TXT_KEY_CIV_KHMER_BURMA"

		if isCapital(iPlayer, ["Dali"]):
			return "TXT_KEY_CIV_KHMER_NANZHAO"
			
	#elif iPlayer == iIndonesia:
	#	if iReligion == iIslam:
	#		return "TXT_KEY_CIV_INDONESIA_MATARAM"
			
	#	if iEra <= iRenaissance:
	#		if bEmpire:
	#			return "TXT_KEY_CIV_INDONESIA_MAJAPAHIT"
				
	#		return "TXT_KEY_CIV_INDONESIA_SRIVIJAYA"

	#elif iPlayer == iMoors:	
	#	if utils.isPlotInArea(tCapitalCoords, vic.tIberiaTL, vic.tIberiaBR):
	#		return capitalName(iPlayer)
			
	#	return "TXT_KEY_CIV_MOORS_MOROCCO"
	
	elif iPlayer == iSpain:
		if iReligion == iIslam:
			return "TXT_KEY_CIV_SPAIN_AL_ANDALUS"

		bSpain = not pMoors.isAlive() or not utils.isPlotInArea(capitalCoords(iMoors), vic.tIberiaTL, vic.tIberiaBR)

		if bSpain:
			if not pPortugal.isAlive() or not utils.isPlotInArea(capitalCoords(iPortugal), vic.tIberiaTL, vic.tIberiaBR):
				return "TXT_KEY_CIV_SPAIN_IBERIA"

		if isCapital(iPlayer, ["Barcelona", "Valencia"]):
			return "TXT_KEY_CIV_SPAIN_ARAGON"

		if not bSpain:
			return "TXT_KEY_CIV_SPAIN_CASTILE"

			
	#elif iPlayer == iFrance:
	#	if iEra == iMedieval and not pHolyRome.isAlive():
	#		return "TXT_KEY_CIV_FRANCE_FRANCIA"

	elif iPlayer == iEngland:
		if getColumn(iEngland) >= 12 and countPlayerAreaCities(iPlayer, tBritainTL, tBritainBR) >= 3:
			return "TXT_KEY_CIV_ENGLAND_GREAT_BRITAIN"

	elif iPlayer == iHolyRome:
		if isCapital(iPlayer, ["Buda"]):
			return "TXT_KEY_CIV_HOLY_ROME_HUNGARY"

		if not bEmpire:
			if iGameTurn < getTurnForYear(tBirth[iGermany]):
				return "TXT_KEY_CIV_HOLY_ROME_GERMANY"
			else:
				return "TXT_KEY_CIV_AUSTRIA_SHORT_DESC"

	elif iPlayer == iRussia:
		if not (bEmpire and iEra >= iRenaissance) and not isAreaControlled(iPlayer, tEuropeanRussiaTL, tEuropeanRussiaBR, 5, tEuropeanRussiaExceptions):
			if not bCityStates and isCapital(iPlayer, ["Moskva"]):
				return "TXT_KEY_CIV_RUSSIA_MUSCOVY"

			return capitalName(iPlayer)

	elif iPlayer == iPhilippines:
		if iEra >= iGlobal:
			return "TXT_KEY_CIV_PHILIPPINES_THE"
	
		if isCapital(iPlayer, ["Tondo"]):
			return "TXT_KEY_CIV_PHILIPPINES_TONDO"
			
		if isCapital(iPlayer, ["Butuan"]):
			return "TXT_KEY_CIV_PHILIPPINES_BUTUAN"

	elif iPlayer == iInca:
		if bResurrected:
			if isCapital(iPlayer, ["La Paz"]):
				return "TXT_KEY_CIV_INCA_BOLIVIA"

		else:
			if not bEmpire:
				return capitalName(iPlayer)

	#elif iPlayer == iItaly:
	#	if not bResurrected and not bEmpire and not bCityStates:
	#		if isCapital(iPlayer, ["Fiorenza"]):
	#			return "TXT_KEY_CIV_ITALY_TUSCANY"
				
	#		return capitalName(iPlayer)

	elif iPlayer == iThailand:
		if iEra <= iRenaissance:
			return "TXT_KEY_CIV_THAILAND_AYUTTHAYA"
			
	elif iPlayer == iSweden:
		if iEra >= iIndustrial and (isAreaControlled(iPlayer, (58, 59), (61, 63)) and not pVikings.isAlive()) or getMaster(iVikings) == iPlayer:
			return "TXT_KEY_CIV_SWEDEN_AND_NORWAY"

	elif iPlayer == iNetherlands:
		if isCapital(iPlayer, ["Brussels", "Antwerpen"]):
			return "TXT_KEY_CIV_NETHERLANDS_BELGIUM"

		if bCityStates:
			return short(iPlayer)

	elif iPlayer == iManchuria:
		return "TXT_KEY_CIV_CHINA_QING"

	elif iPlayer == iGermany:
		if getColumn(iGermany) <= 14 and pHolyRome.isAlive():
			return "TXT_KEY_CIV_GERMANY_PRUSSIA"

	elif iPlayer == iIsrael:
		if iReligion == iIslam:
			return "TXT_KEY_CIV_ISRAEL_PALESTINE"

def adjective(iPlayer, bIgnoreVassal = False):
	if isCapitulated(iPlayer):
		sForeignAdjective = getOrElse(getOrElse(dForeignAdjectives, getMaster(iPlayer), {}), iPlayer)
		if sForeignAdjective: return sForeignAdjective

		if not bIgnoreVassal: return adjective(getMaster(iPlayer))
	
	tPolity = getPolity(iPlayer)
	if tPolity:
		return getPolityTitleAdjective(tPolity)

	if isCommunist(iPlayer) or isFascist(iPlayer) or isRepublic(iPlayer):
		sRepublicAdjective = republicAdjective(iPlayer)
		if sRepublicAdjective: return sRepublicAdjective

	sSpecificAdjective = specificAdjective(iPlayer)
	if sSpecificAdjective: return sSpecificAdjective

	#sDefaultInsertAdjective = getOrElse(dDefaultInsertAdjectives, iPlayer)
	#if sDefaultInsertAdjective: return sDefaultInsertAdjective

	return gc.getPlayer(iPlayer).getCivilizationAdjective(0)

def republicAdjective(iPlayer):
	if iPlayer == iRome:
		if pByzantium.isAlive(): return None

	if iPlayer == iByzantium:
		if pRome.isAlive(): return None

	if iPlayer in [iMoors, iEngland]: return None

	if iPlayer == iInca and data.players[iPlayer].iResurrections > 0: return None

	return gc.getPlayer(iPlayer).getCivilizationAdjective(0)

def specificAdjective(iPlayer):
	iGameTurn = gc.getGame().getGameTurn()
	pPlayer = gc.getPlayer(iPlayer)
	tPlayer = gc.getTeam(pPlayer.getTeam())
	iCivicGovernment, iCivicLegitimacy, iCivicSociety, iCivicEconomy, iCivicReligion, iCivicTerritory = getCivics(iPlayer)

	iNumCities = pPlayer.getNumCities()
	if iNumCities == 0: return gc.getPlayer(iPlayer).getCivilizationAdjective(0)

	bReborn = pPlayer.isReborn()
	iReligion = pPlayer.getStateReligion()
	capital = gc.getPlayer(iPlayer).getCapitalCity()
	tCapitalCoords = capitalCoords(iPlayer)
	bAnarchy = pPlayer.isAnarchy()
	bEmpire = isEmpire(iPlayer)
	bCityStates = isCityStates(iPlayer)
	bTheocracy = (iCivicReligion == iTheocracy)
	bResurrected = data.players[iPlayer].iResurrections > 0
	bCapitulated = isCapitulated(iPlayer)
	iAnarchyTurns = data.players[iPlayer].iAnarchyTurns
	iEra = pPlayer.getCurrentEra()
	iGameEra = gc.getGame().getCurrentEra()
	bWar = isAtWar(iPlayer)

	bMonarchy = not isCommunist(iPlayer) and not isFascist(iPlayer) and not isRepublic(iPlayer)

	# if iPlayer == iEgypt:
		# if bMonarchy:
			# if bResurrected:
				# if tPlayer.isHasTech(iGunpowder):
					# return "TXT_KEY_CIV_EGYPT_MAMLUK"
		
				# if pArabia.isAlive():
					# return "TXT_KEY_CIV_EGYPT_FATIMID"
			
				# return "TXT_KEY_CIV_EGYPT_AYYUBID"

	if iPlayer == iHittite:
		if bResurrected:
			return "TXT_KEY_CIV_LYDIANS_ADJECTIVE"
		return "TXT_KEY_CIV_HITTITES_ADJECTIVE"

	elif iPlayer == iIndia:
		if bMonarchy and not bCityStates:
			if iEra >= iRenaissance:
				return "TXT_KEY_CIV_INDIA_MARATHA"

			if iEra >= iMedieval:
				if iReligion == iBuddhism:
					return "TXT_KEY_CIV_INDIA_PALA"
				
				if iReligion == iHinduism:
					return "TXT_KEY_CIV_INDIA_GUPTA"

			if bEmpire:
				return "TXT_KEY_CIV_INDIA_MAURYA"

	elif iPlayer == iChina:
		if bMonarchy:
			if iEra >= iMedieval:
				if tPlayer.isHasTech(iPaper) and tPlayer.isHasTech(iGunpowder):
					return "TXT_KEY_CIV_CHINA_SONG"

				if iGameTurn >= getTurnForYear(600):
					return "TXT_KEY_CIV_CHINA_TANG"
				
				return "TXT_KEY_CIV_CHINA_JIN"
			
			if iEra <= iClassical:
				if iGameTurn >= getTurnForYear(0):
					return "TXT_KEY_CIV_CHINA_HAN"

				return "TXT_KEY_CIV_CHINA_QIN"

			return "TXT_KEY_CIV_CHINA_ZHOU"

	elif iPlayer == iBabylonia:
		if bCityStates and not bEmpire:
			return "TXT_KEY_CIV_BABYLONIA_MESOPOTAMIAN"

		if isCapital(iPlayer, ["Ninua", "Kalhu"]):
			return "TXT_KEY_CIV_BABYLONIA_ASSYRIAN"

		
		if gc.getPlayer(iPlayer).getCapitalCity().getName() == "Akkad":
			return "TXT_KEY_CIV_BABYLONIA_AKKADIAN"

	elif iPlayer == iGreece:
		if iEra < iClassical:
			return "TXT_KEY_CIV_GREECE_MYCENEAN"
		if iCivicGovernment == iMonarchy and bEmpire and iEra == iClassical:
			return "TXT_KEY_CIV_GREECE_MACEDONIAN"
	
	
	elif iPlayer == iPhoenicia:
		if isCapital(iPlayer, ["Sur", "Sydwn"]):
			return "TXT_KEY_CIV_PHOENICIA_ADJECTIVE"
		else:
			if iEra <= iClassical:
				return "TXT_KEY_CIV_CARTHAGE_ADJECTIVE"
			elif iEra == iMedieval:
				return "TXT_KEY_CIV_AFRICA_ADJECTIVE"
			elif iEra >= iRenaissance:
				return "TXT_KEY_CIV_TUNIS_ADJECTIVE"

	elif iPlayer == iPersia:
		if bEmpire:
			if bReborn:
				if iEra <= iRenaissance:
					return "TXT_KEY_CIV_PERSIA_SAFAVID"

				if iEra == iIndustrial:
					return "TXT_KEY_CIV_PERSIA_QAJAR"

				return "TXT_KEY_CIV_PERSIA_PAHLAVI"

			if iEra <= iClassical:
				if bResurrected:
					return "TXT_KEY_CIV_PERSIA_PARTHIAN"

				return "TXT_KEY_CIV_PERSIA_ACHAEMENID"

			if getColumn(iPlayer) >= 6: 
				return "TXT_KEY_CIV_PERSIA_SASSANID"

		if iEra <= iClassical:
			return "TXT_KEY_CIV_PERSIA_MEDIAN"

	elif iPlayer == iPolynesia:
		if isCapital(iPlayer, ["Manu'a"]):
			return "TXT_KEY_CIV_POLYNESIA_TUI_MANUA"

		return "TXT_KEY_CIV_POLYNESIA_TUI_TONGA"

	elif iPlayer == iRome:
		if pByzantium.isAlive():
			return "TXT_KEY_CIV_ROME_WESTERN"

	elif iPlayer == iTamils:
		if iReligion == iIslam:
			if iEra in [iMedieval, iRenaissance]:
				return "TXT_KEY_CIV_TAMILS_BAHMANI"
	
		if iEra <= iClassical:
			if isCapital(iPlayer, ["Madurai", "Thiruvananthapuram"]):
				return "TXT_KEY_CIV_TAMILS_PANDYAN"

			if isCapital(iPlayer, ["Cochin", "Kozhikode"]):
				return "TXT_KEY_CIV_TAMILS_CHERA"

			return "TXT_KEY_CIV_TAMILS_CHOLA"

	elif iPlayer == iEthiopia:
		if iReligion == iIslam:
			return "TXT_KEY_CIV_ETHIOPIA_ADAL"
		elif iEra < iMedieval:
			return "TXT_KEY_CIV_ETHIOPIA_AKSUMITE"

	elif iPlayer == iTeotihuacan:
		if iGameTurn >= getTurnForYear(800):
			return "TXT_KEY_CIV_TEOTIHUACAN_TOLTEC"

	elif iPlayer == iByzantium:
		if pRome.getNumCities() > 0:
			return "TXT_KEY_CIV_BYZANTIUM_EASTERN"

		if bEmpire and controlsCity(iPlayer, Areas.getCapital(iRome)):
			return gc.getPlayer(iRome).getCivilizationAdjective(0)

	#elif iPlayer == iVikings:
	#	if bEmpire:
	#		return "TXT_KEY_CIV_VIKINGS_SWEDISH"
			
	#elif iPlayer == iArabia:
	#	if (bTheocracy or controlsHolyCity(iArabia, iIslam)) and iReligion == iIslam:
	#		if not bEmpire:
	#			return "TXT_KEY_CIV_ARABIA_RASHIDUN"
	#			
	#		if isCapital(iPlayer, ["Dimashq"]):
	#			return "TXT_KEY_CIV_ARABIA_UMMAYAD"
	#			
	#		return "TXT_KEY_CIV_ARABIA_ABBASID"
			
	elif iPlayer == iTurks:
		if bResurrected:
			return "TXT_KEY_CIV_TURKS_TIMURID"
	
		if utils.isPlotInArea(tCapitalCoords, tKhazariaTL, tKhazariaBR):
			return "TXT_KEY_CIV_TURKS_KHAZAR"
			
		if isAreaControlled(iTurks, Areas.tCoreArea[iPersia][0], Areas.tCoreArea[iPersia][1]):
			return "TXT_KEY_CIV_TURKS_SELJUK"
			
		if utils.isPlotInArea(tCapitalCoords, tAnatoliaTL, tAnatoliaBR):
			return "TXT_KEY_CIV_TURKS_SELJUK"
			
		if iEra >= iRenaissance:
			if bEmpire:
				return "TXT_KEY_CIV_TURKS_SHAYBANID"
		
			return "TXT_KEY_CIV_TURKS_UZBEK"
			
		easternmostCity = utils.getHighestEntry(utils.getCityList(iTurks), lambda city: city.getX())
		if easternmostCity and easternmostCity.getX() < iTurkicEastWestBorder:
			return "TXT_KEY_CIV_TURKS_WESTERN_TURKIC"
			
		westernmostCity = utils.getHighestEntry(utils.getCityList(iTurks), lambda city: -city.getX())
		if westernmostCity and westernmostCity.getX() >= iTurkicEastWestBorder:
			return "TXT_KEY_CIV_TURKS_EASTERN_TURKIC"

			
	elif iPlayer == iMoors:
		if bEmpire and iEra <= iRenaissance:
			return "TXT_KEY_CIV_MOORS_ALMOHAD"
			
	#elif iPlayer == iMoors:
	#	if bEmpire and iEra <= iRenaissance:
	#		return "TXT_KEY_CIV_MOORS_ALMOHAD"
			
	#	if not utils.isPlotInArea(tCapitalCoords, vic.tIberiaTL, vic.tIberiaBR):
	#		return "TXT_KEY_CIV_MOORS_MOROCCAN"

	elif iPlayer == iSpain:
		bSpain = not pMoors.isAlive() or not utils.isPlotInArea(capitalCoords(iMoors), vic.tIberiaTL, vic.tIberiaBR)

		if bSpain:
			if not pPortugal.isAlive() or getMaster(iPortugal) == iPlayer or not utils.isPlotInArea(capitalCoords(iPortugal), vic.tIberiaTL, vic.tIberiaBR):
				return "TXT_KEY_CIV_SPAIN_IBERIAN"

		if isCapital(iPlayer, ["Barcelona", "Valencia"]):
			return "TXT_KEY_CIV_SPAIN_ARAGONESE"

		if not bSpain:
			return "TXT_KEY_CIV_SPAIN_CASTILIAN"

	#elif iPlayer == iFrance:
	#	if iEra == iMedieval and not pHolyRome.isAlive():
	#		return "TXT_KEY_CIV_FRANCE_FRANKISH"

	elif iPlayer == iEngland:
		if getColumn(iEngland) >= 12 and countPlayerAreaCities(iPlayer, tBritainTL, tBritainBR) >= 3:
			return "TXT_KEY_CIV_ENGLAND_BRITISH"

	elif iPlayer == iHolyRome:
		if isCapital(iPlayer, ["Buda"]):
			return "TXT_KEY_CIV_HOLY_ROME_HUNGARIAN"

		if pGermany.isAlive() and iCivicLegitimacy == iConstitution:
			return "TXT_KEY_CIV_HOLY_ROME_AUSTRO_HUNGARIAN"

		iVassals = 0
		for iLoopPlayer in lCivGroups[0]:
			if getMaster(iLoopPlayer) == iPlayer:
				iVassals += 1

		if iVassals >= 2:
			return "TXT_KEY_CIV_HOLY_ROME_HABSBURG"

		if not bEmpire and iGameTurn < getTurnForYear(tBirth[iGermany]):
			return "TXT_KEY_CIV_HOLY_ROME_GERMAN"

	elif iPlayer == iMamluks:
		if tPlayer.isHasTech(iGunpowder):
			return "TXT_KEY_CIV_MAMLUKS_MAMLUK"

		if pArabia.isAlive():
			return "TXT_KEY_CIV_MAMLUKS_FATIMID"
	
		return "TXT_KEY_CIV_MAMLUKS_AYYUBID"

	elif iPlayer == iInca:
		if bResurrected:
			if isCapital(iPlayer, ["La Paz"]):
				return "TXT_KEY_CIV_INCA_BOLIVIAN"

	#elif iPlayer == iItaly:
	#	if bCityStates and bWar:
	#		if not bEmpire:
	#			return "TXT_KEY_CIV_ITALY_LOMBARD"

	elif iPlayer == iMongolia:
		if not bEmpire and iEra <= iRenaissance:
			if capital.getRegionID() == rChina:
				return "TXT_KEY_CIV_MONGOLIA_YUAN"

			if capital.getRegionID() == rPersia:
				return "TXT_KEY_CIV_MONGOLIA_HULAGU"
				
			if capital.getRegionID() == rCentralAsia:
				return "TXT_KEY_CIV_MONGOLIA_CHAGATAI"

		if bMonarchy:
			return "TXT_KEY_CIV_MONGOLIA_MONGOL"

	elif iPlayer == iOttomans:
		if iReligion == iIslam:
			return "TXT_KEY_CIV_OTTOMANS_OTTOMAN"

	elif iPlayer == iNetherlands:
		if isCapital(iPlayer, ["Brussels", "Antwerpen"]):
			return "TXT_KEY_CIV_NETHERLANDS_BELGIAN"

	elif iPlayer == iGermany:
		if getColumn(iGermany) <= 14 and pHolyRome.isAlive():
			return "TXT_KEY_CIV_GERMANY_PRUSSIAN"

### Title methods ###

def title(iPlayer):
	if isCapitulated(iPlayer):
		sVassalTitle = vassalTitle(iPlayer, getMaster(iPlayer))
		if sVassalTitle: return sVassalTitle

	polityTitle = getPolityTitle(iPlayer)
	if polityTitle:
		return polityTitle

	if isCommunist(iPlayer):
		sCommunistTitle = communistTitle(iPlayer)
		if sCommunistTitle: return sCommunistTitle

	if isFascist(iPlayer):
		sFascistTitle = fascistTitle(iPlayer)
		if sFascistTitle: return sFascistTitle

	if isRepublic(iPlayer):
		sRepublicTitle = republicTitle(iPlayer)
		if sRepublicTitle: return sRepublicTitle

	sSpecificTitle = specificTitle(iPlayer)
	if sSpecificTitle: return sSpecificTitle

	return defaultTitle(iPlayer)

def vassalTitle(iPlayer, iMaster):
	if isCommunist(iMaster):
		sCommunistTitle = getOrElse(getOrElse(dCommunistVassalTitles, iMaster, {}), iPlayer)
		if sCommunistTitle: return sCommunistTitle

		sCommunistTitle = getOrElse(dCommunistVassalTitlesGeneric, iMaster)
		if sCommunistTitle: return sCommunistTitle

	if isFascist(iMaster):
		sFascistTitle = getOrElse(getOrElse(dFascistVassalTitles, iMaster, {}), iPlayer)
		if sFascistTitle: return sFascistTitle

		sFascistTitle = getOrElse(dFascistVassalTitlesGeneric, iMaster)
		if sFascistTitle: return sFascistTitle

	if short(iMaster) == "Austria" and iPlayer == iPoland:
		return "TXT_KEY_CIV_AUSTRIAN_POLAND"

	if iMaster == iEngland and iPlayer == iMughals:
		if not pIndia.isAlive():
			return vassalTitle(iIndia, iEngland)

	if iMaster == iSpain and short(iPlayer) == "Colombia":
		return "TXT_KEY_CIV_SPANISH_COLOMBIA"

	if iMaster not in lRebirths or not gc.getPlayer(iMaster).isReborn():
		sSpecificTitle = getOrElse(getOrElse(dSpecificVassalTitles, iMaster, {}), iPlayer)
		if sSpecificTitle: return sSpecificTitle

		sMasterTitle = getOrElse(dMasterTitles, iMaster)
		if sMasterTitle: return sMasterTitle

	if iPlayer in lColonies:
		return "TXT_KEY_COLONY_OF"

	return "TXT_KEY_PROTECTORATE_OF"

#this should be the generic fallback title method
def monarchyTitle(iPlayer):
	iGameTurn = gc.getGame().getGameTurn()
	pPlayer = gc.getPlayer(iPlayer)
	tPlayer = gc.getTeam(pPlayer.getTeam())
	iCivicGovernment, iCivicLegitimacy, iCivicSociety, iCivicEconomy, iCivicReligion, iCivicTerritory = getCivics(iPlayer)
	iNumCities = pPlayer.getNumCities()
	bReborn = pPlayer.isReborn()
	iReligion = pPlayer.getStateReligion()
	capital = gc.getPlayer(iPlayer).getCapitalCity()
	tCapitalCoords = capitalCoords(iPlayer)
	bAnarchy = pPlayer.isAnarchy()
	bEmpire = isEmpire(iPlayer)
	bCityStates = isCityStates(iPlayer)
	bTheocracy = (iCivicReligion == iTheocracy)
	bResurrected = data.players[iPlayer].iResurrections > 0
	bCapitulated = isCapitulated(iPlayer)
	iAnarchyTurns = data.players[iPlayer].iAnarchyTurns
	iEra = pPlayer.getCurrentEra()
	iGameEra = gc.getGame().getCurrentEra()
	bWar = isAtWar(iPlayer)
	bCityState = (iNumCities == 1)
	
	case = "ADJECTIVE"
	if bEmpire:
		type = "EMPIRE"
	else:
		type = "KINGDOM"

	if iReligion == iIslam:
		if controlsHolyCity(iPlayer, iIslam):
			type = "CALIPHATE"
		else:
			if bCityState:
				type = "EMIRATE"
			elif bEmpire:
				type = "CALIPHATE"
			else:
				type = "SULTANATE"
	elif iReligion == iOrthodoxy:
		if bCityState:
			case = "OF"
			type = "DESPOTATE"
		elif bEmpire:
			case = "ADJECTIVE"
			type = "EMPIRE"
		else:
			case = "OF"
			type = "KINGDOM"
	elif iReligion in [iCatholicism, iProtestantism]:
		if bEmpire and isColonialEmpire(iPlayer):
			case = "ADJECTIVE"
			type = "COLONIAL_EMPIRE"
		if bEmpire:
			case = "ADJECTIVE"
			type = "EMPIRE"
		else:
			case = "OF"
			type = "KINGDOM"
	elif iReligion not in [iIslam, iOrthodoxy, iCatholicism, iProtestantism, None]:
		if bEmpire:
			type = "GREATER_EMPIRE"
			case = "OF"
	
	if iPlayer in lMonarchyOf:
		case = "OF"
	elif iPlayer in lMonarchyAdj:
		case = "ADJECTIVE"
	
	tPolity = getPolity(iPlayer)
	if tPolity and not getPolityTitleAdjective(tPolity):
		case = "OF"
		
	return "TXT_KEY_" + type + "_" + case

def grandDuchyTitle(iPlayer):
	iGameTurn = gc.getGame().getGameTurn()
	pPlayer = gc.getPlayer(iPlayer)
	tPlayer = gc.getTeam(pPlayer.getTeam())
	iCivicGovernment, iCivicLegitimacy, iCivicSociety, iCivicEconomy, iCivicReligion, iCivicTerritory = getCivics(iPlayer)
	iNumCities = pPlayer.getNumCities()
	bReborn = pPlayer.isReborn()
	iReligion = pPlayer.getStateReligion()
	capital = gc.getPlayer(iPlayer).getCapitalCity()
	tCapitalCoords = capitalCoords(iPlayer)
	bAnarchy = pPlayer.isAnarchy()
	bEmpire = isEmpire(iPlayer)
	bCityStates = isCityStates(iPlayer)
	bTheocracy = (iCivicReligion == iTheocracy)
	bResurrected = data.players[iPlayer].iResurrections > 0
	bCapitulated = isCapitulated(iPlayer)
	iAnarchyTurns = data.players[iPlayer].iAnarchyTurns
	iEra = pPlayer.getCurrentEra()
	iGameEra = gc.getGame().getCurrentEra()
	bWar = isAtWar(iPlayer)
	bCityState = (iNumCities == 1)
	
	case = "OF"
	type = "GRAND_DUCHY"
	
	if bCityState:
		case = "OF"
		type = "DUCHY"
	
	if bEmpire:
		case = "ADJECTIVE"
		type = "COMMONWEALTH"

	return "TXT_KEY_" + type + "_" + case
	
def cityStatesTitle(iPlayer):
	
	iGameTurn = gc.getGame().getGameTurn()
	pPlayer = gc.getPlayer(iPlayer)
	tPlayer = gc.getTeam(pPlayer.getTeam())
	iCivicGovernment, iCivicLegitimacy, iCivicSociety, iCivicEconomy, iCivicReligion, iCivicTerritory = getCivics(iPlayer)
	iNumCities = pPlayer.getNumCities()
	bReborn = pPlayer.isReborn()
	iReligion = pPlayer.getStateReligion()
	capital = gc.getPlayer(iPlayer).getCapitalCity()
	tCapitalCoords = capitalCoords(iPlayer)
	bAnarchy = pPlayer.isAnarchy()
	bEmpire = isEmpire(iPlayer)
	bCityStates = isCityStates(iPlayer)
	bTheocracy = (iCivicReligion == iTheocracy)
	bResurrected = data.players[iPlayer].iResurrections > 0
	bCapitulated = isCapitulated(iPlayer)
	iAnarchyTurns = data.players[iPlayer].iAnarchyTurns
	iEra = pPlayer.getCurrentEra()
	iGameEra = gc.getGame().getCurrentEra()
	bWar = isAtWar(iPlayer)
	bCityState = (iNumCities == 1)
	
	title = "TXT_KEY_CITY_STATES_ADJECTIVE"
	if bWar:
		title = "TXT_KEY_LEAGUE_ADJECTIVE"
	
	if iEra >= iMedieval or bCityState:
		title = "TXT_KEY_REPUBLIC_OF"
	
	if iReligion == iCatholicism:
		title = "TXT_KEY_MOST_SERENE_REPUBLIC_OF"
	
	return title

def communistTitle(iPlayer):
	if iPlayer in lSocialistRepublicOf: return "TXT_KEY_SOCIALIST_REPUBLIC_OF"
	if iPlayer in lSocialistRepublicAdj: return "TXT_KEY_SOCIALIST_REPUBLIC_ADJECTIVE"
	if iPlayer in lPeoplesRepublicOf: return "TXT_KEY_PEOPLES_REPUBLIC_OF"
	if iPlayer in lPeoplesRepublicAdj: return "TXT_KEY_PEOPLES_REPUBLIC_ADJECTIVE"

	return key(iPlayer, "COMMUNIST")

def fascistTitle(iPlayer):
	return key(iPlayer, "FASCIST")

def republicTitle(iPlayer):
	if iPlayer == iHolyRome:
		return "TXT_KEY_REPUBLIC_ADJECTIVE"

	if iPlayer == iPoland:
		if gc.getPlayer(iPlayer).getCurrentEra() <= iIndustrial:
			return key(iPlayer, "COMMONWEALTH")

	if iPlayer == iEngland:
		iEra = gc.getPlayer(iPlayer).getCurrentEra()
		if isEmpire(iEngland) and iEra == iIndustrial:
			return "TXT_KEY_EMPIRE_ADJECTIVE"

		if iEra >= iGlobal:
			return "TXT_KEY_CIV_ENGLAND_UNITED_REPUBLIC"

	if iPlayer == iAmerica:
		_, _, iCivicSociety, _, _, _ = getCivics(iPlayer)
		if iCivicSociety in [iManorialism, iSlavery]:
			return key(iPlayer, "CSA")

	if gc.getPlayer(iPlayer).getStateReligion() == iIslam:
		if iPlayer in lIslamicRepublicOf: return "TXT_KEY_ISLAMIC_REPUBLIC_OF"

		if iPlayer == iOttomans: return key(iPlayer, "ISLAMIC_REPUBLIC")

	if iPlayer in lRepublicOf: return "TXT_KEY_REPUBLIC_OF"
	if iPlayer in lRepublicAdj: return "TXT_KEY_REPUBLIC_ADJECTIVE"

	return key(iPlayer, "REPUBLIC")

def defaultTitle(iPlayer):
	iGameTurn = gc.getGame().getGameTurn()
	pPlayer = gc.getPlayer(iPlayer)
	tPlayer = gc.getTeam(pPlayer.getTeam())
	iCivicGovernment, iCivicLegitimacy, iCivicSociety, iCivicEconomy, iCivicReligion, iCivicTerritory = getCivics(iPlayer)
	
	iNumCities = pPlayer.getNumCities()
	if iNumCities == 0:
		return desc(iPlayer, key(iPlayer, "DEFAULT"))
	
	bReborn = pPlayer.isReborn()
	iReligion = pPlayer.getStateReligion()
	capital = gc.getPlayer(iPlayer).getCapitalCity()
	tCapitalCoords = capitalCoords(iPlayer)
	bAnarchy = pPlayer.isAnarchy()
	bEmpire = isEmpire(iPlayer)
	bCityStates = isCityStates(iPlayer)
	bTheocracy = (iCivicReligion == iTheocracy)
	bResurrected = data.players[iPlayer].iResurrections > 0
	bCapitulated = isCapitulated(iPlayer)
	iAnarchyTurns = data.players[iPlayer].iAnarchyTurns
	iEra = pPlayer.getCurrentEra()
	iGameEra = gc.getGame().getCurrentEra()
	bWar = isAtWar(iPlayer)
	bMonarchy = not (isCommunist(iPlayer) or isFascist(iPlayer) or isRepublic(iPlayer) or isCityStates(iPlayer))
	bGrandDuchy = isGrandDuchy(iPlayer)
	
	if bCityStates:
		title = cityStatesTitle(iPlayer)
	elif bGrandDuchy:
		title = grandDuchyTitle(iPlayer)
	else:
		title = monarchyTitle(iPlayer)
	
	if iEra == iAncient:
		if not bMonarchy:
			title = "TXT_KEY_CHIEFDOM_ADJECTIVE"
	
	return title
	
def specificTitle(iPlayer, lPreviousOwners=[]):
	iGameTurn = gc.getGame().getGameTurn()
	pPlayer = gc.getPlayer(iPlayer)
	tPlayer = gc.getTeam(pPlayer.getTeam())
	iCivicGovernment, iCivicLegitimacy, iCivicSociety, iCivicEconomy, iCivicReligion, iCivicTerritory = getCivics(iPlayer)
	
	iNumCities = pPlayer.getNumCities()
	if iNumCities == 0:
		return desc(iPlayer, key(iPlayer, "DEFAULT"))
	
	bReborn = pPlayer.isReborn()
	iReligion = pPlayer.getStateReligion()
	capital = gc.getPlayer(iPlayer).getCapitalCity()
	tCapitalCoords = capitalCoords(iPlayer)
	bAnarchy = pPlayer.isAnarchy()
	bEmpire = isEmpire(iPlayer)
	bCityStates = isCityStates(iPlayer)
	bTheocracy = (iCivicReligion == iTheocracy)
	bResurrected = data.players[iPlayer].iResurrections > 0
	bCapitulated = isCapitulated(iPlayer)
	iAnarchyTurns = data.players[iPlayer].iAnarchyTurns
	iEra = pPlayer.getCurrentEra()
	iGameEra = gc.getGame().getCurrentEra()
	bWar = isAtWar(iPlayer)
	bMonarchy = not (isCommunist(iPlayer) or isFascist(iPlayer) or isRepublic(iPlayer))


	if iPlayer == iEgypt:
		# if bResurrected:
			# if data.players[iPlayer].iResurrections < 2:
				# if iReligion == iIslam:
					# if bTheocracy: return "TXT_KEY_CALIPHATE_ADJECTIVE"
					# return "TXT_KEY_SULTANATE_ADJECTIVE"
				# return "TXT_KEY_KINGDOM_ADJECTIVE"

		if iGreece in lPreviousOwners:
			return "TXT_KEY_CIV_EGYPT_PTOLEMAIC"

		if bCityStates:
			return "TXT_KEY_CITY_STATES_ADJECTIVE"

		if iEra == iAncient:
			if iAnarchyTurns < 1: return "TXT_KEY_CIV_EGYPT_OLD_KINGDOM"
			return "TXT_KEY_CIV_EGYPT_MIDDLE_KINGDOM"

		if iEra == iClassical:
			return "TXT_KEY_CIV_EGYPT_NEW_KINGDOM"

	elif iPlayer == iIndia:
		if iReligion == iIslam:
			return "TXT_KEY_SULTANATE_OF"

		if bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"

		if iEra >= iRenaissance:
			return "TXT_KEY_CONFEDERACY_ADJECTIVE"

		if bCityStates:
			return "TXT_KEY_CIV_INDIA_MAHAJANAPADAS"

		#not bEmpire and iEra <= iMedieval and not bCityStates
		if gc.getPlayer(iPlayer).getNumCities() == 1:
			return "TXT_KEY_CIV_INDIA_MAGADHA"

		if iEra == iClassical:
			if bResurrected:
				return "TXT_KEY_CIV_INDIA_SHUNGA"
			else:
				return "TXT_KEY_CIV_INDIA_NANDA"

	elif iPlayer == iChina:
		if bEmpire:
			if iEra >= iIndustrial or utils.getScenario() == i1700AD:
				return "TXT_KEY_EMPIRE_OF"

			if iEra == iRenaissance and iGameTurn >= getTurnForYear(1400):
				return "TXT_KEY_EMPIRE_OF"

			return "TXT_KEY_EMPIRE_ADJECTIVE"

	elif iPlayer == iBabylonia:
		if bCityStates and not bEmpire:
			return "TXT_KEY_CITY_STATES_ADJECTIVE"

		if bEmpire and iEra > iAncient:
			return "TXT_KEY_CIV_BABYLONIA_NEO_EMPIRE"

	elif iPlayer == iGreece:
		if bCityStates:	
			if bWar:
				return "TXT_KEY_CIV_GREECE_LEAGUE"
			if bEmpire:
				return "TXT_KEY_COLONIAL_EMPIRE_ADJECTIVE"
			return "TXT_KEY_CITY_STATES_ADJECTIVE"

	elif iPlayer == iPersia:
		if bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"

			
		if bMonarchy:
			return "TXT_KEY_CIV_PERSIA_SHAHDOM"

	elif iPlayer == iPhoenicia:
		if bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"

		if bCityStates:
			return "TXT_KEY_CITY_STATES_ADJECTIVE"

	elif iPlayer == iPolynesia:
		if isCapital(iPlayer, ["Kaua'i", "O'ahu", "Maui"]):
			return "TXT_KEY_KINGDOM_OF"

		if bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"

	elif iPlayer == iRome:
		if bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"

		if bCityStates:
			return "TXT_KEY_REPUBLIC_ADJECTIVE"

	#elif iPlayer == iJapan:
	#	if iEra < iIndustrial:
	#		plot = gc.getMap().plot(113, 45)
	#		if plot.isCity() and plot.getPlotCity().getOwner() == iPlayer:
	#			return "TXT_KEY_CIV_JAPAN_DEFAULT" #shogunate
	#	return "TXT_KEY_CIV_JAPAN_CLAN"

	elif iPlayer == iTamils:
		if iReligion == iIslam:
			return "TXT_KEY_SULTANATE_ADJECTIVE"
	
		if iEra >= iMedieval:
			return "TXT_KEY_KINGDOM_OF"

		if bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"

	elif iPlayer == iEthiopia:
		if bCityStates:
			return "TXT_KEY_CITY_STATES_ADJECTIVE"

		if iReligion == iIslam:
			return "TXT_KEY_SULTANATE_ADJECTIVE"

		if bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"

	elif iPlayer == iVietnam:
		pass

	elif iPlayer == iTeotihuacan:
		if bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"
			
		if bCityStates:
			return "TXT_KEY_CIV_TEOTIHUACAN_ALTEPETL"

	elif iPlayer == iKorea:
		if iEra >= iIndustrial:
			if bEmpire:
				return "TXT_KEY_EMPIRE_ADJECTIVE"

		if iEra == iClassical:
			if bEmpire:
				return "TXT_KEY_EMPIRE_OF"

		if bCityStates:
			return "TXT_KEY_CIV_KOREA_SAMHAN"

	elif iPlayer == iMaya:
		if bReborn:
			if bEmpire:
				return "TXT_KEY_CIV_COLOMBIA_EMPIRE"

	elif iPlayer == iByzantium:
		if iReligion == iIslam:
			return "TXT_KEY_SULTANATE_OF"

		if not bEmpire:
			if capital.getRegionID() == rAnatolia or tCapitalCoords == Areas.getCapital(iPlayer):
				return "TXT_KEY_EMPIRE_OF"

			return "TXT_KEY_CIV_BYZANTIUM_DESPOTATE"
			
	#elif iPlayer == iVikings:
	#	if bCityStates:
	#		return "TXT_KEY_CIV_VIKINGS_ALTHINGS"
				
	#	if iReligion < 0 and iEra < iRenaissance:
	#		return "TXT_KEY_CIV_VIKINGS_NORSE_KINGDOMS"
			
	#	if bEmpire:
	#		if iEra <= iMedieval:
	#			return "TXT_KEY_CIV_VIKINGS_KALMAR_UNION"

	#		if iEra == iRenaissance or isCapital(iPlayer, ["Stockholm"]):
	#			return "TXT_KEY_EMPIRE_ADJECTIVE"

	elif iPlayer == iTurks:
		if bCityStates or iCivicGovernment == iElective:
			return "TXT_KEY_CIV_TURKS_KURULTAI"
			
		if iReligion >= 0:
			if bEmpire:
				if isAreaControlled(iTurks, Areas.tCoreArea[iPersia][0], Areas.tCoreArea[iPersia][1]) and not bResurrected:
					return "TXT_KEY_CIV_TURKS_GREAT_EMPIRE"
			
				return "TXT_KEY_EMPIRE_ADJECTIVE"
				
			if not isAreaControlled(iTurks, Areas.tCoreArea[iPersia][0], Areas.tCoreArea[iPersia][1]):
				return "TXT_KEY_CIV_TURKS_KHANATE_OF"
				
			if iReligion == iIslam:
				return "TXT_KEY_SULTANATE_OF"
				
			return "TXT_KEY_KINGDOM_OF"
			
		if bEmpire:
			return "TXT_KEY_CIV_TURKS_KHAGANATE"
			
	#elif iPlayer == iArabia:
	#	if bResurrected:
	#		return "TXT_KEY_KINGDOM_OF"
	#		
	#	if iReligion == iIslam and (bTheocracy or controlsHolyCity(iArabia, iIslam)):
	#		return "TXT_KEY_CALIPHATE_ADJECTIVE"
			
	#elif iPlayer == iTibet:
	#	if bEmpire:
	#		return "TXT_KEY_EMPIRE_ADJECTIVE"
			
	elif iPlayer == iKhmer:
		if iEra <= iRenaissance and isCapital(iPlayer, ["Angkor"]):
			return "TXT_KEY_EMPIRE_ADJECTIVE"
			
		if isCapital(iPlayer, ["Hanoi"]):
			return "TXT_KEY_CIV_KHMER_DAI_VIET"
			
	#elif iPlayer == iIndonesia:
	#	if iReligion == iIslam:
	#		return "TXT_KEY_SULTANATE_OF"
			
	#elif iPlayer == iMoors:
	#	if bCityStates:
	#		return "TXT_KEY_CIV_MOORS_TAIFAS"
			
	#	if iReligion == iIslam and utils.isPlotInArea(tCapitalCoords, vic.tIberiaTL, vic.tIberiaBR):
	#		if bEmpire:
	#			return "TXT_KEY_CALIPHATE_OF"
				
	#		return "TXT_KEY_CIV_MOORS_EMIRATE_OF"
			
	#	if bEmpire and iEra <= iRenaissance:
	#		if iReligion == iIslam and bTheocracy:
	#			return "TXT_KEY_CALIPHATE_ADJECTIVE"
				
	#		return "TXT_KEY_EMPIRE_ADJECTIVE"
			
	elif iPlayer == iSpain:
		if iReligion == iIslam:
			return "TXT_KEY_SULTANATE_OF"

		if bEmpire and iEra > iMedieval:
			return "TXT_KEY_EMPIRE_ADJECTIVE"

		if iEra == iMedieval and isCapital(iPlayer, ["Barcelona", "Valencia"]):
			return "TXT_KEY_CIV_SPAIN_CROWN_OF"

	#elif iPlayer == iFrance:
	#	if not tCapitalCoords in Areas.getNormalArea(iPlayer):
	#		return "TXT_KEY_CIV_FRANCE_EXILE"
			
	#	if iEra >= iIndustrial and bEmpire:
	#		return "TXT_KEY_EMPIRE_ADJECTIVE"
			
	#	if iCivicLegitimacy == iIdeology:
	#		return "TXT_KEY_EMPIRE_ADJECTIVE"
			
	#	if not pHolyRome.isAlive() and iEra == iMedieval and iNumCities > 2:
	#		return "TXT_KEY_EMPIRE_ADJECTIVE"

	elif iPlayer == iEngland:
		if not utils.isPlotInCore(iPlayer, tCapitalCoords):
			return "TXT_KEY_CIV_ENGLAND_EXILE"

		if iEra == iMedieval and getMaster(iFrance) == iEngland:
			return "TXT_KEY_CIV_ENGLAND_ANGEVIN_EMPIRE"

		if getColumn(iPlayer) >= 12:
			if bEmpire:
				return "TXT_KEY_EMPIRE_ADJECTIVE"

			if countPlayerAreaCities(iPlayer, tBritainTL, tBritainBR) >= 3:
				return "TXT_KEY_CIV_ENGLAND_UNITED_KINGDOM_OF"

	elif iPlayer == iHolyRome:
		if bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"

		if isCapital(iPlayer, ["Buda"]):
			return "TXT_KEY_KINGDOM_OF"

		if pGermany.isAlive():
			return "TXT_KEY_CIV_HOLY_ROME_ARCHDUCHY_OF"

	elif iPlayer == iRussia:
		if bEmpire and iEra >= iRenaissance:
			return "TXT_KEY_EMPIRE_ADJECTIVE"

		if bCityStates and iEra <= iMedieval:
			if isCapital(iPlayer, ["Kiev"]):
				return "TXT_KEY_CIV_RUSSIA_KIEVAN_RUS"

			return "TXT_KEY_CIV_RUSSIA_RUS"

		if isAreaControlled(iPlayer, tEuropeanRussiaTL, tEuropeanRussiaBR, 5, tEuropeanRussiaExceptions):
			return "TXT_KEY_CIV_RUSSIA_TSARDOM_OF"
			
	elif iPlayer == iPhilippines:
		if iReligion == iHinduism:
			return "TXT_KEY_CIV_PHILIPPINES_RAJAHNATE"

	elif iPlayer == iMamluks:
		if iReligion == iIslam:
			if bTheocracy: return "TXT_KEY_CALIPHATE_ADJECTIVE"
			return "TXT_KEY_SULTANATE_ADJECTIVE"
		return "TXT_KEY_KINGDOM_ADJECTIVE"

	elif iPlayer == iNetherlands:
		if bCityStates:
			return "TXT_KEY_CIV_NETHERLANDS_REPUBLIC"

		if not utils.isPlotInCore(iPlayer, tCapitalCoords):
			return "TXT_KEY_CIV_NETHERLANDS_EXILE"

		if bEmpire:
			if iEra >= iIndustrial:
				return "TXT_KEY_EMPIRE_ADJECTIVE"

			return "TXT_KEY_CIV_NETHERLANDS_UNITED_KINGDOM_OF"

	# Nothing for Mali

	elif iPlayer == iPoland:
		if iEra >= iRenaissance and bEmpire:
			return "TXT_KEY_CIV_POLAND_COMMONWEALTH"

		if isCapital(iPlayer, ["Kowno", "Medvegalis", "Wilno", "Ryga"]):
			return "TXT_KEY_CIV_POLAND_GRAND_DUCHY_OF"

	elif iPlayer == iPortugal:
		if utils.isPlotInCore(iBrazil, tCapitalCoords) and not pBrazil.isAlive():
			return "TXT_KEY_CIV_PORTUGAL_BRAZIL"

		if not utils.isPlotInArea(tCapitalCoords, vic.tIberiaTL, vic.tIberiaBR):
			return "TXT_KEY_CIV_PORTUGAL_EXILE"

		if bEmpire and iEra >= iRenaissance:
			return "TXT_KEY_EMPIRE_ADJECTIVE"

	elif iPlayer == iInca:
		if not bResurrected:
			if bEmpire:
				return "TXT_KEY_CIV_INCA_FOUR_REGIONS"

	#elif iPlayer == iItaly:
		#if bCityStates:
		#	if bWar:
		#		return "TXT_KEY_CIV_ITALY_LEAGUE"
				
		#	return "TXT_KEY_CIV_ITALY_MARITIME_REPUBLICS"
		#	
		#if not bResurrected:
		#	if iReligion == iCatholicism:
		#		if bTheocracy:
		#			return "TXT_KEY_CIV_ITALY_PAPAL_STATES"
				
		#		if isCapital(iItaly, ["Roma"]):
		#			return "TXT_KEY_CIV_ITALY_PAPAL_STATES"
					
		#	if not bEmpire:
		#		return "TXT_KEY_CIV_ITALY_DUCHY_OF"
				
		#if bEmpire:
		#	return "TXT_KEY_EMPIRE_ADJECTIVE"

	elif iPlayer == iMongolia:
		if capital.getRegionID() == rPersia:
			return "TXT_KEY_CIV_MONGOLIA_ILKHANATE"
	
		if bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"

		if iEra <= iRenaissance:
			if iNumCities <= 3:
				return "TXT_KEY_CIV_MONGOLIA_KHAMAG"

			return "TXT_KEY_CIV_MONGOLIA_KHANATE"

	elif iPlayer == iAztecs:
		if bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"

		if bCityStates:
			return "TXT_KEY_CIV_AZTEC_ALTEPETL"

	elif iPlayer == iMughals:
		if bResurrected:
			if bEmpire:
				return "TXT_KEY_EMPIRE_OF"

			return "TXT_KEY_SULTANATE_OF"

		if iEra == iMedieval and not bEmpire:
			return "TXT_KEY_SULTANATE_OF"

	elif iPlayer == iOttomans:
		if iReligion == iIslam:
			if bTheocracy and gc.getGame().getHolyCity(iIslam) and gc.getGame().getHolyCity(iIslam).getOwner() == iOttomans:
				return "TXT_KEY_CALIPHATE_ADJECTIVE"

			if bEmpire:
				return "TXT_KEY_EMPIRE_ADJECTIVE"

			return "TXT_KEY_SULTANATE_ADJECTIVE"

		if bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"

	elif iPlayer == iThailand:
		if iEra >= iIndustrial and bEmpire:
			return "TXT_KEY_EMPIRE_OF"

	elif iPlayer == iGermany:
		if iEra >= iIndustrial and bEmpire:
			if getMaster(iHolyRome) == iGermany:
				return "TXT_KEY_CIV_GERMANY_GREATER_EMPIRE"

			return "TXT_KEY_EMPIRE_ADJECTIVE"

	elif iPlayer == iAmerica:
		if iCivicSociety in [iSlavery, iManorialism]:
			return "TXT_KEY_CIV_AMERICA_CSA"

	elif iPlayer == iArgentina:
		if bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"

		if tCapitalCoords != Areas.getCapital(iPlayer):
			return "TXT_KEY_CIV_ARGENTINA_CONFEDERATION"

	elif iPlayer == iBrazil:
		if bEmpire:
			return "TXT_KEY_EMPIRE_OF"
			
	elif iPlayer == iBoers:
		if iEra >= iGlobal:
			return "TXT_KEY_CIV_BOER_UNION"
		
		if bEmpire:
			return "TXT_KEY_CIV_BOER_UNION"
		
		if isCapital(iPlayer, ["Pretoria", "Johannesburg"]):
			return "TXT_KEY_CIV_BOER_TRANSVAAL"
		if isCapital(iPlayer, ["Bloemfontein"]):
			return "TXT_KEY_CIV_BOER_ORANGE_FREE_STATE"
		if isCapital(iPlayer, ["Pietermaritzburg", "Durban"]):
			return "TXT_KEY_CIV_BOER_NATALIA"
			
	return None

### Leader methods ###

def startingLeader(iPlayer):
	if iPlayer in dStartingLeaders[utils.getScenario()]: return dStartingLeaders[utils.getScenario()][iPlayer]
	
	if iPlayer in dStartingLeaders[i3000BC]: return dStartingLeaders[i3000BC][iPlayer]
	
	return None

def leader(iPlayer):
	
	if iPlayer >= iNumPlayers: return None

	if not gc.getPlayer(iPlayer).isAlive(): return None

	#if gc.getPlayer(iPlayer).isHuman(): return None

	pPlayer = gc.getPlayer(iPlayer)
	tPlayer = gc.getTeam(pPlayer.getTeam())
	bReborn = pPlayer.isReborn()
	iReligion = pPlayer.getStateReligion()
	capital = gc.getPlayer(iPlayer).getCapitalCity()
	tCapitalCoords = (capital.getX(), capital.getY())
	iCivicGovernment, iCivicLegitimacy, iCivicSociety, iCivicEconomy, iCivicReligion, iCivicTerritory = getCivics(iPlayer)
	iGameTurn = gc.getGame().getGameTurn()
	bEmpire = isEmpire(iPlayer)
	bCityStates = isCityStates(iPlayer)
	bTheocracy = (iCivicReligion == iTheocracy)
	bResurrected = data.players[iPlayer].iResurrections > 0
	bMonarchy = not (isCommunist(iPlayer) or isFascist(iPlayer) or isRepublic(iPlayer))
	iAnarchyTurns = data.players[iPlayer].iAnarchyTurns
	iEra = pPlayer.getCurrentEra()
	iGameEra = gc.getGame().getCurrentEra()

	if iPlayer == iEgypt:
		if getColumn(iPlayer) >= 4: return iCleopatra

	elif iPlayer == iIndia:
		if not bMonarchy and iEra >= iGlobal: return iGandhi

		if iEra >= iRenaissance: return iShahuji

		if iGameTurn >= getTurnForYear(605): return iDharmapala

		if getColumn(iPlayer) >= 5: return iChandragupta

	elif iPlayer == iChina:
		if isCommunist(iPlayer) or isRepublic(iPlayer) and iEra >= iIndustrial: return iMao

		if iEra >= iRenaissance and iGameTurn >= getTurnForYear(1400): return iHongwu

		if bResurrected: return iHongwu

		if utils.getScenario() >= i1700AD: return iHongwu

		if iEra >= iMedieval: return iTaizong

	elif iPlayer == iBabylonia:
		if iGameTurn >= getTurnForYear(-1600): return iHammurabi

	elif iPlayer == iGreece:
		if iEra >= iIndustrial: return iGeorge

		if bResurrected and getColumn(iPlayer) >= 11: return iGeorge

		if iGameTurn >= getTurnForYear(-338): return iAlexanderTheGreat

	elif iPlayer == iPersia:
		if bReborn:
			if iEra >= iGlobal: return iKhomeini

			return iAbbas

		if getColumn(iPlayer) >= 6: return iKhosrow

		if bEmpire:
			return iDarius

	elif iPlayer == iPhoenicia:
		if not bCityStates: return iHannibal

		if capital.getRegionID() not in [rMesopotamia, rAnatolia]: return iHannibal

	elif iPlayer == iRome:
		if bEmpire or not bCityStates: return iAugustus

	elif iPlayer == iKorea:
		if iEra >= iRenaissance: return iSejong

		if utils.getScenario() >= i1700AD: return iSejong

	elif iPlayer == iMaya:
		if bReborn:
			return iBolivar
			
	#elif iPlayer == iJapan:
	#	if iEra >= iIndustrial: return iMeiji
		
	#	if tPlayer.isHasTech(iFeudalism): return iOdaNobunaga
		
	elif iPlayer == iEthiopia:
		if iEra >= iIndustrial: return iHaileSelassie

	elif iPlayer == iVietnam:
		if iEra >= iGlobal: return iHoChiMinh
		
		if iEra >= iMedieval: return iChieuHoang

	elif iPlayer == iTamils:
		if iEra >= iRenaissance: return iKrishnaDevaRaya

	elif iPlayer == iByzantium:
		if iGameTurn >= getTurnForYear(1000): return iBasil
		
	#elif iPlayer == iVikings:
	#	if iEra >= iGlobal: return iGerhardsen
		
	#	if iEra >= iRenaissance: return iGustav

	#elif iPlayer == iArabia:
	#	if iGameTurn >= getTurnForYear(1000): return iSaladin

	elif iPlayer == iTurks:
		if bResurrected or bReborn: return iTamerlane
	
		if iGameTurn >= getTurnForYear(1000): return iAlpArslan

	#elif iPlayer == iTibet:
	#	if iGameTurn >= getTurnForYear(1500): return iLobsangGyatso
		
	#elif iPlayer == iIndonesia:
	#	if iEra >= iGlobal: return iSuharto
		
	#	if bEmpire: return iHayamWuruk
		
	#elif iPlayer == iMoors:
	#	if not utils.isPlotInArea(tCapitalCoords, vic.tIberiaTL, vic.tIberiaBR): return iYaqub
		
	elif iPlayer == iSpain:
		if isFascist(iPlayer): return iFranco

		if True in data.lFirstContactConquerors: return iPhilip

	elif iPlayer == iFrance:
		if iEra >= iGlobal: return iDeGaulle

		if iEra >= iIndustrial: return iNapoleon

		if iEra >= iRenaissance: return iLouis

	elif iPlayer == iEngland:
		if iEra >= iGlobal: return iChurchill

		if iEra >= iIndustrial: return iVictoria

		if utils.getScenario() == i1700AD: return iVictoria

		if iEra >= iRenaissance: return iElizabeth

	elif iPlayer == iHolyRome:
		if iEra >= iIndustrial: return iFrancis

		if utils.getScenario() == i1700AD: return iFrancis

		if iEra >= iRenaissance: return iCharles

	elif iPlayer == iRussia:
		if iEra >= iIndustrial:
			if not bMonarchy: return iStalin

			return iAlexanderII

		if iEra >= iRenaissance:
			if iGameTurn >= getTurnForYear(1750): return iCatherine

			return iPeter
			
	elif iPlayer == iSwahili:
		if iEra >= iIndustrial: return iBarghash
		
		if bEmpire: return iDawud
		
	elif iPlayer == iMamluks:
		if not bMonarchy and iEra >= iGlobal: return iNasser
		
		if tPlayer.isHasTech(iGunpowder): return iBaibars
		
	elif iPlayer == iNetherlands:
		if iGameTurn >= getTurnForYear(1650): return iWilliam

	elif iPlayer == iPoland:
		if iEra >= iGlobal: return iWalesa

		if isFascist(iPlayer) or isCommunist(iPlayer): return iPilsudski

		if iEra >= iRenaissance: return iSobieski

		if utils.getScenario() == i1700AD: return iSobieski

	elif iPlayer == iPortugal:
		if iEra >= iIndustrial: return iMaria

		if tPlayer.isHasTech(iCartography): return iJoao

	elif iPlayer == iInca:
		if iEra >= iIndustrial: return iCastilla

		if bResurrected and iGameTurn >= getTurnForYear(1600): return iCastilla
	#elif iPlayer == iItaly:
	#	if isFascist(iPlayer): return iMussolini
	
	#	if iEra >= iIndustrial: return iCavour
		
	elif iPlayer == iMongolia:
		if iGameTurn >= getTurnForYear(1400): return iKublaiKhan

	elif iPlayer == iAztecs:
		if bReborn:
			if bMonarchy: return iSantaAnna

			if isFascist(iPlayer): return iSantaAnna

			if iEra >= iGlobal: return iCardenas

			return iJuarez

	elif iPlayer == iMughals:
		if iEra >= iGlobal: return iBhutto

		if getColumn(iPlayer) >= 9: return iAkbar

	elif iPlayer == iOttomans:
		if not bMonarchy and iEra >= iIndustrial: return iAtaturk

		if iEra >= iRenaissance: return iSuleiman

	elif iPlayer == iThailand:
		if iEra >= iIndustrial: return iMongkut

	elif iPlayer == iSweden:
		if iEra >= iIndustrial: return iKarl
		
		if bEmpire: return iGustav

	elif iPlayer == iManchuria:
		if iEra >= iIndustrial: return iCixi

	elif iPlayer == iGermany:
		if isFascist(iPlayer): return iHitler

		if getColumn(iPlayer) >= 14: return iBismarck

	elif iPlayer == iAmerica:
		if iEra >= iGlobal: return iRoosevelt

		if iGameTurn >= getTurnForYear(1850): return iLincoln

	elif iPlayer == iArgentina:
		if iEra >= iGlobal: return iPeron

	elif iPlayer == iBrazil:
		if iEra >= iGlobal: return iVargas
		
	elif iPlayer == iBoers:
		if iEra >= iDigital: return iMandela
		
	elif iPlayer == iAustralia:
		if iEra >= iGlobal: return iMenzies
		
	elif iPlayer == iCanada:
		if iEra >= iGlobal: return iTrudeau

	return startingLeader(iPlayer)


def leaderName(iPlayer):
	pPlayer = gc.getPlayer(iPlayer)
	iLeader = pPlayer.getLeader()

	iGameTurn = gc.getGame().getGameTurn()

	if iPlayer == iChina:
		if iLeader == iHongwu:
			if iGameTurn >= getTurnForYear(1700):
				return "TXT_KEY_LEADER_KANGXI"

	elif iPlayer == iTamils:
		if iLeader == iKrishnaDevaRaya:
			if iGameTurn >= getTurnForYear(1700):
				return "TXT_KEY_LEADER_TIPU_SULTAN"

	return None


### citis: Polity methods

def mapMinusOne(result):
	if result == -1:
		return None
	return result

def polityFallback(iPlayer, lPolities):
	for iPolity in lPolities:	
		dPolity = dPolities[iPolity]
		dCore = dPolity[iFieldCore]
		lPlots = Areas.getArea(iPlayer, {iPlayer : dCore["tRectangle"]}, {iPlayer : dCore["lExceptions"]})
		for (x, y) in lPlots:
			plot = gc.getMap().plot(x, y)
			if plot.isCity():
				city = plot.getPlotCity()
				if city.getOwner() == iPlayer:
					return iPolity
	return lPolities[0]
	
def getPolity(iPlayer):
	
	iGameTurn = gc.getGame().getGameTurn()
	pPlayer = gc.getPlayer(iPlayer)
	tPlayer = gc.getTeam(pPlayer.getTeam())
	iCivicGovernment, iCivicLegitimacy, iCivicSociety, iCivicEconomy, iCivicReligion, iCivicTerritory = getCivics(iPlayer)
	iNumCities = pPlayer.getNumCities()
	bReborn = pPlayer.isReborn()
	iReligion = pPlayer.getStateReligion()
	capital = gc.getPlayer(iPlayer).getCapitalCity()
	tCapitalCoords = capitalCoords(iPlayer)
	bAnarchy = pPlayer.isAnarchy()
	bEmpire = isEmpire(iPlayer)
	bCityStates = isCityStates(iPlayer)
	bTheocracy = (iCivicReligion == iTheocracy)
	bResurrected = data.players[iPlayer].iResurrections > 0
	bCapitulated = isCapitulated(iPlayer)
	iAnarchyTurns = data.players[iPlayer].iAnarchyTurns
	iEra = pPlayer.getCurrentEra()
	iGameEra = gc.getGame().getCurrentEra()
	bWar = isAtWar(iPlayer)
	bCityState = (iNumCities == 1)
	
	if iPlayer == iFrance:
		if iGameTurn < getTurnForYear(tBirth[iEngland]):
			return dPolities[iPolityFrancia]
		if isCommunist(iPlayer):
			return dPolities[iPolityFrenchCommune]
		x, y = tCapitalCoords
		if 55 <= x  and x <= 57 and 46 <= y and y <= 49:
			return dPolities[iPolityBurgundy]
		return dPolities[iPolityFrance]
	
	if iPlayer == iArabia:
		if iEra < iRenaissance:
			if iGameTurn > getTurnForYear(tBirth[iMoors]):
				return dPolities[iPolityAbbasids]
			bDamascus = gc.getMap().plot(74, 41).getOwner() == iArabia
			if bDamascus:
				return dPolities[iPolityUmmayads]
			return dPolities[iPolityRashiduns]
		if not bEmpire:
			if iEra == iRenaissance:
				return dPolities[iPolityDiriyah]
			elif iEra == iIndustrial:
				return dPolities[iPolityNedj]
			else:
				return dPolities[iPolitySaudis]
		if bEmpire and iEra > iRenaissance:
			return dPolities[iPolityArabLeague]
	
	if iPlayer == iTibet:
		return dPolities[iPolityTibet]
	
	if iPlayer == iIndonesia:
		if iEra >= iIndustrial:
			return dPolities[iPolityIndonesia]
		if iEra == iRenaissance or iReligion == iIslam:
			return dPolities[iPolityMataram]
		if getColumn(iPlayer) >= 8:
			return dPolities[iPolityMajapahit]
		if iEra == iMedieval:
			return dPolities[iPolityMelayu]
		else:
			return dPolities[iPolitySrivijaya]
	
	if iPlayer == iItaly:
		if iEra <= iRenaissance:
			return dPolities[iPolityVenice]
		else:
			return dPolities[iPolityItaly]
	
	if iPlayer == iVikings:
		if iEra == iMedieval and bEmpire:
			return dPolities[iPolityNorthSea]
		if iEra == iRenaissance and iGameTurn < getTurnForYear(1550):
			return dPolities[iPolityKalmarUnion]
		
		if utils.getHumanID() != iPlayer:
			if iEra == iMedieval:
				iPolity = polityFallback(iVikings, [iPolityDenmark, iPolityNorway, iPolitySweden])
			elif iEra == iRenaissance:
				iPolity = polityFallback(iVikings, [iPolitySweden, iPolityDenmark, iPolityNorway])
			elif iEra == iIndustrial:
				iDN = iPolityDenmark
				if bEmpire:
					iDN = iPolityDenmarkNorway
				iPolity = polityFallback(iVikings, [iDN, iPolityNorway, iPolitySweden])
			else:
				iPolity = polityFallback(iVikings, [iPolityNorway, iPolityDenmark, iPolitySweden])
			return dPolities[iPolity]

		x, y = tCapitalCoords
		if x > 60:
			return dPolities[iPolitySweden]
		elif y < 59:
			if bEmpire and iEra > iRenaissance:
				return dPolities[iPolityDenmarkNorway]
			return dPolities[iPolityDenmark]
		else:
			return dPolities[iPolityNorway]
	
	if iPlayer == iJapan:
		plot = gc.getMap().plot(113, 45)
		bKyoto = plot.isCity() and plot.getPlotCity().getOwner() == iPlayer
		if iEra == iMedieval and not bKyoto:
			return dPolities[iPolityOda]
		elif iEra <= iRenaissance:
			return dPolities[iPolityTokugawa]
		else:
			return dPolities[iPolityJapan]
	
	if iPlayer == iMoors:
		x, y = tCapitalCoords
		if y >= 40: #capital in Iberia
			if bCityStates:
				return dPolities[iPolityAndalus]
			else:
				return dPolities[iPolityCordoba]
		else:
			if iEra < iIndustrial:
				return dPolities[iPolityAlmohads]
			else:
				return dPolities[iPolityMorocco]
	
	return None

def getPolityTitle(iPlayer):
	polity = getPolity(iPlayer)
	if polity:
		return mapMinusOne(polity[iFieldTitle])
	return None
	
def getPolityTitleName(iPlayer):
	polity = getPolity(iPlayer)
	if polity:
		if polity[iFieldNameType] in [iTypeCapital] or isCityStates(iPlayer):
			capital = gc.getPlayer(iPlayer).getCapitalCity()
			if capital:
				return capital.getName()
			return None
		return mapMinusOne(polity[iFieldName])
	return None

def getPolityTitleAdjective(tPolity):
	if tPolity[iFieldNameType] in [iTypeNationalShort]:
		return None
	return mapMinusOne(tPolity[iFieldAdjective])

def getPolityShortName(iPlayer):
	polity = getPolity(iPlayer)
	if polity:
		if mapMinusOne(polity[iFieldName]):
			return polity[iFieldName]
		if polity[iFieldNameType] in [iTypeCapital]:
			capital = gc.getPlayer(iPlayer).getCapitalCity()
			if capital:
				return capital.getName()
	return None

def getPolityAdjective(iPlayer):
	polity = getPolity(iPlayer)
	if polity:
		if polity[iFieldNameType] in [iTypeDynastic]:
			return None
		return mapMinusOne(polity[iFieldAdjective])
	return None

def getPolityCapitalLocation(iPlayer):
	polity = getPolity(iPlayer)
	if polity:
		return mapMinusOne(polity[iFieldCapitalLocation])
	return None

def getPolityLeader(iPlayer):
	iGameTurn = gc.getGame().getGameTurn()
	pPlayer = gc.getPlayer(iPlayer)
	tPlayer = gc.getTeam(pPlayer.getTeam())
	iCivicGovernment, iCivicLegitimacy, iCivicSociety, iCivicEconomy, iCivicReligion, iCivicTerritory = getCivics(iPlayer)
	iNumCities = pPlayer.getNumCities()
	bReborn = pPlayer.isReborn()
	iReligion = pPlayer.getStateReligion()
	capital = gc.getPlayer(iPlayer).getCapitalCity()
	tCapitalCoords = capitalCoords(iPlayer)
	bAnarchy = pPlayer.isAnarchy()
	bEmpire = isEmpire(iPlayer)
	bCityStates = isCityStates(iPlayer)
	bTheocracy = (iCivicReligion == iTheocracy)
	bResurrected = data.players[iPlayer].iResurrections > 0
	bCapitulated = isCapitulated(iPlayer)
	iAnarchyTurns = data.players[iPlayer].iAnarchyTurns
	iEra = pPlayer.getCurrentEra()
	iGameEra = gc.getGame().getCurrentEra()
	bWar = isAtWar(iPlayer)
	bCityState = (iNumCities == 1)
	
	iCurrentLeader = gc.getPlayer(iPlayer).getLeader()
		
	polity = getPolity(iPlayer)
	if polity:
		if polity == iPolityFrance:
			if iEra >= iGlobal: return iDeGaulle
			if iEra >= iIndustrial: return iNapoleon
			if iEra >= iRenaissance: return iLouis
		elif polity == iPolityTibet:
			if iGameTurn >= getTurnForYear(1500): return iLobsangGyatso
		elif polity == iPolityItaly:
			if iEra >= iGlobal: return iMussolini
			return iCavour
		
		iLeader = polity[iFieldLeader]
		if iLeader > -1:
			return iLeader
		return iCurrentLeader
	return leader(iPlayer)

def getPolityCore(iPlayer):
	polity = getPolity(iPlayer)
	if polity:
		dCore = mapMinusOne(polity[iFieldCore])
		if dCore:
			tCore = dCore['tRectangle']
			lExceptions = dCore['lExceptions']
			return Areas.getArea(iPlayer, {iPlayer : tCore}, {iPlayer : lExceptions})
	return None
	

def foundCity(iPlayer, tPlot, sName, iPopulation, iUnitType = -1, iNumUnits = -1, lReligions = [], lBuildings = [], iCulture = 1):
	pPlayer = gc.getPlayer(iPlayer)
	x, y = tPlot
	plot = gc.getMap().plot(x, y)
	plot.setOwner(iPlayer)
	pPlayer.found(x, y)
	
	if plot.isCity():
		city = gc.getMap().plot(x, y).getPlotCity()
		
		city.setName(sName, False)
		city.setPopulation(iPopulation)
		
		plot.changeCulture(iPlayer, iCulture, True)
		city.changeCulture(iPlayer, iCulture, True)
		
		if iNumUnits > 0 and iUnitType > 0:
			utils.makeUnit(iUnitType, iPlayer, tPlot, iNumUnits)
			
		for iReligion in lReligions:
			if gc.getGame().isReligionFounded(iReligion):
				city.setHasReligion(iReligion, True, False, False)
				
		for iBuilding in lBuildings:
			city.setHasRealBuilding(iBuilding, True)
		
		return True
	
	return False
	
def checkShortAdjectiveCapitalLeaderCore(iPlayer):
	
	short = getPolityShortName(iPlayer)
	if short:
		setShort(iPlayer, short)
	
	adjective = getPolityAdjective(iPlayer)
	if adjective:
		setAdjective(iPlayer, adjective)
	
	iLeader = getPolityLeader(iPlayer)
	setLeader(iPlayer, iLeader)
	
	lCore = getPolityCore(iPlayer)
	if lCore:
		Areas.updateCore(iPlayer, lCore)
	
	if gc.getPlayer(iPlayer).getNumCities() == 0 or iPlayer == utils.getHumanID():
		return
	
	tNewCapital = getPolityCapitalLocation(iPlayer)
	if not tNewCapital:
		return
	x, y = tNewCapital
	currentCapital = gc.getPlayer(iPlayer).getCapitalCity()
	if currentCapital.getX() != x or currentCapital.getY() != y:
		plot = gc.getMap().plot(x, y)
		if plot.isCity():
			if controlsCity(iPlayer, tNewCapital):
				utils.moveCapital(iPlayer, tNewCapital)
		else:
			#shall found the new capital
			pPlayer = gc.getPlayer(iPlayer)
			iEra = pPlayer.getCurrentEra()
			iEraModifier = iEra + 1
			tPlot = tNewCapital
			sName = cnm.getFoundName(iPlayer, tPlot)
			iPopulation = iEraModifier
			iUnitType = iArcher
			iNumUnits = iEraModifier
			lReligions = []
			iReligion = pPlayer.getStateReligion()
			if iReligion:
				lReligions.append(iReligion)
			lBuildings = []
			if iEra >= iClassical:
				lBuildings = lBuildings + [iGranary, iSmokehouse, iMonument]
			if iEra >= iMedieval:
				lBuildings = lBuildings + [iMarket, iLibrary]
			if iEra >= iRenaissance:
				lBuildings = lBuildings + [iWalls, iCastle, iPostOffice]
			if iEra >= iGlobal:
				lBuildings = lBuildings + [iFactory]
			iCulture = 10 * iEraModifier
			foundCity(iPlayer, tPlot, sName, iPopulation, iUnitType, iNumUnits, lReligions, lBuildings, iCulture)
			city = gc.getMap().plot(x, y).getPlotCity()
			if city.isCoastal(20):
				city.setHasRealBuilding(iHarbor, True)
			utils.moveCapital(iPlayer, tPlot)

