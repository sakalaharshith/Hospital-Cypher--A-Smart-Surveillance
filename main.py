import untitled2
import facerecognition
import face_recognition
#import FirebaseHC
from functools import partial
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from functions import *
from pyrebase import *
import click
import cv2
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from random import randrange
from mail import *

global i
i=0
firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
# cred = credentials.Certificate(firebase_aconfig)
# firebase_admin.initialize_app(cred)
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_aconfig)
    default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

root = Tk()
root.minsize(height=800, width=800)
root.maxsize(height=800, width=800)
root.title("Splash Screen")
root.configure()
img_path = "logo.png"
image = Image.open(img_path)
image = image.resize((300, 300), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
my = Label(root, image=img)
my.image = img
my.place(x=250, y=150)
name = Label(root, text="Hospital Cipher", font=("Ubuntu", 32))
name.place(x=260, y=450)


########################################################################################################################

# AUTHENTICATION PART

# login page
def mainroot(signup_root):
    signup_root.destroy()
    login_root = Tk()
    login_root.geometry('800x800')
    login_root.minsize(width=800, height=800)
    login_root.maxsize(width=800, height=800)
    login_root.configure(bg='white')
    login_root.title("Login")

    # frame
    frame1 = Frame(login_root, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=650,
                   height=650, bd=0)
    frame1.pack(fill="both", expand=False, padx=60, pady=70)
    img_path = "logo.png"
    image = Image.open(img_path)
    image = image.resize((150, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    my = Label(frame1, image=img)
    my.image = img
    my.place(x=0, y=0)
    name = Label(frame1, text="Hospital Cipher", font=("Ubuntu", 30))
    name.place(x=160, y=55)

    # validation
    def validateLogin(username, password):
        try:
            auth.sign_in_with_email_and_password(username.get(), password.get())
            # messagebox.showinfo("Info", "You Logged in")
            dashboard(login_root)
        # print("1")
        except:
            messagebox.showerror("Error", "Looks like something's wrong please try again.")
        # print("0")

    def tosignUp(event):
        signup(login_root)

    def toforgotpswd(event):
        forgot_password(login_root)

    # email
    email_txt = Label(frame1, text="Email", font=("Ubuntu", 15)).place(x=160, y=200)
    email_type = StringVar()
    email = Entry(frame1, show=None, highlightthickness=2, textvariable=email_type, font=("Ubuntu", 13)).place(x=160,
                                                                                                               y=240,
                                                                                                               height=40,
                                                                                                               width=300)

    # password
    pswd_txt = Label(frame1, text="Password", font=("Ubuntu", 15)).place(x=160, y=300)
    password_type = StringVar()
    pswd = Entry(frame1, show='*', highlightthickness=2, textvariable=password_type, font=('Ubuntu', 14)).place(x=160,
                                                                                                                y=340,
                                                                                                                height=40,
                                                                                                                width=300)

    # forgot password
    fpswd_txt = Label(frame1, fg='#8AA2D4', text="forgot password?", font=("Ubuntu", 13))
    fpswd_txt.place(x=160, y=400)
    fpswd_txt.bind('<Button-1>', toforgotpswd)

    # new user
    newuser_txt = Label(frame1, fg='#8AA2D4', text="new user?", font=("Ubuntu", 13))
    newuser_txt.place(x=380, y=400)
    newuser_txt.bind('<Button-1>', tosignUp)

    # sending given values for validation
    validateLogin = partial(validateLogin, email_type, password_type)

    # login button
    loginButton = Button(frame1, bg='#8AA2D4', fg='#fff', text="Login", command=validateLogin, font=("Ubuntu", 15),
                         activebackground='#8AA2D4', activeforeground='#fff', borderwidth=0, relief=tk.RIDGE).place(
        x=160, y=440, height=40, width=180)


# signup
def signup(login_root):
    login_root.destroy();
    signup_root = Tk()
    signup_root.geometry('800x800')
    signup_root.minsize(width=800, height=800)
    signup_root.maxsize(width=800, height=800)
    signup_root.configure(bg='white')
    signup_root.title("Sign Up")

    # frame
    frame1 = Frame(signup_root, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=650,
                   height=650, bd=0)
    frame1.pack(fill="both", expand=False, padx=60, pady=70)
    img_path = "logo.png"
    image = Image.open(img_path)
    image = image.resize((150, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    my = Label(frame1, image=img)
    my.image = img
    my.place(x=0, y=0)
    name = Label(frame1, text="Hospital Cipher", font=("Ubuntu", 30))
    name.place(x=160, y=55)

    # email
    email_txt = Label(frame1, text="Email", font=("Ubuntu", 15)).place(x=160, y=200)
    email_type = StringVar()
    email = Entry(frame1, show=None, highlightthickness=2, textvariable=email_type, font=("Ubuntu", 13)).place(x=160,
                                                                                                               y=240,
                                                                                                               height=40,
                                                                                                               width=300)

    # password
    pswd_txt = Label(frame1, text="Password", font=("Ubuntu", 15)).place(x=160, y=300)
    password_type = StringVar()
    pswd = Entry(frame1, show='*', highlightthickness=2, textvariable=password_type, font=('Ubuntu', 14)).place(x=160,
                                                                                                                y=340,
                                                                                                                height=40,
                                                                                                                width=300)

    # validation
    def validateSignup(username, password):
        try:
            auth.create_user_with_email_and_password(username.get(), password.get())
            code = randrange(1000, 9999)
            db.collection("users").add({"email": username.get(), "code": code, 'password': password.get()})
            # print(1)
            messagebox.showinfo("Info", "Your account is created")
            mainroot(signup_root)

        except:
            messagebox.showerror("Error", "Looks like something's wrong please try again.")
        # print(0)

    # backtoLogin
    def backtoLogin():
        mainroot(signup_root)

    # sending given values for validation
    validateSignup = partial(validateSignup, email_type, password_type)

    # signup button
    signupButton = Button(frame1, bg='#8AA2D4', fg='#fff', text="Sign Up", command=validateSignup, font=("Ubuntu", 15),
                          activebackground='#8AA2D4', activeforeground='#fff', borderwidth=0, relief=tk.RIDGE).place(
        x=160, y=400, height=40, width=100)

    # back button
    backButton = Button(frame1, bg='#8AA2D4', fg='#fff', text="Back", command=backtoLogin, font=("Ubuntu", 15),
                        activebackground='#8AA2D4', activeforeground='#fff', borderwidth=0, relief=tk.RIDGE).place(
        x=360, y=400, height=40, width=100)


# forgot password
def forgot_password(login_root):
    login_root.destroy();
    forgot_password_root = Tk()
    forgot_password_root.geometry('800x800')
    forgot_password_root.minsize(width=800, height=800)
    forgot_password_root.maxsize(width=800, height=800)
    forgot_password_root.configure(bg='white')
    forgot_password_root.title("Forgot Password")

    # backtoLogin
    def backtoLogin():
        mainroot(forgot_password_root)

    # verifyCode
    def code_Verify(email):
        data = db.collection("users").where("email", "==", email.get()).get()
        obj = []
        if (len(data) >= 1):
            for doc in data:
                obj = doc.to_dict()
            mail_sent = mail(obj["email"], str(obj["code"]))
            if (mail_sent == 1):
                messagebox.showinfo("Info", "Your code has been sent to your registered email account.")
                codeVerify(forgot_password_root, email.get())

            else:
                messagebox.showerror("Error", "Unable to send the mail. Please try again.")
            # print("Unable send Mail")
        else:
            messagebox.showerror("Error", "Mail not found")
        # print("No Email Found")

    # frame
    frame1 = Frame(forgot_password_root, highlightbackground="black", highlightcolor="black", highlightthickness=1,
                   width=650, height=650, bd=0)
    frame1.pack(fill="both", expand=False, padx=60, pady=70)
    img_path = "logo.png"
    image = Image.open(img_path)
    image = image.resize((150, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    my = Label(frame1, image=img)
    my.image = img
    my.place(x=0, y=0)
    name = Label(frame1, text="Hospital Cipher", font=("Ubuntu", 30))
    name.place(x=160, y=55)

    fpswd_txt = Label(frame1, fg='#8AA2D4',
                      text="Enter your registered email id to recieve your PIN ID. If not sign up.",
                      font=("Ubuntu", 15)).place(x=40, y=200)

    email_txt = Label(frame1, text="Email", font=("Ubuntu", 15)).place(x=160, y=260)
    email_type = StringVar()
    email = Entry(frame1, show=None, highlightthickness=2, textvariable=email_type, font=("Ubuntu", 13)).place(x=160,
                                                                                                               y=300,
                                                                                                               height=40,
                                                                                                               width=280)
    code_Verify = partial(code_Verify, email_type)
    # submit button
    submitButton = Button(frame1, bg='#8AA2D4', fg='#fff', text="Submit", command=code_Verify, font=("Ubuntu", 15),
                          activebackground='#8AA2D4', activeforeground='#fff', borderwidth=0, relief=tk.RIDGE).place(
        x=160, y=360, height=40, width=100)

    # back button
    backButton = Button(frame1, bg='#8AA2D4', fg='#fff', text="Back", command=backtoLogin, font=("Ubuntu", 15),
                        activebackground='#8AA2D4', activeforeground='#fff', borderwidth=0, relief=tk.RIDGE).place(
        x=340, y=360, height=40, width=100)


# codeVerify
def codeVerify(forgot_password_root, email):
    forgot_password_root.destroy();
    verify_root = Tk()
    verify_root.geometry('800x800')
    verify_root.minsize(width=800, height=800)
    verify_root.maxsize(width=800, height=800)
    verify_root.configure(bg='white')
    verify_root.title("Verification")

    # back to forgot password
    def backtofpswd():
        forgot_password(verify_root)

    # to reset
    def re_set(pin_code):
        pin = str(pin_code.get())
        if (pin == "" or len(pin) <= 0):
            messagebox.showerror("Error", "Enter the PIN. Please try again.")
        else:
            docs = db.collection("users").where('email', '==', email).get()
            if (pin == str(docs[0].to_dict()['code'])):
                db.collection('users').document(docs[0].id).update({'code': randrange(1000, 9999)})
                reset_password(verify_root, email)
            else:
                messagebox.showerror("Error", "Incorrect PIN. Please try again.")

    # frame
    frame1 = Frame(verify_root, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=650,
                   height=650, bd=0)
    frame1.pack(fill="both", expand=False, padx=60, pady=70)
    img_path = "logo.png"
    image = Image.open(img_path)
    image = image.resize((150, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    my = Label(frame1, image=img)
    my.image = img
    my.place(x=0, y=0)
    name = Label(frame1, text="Hospital Cipher", font=("Ubuntu", 30))
    name.place(x=160, y=55)

    fpswd_txt = Label(frame1, fg='#8AA2D4', text="Enter your recieved your PIN ID. If not sign up.",
                      font=("Ubuntu", 15)).place(x=120, y=200)

    # password
    pswd_txt = Label(frame1, text="PIN ID", font=("Ubuntu", 15)).place(x=160, y=300)
    password_type = StringVar()
    pswd = Entry(frame1, highlightthickness=2, textvariable=password_type, font=('Ubuntu', 14)).place(x=160, y=340,
                                                                                                      height=40,
                                                                                                      width=300)

    # sending given values for validation
    re_set = partial(re_set, password_type)

    # reset button
    resetButton = Button(frame1, bg='#8AA2D4', fg='#fff', text="Reset", command=re_set, font=("Ubuntu", 15),
                         activebackground='#8AA2D4', activeforeground='#fff', borderwidth=0, relief=tk.RIDGE).place(
        x=160, y=400, height=40, width=100)

    # back button
    backButton = Button(frame1, bg='#8AA2D4', fg='#fff', text="Back", command=backtofpswd, font=("Ubuntu", 15),
                        activebackground='#8AA2D4', activeforeground='#fff', borderwidth=0, relief=tk.RIDGE).place(
        x=360, y=400, height=40, width=100)


# reset password
def reset_password(verify_root, email):
    verify_root.destroy();
    reset_root = Tk()
    reset_root.geometry('800x800')
    reset_root.minsize(width=800, height=800)
    reset_root.maxsize(width=800, height=800)
    reset_root.configure(bg='white')
    reset_root.title("Reset Paasword")

    # frame
    frame1 = Frame(reset_root, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=650,
                   height=650, bd=0)
    frame1.pack(fill="both", expand=False, padx=60, pady=70)
    img_path = "logo.png"
    image = Image.open(img_path)
    image = image.resize((150, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    my = Label(frame1, image=img)
    my.image = img
    my.place(x=0, y=0)
    name = Label(frame1, text="Hospital Cipher", font=("Ubuntu", 30))
    name.place(x=160, y=55)

    # new password
    npswd_txt = Label(frame1, text="New Password", font=("Ubuntu", 15)).place(x=160, y=200)
    npswd_type = StringVar()
    npswd = Entry(frame1, show='*', highlightthickness=2, textvariable=npswd_type, font=("Ubuntu", 13)).place(x=160,
                                                                                                              y=240,
                                                                                                              height=40,
                                                                                                              width=300)

    # confirm password
    cpswd_txt = Label(frame1, text="Confirm Password", font=("Ubuntu", 15)).place(x=160, y=300)
    cpassword_type = StringVar()
    cpswd = Entry(frame1, show='*', highlightthickness=2, textvariable=cpassword_type, font=('Ubuntu', 14)).place(x=160,
                                                                                                                  y=340,
                                                                                                                  height=40,
                                                                                                                  width=300)

    # validation
    def validateReset(npassword, cpassword):
        if (len(npassword.get())==0 or len(cpassword.get())==0):
            messagebox.showerror("ERROR","One of The Fields are empty")
        else:
            
            if (npassword.get() == cpassword.get()):
                docs = db.collection("users").where('email', '==', email).get()
                password = docs[0].to_dict()['password']
                try:
                    auth.current_user = ""
                    user = auth.sign_in_with_email_and_spassword(email, password)
                    auth.delete_user_account(user['idToken'])
                    auth.create_user_with_email_and_password(email, npassword.get())
                    db.collection('users').document(docs[0].id).update({'password': npassword.get()})
                    messagebox.showinfo("Info", "Done changing password press back to login.")
                    print("1")
                except:
                    messagebox.showinfo("Info", "Done changing password press back to login.")
            # print("0")
            else:
                messagebox.showerror("Error", "Passwords do not match please try again.")

    # backtoLogin
    def backtoVerify():
        mainroot(reset_root)

    # sending given values for validation
    validateReset = partial(validateReset, npswd_type, cpassword_type)

    # reset button
    resetButton = Button(frame1, bg='#8AA2D4', fg='#fff', text="reset", command=validateReset, font=("Ubuntu", 15),
                         activebackground='#8AA2D4', activeforeground='#fff', borderwidth=0, relief=tk.RIDGE).place(
        x=160, y=400, height=40, width=100)

    # Back button
    backButton = Button(frame1, bg='#8AA2D4', fg='#fff', text="Back", command=backtoVerify, font=("Ubuntu", 15),
                        activebackground='#8AA2D4', activeforeground='#fff', borderwidth=0, relief=tk.RIDGE).place(
        x=360, y=400, height=40, width=100)


########################################################################################################################

# DASHBOARD PART

def dashboard(login_root):
    login_root.destroy();
    dashboard_root = Tk()
    dashboard_root.geometry('800x800')
    dashboard_root.minsize(width=800, height=800)
    dashboard_root.maxsize(width=800, height=800)
    dashboard_root.configure(bg='white')
    dashboard_root.title("Dashboard")

    # frame
    frame1 = Frame(dashboard_root, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=650,
                   height=650, bd=0)
    frame1.pack(fill="both", expand=False, padx=60, pady=70)
    img_path = "logo.png"
    image = Image.open(img_path)
    image = image.resize((150, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    my = Label(frame1, image=img)
    my.image = img
    my.place(x=100, y=0)
    name = Label(frame1, text="Hospital Cipher", font=("Ubuntu", 30))
    name.place(x=240, y=55)

    def patientReg():
        patientRegistration(dashboard_root)

    def surveillance():
        capture = cv2.VideoCapture(0)
        flag,img = capture.read()
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        location=face_recognition.face_locations(img)
        if len(location)>=1:
            facerecognition.imgrecog()
        else:
            facemask_recognition.get()
        
        

    def imgRecognition():
        facerecognition.imgrecog()

    def faceMaskDetection():
        facemask_recogntion.get()


    def logout():
        try:
            mainroot(dashboard_root)

        except:
            messagebox.showerror("Error", "Looks like something's wrong please try again.")

    # PAITENT REGISTRATION BUTTON
    patient_reg_btn = Button(frame1, bg='#8AA2D4', fg='#fff', text="Paitent Registration", command=patientReg,
                             font=("Ubuntu", 17), activebackground='#8AA2D4', activeforeground='#fff', borderwidth=0,
                             relief=tk.RIDGE).place(x=165, y=180, height=50, width=350)

    # SURVEILLANCE BUTTON
    surveillance_btn = Button(frame1, bg='#8AA2D4', fg='#fff', text="Surveillance", command=surveillance,
                              font=("Ubuntu", 17), activebackground='#8AA2D4', activeforeground='#fff', borderwidth=0,
                              relief=tk.RIDGE).place(x=165, y=280, height=50, width=350)

    # IMAGE RECOGNITION
    img_recognition_btn = Button(frame1, bg='#8AA2D4', fg='#fff', text="Image Recognition", command=imgRecognition,
                                 font=("Ubuntu", 17), activebackground='#8AA2D4', activeforeground='#fff',
                                 borderwidth=0, relief=tk.RIDGE).place(x=165, y=380, height=50, width=350)

    # FACE MASK DETECTION
    face_mask_detection_btn = Button(frame1, bg='#8AA2D4', fg='#fff', text="Face Mask Detection",
                                     command=faceMaskDetection, font=("Ubuntu", 17), activebackground='#8AA2D4',
                                     activeforeground='#fff', borderwidth=0, relief=tk.RIDGE).place(x=165, y=480,
                                                                                                    height=50,
                                                                                                    width=350)

    # LOGOUT
    logout_btn = Button(frame1, bg='#8AA2D4', fg='#fff', text="Logout", command=logout, font=("Ubuntu", 17),
                        activebackground='#8AA2D4', activeforeground='#fff', borderwidth=0, relief=tk.RIDGE).place(
        x=165, y=580, height=50, width=350)


# PAITIENT REGISTRATION
def patientRegistration(dashboard_root):
    dashboard_root.destroy();
    dashboard_root = Tk()
    dashboard_root.geometry('800x800')
    dashboard_root.minsize(width=800, height=800)
    dashboard_root.maxsize(width=800, height=800)
    dashboard_root.configure(bg='white')
    dashboard_root.title("Patient Registration")

    # frame
    frame1 = Frame(dashboard_root, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=650,
                   height=650, bd=0)
    frame1.pack(fill="both", expand=False, padx=60, pady=70)
    img_path = "logo.png"
    image = Image.open(img_path)
    image = image.resize((150, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    my = Label(frame1, image=img)
    my.image = img
    my.place(x=0, y=0)
    name = Label(frame1, text="Hospital Cipher", font=("Ubuntu", 30))
    name.place(x=160, y=55)

    patient_reg_txt = Label(frame1, text="Patient Registration", font=("Ubuntu", 20)).place(x=220, y=150)
    
    def uploadImage(patient, npatient):
        a = patient.get()
        b = npatient.get()
        capture = cv2.VideoCapture(0)
        flag,img = capture.read()
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        location=face_recognition.face_locations(img)
        if len(location)>=1 and len(a)>0 and len(b)>0:
            cv2.imwrite("images/"+a+b+".jpg",img)
            messagebox.showinfo("INFO","Sucessfully image created")
            i=1
        else:
            messagebox.showerror("Error"," Either Face is not visible to camera please retake the photo or you might have skipped one of the fields of entry")
        
        
        

    
    def backToDashboard():
        dashboard(dashboard_root)

    # PATIENT NAME
    patient_txt = Label(frame1, text="Patient Name", font=("Ubuntu", 15)).place(x=220, y=240)
    patient_type = StringVar()
    patient = Entry(frame1, highlightthickness=2, textvariable=patient_type, font=("Ubuntu", 13)).place(x=220, y=280,
                                                                                                        height=40,
                                                                                                        width=300)

    # PATIENT NUMBER
    npatient_txt = Label(frame1, text="Patient Number", font=("Ubuntu", 15)).place(x=220, y=340)
    npatient_type = StringVar()
    npatient = Entry(frame1, highlightthickness=2, textvariable=npatient_type, font=('Ubuntu', 14)).place(x=220, y=380,
                                                                                                         height=40,
                                                                                                          width=300)
    uploadImage = partial(uploadImage, patient_type, npatient_type)
    # UPLOAD IMAGE
    upload_pic_btn = Button(frame1, bg='#8AA2D4', fg='#fff', text="Add Image", command=uploadImage,
                            font=("Ubuntu", 15), activebackground='#8AA2D4', activeforeground='#fff', borderwidth=0,
                            relief=tk.RIDGE).place(x=220, y=440, height=40, width=300)

   
   
    # BACK TO DASHBOARD
    back_to_dashboard = Button(frame1, bg='#8AA2D4', fg='#fff', text="Back", command=backToDashboard,
                               font=("Ubuntu", 15), activebackground='#8AA2D4', activeforeground='#fff', borderwidth=0,
                               relief=tk.RIDGE).place(x=420, y=500, height=40, width=100)


########################################################################################################################

def call_mainroot():
    mainroot(root)


root.after(3000, call_mainroot)  # TimeOfSplashScreen
mainloop()