#Gabriel Soares
#Programmer Test

import regex as re
import json

class contacts: # initiating the class for contact, note ability to handle number and character input
    def __init__(self, name, email=None, phoneNumber=None):
        self.name = str(name)
        self.email = str(email)
        if phoneNumber:
            tempPhoneNumber = re.sub('[()-]', '', str(phoneNumber))
            self.phoneNumber = tempPhoneNumber
        if not phoneNumber:
            self.phoneNumber = None
    def getName(self): # method for returning name
        return self.name
    def getEmail(self): # method for returning email
        return self.email
    def getPhoneNumber(self): # method for returning number
        return self.phoneNumber
    def setName(self,newName): # method to set new name
        self.name = (newName)
    def setName(self,newEmail=None): # method to set new email
        self.email = str(newEmail)
    def setName(self,newNumber=None): # method to set new phone number given input as str, int, or including characters
        if newNumber:
            tempNewNumber = re.sub('[()-]', '', str(newNumber))
            self.phoneNumber = tempNewNumber
        if not newNumber:
            self.phoneNumber = None

class leads: # initiating the class for leads, similar to above contact class but adding contacted status
    def __init__(self, name=None, email=None, phoneNumber=None, contactedStatus=False):
        self.name = str(name)
        self.email = str(email)
        if phoneNumber:
            tempPhoneNumber = re.sub('[()-]', '', str(phoneNumber))
            self.phoneNumber = tempPhoneNumber
        if not phoneNumber:
            self.phoneNumber = None
        self.contactedStatus = contactedStatus
    def getName(self):
        return self.name
    def getEmail(self):
        return self.email
    def getPhoneNumber(self):
        return self.phoneNumber
    def getStatus(self): # method to get the contacted status of a lead
        return self.contactedStatus
    def setName(self,newName):
        self.name = (newName)
    def setName(self,newEmail=None):
        self.email = str(newEmail)
    def setName(self,newNumber=None):
        if newNumber:
            tempNewNumber = re.sub('[()-]', '', str(newNumber))
            self.phoneNumber = tempNewNumber
        if not newNumber:
            self.phoneNumber = None
    def setStatus(self, contactedStatus=False): #method to seet new contacted status
        self.contactedStatus = contactedStatus

def main():
    # initiating contacts, using various input types for phone numbers

    contactsList = [contacts('Alice Brown', phoneNumber='(123)111-2223'),
                    contacts('Bob Crown', 'bob@crowns.com'),
                    contacts('Carlos Drew', 'carl@drewwss.com', 3453334445),
                    contacts('Doug Emerty', phoneNumber=4564445556),
                    contacts('Egan Fair', email='eg@fairness.com', phoneNumber='5675556667')]

    # print(contactsList[0].getPhoneNumber())     # used for testing
    # print(contactsList[0].getEmail())           # used for testing
    # print(contactsList[3].getPhoneNumber())     # used for testing
    # print(contactsList[4].getEmail())           # used for testing
    # for cont in contactsList:                   # used for testing
    #     print(cont.getPhoneNumber())            # used for testing

    leadsList = [leads(email='kevin@keith.com'),
                 leads('Lucy', 'lucy@liu.com', 3210001112, True),
                 leads('Mary Middle', 'mary@middle.com', '(333)111-2223'),
                 leads(phoneNumber='444-222-3333'),
                 leads(email='ole@olson.com')]

    # leadsList[0].setStatus(True)               # used for testing
    # print(leadsList[0].getStatus())            # used for testing
    # print(leadsList[1].getPhoneNumber())       # used for testing
    # print(leadsList[1].getStatus())            # used for testing
    # print(leadsList[3].getPhoneNumber())       # used for testing
    # for lead in leadsList:                     # used for testing
    #     print(lead.getEmail())                 # used for testing

    registrants = '''
    {
      "registrant": [
        {
          "name": "Lucy Liu",
          "email": "lucy@liu.com",
          "phone": null
        },
        {
          "name":"Doug",
          "email":"doug@emmy.com",
          "phone":"4564445556"
        },
        {
          "name":"Uma Thurman",
          "email":"uma@thurs.com",
          "phone":null
        }
      ]
    }'''
    registrantData = json.loads(registrants)
    # print(registrantData)
    regList = list(registrantData['registrant'])
    dropList = []
    print(regList)
    for reg in regList:
        print(reg)
        for cont in contactsList:
            if reg['email'] != None and reg['email'] == cont.getEmail():
                dropList.append(reg)
                break
            if reg['phone'] != None and reg['phone'] == cont.getPhoneNumber():
                dropList.append(reg)
                break
        for lead in leadsList:
            if reg['email'] != None and reg['email'] == lead.getEmail():
                dropList.append(reg)
                break
            if reg['phone'] != None and reg['phone'] == lead.getPhoneNumber():
                dropList.append(reg)
                break
    # here i create a list of names that need to be dropped from the registrants in order to populate a list of
    # registrants that need to be added to contact list
    for matches in dropList:
        regList.remove(matches)
    # here i add the remaining registrants to contacts
    for remaining in regList:
        contactsList.append(contacts(name=remaining['name'], email=remaining['email'], phoneNumber=remaining['phone']))

    # for x in contactsList:       # see contacts
    #     print(x.getName(), x.getEmail(), x.getPhoneNumber())

if __name__ == '__main__':
    main()
