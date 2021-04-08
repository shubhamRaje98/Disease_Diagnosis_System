go:-
proposition(_),
undo.

 
proposition(arrythmias) :- arrythmias, !.
proposition(congenital_heart_disease)      :- congenital_heart_disease, !.
proposition(coronary_artery_disease)  :- coronary_artery_disease, !.
proposition(heart_attack)  :- heart_attack, !.
proposition(stroke)  :- stroke, !.
proposition(unknown_disease). 


arrythmias :-
prove(fluttering_in_chest),
prove(chest_pain),
prove(fainting),
prove(dizziness).

congenital_heart_disease :-
prove(blue_tiny_on_skin),
prove(rapid_breathing),
prove(rapid_heart_beat),
prove(extreme_fatigue),
prove(fainting_during_exercise),
prove(shortness_of_breath),
prove(swelling_in_legs_tummy_ankels).

coronary_artery_disease :-
prove(chest_pain_or_angina),
prove(pain_in_leg_arms),
prove(confusion),
prove(fatigue),
prove(shortness_of_breath).

heart_attack :-
prove(chest_pain),
prove(shortness_of_breath),
prove(pain_discomfort_in_neck_lower_jaw),
prove(sweating),
prove(palpitation),
prove(nausea).

stroke :-
prove(difficulty_in_walking_weak_muscels),
prove(blummed_vision_or_double_vision),
prove(loss_of_speech_or_difficulty_in_speaking),
prove(fatigue_vertigo),
prove(inability_to_understand).

prove(S) :- (yes(S) -> true; no(S) -> fail).

:- dynamic yes/1,no/1.

undo :- retract(yes(_)),fail.
undo :- retract(no(_)),fail.
undo.