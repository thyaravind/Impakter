class CertificateResponse {
    constructor(basicDetails,sdgs,sdgTargets){
        this.basicDetails = basicDetails
        this.sdgs = sdgs
        this.sdgTargets = sdgTargets

    }

    setSdgs (sdgs){
        this.sdgs = sdgs
    }
    setSdgTargets (sdgTargets){
        this.sdgTargets = sdgTargets
    }


}

module.exports = CertificateResponse
