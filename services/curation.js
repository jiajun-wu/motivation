const Response = require(response);

module.exports = class Curation {
    constructor(user, webhookEvent) {
        this.user = user
        this.webhookEvent = webhookEvent;
    }

    handlePayload(payload) {
        let response;

        switch (payload) {
            case "CURRATION":
                response = Response.genQuickReply((curation.prompt), [{
                        title: ("curation.music"),
                        payload: "CURATION_MUSIC"
                    },
                    {
                        title: ("curation.cooking"),
                        payload: "CURATION_COOKING"
                    },
                    {
                        title: ("curation.art"),
                        payload: "CURATION_ART"
                    }
                ]);
                break;
            case "CURRATION_MUSIC":
                response = Response.genQuickReply((curation.instrument), [{
                        title: ("curation.piano"),
                        payload: "CURATION_PIANO"
                    },
                    {
                        title: ("curation.guitar"),
                        payload: "CURATION_GUITAR"
                    }
                ]);
                break;
            case "CURRATION_COOKING":
                response = Response.genQuickReply((curation.culture), [{
                        title: ("curation.asian"),
                        payload: "CURATION_ASIAN"
                    },
                    {
                        title: ("curation.european"),
                        payload: "CURATION_EUROPEAN"
                    },
                    {
                        title: ("curation.american"),
                        payload: "CURATION_AMERICAN"
                    }
                ]);
                break;
            case "CURRATION_ART":
                response = Response.genQuickReply((curation.style), [{
                        title: ("curation.pencil"),
                        payload: "CURATION_PENCIL"
                    },
                    {
                        title: ("curation.paint"),
                        payload: "CURATION_PAINT"
                    }
                ]);
                break;
            case "CURRATION_PIANO":
                //list
                break;
            case "CURRATION_GUITAR":
                //list
                break;
            case "CURRATION_ASIAN":
                //list
                break;
            case "CURRATION_EUROPEAN":
                //list
                break;
            case "CURRATION_AMERICAN":
                //list
                break;
            case "CURRATION_PENCIL":
                //list
                break;
            case "CURRATION_PAINT":
                //list
                break;

        }
        return response;
    }


}