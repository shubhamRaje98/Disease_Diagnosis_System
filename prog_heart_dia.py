#If fatality risk above 60 is considerable fatality risk.
from pyswip import Prolog
class Prog:

	def __init__(self):
		self.prolog = Prolog()
		self.prolog.consult("heart.pl")
		self.fatality_risk = 0
		self.risk = 0
		self.risk_factor = 0

	def calculate_risk_factor(self):
		total_no_questions = 10

		que_1 = input("Do you smoke? : ")
		if que_1 == 'yes':
			self.risk += 1
		que_2 = input("How often you have junk/unhealthy food [often/rarely] : ")		
		if que_2 == 'often':
			self.risk += 1
		que_3 = input("How often you do some physical activity [frequently/rarely] : ")
		if que_3 == 'frequently':
			self.risk += 1
		que_4 = input("How often you feel stressed in daily life? [often/rarely] : ")
		if que_4 == 'often':			
			self.risk += 1

		#from here
		que_5 = input("What is your gender? : ")
		if que_5 == 'male' or 'm':
			self.risk += 1
		
		que_6 = input("Do you have genetic history of heart disease? : ")
		if que_6 == 'yes':
			self.risk += 1
		
		que_7 = input("Do you have diabetes? : ")
		if que_7 == 'yes':
			self.risk += 1
		
		que_8 = int(input("What is your total cholesterol count? : "))
		if que_8 > 200:
			self.risk += 1
		
		que_9 = input("Have you had heart attack before? : ")
		if que_9 == 'yes':
			self.risk += 1
		
		que_10 = int(input("What is your BMI index? : "))  #extreme obesity
		if que_10 > 40:
			self.risk += 1

		# Risk Calculation formula :
		''' here variabl risk is sum of positive responses from user, we are dividing it by total question asked and multipling it by 100 to 
			calculate risk factor in percentage.
		 '''

		self.risk_factor = self.risk*(100/total_no_questions)
		print("Your risk of having heart related issue is : " + str(self.risk_factor) + "%")

	def calculate_fatality_risk(self, general_fatality_risk):
		''' Fatality risk calculation : fatality_risk = general fatality risk of that disease + 50% of (that indviduals risk factor) 
			this we can calculate unique fatality risk percentage for each user.
		''' 
		self.fatality_risk = general_fatality_risk + (self.risk_factor/2) 
		print("Your fatality risk factor is : " + str(self.fatality_risk) + "%")
		

	def diagnose_Arrythmias(self):
	
		print("********Arrythmias Diagnosis*********\n")
		symptoms = ["fluttering_in_chest", "chest_pain", "fainting",
			"dizziness"]
		general_fatality_risk = 50
			
		for element in symptoms:
			res = input("Do you have " + element + " : ")
			if res == 'yes':
				print("Here!")
				assertion = "yes(%s)"%element
				print(assertion)
				self.prolog.assertz(assertion)
			if res == 'no':
				assertion = "no(%s)"%element
				self.prolog.assertz(assertion)

		print(bool(list((self.prolog.query("proposition(arrythmias)")))))
		#print(list(self.prolog.query("proposition(arrythmias)")))


		if bool(list(self.prolog.query("proposition(arrythmias)"))):
			print("Your sufering from Arrythmias")
			self.calculate_fatality_risk(general_fatality_risk)
		else:
			print("Your definatly not sufering from Arrythmias")

		self.prolog.query("undo.")
		
	def diagnose_congenital_heart_disease(self):
		symptoms = ["blue_tiny_on_skin", "rapid_breathing", "rapid_heart_beat",
			"extreme_fatigue", "fainting_during_exercise", "shortness_of_breath",
			"swelling_in_legs_tummy_ankels"]
		general_fatality_risk = 50
			
		for element in symptoms:
			res = input("Do you have " + element + " : ")
			if res == 'yes':
				print("Here!")
				assertion = "yes(%s)"%element
				print(assertion)
				self.prolog.assertz(assertion)
			if res == 'no':
				assertion = "no(%s)"%element
				self.prolog.assertz(assertion)
		
		print(bool(list(self.prolog.query("proposition(congenital_heart_disease)"))))
		
		if bool(list(self.prolog.query("proposition(congenital_heart_disease)"))):
			print("Your suffering from Congenital Heart Disease")
			self.calculate_fatality_risk(general_fatality_risk)
		else:
			print("Your not suffering from Congenital Heart Disease")
			
		self.prolog.query("undo.")
		
	def diagnose_coronary_artery_disease(self):
		symptoms = ["chest_pain_or_angina", "pain_in_leg_arms", "confusion",
			"fatigue", "shortness_of_breath"]
		general_fatality_risk = 50
			
		for element in symptoms:
			res = input("Do you have " + element + " : ")
			if res == 'yes':
				print("Here!")
				assertion = "yes(%s)"%element
				print(assertion)
				self.prolog.assertz(assertion)
			if res == 'no':
				assertion = "no(%s)"%element
				self.prolog.assertz(assertion)
		
		print(bool(list(self.prolog.query("proposition(coronary_artery_disease)"))))
		
		if bool(list(self.prolog.query("proposition(coronary_artery_disease)"))):
			print("Your suffering from Coronary Artery Disease")
			self.calculate_fatality_risk(general_fatality_risk)
		else:
			print("Your not suffering from Coronary Artery Disease")
			
		self.prolog.query("undo.")

	def diagnose_heart_attack(self):
		symptoms = ["chest_pain", "shortness_of_breath", "pain_discomfort_in_neck_lower_jaw",
			"sweating", "palpitation", "nausea"]
		general_fatality_risk = 50
			
		for element in symptoms:
			res = input("Do you have " + element + " : ")
			if res == 'yes':
				print("Here!")
				assertion = "yes(%s)"%element
				print(assertion)
				self.prolog.assertz(assertion)
			if res == 'no':
				assertion = "no(%s)"%element
				self.prolog.assertz(assertion)
		
		print(bool(list(self.prolog.query("proposition(heart_attack)"))))
		
		if bool(list(self.prolog.query("proposition(heart_attack)"))):
			print("You may have Heart Attack!")
			self.calculate_fatality_risk(general_fatality_risk)
		else:
			print("You don't have Heart Attack")
			
		self.prolog.query("undo.")
		
	def diagnose_stroke(self):
		symptoms = ["difficulty_in_walking_weak_muscels", "blummed_vision_or_double_vision",
			"loss_of_speech_or_difficulty_in_speaking", "fatigue_vertigo", "inability_to_understand"]
		general_fatality_risk = 50
			
		for element in symptoms:
			res = input("Do you have " + element + " : ")
			if res == 'yes':
				print("Here!")
				assertion = "yes(%s)"%element
				print(assertion)
				self.prolog.assertz(assertion)
			if res == 'no':
				assertion = "no(%s)"%element
				self.prolog.assertz(assertion)
		
		print(bool(list(self.prolog.query("proposition(stroke)"))))
		
		if bool(list(self.prolog.query("proposition(stroke)"))):
			print("You may have stroke!")
			self.calculate_fatality_risk(general_fatality_risk)
		else:
			print("You don't have stroke")
			
		self.prolog.query("undo.")
		
obj = Prog()
obj.calculate_risk_factor()
#obj.diagnose_stroke()
#obj.diagnose_heart_attack()
#obj.diagnose_coronary_artery_disease()
#obj.diagnose_congenital_heart_disease()
#obj.calculate_fatality_risk()
obj.diagnose_Arrythmias()