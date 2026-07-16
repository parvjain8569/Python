# import math

# def simulate_battle(energy_levels, hammer_power):
#     total_strikes = 0
#     titans_defeated = 0

#     for energy in energy_levels:
#         if energy > 0:
           
#             strikes = math.ceil(energy / hammer_power)
            
#             total_strikes += strikes
#             titans_defeated += 1
#         else:
            
#             continue

#     print(titans_defeated)
#     print(total_strikes)


# titan_energies = [120, 0, 95, 150, 0, 80, 60] 
# hammer_strength = 40 


# simulate_battle(titan_energies, hammer_strength)





# def validate_ticket(code):
#     try:
#         if code[0:4] != "TKT-":
#             raise Exception("Bad Input")
        
#         after_dash = code[4:]
        
#         if len(after_dash) != 4:
#             raise Exception("Bad Format")
            
#         digits = after_dash[0:2]
#         letters = after_dash[2:4]
        
#         if digits.isdigit() and letters.isupper():
#             return "Valid Ticket"
#         else:
#             raise Exception("Bad Format")

#     except Exception as error:
#         return str(error)








# user_entry = input()
# print(validate_ticket(user_entry))



# def process_crew_pay(crew_data):
#     updated_data = {}
#     highEarners = {}

#     for name, values in crew_data.items():
#         base = values[0]
#         bonus_percent = values[1]
        
        
#         final_pay = base + (base * bonus_percent) / 100
#         if final_pay >= 20000:
#             updated_data[name] = float(final_pay)
            

#             if final_pay > 50000:
#                 highEarners[name] = float(final_pay)
                
#     return (updated_data, highEarners)


# input_data = {'Pilot1':[30000,30], 'CrewA':[16000,25], 'CrewB':[55000,10]}
# result = process_crew_pay(input_data)
# print(result)






def chemical_batch(identifier):
    try:
        if identifier[0:5] != "CHEM-":
            raise Exception("Protocol Error")
        
        after_dash = identifier[5:]
        
        if len(after_dash) != 5:
            raise Exception("Bad Format")
            
        digits = after_dash[0]
        letters = after_dash[1:5]
        
        if digits.isupper() and letters.isdigit:
            return "batch ready"
        else:
            raise Exception("Format error")

    except Exception as error:
        return str(error)
print(chemical_batch("CHEM-Z0001"))




def verify_telemetry(code):
    try:
        if code[0:4] != "TLM-":
            raise Exception("Code Missing")
        
        segment = code[4:]
        
        if len(segment) != 4:
            raise Exception("Code Corrupt")
            
        digit_part = segment[0]
        letter_part = segment[1:4]
        
        if digit_part.isdigit() and letter_part.isupper():
            return "Code Accepted"
        else:
            raise Exception("Code Corrupt")

    except Exception as error:
        return str(error)

user_input = input()
print(verify_telemetry(user_input))




def normalize_salaries(employee_data):
    updated_data = {}
    highEarners = {}
    
    for name, values in employee_data.items():
        base = values[0]
        bonus_pct = values[1]
        
        final_salary = base + (base * bonus_pct) / 100
        
        if final_salary >= 20000:
            updated_data[name] = float(final_salary)
            
            if final_salary > 50000:
                highEarners[name] = float(final_salary)
                
    return updated_data, highEarners

input_dict = eval(input())
print(normalize_salaries(input_dict))





def recalculate_rewards(player_data):
    updated_data = {}
    highEarners = {}
    
    for name, info in player_data.items():
        base = info[0]
        bonus_pct = info[1]
        
        final_reward = base + (base * bonus_pct) / 100
        
        if final_reward >= 20000:
            updated_data[name] = float(final_reward)
            
            if final_reward > 50000:
                highEarners[name] = float(final_reward)
                
    return (updated_data, highEarners)

input_dict = eval(input())
print(recalculate_rewards(input_dict))