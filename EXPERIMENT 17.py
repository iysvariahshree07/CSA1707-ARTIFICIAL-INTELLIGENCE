% sum_to_n.pl
% sum_to_n(N, Sum) means Sum is the sum of numbers from 1 to N

sum_to_n(1, 1).
sum_to_n(N, Sum) :-
    N > 1,
    N1 is N - 1,
    sum_to_n(N1, Partial),
    Sum is Partial + N.
