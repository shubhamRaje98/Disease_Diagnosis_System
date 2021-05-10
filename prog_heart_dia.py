#If fatality risk above 60 is considerable fatality risk.
from pyswip import Prolog
class Prog:

	def __init__(self):
		self.prolog = Prolog()
		self.prolog.consult("heart.pl")
		self.fatality_risk = 0
		self.risk = 0
		self.risk_factor = 0

	def calculate_risk_factor(self, que_1,que_2, que_3, que_4, que_5, que_6, que_7, que_8, que_9, que_10):
		total_no_questions = 10

		if que_1 == 'yes':
			self.risk += 1
			print("in que_1")
#		que_2 = input("How often you have junk/unhealthy food [often/rarely] : ")		
		if que_2 == 'often':
			self.risk += 1
			print("in que_2")
#		que_3 = input("How often you do some physical activity [frequently/rarely] : ")
		if que_3 == 'rarely':
			self.risk += 1
			print("in que_3")
#		que_4 = input("How often you feel stressed in daily life? [often/rarely] : ")
		if que_4 == 'often':			
			self.risk += 1
			print("in que_4")

		#from here
#		que_5 = input("What is your gender? : ")
		if que_5 == 'male':
			self.risk += 1
			print("in que_5")
		
#		que_6 = input("Do you have genetic history of heart disease? : ")
		if que_6 == 'yes':
			self.risk += 1
			print("in que_6")
		
#		que_7 = input("Do you have diabetes? : ")
		if que_7 == 'yes':
			self.risk += 1
			print("in que_7")
		
#		que_8 = int(input("What is your total cholesterol count? : "))
		if que_8 == ">200":
			self.risk += 1
			print("in que_8")
		
#		que_9 = input("Have you had heart attack before? : ")
		if que_9 == 'yes':
			self.risk += 1
			print("in que_9")
		
