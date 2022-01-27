import os

folder = '19Jen22_dd_summedyears_SR_explin_v18_LH_wp30'
year = '2020'
histo_rep = '/eos/user/a/adeiorio/Wprime/nosynch/v17/plot_fit_ddsummed_explin_bis/'
histo_rep = '/eos/user/a/adeiorio/Wprime/nosynch/v17/plot_fit_ddsummed_explin_v4/'
histo_rep = '/eos/home-o/oiorio/Wprime/nosynch/v18/plot_explin_fit/'
histo_rep = '/eos/user/a/adeiorio/Wprime/nosynch//v18/plot_fit/'
fit = 1
fit_diag = 0
impact = 0
pull = 0
gof = 0
unblind = 0

if fit:
    if unblind:
        os.system('python collectHistos.py -i ' + histo_rep + ' -o histo' + str(year) + '.root -u')
        os.system('python createDatacards.py -i histo' + str(year) + '.root -d  ' + folder + ' -u')
        #python runCombine.py -c SR_$year -y $year -d  ' + folder + ' --runSingleCat -m hist
        os.system('python runCombine.py -y ' + str(year) + ' -d ' + folder + ' -m hist') #--runSingleCat
        os.system('python getLimitData.py -d ' + folder) #--runSingleCat
        os.system('python brazilPlot.py  -l ' + folder + ' -o' + ' -y ' + str(year)) #--runSingleCat
    else:
        #os.system('python collectHistos.py -i ' + histo_rep + ' -o histo' + str(year) + '.root')
        os.system('python createDatacards.py -i histo' + str(year) + '.root -d  ' + folder)
        #python runCombine.py -c SR_$year -y $year -d  ' + folder + ' --runSingleCat -m hist
        os.system('python runCombine.py -y ' + str(year) + ' -d ' + folder + ' -m hist') #--runSingleCat
        os.system('python getLimitData.py -d ' + folder) #--runSingleCat
        os.system('python brazilPlot.py  -l ' + folder + ' -y ' + str(year)) #--runSingleCat

signal = 'WP_M4000W40_RH'
metadatacard_out = folder + '/' + signal +'/'+ signal + '_hist'

#do fit diagonistics
if fit_diag:
    os.system("combine -M FitDiagnostics " + metadatacard_out + ".txt --saveShapes --saveWithUncertainties --plots --saveNormalizations --robustFit 1 --customStartingPoint --stepSize 0.004 --out " + folder + " --profilingMode all --keepFailures  --autoBoundsPOIs r")

if pull:
    print "Making pull distributions ..."
    os.system("./make_pulls.sh " + folder +"/fitDiagnostics.root")
    os.system("cat pulls.txt")
    os.system("python pulls.py -f pulls.txt")
    os.system("mv pulls.txt "+folder+"/pulls_"+ signal + ".txt") 
    os.system("mv pulls.tex "+folder+"/pulls_"+ signal + ".tex") 
    os.system("mv pulls_no_binbybin.png "+folder+"/pulls_"+ signal +".png") 
    os.system("mv rho_no_binbybin.png "+folder+"/rho_"+ signal + ".png")
    os.system("mv pulls_no_binbybin.pdf "+folder+"/pulls_"+ signal + ".pdf") 
    os.system("mv rho_no_binbybin.pdf "+folder+"/rho_"+ signal + ".pdf")
    #os.system("python rateParam.py -L "+folder+" "+opt.lep+"/mlfit.root >& "+opt.lep+"/infoPF_"+ signal + "_"+opt.lep+".log ")
    #os.system("cat "+opt.lep+"/infoPF_"+ signal + "_"+opt.lep+".log")

# do impact plot?
if impact:
    os.system('text2workspace.py ' + metadatacard_out + '.txt -m 125')
    fit_option = '--autoBoundsPOIs r  --autoRange 1 '
    os.system("combineTool.py -M Impacts -d  " + metadatacard_out + ".root -m 125 --robustFit 1 --doInitialFit " + fit_option) # 
    os.system("combineTool.py -M Impacts -d  " + metadatacard_out + ".root -m 125 --robustFit 1 --doFits " + fit_option) #--autoBoundsPOIs r  --autoRange 1 --parallel 4
    os.system("combineTool.py -M Impacts -d  " + metadatacard_out + ".root -m 125 -o prova.json")
    os.system("plotImpacts.py -i prova.json -o impacts")
    os.system("rm prova.json")
    #os.system("mv impacts.pdf "+opt.lep+"/impacts_"+ signal + "_"+opt.lep+".pdf")

# do gof test?
suffix = folder
ntoys = 500
xmax = 180
if gof:
    os.system("combine -M GoodnessOfFit " + metadatacard_out + ".txt --algo=saturated --toysFrequentist --bypassFrequentistFit -n gof_data_" + suffix + " --rMax 250 --rMin -250")
    os.system("combine -M GoodnessOfFit " + metadatacard_out + ".txt --algo=saturated -t " + str(ntoys) + " --toysFrequentist --bypassFrequentistFit -n gof_" + suffix + " --rMax 250 --rMin -250")
    os.system('python drawgof.py -s ' + suffix + ' --xmax ' + str(xmax))
