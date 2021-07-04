# keep the pre-VFP , _preVFP for all the samples


# # =======================================  2Lepton_OS_16_VVV ======================================
KeyWords['2Lepton_OS_16_VVV'] = {
    # keep the None DiLeptonFilter ?
     "elect" : [("WWW"), ("WWZ"), ("WZZ"), ("ZZZ"),("WWW", "DiLeptonFilter"), ("WWZ", "DiLeptonFilter"), ("WZZ", "DiLeptonFilter"), ("ZZZ", "DiLeptonFilter"),("VHToNonbb"),("HZJ_HToWW"),("GluGluZH")],
     "exclude": [],
}
# # =============================================================================



# # =======================================  2Lepton_OS_16_TT ======================================
KeyWords['2Lepton_OS_16_TT'] = {
    # keep -FPMC-
     "elect" : [("TT", "SemiLeptonic_"), ("TT", "2L2Nu"), ("TTJets", "SingleLept"), ("TTJets",),("TTPlus1Jet", "DiLept") , ("TT", "DiLept_")],
     "exclude": ['Zprime','RSG','VBS','mtop','width','hdamp','Mtt','CP5up','CP5down',"TTG","TTW"],
}
# # =============================================================================




# # ======================================= 2Lepton_OS_16 TV TTT TTV TTVV TTTT  ======================================
KeyWords['2Lepton_OS_16_TTV_TTVV'] = {
    # keep amcatnloFXFX NLO? /TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM
     "elect" : [("tZq"), ("TTW" ), ("TTZ"), ("ttWJets"),("ttZJets"), ("TTZToQQ"),("TTWW"),("TTWZ"),("TTZZ"),("TTZH"),("TTWH"), "TTTJ", "TTTT"],
     "exclude": ['Zprime','RSG','VBS','mtop','width','hdamp','CP5up','CP5down',],
}
# # =======================================  ======================================


# # ======================================= 2Lepton_OS_16_TWZ ======================================
KeyWords['2Lepton_OS_16_TWZ'] = {
    # keep amcatnloFXFX NLO? /TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM
     "elect" : [("ST_tWll" ), ],
     "exclude": ['Zprime','RSG','VBS','width','hdamp','CP5up','CP5down',],
}
# # =======================================  ======================================


# # =======================================  2Lepton_OS_16_VV ======================================
KeyWords['2Lepton_OS_16_VV'] = {
    # keep ?
     "elect" : [("WW" ), ("WZ" ), ("ZZ" ), ("GluGluToContinToZZ"), ("GluGluToContin","ZZ"), ("WG", "ToLNu"), ("WW", "DoubleScattering"), ("WpWpJJ"), ("ZGToLLG")],
    # remove SSWW_? 
    # remove ("_EWK","Polarization") ? /WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL18NanoAOD-106X_upgrade2018_realistic_v11_L1v1-v1/NANOAODSIM
     "exclude": ['_PDFWeights_TuneCP5','hdamp','CP5up','CP5down',("_EWK","Polarization"),"Wprime", 'SSWW_','TWZ',"VBF_HTo","VBS",("WWW",), ("WWZ"), ("WZZ"), ("ZZZ"),"TTWW", "WZG", "GluGluHToZZ"]
}
# # =============================================================================

# # ======================================= 2Lepton_OS_16_VVG======================================
KeyWords['2Lepton_OS_16_VVG'] = {
    # keep ?
     "elect" : [("WZG" ), "WWG" ],
    # remove SSWW_? 
    # remove ("_EWK","Polarization") ? /WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL18NanoAOD-106X_upgrade2018_realistic_v11_L1v1-v1/NANOAODSIM
     "exclude": ['_PDFWeights_TuneCP5','hdamp','CP5up','CP5down',("_EWK","Polarization"),  'GluGluHTo','GluGluTo','SSWW_',"VBF_HTo","VBS",("WWW",), ("WWZ"), ("WZZ"), ("ZZZ"),"TTWW",]
}
# # =============================================================================


# # ======================================= 2Lepton_OS_16_DY ======================================
KeyWords['2Lepton_OS_16_DY'] = {
     "elect" : [("DYJetsToLL","M-10to50" ),("DYJetsToLL","M-50" ),("DYJetsToLL","M-50", "Zpt" ),],
     "exclude": []
}

# # =======================================  ======================================


# # ======================================= 2Lepton_OS_16_GluGluH ======================================
KeyWords['2Lepton_OS_16_GluGluH'] = {
    # remove '/GluGluHToZZTo2L2Q_M900_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM'  , new physics?
    # keep '/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL18NanoAOD-106X_upgrade2018_realistic_v11_L1v1-v1/NANOAODSIM' ?
    "elect" : [("GluGluTo", "M125"),("GluGluHTo", "M125"),("GluGlu","ZZ", "M125"),("GluGlu","H","ZZ", "M125")],
     # remove dataset contains JHUGenV7011 ? Seems to be new physics:
    # '/GluGluHToZZTo2L2Q_M1000_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM',
     "exclude": ["JHUGenV7011"],
}

