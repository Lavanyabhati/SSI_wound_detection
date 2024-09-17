from django import forms

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

ANTIBIOTIC_SUSCEPTIBILITY_CHOICES = [
    ('sensitive', 'Sensitive'),
    ('resistant', 'Resistant'),
    ('intermediate', 'Intermediate')
]


class PatientAdministrationForm(forms.Form):
    patient_name = forms.CharField(max_length=100, label="Patient Name")
    patient_id = forms.CharField(max_length=100, label="Patient ID")
    age = forms.IntegerField(label="Age")
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], required=True,
                               label="Gender")
    date_of_admission = forms.DateField(label="Date of Admission", widget=forms.SelectDateWidget())
    date_of_procedure = forms.DateField(label="Date of Operative Procedure", widget=forms.SelectDateWidget())
    admitting_department = forms.CharField(max_length=100, label="Admitting Department")
    department_primary_surgeon = forms.CharField(max_length=100, label="Department (Primary Surgeon)")
    name_of_procedure = forms.CharField(max_length=200, label="Name of the Procedure")
    diagnosis = forms.CharField(widget=forms.Textarea, label="Diagnosis")
    procedure_done_by = forms.CharField(max_length=100, label="Procedure done by (Primary Surgeon)")
    operation_theatre = forms.CharField(max_length=100, label="Operation Theatre where Procedure done")
    outpatient_procedure = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label="Outpatient Procedure")
    scenario_of_procedure = forms.ChoiceField(choices=SCENARIO_CHOICES, label="Scenario of Procedure")
    wound_class = forms.ChoiceField(choices=WOUND_CLASS_CHOICES, label="Wound Class")
    pap_given = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')],
                                  label="Pre/Peri-operative Antibiotic Prophylaxis (PAP) given")
    antibiotics_given = forms.CharField(max_length=200, label="If Yes, Antibiotics given", required=False)
    duration_of_pap = forms.CharField(max_length=100, label="Duration of PAP", required=False)
    ssi_event_occurred = forms.ChoiceField(choices=SSI_EVENT_CHOICES, label="SSI Event Occurred")
    date_of_event = forms.DateField(label="If Yes, Date of Event", widget=forms.SelectDateWidget(), required=False)

    # Event Details
    specific_event_sip = forms.BooleanField(required=False, label="Superficial Incisional Primary (SIP)")
    specific_event_sis = forms.BooleanField(required=False, label="Superficial Incisional Secondary (SIS)")
    specific_event_dip = forms.BooleanField(required=False, label="Deep Incisional Primary (DIP)")
    specific_event_dis = forms.BooleanField(required=False, label="Deep Incisional Secondary (DIS)")
    organ_space = forms.CharField(max_length=200, label="Organ/Space (specify site)", required=False)

    detected = forms.MultipleChoiceField(choices=EVENT_DETECTED_CHOICES, label="Detected",
                                         widget=forms.CheckboxSelectMultiple)
    death_by_BSI = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label="Secondary BSI contributed to Death")


    # Micro-organisms
    microorganism_1 = forms.CharField(max_length=100, label="Micro-organism 1", required=False)
    microorganism_2 = forms.CharField(max_length=100, label="Micro-organism 2", required=False)

    # Antibiotic Susceptibility Patterns
    isolate_1_sensitive = forms.ChoiceField(choices=ANTIBIOTIC_SUSCEPTIBILITY_CHOICES,
                                            label="Isolate 1 (Antibiotic Susceptibility Pattern)")
    isolate_2_sensitive = forms.ChoiceField(choices=ANTIBIOTIC_SUSCEPTIBILITY_CHOICES,
                                            label="Isolate 2 (Antibiotic Susceptibility Pattern)")




# class PatientSurgeryDetails
# class PatientAntibioticDetails
# class PatientMicrobiologyDetails
