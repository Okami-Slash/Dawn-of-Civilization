//Rhye
#ifndef CVRHYES_H
#define CVRHYES_H

using namespace std;
typedef list<char*> LISTCHAR;

// rhyes.h
#define EARTH_X					(124)
#define EARTH_Y					(68)

#define MAX_COM_SHRINE			(20)
#define BEGIN_WONDERS				(182) // increment if normal building (not for wonders) is added
#define BEGIN_GREAT_WONDERS			(BEGIN_WONDERS+12)
#define NUM_BUILDINGS_PLAGUE		(259) // always increment when a building is added
#define NUM_BUILDINGTYPES_PLAGUE	(168) // increment when a building class is added

#define NUM_MAJOR_PLAYERS		(55)
#define NUM_MINORS				(5)	 // Independent, Independent2, Natives, Celtia, Barbarians
#define NUM_CIVS				(62)

#define NUM_ERAS				(ERA_DIGITAL+1)

#define PAGAN_TEMPLE			((BuildingTypes)GC.getInfoTypeForString("BUILDING_PAGAN_TEMPLE"))
#define BUILDING_PALACE			((BuildingClassTypes)0)
#define BUILDING_PLAGUE			(NUM_BUILDINGS_PLAGUE-1)

#define UNITCLASS_SLAVE			((UnitClassTypes)GC.getInfoTypeForString("UNITCLASS_SLAVE"))

enum DoCTechs
{
	TANNING,
	MINING,
	POTTERY,
	PASTORALISM,
	AGRICULTURE,
	MYTHOLOGY,
	SAILING,

	SMELTING,
	MASONRY,
	LEVERAGE,
	PROPERTY,
	CEREMONY,
	DIVINATION,
	SEAFARING,

	ALLOYS,
	CONSTRUCTION,
	RIDING,
	ARITHMETICS,
	WRITING,
	CALENDAR,
	SHIPBUILDING,

	BLOOMERY,
	CEMENT,
	MATHEMATICS,
	CONTRACT,
	LITERATURE,
	PRIESTHOOD,
	NAVIGATION,

	GENERALSHIP,
	ENGINEERING,
	AESTHETICS,
	CURRENCY,
	LAW,
	PHILOSOPHY,
	MEDICINE,

	NOBILITY,
	STEEL,
	ARCHITECTURE,
	ARTISANRY,
	POLITICS,
	SCHOLARSHIP,
	ETHICS,

	FEUDALISM,
	FORTIFICATION,
	MACHINERY,
	ALCHEMY,
	GUILDS,
	CIVIL_SERVICE,
	THEOLOGY,

	COMMUNE,
	CROP_ROTATION,
	PAPER,
	COMPASS,
	PATRONAGE,
	EDUCATION,
	DOCTRINE,

	GUNPOWDER,
	COMPANIES,
	FINANCE,
	CARTOGRAPHY,
	HUMANITIES,
	PRINTING,
	JUDICIARY,

	FIREARMS,
	LOGISTICS,
	EXPLORATION,
	OPTICS,
	ACADEMIA,
	STATECRAFT,
	HERITAGE,

	COMBINED_ARMS,
	ECONOMICS,
	GEOGRAPHY,
	SCIENTIFIC_METHOD,
	URBAN_PLANNING,
	CIVIL_LIBERTIES,
	HORTICULTURE,

	REPLACEABLE_PARTS,
	HYDRAULICS,
	PHYSICS,
	GEOLOGY,
	MEASUREMENT,
	SOCIOLOGY,
	SOCIAL_CONTRACT,

	MACHINE_TOOLS,
	THERMODYNAMICS,
	METALLURGY,
	CHEMISTRY,
	BIOLOGY,
	REPRESENTATION,
	NATIONALISM,

	BALLISTICS,
	ENGINE,
	RAILROAD,
	ELECTRICITY,
	REFRIGERATION,
	LABOUR_UNIONS,
	JOURNALISM,

	PNEUMATICS,
	ASSEMBLY_LINE,
	REFINING,
	FILM,
	MICROBIOLOGY,
	CONSUMERISM,
	CIVIL_RIGHTS,

	INFRASTRUCTURE,
	FLIGHT,
	SYNTHETICS,
	RADIO,
	PSYCHOLOGY,
	MACROECONOMICS,
	SOCIAL_SERVICES,

	AVIATION,
	ROCKETRY,
	FISSION,
	ELECTRONICS,
	TELEVISION,
	POWER_PROJECTION,
	GLOBALISM,

	RADAR,
	SPACEFLIGHT,
	NUCLEAR_POWER,
	LASER,
	COMPUTERS,
	TOURISM,
	ECOLOGY,

	AERODYNAMICS,
	SATELLITES,
	SUPERCONDUCTORS,
	ROBOTICS,
	TELECOMMUNICATIONS,
	RENEWABLE_ENERGY,
	GENETICS,

