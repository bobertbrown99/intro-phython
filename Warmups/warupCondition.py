month = int(input)("what month is it?)")
seasons = [1,2,3,4,5,6,7,8,9,10,11,12]

# we need to consider 1 for winter.
if month > seasons[10] and month =< seasons[12]:
    print("the season is winter.")
elif month > seasons[2]:
    print("the season is spring")
elif month > seasons[5]
    print("the season is summer")
elif month > seasons[8]:
    print('the season is Fall')
else:
    print('something went wrong.')