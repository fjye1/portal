from flask import current_app

def inject_urls():
    return {
        "EVENT_BUILDER_URL": current_app.config["EVENT_BUILDER_URL"]
    }