	SUPERMATERIALS,
	FUSION,
	NANTECHNOLOGY,
	AUTOMATION,
	BIOTECHNOLOGY,

	UNIFIED_THEORY,
	ARTIFICIAL_INTELLIGENCE,

	TRANSHUMANISM,
};

enum DoCBuildings
{
	TRIUMPHAL_ARCH = BEGIN_WONDERS,
	NATIONAL_THEATRE,
	TRADING_COMPANY,
	IBERIAN_TRADING_COMPANY,
	CENTRAL_BANK,
	NATIONAL_COLLEGE,
	NATIONAL_GALLERY,
	NATIONAL_MONUMENT,
	IRONWORKS,
	MILITARY_ACADEMY,
	NATIONAL_PARK,
	RED_CROSS,
	GREAT_SPHINX,
	GREAT_LIGHTHOUSE,
	GREAT_COTHON,
	TERRACOTTA_ARMY,
	TEMPLE_OF_ARTEMIS,
	PYRAMIDS,
	HANGING_GARDENS,
	ORACLE,
	MOAI_STATUES,
	ISHTAR_GATE,
	COLOSSUS,
	PARTHENON,
	STATUE_OF_ZEUS,
	SHWEDAGON_PAYA,
	KHAJURAHO,
	GREAT_LIBRARY,
	MAUSOLEUM_OF_MAUSSOLLOS,
	FLOATING_GARDENS,
	COLOSSEUM,
	GREAT_WALL,
	THEODOSIAN_WALLS,
	MACHU_PICCHU,
	BOROBUDUR,
	GRAND_CANAL,
	HAGIA_SOPHIA,
	NOTRE_DAME,
	TEMPLE_OF_KUKULKAN,
	HIMEJI_CASTLE,
	BLUE_MOSQUE,
	WAT_PREAH_PISNULOK,
	TOPKAPI_PALACE,
	LA_MEZQUITA,
	SISTINE_CHAPEL,
	LEANING_TOWER,
	RED_FORT,
	VERSAILLES,
	FORBIDDEN_PALACE,
	SPIRAL_MINARET,
	DOME_OF_THE_ROCK,
	UNIVERSITY_OF_SANKORE,
	TAJ_MAHAL,
	SAN_MARCO_BASILICA,
	PORCELAIN_TOWER,
	ST_BASILS_CATHEDRAL,
	HARMANDIR_SAHIB,
	TRAFALGAR_SQUARE,
	BRANDENBURG_GATE,
	STATUE_OF_LIBERTY,
	PENTAGON,
	LUBYANKA,
	WESTMINSTER_PALACE,
	EIFFEL_TOWER,
	EMPIRE_STATE_BUILDING,
	CERN_RESEARCH_COMPLEX,
	WEMBLEY,
	GRACELAND,
	CRISTO_REDENTOR,
	ITAIPU_DAM,
	HOLLYWOOD,
	UNITED_NATIONS,
	CN_TOWER,
	SYDNEY_OPERA,
	ASHURBANIPAL_LIBRARY,
	SPACE_ELEVATOR,
};

enum DoCEras
{
	ERA_ANCIENT,
	ERA_CLASSICAL,
	ERA_MEDIEVAL,
	ERA_RENAISSANCE,
	ERA_INDUSTRIAL,
	ERA_GLOBAL,
	ERA_DIGITAL,
	ERA_MIDDLE_EAST,
	ERA_EAST_ASIA,
	ERA_SOUTH_ASIA,
};

enum Regions
{
	REGION_BRITAIN,
	REGION_IBERIA,
	REGION_ITALY,
	REGION_BALKANS,
	REGION_EUROPE,
	REGION_SCANDINAVIA,
	REGION_RUSSIA,
	REGION_ANATOLIA,
	REGION_MESOPOTAMIA,
	REGION_ARABIA,
	REGION_EGYPT,
	REGION_MAGHREB,
	REGION_PERSIA,
	REGION_INDIA,
	REGION_DECCAN,
	REGION_INDOCHINA,
	REGION_INDONESIA,
	REGION_CHINA,
	REGION_KOREA,
	REGION_JAPAN,
	REGION_MANCHURIA,
	REGION_TIBET,
	REGION_CENTRAL_ASIA,
	REGION_SIBERIA,
	REGION_AUSTRALIA,
	REGION_OCEANIA,
	REGION_ETHIOPIA,
	REGION_WEST_AFRICA,
	REGION_SOUTH_AFRICA,
	REGION_CANADA,
	REGION_ALASKA,
	REGION_UNITED_STATES,
	REGION_CARIBBEAN,
	REGION_MESOAMERICA,
	REGION_BRAZIL,
	REGION_ARGENTINA,
	REGION_PERU,
	REGION_COLOMBIA,
	NUM_REGIONS
};

