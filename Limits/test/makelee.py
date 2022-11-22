import ROOT
import os,time
import optparse


usage = 'usage: %prog [--cat N]'
parser = optparse.OptionParser(usage)
parser.add_option("-m","--mode",dest="mode",type="string",default="gfr",help="mode: g(generate), f(fit) r(read) F(fitparallel: not compatible with r)")
parser.add_option("-s","--suffix",dest="suffix",type="string",default="v18N",help="suffix for the files")
#parser.add_option("-d","--datacarddir",dest="datacarddir",type="string",default="an_v17_tercentral",help="datacard directory")
#parser.add_option("-d","--datacarddir",dest="datacarddir",type="string",default="5May22_SRNW_RH_systsall_unblind_QCDsmooth",help="datacard directory")
parser.add_option("-d","--datacarddir",dest="datacarddir",type="string",default="22Jun22_SRNW_RH_systsall_unblind_MCstats_shapeN",help="datacard directory")
parser.add_option("-n","--npseudoexperiments",dest="npe",type="string",default="100",help="number of pseudoexperiments to throw")
parser.add_option("-b","--basepe",dest="base",type="int",default=1,help="starting number of pe")
(opt, args) = parser.parse_args()

mode= opt.mode
masses = [str(2*x) for x in range(10,31)]
print (masses)
verbose=False
generate=False

fit=False
parallelfit=False

read=False
saveplots=False

readmean=False

if "g" in mode:
    generate=True
if "f" in mode:
    fit=True
if "F" in mode:
    fit=True
    parallelfit=True
if "r" in mode:
    read=True
if "m" in mode:
    readmean=True
if "R" in mode:
    read=True
    saveplots=True
datacarddir="outstatNovtestwFull"
datacarddir=opt.datacarddir

suffix=""
suffix=opt.suffix

npe="100" #number of pseudoexperiments
npe=int(opt.npe)
signifs=[]

datacardinit=datacarddir+"/WP_M4000W40_RH/WP_M4000W40_RH_hist.txt" 
#combination/fit_v16/Combination_Tprime_Run2_v16/combination_Tprime700.txt
#datacardinit=datacarddir+"/combination_Tprime700.txt"

base=1
base = opt.base
for n in xrange(base,npe+base): 
    if generate:
        commandgen=" combine -M GenerateOnly "+datacardinit+"  --toysFrequentist  -t 1 --saveToys --expectSignal 0 -n _toys_bonly"+suffix+" --rMax 150 --rMin -1000 -s "+str(n) #--bypassFrequentistFit
#       print commandgen
        os.system(commandgen)

    for mi in xrange(0,len(masses)):
        m = masses[mi]            
        r=1 
        commandsignif ="combine -M Significance "+datacarddir+"/WP_M"+(m)+"00W"+str(m)+"_RH/WP_M"+(m)+"00W"+str(m)+"_RH_hist.txt -n _signif_seed_"+str(n)+" --toysFile  higgsCombine_toys_bonly"+suffix+".GenerateOnly.mH120."+str(n)+".root -m "+str(m)+" -t 1 --usePLC"
    
        if(parallelfit and mi < len(masses)-1):commandsignif = commandsignif+" &"
        print commandsignif
        if(fit):os.system(commandsignif)
    if(parallelfit):time.sleep(10)
    cmdhadd = "hadd -f signifs_seed_"+str(n)+"_"+suffix+".root higgsCombine_signif_seed_"+str(n)+".Significance.mH*.123456.root"
    cmdrm = "rm higgsCombine_signif_seed_"+str(n)+".Significance.mH*.123456.root"
    if(fit):
        print ""
        os.system(cmdhadd)
        os.system(cmdrm)


if(read):
    fout= ROOT.TFile.Open("signifs_tot_"+suffix+str(base)+"to"+str(base+npe-1)+".root","RECREATE")
    maxSignif = ROOT.TH1D("maxSignifs","maxSignifs",1000,0,10) 
    for n in xrange(base,npe+base): 
        f= ROOT.TFile.Open("signifs_seed_"+str(n)+"_"+suffix+".root")
        t = f.Get("limit")
        tempmax = t.GetMaximum("limit")
        maxSignif.Fill(tempmax)
    fout.cd()
    maxSignif.Write()
                
