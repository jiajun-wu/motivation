const Response = require(response);

module.exports = class Curation {
    constructor(user, webhookEvent) {
        this.user = user
        this.webhookEvent = webhookEvent;
    }

    handlePayload(payload) {
        let response;

        switch (payload) {
            case "CURRATION_MUSIC":
                break;
            case "CURRATION_COOKING":
                break;
            case "CURRATION_ART":
                break;
            case "CURRATION_PIANO":
                break;
            case "CURRATION_GUITAR":
                break;
            case "CURRATION_ASIAN":
                break;
            case "CURRATION_EUROPEAN":
                break;
            case "CURRATION_AMERICAN":
                break;
            case "CURRATION_PENCIL":
                break;
            case "CURRATION_PAINT":
                break;

        }
    }


}