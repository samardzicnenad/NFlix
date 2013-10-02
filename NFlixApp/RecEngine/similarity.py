class Sim():
    ''' User similarity calculator.

    Below are methods that any implementation must provide. '''

    def sim(self, ratings_a, ratings_b):
        raise NotImplementedError

class Euclidian(Sim):
    ''' An implementation of the Euclidian distance calculator between two users.

    The distance is calculated in a space of all movies seen by both person. '''

    def sim(self, ratings_a, ratings_b):
        ''' Compute the similarity between two users.
        
        Parameters
          ratings_a : an a's dictionary of {movie name : rating}
          ratings_b : a b's dictionary of {movie name : rating}

        Returns
          A number [0-1], with 0 indicating no similarity, and 1 indicating maximum similarity. '''

        #add up the squares of all the differences
        differences = []
        for movie, rating_a in ratings_a.items():
            if movie in ratings_b:
                rating_b = ratings_b[movie]
                differences.append(pow(rating_a - rating_b, 2))
        #no movies in common -> 0
        return 1/(1+float(sum(differences))) if (len(differences)!=0) else 0
