from requests import get
import re

male_file = open("male.txt", 'a+')
female_file = open("female.txt", 'a+')
for i in range(50): 
    resp = get("https://www.theyfightcrime.org/")
    text = resp.text.split("</P>")
    
    he_list = re.findall(r"<P>(.*(?=She))", text[1])   # find male characters
    he_str = " ".join(he_list)
    male_file.write(str(i+1)+":"+he_str+'\n')
    
    she_list = re.findall(r"(She.*(?=They))", text[1])    # find female characters
    she_str = " ".join(she_list)
    female_file.write(str(i+1)+":"+she_str+'\n')

male_file.close()
female_file.close()
