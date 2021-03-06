#1500
combine -M GenerateOnly outstatNovtestwFull/TprimeLH1500/TprimeLH1500_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 75 -n r_75_1500_toys_testw --rMax 150
combine -M FitDiagnostics outstatNovtestwFull/TprimeLH1500/TprimeLH1500_hist.txt --skipBOnlyFit -t 100 -n r_75_1500_toys_testw --toysFile higgsCombiner_75_1500_toys_testw.GenerateOnly.mH120.123456.root --rMax 150 &

combine -M GenerateOnly outstatNovtestwFull/TprimeLH1500/TprimeLH1500_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 5 -n r_5_1500_toys_testw --rMax 100
combine -M FitDiagnostics outstatNovtestwFull/TprimeLH1500/TprimeLH1500_hist.txt --skipBOnlyFit -t 100 -n r_5_1500_toys_testw --toysFile higgsCombiner_5_1500_toys_testw.GenerateOnly.mH120.123456.root --rMax 100 &

combine -M GenerateOnly outstatNovtestwFull/TprimeLH1500/TprimeLH1500_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 18 -n r_18_1500_toys_testw --rMax 100
combine -M FitDiagnostics outstatNovtestwFull/TprimeLH1500/TprimeLH1500_hist.txt --skipBOnlyFit -t 100 -n r_18_1500_toys_testw --toysFile higgsCombiner_18_1500_toys_testw.GenerateOnly.mH120.123456.root --rMax 100 &

combine -M GenerateOnly outstatNovtestwFull/TprimeLH1500/TprimeLH1500_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 35 -n r_35_1500_toys_testw --rMax 100
combine -M FitDiagnostics outstatNovtestwFull/TprimeLH1500/TprimeLH1500_hist.txt --skipBOnlyFit -t 100 -n r_35_1500_toys_testw --toysFile higgsCombiner_35_1500_toys_testw.GenerateOnly.mH120.123456.root --rMax 100 &

combine -M GenerateOnly outstatNovtestwFull/TprimeLH1500/TprimeLH1500_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 0 -n r_0_1500_toys_testw --rMax 100 --rMin -100
combine -M FitDiagnostics outstatNovtestwFull/TprimeLH1500/TprimeLH1500_hist.txt --skipBOnlyFit -t 100 -n r_0_1500_toys_testw --toysFile higgsCombiner_0_1500_toys_testw.GenerateOnly.mH120.123456.root --rMax 100 --rMin -100 &

#combine -M GenerateOnly outstatNovtestwFull/TprimeLH1300/TprimeLH1300_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 75 -n r_75_1300_toys_testw --rMax 150
#combine -M FitDiagnostics outstatNovtestwFull/TprimeLH1300/TprimeLH1300_hist.txt --skipBOnlyFit -t 100 -n r_75_1300_toys_testw --toysFile higgsCombiner_75_1300_toys_testw.GenerateOnly.mH120.123456.root --rMax 150 &

#combine -M GenerateOnly outstatNovtestwFull/TprimeLH1300/TprimeLH1300_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 35 -n r_35_1300_toys_testw --rMax 100
#combine -M FitDiagnostics outstatNovtestwFull/TprimeLH1300/TprimeLH1300_hist.txt --skipBOnlyFit -t 100 -n r_35_1300_toys_testw --toysFile higgsCombiner_35_1300_toys_testw.GenerateOnly.mH120.123456.root --rMax 100 &

#combine -M GenerateOnly outstatNovtestwFull/TprimeLH1300/TprimeLH1300_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 0 -n r_0_1300_toys_testw --rMax 100 --rMin -100
#combine -M FitDiagnostics outstatNovtestwFull/TprimeLH1300/TprimeLH1300_hist.txt --skipBOnlyFit -t 100 -n r_0_1300_toys_testw --toysFile higgsCombiner_0_1300_toys_testw.GenerateOnly.mH120.123456.root --rMax 100 --rMin -100 &

#700
combine -M GenerateOnly outstatNovtestwFull/TprimeLH700/TprimeLH700_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 10 -n r_10_700_toys_testw --rMax 150
combine -M FitDiagnostics outstatNovtestwFull/TprimeLH700/TprimeLH700_hist.txt --skipBOnlyFit -t 100 -n r_10_700_toys_testw --toysFile higgsCombiner_10_700_toys_testw.GenerateOnly.mH120.123456.root --rMax 150 &

