from django import forms
from django.utils.translation import gettext_lazy as _

WOUND_CLASS_CHOICES = [
    ('clean', 'Clean'),
    ('clean_contaminated', 'Clean Contaminated'),
    ('contaminated', 'Contaminated'),
    ('dirty_infected', 'Dirty/Infected')
]

SCENARIO_CHOICES = [
    ('elective', 'Elective'),
    ('emergency', 'Emergency')
]

SSI_EVENT_CHOICES = [
    ('yes', 'Yes'),
    ('no', 'No')
]

EVENT_DETECTED_CHOICES = [
    ('A', 'During admission'),
    ('P', 'Post-discharge surveillance'),
    ('RF', 'Readmission to facility where procedure performed')
]

MICROORGANISM_CHOICES = [
    ('E. coli', 'E. coli'),
    ('Klebsiella pneumoniae', 'Klebsiella pneumoniae'),
    ('Enterococcus faecium', 'Enterococcus faecium'),
    ('Enterococcus faecalis', 'Enterococcus faecalis'),
    ('Staphylococcus haemolyticus', 'Staphylococcus haemolyticus'),
    ('Skin commensal flora', 'Skin commensal flora'),
    ('Pseudomonas aeruginosa', 'Pseudomonas aeruginosa'),
    ('Staphylococcus aureus (MRSA)', 'Staphylococcus aureus (MRSA)'),
    ('Staphylococcus aureus (MSSA)', 'Staphylococcus aureus (MSSA)'),
    ('CONS', 'CONS'),
    ('Acinetobacter baumanii', 'Acinetobacter baumanii'),
    ('Citrobacter koseri', 'Citrobacter koseri'),
    ('Citrobacter freundii', 'Citrobacter freundii'),
    ('Enterobacter cloacae', 'Enterobacter cloacae'),
    ('Enterobacter aerogenes', 'Enterobacter aerogenes'),
    ('Proteus mirabilis', 'Proteus mirabilis'),
    ('Morganella morganii', 'Morganella morganii'),
    ('Others', 'Others'),
]

ANTIBIOTIC_CHOICES = [
    ('Amoxicillin-clavulanic acid', 'Amoxicillin-clavulanic acid'),
    ('Amikacin', 'Amikacin'),
    ('Aztreonam', 'Aztreonam'),
    ('Cefepime', 'Cefepime'),
    ('Ceftazidime', 'Ceftazidime'),
    ('Ceftriaxone', 'Ceftriaxone'),
    ('Netilmicin', 'Netilmicin'),
    ('Meropenem', 'Meropenem'),
    ('Imipenem', 'Imipenem'),
    ('Levofloxacin', 'Levofloxacin'),
    ('Norfloxacin', 'Norfloxacin'),
    ('Ciprofloxacin', 'Ciprofloxacin'),
    ('Cefoperazone/Sulbactum', 'Cefoperazone/Sulbactum'),
    ('Ticarcillin/Clavulanic acid', 'Ticarcillin/Clavulanic acid'),
    ('Piperacillin-tazobactum', 'Piperacillin-tazobactum'),
    ('Ceftazidime/Avibactam', 'Ceftazidime/Avibactam'),
    ('Penicillin', 'Penicillin'),
    ('Oxacillin', 'Oxacillin'),
    ('Gentamicin', 'Gentamicin'),
    ('Tetracycline', 'Tetracycline'),
    ('Clindamycin', 'Clindamycin'),
    ('Vancomycin E STRIP', 'Vancomycin E STRIP'),
    ('Linezolid', 'Linezolid'),
    ('Teicoplanin', 'Teicoplanin'),
    ('Nitrofurantoin', 'Nitrofurantoin'),
    ('Erythromycin', 'Erythromycin'),
    ('Cefoxitin', 'Cefoxitin'),
    ('Co-trimoxazole', 'Co-trimoxazole'),
    ('Netilmicin', 'Netilmicin'),
    ('Ertapenem', 'Ertapenem'),
    ('Chloramphenicol', 'Chloramphenicol'),
    ('Fosfomycin', 'Fosfomycin'),
    ('Colistin E STRIP', 'Colistin E STRIP'),
]

ROUTE_CHOICES = [
    ('iv', 'I/V'),
    ('im', 'I/M'),
    ('sc', 'S/C'),
    ('id', 'I/D'),
    ('po', 'P/O'),
    ('local', 'LOCAL APPLICATION'),
    ('sublingual', 'SUB LINGUAL')
]

DOSE_CHOICES = [
    ('01', '01'),
    ('02', '02'),
    ('03', '03'),
    ('04', '04'),
    ('05', '05')
]

DURATION_CHOICES = [
    ('within 30 mins', 'within 30 mins'),
    ('within 60 mins', 'within 60 mins'),
    ('within 90 mins', 'within 90 mins'),
    ('more than 90 mins', 'more than 90 mins')
]

