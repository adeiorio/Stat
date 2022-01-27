import collections

#*********************************
#                                *
#       List of channels         *
#                                *
#*********************************
### List of histos to include in the root files
histos = { "SR":"h_jets_best_Wprime_m_selection_AND_best_topjet_isbtag_AND_best_Wpjet_isbtag_AND_best_top_m_G_120_AND_best_top_m_L_220_AND_deltaR_bestWAK4_closestAK8_L_0p4_AND_WprAK8_mSD_L_60", "CRTT":"h_jets_best_Wprime_m_selection_AND_best_topjet_isbtag_AND_best_Wpjet_isbtag_EQ_0_AND_best_top_m_G_120_AND_best_top_m_L_220_AND_deltaR_bestWAK4_closestAK8_L_0p4_AND_WprAK8_mSD_L_60", "CRWJ":"h_jets_best_Wprime_m_selection_AND_best_topjet_isbtag_EQ_0_AND_best_Wpjet_isbtag_AND_best_top_m_G_120_AND_best_top_m_L_220_AND_deltaR_bestWAK4_closestAK8_L_0p4_AND_WprAK8_mSD_L_60",
"CR0B":"h_jets_best_Wprime_m_selection_AND_best_topjet_isbtag_EQ_0_AND_best_Wpjet_isbtag_EQ_0_AND_nbjet_pt100_EQ_0_AND_best_top_m_G_120_AND_best_top_m_L_220_AND_deltaR_bestWAK4_closestAK8_L_0p4_AND_WprAK8_mSD_L_60"
}
histos = { "SR":"h_jets_best_Wprime_m_SR2B", "CRTT":"h_jets_best_Wprime_m_SRT", "CRWJ":"h_jets_best_Wprime_m_SRW",
"CR0B":"h_jets_best_Wprime_m_CR0B"
}

### List of regions for which creating the datacards
channels = ["SR_muon", "CRTT_muon", "CRWJ_muon", "SR_electron", "CRTT_electron", "CRWJ_electron"]
leptons = ['muon', 'electron']
#leptons = ['muon']
#channels = ["CR0B_muon", "CR0B_electron", "SR_muon", "CRTT_muon", "CRWJ_muon", "SR_electron", "CRTT_electron", "CRWJ_electron"]
#channels = ["CR0B_muon", "CR0B_electron"]
#leptons = ['muon', 'electron']
#channels = ["CR0B_muon"]
#leptons = ['muon']
#channels = ["CR0B_electron"]
#leptons = ['electron']

channels_labels = {"SR":"Signal region", "CRTT":"\ttbar Control region", "CRWJ":"wjets Control region"}
#channels_labels = {"CR0B":"0 b-jet control region"}

class rateParam(object):
    pass

rateParams = {}
'''
DD_rate_2016 = rateParam()
DD_rate_2016.chs = channels
DD_rate_2016.bkg = "DDFitWJetsTT_MttST"
rateParams["DD_rate_2016"] = DD_rate_2016

DD_mu_rate_2017 = rateParam()
DD_mu_rate_2017.chs = channels
DD_mu_rate_2017.bkg = "DDFitWJetsTT_MttST"
rateParams["DD_mu_rate_2017"] = DD_mu_rate_2017

DD_mu_rate_2018 = rateParam()
DD_mu_rate_2018.chs = channels
DD_mu_rate_2018.bkg = "DDFitWJetsTT_MttST"
rateParams["DD_mu_rate_2018"] = DD_mu_rate_2018

DD_ele_rate_2017 = rateParam()
DD_ele_rate_2017.chs = channels
DD_ele_rate_2017.bkg = "DDFitWJetsTT_MttST"
rateParams["DD_ele_rate_2017"] = DD_ele_rate_2017

DD_ele_rate_2018 = rateParam()
DD_ele_rate_2018.chs = channels
DD_ele_rate_2018.bkg = "DDFitWJetsTT_MttST"
rateParams["DD_ele_rate_2018"] = DD_ele_rate_2018
'''
DD_mu_rate_2020 = rateParam()
DD_mu_rate_2020.chs = channels
DD_mu_rate_2020.bkg = "DDFitWJetsTT_MttST"
rateParams["DD_mu_rate"] = DD_mu_rate_2020

