#!/usr/bin/env python3

from datetime import date
import yaml

with open('templates/index.html', 'r') as tmpfile:
    _mainTemplate = tmpfile.read()

HEADER = _mainTemplate.split('------')[0]
BODY = _mainTemplate.split('------')[1]
TESTTEMPLATE =  _mainTemplate.split('------')[2]
TESTFOOTER =  _mainTemplate.split('------')[3]
FOOTER =  _mainTemplate.split('------')[4]

myos = "UBPorts"
build_number = input("Build Number: ")
carrier = input("What carrier are you testing against? ")
mydate = str(date.today())
device = "PinePhone - CE UBPorts"
title = "{0} - {1} - {2}".format(mydate, myos, carrier)
magic_number = 0
build_stat = 'pass'
myTests = ''

try:
    with open('datasets.yaml', 'r') as tmptests:
        testCases = yaml.load(tmptests.read())
except Exception as e:
    print("Faild to load predefined test cases. \n {0}\n".format(e))
    exit(1)

for item in testCases['tests']:
    testblock = TESTTEMPLATE
    TESTNAME = item['name']
    TESTDESC = item['description']
    print("---------------------------------------------------------\n\n")
    print("{0}\n{1}\n".format(TESTNAME,TESTDESC))
    TESTNOTES = input("Notes: ")
    RESULTS = input("Final Results: (pass/fail/skip) ")
    testblock = testblock.replace('###TEST-NAME###', TESTNAME)
    testblock = testblock.replace('###TEST-DESCRIPTION###', TESTDESC)
    testblock = testblock.replace('###TEST-NOTES###', TESTNOTES)
    testblock = testblock.replace('###TEST-RESULTS###', RESULTS.upper())
    if RESULTS.upper().strip() == "PASS":
        testblock = testblock.replace('###RESULTS-COLOR###', 'tg-pass')
    elif  RESULTS.upper().strip() == "SKIP":
        testblock = testblock.replace('###RESULTS-COLOR###', 'tg-skip')
    else:
        testblock = testblock.replace('###RESULTS-COLOR###', 'tg-fail')
        build_stat = 'fail'
    myTests += testblock

while magic_number < 1:
    STOP = input("Do you have more tests? (y/n) ")
    if STOP == 'n':
        break
    testblock = TESTTEMPLATE
    TESTNAME = input("Test Name:  ")
    TESTDESC = input("Description: ")
    TESTNOTES = input("Notes: ")
    RESULTS = input("Final Results: (pass/fail/skip) ")
    testblock = testblock.replace('###TEST-NAME###', TESTNAME)
    testblock = testblock.replace('###TEST-DESCRIPTION###', TESTDESC)
    testblock = testblock.replace('###TEST-NOTES###', TESTNOTES)
    testblock = testblock.replace('###TEST-RESULTS###', RESULTS.upper())
    if RESULTS.upper().strip() == "PASS":
        testblock = testblock.replace('###RESULTS-COLOR###', 'tg-pass')
    elif  RESULTS.upper().strip() == "SKIP":
        testblock = testblock.replace('###RESULTS-COLOR###', 'tg-skip')
    else:
        testblock = testblock.replace('###RESULTS-COLOR###', 'tg-fail')
        build_stat = 'fail'
    myTests += testblock

HEADER = HEADER.replace("###TITLE###", title)
BODY = BODY.replace("###DEVICE###", device)
BODY = BODY.replace("###OS###", myos)
BODY = BODY.replace("###RESULT###", build_stat.upper())
BODY = BODY.replace("###BUILD###", build_number)
BODY = BODY.replace("###DATE###", mydate)

myDocument = HEADER + BODY + myTests + TESTFOOTER + FOOTER

with open("{0}/{1}-{2}.html".format(myos.lower(), mydate, carrier), 'w') as outfile:
    outfile.write(myDocument)

print("Done")
