from app import app


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):

    return info