enum ECSArtStyles
{
	ARTSTYLE_AFRICA,
	ARTSTYLE_ANGLO_AMERICA,
	ARTSTYLE_ARABIA,
	ARTSTYLE_ASIA,
	ARTSTYLE_BARBARIAN,
	ARTSTYLE_CRESCENT,
	ARTSTYLE_EGYPT,
	ARTSTYLE_EUROPE,
	ARTSTYLE_GRECO_ROMAN,
	ARTSTYLE_INDIA,
	ARTSTYLE_IBERIA,
	ARTSTYLE_JAPAN,
	ARTSTYLE_MESO_AMERICA,
	ARTSTYLE_MONGOLIA,
	ARTSTYLE_NATIVE_AMERICA,
	ARTSTYLE_NORSE,
	ARTSTYLE_RUSSIA,
	ARTSTYLE_SOUTH_AMERICA,
	ARTSTYLE_SOUTH_EAST_ASIA,
	ARTSTYLE_SOUTH_PACIFIC,
};

#endif	// CVRHYES_H

static const int lTechLeaderPenalty[NUM_ERAS] = {0, 0, 20, 25, 30, 40, 50};
static const int lTechBackwardsBonus[NUM_ERAS] = {0, 20, 30, 40, 50, 60, 75};

// Leoreth: order of persecution
static const int persecutionOrder[NUM_RELIGIONS][NUM_RELIGIONS-1] =
{
	// Judaism
	{HINDUISM, BUDDHISM, TAOISM, CONFUCIANISM, ZOROASTRIANISM, ISLAM, PROTESTANTISM, CATHOLICISM, ORTHODOXY},
	// Orthodoxy
	{ISLAM, PROTESTANTISM, CATHOLICISM, JUDAISM, ZOROASTRIANISM, HINDUISM, BUDDHISM, CONFUCIANISM, TAOISM},
	// Catholicism
	{ISLAM, PROTESTANTISM, ORTHODOXY, JUDAISM, ZOROASTRIANISM, HINDUISM, BUDDHISM, CONFUCIANISM, TAOISM},
	// Protestantism
	{ISLAM, CATHOLICISM, ORTHODOXY, JUDAISM, ZOROASTRIANISM, HINDUISM, BUDDHISM, CONFUCIANISM, TAOISM},
	// Islam
	{ZOROASTRIANISM, HINDUISM, PROTESTANTISM, CATHOLICISM, ORTHODOXY, JUDAISM, BUDDHISM, CONFUCIANISM, TAOISM},
	// Hinduism
	{ISLAM, ORTHODOXY, PROTESTANTISM, CATHOLICISM, JUDAISM, CONFUCIANISM, TAOISM, ZOROASTRIANISM, BUDDHISM},
	// Buddhism
	{ORTHODOXY, PROTESTANTISM, CATHOLICISM, JUDAISM, ZOROASTRIANISM, TAOISM, ISLAM, CONFUCIANISM, HINDUISM},
	// Confucianism
	{ISLAM, ORTHODOXY, PROTESTANTISM, CATHOLICISM, JUDAISM, ZOROASTRIANISM, HINDUISM, BUDDHISM, TAOISM},
	// Taoism
	{ISLAM, ORTHODOXY, PROTESTANTISM, CATHOLICISM, JUDAISM, ZOROASTRIANISM, HINDUISM, BUDDHISM, CONFUCIANISM},
	// Zoroastrianism
	{ISLAM, PROTESTANTISM, CATHOLICISM, ORTHODOXY, JUDAISM, HINDUISM, BUDDHISM, CONFUCIANISM, TAOISM},
};

// Leoreth: persecution priority
static const int persecutionValue[NUM_RELIGIONS][NUM_RELIGIONS] =
{
	// JUD ORT CAT PRO ISL HIN BUD CON TAO ZOR
	{  -1,  1,  1,  1,  1,  1,  1,  1,  1,  1 }, // Judaism
	{   1, -1,  3,  3,  4,  1,  1,  1,  1,  2 }, // Orthodoxy
	{   2,  2, -1,  3,  4,  1,  1,  1,  1,  2 }, // Catholicism
	{   3,  2,  3, -1,  4,  1,  1,  1,  1,  2 }, // Protestantism
	{   1,  2,  2,  2, -1,  3,  1,  1,  1,  4 }, // Islam
	{   1,  3,  3,  3,  4, -1,  0,  1,  1,  2 }, // Hinduism
	{   1,  3,  3,  3,  4,  0, -1,  1,  1,  2 }, // Buddhism
	{   1,  2,  2,  2,  3,  1,  1, -1,  0,  1 }, // Confucianism
	{   1,  2,  2,  2,  3,  1,  1,  0, -1,  1 }, // Taoism
	{   1,  3,  3,  3,  4,  1,  1,  1,  1, -1 }, // Zoroastrianism
};
