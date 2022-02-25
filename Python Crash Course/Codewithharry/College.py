def function_12(Vaccine_1, Vaccine_2, consent_form):
    

    if Vaccine_1 and Vaccine_2 == 1 and consent_form == 1:
        print("1.Yes")
    elif consent_form == 1 and Vaccine_1 == 0 or Vaccine_2 == 0 :
        print("2.Yes")
    elif consent_form == 0 and Vaccine_1 and Vaccine_2 == 1:
        print("3. Cannot")


function_12(0, 1, 1)