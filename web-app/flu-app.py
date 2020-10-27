import flask
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import random
import pickle
import copy

"""
run from flu-shot-analysis folder
git subtree push --prefix web-app heroku master
"""

app = flask.Flask(__name__)  # create instance of Flask class

model_filename = "combined_model.pkl"
combined_model = pickle.load(open(model_filename, 'rb'))

scale_data_1_5 = [('h1n1_concern', "H1N1 Concern", "3"), ('h1n1_knowledge', "H1N1 Knowledge", "2"), ('opinion_h1n1_vacc_effective', "Opinion H1N1 Effectivity", "5"),
 ('opinion_h1n1_risk', "Opinion H1N1 Risk", "5"), ('opinion_h1n1_sick_from_vacc', "Opinion H1N1 Sick From Vaccince", "5"),
 ('opinion_seas_vacc_effective', "Opinion Seasonal Vaccince Effectivity", "5"),('opinion_seas_risk', 'Opinion Seasonal Risk', "5"),
 ('opinion_seas_sick_from_vacc', 'Opinion Seasonal Sick From Vaccine', "5")]

drop_down_data = [
                {'cat_id': 'age_group', 'label':'Age Group', 'values': [("18-34 Years", "18"), ("35-44 Years", "35"), ("45-54 Years", "45"), ("55-64 Years", "55"), ("65+ Years", "65")]},
                {'cat_id': 'education', 'label': 'Education', 'values': [("< 12 Years", "10"), ("12 Years", "12"), ("Some College", "14"), ("College Graduate", "16")]},
                {'cat_id': 'household_adults', 'label': "Household Adults", 'values': [("0", "0"), ("1", "1"), ("2","2"), ("3","3")]},
                {'cat_id': 'household_children', 'label': "Household Children", 'values': [("0", "0"), ("1", "1"), ("2","2"), ("3","3"), ("4", "4"), ("5", "5"), ("6","6"), ("7","7")]},
                ]

binary_data = [('behavioral_antiviral_meds',"Takes Antiviral Meds" ), ('behavioral_avoidance', 'Behavioral Avoidance'), ('behavioral_face_mask', 'Wears Face Mask'),
('behavioral_wash_hands', 'Regularly Washes Hands'), ('behavioral_large_gatherings', 'behavioral_large_gatherings'), ('behavioral_outside_home', 'behavioral_outside_home'),
('behavioral_touch_face', 'behavioral_touch_face'), ('chronic_med_condition', 'Has Chronic Medical Conditions'), ('child_under_6_months', 'Has Child under 6 months'),
('health_worker', 'Is Health Worker'), ("sex_Male", 'Is a Male'), ("marital_status_Not_Married", "Not Married"), ("Rents Home (Does not own)" , "rent_or_own_Rent")]

dummy_binary_data = [
('health_insurance', 'Has Health Insurance' ),
('doctor_recc_h1n1', 'Had Doctor Reccomendation for H1N1' ),
('doctor_recc_seasonal', 'Had Doctor Reccomendation for Seasonal' ),
]

dummy_dropdown_data = [
{'cat_id': 'income_poverty_',  'label': 'Income Level', "values": [("Below Poverty", "Below_Poverty"), ("<$75,000, Above Poverty", "<=_$75,000,_Above_Poverty"), (">$75,000", ">_$75,000")]},
{'cat_id': "race_", 'label': 'Race', "values" : [("White", "White"), ("Hispanic", "Hispanic"), ("Other or Multiple", "Other_or_Multiple")]},
{'cat_id': "employment_status_", 'label': 'Employment Status', "values": [("Employed", "None"), ("Unemployed", "Unemployed"), ("Not in Labor Force", "Not_in_Labor_Force")]},
# "hhs_geo_region": ["bhuqouqj", "dqpwygqj", "fpwskwrf", "kbazzjca", "lrircsnp", "lzgpxyit", "mlyzmhmf", "oxchjgsf", "qufhixun"],
# "census_msa": ["MSA, Non Principle City", "MSA, Principle City", "Non MSA"]
                        ]

