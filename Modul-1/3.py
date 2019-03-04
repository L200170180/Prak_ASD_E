#3a
def jumlahVokal (String):
    vo = 0
    a = "aiueoAIUEO"
    for car in String.lower ():
        if car  in a :
            vo +=1
    vokal = len(String)
    return (vokal, vo)
#3b
def jumlahKonsonan (String):
    vo = 0
    a = "aiueoAIUEO"
    for car in String.lower ():
        if car not in a :
            vo +=1
    vokal = len(String)
    return (vokal, vo)
