"use strict";

// const i18n = require("../i18n.config");

module.exports = class Response {
    static genQuickReply(text, quickReplies) {
        let response = {
            text: text,
            quick_replies: []
        };

        return response;
    }
    static genListReply() {
        let response = {
            attatchment: {
                type: "template",
                payload: {
                    "template_type": "list",
                    "top_element_style": "compact",
                    "elements": [{
                            "title": "<TITLE_TEXT>",
                            //"subtitle": "<SUBTITLE_TEXT>",
                            "image_url": "<IMAGE_URL_FOR_THUMBNAIL>",
                            "default_action": {
                                "type": "web_url",
                                "url": "<URL_TO_OPEN_WHEN_ITEM_IS_TA  PPED>",
                                "messenger_extensions": true,
                                "webview_height_ratio": "tall"
                            }
                        },
                        {
                            "title": "<TITLE_TEXT>",
                            //"subtitle": "<SUBTITLE_TEXT>",
                            "image_url": "<IMAGE_URL_FOR_THUMBNAIL>",
                            "default_action": {
                                "type": "web_url",
                                "url": "<URL_TO_OPEN_WHEN_ITEM_IS_TAPPED>",
                                "messenger_extensions": true,
                                "webview_height_ratio": "tall"
                            }
                        },
                        {
                            "title": "<TITLE_TEXT>",
                            //"subtitle": "<SUBTITLE_TEXT>",
                            "image_url": "<IMAGE_URL_FOR_THUMBNAIL>",
                            "default_action": {
                                "type": "web_url",
                                "url": "<URL_TO_OPEN_WHEN_ITEM_IS_TAPPED>",
                                "messenger_extensions": true,
                                "webview_height_ratio": "tall"
                            }
                        }

                    ],

                }
            }
        }
        return response;
    }
};