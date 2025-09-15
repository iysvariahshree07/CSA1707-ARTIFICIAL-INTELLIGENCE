% Symptoms facts (example patient)
symptom(john, fever).
symptom(john, cough).
symptom(john, headache).

symptom(mary, chest_pain).
symptom(mary, breathlessness).

% Rules (forward-chaining style: if symptoms match, infer disease)
disease(Patient, flu) :-
    symptom(Patient, fever),
    symptom(Patient, cough),
    symptom(Patient, headache).

disease(Patient, heart_problem) :-
    symptom(Patient, chest_pain),
    symptom(Patient, breathlessness).
