% Diseases and required symptoms
has_symptom(fever).
has_symptom(cough).
has_symptom(headache).
has_symptom(chest_pain).
has_symptom(breathlessness).

disease(flu) :-
    has_symptom(fever),
    has_symptom(cough),
    has_symptom(headache).

disease(heart_problem) :-
    has_symptom(chest_pain),
    has_symptom(breathlessness).
