#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import sys

class bcolor:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'        
    ENDC = '\033[0m'
    
def main():
    outfile = open(sys.argv[2], 'w')
    outfile.write('')
    outfile.close()
    outfile = open(sys.argv[2], 'a')
    file = open (sys.argv[1], 'r')

    for line in file:
        outfile.write('STRING {0}\n'.format(line.replace('\n', '')))
        outfile.write('DELAY 50\n')
        outfile.write('ENTER\n')
        outfile.write('DELAY {0}\n'.format(sys.argv[3]))
        
    file.close()
    outfile.close()
    print(bcolor.OKGREEN + 'FINISHED' + bcolor.ENDC)

def checkArg():
    argCount = 0
    for arg in sys.argv:
        argCount = argCount + 1
    if argCount == 4:
        return True
    else:
        return False
        
        
if checkArg() == False:
    print '\n'.join([
    	bcolor.OKBLUE,
    	'\n',
    	'USAGE: {0} + [INPUT SCRIPT] + [OUTPUT FILE] + [DELAY]'.format(sys.argv[0]),
    	'#################################################################',
    	'Input Script: As an example: .sh, .bat',
    	'Output File : You can Copy the Output where ever you want',
    	'Delay       : Default Delay between eyery Ducky Scrpit ¨STRING¨',
    	'              Delay in miliseconds like: 100, 150, 200, 250',
    	'#################################################################',
    	bcolor.ENDC
    	])
elif checkArg() == True:
    main()
    