export default class organizationModel {
    name = ""
    organizationID = null
    accessToken = ""
    industries = []
    countryID = null
    website = ""

    map(organizationResponseObj) {
        this.name = organizationResponseObj.name
        this.organizationID = organizationResponseObj.organizationID
        this.accessToken = organizationResponseObj.organizationID
        this.website = organizationResponseObj.website
    }

}