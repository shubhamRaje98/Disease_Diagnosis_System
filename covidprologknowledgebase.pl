
checkfor(travel_history) :- travel_history.
checkfor(contact_tracing) :- contact_tracing.
checkfor(contaminated_zone_check) :- contaminated_zone_check.

checkfor(serious1) :- serious1.
checkfor(serious2) :- serious2.
checkfor(serious3) :- serious3.
checkfor(slot_2) :- slot_2.
checkfor(slot_3) :- slot_3.
checkfor(slot_4) :- slot_4.
checkfor(slot_5) :- slot_5.

travel_history :-
prove(travelled).

contact_tracing :-
prove(contacted).

contaminated_zone_check:
prove(live_in_contaminated_zone).

serious1 :-
prove(breathing_problem).

serious2 :-
prove(chest_pain_or_pressure).

serious3 :-
prove(loss_of_speech_or_movement).


slot_2 :-
prove(fever),
prove(dry_cough),
prove(tiredness).

slot_3 :-
prove(aches_pain),
prove(sore_throat).

slot_4:-
prove(loss_taste),
prove(headache).

slot_5 :-
prove(diarrhea),
prove(conjunctivitis),
prove(rash_on_skin).

prove(S) :- (yes(S) -> true; no(S) -> fail).

:- dynamic yes/1,no/1.


undo :- retract(yes(_)),fail.
undo :- retract(no(_)),fail.
undo.
