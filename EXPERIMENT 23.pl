% Monkey can get banana if it climbs on box and grasps.
canget(state(_,_,onbox,no)) :- !, write('Monkey grasps banana'), nl.
canget(state(atdoor, middle, onfloor, no)) :- 
    write('Monkey walks, pushes box, climbs...'), nl,
    canget(state(middle,middle,onbox,no)).
