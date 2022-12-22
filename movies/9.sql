SELECT name FROM people JOIN stars on people.id = stars.person_id WHERE movie_id = (SELECT id FROM movies WHERE year = 2004) ORDER BY birth;
