from flask import Flask,request, render_template
import pickle
from sklearn.preprocessing  import StandardScaler
scaler =StandardScaler()

model = pickle.load(open("model_pickle.pkl",'rb'))

app = Flask(__name__)
@app.route('/analysis')
def analysis():
    return render_template("stroke.html")

@app.route('/', methods=['GET','POST'])
def home():
    if request.method =="POST":
        gender = request.form["gender"]
        age = int(request.form["age"])
        hypertension = int(request.form["hypertension"])
        disease = int(request.form["disease"])
        married = request.form["married"]
        work = request.form["work"]
        residence = request.form["residence"]
        glucose = float(request.form["glucose"])
        bmi = float(request.form["bmi"])
        smoking = request.form["smoking"]

        #gender
        if gender =="Male":
            gender_Male=1
            gender_other=0
        elif(gender =="other"):
            gender_Male=0
            gender_other=1
        else:
            gender_Male=0
            gender_other=0

        #married
        if married =="Yes":
            married_Yes=1
        else:
            married_Yes=0 

        #work type
        if(work =='self-employed'):
            work_type_Never_worked =0
            work_type_private =0
            work_type_Self_employed =1
            work_type_childern =0
        elif(work =='private'):
            work_type_Never_worked =0
            work_type_private =1
            work_type_Self_employed =0
            work_type_childern =0 
        elif(work =='childern'):
            work_type_Never_worked =0
            work_type_private =1
            work_type_Self_employed =0
            work_type_childern =1 
        elif(work =='Never_worked'):
            work_type_Never_worked =1
            work_type_private =0
            work_type_Self_employed =0
            work_type_childern =0
        else:
             work_type_Never_worked =0
             work_type_private =0
             work_type_Self_employed =0
             work_type_childern =0


        #residence
        if (residence=="Urban"):
            Residence_type_Urban=1
        else:
            Residence_type_Urban=0


        #smoking status
        if(smoking=="formely smoked"):
            smoking_status_formely_smoked =1
            smoking_status_never_smoked =0
            smoking_status_smokes=0
        elif(smoking=="smokes"):
            smoking_status_formely_smoked =0
            smoking_status_never_smoked =0
            smoking_status_smokes=1
        elif(smoking=="never smokes"):
            smoking_status_formely_smoked =0
            smoking_status_never_smoked =1
            smoking_status_smokes=0
        else:
            smoking_status_formely_smoked =0
            smoking_status_never_smoked =0
            smoking_status_smokes=0

        feature = scaler.fit_transform([[age,hypertension,disease,glucose,bmi,gender_Male,gender_other,married_Yes,work_type_Never_worked,
                                         work_type_private,work_type_Self_employed,work_type_childern,Residence_type_Urban,smoking_status_formely_smoked,
                                         smoking_status_never_smoked,smoking_status_smokes]])
        
        predicition =model.predict(feature)
        #print(predicition)
        if predicition ==0:
             predicition = "No"
        else:
            predicition ="Yes"    

        return render_template("index.html", predicition_text ="chance of stroke is --> {}".format(predicition))
    else:
        return render_template("index.html")
    

if __name__ =="__main__":
    app.run(debug=True)  