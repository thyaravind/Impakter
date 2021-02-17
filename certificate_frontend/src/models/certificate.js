import compute from "./compute"
import {sdgs} from "./constants"

export default class certificateModel {

    certificateID = null
    organizationID = null
    name = ""
    description = ""
    priority = ""
    applicationLength = ""
    imagePath = ""
    difficulty = null
    relevance = null
    validity = null
    region = null
    countries = []
    goal = null
    rating = "P3"
    pricing = ""
    sdgEngagement = ""
    sdgs = []
    sdgTargets = []
    industries = []
    industrySectors = []
    activeStatus = true
    computedActiveStatus = null
    computedPriority = null
    computedSdgs = []


    setOrganizationID(id) {
        this.organizationID = id
    }

    getCertificatePayload() {
        return {
            certificateID: this.certificateID,
            basicDetails: {
                name: this.name,
                organizationID: this.organizationID,
                description: this.description,
                priority: this.priority,
                activeStatus: this.activeStatus,
                sdgEngagement: this.sdgEngagement
            },
            sdgs: this.sdgs,
            sdgTargets: this.sdgTargets,
            additionalDetails: {
                applicationLength: this.applicationLength,
                difficulty: this.difficulty,
                relevance: this.relevance,
                validity: this.validity,
                goal: this.goal,
                specificity: this.rating,
                pricing: this.pricing
            },
            computedDetails: {
                computedActiveStatus: this.computedActiveStatus,
                computedSdgs: this.computedSdgs
            }
        }




    }
    change(certificateResponseObj) {
        this.certificateID = certificateResponseObj.details.certificateID
        this.name = certificateResponseObj.details.name
        this.organizationID = certificateResponseObj.details.organizationID
        this.description = certificateResponseObj.details.description
        this.priority = certificateResponseObj.details.priority
        this.sdgEngagement = certificateResponseObj.details.sdgEngagement


        this.sdgs = certificateResponseObj.sdgs;
        this.sdgTargets = certificateResponseObj.sdgTargets;

        this.computedActiveStatus = certificateResponseObj.details.activeStatus == 1 ? true : false
        this.computedPriority = compute.convertFromScale(certificateResponseObj.details.priority)

    }

    computeSdgs() {
        this.sdgs.forEach(
            sdg => {
                var temp = sdgs.filter(function (item) {
                    return item.value == sdg;
                })
                this.computedSdgs.push(temp[0])
                
            })
    }

}

