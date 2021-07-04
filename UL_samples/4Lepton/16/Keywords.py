# keep the pre-VFP , _preVFP for all the samples


# # =======================================  4Lepton_16_VVV ======================================
KeyWords['4Lepton_16_VVV'] = {
    # keep the None DiLeptonFilter ?
     "elect" : [("WWW"), ("WWZ"), ("WZZ"), ("ZZZ"),("WWW", "DiLeptonFilter"), ("WWZ", "DiLeptonFilter"), ("WZZ", "DiLeptonFilter"), ("ZZZ", "DiLeptonFilter"),("VHToNonbb"),("HZJ_HToWW"),("GluGluZH")],
     "exclude": [],
}
# # =============================================================================



# # =======================================  4Lepton_16_TT ======================================
KeyWords['4Lepton_16_TT'] = {
    # keep -FPMC-
     "elect" : [("TT", "SemiLeptonic_"), ("TT", "2L2Nu"),],
     "exclude": ['Zprime','RSG','WZJJ','VBS','TTZ','mtop','width','hdamp','Njet','Mtt','CP5up','CP5down',"TTG","TTW","TTbb"],
}
# # =============================================================================




# # ======================================= 4Lepton_18 TTV or TTVV  ======================================
KeyWords['4Lepton_16_TTV_TTVV'] = {
    # keep amcatnloFXFX NLO? /TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM
     "elect" : [("TTW" ), ("TTZ"), ("ttWJets"),("ttZJets"), ("TTZToQQ"),("TTWW"),("TTWZ"),("TTZZ"),("TTZH"),("TTWH")],
     "exclude": ['Zprime','RSG','VBS','mtop','width','hdamp','CP5up','CP5down',],
}
# # =======================================  ======================================


# # ======================================= 4Lepton_16_TWZ ======================================
KeyWords['4Lepton_16_TWZ'] = {
    # keep amcatnloFXFX NLO? /TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM
     "elect" : [("ST_tWll" ), ],
     "exclude": ['Zprime','RSG','VBS','mtop','width','hdamp','CP5up','CP5down','TTWZ'],
}
# # =======================================  ======================================


# # =======================================  4Lepton_16_VV ======================================
KeyWords['4Lepton_16_VV'] = {
    # keep ?
     "elect" : [("WW" ), ("WZ" ), ("ZZ" ),("GluGluToContinToZZ")],
    # remove SSWW_? 
    # remove ("_EWK","Polarization") ? /WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL18NanoAOD-106X_upgrade2018_realistic_v11_L1v1-v1/NANOAODSIM
     "exclude": ['_PDFWeights_TuneCP5','hdamp','CP5up','CP5down',("_EWK","Polarization"),"WminusH","Wprime",      'GluGluHTo','SSWW_','TWZ',"VBF_HTo","VBS",("WWW",), ("WWZ"), ("WZZ"), ("ZZZ"),"TTWW","WplusH","WZG","TTZZ"]
}
# # =============================================================================

# # ======================================= 4Lepton_16_VVG======================================
KeyWords['4Lepton_16_VVG'] = {
    # keep ?
     "elect" : [("WZG" ), ],
    # remove SSWW_? 
    # remove ("_EWK","Polarization") ? /WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL18NanoAOD-106X_upgrade2018_realistic_v11_L1v1-v1/NANOAODSIM
     "exclude": ['_PDFWeights_TuneCP5','hdamp','CP5up','CP5down',("_EWK","Polarization"),"WminusH","Wprime",      'GluGluHTo','GluGluTo','SSWW_','TWZ',"VBF_HTo","VBS",("WWW",), ("WWZ"), ("WZZ"), ("ZZZ"),"TTWW","WplusH",]
}
# # =============================================================================


# # ======================================= 4Lepton_16_DY ======================================
KeyWords['4Lepton_16_DY'] = {
     "elect" : [("DYJetsToLL","M-10to50" ),("DYJetsToLL","M-50" ),],
     "exclude": []
}

# # =======================================  ======================================


# # ======================================= 4Lepton_16_GluGluH ======================================
KeyWords['4Lepton_16_GluGluH'] = {
    "elect" : [("GluGlu","H","ZZ")],
     # remove dataset contains JHUGenV7011 ? Seems to be new physics:
    # '/GluGluHToZZTo2L2Q_M1000_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM',
     "exclude": ["JHUGenV7011"],
}

# # =======================================  ======================================


# # ======================================= 4Lepton_16_ttH ======================================
KeyWords['4Lepton_16_ttH'] = {
    "elect" : [("ttH"),("TTH"),("ttH","Nonbb"),("TTH","Nonbb")],
     # remove dataset contains JHUGenV7011 ? Seems to be new physics:
    # '/GluGluHToZZTo2L2Q_M1000_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM',
     "exclude": ["JHUGenV7011",'Zprime','RSG','VBS','mtop','width','hdamp','CP5up','CP5down',],
}

# # =======================================  ======================================