DEPARTMENT_CHOICES = [
    ("Cardiothoracic Surgery", "Cardiothoracic Surgery"),
    ("Internal Medicine", "Internal Medicine"),
    ("Anesthesia", "Anesthesia"),
    ("Cardiology", "Cardiology"),
    ("Hemato-Oncology & Bone Marrow Transplant", "Hemato-Oncology & Bone Marrow Transplant"),
    ("Liver Transplant & Surgical Gastroenterology", "Liver Transplant & Surgical Gastroenterology"),
    ("Oncology", "Oncology"),
    ("GI & Hepato-Pancreatico-Biliary Surgery", "GI & Hepato-Pancreatico-Biliary Surgery"),
    ("Critical Care", "Critical Care"),
    ("Pulmonary Medicine & Critical Care", "Pulmonary Medicine & Critical Care"),
    ("Radiodiagnosis & Imaging", "Radiodiagnosis & Imaging"),
    ("Nephrology", "Nephrology"),
    ("Urology & Renal Transplant", "Urology & Renal Transplant"),
    ("Plastic & Aesthetic Surgery", "Plastic & Aesthetic Surgery"),
    ("Gastroenterology", "Gastroenterology"),
    ("Orthopedics & Joint Replacement", "Orthopedics & Joint Replacement"),
    ("NeuroSciences", "NeuroSciences"),
    ("Pediatric", "Pediatric"),
    ("Laboratory Medicine", "Laboratory Medicine"),
    ("Endocrinology", "Endocrinology"),
    ("General & Minimally Access Surgery", "General & Minimally Access Surgery"),
    ("Obstetrics & Gynaecology", "Obstetrics & Gynaecology"),
    ("Dental Department", "Dental Department"),
    ("Nuclear Medicine", "Nuclear Medicine"),
    ("Dermatology", "Dermatology"),
    ("Rheumatology", "Rheumatology"),
    ("IVF & Reproductive Medicine", "IVF & Reproductive Medicine"),
    ("Orthopedic Spine", "Orthopedic Spine"),
    ("Behavioral Sciences", "Behavioral Sciences"),
    ("Onco Surgery", "Onco Surgery"),
    ("Medical Services", "Medical Services"),
    ("Ophthalmology", "Ophthalmology"),
    ("ENT", "ENT"),
    ("IVF", "IVF"),
    ("Respiratory, Critical Care & Sleep Medicine", "Respiratory, Critical Care & Sleep Medicine"),
    ("Bone Marrow Transplant", "Bone Marrow Transplant"),
    ("IVG", "IVG"),
    ("Obstetrics & Gynaecology", "Obstetrics & Gynaecology")
]

