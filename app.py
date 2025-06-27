from flask import Flask, Response
import requests
import gzip
import io

app = Flask(__name__)

@app.route("/epg.xml")
def serve_epg():
    # Download the gzipped XMLTV file
    url = "https://epgshare01.online/epgshare01/epg_ripper_US_LOCALS2.xml.gz"
    r = requests.get(url, stream=True)
    if r.status_code != 200:
        return "Failed to fetch XMLTV", 500

    # Decompress .gz
    compressed = io.BytesIO(r.content)
    decompressed = gzip.GzipFile(fileobj=compressed).read()

    return Response(decompressed, mimetype='application/xml')
