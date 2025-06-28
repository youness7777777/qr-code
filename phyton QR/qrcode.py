from flask import Flask, render_template, request
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_image = None
    if request.method == "POST":
        data = request.form["data"]
        if data:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill="black", back_color="white")

            buf = BytesIO()
            img.save(buf, format="PNG")
            buf.seek(0)
            qr_image = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
    return render_template("front.html", qr_image=qr_image)

if __name__ == "__main__":
    app.run(debug=True)