DOCTOR_CHOICES = [
    ('Dr. Manoj Luthra', 'Dr. Manoj Luthra'),
    ('Dr. Vinay Labroo', 'Dr. Vinay Labroo'),
    ('Dr. Ramesh Gourishankar', 'Dr. Ramesh Gourishankar'),
    ('Dr. Biswajit Paul', 'Dr. Biswajit Paul'),
    ('Dr. Brig (Dr.) Satyaranjan Das', 'Dr. Brig (Dr.) Satyaranjan Das'),
    ('Dr. Karisangal Vasudevan Ramaswamy', 'Dr. Karisangal Vasudevan Ramaswamy'),
    ('Dr. (Col) Sunil Sofat', 'Dr. (Col) Sunil Sofat'),
    ('Dr. Ashish Goel', 'Dr. Ashish Goel'),
    ('Dr. Rajesh Kapoor', 'Dr. Rajesh Kapoor'),
    ('Dr. Shalendra Goel', 'Dr. Shalendra Goel'),
    ('Dr. Gyanendra Agrawal', 'Dr. Gyanendra Agrawal'),
    ('Dr. Chandra Prakash Singh Chauhan', 'Dr. Chandra Prakash Singh Chauhan'),
    ('Dr. Anil Prasad Bhatt', 'Dr. Anil Prasad Bhatt'),
    ('Dr. Amit Kumar Devra', 'Dr. Amit Kumar Devra'),
    ('Dr. Ashish Rai', 'Dr. Ashish Rai'),
    ('Dr. Manik Sharma', 'Dr. Manik Sharma'),
    ('Dr. B. L. Agarwal', 'Dr. B. L. Agarwal'),
    ('Dr. Vijay Kumar Sinha', 'Dr. Vijay Kumar Sinha'),
    ('Dr. Sumit Bhushan Sharma', 'Dr. Sumit Bhushan Sharma'),
    ('Dr. Rohan Sinha', 'Dr. Rohan Sinha'),
    ('Dr. Dinesh Rattnani', 'Dr. Dinesh Rattnani'),
    ('Dr. Ashu Sawhney', 'Dr. Ashu Sawhney'),
    ('Dr. Suryasnata Das', 'Dr. Suryasnata Das'),
    ('Dr. (Col) Vimal Upreti', 'Dr. (Col) Vimal Upreti'),
    ('Dr. Nidhi Malhotra', 'Dr. Nidhi Malhotra'),
    ('Dr. Manish Gupta', 'Dr. Manish Gupta'),
    ('Dr. Abhishek Goyal', 'Dr. Abhishek Goyal'),
    ('Dr. Poonam Yadav', 'Dr. Poonam Yadav'),
    ('Dr. Praveen Kumar', 'Dr. Praveen Kumar'),
    ('Dr. Reenu Jain', 'Dr. Reenu Jain'),
    ('Dr. Abhishek Gulia', 'Dr. Abhishek Gulia'),
    ('Dr. Kishore Das', 'Dr. Kishore Das'),
    ('Dr. Pooja Goel', 'Dr. Pooja Goel'),
    ('Dr. Suhas Singla', 'Dr. Suhas Singla'),
    ('Dr. Asfaq Khan', 'Dr. Asfaq Khan'),
    ('Dr. Shalini Sharma', 'Dr. Shalini Sharma'),
    ('Dr. Sharique Ahmed', 'Dr. Sharique Ahmed'),
    ('Dr. Deepak Singhal', 'Dr. Deepak Singhal'),
    ('Dr. Smita Sharma', 'Dr. Smita Sharma'),
    ('Dr. Pankaj Kumar Goyal', 'Dr. Pankaj Kumar Goyal'),
    ('Dr. Sakshi Srivastava', 'Dr. Sakshi Srivastava'),
    ('Dr. Suvrat Arya', 'Dr. Suvrat Arya'),
    ('Dr. Soma Singh', 'Dr. Soma Singh'),
    ('Dr. Devender Chhonker', 'Dr. Devender Chhonker'),
    ('Dr. Pramod Saini', 'Dr. Pramod Saini'),
    ('Dr. Lok Prakash Choudhary', 'Dr. Lok Prakash Choudhary'),
    ('Dr. Dhirendra Pratap Singh Yadav', 'Dr. Dhirendra Pratap Singh Yadav'),
    ('Dr. Ashish Kumar Govil', 'Dr. Ashish Kumar Govil'),
    ('Dr. Atul Sharma', 'Dr. Atul Sharma'),
    ('Dr. Mansoor Ahmed Siddiqui', 'Dr. Mansoor Ahmed Siddiqui'),
    ('Dr. Krishnanu Dutta Choudhury', 'Dr. Krishnanu Dutta Choudhury'),
    ('Dr. Mrinmay Kumar Das', 'Dr. Mrinmay Kumar Das'),
    ('Dr. Minal Singh', 'Dr. Minal Singh'),
    ('Dr. Anshul Jain', 'Dr. Anshul Jain'),
    ('Dr. Swapnil Yashwant Gajway', 'Dr. Swapnil Yashwant Gajway'),
    ('Dr. Ashish Soni', 'Dr. Ashish Soni'),
    ('Dr. Kapil Kumar', 'Dr. Kapil Kumar'),
    ('Dr. Abhinav kumar', 'Dr. Abhinav kumar'),
    ('Dr. Hema Rattnani', 'Dr. Hema Rattnani'),
    ('Dr. Vikash Nayak', 'Dr. Vikash Nayak'),
    ('Dr. Naveen Prakash Verma', 'Dr. Naveen Prakash Verma'),
    ('Dr. Bhupender Singh', 'Dr. Bhupender Singh'),
    ('Dr. Aditya Bhatla', 'Dr. Aditya Bhatla'),
    ('Dr. Shovna Veshnavi', 'Dr. Shovna Veshnavi'),
    ('Dr. Purnima Sahni Sood', 'Dr. Purnima Sahni Sood'),
    ('Dr. (Col) Subodh Kumar', 'Dr. (Col) Subodh Kumar'),
    ('Dr. Shweta Goswami', 'Dr. Shweta Goswami'),
    ('Dr. Sunita Maheshwari', 'Dr. Sunita Maheshwari'),
    ('Dr. Atul K Maheshwari', 'Dr. Atul K Maheshwari'),
    ('Dr. Sharad Dev', 'Dr. Sharad Dev'),
    ('Dr. Vikram Singh Solanki', 'Dr. Vikram Singh Solanki'),
    ('Dr. Radha Agartaniya', 'Dr. Radha Agartaniya'),
    ('Dr. Mithee Bhanot', 'Dr. Mithee Bhanot'),
    ('Dr. Vibha Bansal', 'Dr. Vibha Bansal'),
    ('Dr. Rashmi Vyas', 'Dr. Rashmi Vyas'),
    ('Dr. Richa Thukral', 'Dr. Richa Thukral'),
    ('Dr. Nischal Anand', 'Dr. Nischal Anand'),
    ('Dr. Abhishek', 'Dr. Abhishek'),
    ('Dr. Vikram Bhardwaj', 'Dr. Vikram Bhardwaj'),
    ('Dr. Devashish Sharma', 'Dr. Devashish Sharma'),
    ('Dr. Aastha Gupta', 'Dr. Aastha Gupta'),
    ('Dr. Dipali Taneja', 'Dr. Dipali Taneja'),
    ('Dr. Priyadarshi Jitendra Kumar', 'Dr. Priyadarshi Jitendra Kumar'),
    ('Dr. Priyanka Srivastava', 'Dr. Priyanka Srivastava'),
    ('Dr. Manasi Mehra', 'Dr. Manasi Mehra'),
    ('Dr. Anita Singla', 'Dr. Anita Singla'),
    ('Dr. Abhishek Kumar', 'Dr. Abhishek Kumar'),
    ('Dr. Parul Singhal', 'Dr. Parul Singhal'),
    ('Dr. Prerna Sharma', 'Dr. Prerna Sharma'),
    ('Dr. Shweta Gupta', 'Dr. Shweta Gupta'),
    ('Dr. Kumari Madhulika', 'Dr. Kumari Madhulika'),
    ('Dr. Jyoti Jain', 'Dr. Jyoti Jain'),
    ('Dr. Sanjay Sharma', 'Dr. Sanjay Sharma'),
    ('Dr. Sandeep Yadav', 'Dr. Sandeep Yadav'),
    ('Dr. Sonalika Singh Chauhan', 'Dr. Sonalika Singh Chauhan'),
    ('Dr. Meenakshi Maurya', 'Dr. Meenakshi Maurya'),
    ('Dr. Manisha Ranjan', 'Dr. Manisha Ranjan'),
    ('Dr. Pankaj Kumar', 'Dr. Pankaj Kumar'),
    ('Dr. Rohit Kumar Pandey', 'Dr. Rohit Kumar Pandey'),
    ('Dr. Deepshikha', 'Dr. Deepshikha'),
    ('Dr. Meenakshi', 'Dr. Meenakshi'),
    ('Dr. Arti Yadav', 'Dr. Arti Yadav'),
    ('Dr. Anjali Gupta', 'Dr. Anjali Gupta'),
    ('Dr. Rajesh Prasad Gupta', 'Dr. Rajesh Prasad Gupta'),
    ('Dr. Abhay Kumar Singh', 'Dr. Abhay Kumar Singh'),
    ('Dr. Raman Mehta', 'Dr. Raman Mehta'),
    ('Dr. Abhishek Dave', 'Dr. Abhishek Dave'),
    ('Dr. Preeti Deolwari', 'Dr. Preeti Deolwari'),
    ('Dr. Abhijeet Kotabagi', 'Dr. Abhijeet Kotabagi'),
    ('Dr. Chandrika ', 'Dr. Chandrika'),
    ('Dr. Parineeta Maria', 'Dr. Parineeta Maria'),
    ('Dr. Soma Singh', 'Dr. Soma Singh'),
    ('Dr. Rakhi Gupta', 'Dr. Rakhi Gupta')
]

