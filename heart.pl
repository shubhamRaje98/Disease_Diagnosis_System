go:-
proposition(_),
revoke.

 
proposition(arrythmias) :- arrythmias, !.
proposition(congenital_heart_disease)      :- congenital_heart_disease, !.
proposition(coronary_artery_disease)  :- coronary_artery_disease, !.
proposition(heart_attack)  :- heart_attack, !.
proposition(stroke)  :- stroke, !.
proposition(unknown_disease). 


arrythmias :-
verify(fluttering_in_chest),
verify(chest_pain),
verify(fainting),
verify(dizziness).

congenital_heart_disease :-
verify(blue_tiny_on_skin),
verify(rapid_breathing),
verify(rapid_heart_beat),
verify(extreme_fatigue),
verify(fainting_during_exercise),
verify(shortness_of_breath),
verify(swelling_in_legs_tummy_ankels).

coronary_artery_disease :-
verify(chest_pain_or_angina),
verify(pain_in_leg_arms),
verify(confusion),
verify(fatigue),
verify(shortness_of_breath).

heart_attack :-
verify(chest_pain),
verify(shortness_of_breath),
verify(pain_discomfort_in_neck_lower_jaw),
verify(sweating),
verify(palpitation),
verify(nausea).

stroke :-
verify(difficulty_in_walking_weak_muscels),
verify(blummed_vision_or_double_vision),
verify(loss_of_speech_or_difficulty_in_speaking),
verify(fatigue_vertigo),
verify(inability_to_understand).

verify(S) :- (yes(S) -> true; no(S) -> fail).

:- dynamic yes/1,no/1.

revoke :- retract(yes(_)),fail.		
revoke :- retract(no(_)),fail.
revoke.
