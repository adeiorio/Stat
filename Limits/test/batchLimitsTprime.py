#!/usr/bin/env python
import os, commands
import string
import optparse 
from Stat.Limits.settings import *


usage = 'usage: %prog -r runNum'
parser = optparse.OptionParser(usage)

parser.add_option("-c","--channel",dest="ch",type="string",default="all",help="Indicate channels of interest. Default is all")
parser.add_option("-y","--years",dest="years",type="string",default="all",help="Indicate years of interest. Default is 2016")
parser.add_option("-d","--dir",dest="outdir",type="string",help="Outdir created by the analyseSamples")
parser.add_option('-m', '--method', dest='method', type='string', default = 'hist', help='Run a single method (hist, template)')
(opt, args) = parser.parse_args()

filename = "runBatch"
ext = ".csh"



if(not os.path.isdir("txt")): os.makedirs("txt")
workDir ="workDir/"
if(not os.path.isdir(workDir)): os.makedirs(workDir)



cmdCombine = "python runCombineSinglePoint.py --mZprime mZprime  -c channels -y years -m method -d outdir"

for point in sigpoints:

    mZprime=point
    
    newcmd = string.replace(cmdCombine, "-c channels", "-c " + opt.ch)
    newcmd = string.replace(newcmd, "-y years", "-y " + opt.years)
    newcmd = string.replace(newcmd, "--mZprime mZprime", "--mZprime " + mZprime)
    newcmd = string.replace(newcmd, "-m method", "-m " + opt.method)
    newcmd = string.replace(newcmd, "-d outdir", "-d " + opt.outdir)
    newcmd = string.replace(newcmd, "-M shape", "-M  " + opt.method)

    print "Command to execute ", newcmd                   

    sample = 'TprimeLH%s_%s' % (mZprime,  opt.method)
    jid = '%s' % (sample)


    cmd = 'qexe.py -w '+ os.getcwd()+"/"+workDir+'/'+opt.outdir + ' '+ jid+' -- '+newcmd
    print cmd
    os.system(cmd)

    



