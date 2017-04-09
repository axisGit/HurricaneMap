from bs4 import BeautifulSoup
import pandas as pd
import re

data = pd.read_csv('data.csv', sep = ' ')

i = 0

for i in range(1, 48):
    if i < 10:
        soup = BeautifulSoup(open("data/AL142016_00" + str(i) + 'adv_TRACK.kml'), "html.parser")
    else:
        soup = BeautifulSoup(open("data/AL142016_0" + str(i) + 'adv_TRACK.kml'), "html.parser")

    des = soup.find_all('description')[2]
    des_str =  des.contents[1].string
    m = re.search('Maximum Wind: .* knots', des_str)
    speed = m.group(0).split()[2]

    des = soup.find_all('coordinates')[1]
    coor =  des.contents[0].string.strip().split(',')[:-1]

    data.loc[i] = [coor[0], coor[1], speed]
    i += 1

    print coor[0], ',', coor[1], ',', 0

print data
#data.to_csv('data.csv')


