"""
This script pulls the actual presidential portraits from Library of Congress.

"""


import re

img_string= '/static/portals/free-to-use/public-domain/presidential-portraits/46-joe-biden.png'


#function to return the image of president,
def getPrez(img_string):
    match=re.search('portraits/.*',img_string)
    match_end= match.group()
    match2=re.search(r'[0-9].*[a-z]*-[a-z]*',match_end)
    match_end2= match2.group()
    return(match_end2.replace('-',"_"))

match=re.search('portraits/.*',img_string)
match_end= match.group()
match2=re.search(r'[0-9].*[a-z]*-[a-z]*',match_end)
match_end2= match2.group()

print(match_end2.replace('-','_'))