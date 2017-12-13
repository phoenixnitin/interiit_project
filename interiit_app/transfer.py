from .models import Sport_Weightlifting, Sport_Athletics_Men, Sport_Athletics_Women, Sport_All_Common_Games_Men, Sport_All_Common_Games_Women
import requests
from django.db.models import Q

def iit_name(iit):
    if iit == 'IIT KHARAGPUR':
        return '5572921611255808'
    elif iit == 'IIT BOMBAY':
        return '6755040492519424'
    elif iit == 'IIT KANPUR':
        return '5530968907579392'
    elif iit == 'IIT MADRAS':
        return '5578364408561664'
    elif iit == 'IIT DELHI':
        return '5520813188972544'
    elif iit == 'IIT GUWAHATI':
        return '5559028834893824'
    elif iit == 'IIT ROORKEE':
        return '6656868814422016'
    elif iit == 'IIT BHUBANESHWAR':
        return '5500099199238144'
    elif iit == 'IIT GANDHINAGAR':
        return '5526923853692928'
    elif iit == 'IIT HYDERABAD':
        return '5560793160482816'
    elif iit == 'IIT JODHPUR':
        return '5536404457127936'
    elif iit == 'IIT PATNA':
        return '5581517283655680'
    elif iit == 'IIT ROPAR':
        return '5509293113606144'
    elif iit == 'IIT INDORE':
        return '5529877180579840'
    elif iit == 'IIT MANDI':
        return '5535127241228288'
    elif iit == 'IIT (BHU) VARANASI':
        return '5586379186634752'
    elif iit == 'IIT PALAKKAD':
        return '5552466661736448'
    elif iit == 'IIT TIRUPATI':
        return '5500935107248128'
    elif iit == 'IIT (ISM) DHANBAD':
        return '6667676294316032'
    elif iit == 'IIT BHILAI':
        return '6745193038479360'
    elif iit == 'IIT GOA':
        return '6662304363970560'
    elif iit == 'IIT JAMMU':
        return '5603755181473792'
    elif iit == 'IIT DHARWAD':
        return '6720498218041344'

def get_game(game,gender):
    if gender == 'M':
        if game == 'Badminton':
            return '5702198247817216'
        elif game == 'Basketball':
            return '5490851060908032'
        elif game == 'Cricket':
            return '5627473970593792'
        elif game == 'Football':
            return '5221684386725888'
        elif game == 'Hockey':
            return '6530529935491072'
        elif game == 'Squash':
            return '5337154045607936'
        elif game == 'Table Tennis':
            return '5598764429475840'
        elif game == 'Tennis':
            return '5258729553395712'
        elif game == 'Volleyball':
            return '6274032072654848'
    elif gender == 'F':
        if game == 'Badminton':
            return '5744307986235392'
        elif game == 'Basketball':
            return '5526756987502592'
        elif game == 'Table Tennis':
            return '6347584293568512'
        elif game == 'Tennis':
            return '6354717697376256'
        elif game == 'Volleyball':
            return '5607342552907776'

def get_athletics_events(event_name, gender):
    if gender == 'M':
        if event_name == '_100m':
            return '5642195944079360'
        elif event_name == '_200m':
            return '6228221246832640'
        elif event_name == '_400m':
            return '5751193724780544'
        elif event_name == '_800m':
            return '5698038035120128'
        elif event_name == '_1500m':
            return '6698948588732416'
        elif event_name == '_5000m':
            return '5143685532483584'
        elif event_name == 'hurdles_110m':
            return '5631679716655104'
        elif event_name == 'hurdles_400m':
            return '6042040219467776'
        elif event_name == 'high_jump':
            return '4552701891313664'
        elif event_name == 'long_jump':
            return '5377308131065856'
        elif event_name == 'triple_jump':
            return '4920270997422080'
        elif event_name == 'pole_vault':
            return '5715081639755776'
        elif event_name == 'shot_put':
            return '5188243771359232'
        elif event_name == 'discuss_throw':
            return '4820846363279360'
        elif event_name == 'javelin_throw':
            return '6269585439326208'
        elif event_name == 'hammer_throw':
            return '6314143678201856'
        elif event_name == 'relay_4x100m':
            return '6746595244638208'
        elif event_name == 'relay_4x400m':
            return '4589181732913152'
    elif gender == 'F':
        if event_name == '_100m':
            return '5675524890296320'
        elif event_name == '_200m':
            return '5526034258591744'
        elif event_name == '_400m':
            return '6721106761220096'
        elif event_name == '_800m':
            return '5153607443808256'
        elif event_name == '_1500m':
            return '5079245990658048'
        elif event_name == 'high_jump':
            return '5440495790587904'
        elif event_name == 'long_jump':
            return '6625693626531840'
        elif event_name == 'shot_put':
            return '5483220950843392'
        elif event_name == 'discuss_throw':
            return '5379167315034112'
        elif event_name == 'relay_4x100m':
            return '4607038495653888'
        elif event_name == 'relay_4x400m':
            return '5983800295161856'

def get_weightlifting_events(event_name):
    if event_name == 'upto_56kg':
        return '5504541436936192'
    elif event_name == 'upto_62kg':
        return '5571306435117056'
    elif event_name == 'upto_69kg':
        return '5523716150657024'
    elif event_name == 'upto_77kg':
        return '5588930934079488'
    elif event_name == 'above_77kg':
        return '5556632780013568'

# indiaatsports.com/events/5568384246743040/instituteid/playername/MorF/evevtid1,eventid2/createaparticipantofteam/

def create_url(iit_id, name, gender, event):
    url = 'http://indiaatsports.com/events/5568384246743040/'+iit_id+'/'+name+'/'+gender+'/'+event+'/createaparticipantofteam/'
    return url

def read_weight():
    # list = ['upto_56kg', 'upto_62kg', 'upto_69kg', 'upto_77kg', 'above_77kg']
    # list = ['_100m', '_200m', '_400m', '_800m', '_1500m', 'high_jump', 'long_jump', 'shot_put', 'discuss_throw', 'relay_4x100m', 'relay_4x400m']
    queryset = Sport_All_Common_Games_Men.objects.values()
    for obj in queryset:
        if obj['id'] >= 0:
            stu_Name = obj['student_name']
            iit_ID = iit_name(obj['iit_name'])
            gender = 'M'
            event_ID = get_game(obj['sport_name'],'M')
            # for item in list:
            #     if obj[item] != 'NO':
            #         event_ID = event_ID + get_athletics_events(item,'F') + ','
            # event_ID = event_ID[0:-1]
            print(stu_Name.title(), iit_ID, gender, event_ID)
            r = requests.get(create_url(iit_id=iit_ID, name=stu_Name.title(), gender=gender, event=event_ID))
            # return 0