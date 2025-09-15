can_fly(sparrow).
can_fly(pigeon).
can_fly(eagle).

cannot_fly(penguin).
cannot_fly(ostrich).

bird(X) :- can_fly(X), write(X), write(' can fly'), nl.
bird(X) :- cannot_fly(X), write(X), write(' cannot fly'), nl.
