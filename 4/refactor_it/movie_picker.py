if __name__ == '__main__':
    print('Tasks 18. Movie picker 2. Part 1')

    GENRES = {
        'comedy': ['Meet The Parents', 'Anger Management'],
        'adventures': ['Mummy'],
        'romantic': ['Vanilla Sky', 'Meet Joe Black'],
        'drama': ['Meet Joe Black'],
        'thriller': ['Vanilla Sky'],
        'action': ['Mission Impossible']
    }

    CAST = {
        'Meet The Parents': ['Robert De Niro', 'Ben Stiller'],
        'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
        'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
        'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
        'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
        'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
    }


    def movies_by_actors(cast):
        actors = {}
        for movie, actor_list in cast.items():
            for actor in actor_list:
                if actor not in actors:
                    actors[actor] = []
                actors[actor].append(movie)
        return actors


    def search(source, source_name):
        while True:
            print(f'Available {source_name}s: {list(source.keys())}')
            search_input = input(f'Enter {source_name}: ').lower()

            if search_input in source:
                items = source[search_input]
                print(f'Available {source_name} items: {items}')

                while True:
                    selected_item = input(f'Enter {source_name} item: ').title()

                    if selected_item in items:
                        print(f'{source_name.title()} to watch: {selected_item}. {source_name.title()}: {search_input}')
                        return
                    else:
                        print(f'Invalid {source_name} item. Try again.')
            else:
                print(f'Invalid {source_name}. Try again.')


    ACTORS = movies_by_actors(CAST)

    genre_check = input('Search by Genre(y/n): ').lower()
    if genre_check == 'y':
        search(GENRES, 'genre')

    elif genre_check == 'n':
        actor_check = input('Search by Actor(y/n): ')

        if actor_check == 'y':
            search(ACTORS, 'actor')

    else:
        exit()