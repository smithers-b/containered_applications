import re
import collections
## Must be 10 characters include uppercase and lowercase letters, numbers, and symbols. 14 characters is best.
## https://www.cisecurity.org/insights/white-papers/cis-primer-securing-login-credentials#:~:text=CIS%20recommends%20the%20use%20of%2014%20characters.%20Use,passwords%20regularly%20%E2%80%93%20at%20least%20every%2060%20days.
passwd = ''
specials = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

def main():
    weak = 0
    strong = 0
    passwds = open('passphrases.txt', 'r+', encoding='utf-8')
    passwd = passwds.readline()
    while passwd:
        passwd = passwds.readline()
        result = re.search('[a-z][A-Z][0-9]', passwd)
        if result != None and len(passwd) >= 10:
            specialsearch = re.search(specials,passwd)
            if specialsearch != None:
                strong = strong + 1
        else:
            weak = weak + 1
        passwd = passwds.readline()
    passwds.close()

    print("There are ", +strong, " secure passwords in this file")
    print("There are ", +weak, " insecure passwords in this file")
       
 
main()
    


