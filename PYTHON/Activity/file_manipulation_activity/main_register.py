import register_patient_module

yes_options = ['s', 'sim', 'y', 'yes']
confirmation = 's'

if __name__ == '__main__':
    while confirmation in yes_options:
        register_patient_module.register_patient()
        confirmation = input("Deseja cadastrar novo paciente? ")
        confirmation = confirmation.lower()
    
    with open('PYTHON/Activity/file_manipulation_activity/patients.txt') as my_patients:
        print(my_patients.read())
