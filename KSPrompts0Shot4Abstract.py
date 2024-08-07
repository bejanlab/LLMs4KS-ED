def p1(note_text):
    messages = []
    messages.append({"role": "system", "content": f"""You are a clinical expert in identifying symptomatic 
                     kidney stone or nephrolithiasis from emergency department reports. 
                     Instructions: The only answer choices are 'Yes' or 'No'!"""})
    messages.append({"role": "user", "content": f"""Does the following emergency department report describe 
                     a symptomatic kidney stone or nephrolithiasis? 
                     Emergency department report: {note_text}"""})                     
    return messages

def p2(note_text):
    messages = []
    messages.append({"role": "system", "content": f"""As a clinical expert, your role is to determine if 
                     the patient's visit to the emergency department is primarily due to experiencing a 
                     symptomatic kidney stone or nephrolithiasis. Instructions: Choose either 'Yes' or 'No'."""})
    messages.append({"role": "user", "content": f"""Is the main cause of the emergency department visit indicated 
                     in the following report due to a symptomatic kidney stone or nephrolithiasis? 
                     Emergency department report: {note_text}"""})                     
    return messages

def p3(note_text):
    messages = []
    messages.append({"role": "system", "content": f"""As a clinical expert, your role is to determine if 
                     the patient's visit to the emergency room is primarily due to experiencing a symptomatic 
                     kidney stone or nephrolithiasis. Instructions: Choose either 'Yes' or 'No'."""})
    messages.append({"role": "user", "content": f"""Is the main cause of the emergency room visit indicated 
                     in the following report due to a symptomatic kidney stone or nephrolithiasis? 
                     Emergency room report: {note_text}"""})                     
    return messages

def p4(note_text):
    messages = []
    messages.append({"role": "system", "content": f"""As a clinical expert, your task is to ascertain whether 
                     the patient's emergency department visit is caused by experiencing a symptomatic kidney 
                     stone or nephrolithiasis. Instructions: Respond with either 'Yes' or 'No'."""})
    messages.append({"role": "user", "content": f"""Does the emergency department report specify that the 
                     primary reason for the visit is a symptomatic kidney stone or nephrolithiasis? 
                     Emergency department report: {note_text}"""})                     
    return messages

def p5(note_text):
    messages = []
    messages.append({"role": "system", "content": f"""Your expertise lies in determining if the 
                     patient's emergency department visit is mainly a result of experiencing a 
                     symptomatic kidney stone or nephrolithiasis. Instructions: Select either 'Yes' or 'No'."""})
    messages.append({"role": "user", "content": f"""In the following emergency department report, is the 
                     primary cause of the visit attributed to a symptomatic kidney stone or nephrolithiasis? 
                     Emergency department report: {note_text}"""})                     
    return messages

def p6(note_text):
    messages = []
    messages.append({"role": "system", "content": f"""In your clinical capacity, you are tasked with identifying 
                     whether the primary reason for the patient's emergency department visit is the experience 
                     of a symptomatic kidney stone or nephrolithiasis. Instructions: Choose 'Yes' or 'No.'"""})
    messages.append({"role": "user", "content": f"""Is a symptomatic kidney stone or nephrolithiasis cited 
                     as the main reason for the emergency department visit in the following report? 
                     Emergency department report: {note_text}"""})                     
    return messages

def p7(note_text):
    messages = []
    messages.append({"role": "system", "content": f"""You are a clinician tasked with analyzing emergency 
                     department reports."""})
    messages.append({"role": "user", "content": f"""Given the following emergency department report, 
                     output 'Yes' if the reason for the encounter is due to a symptomatic kidney stone 
                     or nephrolithiasis. Otherwise, output 'No'.  The stone could be in the kidney or ureter. 
                     Emergency department report: {note_text}"""})                     
    return messages

def p8(note_text):
    messages = []
    messages.append({"role": "system", "content": f"""You are a clinician tasked with analyzing emergency 
                     department reports."""})
    messages.append({"role": "user", "content": f"""Given the following emergency department report, 
                     output 'Yes' if the reason for the encounter is due to a symptomatic stone in the 
                     urinary tract, especially if the stone is in the kidney or ureter. Otherwise, output 'No'. 
                     Emergency department report: {note_text}"""}) 
    return messages

def p9(note_text):
    messages = []
    messages.append({"role": "system", "content": f"""Your responsibility is to assess emergency department 
                     reports and ascertain whether the primary reason for the related encounters is due 
                     to a symptomatic stone in the urinary tract. A prior definition of this is based on 
                     the ROKS nomogram criteria (Rule et al, JASN, 2014).  The criteria were: 1) the patient 
                     presented for clinical care with gross hematuria or pain, 2) a stone was either seen on 
                     imaging in a location consistent with partial, complete, or intermittent obstruction (ureter, 
                     uretero-pelvic junction, uretero-vesicular junction, kidney pelvis, or lower kidney pole) or 
                     there was documentation that it was voided, and 3) no prior symptomatic episodes from a 
                     kidney stone confirmed on imaging or voided. The pain could be typical renal colic or 
                     atypical (vague nonlocalized abdominal, pelvic, or back pain). Symptomatic lower pole 
                     stones required a clinical pattern of intermittent symptoms from intermittent obstruction 
                     at the ureteropelvic junction. In addition to obstructing stones, stone episodes were also 
                     considered valid if the patient presented with a symptomatic urinary tract infection from 
                     a struvite stone, even if the stone was not obstructing. Incidentally discovered asymptomatic 
                     kidney stones on imaging, bladder stones, and “suspected stones” (renal colic but no stone 
                     ever seen) were not considered valid episodes."""})
    messages.append({"role": "user", "content": f"""Given the following emergency department report, determine 
                     if the reason for the encounter is due to a symptomatic stone in the urinary tract. 
                     The only answer choices are 'Yes' or 'No'! 
                     Emergency department report: {note_text}"""}) 
    return messages