PROCEDURE_NAME_CHOICES = [
    ('Abdominal aortic aneurysm repair', 'Abdominal aortic aneurysm repair'),
    ('Limb amputation', 'Limb amputation'),
    ('Appendix surgery', 'Appendix surgery'),
    ('Shunt for dialysis', 'Shunt for dialysis'),
    ('Bile duct, liver or pancreatic surgery', 'Bile duct, liver or pancreatic surgery'),
    ('Carotid endarterectomy', 'Carotid endarterectomy'),
    ('Gallbladder surgery', 'Gallbladder surgery'),
    ('Colon surgery', 'Colon surgery'),
    ('Cesarean section', 'Cesarean section'),
    ('Gastric surgery', 'Gastric surgery'),
    ('Heart transplant', 'Heart transplant'),
    ('Abdominal hysterectomy', 'Abdominal hysterectomy'),
    ('Kidney transplant', 'Kidney transplant'),
    ('Laminectomy', 'Laminectomy'),
    ('Liver transplant', 'Liver transplant'),
    ('Neck surgery', 'Neck surgery'),
    ('Kidney surgery', 'Kidney surgery'),
    ('Ovarian surgery', 'Ovarian surgery'),
    ('Prostate surgery', 'Prostate surgery'),
    ('Rectal surgery', 'Rectal surgery'),
    ('Small bowel surgery', 'Small bowel surgery'),
    ('Spleen surgery', 'Spleen surgery'),
    ('Thoracic surgery', 'Thoracic surgery'),
    ('Thyroid and/or parathyroid surgery', 'Thyroid and/or parathyroid surgery'),
    ('Vaginal hysterectomy', 'Vaginal hysterectomy'),
    ('Exploratory laparotomy', 'Exploratory laparotomy'),
    ('Breast surgery', 'Breast surgery'),
    ('Cardiac surgery', 'Cardiac surgery'),
    ('Coronary artery bypass graft with both chest and donor site incisions',
     'Coronary artery bypass graft with both chest and donor site incisions'),
    ('Coronary artery bypass graft with chest incision only',
     'Coronary artery bypass graft with chest incision only'),
    ('Craniotomy', 'Craniotomy'),
    ('Spinal fusion', 'Spinal fusion'),
    ('Open reduction of fracture', 'Open reduction of fracture'),
    ('Herniorrhaphy', 'Herniorrhaphy'),
    ('Hip prosthesis', 'Hip prosthesis'),
    ('Knee prosthesis', 'Knee prosthesis'),
    ('Pacemaker surgery', 'Pacemaker surgery'),
    ('Peripheral vascular bypass surgery', 'Peripheral vascular bypass surgery'),
    ('Ventricular shunt', 'Ventricular shunt'),
    ('Laparotomy', 'Laparotomy'),
    ('Coronary artery bypass graft with donor incision(s)',
     'Coronary artery bypass graft with donor incision(s)'),
    ('Coronary artery bypass graft, chest incision only',
     'Coronary artery bypass graft, chest incision only'),
    ('Thyroid and or parathyroid surgery', 'Thyroid and or parathyroid surgery')
]

OT_CHOICES = [
    ('OT NO. 1', 'OT NO. 1'),
    ('OT NO. 2', 'OT NO. 2'),
    ('OT NO. 3', 'OT NO. 3'),
    ('OT NO. 4', 'OT NO. 4'),
    ('OT NO. 5', 'OT NO. 5'),
    ('OT NO. 6', 'OT NO. 6'),
    ('OT NO. 7', 'OT NO. 7'),
    ('OT NO. 8', 'OT NO. 8'),
    ('OT NO. 9', 'OT NO. 9'),
    ('OT NO. 10', 'OT NO. 10'),
    ('OT NO. 11', 'OT NO. 11'),
    ('OT NO. 12', 'OT NO. 12'),
    ('ROBOTIC OT', 'ROBOTIC OT'),
    ('C-SEC OT', 'C-SEC OT'),
    ('MINOR OT', 'MINOR OT'),
    ('COSMETOLOGY OT', 'COSMETOLOGY OT'),
    ('Others', 'Others')
]

INTERPRETATION_CHOICES = [
    ('', 'Select Interpretation'),
    ('Sensitive', 'Sensitive'),
    ('Resistant', 'Resistant'),
    ('Intermediate', 'Intermediate')
]

DAY_OPTIONS = [
    ("1", "Day 1"),
    ("2", "Day 2"),
    ("3", "Day 3"),
    ("4", "Day 4"),
    ("5", "Day 5"),
    ("6", "Day 6"),
    ("7", "Day 7"),
    ("8", "Day 8"),
    ("9", "Day 9"),
    ("10", "Day 10"),
    ("11", "Day 11"),
    ("12", "Day 12"),
    ("13", "Day 13"),
    ("14", "Day 14"),
    ("15", "Day 15"),
    ("16-30", "Days 16-30"),
    ("31-60", "Days 31-60"),
    ("60-90", "Days 60-90"),
]

YES_NO_EMPTY_CHOICES = [
    ("", "Empty"),
    ("Yes", "Yes"),
    ("No", "No"),
]


