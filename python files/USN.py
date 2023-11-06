import re
def validate(s):
    ug="[0-4]{1}[a-zA-z]{2}[0-9]{2}[a-zA-z]{2}[0-9]{3}"
    pg="[0-4]{1}[a-zA-z]{2}[0-9]{2}[a-zA-z]{3}[0-9]{2}"
    pat=ug+ "|" +pg
    if re.search(pat,s):
        print("valid")
    else:
        print("not")
validate("1DA21IS049")
validate("8DA45gHF0789")