combine -M GenerateOnly outstatNovtestwFull/TprimeLH700/TprimeLH700_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 30 -n r_30_700_toys_testw --rMax 150
combine -M FitDiagnostics outstatNovtestwFull/TprimeLH700/TprimeLH700_hist.txt --skipBOnlyFit -t 100 -n r_30_700_toys_testw --toysFile higgsCombiner_30_700_toys_testw.GenerateOnly.mH120.123456.root --rMax 150 &

combine -M GenerateOnly outstatNovtestwFull/TprimeLH700/TprimeLH700_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 120 -n r_120_700_toys_testw --rMax 150
combine -M FitDiagnostics outstatNovtestwFull/TprimeLH700/TprimeLH700_hist.txt --skipBOnlyFit -t 100 -n r_120_700_toys_testw --toysFile higgsCombiner_120_700_toys_testw.GenerateOnly.mH120.123456.root --rMax 150 &

combine -M GenerateOnly outstatNovtestwFull/TprimeLH700/TprimeLH700_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 75 -n r_75_700_toys_testw --rMax 100
combine -M FitDiagnostics outstatNovtestwFull/TprimeLH700/TprimeLH700_hist.txt --skipBOnlyFit -t 100 -n r_75_700_toys_testw --toysFile higgsCombiner_75_700_toys_testw.GenerateOnly.mH120.123456.root --rMax 100 &

combine -M GenerateOnly outstatNovtestwFull/TprimeLH700/TprimeLH700_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 0 -n r_0_700_toys_testw --rMax 100 --rMin -100
combine -M FitDiagnostics outstatNovtestwFull/TprimeLH700/TprimeLH700_hist.txt --skipBOnlyFit -t 100 -n r_0_700_toys_testw --toysFile higgsCombiner_0_700_toys_testw.GenerateOnly.mH120.123456.root --rMax 100 --rMin -100&

##11000
combine -M GenerateOnly outstatNovtestwFull/TprimeLH1100/TprimeLH1100_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 5 -n r_5_1100_toys_testw --rMax 150
combine -M FitDiagnostics outstatNovtestwFull/TprimeLH1100/TprimeLH1100_hist.txt --skipBOnlyFit -t 100 -n r_5_1100_toys_testw --toysFile higgsCombiner_5_1100_toys_testw.GenerateOnly.mH120.123456.root --rMax 150 &

combine -M GenerateOnly outstatNovtestwFull/TprimeLH1100/TprimeLH1100_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 10 -n r_10_1100_toys_testw --rMax 150
combine -M FitDiagnostics outstatNovtestwFull/TprimeLH1100/TprimeLH1100_hist.txt --skipBOnlyFit -t 100 -n r_10_1100_toys_testw --toysFile higgsCombiner_10_1100_toys_testw.GenerateOnly.mH120.123456.root --rMax 150 &

combine -M GenerateOnly outstatNovtestwFull/TprimeLH1100/TprimeLH1100_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 50 -n r_50_1100_toys_testw --rMax 150
combine -M FitDiagnostics outstatNovtestwFull/TprimeLH1100/TprimeLH1100_hist.txt --skipBOnlyFit -t 100 -n r_50_1100_toys_testw --toysFile higgsCombiner_50_1100_toys_testw.GenerateOnly.mH120.123456.root --rMax 150 &

combine -M GenerateOnly outstatNovtestwFull/TprimeLH1100/TprimeLH1100_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 35 -n r_35_1100_toys_testw --rMax 100
combine -M FitDiagnostics outstatNovtestwFull/TprimeLH1100/TprimeLH1100_hist.txt --skipBOnlyFit -t 100 -n r_35_1100_toys_testw --toysFile higgsCombiner_35_1100_toys_testw.GenerateOnly.mH120.123456.root --rMax 100 &

combine -M GenerateOnly outstatNovtestwFull/TprimeLH1100/TprimeLH1100_hist.txt  --toysFrequentist --bypassFrequentistFit -t 100 --saveToys --expectSignal 0 -n r_0_1100_toys_testw --rMax 100 --rMin -100
combine -M FitDiagnostics outstatNovtestwFull/TprimeLH1100/TprimeLH1100_hist.txt --skipBOnlyFit -t 100 -n r_0_1100_toys_testw --toysFile higgsCombiner_0_1100_toys_testw.GenerateOnly.mH120.123456.root --rMax 100 --rMin -100 &