#		que_10 = int(input("What is your BMI index? : "))  #extreme obesity
		if que_10 == ">40":
			self.risk += 1
			print("in que_10")

		# Risk Calculation formula :
		''' here variabl risk is sum of positive responses from user, we are dividing it by total question asked and multipling it by 100 to 
			calculate risk factor in percentage.
		 '''
		print(self.risk)
		return self.risk, total_no_questions
		'''

		self.risk_factor = self.risk*(100/total_no_questions)
		print("Your risk of having heart related issue is : " + str(self.risk_factor) + "%")
		'''
	def calculate_fatality_risk(self, general_fatality_risk, risk_factor):
		''' Fatality risk calculation : fatality_risk = general fatality risk of that disease + 50% of (that indviduals risk factor) 
			this we can calculate unique fatality risk percentage for each user.
		''' 
		self.fatality_risk = general_fatality_risk + (risk_factor/2) 
		print("Your fatality risk factor is : " + str(self.fatality_risk) + "%")
		print("In Here!!!!")
		return self.fatality_risk
		

	def diagnose_Arrythmias(self, que_1, que_2, que_3, que_4, risk_factor):
				
		print("********Arrythmias Diagnosis*********\n")
		symptoms = ["fluttering_in_chest", "chest_pain", "fainting",
			"dizziness"]
		general_fatality_risk = 50

		if que_1 == "yes":
			print("que_1")
			assertion = "yes(fluttering_in_chest)"
			self.prolog.assertz(assertion)

		if que_2 == "yes":
			print("que_2")
			assertion = "yes(chest_pain)"
			self.prolog.assertz(assertion)
		
		if que_3 == "yes":
			print("que_3")
			assertion = "yes(fainting)"
			self.prolog.assertz(assertion)

		if que_4 == "yes":
			print("que_4")
			assertion = "yes(dizziness)"
			self.prolog.assertz(assertion)

		if bool(list(self.prolog.query("proposition(arrythmias)"))):
			print("Your sufering from Arrythmias")
			self.prolog.query("undo.")
			ft = self.calculate_fatality_risk(general_fatality_risk, risk_factor)
			return ft
		else:
			print("Your definatly not sufering from Arrythmias")
			self.prolog.query("undo.")
			return 0
	
		
	def diagnose_congenital_heart_disease(self, CHD_que_1,CHD_que_2, CHD_que_3, CHD_que_4, CHD_que_5, CHD_que_6, CHD_que_7, risk_factor):
		responses = [(CHD_que_1, "blue_tiny_on_skin"), (CHD_que_2, "rapid_breathing"), (CHD_que_3, "rapid_heart_beat"), (CHD_que_4, "extreme_fatigue"), (CHD_que_5, "fainting_during_exercise"), (CHD_que_6, "shortness_of_breath"), (CHD_que_7, "swelling_in_legs_tummy_ankels")]

		general_fatality_risk = 50

		for response in responses:
			if response[0] == "yes":
				assertion = "yes(%s)"%response[1]
				print(assertion)
				self.prolog.assertz(assertion)
			if response[0] == "no":
				assertion = "no(%s)"%response[1]
				self.prolog.assertz(assertion)

		if bool(list(self.prolog.query("proposition(congenital_heart_disease)"))):
			print("Your sufering from Congenital Heart Disease")
			self.prolog.query("undo.")
			ft = self.calculate_fatality_risk(general_fatality_risk, risk_factor)
			return ft

		else:
			print("Your definatly not sufering from Congenital Heart Disease")
			self.prolog.query("undo.")
			return 0

		
	def diagnose_coronary_artery_disease(self, CAD_que_1,CAD_que_2, CAD_que_3, CAD_que_4, CAD_que_5, risk_factor):
		responses = [(CAD_que_1, "chest_pain_or_angina"), (CAD_que_2, "pain_in_leg_arms") , (CAD_que_3, "confusion"), (CAD_que_4, "fatigue"), (CAD_que_5, "shortness_of_breath")]
		general_fatality_risk = 50
			
		for response in responses:
			if response[0] == 'yes':
				print("Here!")
				assertion = "yes(%s)"%response[1]
				print(assertion)
				self.prolog.assertz(assertion)
			if response[0] == 'no':
				assertion = "no(%s)"%response[1]
				self.prolog.assertz(assertion)
		
		#print(bool(list(self.prolog.query("proposition(coronary_artery_disease)"))))
		
		if bool(list(self.prolog.query("proposition(coronary_artery_disease)"))):
			print("Your sufering from Coronary Artery Disease")
			self.prolog.query("undo.")
			ft = self.calculate_fatality_risk(general_fatality_risk, risk_factor)
			return ft
		else:
			print("Your definatly not sufering from Coronary Artery Disease")
			self.prolog.query("undo.")
			return 0
			
		#self.prolog.query("undo.")

	def diagnose_heart_attack(self, HearAtt_que_1, HearAtt_que_2, HearAtt_que_3, HearAtt_que_4, HearAtt_que_5, HearAtt_que_6, risk_factor):
		responses = [(HearAtt_que_1, "chest_pain"), (HearAtt_que_2, "shortness_of_breath"), (HearAtt_que_3, "pain_discomfort_in_neck_lower_jaw"),
			(HearAtt_que_4, "sweating"), (HearAtt_que_5, "palpitation"), (HearAtt_que_6, "nausea")]
		general_fatality_risk = 50

		for response in responses:
			if response[0] == 'yes':
				print("Here!")
				assertion = "yes(%s)"%response[1]
				print(assertion)
				self.prolog.assertz(assertion)
			if response[0] == 'no':
				assertion = "no(%s)"%response[1]
				self.prolog.assertz(assertion)		
		
		if bool(list(self.prolog.query("proposition(heart_attack)"))):
			print("You may have heart attack")
			self.prolog.query("undo.")
			ft = self.calculate_fatality_risk(general_fatality_risk, risk_factor)
			return ft
		else:
			print("You might not have heart attack")
			self.prolog.query("undo.")
			return 0
			
		#self.prolog.query("undo.")
		
	def diagnose_stroke(self, stroke_que_1, stroke_que_2, stroke_que_3, stroke_que_4, stroke_que_5, risk_factor):
		responses = [(stroke_que_1, "difficulty_in_walking_weak_muscels"), (stroke_que_2, "blummed_vision_or_double_vision"),
			(stroke_que_3, "loss_of_speech_or_difficulty_in_speaking"), (stroke_que_4, "fatigue_vertigo"), (stroke_que_5, "inability_to_understand")]
		general_fatality_risk = 50

		for response in responses:
			if response[0] == 'yes':
				print("Here!")
				assertion = "yes(%s)"%response[1]
				print(assertion)
				self.prolog.assertz(assertion)
			if response[0] == 'no':
				assertion = "no(%s)"%response[1]
				self.prolog.assertz(assertion)		
			
		
		#print(bool(list(self.prolog.query("proposition(stroke)"))))
		
		if bool(list(self.prolog.query("proposition(stroke)"))):
			print("You may have Stroke")
			self.prolog.query("undo.")
			ft = self.calculate_fatality_risk(general_fatality_risk, risk_factor)
			return ft
		else:
			print("You might not have Stroke")
			self.prolog.query("undo.")
			return 0
			
		#self.prolog.query("undo.")
		
obj = Prog()
#obj.calculate_risk_factor()
#obj.diagnose_stroke("yes", "yes", "yes", "yes", "yes", 40)
#obj.diagnose_heart_attack("yes", "yes", "yes", "yes", "yes", "yes", 40)
#obj.diagnose_coronary_artery_disease("yes", "yes", "yes", "yes", "yes", 40)
#obj.diagnose_congenital_heart_disease("yes", "yes", "yes", "yes", "yes", "yes", "yes", 30)
#obj.calculate_fatality_risk()
#obj.diagnose_Arrythmias("yes", "yes", "yes", "yes", 40)