class PatientAdministrationForm(forms.Form):
    patientName = forms.CharField(max_length=100, label="Patient Name", required=True)
    patientID = forms.CharField(max_length=100, label="Patient ID", required=True)
    age = forms.IntegerField(label="Age", required=True)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], required=True,
                               label="Gender")
    dateOfAdmission = forms.DateField(label="Date of Admission", widget=forms.SelectDateWidget(), required=True)
    dateOfProcedure = forms.DateField(label="Date of Operative Procedure", widget=forms.SelectDateWidget(),required=True)
    admittingDepartment = forms.ChoiceField(choices=DEPARTMENT_CHOICES, label="Admitting Department", required=True)
    departmentPrimarySurgeon = forms.ChoiceField(choices=DOCTOR_CHOICES, label="Department (Primary Surgeon)", required=True)
    procedureName = forms.ChoiceField(choices=PROCEDURE_NAME_CHOICES, label="Name of the Procedure", required=True)
    diagnosis = forms.CharField(widget=forms.Textarea, label="Diagnosis",required=True)
    procedureDoneBy = forms.ChoiceField(choices=DOCTOR_CHOICES, label="Procedure done by (Primary Surgeon)",required=True)
    operationTheatre = forms.ChoiceField(choices=OT_CHOICES, label="Operation Theatre where Procedure done", required=True)
    outpatientProcedure = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label="Outpatient Procedure",required=True)
    scenarioProcedure = forms.ChoiceField(choices=SCENARIO_CHOICES, label="Scenario of Procedure", required=True)
    woundClass = forms.ChoiceField(choices=WOUND_CLASS_CHOICES, label="Wound Class", required=True)
    papGiven = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label="Pre/Peri-operative Antibiotic Prophylaxis (PAP) given", required=True)
    antibioticsGiven = forms.ChoiceField(choices=ANTIBIOTIC_CHOICES, label="If Yes, Antibiotics given", required=True)
    durationPAP = forms.CharField(max_length=100, label="Duration of PAP", required=True)
    ssiEventOccurred = forms.ChoiceField(choices=SSI_EVENT_CHOICES, label="SSI Event Occurred", required=True)
    dateOfEvent = forms.DateField(label="If Yes, Date of Event", widget=forms.SelectDateWidget(), required=True)


    # # Event Details
    # specific_event_sip = forms.BooleanField(required=False, label="Superficial Incisional Primary (SIP)")
    # specific_event_sis = forms.BooleanField(required=False, label="Superficial Incisional Secondary (SIS)")
    # specific_event_dip = forms.BooleanField(required=False, label="Deep Incisional Primary (DIP)")
    # specific_event_dis = forms.BooleanField(required=False, label="Deep Incisional Secondary (DIS)")
    # organ_space = forms.CharField(max_length=200, label="Organ/Space (specify site)", required=False)
    #
    # detected = forms.MultipleChoiceField(choices=EVENT_DETECTED_CHOICES, label="Detected",
    #                                      widget=forms.CheckboxSelectMultiple)
    # death_by_BSI = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label="Secondary BSI contributed to Death")
    #