starting_data = {
    'h1n1_concern': 2,
    'h1n1_knowledge': 2,
    'behavioral_antiviral_meds': 0,
    'behavioral_avoidance':0,
    'behavioral_face_mask': 0,
    'behavioral_wash_hands': 0,
    'behavioral_large_gatherings': 0,
    'behavioral_outside_home': 0,
    'behavioral_touch_face': 0,
    'chronic_med_condition': 0,
    'child_under_6_months': 0,
    'health_worker': 0,
    'opinion_h1n1_vacc_effective': 2,
    'opinion_h1n1_risk': 2,
    'opinion_h1n1_sick_from_vacc': 2,
    'opinion_seas_vacc_effective': 2,
    'opinion_seas_risk': 2,
    'opinion_seas_sick_from_vacc': 2,
    'age_group': 18,
    'education': 10,
    'household_adults': 0,
    'household_children': 0,
    'health_insurance_0.0': 1,
    'health_insurance_1.0': 0,
    'health_insurance_nan': 0,
    'doctor_recc_h1n1_0.0': 1,
    'doctor_recc_h1n1_1.0': 0,
    'doctor_recc_h1n1_nan': 0,
    'doctor_recc_seasonal_0.0': 1,
    'doctor_recc_seasonal_1.0': 0,
    'doctor_recc_seasonal_nan': 0,
    'income_poverty_<=_$75,000,_Above_Poverty': 0,
    'income_poverty_>_$75,000': 0,
    'income_poverty_Below_Poverty': 1,
    'income_poverty_nan': 0,
    'race_Hispanic': 0,
    'race_Other_or_Multiple': 0,
    'race_White': 1,
    'sex_Male': 0,
    'marital_status_Not_Married': 0,
    'rent_or_own_Rent': 0,
    'employment_status_Not_in_Labor_Force': 0,
    'employment_status_Unemployed': 1,
    'hhs_geo_region_bhuqouqj': 0,
    'hhs_geo_region_dqpwygqj': 0,
    'hhs_geo_region_fpwskwrf': 0,
    'hhs_geo_region_kbazzjca': 0,
    'hhs_geo_region_lrircsnp': 0,
    'hhs_geo_region_lzgpxyit': 0,
    'hhs_geo_region_mlyzmhmf': 0,
    'hhs_geo_region_oxchjgsf': 0,
    'hhs_geo_region_qufhixun': 0,
    'census_msa_MSA, Principle City': 1,
    'census_msa_Non-MSA': 0
}


prediction_data = {}


@app.route('/')  # the site to route to, index/main in this case
def viz_page():
    """
    Homepage: serve our visualization page, awesome.html
    """
    global prediction_data
    prediction_data = copy.deepcopy(starting_data)
    print(starting_data.values())
    user_info = prediction_data.values()
    preds = combined_model.predict_proba([list(user_info)])

    initial_data = {
        "#Seasonal_No": preds[0][0][0] * 100,
        "#Seasonal_Yes": preds[0][0][1] * 100,
        "#H1N1_No": preds[1][0][0] * 100,
        "#H1N1_Yes": preds[1][0][1] * 100,
    }

    return flask.render_template('main.html', scale_questions=scale_data_1_5, dropdown_questions=drop_down_data,
                                 binary_data=binary_data, dummy_binary_data=dummy_binary_data,
                                 dummy_dropdown_data=dummy_dropdown_data, initial_data=initial_data)

@app.route('/api/estimate', methods=["POST"])
def estimate():

    data = flask.request.json
    prediction_data[data["value_id"]] = int(data["value"])
    user_info = prediction_data.values()
    preds = combined_model.predict_proba([list(user_info)])

    return_data = {
        "#Seasonal_No": preds[0][0][0] * 100,
        "#Seasonal_Yes": preds[0][0][1] * 100,
        "#H1N1_No": preds[1][0][0] * 100,
        "#H1N1_Yes": preds[1][0][1] * 100,
    }

    return( return_data )


if __name__ == '__main__':
    app.run(debug=True)
