import pandas as pd

# Mock data for Baltimore area golf courses
def load_golf_courses():
    courses = {
        'name': [
            'Carroll Park Golf Course',
            'Forest Park Golf Course',
            'Mount Pleasant Golf Course',
            'Pine Ridge Golf Course',
            'Clifton Park Golf Course'
        ],
        'address': [
            '2100 Washington Blvd, Baltimore, MD 21230',
            '2900 Hillsdale Rd, Baltimore, MD 21207',
            '6001 Hillen Road, Baltimore, MD 21239',
            '2101 Dulaney Valley Rd, Lutherville-Timonium, MD 21093',
            '2701 St Lo Dr, Baltimore, MD 21213'
        ],
        'holes': [18, 18, 18, 18, 18],
        'par': [70, 71, 71, 72, 70],
        'weekday_price': [25, 28, 32, 35, 26],
        'weekend_price': [32, 35, 40, 45, 33],
        'phone': [
            '410-685-8344',
            '410-448-4653',
            '410-254-5100',
            '410-252-1408',
            '410-243-3200'
        ],
        'amenities': [
            'Driving Range, Pro Shop, Restaurant',
            'Pro Shop, Putting Green, Restaurant',
            'Driving Range, Pro Shop, Lessons',
            'Driving Range, Pro Shop, Restaurant, Lessons',
            'Pro Shop, Putting Green'
        ],
        'lat': [39.2675, 39.3219, 39.3645, 39.4139, 39.3199],
        'lon': [-76.6589, -76.6883, -76.5874, -76.5947, -76.5838],
        'description': [
            'Historic municipal course with scenic city views',
            'Challenging course with tree-lined fairways',
            'Well-maintained course with practice facilities',
            'Picturesque course surrounded by natural beauty',
            'Classic design with rolling terrain'
        ]
    }
    return pd.DataFrame(courses)