#qcd_mu_rate_2020 = rateParam()
#qcd_mu_rate_2020.chs = channels
#qcd_mu_rate_2020.bkg = "QCD"
#rateParams["qcd_mu_rate"] = qcd_mu_rate_2020

DD_ele_rate_2020 = rateParam()
DD_ele_rate_2020.chs = channels
DD_ele_rate_2020.bkg = "DDFitWJetsTT_MttST"
rateParams["DD_ele_rate"] = DD_ele_rate_2020


#TT_rate = rateParam()
#TT_rate.chs = ["SR_muon", "CRTT_muon", "CRWJ_muon", "SR_electron", "CRTT_electron", "CRWJ_electron"]
#TT_rate.bkg = "TT_Mtt"
#rateParams["TT_rate"] = TT_rate

#WJ_rate = rateParam()
#WJ_rate.chs = ["SR_muon", "CRTT_muon", "CRWJ_muon", "SR_electron", "CRTT_electron", "CRWJ_electron"]
#WJ_rate.bkg = "WJets"
#rateParams["WJ_rate"] = WJ_rate

#*********************************
#                                *
#       List of backgrounds      *
#                                *
#*********************************
processes = ["ST", "QCD", "TT_Mtt", "WJets"]
#processes = ["ST", "QCD", "DDWJetsTT_Mtt"]
processes = ["QCD", "DDFitWJetsTT_MttST"]
bkgs = []

#*********************************
#                                *
#       List of systematics      *
#                                *
#*********************************
syst = collections.OrderedDict()
#syst["lumi_2016"] = ["lnN", "all", 1.025]
#syst["lumi_2017"] = ["lnN", "all", 1.023]
#syst["lumi_2018"] = ["lnN", "all", 1.025]
syst["lumi"] = ["lnN", ("QCD"), 1.018]
syst["qcd_rate"] = ["lnN", ("QCD"), 1.25]
#syst["DD_rate"] = ["lnN", ("DDFitWJetsTT_MttST"), 1.25]
''' #systs for MC 2020
syst["jes2016"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["jer2016"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["lep2016"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["trig2016"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["PF2016"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["btag2016"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["mistag2016"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["jes2017"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["jer2017"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["lep2017"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["trig2017"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["PF2017"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["btag2017"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["mistag2017"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["jes2018"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["jer2018"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["lep2018"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["trig2018"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["PF2018"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["btag2018"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
syst["mistag2018"] = ["shape", ("QCD", "TT_Mtt", "WJets", "ST", "sig")]
'''

''' #systs for dd in separate years
syst["PF"] = ["shape", ("QCD",  "sig")]
syst["pu"] = ["shape", ("QCD",  "sig")]
syst["lep"] = ["shape", ("QCD",  "sig")]
syst["trig"] = ["shape", ("QCD",  "sig")]
syst["jes"] = ["shape", ("QCD",  "sig")]
syst["jer"] = ["shape", ("QCD",  "sig")]
syst["btag"] = ["shape", ("QCD",  "sig")]
syst["mistag"] = ["shape", ("QCD",  "sig")]
syst["pdf_total"] = ["shape", ("QCD",  "sig")]

syst["TT_Mtt"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["WJets"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["ST"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["TF_mu_2016"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["DD_mu_2016"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["Alt_mu_2016"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["TF_mu_2017"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["DD_mu_2017"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["Alt_mu_2017"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["TF_mu_2018"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["DD_mu_2018"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["Alt_mu_2018"] = ["shape", ("DDFitWJetsTT_MttST")]

syst["TF_ele_2016"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["DD_ele_2016"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["Alt_ele_2016"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["TF_ele_2017"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["DD_ele_2017"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["Alt_ele_2017"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["TF_ele_2018"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["DD_ele_2018"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["Alt_ele_2018"] = ["shape", ("DDFitWJetsTT_MttST")]
#syst["AltBis_2018"] = ["shape", ("DDFitWJetsTT_MttST")]
'''

