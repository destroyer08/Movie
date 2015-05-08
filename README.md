Portable Movie Recommondation is a program to give apropriate movie suggestion for user on the basis of his wathed movies rating 
and IMDB ratings.

How does it work:
1. User supplies his watched movies with his ratings.
2. User also supplies his unwatched movies.
2. Program calculates deviation between his unwatched movies IMDB rating and his watched movies ratings. (Program will 
automatically retrive IMDB ratings of his watched and unwatched movies with help of API)
3. Once I have calculated deviations we use slope one algorithm to predict his ratings for unwatched movies.
4. It also calculates weight for each of your movie's category(action, comedy etc.) with help of Cosine simillarity index.
5. Sums up both predected rating and weight of category and gives you Reccomendation Score between 0 and 1.(score near 1 has higher priority)

Works to do:
1. Give some user interface.
