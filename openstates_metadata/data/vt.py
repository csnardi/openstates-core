from ..models import State, Chamber, District

VT = State(
    name="Vermont",
    abbr="VT",
    capital="Montpelier",
    capital_tz="America/New_York",
    fips="50",
    unicameral=False,
    legislature_name="Vermont General Assembly",
    division_id="ocd-division/country:us/state:vt",
    jurisdiction_id="ocd-jurisdiction/country:us/state:vt/government",
    url="http://legislature.vermont.gov/",
    lower=Chamber(
        chamber_type="lower",
        name="House",
        num_seats=150,
        title="Representative",
        districts=[
            District("Addison-1", 2),
            District("Addison-2", 1),
            District("Addison-3", 2),
            District("Addison-4", 2),
            District("Addison-5", 1),
            District("Addison-Rutland", 1),
            District("Bennington-1", 1),
            District("Bennington-2-1", 2),
            District("Bennington-2-2", 2),
            District("Bennington-3", 1),
            District("Bennington-4", 2),
            District("Bennington-Rutland", 1),
            District("Caledonia-1", 1),
            District("Caledonia-2", 1),
            District("Caledonia-3", 2),
            District("Caledonia-4", 2),
            District("Caledonia-Washington", 1),
            District("Chittenden-10", 2),
            District("Chittenden-1", 1),
            District("Chittenden-2", 2),
            District("Chittenden-3", 2),
            District("Chittenden-4-1", 1),
            District("Chittenden-4-2", 1),
            District("Chittenden-5-1", 1),
            District("Chittenden-5-2", 1),
            District("Chittenden-6-1", 2),
            District("Chittenden-6-2", 1),
            District("Chittenden-6-3", 2),
            District("Chittenden-6-4", 2),
            District("Chittenden-6-5", 2),
            District("Chittenden-6-6", 1),
            District("Chittenden-6-7", 2),
            District("Chittenden-7-1", 1),
            District("Chittenden-7-2", 1),
            District("Chittenden-7-3", 1),
            District("Chittenden-7-4", 1),
            District("Chittenden-8-1", 2),
            District("Chittenden-8-2", 2),
            District("Chittenden-8-3", 1),
            District("Chittenden-9-1", 2),
            District("Chittenden-9-2", 2),
            District("Essex-Caledonia", 1),
            District("Essex-Caledonia-Orleans", 1),
            District("Franklin-1", 1),
            District("Franklin-2", 1),
            District("Franklin-3-1", 2),
            District("Franklin-3-2", 1),
            District("Franklin-4", 2),
            District("Franklin-5", 2),
            District("Franklin-6", 1),
            District("Franklin-7", 1),
            District("Grand Isle-Chittenden", 2),
            District("Lamoille-1", 1),
            District("Lamoille-2", 2),
            District("Lamoille-3", 1),
            District("Lamoille-Washington", 2),
            District("Orange-1", 2),
            District("Orange-2", 1),
            District("Orange-Caledonia", 1),
            District("Orange-Washington-Addison", 2),
            District("Orleans-1", 2),
            District("Orleans-2", 2),
            District("Orleans-Caledonia", 2),
            District("Orleans-Lamoille", 1),
            District("Rutland-1", 1),
            District("Rutland-2", 2),
            District("Rutland-3", 2),
            District("Rutland-4", 1),
            District("Rutland-5-1", 1),
            District("Rutland-5-2", 1),
            District("Rutland-5-3", 1),
            District("Rutland-5-4", 1),
            District("Rutland-6", 2),
            District("Rutland-Bennington", 1),
            District("Rutland-Windsor-1", 1),
            District("Rutland-Windsor-2", 1),
            District("Washington-1", 2),
            District("Washington-2", 2),
            District("Washington-3", 2),
            District("Washington-4", 2),
            District("Washington-5", 1),
            District("Washington-6", 1),
            District("Washington-7", 2),
            District("Washington-Chittenden", 2),
            District("Windham-1", 1),
            District("Windham-2-1", 1),
            District("Windham-2-2", 1),
            District("Windham-2-3", 1),
            District("Windham-3", 2),
            District("Windham-4", 2),
            District("Windham-5", 1),
            District("Windham-6", 1),
            District("Windham-Bennington", 1),
            District("Windham-Bennington-Windsor", 1),
            District("Windsor-1", 2),
            District("Windsor-2", 1),
            District("Windsor-3-1", 1),
            District("Windsor-3-2", 2),
            District("Windsor-4-1", 1),
            District("Windsor-4-2", 2),
            District("Windsor-5", 1),
            District("Windsor-Orange-1", 1),
            District("Windsor-Orange-2", 2),
            District("Windsor-Rutland", 1),
        ],
    ),
    upper=Chamber(
        chamber_type="upper",
        name="Senate",
        num_seats=30,
        title="Senator",
        districts=[
            District("Addison", 2),
            District("Bennington", 2),
            District("Caledonia", 2),
            District("Chittenden", 6),
            District("Essex-Orleans", 2),
            District("Franklin", 2),
            District("Grand Isle", 1),
            District("Lamoille", 1),
            District("Orange", 1),
            District("Rutland", 3),
            District("Washington", 3),
            District("Windham", 2),
            District("Windsor", 3),
        ],
    ),
)