# # =======================================  ======================================


# # ======================================= 2Lepton_OS_16_ttH ======================================
KeyWords['2Lepton_OS_16_ttH'] = {
    "elect" : [("ttH"),("TTH"),("ttH","Nonbb"),("TTH","Nonbb")],
     # remove dataset contains JHUGenV7011 ? Seems to be new physics:
    # '/GluGluHToZZTo2L2Q_M1000_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM',
     "exclude": ["JHUGenV7011",'Zprime','RSG','VBS','mtop','width','hdamp','CP5up','CP5down',],
}

# # =======================================  ======================================


# # ======================================= 2Lepton_OS_16_ST ======================================
KeyWords['2Lepton_OS_16_ST'] = {
    # keep comphep-? /ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL18NanoAOD-106X_upgrade2018_realistic_v11_L1v1-v1/NANOAODSIM
    "elect" : [("ST_tW","NoFullyHadronic"),],
    # remove dataset contains _eDecays ?  '/ST_t-channel_eDecays_anomwtbLVLT_LT_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL17NanoAOD-106X_mc2017_realistic_v6-v1/NANOAODSIM',
    # remove dataset contains _eDecays ?  /ST_t-channel_eleDecays_anomwtbLVRV_LVRVunphys_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL16NanoAOD-106X_mcRun2_asymptotic_v13-v1/NANOAODSIM
    # remove dataset contains _eDecays ?  /ST_t-channel_muDecays_anomwtbLVLT_LT_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL16NanoAOD-106X_mcRun2_asymptotic_v13-v1/NANOAODSIM
    # remove dataset contains _anomwtb ?  /ST_t-channel_muDecays_anomwtbLVLT_LT_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL16NanoAOD-106X_mcRun2_asymptotic_v13-v1/NANOAODSIM
     "exclude": ["_eDecays","_anomwtbLVRV","_anomwtbLVLT","_anomwtb"],
}
# # =======================================  ======================================



# # ======================================= 2Lepton_OS_16_TG ======================================
KeyWords['2Lepton_OS_16_TG'] = {
    # keep comphep-? /ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL18NanoAOD-106X_upgrade2018_realistic_v11_L1v1-v1/NANOAODSIM
    "elect" : [("TGJets","leptonDecays"),],
    # remove dataset contains _eDecays ?  '/ST_t-channel_eDecays_anomwtbLVLT_LT_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL17NanoAOD-106X_mc2017_realistic_v6-v1/NANOAODSIM',
    # remove dataset contains _eDecays ?  /ST_t-channel_eleDecays_anomwtbLVRV_LVRVunphys_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL16NanoAOD-106X_mcRun2_asymptotic_v13-v1/NANOAODSIM
    # remove dataset contains _eDecays ?  /ST_t-channel_muDecays_anomwtbLVLT_LT_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL16NanoAOD-106X_mcRun2_asymptotic_v13-v1/NANOAODSIM
    # remove dataset contains _anomwtb ?  /ST_t-channel_muDecays_anomwtbLVLT_LT_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL16NanoAOD-106X_mcRun2_asymptotic_v13-v1/NANOAODSIM
     "exclude": ["_eDecays","_anomwtbLVRV","_anomwtbLVLT","_anomwtb"],
}
# # =======================================  ======================================

        
# # =======================================  2Lepton_OS_16_VH  ======================================
KeyWords['2Lepton_OS_16_VH'] = {
    # keep ?
     "elect" : ["WplusH",("ZH","HToBB","ZToQQ"),("ZH","HTobb","ZToQQ"),"WminusH", ("VH","ToNonbb")],
    # remove ?
     "exclude": ['_PDFWeights_TuneCP5','hdamp','CP5up','CP5down',("_EWK","Polarization"),"WminusH","Wprime",      "TWZ","Polarization","prime"]
}
# # =============================================================================
       
        
        
# # ======================================= 2Lepton_OS_16_WJets ======================================
KeyWords['2Lepton_OS_16_WJets'] = {
    # keep  ? 
     "elect" : [("WJets","_HT-", "LNu"),("W2Jets","ToLNu"), ("W4Jets", "ToLNu"), ("W", "Jets", "ToLNu"), ("WJets", "ToLNu")],
     "exclude": ['Zprime','RSG','VBS','mtop','width','hdamp','CP5up','CP5down',"TTWJets"],
}
# # =============================================================================
        
        
