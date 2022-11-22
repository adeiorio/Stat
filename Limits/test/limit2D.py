import ROOT
from array import array
import os
from Stat.Limits.samples import *
from Stat.Limits.settings import *
'''
ROOT.gROOT.Reset()
ROOT.gStyle.SetCanvasColor(0)
ROOT.gStyle.SetFrameBorderMode(0)
ROOT.gStyle.SetPalette(1,0)
ROOT.gStyle.SetTitleX(0.5) #title X location
ROOT.gStyle.SetTitleY(0.96) #title Y location
ROOT.gStyle.SetPaintTextFormat(".2f")
ROOT.gErrorIgnoreLevel = ROOT.kError
'''
ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch()

def crossing(observed, sigpoints, xs):
    cross = 0.0
    prev_value = 2.
    for i, obvalue in enumerate(observed):
        if obvalue > 1. and i == 0:
            cross = None
        elif cross > 0.:
            break
        elif obvalue > 1. and prev_value < 1.:
            cross = int(sigpoints[i-1][0])+(1-obvalue)/(prev_value-obvalue)#*(xs[sigpoints[i][0]]-xs[sigpoints[i-1][0]])
            #print(xs[sigpoints[i-1][0]], xs[sigpoints[i][0]], obvalue, prev_value)
            prev_value = obvalue
        else:
            prev_value = obvalue
    return cross

def get_obs(foldername):
    o = []
    ifile = open(foldername + "/limit_hist.txt")
    #print "Reading ", filename
    for l in ifile.readlines():
        if l.strip()== "": 
            continue
        else:
            l_split = l.split()
            if l.startswith("y_observed_hist"):
                o = [float(i) for i in l_split[1:] if float(i)!= 0.0]
    return o

