import pandas as pd

# Golf courses data for all Maryland regions
def load_golf_courses():
    courses = {
        'name': [
            # Baltimore City
            'Carroll Park Golf Course',
            'Forest Park Golf Course',
            'Mount Pleasant Golf Course',
            'Pine Ridge Golf Course',
            'Clifton Park Golf Course',
            # Baltimore County
            'Diamond Ridge Golf Course',
            'Fox Hollow Golf Course',
            'Rocky Point Golf Course',
            'The Woodlands Golf Course',
            'Greystone Golf Course',
            'Oakmont Green Golf Course',
            'Gunpowder Falls Golf Course',
            # Howard County
            'Fairway Hills Golf Club',
            'Hobbit\'s Glen Golf Club',
            'Timbers at Troy Golf Course',
            # Anne Arundel County
            'Compass Pointe Golf Courses',
            'Eisenhower Golf Course',
            'Bay Hills Golf Club',
            # Harford County
            'Mountain Branch Golf Course',
            'Swan Creek Golf Club',
            'Winter\'s Run Golf Club',
            # Western Maryland - Existing
            'Black Rock Golf Course',
            'Musket Ridge Golf Club',
            'Maryland National Golf Club',
            'Clustered Spires Golf Club',
            # Western Maryland - New
            'Cumberland Country Club',
            'Rocky Gap Casino Resort Golf Course',
            'Maplehurst Country Club',
            'Polish Mountain Golf Course',
            # Southern Maryland - Existing
            'Chesapeake Hills Golf Course',
            'Wicomico Shores Golf Course',
            'White Plains Golf Course',
            'Swan Point Yacht & Country Club',
            # Southern Maryland - New
            'Breton Bay Golf & Country Club',
            'Twin Shields Golf Club',
            'Laurel Springs Regional Park Golf Course',
            'Lake Presidential Golf Club',
            # Eastern Shore - Existing
            'Ocean City Golf Club',
            'Eagle\'s Landing Golf Course',
            'River Run Golf Club',
            'Rum Pointe Seaside Golf Links',
            'Bay Club Golf Course',
            # Eastern Shore - New
            'Ocean Pines Golf Club',
            'Glen Riddle Golf Club',
            'The Links at Lighthouse Sound',
            'Newport Bay Golf Club',
            'Beach Club Golf Links',
            # Central Maryland - Existing
            'Blue Mash Golf Course',
            'Hampshire Greens Golf Course',
            'Rattlewood Golf Course',
            'Waverly Woods Golf Club',
            'Worthington Manor Golf Club',
            # Central Maryland - New
            'Little Bennett Golf Course',
            'Poolesville Golf Course',
            'Whiskey Creek Golf Club',
            'Holly Hills Country Club',
            'Bretton Woods Recreation Center'
        ],
        'address': [
            # Baltimore City
            '2100 Washington Blvd, Baltimore, MD 21230',
            '2900 Hillsdale Rd, Baltimore, MD 21207',
            '6001 Hillen Road, Baltimore, MD 21239',
            '2101 Dulaney Valley Rd, Lutherville-Timonium, MD 21093',
            '2701 St Lo Dr, Baltimore, MD 21213',
            '2701 Ridge Rd, Windsor Mill, MD 21244',
            '1 Cardigan Rd, Timonium, MD 21093',
            '1935 Back River Neck Rd, Essex, MD 21221',
            '2309 Ridge Rd, Windsor Mill, MD 21244',
            '2115 White Hall Rd, White Hall, MD 21161',
            '2290 Golf View Ln, Hampstead, MD 21074',
            '2801 Jerusalem Rd, Kingsville, MD 21087',
            '5100 Columbia Rd, Columbia, MD 21044',
            '11130 Willow Bottom Dr, Columbia, MD 21044',
            '6100 Marshalee Drive, Elkridge, MD 21075',
            '9010 Fort Smallwood Rd, Pasadena, MD 21122',
            '1576 Generals Hwy, Crownsville, MD 21032',
            '545 Bay Hills Dr, Arnold, MD 21012',
            '1827 Mountain Rd, Joppa, MD 21085',
            '100 Walter Ward Blvd, Aberdeen, MD 21001',
            '800 S Main St, Bel Air, MD 21014',
            # Western Maryland - Existing
            '12287 Greencastle Pike, Hagerstown, MD 21740',
            '3880 Arabis Dr, Myersville, MD 21773',
            '8836 Hollow Rd, Middletown, MD 21769',
            '3225 Clustered Spires Dr, Frederick, MD 21704',
            # Western Maryland - New
            '10200 Country Club Rd, Cumberland, MD 21502',
            '16700 Lakeview Rd NE, Flintstone, MD 21530',
            '1 Maplehurst Country Club, Frostburg, MD 21532',
            '13100 Polish Mountain Rd, Cumberland, MD 21502',
            # Southern Maryland - Existing
            '11352 HG Trueman Rd, Lusby, MD 20657',
            '35794 Aviation Yacht Club Rd, Mechanicsville, MD 20659',
            '1015 St Charles Pkwy, White Plains, MD 20695',
            '11550 Swan Point Blvd, Issue, MD 20645',
            # Southern Maryland - New
            '21935 Society Hill Rd, Leonardtown, MD 20650',
            '2222 Solomons Island Rd, Huntingtown, MD 20639',
            '9400 Piscataway Dr, Clinton, MD 20735',
            '3151 Presidential Golf Dr, Upper Marlboro, MD 20774',
            # Eastern Shore - Existing
            '11401 Country Club Dr, Berlin, MD 21811',
            '12367 Eagles Nest Rd, Berlin, MD 21811',
            '11605 Masters Ln, Berlin, MD 21811',
            '7000 Rum Pointe Ln, Berlin, MD 21811',
            '9122 Libertytown Rd, Berlin, MD 21811',
            # Eastern Shore - New
            '100 Clubhouse Dr, Ocean Pines, MD 21811',
            '11501 Maid at Arms Ln, Berlin, MD 21811',
            '12723 St Martins Neck Rd, Bishopville, MD 21813',
            '11444 Newport Bay Dr, Berlin, MD 21811',
            '9715 Deer Park Dr, Berlin, MD 21811',
            # Central Maryland - Existing
            '5821 Olney Laytonsville Rd, Laytonsville, MD 20882',
            '2300 York Rd, Silver Spring, MD 20904',
            '1600 Rattlewood Dr, Mt Airy, MD 21771',
            '2100 Warwick Way, Marriottsville, MD 21104',
            '8329 Fingerboard Rd, Urbana, MD 21704',
            # Central Maryland - New
            '25900 Prescott Rd, Clarksburg, MD 20871',
            '16601 W Willard Rd, Poolesville, MD 20837',
            '4804 Whiskey Creek Rd, Ijamsville, MD 21754',
            '5502 Mussetter Rd, Ijamsville, MD 21754',
            '15700 River Rd, Potomac, MD 20878'
        ],
        'holes': [
            # First 21 courses remain unchanged
            18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 36, 18, 18, 18, 18, 18,
            # Western Maryland (Existing + New)
            18, 18, 18, 18, 18, 18, 18, 18,
            # Southern Maryland (Existing + New)
            18, 18, 18, 18, 18, 18, 18, 18,
            # Eastern Shore (Existing + New)
            36, 18, 18, 18, 18, 18, 36, 18, 18, 18,
            # Central Maryland (Existing + New)
            18, 18, 18, 18, 18, 18, 18, 18, 18, 18
        ],
        'par': [
            # First 21 courses remain unchanged
            70, 71, 71, 72, 70, 72, 71, 71, 70, 72, 71, 70, 70, 72, 72, 72, 71, 71, 72, 71, 70,
            # Western Maryland (Existing + New)
            72, 72, 71, 72, 72, 72, 71, 70,
            # Southern Maryland (Existing + New)
            72, 71, 72, 72, 72, 71, 72, 72,
            # Eastern Shore (Existing + New)
            72, 72, 72, 72, 72, 72, 72, 72, 72, 71,
            # Central Maryland (Existing + New)
            72, 72, 72, 72, 72, 71, 70, 72, 72, 72
        ],
        'weekday_price': [
            # First 21 courses remain unchanged
            25, 28, 32, 35, 26, 45, 42, 38, 40, 48, 42, 35, 42, 55, 48, 52, 45, 48, 52, 38, 42,
            # Western Maryland (Existing + New)
            45, 65, 59, 45, 65, 89, 45, 35,
            # Southern Maryland (Existing + New)
            42, 38, 45, 75, 52, 45, 39, 89,
            # Eastern Shore (Existing + New)
            89, 69, 65, 89, 49, 59, 79, 95, 65, 55,
            # Central Maryland (Existing + New)
            65, 55, 48, 62, 69, 45, 39, 85, 75, 69
        ],
        'weekend_price': [
            # First 21 courses remain unchanged
            32, 35, 40, 45, 33, 55, 52, 48, 50, 58, 52, 45, 52, 65, 58, 62, 55, 58, 62, 48, 52,
            # Western Maryland (Existing + New)
            55, 85, 79, 55, 85, 119, 55, 45,
            # Southern Maryland (Existing + New)
            52, 48, 55, 95, 65, 55, 49, 109,
            # Eastern Shore (Existing + New)
            109, 89, 85, 109, 59, 79, 99, 125, 85, 75,
            # Central Maryland (Existing + New)
            85, 75, 58, 82, 89, 55, 49, 105, 95, 89
        ],
        'phone': [
            # First 21 phones remain unchanged
            '410-685-8344', '410-448-4653', '410-254-5100', '410-252-1408', '410-243-3200',
            '410-887-1349', '410-887-7735', '410-887-0215', '410-887-1349', '410-887-1945',
            '410-239-7114', '410-592-8877', '410-730-1112', '410-730-5980', '410-313-4653',
            '410-255-7764', '410-571-0973', '410-974-0669', '410-836-9600', '410-272-7500',
            '410-879-1500',
            # Western Maryland (Existing + New)
            '240-313-2816', '301-293-9930', '301-371-0000', '301-600-1295',
            '301-724-6200', '301-784-8690', '301-689-3200', '301-722-4512',
            # Southern Maryland (Existing + New)
            '410-326-4653', '301-769-2500', '301-645-1300', '301-259-0047',
            '301-475-2300', '410-535-1393', '301-868-6700', '301-627-8577',
            # Eastern Shore (Existing + New)
            '410-641-1779', '410-213-7277', '410-641-7200', '410-213-2325', '410-641-4081',
            '410-641-6057', '410-213-2325', '410-641-7200', '410-208-2827', '410-213-1173',
            # Central Maryland (Existing + New)
            '301-948-1075', '301-476-7999', '301-831-7389', '410-442-2250', '301-874-5400',
            '301-253-1335', '301-428-8401', '301-607-7200', '301-371-0200', '301-299-5156'
        ],
        'amenities': [
            # First 21 amenities remain unchanged
            'Driving Range, Pro Shop, Restaurant',
            'Pro Shop, Putting Green, Restaurant',
            'Driving Range, Pro Shop, Lessons',
            'Driving Range, Pro Shop, Restaurant, Lessons',
            'Pro Shop, Putting Green',
            'Driving Range, Pro Shop, Restaurant, Practice Facility',
            'Driving Range, Pro Shop, Restaurant, Lessons',
            'Pro Shop, Restaurant, Practice Green',
            'Driving Range, Pro Shop, Restaurant',
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Lessons',
            'Pro Shop, Restaurant, Practice Facility',
            'Pro Shop, Practice Green, Snack Bar',
            'Pro Shop, Practice Facility, Restaurant',
            'Driving Range, Pro Shop, Restaurant, Lessons',
            'Driving Range, Pro Shop, Restaurant, Practice Facility',
            'Driving Range, Pro Shop, Restaurant, Practice Facility, 36 Holes',
            'Pro Shop, Practice Facility, Restaurant',
            'Pro Shop, Restaurant, Practice Green',
            'Driving Range, Pro Shop, Restaurant, Practice Facility',
            'Pro Shop, Restaurant, Practice Green',
            'Pro Shop, Restaurant, Practice Facility',
            # Western Maryland (Existing + New)
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Lessons',
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Club Rentals',
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Lessons',
            'Pro Shop, Restaurant, Practice Facility, Club Rentals',
            'Pro Shop, Restaurant, Practice Facility, Pool, Tennis Courts',
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Resort Amenities',
            'Pro Shop, Restaurant, Practice Green, Club Rentals',
            'Pro Shop, Practice Green, Snack Bar',
            # Southern Maryland (Existing + New)
            'Pro Shop, Restaurant, Practice Facility, Club Rentals',
            'Pro Shop, Restaurant, Practice Green, Club Rentals',
            'Driving Range, Pro Shop, Restaurant, Practice Facility',
            'Pro Shop, Restaurant, Practice Facility, Club Rentals, Pool',
            'Pro Shop, Restaurant, Practice Facility, Tennis Courts',
            'Driving Range, Pro Shop, Restaurant, Practice Green',
            'Pro Shop, Restaurant, Practice Facility',
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Club Rentals',
            # Eastern Shore (Existing + New)
            'Driving Range, Pro Shop, Restaurant, Practice Facility, 36 Holes',
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Ocean Views',
            'Driving Range, Pro Shop, Restaurant, Practice Facility',
            'Pro Shop, Restaurant, Practice Facility, Ocean Views',
            'Pro Shop, Restaurant, Practice Facility, Club Rentals',
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Pool',
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Two Courses',
            'Pro Shop, Restaurant, Practice Facility, Bay Views, Club Rentals',
            'Pro Shop, Restaurant, Practice Facility, Ocean Views',
            'Pro Shop, Restaurant, Practice Green, Beach Access',
            # Central Maryland (Existing + New)
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Lessons',
            'Driving Range, Pro Shop, Restaurant, Practice Facility',
            'Pro Shop, Restaurant, Practice Facility, Club Rentals',
            'Driving Range, Pro Shop, Restaurant, Practice Facility',
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Lessons',
            'Driving Range, Pro Shop, Restaurant, Practice Facility',
            'Pro Shop, Restaurant, Practice Green',
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Club Rentals',
            'Pro Shop, Restaurant, Practice Facility, Club Rentals',
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Tennis'
        ],
        'lat': [
            # First 21 coordinates remain unchanged
            39.2675, 39.3219, 39.3645, 39.4139, 39.3199,
            39.3507, 39.4374, 39.3238, 39.3507, 39.6847, 39.6523, 39.4427,
            39.2123, 39.2073, 39.2031,
            39.1335, 39.0279, 39.0379,
            39.4397, 39.5094, 39.5359,
            # Western Maryland (Existing + New)
            39.6515, 39.5085, 39.4436, 39.4246,
            39.6429, 39.7223, 39.6527, 39.6234,
            # Southern Maryland (Existing + New)
            38.3835, 38.3721, 38.5847, 38.4127,
            38.2891, 38.6435, 38.7654, 38.8156,
            # Eastern Shore (Existing + New)
            38.3366, 38.3434, 38.3789, 38.3328, 38.3445,
            38.3599, 38.3789, 38.3988, 38.3456, 38.3234,
            # Central Maryland (Existing + New)
            39.1834, 39.1012, 39.3765, 39.3428, 39.3255,
            39.2544, 39.1407, 39.4123, 39.3876, 39.0234
        ],
        'lon': [
            # First 21 coordinates remain unchanged
            -76.6589, -76.6883, -76.5874, -76.5947, -76.5838,
            -76.7983, -76.6024, -76.4033, -76.7947, -76.6478, -76.8515, -76.4177,
            -76.8614, -76.8697, -76.7514,
            -76.4469, -76.5844, -76.5027,
            -76.3485, -76.1645, -76.3359,
            # Western Maryland (Existing + New)
            -77.7373, -77.5645, -77.5544, -77.4208,
            -78.7623, -78.5921, -78.9234, -78.7456,
            # Southern Maryland (Existing + New)
            -76.3872, -76.7135, -76.9547, -77.2541,
            -76.6532, -76.5834, -76.8745, -76.7234,
            # Eastern Shore (Existing + New)
            -75.1369, -75.1397, -75.1556, -75.1414, -75.1578,
            -75.1456, -75.1623, -75.1789, -75.1345, -75.1678,
            # Central Maryland (Existing + New)
            -77.1387, -76.9547, -77.1545, -76.8814, -77.3387,
            -77.2786, -77.4123, -77.3456, -77.3234, -77.2456
        ],
        'description': [
            # First 21 descriptions remain unchanged
            'Historic municipal course with scenic city views',
            'Challenging course with tree-lined fairways',
            'Well-maintained course with practice facilities',
            'Picturesque course surrounded by natural beauty',
            'Classic design with rolling terrain',
            'Championship course with challenging layout and excellent practice facilities',
            'Scenic course with well-maintained greens and full practice facility',
            'Waterfront course with beautiful Bay views',
            'Traditional layout with tree-lined fairways',
            'Upscale municipal course with dramatic elevation changes and panoramic views',
            'Family-friendly course with rolling terrain and challenging holes',
            'Scenic course along Gunpowder Falls with natural beauty',
            'Player-friendly course perfect for all skill levels',
            'Premium public course with country club atmosphere',
            'Modern design with challenging holes and great conditions',
            'Two distinct 18-hole courses offering variety for all skill levels',
            'Recently renovated municipal course with great value',
            'Challenging course with scenic water views',
            'Upscale public course with excellent amenities',
            'Military-friendly course with water features',
            'Traditional layout with friendly atmosphere',
            # Western Maryland (Existing + New)
            'Municipal gem with mountain views and challenging layout',
            'Upscale course with panoramic mountain vistas',
            'Championship course nestled in the Middletown Valley',
            'Historic Frederick course with excellent conditions',
            'Historic private course with public access and mountain scenery',
            'Resort course with stunning lake views and challenging elevation changes',
            'Traditional mountain course with scenic views and friendly atmosphere',
            'Affordable course with scenic mountain backdrop',
            # Southern Maryland (Existing + New)
            'Scenic bay views with challenging coastal winds',
            'Riverside course with beautiful Potomac River views',
            'Modern design with excellent practice facilities',
            'Premium waterfront course with yacht club amenities',
            'Classic course with water features and tree-lined fairways',
            'Family-friendly course with scenic Chesapeake Bay views',
            'Municipal course with excellent practice facilities',
            'Upscale daily fee course with championship layout',
            # Eastern Shore (Existing + New)
            'Two championship courses near Ocean City',
            'Links-style course with coastal views',
            'Challenging course with water features throughout',
            'Premium links course with stunning ocean views',
            'Traditional Eastern Shore layout with great value',
            'Robert Trent Jones designed course with beautiful water features',
            'Two distinct championship courses with varying challenges',
            'Award-winning course with spectacular bay views',
            'Ocean City favorite with scenic water views',
            'Links-style course with ocean breezes',
            # Central Maryland (Existing + New)
            'Modern design with excellent conditions year-round',
            'Upscale public course with championship layout',
            'Scenic course in Mount Airy with varied terrain',
            'Premium design with excellent practice facilities',
            'Championship course with tournament-quality conditions',
            'Challenging municipal course with scenic views',
            'Historic course with traditional layout',
            'Arthur Hills designed course with dramatic elevation changes',
            'Private course with limited public access',
            'Upscale semi-private course with excellent amenities'
        ]
    }
    return pd.DataFrame(courses)