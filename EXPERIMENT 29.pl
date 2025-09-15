% --- Base Symptoms (Facts) ---
symptom(john, fever).
symptom(john, cough).
symptom(john, headache).
symptom(mary, chest_pain).
symptom(mary, breathlessness).

% --- Forward Chaining Rules ---
derive :-
    symptom(P, fever),
    symptom(P, cough),
    symptom(P, headache),
    \+ disease(P, flu),          % not already derived
    assertz(disease(P, flu)),
    fail.

derive :-
    symptom(P, chest_pain),
    symptom(P, breathlessness),
    \+ disease(P, heart_problem),
    assertz(disease(P, heart_problem)),
    fail.

derive.  % stop when no more rules apply

% --- Query diseases after forward chaining ---
diagnose(P) :-
    derive,                      % perform forward chaining
    disease(P, D),
    format('~w is diagnosed with ~w.~n', [P, D]),
    fail.
diagnose(_).
