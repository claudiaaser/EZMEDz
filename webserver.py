from flask import Flask, redirect, url_for, render_template, request
import cv2
from pyzbar.pyzbar import decode
from datetime import date
from csv_operations import create_cabinet 
from generate_medical_box import add_medical_box


app = Flask(__name__)


#creating the tool that will return the barcode numbers 
def read_barcodes(frame):
    barcodes = decode(frame)
    for barcode in barcodes:
        barcode_info = barcode.data.decode('utf-8')
        return barcode_info
    return None


#creating the homepage route
@app.route("/")
def home():
    return render_template("HTML_template1.html")

# creating the camera route; the camera runs until the barcode reading tool retrieves the number.
# The date of today is also retrieved in order to display it as value in the purchase date input box.
@app.route("/camera")
def open_camera():
    camera = cv2.VideoCapture(0)
    barcode = None
    while True:
        ret, frame = camera.read()
        #cv2.imshow('Barcode/QR code reader', frame)
        barcode = read_barcodes(frame)
        print("Found barcode: " + str(barcode))
        if not (barcode is None):
            break
    camera.release()
    cv2.destroyAllWindows()
    year_month_day = date.today()
    return render_template("barcode.html", barcode=barcode, todays_date = year_month_day)

    
#creating the input route. We are retrieving the barcode number,the purchase date, the expiry date and the doctor's instructions
@app.route("/input", methods=["POST"])
def input_y():
    print(request.form)
    add_medical_box(request.form["barcode"], request.form["purchase_date"], request.form["expiry_date"], request.form["doctor_instructions"])
    return render_template("inv_scan.html")

#creating the cabinet route. The function create_cabinet() is a backend function which retrieves the cabinet values from the cabinet csv file.
@app.route("/cabinet")
def choose():
    cabinet = create_cabinet()
    return render_template("inventory.html", cabinet=cabinet)
 


if __name__ == "__main__":
    app.run(debug=True)


