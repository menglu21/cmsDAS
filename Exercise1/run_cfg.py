import FWCore.ParameterSet.Config as cms

process = cms.Process("photonAnalyzer")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(40) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        #'file:/home/cmsdas/lum/cmsDAS/CMSSW_10_2_18/src/photonAna/photonAnalyzer/ZG1.root'
        'file:/home/cmsdas/lum/cmsDAS/CMSSW_10_2_18/src/photonAna/photonAnalyzer/DY1.root'
    )
)

process.demo = cms.EDAnalyzer('photonAnalyzer',
		 Photons =  cms.InputTag("slimmedPhotons"),
		# lhe1 =  cms.VInputTag(cms.InputTag("externalLHEProducer"), cms.InputTag("source")),
)


process.p = cms.Path(process.demo)
