from flask import Flask, request, render_template, send_file, jsonify
from xhtml2pdf import pisa
from io import BytesIO
from threading import Thread
from scanner_engine import crawl_and_scan

app = Flask(__name__)

# Global scan data to track status
scan_data = {
    "pages": [],
    "vulnerabilities": [],
    "progress": 0,
    "target": ""
}

# Background scan thread logic
def run_scan(target_url):
    print(f"▶️ Scan started on: {target_url}")
    scan_data["progress"] = 0
    scan_data["target"] = target_url

    pages, vulnerabilities = crawl_and_scan(target_url)

    print(f"➡️ Pages: {len(pages)}")
    print(f"➡️ Vulns: {len(vulnerabilities)}")

    scan_data["pages"] = pages
    scan_data["vulnerabilities"] = vulnerabilities
    scan_data["progress"] = 100

    print(f"✅ Scan complete!")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/progress')
def progress():
    return render_template("progress.html", scan_data=scan_data)

@app.route('/report')
def report():
    return render_template("report.html", scan_data=scan_data)



from flask import redirect, url_for

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form['url']
    scan_data["progress"] = 0
    scan_data["pages"] = []
    scan_data["vulnerabilities"] = []

    thread = Thread(target=run_scan, args=(url,))
    thread.start()

    print("🚦 Background scan thread started.")
    return redirect(url_for('progress'))  # ✅ redirect to GET-safe route


@app.route('/download', methods=['GET'])
def download_pdf():
    from xhtml2pdf import pisa
    from io import BytesIO

    html = render_template("report.html", scan_data=scan_data)
    pdf = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=pdf)

    if pisa_status.err:
        return "PDF generation failed", 500

    pdf.seek(0)
    return send_file(pdf, as_attachment=True, download_name="scan_report.pdf")

if __name__ == "__main__":
    print("🚀 Flask app starting at http://127.0.0.1:5000")
    app.run(debug=True)
