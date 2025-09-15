% planetdb.pl
% planet(Name, Distance_from_Sun, Moons)

planet(mercury, 57.9, 0).
planet(venus, 108.2, 0).
planet(earth, 149.6, 1).
planet(mars, 227.9, 2).
planet(jupiter, 778.3, 79).
planet(saturn, 1427.0, 82).
planet(uranus, 2871.0, 27).
planet(neptune, 4497.1, 14).

% Rule to check if a planet has moons
has_moons(Name) :-
    planet(Name, _, Moons),
    Moons > 0.
