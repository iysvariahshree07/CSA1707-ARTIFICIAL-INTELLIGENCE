% Graph edges (costs don’t matter in Best First, heuristic does)
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(e, g).

% Heuristic values (closer to goal g)
h(a, 6).
h(b, 4).
h(c, 5).
h(d, 3).
h(e, 2).
h(f, 6).
h(g, 0).

% Best First Search
bestfs(Node, Goal, Path) :- bestfs_helper([[Node]], Goal, Path).

bestfs_helper([[Goal|Rest]|_], Goal, Path) :- 
    reverse([Goal|Rest], Path).

bestfs_helper([ [Node|Rest] | Others], Goal, Path) :-
    findall([X,Node|Rest],
            (edge(Node,X), \+ member(X,[Node|Rest])),
            Children),
    evaluate_paths(Children, Scored),
    append(Others, Scored, Temp),
    sort(1, @=<, Temp, Sorted),
    pairs_values(Sorted, NewQueue),
    bestfs_helper(NewQueue, Goal, Path).

% Attach heuristic score
evaluate_paths([], []).
evaluate_paths([[Node|Rest]|T], [Score-[Node|Rest]|NT]) :-
    h(Node, Score),
    evaluate_paths(T, NT).
