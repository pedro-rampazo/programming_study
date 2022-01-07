import os

def register_patient():
    patient_data = {
        "Nome Completo": None,
        "E-mail": None,
        "CPF": None,
        "RG": None,
        "Telefone": None,
        "Ano de Nascimento": None,
    }

    for key in patient_data.keys():
        personal_data = input(f"{key}: ")
        if key == "Ano de Nascimento":
            personal_data = int(personal_data)
        patient_data[f"{key}"] = personal_data
    
    age = 2022 - patient_data.get("Ano de Nascimento")
    
    if age >= 65:
        patient_data["Grupo de Risco"] = "Sim"
    
    if os.path.exists('PYTHON/Activity/file_manipulation_activity/patients.txt') is False:
        os.mknod('PYTHON/Activity/file_manipulation_activity/patients.txt')
    
    with open('PYTHON/Activity/file_manipulation_activity/patients.txt', 'a') as save_patient_data:
        for k, v in patient_data.items():
            save_patient_data.write(f"{k}: {v}\n")
        save_patient_data.write("\n")