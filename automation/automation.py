import re
with open("assets/potential-contacts.txt", "r")as file:
    text = file.read()
    print(text)

def email(text):
    email_pattern = r"\S+@\S+"
    emails = re.findall(email_pattern, text)
    emails = list(set(emails))
    emails.sort()
    return emails

def phone_num(text):
    number_pattern_ = r"[0-9-+x.()]{7,}"
    phone_numbers = []
    numbers = re.findall(number_pattern_, text)
    
    for num in numbers:
        num = num.replace(".", "").replace("(", "").replace(")", "")
        if len(num) == 10:
            num = num[:3]+"-"+num[3:6]+"-"+num[6:]
        phone_numbers.append(num)
        
    phone_numbers = list(set(phone_numbers))
    return phone_numbers


def writer(url, fun):
    with open(url, "w") as file:
        string2 = ""
        for item in fun(text):
            string2 += item+"\n"
        file.write(string2)

writer("assets/phone_numbers.txt", phone_num)
writer("assets/emails.txt", email)
