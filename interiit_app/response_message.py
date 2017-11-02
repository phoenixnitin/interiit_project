listmen = ('iit_name', 'student_name', 'blood_group', 'mobile_no', 'email', 'mode_of_transportation',
              'transport_name', 'arrival_date', 'arrival_time', 'departure_date', 'departure_time', 'food',
              'water_polo', 'free_50m', 'free_100m', 'free_200m', 'free_400m', 'free_1500m', 'back_50m', 'back_100m',
              'back_200m', 'breast_50m', 'breast_100m', 'breast_200m', 'b_fly_50m', 'b_fly_100m', 'i_m_200m',
              'free_relay_4x100m', 'medley_relay_4x100m',)
listwomen = ('iit_name', 'student_name', 'blood_group', 'mobile_no', 'email', 'mode_of_transportation',
              'transport_name', 'arrival_date', 'arrival_time', 'departure_date', 'departure_time', 'food',
              'freestyle_50m', 'freestyle_100m', 'breast_stroke_50m', 'back_stroke_50m', 'butterfly_50m',
              'freestyle_relay_4x50m',)
liststaff = ('iit_name', 'staff_name', 'blood_group', 'mobile_no', 'email', 'mode_of_transportation',
              'transport_name', 'arrival_date', 'arrival_time', 'departure_date', 'departure_time', 'food',
              'designation',)

list_all_staff = ('iit_name', 'staff_name', 'blood_group', 'mobile_no', 'email', 'food', 'designation',)
list_athletics_men = ('iit_name', 'student_name', 'blood_group', 'mobile_no', 'email', 'food',
              '_100m', '_200m', '_400m', '_800m', '_1500m', '_5000m', 'hurdles_110m', 'hurdles_400m','high_jump',
              'long_jump', 'triple_jump', 'pole_vault', 'shot_put', 'discuss_throw', 'javelin_throw', 'hammer_throw',
              'relay_4x100m', 'relay_4x400m',)
list_athletics_women = ('iit_name', 'student_name', 'blood_group', 'mobile_no', 'email', 'food',
              '_100m', '_200m', '_400m', '_800m', '_1500m', 'high_jump', 'long_jump', 'shot_put', 'discuss_throw',
              'relay_4x100m', 'relay_4x400m',)
list_weightlifting_men = ('iit_name', 'student_name', 'blood_group', 'mobile_no', 'email', 'food', 'upto_56kg', 'upto_62kg', 'upto_69kg',
              'upto_77kg','above_77kg',)
list_all_other_games = ('iit_name', 'student_name', 'blood_group', 'mobile_no', 'email', 'food',)

def response(dict, category, sport_name):
    if category == 'men':
        if sport_name == 'athletics':
            mylist = list_athletics_men
        elif sport_name == 'weightlifting':
            mylist = list_weightlifting_men
        else:
            mylist = list_all_other_games
        recepient_name = dict['student_name']
    elif category == 'women':
        if sport_name == 'athletics':
            mylist = list_athletics_women
        else:
            mylist = list_all_other_games
        recepient_name = dict['student_name']
    elif category == 'facultyandstaff':
        mylist = list_all_staff
        recepient_name = dict['staff_name']
    n = len(mylist)

    details = ""
    #print(dict)
    for i in range(0, n):
        for field in mylist:
            if mylist[i] == field:
                if field == 'student_name' or field == 'staff_name':
                    details = details +"name : " + dict[field] + "\n"
                elif field == 'iit_name':
                    details = details + dict[field] + "\n"
                else:
                    details = details + field + " : " + dict[field] + "\n"

    if sport_name.find("_") > 0:
        sport_name = sport_name.replace("_", " ")
    message ='''Dear {}, 
    You have successfully registered for InterIIT Sports Meet 2017.

You have registered for {}.

Details:
{}

In case of any error reply to this mail. Your image is stored in our database.
'''.format(recepient_name, sport_name, details)
    return message