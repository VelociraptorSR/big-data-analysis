"""
Movie Night Playlist
Scenario: You are organizing a movie marathon. You start with a playlist: 
["Inception", "The Matrix", "Interstellar"]. Prompt the user to enter the name of a movie they want to add.

If the movie is already in the list, print "Already added!" and do not insert it.
If it is not in the list, append it to the end of the list. Finally, sort the movie list alphabetically and 
print the updated playlist.

Sample Input: "Interstellar"
Sample Output:
Already added!
Alphabetical Playlist: ['Inception', 'Interstellar', 'The Matrix']
Sample Input: "Avatar"
Sample Output:
Added Avatar!
Alphabetical Playlist: ['Avatar', 'Inception', 'Interstellar', 'The Matrix']
"""
movie = input("Enter a movie ")
playlist = ['Inception', 'Interstellar', 'The Matrix']
if movie in playlist:
    print("Already added!")
    print(f"Alphabetical Playlist: {sorted(playlist)}")
else:
    print(f"Added {movie}!")
    playlist.append(movie.title())
    new_playlist = sorted(playlist)
    print(f"Alphabetical Playlist: {new_playlist}")
    