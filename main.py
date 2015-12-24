import parser
import sys
def main():
        filename = input("enter your file name")
        file = open(filename)
        f=file.read()
        print (f)		
        for token in lexrepars.tokenize(f):
                                
                 print ("value:",token["value"],",type:",token["type"],",line:",token["line"],",column:",token["column"])
        else:
                print ('Invalid parameters.\n')
        sys.exit(1)
        file.close()
main()