syst["PF"] = ["shape", ( "sig")]
syst["pu"] = ["shape", ( "sig")]
syst["lep_ele"] = ["shape", ( "sig")]
syst["lep_mu"] = ["shape", ( "sig")]
syst["trig_ele"] = ["shape", ( "sig")]
syst["trig_mu"] = ["shape", ( "sig")]
syst["jes"] = ["shape", ( "sig")]
syst["jer"] = ["shape", ( "sig")]
syst["btag"] = ["shape", ( "sig")]
syst["mistag"] = ["shape", ( "sig")]
#syst["pdf_total"] = ["shape", ( "sig")]

syst["Altmu"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["Altele"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["DDmu"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["DDele"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["TFmu"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["TFele"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["TT_Mtt_mu"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["TT_Mtt_ele"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["WJets_mu"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["WJets_ele"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["ST_mu"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["ST_ele"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["AltTFmu"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["AltTFele"] = ["shape", ("DDFitWJetsTT_MttST")]
#syst["CFmu"] = ["shape", ("DDFitWJetsTT_MttST")]
#syst["CFele"] = ["shape", ("DDFitWJetsTT_MttST")]

years = ["2020"]
#years = ["2016","2017","2018"]
'''
splityearjes=False
#splityearjes=True
if(splityearjes):
    for y in ys:
        #if(y=="2016"):syst["jer"+y] = ["shape", [ sigTTW]] #No QCD : low stat
        if(y=="2016"):syst["jes"+y] = ["shape", ["sig", sigZ, sigTTW, "SingleTop" ]] #No QCD : low stat
        if(y!="2016"):syst["jer"+y] = ["shape", ["sig", sigZ, sigTTW, "SingleTop"]] #No QCD : low stat
if(not splityearjes):
    syst["jes"] = ["shape", ["sig", sigTTW, sigZ, "SingleTop"]] #No QCD : low stat
    syst["jer"] = ["shape", ["sig", sigTTW, sigZ, "SingleTop"]] #No QCD : low stat
'''

#*********************************
#                                *
#         List of signals        *
#                                *
#*********************************

#*********************************************************#
#                                                         #
#                  Right-Handed samples                   #
#                                                         #
#*********************************************************#
RHvec1 = ("2000", "20", "RH")
RHvec2 = ("2200", "22", "RH")
RHvec3 = ("2400", "24", "RH")
RHvec4 = ("2600", "26", "RH")
RHvec5 = ("2800", "28", "RH")
RHvec6 = ("3000", "30", "RH")
RHvec7 = ("3200", "32", "RH")
RHvec8 = ("3400", "34", "RH")
RHvec9 = ("3600", "36", "RH")
RHvec10 = ("3800", "38", "RH")
RHvec11 = ("4000", "40", "RH")
RHvec12 = ("4200", "42", "RH")
RHvec13 = ("4400", "44", "RH")
RHvec14 = ("4600", "46", "RH")
RHvec15 = ("4800", "48", "RH")
RHvec16 = ("5000", "50", "RH")
RHvec17 = ("5200", "52", "RH")
RHvec18 = ("5400", "54", "RH")
RHvec19 = ("5600", "56", "RH")
RHvec20 = ("5800", "58", "RH")
RHvec21 = ("6000", "60", "RH")
RHsigpointsNW = [RHvec1, RHvec2, RHvec3, RHvec4, RHvec5, RHvec6, RHvec7, RHvec8, RHvec9, RHvec10, RHvec11, RHvec12, RHvec13, RHvec14, RHvec15, RHvec16, RHvec17, RHvec18, RHvec19, RHvec20, RHvec21]

RHvec0wp10 = ("2000", "200", "RH")
RHvec1wp10 = ("2400", "240", "RH")
RHvec2wp10 = ("2800", "280", "RH")
RHvec3wp10 = ("3200", "320", "RH")
RHvec4wp10 = ("3600", "360", "RH")
RHvec5wp10 = ("4000", "400", "RH")
RHvec6wp10 = ("4400", "440", "RH")
RHvec7wp10 = ("4800", "480", "RH")
RHvec8wp10 = ("5200", "520", "RH")
RHvec9wp10 = ("5600", "560", "RH")
RHvec10wp10 = ("6000", "600", "RH")
RHsigspointswp10 = [RHvec0wp10, RHvec1wp10, RHvec2wp10, RHvec3wp10, RHvec4wp10, RHvec6wp10, RHvec7wp10, RHvec8wp10, RHvec9wp10, RHvec10wp10] # RHvec5wp10,

RHvec0wp20 = ("2000", "400", "RH")
RHvec1wp20 = ("2400", "480", "RH")
RHvec2wp20 = ("2800", "560", "RH")
RHvec3wp20 = ("3200", "640", "RH")
RHvec4wp20 = ("3600", "720", "RH")
RHvec5wp20 = ("4000", "800", "RH")
RHvec6wp20 = ("4400", "880", "RH")
RHvec7wp20 = ("4800", "960", "RH")
RHvec8wp20 = ("5200", "1040", "RH")
RHvec9wp20 = ("5600", "1120", "RH")
RHvec10wp20 = ("6000", "1200", "RH")
RHsigspointswp20 = [RHvec0wp20, RHvec2wp20, RHvec3wp20, RHvec4wp20, RHvec5wp20, RHvec6wp20, RHvec7wp20, RHvec8wp20, RHvec9wp20, RHvec10wp20]# RHvec1wp20,

RHvec0wp30 = ("2000", "600", "RH")
RHvec1wp30 = ("2400", "720", "RH")
RHvec2wp30 = ("2800", "840", "RH")
RHvec3wp30 = ("3200", "960", "RH")
RHvec4wp30 = ("3600", "1080", "RH")
RHvec5wp30 = ("4000", "1200", "RH")
RHvec6wp30 = ("4400", "1320", "RH")
RHvec7wp30 = ("4800", "1440", "RH")
RHvec8wp30 = ("5200", "1560", "RH")
RHvec9wp30 = ("5600", "1680", "RH")
RHvec10wp30 = ("6000", "1800", "RH")
RHsigspointswp30 = [RHvec0wp30, RHvec1wp30, RHvec2wp30, RHvec3wp30, RHvec4wp30, RHvec5wp30, RHvec7wp30, RHvec8wp30, RHvec9wp30, RHvec10wp30]# RHvec6wp30,

#*********************************************************#
#                                                         #
#                   Left-Handed samples                   #
#                                                         #
#*********************************************************#
LHvec1 = ("2000", "20", "LHSMinter")
LHvec2 = ("2200", "22", "LHSMinter")
LHvec3 = ("2400", "24", "LHSMinter")
LHvec4 = ("2600", "26", "LHSMinter")
LHvec5 = ("2800", "28", "LHSMinter")
LHvec6 = ("3000", "30", "LHSMinter")
LHvec7 = ("3200", "32", "LHSMinter")
LHvec8 = ("3400", "34", "LHSMinter")
LHvec9 = ("3600", "36", "LHSMinter")
LHvec10 = ("3800", "38", "LHSMinter")
LHvec11 = ("4000", "40", "LHSMinter")
LHvec12 = ("4200", "42", "LHSMinter")
LHvec13 = ("4400", "44", "LHSMinter")
LHvec14 = ("4600", "46", "LHSMinter")
LHvec15 = ("4800", "48", "LHSMinter")
LHvec16 = ("5000", "50", "LHSMinter")
LHvec17 = ("5200", "52", "LHSMinter")
LHvec18 = ("5400", "54", "LHSMinter")
LHvec19 = ("5600", "56", "LHSMinter")
LHvec20 = ("5800", "58", "LHSMinter")
LHvec21 = ("6000", "60", "LHSMinter")
LHsigpointsNW = [LHvec1, LHvec2, LHvec3, LHvec4, LHvec5, LHvec6, LHvec7, LHvec10, LHvec11, LHvec12, LHvec13, LHvec14, LHvec15, LHvec16, LHvec17, LHvec18, LHvec19] # LHvec8, LHvec9,, LHvec20, LHvec21

LHvec0wp10 = ("2000", "200", "LHSMinter")
LHvec1wp10 = ("2400", "240", "LHSMinter")
LHvec2wp10 = ("2800", "280", "LHSMinter")
LHvec3wp10 = ("3200", "320", "LHSMinter")
LHvec4wp10 = ("3600", "360", "LHSMinter")
LHvec5wp10 = ("4000", "400", "LHSMinter")
LHvec6wp10 = ("4400", "440", "LHSMinter")
LHvec7wp10 = ("4800", "480", "LHSMinter")
LHvec8wp10 = ("5200", "520", "LHSMinter")
LHvec9wp10 = ("5600", "560", "LHSMinter")
LHvec10wp10 = ("6000", "600", "LHSMinter")
LHsigspointswp10 = [LHvec0wp10, LHvec2wp10, LHvec4wp10, LHvec6wp10, LHvec8wp10, LHvec10wp10] # LHvec1wp10, LHvec3wp10, LHvec5wp10, LHvec7wp10, LHvec9wp10,

LHvec0wp20 = ("2000", "400", "LHSMinter")
LHvec1wp20 = ("2400", "480", "LHSMinter")
LHvec2wp20 = ("2800", "560", "LHSMinter")
LHvec3wp20 = ("3200", "640", "LHSMinter")
LHvec4wp20 = ("3600", "720", "LHSMinter")
LHvec5wp20 = ("4000", "800", "LHSMinter")
LHvec6wp20 = ("4400", "880", "LHSMinter")
LHvec7wp20 = ("4800", "960", "LHSMinter")
LHvec8wp20 = ("5200", "1040", "LHSMinter")
LHvec9wp20 = ("5600", "1120", "LHSMinter")
LHvec10wp20 = ("6000", "1200", "LHSMinter")
LHsigspointswp20 = [LHvec0wp20, LHvec6wp20, LHvec8wp20, LHvec10wp20]# LHvec1wp20, LHvec2wp20, LHvec3wp20, LHvec4wp20, LHvec5wp20, LHvec7wp20, LHvec9wp20,

LHvec0wp30 = ("2000", "600", "LHSMinter")
LHvec1wp30 = ("2400", "720", "LHSMinter")
LHvec2wp30 = ("2800", "840", "LHSMinter")
LHvec3wp30 = ("3200", "960", "LHSMinter")
LHvec4wp30 = ("3600", "1080", "LHSMinter")
LHvec5wp30 = ("4000", "1200", "LHSMinter")
LHvec6wp30 = ("4400", "1320", "LHSMinter")
LHvec7wp30 = ("4800", "1440", "LHSMinter")
LHvec8wp30 = ("5200", "1560", "LHSMinter")
LHvec9wp30 = ("5600", "1680", "LHSMinter")
LHvec10wp30 = ("6000", "1800", "LHSMinter")
LHsigspointswp30 = [LHvec0wp30, LHvec2wp30, LHvec4wp30, LHvec6wp30, LHvec8wp30, LHvec10wp30]# LHvec1wp30, LHvec3wp30, LHvec5wp30, LHvec7wp30, LHvec9wp30,


sigpoints = RHsigpointsNW
#sigpoints = RHsigspointswp10
#sigpoints = RHsigspointswp20
#sigpoints = RHsigspointswp30
#sigpoints = LHsigpointsNW
sigpoints = LHsigspointswp10
sigpoints = LHsigspointswp20
sigpoints = LHsigspointswp30
