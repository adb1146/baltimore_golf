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
            # Western Maryland
            'Black Rock Golf Course',
            'Musket Ridge Golf Club',
            'Maryland National Golf Club',
            'Clustered Spires Golf Club',
            # Southern Maryland
            'Chesapeake Hills Golf Course',
            'Wicomico Shores Golf Course',
            'White Plains Golf Course',
            'Swan Point Yacht & Country Club',
            # Eastern Shore
            'Ocean City Golf Club',
            'Eagle\'s Landing Golf Course',
            'River Run Golf Club',
            'Rum Pointe Seaside Golf Links',
            'Bay Club Golf Course',
            # Central Maryland
            'Blue Mash Golf Course',
            'Hampshire Greens Golf Course',
            'Rattlewood Golf Course',
            'Waverly Woods Golf Club',
            'Worthington Manor Golf Club'
        ],
        'address': [
            # Baltimore City
            '2100 Washington Blvd, Baltimore, MD 21230',
            '2900 Hillsdale Rd, Baltimore, MD 21207',
            '6001 Hillen Road, Baltimore, MD 21239',
            '2101 Dulaney Valley Rd, Lutherville-Timonium, MD 21093',
            '2701 St Lo Dr, Baltimore, MD 21213',
            # Baltimore County
            '2701 Ridge Rd, Windsor Mill, MD 21244',
            '1 Cardigan Rd, Timonium, MD 21093',
            '1935 Back River Neck Rd, Essex, MD 21221',
            '2309 Ridge Rd, Windsor Mill, MD 21244',
            '2115 White Hall Rd, White Hall, MD 21161',
            '2290 Golf View Ln, Hampstead, MD 21074',
            '2801 Jerusalem Rd, Kingsville, MD 21087',
            # Howard County
            '5100 Columbia Rd, Columbia, MD 21044',
            '11130 Willow Bottom Dr, Columbia, MD 21044',
            '6100 Marshalee Drive, Elkridge, MD 21075',
            # Anne Arundel County
            '9010 Fort Smallwood Rd, Pasadena, MD 21122',
            '1576 Generals Hwy, Crownsville, MD 21032',
            '545 Bay Hills Dr, Arnold, MD 21012',
            # Harford County
            '1827 Mountain Rd, Joppa, MD 21085',
            '100 Walter Ward Blvd, Aberdeen, MD 21001',
            '800 S Main St, Bel Air, MD 21014',
            # Western Maryland
            '12287 Greencastle Pike, Hagerstown, MD 21740',
            '3880 Arabis Dr, Myersville, MD 21773',
            '8836 Hollow Rd, Middletown, MD 21769',
            '3225 Clustered Spires Dr, Frederick, MD 21704',
            # Southern Maryland
            '11352 HG Trueman Rd, Lusby, MD 20657',
            '35794 Aviation Yacht Club Rd, Mechanicsville, MD 20659',
            '1015 St Charles Pkwy, White Plains, MD 20695',
            '11550 Swan Point Blvd, Issue, MD 20645',
            # Eastern Shore
            '11401 Country Club Dr, Berlin, MD 21811',
            '12367 Eagles Nest Rd, Berlin, MD 21811',
            '11605 Masters Ln, Berlin, MD 21811',
            '7000 Rum Pointe Ln, Berlin, MD 21811',
            '9122 Libertytown Rd, Berlin, MD 21811',
            # Central Maryland
            '5821 Olney Laytonsville Rd, Laytonsville, MD 20882',
            '2300 York Rd, Silver Spring, MD 20904',
            '1600 Rattlewood Dr, Mt Airy, MD 21771',
            '2100 Warwick Way, Marriottsville, MD 21104',
            '8329 Fingerboard Rd, Urbana, MD 21704'
        ],
        'holes': [
            # Existing courses (1-21)
            18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 36, 18, 18, 18, 18, 18,
            # New courses (22-39)
            18, 18, 18, 18, 18, 18, 18, 18, 36, 18, 18, 18, 18, 18, 18, 18, 18, 18
        ],
        'par': [
            # Existing courses (1-21)
            70, 71, 71, 72, 70, 72, 71, 71, 70, 72, 71, 70, 70, 72, 72, 72, 71, 71, 72, 71, 70,
            # New courses (22-39)
            72, 72, 71, 72, 72, 71, 72, 72, 72, 72, 72, 72, 72, 71, 72, 72, 72, 72
        ],
        'weekday_price': [
            # Existing courses (1-21)
            25, 28, 32, 35, 26, 45, 42, 38, 40, 48, 42, 35, 42, 55, 48, 52, 45, 48, 52, 38, 42,
            # New courses (22-39)
            45, 65, 59, 45, 42, 38, 45, 75, 89, 69, 65, 89, 49, 65, 55, 48, 62, 69
        ],
        'weekend_price': [
            # Existing courses (1-21)
            32, 35, 40, 45, 33, 55, 52, 48, 50, 58, 52, 45, 52, 65, 58, 62, 55, 58, 62, 48, 52,
            # New courses (22-39)
            55, 85, 79, 55, 52, 48, 55, 95, 109, 89, 85, 109, 59, 85, 75, 58, 82, 89
        ],
        'phone': [
            # Baltimore City
            '410-685-8344', '410-448-4653', '410-254-5100', '410-252-1408', '410-243-3200',
            # Baltimore County
            '410-887-1349', '410-887-7735', '410-887-0215', '410-887-1349', '410-887-1945',
            '410-239-7114', '410-592-8877',
            # Howard County
            '410-730-1112', '410-730-5980', '410-313-4653',
            # Anne Arundel County
            '410-255-7764', '410-571-0973', '410-974-0669',
            # Harford County
            '410-836-9600', '410-272-7500', '410-879-1500',
            # Western Maryland
            '240-313-2816', '301-293-9930', '301-371-0000', '301-600-1295',
            # Southern Maryland
            '410-326-4653', '301-769-2500', '301-645-1300', '301-259-0047',
            # Eastern Shore
            '410-641-1779', '410-213-7277', '410-641-7200', '410-213-2325', '410-641-4081',
            # Central Maryland
            '301-948-1075', '301-476-7999', '301-831-7389', '410-442-2250', '301-874-5400'
        ],
        'amenities': [
            # Baltimore City
            'Driving Range, Pro Shop, Restaurant',
            'Pro Shop, Putting Green, Restaurant',
            'Driving Range, Pro Shop, Lessons',
            'Driving Range, Pro Shop, Restaurant, Lessons',
            'Pro Shop, Putting Green',
            # Baltimore County
            'Driving Range, Pro Shop, Restaurant, Practice Facility',
            'Driving Range, Pro Shop, Restaurant, Lessons',
            'Pro Shop, Restaurant, Practice Green',
            'Driving Range, Pro Shop, Restaurant',
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Lessons',
            'Pro Shop, Restaurant, Practice Facility',
            'Pro Shop, Practice Green, Snack Bar',
            # Howard County
            'Pro Shop, Practice Facility, Restaurant',
            'Driving Range, Pro Shop, Restaurant, Lessons',
            'Driving Range, Pro Shop, Restaurant, Practice Facility',
            # Anne Arundel County
            'Driving Range, Pro Shop, Restaurant, Practice Facility, 36 Holes',
            'Pro Shop, Practice Facility, Restaurant',
            'Pro Shop, Restaurant, Practice Green',
            # Harford County
            'Driving Range, Pro Shop, Restaurant, Practice Facility',
            'Pro Shop, Restaurant, Practice Green',
            'Pro Shop, Restaurant, Practice Facility',
            # Western Maryland
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Lessons',
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Club Rentals',
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Lessons',
            'Pro Shop, Restaurant, Practice Facility, Club Rentals',
            # Southern Maryland
            'Pro Shop, Restaurant, Practice Facility, Club Rentals',
            'Pro Shop, Restaurant, Practice Green, Club Rentals',
            'Driving Range, Pro Shop, Restaurant, Practice Facility',
            'Pro Shop, Restaurant, Practice Facility, Club Rentals, Pool',
            # Eastern Shore
            'Driving Range, Pro Shop, Restaurant, Practice Facility, 36 Holes',
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Ocean Views',
            'Driving Range, Pro Shop, Restaurant, Practice Facility',
            'Pro Shop, Restaurant, Practice Facility, Ocean Views',
            'Pro Shop, Restaurant, Practice Facility, Club Rentals',
            # Central Maryland
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Lessons',
            'Driving Range, Pro Shop, Restaurant, Practice Facility',
            'Pro Shop, Restaurant, Practice Facility, Club Rentals',
            'Driving Range, Pro Shop, Restaurant, Practice Facility',
            'Driving Range, Pro Shop, Restaurant, Practice Facility, Lessons'
        ],
        'lat': [
            # Baltimore City
            39.2675, 39.3219, 39.3645, 39.4139, 39.3199,
            # Baltimore County
            39.3507, 39.4374, 39.3238, 39.3507, 39.6847, 39.6523, 39.4427,
            # Howard County
            39.2123, 39.2073, 39.2031,
            # Anne Arundel County
            39.1335, 39.0279, 39.0379,
            # Harford County
            39.4397, 39.5094, 39.5359,
            # Western Maryland
            39.6515, 39.5085, 39.4436, 39.4246,
            # Southern Maryland
            38.3835, 38.3721, 38.5847, 38.4127,
            # Eastern Shore
            38.3366, 38.3434, 38.3789, 38.3328, 38.3445,
            # Central Maryland
            39.1834, 39.1012, 39.3765, 39.3428, 39.3255
        ],
        'lon': [
            # Baltimore City
            -76.6589, -76.6883, -76.5874, -76.5947, -76.5838,
            # Baltimore County
            -76.7983, -76.6024, -76.4033, -76.7947, -76.6478, -76.8515, -76.4177,
            # Howard County
            -76.8614, -76.8697, -76.7514,
            # Anne Arundel County
            -76.4469, -76.5844, -76.5027,
            # Harford County
            -76.3485, -76.1645, -76.3359,
            # Western Maryland
            -77.7373, -77.5645, -77.5544, -77.4208,
            # Southern Maryland
            -76.3872, -76.7135, -76.9547, -77.2541,
            # Eastern Shore
            -75.1369, -75.1397, -75.1556, -75.1414, -75.1578,
            # Central Maryland
            -77.1387, -76.9547, -77.1545, -76.8814, -77.3387
        ],
        'description': [
            # Baltimore City
            'Historic municipal course with scenic city views',
            'Challenging course with tree-lined fairways',
            'Well-maintained course with practice facilities',
            'Picturesque course surrounded by natural beauty',
            'Classic design with rolling terrain',
            # Baltimore County
            'Championship course with challenging layout and excellent practice facilities',
            'Scenic course with well-maintained greens and full practice facility',
            'Waterfront course with beautiful Bay views',
            'Traditional layout with tree-lined fairways',
            'Upscale municipal course with dramatic elevation changes and panoramic views',
            'Family-friendly course with rolling terrain and challenging holes',
            'Scenic course along Gunpowder Falls with natural beauty',
            # Howard County
            'Player-friendly course perfect for all skill levels',
            'Premium public course with country club atmosphere',
            'Modern design with challenging holes and great conditions',
            # Anne Arundel County
            'Two distinct 18-hole courses offering variety for all skill levels',
            'Recently renovated municipal course with great value',
            'Challenging course with scenic water views',
            # Harford County
            'Upscale public course with excellent amenities',
            'Military-friendly course with water features',
            'Traditional layout with friendly atmosphere',
            # Western Maryland
            'Municipal gem with mountain views and challenging layout',
            'Upscale course with panoramic mountain vistas',
            'Championship course nestled in the Middletown Valley',
            'Historic Frederick course with excellent conditions',
            # Southern Maryland
            'Scenic bay views with challenging coastal winds',
            'Riverside course with beautiful Potomac River views',
            'Modern design with excellent practice facilities',
            'Premium waterfront course with yacht club amenities',
            # Eastern Shore
            'Two championship courses near Ocean City',
            'Links-style course with coastal views',
            'Challenging course with water features throughout',
            'Premium links course with stunning ocean views',
            'Traditional Eastern Shore layout with great value',
            # Central Maryland
            'Modern design with excellent conditions year-round',
            'Upscale public course with championship layout',
            'Scenic course in Mount Airy with varied terrain',
            'Premium design with excellent practice facilities',
            'Championship course with tournament-quality conditions'
        ]
    }
    return pd.DataFrame(courses)
