import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading models correctly in binary mode
dia_model = pickle.load(open(r"C:\Users\hp\ML file\diabetes_model.pkl", "rb"))
heart_model = pickle.load(open(r"C:\Users\hp\ML file\Heart_model.pkl", "rb"))
par_model = pickle.load(open(r"C:\Users\hp\ML file\parkisons_model.pkl", "rb"))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('E-Doctor Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Creating input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', "0")
    with col2:
        Glucose = st.text_input('Glucose Level', "0")
    with col3:
        BloodPressure = st.text_input('Blood Pressure value', "0")
    with col1:
        SkinThickness = st.text_input('Skin Thickness value', "0")
    with col2:
        Insulin = st.text_input('Insulin Level', "0")
    with col3:
        BMI = st.text_input('BMI value', "0")
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', "0")
    with col2:
        Age = st.text_input('Age of the person', "0")

    # Prediction
    if st.button('Diabetes Test Result'):
        try:
            # Convert input values to float
            input_data = [[float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                           float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]]
            
            diab_prediction = dia_model.predict(input_data)

            if diab_prediction[0] == 1:
                st.success('The person is diabetic')
            else:
                st.success('The person is not diabetic')
        except ValueError:
            st.warning("Please enter valid numeric values.")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age', "0")
    with col2:
        sex = st.text_input('Sex (0 = Female, 1 = Male)', "0")
    with col3:
        cp = st.text_input('Chest Pain Types (0-3)', "0")
    with col1:
        trestbps = st.text_input('Resting Blood Pressure', "0")
    with col2:
        chol = st.text_input('Serum Cholesterol (mg/dl)', "0")
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = Yes, 0 = No)', "0")
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results (0-2)', "0")
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved', "0")
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = Yes, 0 = No)', "0")
    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise', "0")
    with col2:
        slope = st.text_input('Slope of Peak Exercise ST Segment (0-2)', "0")
    with col3:
        ca = st.text_input('Major Vessels Colored by Fluoroscopy (0-4)', "0")
    with col1:
        thal = st.text_input('Thalassemia (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)', "0")

    # Prediction
    if st.button('Heart Disease Test Result'):
        try:
            input_data = [[float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
                           float(restecg), float(thalach), float(exang), float(oldpeak), float(slope), 
                           float(ca), float(thal)]]
            
            heart_prediction = heart_model.predict(input_data)

            if heart_prediction[0] == 1:
                st.success('The person has heart disease')
            else:
                st.success('The person does not have heart disease')
        except ValueError:
            st.warning("Please enter valid numeric values.")

# Parkinson's Disease Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson’s Disease Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo(Hz)', "0")
    with col2:
        MDVP_Fhi = st.text_input('MDVP:Fhi(Hz)', "0")
    with col3:
        MDVP_Flo = st.text_input('MDVP:Flo(Hz)', "0")
    with col1:
        MDVP_Jitter = st.text_input('MDVP:Jitter(%)', "0")
    with col2:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer', "0")

    # Prediction
    if st.button('Parkinson’s Test Result'):
        try:
            input_data = [[float(MDVP_Fo), float(MDVP_Fhi), float(MDVP_Flo), float(MDVP_Jitter), float(MDVP_Shimmer)]]

            par_prediction = par_model.predict(input_data)

            if par_prediction[0] == 1:
                st.success('The person has Parkinson’s Disease')
            else:
                st.success('The person does not have Parkinson’s Disease')
        except ValueError:
            st.warning("Please enter valid numeric values.")