class MicrobiologyForm(forms.Form):
    micro_organism = forms.ChoiceField(
        label="Micro-organism implicated for SSI event",
        choices=MICROORGANISM_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    for antibiotic in ANTIBIOTIC_CHOICES:
        antibiotic_name = antibiotic[0].lower().replace(' ', '_').replace('-', '_')

        locals()[f'{antibiotic_name}_mic'] = forms.DecimalField(
            label=f"{antibiotic[0]} MIC",
            required=False,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter MIC'})
        )

        locals()[f'{antibiotic_name}_interpretation'] = forms.ChoiceField(
            label=f"{antibiotic[0]} Interpretation",
            choices=INTERPRETATION_CHOICES,
            required=False,
            widget=forms.Select(attrs={'class': 'form-control'})
        )

class AntibioticSurveillanceForm(forms.Form):
    # Antibiotics prior to operation
    antibiotic_prior_1 = forms.ChoiceField(label='Antibiotic 1', choices=ANTIBIOTIC_CHOICES, required=False)
    route_prior_1 = forms.ChoiceField(label='Route of Administration', choices=ROUTE_CHOICES, required=False)
    duration_prior_1 = forms.ChoiceField(label='Duration', choices=DURATION_CHOICES, required=False)
    doses_prior_1 = forms.ChoiceField(label='Number of doses', choices=DOSE_CHOICES, required=False)

    antibiotic_prior_2 = forms.ChoiceField(label='Antibiotic 2', choices=ANTIBIOTIC_CHOICES, required=False)
    route_prior_2 = forms.ChoiceField(label='Route of Administration', choices=ROUTE_CHOICES, required=False)
    duration_prior_2 = forms.ChoiceField(label='Duration', choices=DURATION_CHOICES, required=False)
    doses_prior_2 = forms.ChoiceField(label='Number of doses', choices=DOSE_CHOICES, required=False)

    antibiotic_prior_3 = forms.ChoiceField(label='Antibiotic 3', choices=ANTIBIOTIC_CHOICES, required=False)
    route_prior_3 = forms.ChoiceField(label='Route of Administration', choices=ROUTE_CHOICES, required=False)
    duration_prior_3 = forms.ChoiceField(label='Duration', choices=DURATION_CHOICES, required=False)
    doses_prior_3 = forms.ChoiceField(label='Number of doses', choices=DOSE_CHOICES, required=False)

    # Antibiotics given pre/perioperatively
    antibiotic_pre_1 = forms.ChoiceField(label='Antibiotic 1 (Pre/Perioperative)', choices=ANTIBIOTIC_CHOICES, required=False)
    route_pre_1 = forms.ChoiceField(label='Route of Administration', choices=ROUTE_CHOICES, required=False)
    duration_pre_1 = forms.ChoiceField(label='Duration', choices=DURATION_CHOICES, required=False)
    doses_pre_1 = forms.ChoiceField(label='Number of doses', choices=DOSE_CHOICES, required=False)

    antibiotic_pre_2 = forms.ChoiceField(label='Antibiotic 2 (Pre/Perioperative)', choices=ANTIBIOTIC_CHOICES, required=False)
    route_pre_2 = forms.ChoiceField(label='Route of Administration', choices=ROUTE_CHOICES, required=False)
    duration_pre_2 = forms.ChoiceField(label='Duration', choices=DURATION_CHOICES, required=False)
    doses_pre_2 = forms.ChoiceField(label='Number of doses', choices=DOSE_CHOICES, required=False)

    antibiotic_pre_3 = forms.ChoiceField(label='Antibiotic 3 (Pre/Perioperative)', choices=ANTIBIOTIC_CHOICES, required=False)
    route_pre_3 = forms.ChoiceField(label='Route of Administration', choices=ROUTE_CHOICES, required=False)
    duration_pre_3 = forms.ChoiceField(label='Duration', choices=DURATION_CHOICES, required=False)
    doses_pre_3 = forms.ChoiceField(label='Number of doses', choices=DOSE_CHOICES, required=False)

    # Antibiotics given after peri-operative prophylaxis
    antibiotic_post_1 = forms.ChoiceField(label='Antibiotic 1 (Post-operative)', choices=ANTIBIOTIC_CHOICES, required=False)
    route_post_1 = forms.ChoiceField(label='Route of Administration', choices=ROUTE_CHOICES, required=False)
    duration_post_1 = forms.ChoiceField(label='Duration', choices=DURATION_CHOICES, required=False)
    doses_post_1 = forms.ChoiceField(label='Number of doses', choices=DOSE_CHOICES, required=False)

    antibiotic_post_2 = forms.ChoiceField(label='Antibiotic 2 (Post-operative)', choices=ANTIBIOTIC_CHOICES, required=False)
    route_post_2 = forms.ChoiceField(label='Route of Administration', choices=ROUTE_CHOICES, required=False)
    duration_post_2 = forms.ChoiceField(label='Duration', choices=DURATION_CHOICES, required=False)
    doses_post_2 = forms.ChoiceField(label='Number of doses', choices=DOSE_CHOICES, required=False)

    antibiotic_post_3 = forms.ChoiceField(label='Antibiotic 3 (Post-operative)', choices=ANTIBIOTIC_CHOICES, required=False)
    route_post_3 = forms.ChoiceField(label='Route of Administration', choices=ROUTE_CHOICES, required=False)
    duration_post_3 = forms.ChoiceField(label='Duration', choices=DURATION_CHOICES, required=False)
    doses_post_3 = forms.ChoiceField(label='Number of doses', choices=DOSE_CHOICES, required=False)

    antibiotic_post_4 = forms.ChoiceField(label='Antibiotic 4 (Post-operative)', choices=ANTIBIOTIC_CHOICES, required=False)
    route_post_4 = forms.ChoiceField(label='Route of Administration', choices=ROUTE_CHOICES, required=False)
    duration_post_4 = forms.ChoiceField(label='Duration', choices=DURATION_CHOICES, required=False)
    doses_post_4 = forms.ChoiceField(label='Number of doses', choices=DOSE_CHOICES, required=False)

    antibiotic_post_5 = forms.ChoiceField(label='Antibiotic 5 (Post-operative)', choices=ANTIBIOTIC_CHOICES, required=False)
    route_post_5 = forms.ChoiceField(label='Route of Administration', choices=ROUTE_CHOICES, required=False)
    duration_post_5 = forms.ChoiceField(label='Duration', choices=DURATION_CHOICES, required=False)
    doses_post_5 = forms.ChoiceField(label='Number of doses', choices=DOSE_CHOICES, required=False)

    antibiotic_post_6 = forms.ChoiceField(label='Antibiotic 6 (Post-operative)', choices=ANTIBIOTIC_CHOICES, required=False)
    route_post_6 = forms.ChoiceField(label='Route of Administration', choices=ROUTE_CHOICES, required=False)
    duration_post_6 = forms.ChoiceField(label='Duration', choices=DURATION_CHOICES, required=False)
    doses_post_6 = forms.ChoiceField(label='Number of doses', choices=DOSE_CHOICES, required=False)

    # Time of induction, incision, and surgery end
    time_induction = forms.TimeField(label='Time of Induction', required=False, widget=forms.TimeInput(format='%H:%M'))
    time_incision = forms.TimeField(label='Time of Incision', required=False, widget=forms.TimeInput(format='%H:%M'))
    time_end_surgery = forms.TimeField(label='End Time of Surgery', required=False, widget=forms.TimeInput(format='%H:%M'))


class PostOpDayForm(forms.Form):
    date_of_procedure = forms.DateField(label=_("Date of Procedure"), widget=forms.DateInput(attrs={"type": "date"}))
    name_of_procedure = forms.ChoiceField(label=_("Name of Procedure"), choices=PROCEDURE_NAME_CHOICES)

    def add_day_fields(self, symptom_name):
        for day_value, day_label in DAY_OPTIONS:
            self.fields[f"{symptom_name}_{day_value}"] = forms.ChoiceField(
                label=f"{day_label} ({symptom_name})",
                choices=YES_NO_EMPTY_CHOICES,
                required=False,
            )

    symptoms = [
        "purulent_discharge",
        "localized_pain_tenderness",
        "localized_swelling",
        "fever",
        "incision_opened",
        "spontaneous_dehiscence",
        "abscess",
        "micro_organism_gram",
        "imaging_infection",
        "positive_culture_discharge",
        "blood_culture_sent",
        "physician_diagnosis",
    ]

    def __init__(self, *args, **kwargs):
        super(PostOpDayForm, self).__init__(*args, **kwargs)
        for symptom in self.symptoms:
            self.add_day_fields(symptom)

    any_other = forms.CharField(label=_("Any other (specify below)"), required=False, widget=forms.Textarea(attrs={"placeholder": "Additional details"}))

# class SSIEvaluationForm(forms.Form):
#
#     procedure_name = forms.ChoiceField(choices=PROCEDURE_NAME_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
#     patient_id = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     patient_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], widget=forms.Select(attrs={'class': 'form-control'}))
#     date_of_procedure = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
#
#     def _create_yes_no_remark_fields(label):
#         return [
#             forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect, label=label),
#             forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Remarks'}), label='')
#         ]
#
#     antimicrobial_prophylaxis_guidelines, antimicrobial_prophylaxis_guidelines_remarks = _create_yes_no_remark_fields("Administer antimicrobial prophylaxis as per guidelines")
#     prophylaxis_within_1_hour, prophylaxis_within_1_hour_remarks = _create_yes_no_remark_fields("Administer antimicrobial prophylaxis within 1 hour of incision")
#     antimicrobial_prophylaxis_surgical_procedure, antimicrobial_prophylaxis_surgical_procedure_remarks = _create_yes_no_remark_fields("Select antimicrobial agents based on procedure")
#     ssi_pathogens_prophylaxis, ssi_pathogens_prophylaxis_remarks = _create_yes_no_remark_fields("Select agents for most common SSI pathogens")
#     published_recommendations_prophylaxis, published_recommendations_prophylaxis_remarks = _create_yes_no_remark_fields("Select agents based on published recommendations")
#     discontinue_antibiotics_24_hours, discontinue_antibiotics_24_hours_remarks = _create_yes_no_remark_fields("Discontinue antibiotics within 24 hours after surgery")
#     redose_3_hour_interval, redose_3_hour_interval_remarks = _create_yes_no_remark_fields("Redose antibiotics for procedures lasting >3 hours")
#     adjust_for_bmi, adjust_for_bmi_remarks = _create_yes_no_remark_fields("Adjust prophylaxis dose for BMI > 30")
#     no_hair_removal, no_hair_removal_remarks = _create_yes_no_remark_fields("Avoid hair removal unless necessary")
#     razors_not_used, razors_not_used_remarks = _create_yes_no_remark_fields("Razors not used for hair removal")
#     clippers_used, clippers_used_remarks = _create_yes_no_remark_fields("Use clippers or depilatory agents")
#     antiseptic_agent_preparation, antiseptic_agent_preparation_remarks = _create_yes_no_remark_fields("Use appropriate antiseptic agent for skin preparation")
#     mechanical_colon_preparation, mechanical_colon_preparation_remarks = _create_yes_no_remark_fields("Mechanically prepare the colon")
#     administer_oral_antimicrobial, administer_oral_antimicrobial_remarks = _create_yes_no_remark_fields("Administer oral antimicrobial agents prior to surgery")
#     keep_doors_closed, keep_doors_closed_remarks = _create_yes_no_remark_fields("Keep operating room doors closed during surgery")
#     maintain_normothermia, maintain_normothermia_remarks = _create_yes_no_remark_fields("Maintain immediate post-op normothermia")
#     protect_primary_closure, protect_primary_closure_remarks = _create_yes_no_remark_fields("Protect primary closure incisions with sterile dressing for 24-48 hours")
#     blood_glucose_control_post_op, blood_glucose_control_post_op_remarks = _create_yes_no_remark_fields("Control blood glucose level during the immediate post-operative period in cardiac procedures")
#     measure_glucose_at_6am, measure_glucose_at_6am_remarks = _create_yes_no_remark_fields("Measure blood glucose level at 6AM on POD#1 and #2 (cardiac procedures)")
#     glucose_level_under_200, glucose_level_under_200_remarks = _create_yes_no_remark_fields("Maintain post-operative blood glucose levels < 200 mg/dL in cardiac procedures")
#     screen_preop_glucose, screen_preop_glucose_remarks = _create_yes_no_remark_fields("Screen pre-op blood glucose levels in elective procedures")
#     tight_glucose_control, tight_glucose_control_remarks = _create_yes_no_remark_fields("Maintain tight glucose control on POD#1 and POD#2 for elective procedures")
#     nasal_screen_cabg, nasal_screen_cabg_remarks = _create_yes_no_remark_fields("Nasal screen and decolonize S. aureus carriers for CABG procedures")
#     nasal_screen_elective, nasal_screen_elective_remarks = _create_yes_no_remark_fields("Nasal screen and decolonize S. aureus carriers for other elective procedures")
#     increased_oxygen_use, increased_oxygen_use_remarks = _create_yes_no_remark_fields("Use increased fraction of inspired oxygen during and post-op")
#     postpone_until_infection_resolves, postpone_until_infection_resolves_remarks = _create_yes_no_remark_fields("Postpone operation until remote infection resolves")
#


# class SSIEvaluationForm(forms.Form):
#     procedure_name = forms.ChoiceField(
#         choices=PROCEDURE_NAME_CHOICES,
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )
#     patient_id = forms.CharField(
#         max_length=50,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     patient_name = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     age = forms.IntegerField(
#         widget=forms.NumberInput(attrs={'class': 'form-control'})
#     )
#     gender = forms.ChoiceField(
#         choices=[('Male', 'Male'), ('Female', 'Female')],
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )
#     date_of_procedure = forms.DateField(
#         widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
#     )
#
#     # Helper method for creating fields
#     @staticmethod
#     def create_yes_no_remark_fields(label):
#         return {
#             f'{label}_choice': forms.ChoiceField(
#                 choices=[('Yes', 'Yes'), ('No', 'No')],
#                 widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
#                 label=label,
#             ),
#             f'{label}_remarks': forms.CharField(
#                 max_length=100,
#                 required=False,
#                 widget=forms.TextInput(attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Remarks'
#                 }),
#                 label=f'{label} Remarks'
#             ),
#         }
#
#     # Define fields dynamically using the helper method
#     fields = [
#         "antimicrobial_prophylaxis_guidelines",
#         "prophylaxis_within_1_hour",
#         "antimicrobial_prophylaxis_surgical_procedure",
#         "ssi_pathogens_prophylaxis",
#         "published_recommendations_prophylaxis",
#         "discontinue_antibiotics_24_hours",
#         "redose_3_hour_interval",
#         "adjust_for_bmi",
#         "no_hair_removal",
#         "razors_not_used",
#         "clippers_used",
#         "antiseptic_agent_preparation",
#         "mechanical_colon_preparation",
#         "administer_oral_antimicrobial",
#         "keep_doors_closed",
#         "maintain_normothermia",
#         "protect_primary_closure",
#         "blood_glucose_control_post_op",
#         "measure_glucose_at_6am",
#         "glucose_level_under_200",
#         "screen_preop_glucose",
#         "tight_glucose_control",
#         "nasal_screen_cabg",
#         "nasal_screen_elective",
#         "increased_oxygen_use",
#         "postpone_until_infection_resolves",
#     ]
#
#     # Add fields dynamically to the form
#     for field in fields:
#         locals().update(create_yes_no_remark_fields(field))


