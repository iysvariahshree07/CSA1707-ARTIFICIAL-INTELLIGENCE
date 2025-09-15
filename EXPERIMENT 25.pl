% Facts
parent(john, mary).
parent(john, david).
parent(susan, mary).
parent(susan, david).
parent(mary, alice).
parent(mary, bob).
parent(david, carl).

male(john).
male(david).
male(bob).
male(carl).
female(susan).
female(mary).
female(alice).

% Rules
father(X,Y) :- parent(X,Y), male(X).
mother(X,Y) :- parent(X,Y), female(X).
grandparent(X,Y) :- parent(X,Z), parent(Z,Y).
sibling(X,Y) :- parent(Z,X), parent(Z,Y), X \= Y.