def make_2Dplot(chir, xbins, ybins, limit_1p, limit_10p,  limit_20p, limit_30p, Exclud, Width):
    xbins2D = array('f', [2000, 2400, 3200, 4000, 4800, 5600, 6000])
    limit_2D = ROOT.TH2F("limit_2D",  "limit_2D", len(xbins2D)-1, xbins2D, len(ybins)-1, ybins)
    min_width = Width[0]
    max_width = Width[-1]
    print(min_width, max_width)
    for i in range(len(ybins)-1):
        for j in range(len(xbins)-1):
            if(i==0):
                limit_2D.SetBinContent(j+1,i+1,limit_1p[j])
            elif(i==1):
                limit_2D.SetBinContent(j+1,i+1,limit_10p[j])
            elif(i==2):
                limit_2D.SetBinContent(j+1,i+1,limit_20p[j])
            elif(i==3):
                limit_2D.SetBinContent(j+1,i+1,limit_30p[j])

    c1 = ROOT.TCanvas("c1","c1",0,0,2000,1400)
    #c1_1 = ROOT.TPad("c1_1","newpad",0.01,0.01,0.99,0.99)
    c1.SetRightMargin(0.2)
    c1.SetBottomMargin(0.15)
    c1.Draw()
    c1.cd()
    
    #limit_2D.GetXaxis().SetLabelOffset(0.030)
    limit_2D.GetYaxis().SetLabelSize(0.045) #0.04
    limit_2D.GetXaxis().SetLabelSize(0.045) #0.04
    limit_2D.GetZaxis().SetLabelSize(0.045) #0.02
    #limit_2D.SetMinimum(0.)
    #limit_2D.SetMaximum(0.15)
    limit_2D.GetXaxis().SetTitleOffset(1.2)#1.0
    limit_2D.GetYaxis().SetTitleOffset(0.8)
    limit_2D.GetZaxis().SetTitleOffset(1.1)#1.6
    limit_2D.GetXaxis().SetTitleSize(0.06) #0.05
    limit_2D.GetYaxis().SetTitleSize(0.06) #0.05
    limit_2D.GetZaxis().SetTitleSize(0.06)#0.04
    limit_2D.GetYaxis().SetTitle("#Gamma/m_{W'} [%]")
    limit_2D.GetXaxis().SetTitle("#it{m}_{W'} [GeV]")
    if chir == 'LH':
        limit_2D.GetZaxis().SetTitle("#sigma(pp #rightarrow tb) [pb]")
    else:
        limit_2D.GetZaxis().SetTitle("#sigma(pp #rightarrow W' #rightarrow tb) [pb]")
    limit_2D.SetTitle("")
    limit_2D.GetYaxis().SetLimits(min_width,max_width)
    limit_2D.GetXaxis().SetLimits(2000, 6000)
    limit_2D.GetXaxis().SetNdivisions(513)
    limit_2D.GetYaxis().SetNdivisions(503)
    limit_2D.SetMarkerSize(0.85)
    limit_2D.Draw("COLZ")
    #limit_2D.Draw("contz")

    limit_obs = ROOT.TGraph(len(Exclud),Exclud,Width)
    limit_obs.SetTitle('')
    limit_obs.SetLineColor(ROOT.kRed+2)
    limit_obs.SetLineWidth(404)
    limit_obs.SetFillStyle(3352)
    limit_obs.SetFillColor(2)
    c1.cd()
    limit_obs.Draw("Lsame")
    limit_obs.GetXaxis().SetRangeUser(2000, 6000)
    c1.Update()

    pad = ROOT.TPad("pad","pad",0.00,0.00,1.00,1.00)
    channelTextFont = 42
    channelTextSize = 0.05
    cmsText = "CMS"
    cmsTextFont   = 61  # default is helvetic-bold                                                                                                                                                     
    writeExtraText = True
    extraText   = "Preliminary"
    #TString extraText   = ""
    extraTextFont = 52  # default is helvetica-italics                                                                                                                                                 
    # text sizes and text offsets with respect to the top frame in unit of the top margin size
    lumiTextSize     = 0.55
    lumiTextOffset   = 0.2
    cmsTextSize      = 0.65
    cmsTextOffset    = 0.1  # only used in outOfFrame version
    relPosX    = 0.045
    relPosY    = 0.035
    relExtraDY = 1.2
    # ratio of "CMS" and extra text size
    extraOverCmsTextSize  = 0.76
    lumi_13TeV = "138 fb^{-1}"
    lumiText = lumi_13TeV
    lumiText += " (13 TeV)"
    channelText = "Excluded"
    #t = pad.GetTopMargin()                                                                                                                                                                           
    #b = pad.GetBottomMargin()                                                                                                                                                                        
    #r = pad.GetRightMargin()                                                                                                                                                                         
    #l = pad.GetLeftMargin()                                                                                                                                                                          
    t = c1.GetTopMargin()
    b = c1.GetBottomMargin()
    r = c1.GetRightMargin()
    l = c1.GetLeftMargin()
    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextAngle(0)
    latex.SetTextColor(ROOT.kBlack)
    extraTextSize = extraOverCmsTextSize*cmsTextSize
    latex.SetTextFont(42)
    latex.SetTextAlign(31)
    latex.SetTextSize(lumiTextSize*t)
    latex.DrawLatex(1-r-0.02,0.92,lumiText)
    latex.SetTextFont(cmsTextFont)
    latex.SetTextAlign(11)
    latex.SetTextSize(cmsTextSize*t)
    latex.DrawLatex(l+0.02, 0.92,cmsText)
    latex.SetTextFont(extraTextFont)
    latex.SetTextSize(extraTextSize*t)
    #latex.DrawLatex(l+0.12, 0.94, extraText)
    latex.SetTextFont(channelTextFont)
    latex.SetTextSize(channelTextSize)
    latex.DrawLatex(0.15, 0.20, channelText)
    #limit_2D.Draw("COLZ")
    c1.RedrawAxis()
    c1.SetLogz()
    limit_2D.GetXaxis().SetRangeUser(2000, 6000)
    c1.SaveAs("limit_2D" + chir + ".png")
    c1.SaveAs("limit_2D" + chir + ".pdf")
    pad.Close()
    c1.Close()
    

chirs = ['RH', 'LH']
sig_dict = {'RH':[RHsigpointsNW, RHsigspointswp10, RHsigspointswp20, RHsigspointswp30],
             'LH':[LHsigpointsNW, LHsigspointswp10, LHsigspointswp20, LHsigspointswp30]}

sig_dict_2 = {'RH':[RHsigpointsNW_2, RHsigspointswp10, RHsigspointswp20, RHsigspointswp30],
             'LH':[LHsigpointsNW_2, LHsigspointswp10, LHsigspointswp20_2, LHsigspointswp30]}

