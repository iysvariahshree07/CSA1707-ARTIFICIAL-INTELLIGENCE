% student_teacher.pl
% student(Name, DOB, Subject)
% teacher(Name, Subject)

student(john, '01-01-2000', math).
student(anna, '12-03-2001', physics).
student(raj, '05-07-2000', math).

teacher(smith, math).
teacher(jones, physics).

% rule: find teacher of a student
teacher_of(Student, Teacher) :-
    student(Student, _, Subject),
    teacher(Teacher, Subject).
