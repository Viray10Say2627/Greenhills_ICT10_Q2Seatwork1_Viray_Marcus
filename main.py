from pyscript import display, document

nicknames = {'France': "L'Hexagone",'Italy': 'The Boot','Spain': 'La Piel de Toro','Portugal': 'Land of Explorers','Switzerland': 'Playground of Europe','Austria': 'Land of Music','Belgium': 'Cockpit of Europe','Netherlands': 'The Low Countries','Greece': 'Cradle of Western Civilization'
}

def search(e):
    country = document.getElementById('country-input').value.strip().title()
    document.getElementById('div1').innerHTML = ''

    if country in nicknames:
        display(nicknames[country], target='div1')
    else:
        display("Country not found", target='div1')



# homogeneous_list = [5, 10, 15, 18]
# heterogeneous_list = [-1, 0.04, 'bye world!', False]
# empty_list = []
# sample_list = [1, [2, 3, 4]]

# display(homogeneous_list, target='div1')
# display(heterogeneous_list, target='div1')
# display(empty_list, target='div1')
# display(sample_list, target='div1')

# ranks = ['iron', 'bronze', 'silver', 'gold', 'platinum', 'diamond', 'ascendant', 'immortal', 'radiant']

# display(ranks[0], target='div1')
# display(ranks[1], target='div1')


# sample_tuple = (1, 2, 3)
# converted_list = list(sample_tuple) # converting to list

# display(converted_list, target='div1')

# class_adviser = 'Marc Lyndon Balmas Cortez'
# display(list(class_adviser), target='div1')

# weapons = ['AK-47', 'M4A1', 'Tongue']
# weapons2 = ['sword', 'molotov', 'deagle', 'apache helicopter']
# final_weapons = weapons + weapons2

# display(final_weapons, target='div1')

# NBA_players = ['Alpren Sengun', 'Tari Eason', 'Amen Thompson', 'Kevin Durant', 'Fred VanVleet']
# NBA_players.append('Jabari Smith Jr.') # adding an item to the end
# display(NBA_players, target='div1')
# NBA_players.insert(3, 'Kevin Durant')

# desserts = ['brownies', 'ice cream', 'banana bread', 'lava cake', 'cookies']
# del desserts[2]
# desserts.remove('cookies')
# desserts.pop(1)
# desserts.clear()
# display(desserts, target='div1')


# DC_characters = ['Batman', 'Dr. Fade', 'King Shark', 'Green Arrow', 'Flash']
# display('Flash' in DC_characters, target='div1')
# DC_characters.append('Joker')
# display(len(DC_characters), target='div1')

# sample_list2 = [1, 0, 1, 0, 1, 0, 1, 0 ,1, 0, 1, 0, 1, 0]
# display(sample_list2.count(1), target='div1')


# cars = ['Nissan', 'Toyota', 'Mazda', 'Dodge']
# duplicate_cars = cars.copy()

# display(duplicate_cars, target='div1')
# display(cars, target='div1')

# Marvel_heros = ['Nova', 'Ironman', 'Daredevil', 'Cyclops', 'Spider-man', 'Gambit', 'Deadpool']
# Marvel_heros.sort(reverse=True)
# display(Marvel_heros, target='div1')

# clubs = ['Glee', 'Science', 'Math', 'Monarch', 'Social Studies', 'Writer\'s guild', 'ICT', 'COCC', 'Varsity', 'CommArts', 'Marching Band', 'Rainbow Catering', 'Art']
# clubs.sort()
# display(clubs, target='div1')


# Music_artist = ['Dominic Fike', 'CAS', 'Kendrick Lamar', 'J. Cole']
# display(sorted(Music_artist), target='div1')
# display(Music_artist, target='div1')