folder_dict = {'RH':["5May22_SRNW_RH_systsall_unblind", "5May22_SR10_RH_systsall_unblind", "5May22_SR20_RH_systsall_unblind", "5May22_SR30_RH_systsall_unblind"],
               'LH':["5May22_SRNW_LH_systsall_unblind", "5May22_SR10_LH_systsall_unblind", "5May22_SR20_LH_systsall_unblind", "5May22_SR30_LH_systsall_unblind"]}
folder_dict = {'RH':["22Jun22_SRNW_RH_systsall_unblind_MCstats_shapeN_v18", "22Jun22_SR10_RH_systsall_unblind_MCstats_shapeN_v18", "22Jun22_SR20_RH_systsall_unblind_MCstats_shapeN_v18", "22Jun22_SR30_RH_systsall_unblind_MCstats_shapeN_v18"],
               'LH':["22Jun22_SRNW_LH_systsall_unblind_MCstats_shapeN_v18", "22Jun22_SR10_LH_systsall_unblind_MCstats_shapeN_v18", "22Jun22_SR20_LH_systsall_unblind_MCstats_shapeN_v18", "22Jun22_SR30_LH_systsall_unblind_MCstats_shapeN_v18"]}

Width = array('f', [1, 10, 20, 30])
#xbins = array('f', [2000, 2800, 3600, 4400, 5200, 6000])
xbins = array('f', [1600, 2400, 3200, 4000, 4800, 5600, 6400])
ybins = array('f', [1, 5, 15, 25, 30])

for chir in chirs:
    Exclud = array('f', [])  #theor cross section - experimental limit intersection
    onw = get_obs(folder_dict[chir][0])
    y_theoNW = {masspoint[0]: sample_dict["WP_M%sW%s_%s_2016" %(masspoint[0],masspoint[1],masspoint[2])].sigma for masspoint in sig_dict_2[chir][0] }
    o10 = get_obs(folder_dict[chir][1])
    y_theo10 = {masspoint[0]: sample_dict["WP_M%sW%s_%s_2016" %(masspoint[0],masspoint[1],masspoint[2])].sigma for masspoint in sig_dict[chir][1] }
    o20 = get_obs(folder_dict[chir][2])
    y_theo20 = {masspoint[0]: sample_dict["WP_M%sW%s_%s_2016" %(masspoint[0],masspoint[1],masspoint[2])].sigma for masspoint in sig_dict_2[chir][2] }
    o30 = get_obs(folder_dict[chir][3])
    y_theo30 = {masspoint[0]: sample_dict["WP_M%sW%s_%s_2016" %(masspoint[0],masspoint[1],masspoint[2])].sigma for masspoint in sig_dict[chir][3] }

    print(crossing(onw, sig_dict[chir][0], y_theoNW))
    print(o10, sig_dict[chir][1], y_theo10)
    print(len(o10), len(sig_dict[chir][1])) 
    print(crossing(o10, sig_dict[chir][1], y_theo10))
    print(crossing(o20, sig_dict[chir][2], y_theo20))
    print(crossing(o30, sig_dict[chir][3], y_theo30))

    cross = [crossing(onw, sig_dict[chir][0], y_theoNW), crossing(o10, sig_dict[chir][1], y_theo10), crossing(o20, sig_dict[chir][2], y_theo20), crossing(o30, sig_dict[chir][3], y_theo30)]
    print cross
    for ve in cross:
        if ve > 0.:
            Exclud.append(ve)
        else:
            Exclud.append(-9999999.)

    limit_1p = []
    limit_10p = []
    limit_20p = []
    limit_30p = []
    for mp in range(1, len(xbins)):
        limit_1p.append(y_theoNW[str(int((xbins[mp]+xbins[mp-1])/2))])
        limit_10p.append(y_theo10[str(int((xbins[mp]+xbins[mp-1])/2))])
        limit_20p.append(y_theo20[str(int((xbins[mp]+xbins[mp-1])/2))])
        limit_30p.append(y_theo30[str(int((xbins[mp]+xbins[mp-1])/2))])
    #print limit_1p
    make_2Dplot(chir, xbins, ybins, limit_1p, limit_10p,  limit_20p, limit_30p, Exclud, Width)
