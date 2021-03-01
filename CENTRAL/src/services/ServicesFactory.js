import CertificateService from './CertificateService'
import OrganizationService from './OrganizationService';

const services = {
    certificates: CertificateService,
    organizations: OrganizationService
};

export const ServicesFactory = {
    get: name => services[name]
};