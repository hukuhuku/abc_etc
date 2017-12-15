#xmlファイルを読みこみセッション番号,国名,種名で分け,
#fastaファイルとして出力するスクリプト

#これは国別

import xml.etree.ElementTree as ET
import sys

tree = ET.parse("arsa_result_1.xml")
root = tree.getroot()

for child in root:
    for grand in child:
        print(grand.tag)
        for e in grand:
            print("",e.tag)
            for k in e:
                print(" ",k.tag)



#https://www.biostars.org/p/48797/