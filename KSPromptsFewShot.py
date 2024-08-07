import KSUtils

## p2: 0-shot - best GPT-4
#def p2(test_note):
#    messages = []
#    messages.append({"role": "system", "content": f"""As a clinical expert, your role is to determine if 
#                     the patient's visit to the emergency department is primarily due to experiencing a 
#                     symptomatic kidney stone or nephrolithiasis. Instructions: Choose either 'Yes' or 'No'."""})
#    messages.append({"role": "user", "content": f"""Is the main cause of the emergency department visit indicated 
#                     in the following report due to a symptomatic kidney stone or nephrolithiasis? 
#                     Emergency department report: {test_note}"""})                     
#    return messages

## p2: few-shot
## input
## - test note
## - list of [note, label] pairs
def p2(test_note, train_note_label_list):
    messages = []
    messages.append({"role": "system", "content": f"""As a clinical expert, your role is to determine if 
                     the patient's visit to the emergency department is primarily due to experiencing a 
                     symptomatic kidney stone or nephrolithiasis. Instructions: Choose either 'Yes' or 'No'."""})

    for note_label_tuple in train_note_label_list:
        train_note, train_label = note_label_tuple
        messages.append({"role": "user", "content": f"""Is the main cause of the emergency department visit indicated 
                        in the following report due to a symptomatic kidney stone or nephrolithiasis? 
                        Emergency department report: {train_note}"""})                     
        messages.append({"role": "assistant", "content": f"{KSUtils.map_01_to_yesno(train_label)}"})                     

    messages.append({"role": "user", "content": f"""Is the main cause of the emergency department visit indicated 
                     in the following report due to a symptomatic kidney stone or nephrolithiasis? 
                     Emergency department report: {test_note}"""})                     
    return messages

##-----------------------------------------------------------------

## p7: 0-shot - best GPT-3.5
#def p7(test_note):
#    messages = []
#    messages.append({"role": "system", "content": f"""You are a clinician tasked with analyzing emergency 
#                     department reports."""})
#   messages.append({"role": "user", "content": f"""Given the following emergency department report, 
#                     output 'Yes' if the reason for the encounter is due to a symptomatic kidney stone 
#                     or nephrolithiasis. Otherwise, output 'No'.  The stone could be in the kidney or ureter. 
#                     Emergency department report: {test_note}"""})                     
#    return messages

## p7: few-shot (0-shot - best GPT-3.5)
def p7(test_note, train_note_label_list):
    messages = []
    messages.append({"role": "system", "content": f"""You are a clinician tasked with analyzing emergency 
                     department reports."""})
    
    for note_label_tuple in train_note_label_list:
        train_note, train_label = note_label_tuple
        messages.append({"role": "user", "content": f"""Given the following emergency department report, 
                        output 'Yes' if the reason for the encounter is due to a symptomatic kidney stone 
                        or nephrolithiasis. Otherwise, output 'No'.  The stone could be in the kidney or ureter. 
                        Emergency department report: {train_note}"""})                     
        messages.append({"role": "assistant", "content": f"{KSUtils.map_01_to_yesno(train_label)}"})                     

    messages.append({"role": "user", "content": f"""Given the following emergency department report, 
                     output 'Yes' if the reason for the encounter is due to a symptomatic kidney stone 
                     or nephrolithiasis. Otherwise, output 'No'.  The stone could be in the kidney or ureter. 
                     Emergency department report: {test_note}"""})                     
    return messages

def p7_demogr(test_note, test_demogr, train_note_demogr_label_list):
    messages = []
    messages.append({"role": "system", "content": f"""You are a clinician tasked with analyzing emergency 
                     department reports."""})
    
    for note_demogr_label_triple in train_note_demogr_label_list:
        train_note, train_demogr, train_label = note_demogr_label_triple
        messages.append({"role": "user", "content": f"""Given the following emergency department report, 
                        output 'Yes' if the reason for the encounter is due to a symptomatic kidney stone 
                        or nephrolithiasis. Otherwise, output 'No'.  The stone could be in the kidney or ureter. 
                         {train_demogr} 
                        Emergency department report: {train_note}"""})                     
        messages.append({"role": "assistant", "content": f"{KSUtils.map_01_to_yesno(train_label)}"})                     

    messages.append({"role": "user", "content": f"""Given the following emergency department report, 
                     output 'Yes' if the reason for the encounter is due to a symptomatic kidney stone 
                     or nephrolithiasis. Otherwise, output 'No'.  The stone could be in the kidney or ureter. 
                     {test_demogr} 
                     Emergency department report: {test_note}"""})                     
    return messages