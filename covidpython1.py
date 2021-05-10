from pyswip import Prolog
class prog:
    def __init__(self):
        self.prolog=Prolog()
        self.prolog.consult("covidprologknowledgebase.pl")
        self.risk_of_getting_covid=0

    def covid_diagnosis1(self,ques_1,ques_2,ques_3,ques_4,ques_5,ques_6,ques_7,ques_8,ques_9,ques_10,ques_11,ques_12,ques_13,ques_14,ques_15,ques_16):
        #ques_1 =input("Have been travelled in last 30 days?: ")
        if ques_1 == "yes":
            self.prolog.assertz("yes(travelled)")
           # global risk_of_getting_covid
            self.risk_of_getting_covid=self.risk_of_getting_covid+10
        else:
            self.prolog.assertz("no(travelled)")

        if ques_2 == "yes":
            self.prolog.assertz("yes(contacted)")
                
            self.risk_of_getting_covid=self.risk_of_getting_covid+10
        else:
            self.prolog.assertz("no(contacted)")

        if ques_3 == "yes":
            self.prolog.assertz("yes(live_in_contaminated_zone)")
                
            self.risk_of_getting_covid=self.risk_of_getting_covid+10
        else:
            self.prolog.assertz("no(live_in_contaminated_zone)")

        if ques_4 == "yes":
            self.prolog.assertz("yes(breathing_problem)")
        else:
            self.prolog.assertz("no(breathing_problem)")

        if ques_5 == "yes":
            self.prolog.assertz("yes(chest_pain_or_pressure)")
        else:
            self.prolog.assertz("no(chest_pain_or_pressure)")

        if ques_6 == "yes":
            self.prolog.assertz("yes(loss_of_speech_or_movement)")
        else:
            self.prolog.assertz("no(loss_of_speech_or_movement)")

        if ques_7 == "yes":
            self.prolog.assertz("yes(fever)")
        else:
            self.prolog.assertz("no(fever)")

        if ques_8 == "yes":
            self.prolog.assertz("yes(dry_cough)")
        else:
            self.prolog.assertz("no(dry_cough)")

        if ques_9 == "yes":
            self.prolog.assertz("yes(tiredness)")
        else:
            self.prolog.assertz("no(tiredness)")

        if ques_10 == "yes":
            self.prolog.assertz("yes(aches_pain)")
        else:
            self.prolog.assertz("no(aches_pain)")
            
        if ques_11 == "yes":
            self.prolog.assertz("yes(sore_throat)")
        else:
            self.prolog.assertz("no(sore_throat)")

        if ques_12 == "yes":
            self.prolog.assertz("yes(loss_taste)")
        else:
            self.prolog.assertz("no(loss_taste)")

        if ques_13 == "yes":
            self.prolog.assertz("yes(headache)")
        else:
            self.prolog.assertz("no(headache)")

        if ques_14 == "yes":
            self.prolog.assertz("yes(diarrhea)")
        else:
            self.prolog.assertz("no(diarrhea)")

        if ques_15 == "yes":
            self.prolog.assertz("yes(conjunctivitis)")
        else:
            self.prolog.assertz("no(conjunctivitis)")

        if ques_16 == "yes":
            self.prolog.assertz("yes(rash_on_skin)")
        else:
            self.prolog.assertz("no(rash_on_skin)")


        if bool(list(self.prolog.query("checkfor(serious1)"))):
            self.risk_of_getting_covid=self.risk_of_getting_covid+7

        if bool(list(self.prolog.query("checkfor(serious2)"))):
            self.risk_of_getting_covid=self.risk_of_getting_covid+7

        if bool(list(self.prolog.query("checkfor(serious3)"))):
            self.risk_of_getting_covid=self.risk_of_getting_covid+8

        if bool(list(self.prolog.query("checkfor(slot_2)"))):
            self.risk_of_getting_covid=self.risk_of_getting_covid+20

        if bool(list(self.prolog.query("checkfor(slot_3)"))):
            self.risk_of_getting_covid=self.risk_of_getting_covid+7

        if bool(list(self.prolog.query("checkfor(slot_4)"))):
            self.risk_of_getting_covid=self.risk_of_getting_covid+8

        if bool(list(self.prolog.query("checkfor(slot_5)"))):
            self.risk_of_getting_covid=self.risk_of_getting_covid+10
            return self.risk_of_getting_covid
        else:
            return self.risk_of_getting_covid
    