# class SSIEvaluationForm(forms.Form):
#     procedure_name = forms.ChoiceField(
#         choices=PROCEDURE_NAME_CHOICES,
#         required=True,
#         label="Procedure Name"
#     )
#     patient_id = forms.CharField(
#         max_length=50,
#         required=True,
#         label="Patient ID"
#     )
#     patient_name = forms.CharField(
#         max_length=100,
#         required=True,
#         label="Patient Name"
#     )
#     age = forms.IntegerField(
#         required=True,
#         label="Age"
#     )
#     gender = forms.ChoiceField(
#         choices=[('Male', 'Male'), ('Female', 'Female')],
#         required=True,
#         label="Gender"
#     )
#     date_of_procedure = forms.DateField(
#         required=True,
#         label="Date of Procedure"
#     )
#
#     # Helper method to generate yes/no choice fields with remarks
#     def create_yes_no_remark_fields(self, field_name):
#         return {
#             f'{field_name}_choice': forms.ChoiceField(
#                 choices=[('Yes', 'Yes'), ('No', 'No')],
#                 required=False
#             ),
#             f'{field_name}_remarks': forms.CharField(
#                 max_length=100,
#                 required=False
#             ),
#         }
#
#     # Fields requiring dynamic yes/no and remarks
#     fields = [
#         "antimicrobial_prophylaxis_guidelines",
#         "prophylaxis_within_1_hour",
#         "antimicrobial_prophylaxis_surgical_procedure",
#         "ssi_pathogens_prophylaxis",
#         "published_recommendations_prophylaxis",
#         "discontinue_antibiotics_24_hours",
#         "redose_3_hour_interval",
#         "adjust_for_bmi",
#         "no_hair_removal",
#         "razors_not_used",
#         "clippers_used",
#         "antiseptic_agent_preparation",
#         "mechanical_colon_preparation",
#         "administer_oral_antimicrobial",
#         "keep_doors_closed",
#         "maintain_normothermia",
#         "protect_primary_closure",
#         "blood_glucose_control_post_op",
#         "measure_glucose_at_6am",
#         "glucose_level_under_200",
#         "screen_preop_glucose",
#         "tight_glucose_control",
#         "nasal_screen_cabg",
#         "nasal_screen_elective",
#         "increased_oxygen_use",
#         "postpone_until_infection_resolves",
#     ]
#
#     for field in fields:
#         locals().update(create_yes_no_remark_fields(field))

