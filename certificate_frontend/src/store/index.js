import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {

        certificate: {
            name: "",
            description:"",
            applicationLength: "",
            imagePath:"",
            difficulty: null,
            relevance: null,
            validity: null,
            region: null,
            countries:[],
            goal:null,
            rating:"P3",
            pricing:"",
            sdgEngagement:"",
            sdgs:[],
            sdgTargets:[],
            industries:[],
            industrySectors:[]
        },
            sdgs: [{value:0,text:"SDG 1 No Poverty",targets:[
                    {value:"1.1",text:"1.1 By 2030, eradicate extreme poverty for all people everywhere, currently measured as people living on less than $1.25 a day"},
                    {value:"1.2",text:"1.2 By 2030, reduce at least by half the proportion of men, women and children of all ages living in poverty in all its dimensions according to national definitions"},
                    {value:"1.3",text:"1.3 Implement nationally appropriate social protection systems and measures for all, including floors, and by 2030 achieve substantial coverage of the poor and the vulnerable"},
                    {value:"1.4",text:"1.4 By 2030, ensure that all men and women, in particular the poor and the vulnerable, have equal rights to economic resources, as well as access to basic services, ownership and control over land and other forms of property, inheritance, natural resources, appropriate new technology and financial services, including microfinance"},
                    {value:"1.5",text:"1.5 By 2030, build the resilience of the poor and those in vulnerable situations and reduce their exposure and vulnerability to climate-related extreme events and other economic, social and environmental shocks and disasters"},
                    {value:"1.a",text:"1.a Ensure significant mobilization of resources from a variety of sources, including through enhanced development cooperation, in order to provide adequate and predictable means for developing countries, in particular least developed countries, to implement programmes and policies to end poverty in all its dimensions"},
                    {value:"1.b",text:"1.b Create sound policy frameworks at the national, regional and international levels, based on pro-poor and gender-sensitive development strategies, to support accelerated investment in poverty eradication actions"}]},
                {value:1,text:"SDG 2 Zero Hunger",targets:[{value:"2.1",text:"2.1 By 2030, end hunger and ensure access by all people, in particular the poor and people in vulnerable situations, including infants, to safe, nutritious and sufficient food all year round"},
                    {value:"2.2",text:"2.2 By 2030, end all forms of malnutrition, including achieving, by 2025, the internationally agreed targets on stunting and wasting in children under 5 years of age, and address the nutritional needs of adolescent girls, pregnant and lactating women and older persons"},
                    {value:"2.3",text:"2.3 By 2030, double the agricultural productivity and incomes of small-scale food producers, in particular women, indigenous peoples, family farmers, pastoralists and fishers, including through secure and equal access to land, other productive resources and inputs, knowledge, financial services, markets and opportunities for value addition and non-farm employment"},
                    {value:"2.4",text:"2.4 By 2030, ensure sustainable food production systems and implement resilient agricultural practices that increase productivity and production, that help maintain ecosystems, that strengthen capacity for adaptation to climate change, extreme weather, drought, flooding and other disasters and that progressively improve land and soil quality"},
                    {value:"2.5",text:"2.5 By 2020, maintain the genetic diversity of seeds, cultivated plants and farmed and domesticated animals and their related wild species, including through soundly managed and diversified seed and plant banks at the national, regional and international levels, and promote access to and fair and equitable sharing of benefits arising from the utilization of genetic resources and associated traditional knowledge, as internationally agreed"},
                    {value:"2.a",text:"2.a Increase investment, including through enhanced international cooperation, in rural infrastructure, agricultural research and extension services, technology development and plant and livestock gene banks in order to enhance agricultural productive capacity in developing countries, in particular least developed countries"},
                    {value:"2.b",text:"2.b Correct and prevent trade restrictions and distortions in world agricultural markets, including through the parallel elimination of all forms of agricultural export subsidies and all export measures with equivalent effect, in accordance with the mandate of the Doha Development Round"},
                    {value:"2.c",text:"2.c Adopt measures to ensure the proper functioning of food commodity markets and their derivatives and facilitate timely access to market information, including on food reserves, in order to help limit extreme food price volatility"}]},
                {value:2,text:"SDG 3 Good Health and Well-Being",targets:[{value:"3.1",text:"3.1 By 2030, reduce the global maternal mortality ratio to less than 70 per 100,000 live births"},
                    {value:"3.2",text:"3.2 By 2030, end preventable deaths of newborns and children under 5 years of age, with all countries aiming to reduce neonatal mortality to at least as low as 12 per 1,000 live births and under-5 mortality to at least as low as 25 per 1,000 live births"},
                    {value:"3.3",text:"3.3 By 2030, end the epidemics of AIDS, tuberculosis, malaria and neglected tropical diseases and combat hepatitis, water-borne diseases and other communicable diseases"},
                    {value:"3.4",text:"3.4 By 2030, reduce by one third premature mortality from non-communicable diseases through prevention and treatment and promote mental health and well-being"},
                    {value:"3.5",text:"3.5 Strengthen the prevention and treatment of substance abuse, including narcotic drug abuse and harmful use of alcohol"},
                    {value:"3.6",text:"3.6 By 2020, halve the number of global deaths and injuries from road traffic accidents"},
                    {value:"3.7",text:"3.7 By 2030, ensure universal access to sexual and reproductive health-care services, including for family planning, information and education, and the integration of reproductive health into national strategies and programmes"},
                    {value:"3.8",text:"3.8 Achieve universal health coverage, including financial risk protection, access to quality essential health-care services and access to safe, effective, quality and affordable essential medicines and vaccines for all"},
                    {value:"3.9",text:"3.9 By 2030, substantially reduce the number of deaths and illnesses from hazardous chemicals and air, water and soil pollution and contamination"},
                    {value:"3.a",text:"3.a Strengthen the implementation of the World Health Organization Framework Convention on Tobacco Control in all countries, as appropriate"},
                    {value:"3.b",text:"3.b Support the research and development of vaccines and medicines for the communicable and non-communicable diseases that primarily affect developing countries, provide access to affordable essential medicines and vaccines, in accordance with the Doha Declaration on the TRIPS Agreement and Public Health, which affirms the right of developing countries to use to the full the provisions in the Agreement on Trade-Related Aspects of Intellectual Property Rights regarding flexibilities to protect public health, and, in particular, provide access to medicines for all"},
                    {value:"3.c",text:"3.c Substantially increase health financing and the recruitment, development, training and retention of the health workforce in developing countries, especially in least developed countries and small island developing States"},
                    {value:"3.d",text:"3.d Strengthen the capacity of all countries, in particular developing countries, for early warning, risk reduction and management of national and global health risks"}]},
                {value:3,text:"SDG 4 Quality Education",targets:[{value:"4.1",text:"4.1 By 2030, ensure that all girls and boys complete free, equitable and quality primary and secondary education leading to relevant and effective learning outcomes"},
                    {value:"4.2",text:"4.2 By 2030, ensure that all girls and boys have access to quality early childhood development, care and pre-primary education so that they are ready for primary education"},
                    {value:"4.3",text:"4.3 By 2030, ensure equal access for all women and men to affordable and quality technical, vocational and tertiary education, including university"},
                    {value:"4.4",text:"4.4 By 2030, substantially increase the number of youth and adults who have relevant skills, including technical and vocational skills, for employment, decent jobs and entrepreneurship"},
                    {value:"4.5",text:"4.5 By 2030, eliminate gender disparities in education and ensure equal access to all levels of education and vocational training for the vulnerable, including persons with disabilities, indigenous peoples and children in vulnerable situations"},
                    {value:"4.6",text:"4.6 By 2030, ensure that all youth and a substantial proportion of adults, both men and women, achieve literacy and numeracy"},
                    {value:"4.7",text:"4.7 By 2030, ensure that all learners acquire the knowledge and skills needed to promote sustainable development, including, among others, through education for sustainable development and sustainable lifestyles, human rights, gender equality, promotion of a culture of peace and non-violence, global citizenship and appreciation of cultural diversity and of culture’s contribution to sustainable development"},
                    {value:"4.a",text:"4.a Build and upgrade education facilities that are child, disability and gender sensitive and provide safe, non-violent, inclusive and effective learning environments for all"},
                    {value:"4.b",text:"4.b By 2020, substantially expand globally the number of scholarships available to developing countries, in particular least developed countries, small island developing States and African countries, for enrolment in higher education, including vocational training and information and communications technology, technical, engineering and scientific programmes, in developed countries and other developing countries"},
                    {value:"4.c",text:"4.c By 2030, substantially increase the supply of qualified teachers, including through international cooperation for teacher training in developing countries, especially least developed countries and small island developing States"}]},
                {value:4,text:"SDG 5 Gender Equality",targets:[]},
                {value:5,text:"SDG 6 Clean Water and Sanitation",targets:[]}
            ]


    },
    getters: {
        certificateForm: state => {
            return state.certificate
        },
        sdgs: state => {
            return state.sdgs
        },
        payload: state =>{
            return {
                name: state.certificate.name,
                organizationID:1,
                description: state.certificate.description,
                applicationLength:state.certificate.applicationLength,
                difficulty: state.certificate.difficulty,
                relevance: state.certificate.relevance,
                validity:state.certificate.validity,
                goal: state.certificate.goal,
                specificity:state.certificate.rating,
                pricing: state.certificate.pricing,
                sdgEngagement: state.certificate.sdgEngagement
            }
        }
    },
    mutations: {
        changeCertificate (state, payload) {
            state.certificate = payload
        },
        addSdgs(state, payload){
            state.certificate.sdgs = payload
        },
        addSdgTargets(state, payload){
            state.certificate.sdgTargets = payload
        },
        addIndustrySectors(state, payload){
            state.certificate.sdgTargets = payload
        },

        resetCertificate (state){
            state.certificate = {
                name: "",
                applicationLength: "",
                difficulty: null,
                relevance: null,
                validity: null,
                region: null,
                countries:[],
                goal:null,
                rating:"P3",
                pricing:"",
                sdgEngagement:"",
                sdgs:[],
                sdgTargets:[],
                industries:[],
                industrySectors:[]
            }
        }

    },
    actions: {}
});
