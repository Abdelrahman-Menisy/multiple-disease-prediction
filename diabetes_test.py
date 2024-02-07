import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open(r'diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(r'heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(r'parkinsons_model.sav', 'rb'))

breast_cancer_model = pickle.load(open(r'Breast_cancer_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person','virus'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
            st.error(diab_diagnosis, icon="🚨")
        else:
            diab_diagnosis = 'The person is not diabetic'
            st.success(diab_diagnosis, icon="✅")
            st.balloons()

    

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
            st.error(heart_diagnosis, icon="🚨")
        else:
            heart_diagnosis = 'The person does not have any heart disease'
            st.success(heart_diagnosis, icon="✅")
            st.balloons()



# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
            st.error(parkinsons_diagnosis, icon="🚨")
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
            st.success(parkinsons_diagnosis, icon="✅")
            st.balloons()


# Breast cancer Prediction Page
if selected == "Breast Cancer Prediction":

    # page title
    st.title("Breast Cancer Prediction Prediction using ML")

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        radius = st.text_input('mean radius')

    with col2:
        texture = st.text_input('mean texture')

    with col3:
        perimeter = st.text_input('mean perimeter')

    with col4:
        area = st.text_input('mean area')

    with col5:
        mean_smoothness = st.text_input('mean smoothness')
        
    with col6:
        worst_fractal_dimension = st.text_input('worst fractal dimension')

    with col1:
        compactness = st.text_input('mean compactness')

    with col2:
        concavity = st.text_input('mean concavity')

    with col3:
        concave_points = st.text_input('mean concave points')

    with col4:
        mean_symmetry = st.text_input('mean symmetry')

    with col5:
        fractal_dimension = st.text_input('mean fractal dimension')
        
    with col6:
        worst_symmetry = st.text_input('worst symmetry')

    with col1:
        radius_error = st.text_input('radius error')

    with col2:
        texture_error = st.text_input('texture error')

    with col3:
        perimeter_error = st.text_input('perimeter error')

    with col4:
        area_error = st.text_input('area error')

    with col5:
        smoothness_error = st.text_input('smoothness error')
        
    with col6:
        worst_concave_points = st.text_input('worst concave points')

    with col1:
        compactness_error = st.text_input('compactness error')

    with col2:
        concavity_error = st.text_input('concavity error')

    with col3:
        concave_points_error = st.text_input('concave points error')

    with col4:
        symmetry_error = st.text_input('symmetry error')

    with col5:
        fractal_dimension_error = st.text_input('fractal dimension error')
        
    with col6:
        worst_concavity = st.text_input('worst concavity')

    with col1:
        worst_radius = st.text_input('worst radius')

    with col2:
        worst_texture = st.text_input('worst texture')
        
    with col3:
        worst_perimeter = st.text_input('worst perimeter')
    
    with col4:
        worst_area = st.text_input('worst area')
    
    with col5:
        worst_smoothness = st.text_input('worst smoothness')
        
    with col6:
        worst_compactness = st.text_input('worst compactness')

    # code for Prediction
    breast_cancer_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [radius, texture, perimeter, area, mean_smoothness,
                      compactness, concavity, concave_points,mean_symmetry,
                      fractal_dimension, radius_error, texture_error,
                      perimeter_error, area_error, smoothness_error, compactness_error, 
                      concavity_error, concave_points_error, symmetry_error,
                      fractal_dimension_error, worst_radius, worst_texture, worst_perimeter, 
                      worst_area, worst_smoothness, worst_compactness,worst_concavity,
                      worst_concave_points, worst_symmetry, worst_fractal_dimension]

        user_input = [float(x) for x in user_input]

        breast_cancer_prediction = breast_cancer_model.predict([user_input])

        if breast_cancer_prediction[0] == 1:
            breast_cancer_diagnosis = "The Breast Cancer is Benign"
            st.success(breast_cancer_diagnosis, icon="✅")
            st.balloons()
        else:
            breast_cancer_diagnosis = "'The Breast cancer is Malignant'"
            st.error(breast_cancer_diagnosis, icon="🚨")

