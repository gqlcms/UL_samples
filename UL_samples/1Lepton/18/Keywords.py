# keep the pre-VFP , _preVFP for all the samples


# # =======================================  1Lepton_18_VVV ======================================
KeyWords['1Lepton_18_VVV'] = {
     "elect" : [("WWW"), ("WWZ"), ("WZZ"), ("ZZZ")],
     "exclude": [],
}
# # =============================================================================


# # ======================================= 1Lepton_18_WJets ======================================
KeyWords['1Lepton_18_WJets'] = {
    # keep  ? 
     "elect" : [("WJets","_HT-"),],
     "exclude": ['Zprime','RSG','VBS','mtop','width','hdamp','CP5up','CP5down',"TTWJets"],
}
# # =============================================================================


# # =======================================  1Lepton_18_TT ======================================
KeyWords['1Lepton_18_TT'] = {
    # keep -FPMC-
     "elect" : [("TT", "SemiLeptonic_"), ("TT", "2L2Nu"), ("TT", "Hadronic_")],
     "exclude": ['Zprime','RSG','WZJJ','VBS','TTZ','mtop','width','hdamp','Njet','Mtt','CP5up','CP5down',"TTG","TTW","TTbb"],
}
# # =============================================================================



# # ======================================= 1Lepton_18_ST ======================================
KeyWords['1Lepton_18_ST'] = {
    # keep comphep-? /ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL18NanoAOD-106X_upgrade2018_realistic_v11_L1v1-v1/NANOAODSIM
    "elect" : [("ST_s",),("ST_t",),("ST_tW","NoFullyHadronic"),],
    # remove dataset contains _eDecays ?  '/ST_t-channel_eDecays_anomwtbLVLT_LT_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL17NanoAOD-106X_mc2017_realistic_v6-v1/NANOAODSIM',
    # remove dataset contains _eDecays ?  /ST_t-channel_eleDecays_anomwtbLVRV_LVRVunphys_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL16NanoAOD-106X_mcRun2_asymptotic_v13-v1/NANOAODSIM
    # remove dataset contains _eDecays ?  /ST_t-channel_muDecays_anomwtbLVLT_LT_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL16NanoAOD-106X_mcRun2_asymptotic_v13-v1/NANOAODSIM
    # remove dataset contains _anomwtb ?  /ST_t-channel_muDecays_anomwtbLVLT_LT_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL16NanoAOD-106X_mcRun2_asymptotic_v13-v1/NANOAODSIM
     "exclude": ["_eDecays","_anomwtbLVRV","_anomwtbLVLT","_anomwtb"],
}
# # =======================================  ======================================


## ======================================= 1Lepton_18_QCD_HT ======================================
KeyWords['1Lepton_18_QCD_HT'] = {
    # keep dataset contains PSWeights ?
     "elect" : [("QCD", "HT")],
     "exclude": ["pomflux","FlatPU0to70","NoPUBX25","upgrade2018_realistic","EpsilonPU",      ("BdToMuMu",),("BuTo",),("bEnriched"),],
}

KeyWords['1Lepton_18_QCD_PT'] = {
    # keep dataset contains PSWeights ?
    # keep upgrade2018_realistic?
     "elect" : [("QCD", "Pt")],
     "exclude": ["pomflux","FlatPU0to70","NoPUBX25","EpsilonPU",      ("BdToMuMu",),("BuTo",),("bEnriched"),],
}
# # =======================================  ======================================


# # ======================================= 1Lepton_18 TTV or TV ======================================
KeyWords['1Lepton_18_TTV'] = {
    # keep amcatnloFXFX NLO? /TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM
     "elect" : [("TTW" ), ("TTZ"), ("ttWJets"),("ttZJets"), ("TTZToQQ")],
     "exclude": ['Zprime','RSG','VBS','mtop','width','hdamp','CP5up','CP5down','TTWZ'],
}
# # =======================================  ======================================


# # ======================================= 1Lepton_18 VV without ZZ ======================================
KeyWords['1Lepton_18_VV'] = {
    # keep ?
     "elect" : [("WW" ), ("WZ" ), ("ZZ" ),],
    # remove SSWW_? 
    # remove ("_EWK","Polarization") ? /WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL18NanoAOD-106X_upgrade2018_realistic_v11_L1v1-v1/NANOAODSIM
     "exclude": ['_PDFWeights_TuneCP5','hdamp','CP5up','CP5down',("_EWK","Polarization"),"WminusH","Wprime",      'GluGluHTo','GluGluTo','SSWW_','TWZ',"VBF_HTo","VBS",("WWW",), ("WWZ"), ("WZZ"), ("ZZZ"),"TTWW","WplusH","WZG","TTZZ"]
}
# # =============================================================================



# # ======================================= 1Lepton_18_EGamma ======================================
KeyWords['1Lepton_18_EGamma'] = {
    # keep ?
     "elect" : [("EGamma","UL2018" ),],
    # remove SSWW_? 
    # remove ("_EWK","Polarization") ? /WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL18NanoAOD-106X_upgrade2018_realistic_v11_L1v1-v1/NANOAODSIM
     "exclude": ["MuonEGamma"]
}

# # ======================================= 1Lepton_18_SingleMuon ======================================
KeyWords['1Lepton_18_SingleMuon'] = {
    # keep ?
     "elect" : [("SingleMuon","UL2018" ),],
    # remove SSWW_? 
    # remove ("_EWK","Polarization") ? /WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL18NanoAOD-106X_upgrade2018_realistic_v11_L1v1-v1/NANOAODSIM
     "exclude": []
}

# # =======================================  ======================================



