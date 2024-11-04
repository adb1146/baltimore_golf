import pandas as pd

# Golf courses data for Baltimore area and surrounding counties
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
            'Winter\'s Run Golf Club'
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
            '800 S Main St, Bel Air, MD 21014'
        ],
        'holes': [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 36, 18, 18, 18, 18, 18],
        'par': [70, 71, 71, 72, 70, 72, 71, 71, 70, 70, 72, 72, 72, 71, 71, 72, 71, 70],
        'weekday_price': [25, 28, 32, 35, 26, 45, 42, 38, 40, 42, 55, 48, 52, 45, 48, 52, 38, 42],
        'weekend_price': [32, 35, 40, 45, 33, 55, 52, 48, 50, 52, 65, 58, 62, 55, 58, 62, 48, 52],
        'phone': [
            # Baltimore City
            '410-685-8344',
            '410-448-4653',
            '410-254-5100',
            '410-252-1408',
            '410-243-3200',
            # Baltimore County
            '410-887-1349',
            '410-887-7735',
            '410-887-0215',
            '410-887-1349',
            # Howard County
            '410-730-1112',
            '410-730-5980',
            '410-313-4653',
            # Anne Arundel County
            '410-255-7764',
            '410-571-0973',
            '410-974-0669',
            # Harford County
            '410-836-9600',
            '410-272-7500',
            '410-879-1500'
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
            'Pro Shop, Restaurant, Practice Facility'
        ],
        'lat': [
            # Baltimore City
            39.2675, 39.3219, 39.3645, 39.4139, 39.3199,
            # Baltimore County
            39.3507, 39.4374, 39.3238, 39.3507,
            # Howard County
            39.2123, 39.2073, 39.2031,
            # Anne Arundel County
            39.1335, 39.0279, 39.0379,
            # Harford County
            39.4397, 39.5094, 39.5359
        ],
        'lon': [
            # Baltimore City
            -76.6589, -76.6883, -76.5874, -76.5947, -76.5838,
            # Baltimore County
            -76.7983, -76.6024, -76.4033, -76.7947,
            # Howard County
            -76.8614, -76.8697, -76.7514,
            # Anne Arundel County
            -76.4469, -76.5844, -76.5027,
            # Harford County
            -76.3485, -76.1645, -76.3359
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
            'Traditional layout with friendly atmosphere'
        ]
    }
    return pd.DataFrame(courses)