class SSIEvaluationForm(forms.Form):
    procedure_name = forms.ChoiceField(
        choices=PROCEDURE_NAME_CHOICES,
        required=True,
        label="Procedure Name"
    )
    patient_id = forms.CharField(
        max_length=50,
        required=True,
        label="Patient ID"
    )
    patient_name = forms.CharField(
        max_length=100,
        required=True,
        label="Patient Name"
    )
    age = forms.IntegerField(
        required=True,
        label="Age"
    )
    gender = forms.ChoiceField(
        choices=[('Male', 'Male'), ('Female', 'Female')],
        required=True,
        label="Gender"
    )
    date_of_procedure = forms.DateField(
        required=True,
        label="Date of Procedure"
    )

    dynamic_fields = [
        "antimicrobial_prophylaxis_guidelines",
        "prophylaxis_within_1_hour",
        "antimicrobial_prophylaxis_surgical_procedure",
        "ssi_pathogens_prophylaxis",
        "published_recommendations_prophylaxis",
        "discontinue_antibiotics_24_hours",
        "redose_3_hour_interval",
        "adjust_for_bmi",
        "no_hair_removal",
        "razors_not_used",
        "clippers_used",
        "antiseptic_agent_preparation",
        "mechanical_colon_preparation",
        "administer_oral_antimicrobial",
        "keep_doors_closed",
        "maintain_normothermia",
        "protect_primary_closure",
        "blood_glucose_control_post_op",
        "measure_glucose_at_6am",
        "glucose_level_under_200",
        "screen_preop_glucose",
        "tight_glucose_control",
        "nasal_screen_cabg",
        "nasal_screen_elective",
        "increased_oxygen_use",
        "postpone_until_infection_resolves",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.dynamic_fields:
            self.fields[f'{field}_choice'] = forms.ChoiceField(
                choices=[('Yes', 'Yes'), ('No', 'No')],
                required=False
            )
            self.fields[f'{field}_remarks'] = forms.CharField(
                max_length=100,
                required=False
            )

# class PatientSurgeryDetails
# class PatientAntibioticDetails
# class PatientMicrobiologyDetails
