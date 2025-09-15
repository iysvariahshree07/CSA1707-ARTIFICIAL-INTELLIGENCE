% Simple pattern matching
match([H|T], H, T).      % Match head
match([_|T], X, R) :-    % Skip until found
    match(T, X, R).
