from requests import get
import re

male = open("male.txt", 'a+')
female = open("female.txt", 'a+')
for i in range(50):
    resp = get("https://www.theyfightcrime.org/")
    text = resp.text.split("</P>")

    him = re.findall(r"<P>(.*(?=She))", text[1])
    him_ = " ".join(him)
    male.write(str(i+1)+":"+him_+'\n')

    her = re.findall(r"(She.*(?=They))", text[1])
    her_ = " ".join(her)
    female.write(str(i+1)+":"+her_+'\n')

male.close()
female.close()
