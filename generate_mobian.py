#!/usr/bin/env python3

from datetime import date

with open('templates/index.html', 'r') as tmpfile:
    _mainTemplate = tmpfile.read()

HEADER = _mainTemplate.split('------')[0]
BODY = _mainTemplate.split('------')[1]
TESTTEMPLATE =  _mainTemplate.split('------')[2]
TESTFOOTER =  _mainTemplate.split('------')[3]
FOOTER =  _mainTemplate.split('------')[4]

myos = "Mobian"
build_number = input("Nightly Build Number: ")
mydate = str(date.today())
device = "PinePhone - CE UBPorts"
title = "{0} - {1} ".format(mydate, myos)
magic_number = 0

myTests = ''

while magic_number < 1:
    testblock = TESTTEMPLATE
    TESTNAME = input("Test Name:  ")
    TESTDESC = input("Description: ")
    TESTNOTES = input("Notes: ")
    RESULTS = input("Final Results: ")
    STOP = input("Do you have more tests? (y/n) ")
    if STOP == 'n':
        magic_number = 2
    testblock = testblock.replace('###TEST-NAME###', TESTNAME)
    testblock = testblock.replace('###TEST-DESCRIPTION###', TESTDESC)
    testblock = testblock.replace('###TEST-NOTES###', TESTNOTES)
    testblock = testblock.replace('###TEST-RESULTS###', RESULTS.upper())
    if RESULTS.upper().strip() == "PASS":
        testblock = testblock.replace('###RESULTS-COLOR###', 'tg-pass')
    else:
        testblock = testblock.replace('###RESULTS-COLOR###', 'tg-fail')
    myTests += testblock

HEADER = HEADER.replace("###TITLE###", title)
BODY = BODY.replace("###DEVICE###", device)
BODY = BODY.replace("###OS###", myos)
BODY = BODY.replace("###BUILD###", build_number)
BODY = BODY.replace("###DATE###", mydate)

myDocument = HEADER + BODY + myTests + TESTFOOTER + FOOTER

with open("{0}/{1}.html".format(myos.lower(), mydate), 'w') as outfile:
    outfile.write(myDocument)

print("Done")
