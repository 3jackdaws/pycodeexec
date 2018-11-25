LANGUAGES = {
    "python": {
        "aliases": [

        ],
        "versions": {
            "default": {
                "image": "python",
                "tag": "latest",
                "command": 'python -c "{}"'
            },
            "3.6": {
                "tag": "3.6-alpine"
            },
            "2": {
                "tag": "2.7-alpine"
            }
        }
    },
    "javascript": {
        "aliases": [
            "js",
            "node",
            "nodejs"
        ],
        "versions": {

        }
    }
}
