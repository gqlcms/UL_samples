# keep the pre-VFP , _preVFP for all the samples


# # =======================================  0Lepton_16_VVV ======================================
KeyWords['0Lepton_16_VVV'] = {
     "elect" : [("WWW"), ("WWZ"), ("WZZ"), ("ZZZ")],
     "exclude": [],
}
# # =============================================================================


# # ======================================= 0Lepton_16_WJets ======================================
KeyWords['0Lepton_16_WJets'] = {
    # keep  ? 
     "elect" : [("WJets","QQ","_HT-"),],
     "exclude": ['Zprime','RSG','VBS','mtop','width','hdamp','CP5up','CP5down',"TTWJets"],
}
# # =============================================================================


# # ======================================= 0Lepton_16_ZJets ======================================
KeyWords['0Lepton_16_ZJets'] = {
    # keep  ? 
     "elect" : [("ZJets","QQ","_HT-"),],
     "exclude": ['Zprime','RSG','VBS','mtop','width','hdamp','CP5up','CP5down',"TTWJets"],
}
# # =============================================================================


# # =======================================  0Lepton_16_TT ======================================
KeyWords['0Lepton_16_TT'] = {
    # keep -FPMC-
     "elect" : [("TT", "SemiLeptonic_"), ("TT", "Hadronic_")],
     "exclude": ['Zprime','RSG','WZJJ','VBS','TTZ','mtop','width','hdamp','Njet','Mtt','CP5up','CP5down',"TTG","TTW","TTbb"],
}
# # =============================================================================



# # ======================================= 0Lepton_16_ST ======================================
KeyWords['0Lepton_16_ST'] = {
    # keep comphep-? /ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL18NanoAOD-106X_upgrade2018_realistic_v11_L1v1-v1/NANOAODSIM
    "elect" : [("ST_s",),("ST_t",),("ST_tW","NoFullyHadronic"),],
    # remove dataset contains _eDecays ?  '/ST_t-channel_eDecays_anomwtbLVLT_LT_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL17NanoAOD-106X_mc2017_realistic_v6-v1/NANOAODSIM',
    # remove dataset contains _eDecays ?  /ST_t-channel_eleDecays_anomwtbLVRV_LVRVunphys_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL16NanoAOD-106X_mcRun2_asymptotic_v13-v1/NANOAODSIM
    # remove dataset contains _eDecays ?  /ST_t-channel_muDecays_anomwtbLVLT_LT_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL16NanoAOD-106X_mcRun2_asymptotic_v13-v1/NANOAODSIM
    # remove dataset contains _anomwtb ?  /ST_t-channel_muDecays_anomwtbLVLT_LT_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL16NanoAOD-106X_mcRun2_asymptotic_v13-v1/NANOAODSIM
     "exclude": ["_eDecays","_anomwtbLVRV","_anomwtbLVLT","_anomwtb"],
}
# # =======================================  ======================================


## ======================================= 0Lepton_16_QCD_HT ======================================
KeyWords['0Lepton_16_QCD_HT'] = {
    # keep dataset contains PSWeights ?
     "elect" : [("QCD", "HT")],
     "exclude": ["pomflux","FlatPU0to70","NoPUBX25","upgrade2018_realistic","EpsilonPU",      ("BdToMuMu",),("BuTo",),("bEnriched"),],
}


# # =======================================  ======================================



# # ======================================= 0Lepton_18 VV  ======================================
KeyWords['0Lepton_16_VV'] = {
    # keep ?
     "elect" : [("WW" ), ("WZ" ), ("ZZ" ),],
    # remove SSWW_? 
    # remove ("_EWK","Polarization") ? /WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL18NanoAOD-106X_upgrade2018_realistic_v11_L1v1-v1/NANOAODSIM
     "exclude": ['_PDFWeights_TuneCP5','hdamp','CP5up','CP5down',("_EWK","Polarization"),"WminusH","Wprime",      'GluGluHTo','GluGluTo','SSWW_','TWZ',"VBF_HTo","VBS",("WWW",), ("WWZ"), ("WZZ"), ("ZZZ"),"TTWW","WplusH","WZG","TTZZ"]
}
# # =============================================================================




# # =======================================  0Lepton_16_VH  ======================================
KeyWords['0Lepton_16_VH'] = {
    # keep ?
     "elect" : ["WplusH",("ZH","HToBB","ZToQQ"),("ZH","HTobb","ZToQQ"),"WminusH",],
    # remove ?
     "exclude": ['_PDFWeights_TuneCP5','hdamp','CP5up','CP5down',("_EWK","Polarization"),"WminusH","Wprime",      "TWZ","Polarization","prime"]
}
# # =============================================================================





