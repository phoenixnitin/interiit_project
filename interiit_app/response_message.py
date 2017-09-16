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

def response(dict, category):
    if category == 'men':
        mylist = listmen
        recepient_name = dict['student_name']
    elif category == 'women':
        mylist = listwomen
        recepient_name = dict['student_name']
    elif category == 'facultyandstaff':
        mylist = liststaff
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


    message ='''Dear {}, 
    You have successfully registered for InterIIT Sports Meet 2017.

Details:
{}

In case of any error reply to this mail.
'''.format(recepient_name,details)
    return message