strawberries=20
is_weekend= False
#is_weekday= True


#if is_weekend==True and strawberries>39:
 #       print('Fun!')
#elif is_weekend==False:
#        print('Not Fun!')
#if is_weekday==True and strawberries>39 and strawberries<61:
#        print('Fun!')
#elif is_weekday==False:
#        print('Not Fun!')

if is_weekend:
    if strawberries>39:
        print('Fun!')
    else:
        print('Not Fun!')
else:
    if strawberries>39 and strawberries<61:
        print('Fun!')
    else:
        print('Not Fun!')
