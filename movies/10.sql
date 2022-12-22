SELECT name FROM people JOIN directors ON people.id = directors.person_id WHERE movie_id = (SELECT movie_id FROM ratings WHERE rating > 9.0 OR rating = 9.0);
