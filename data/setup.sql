CREATE DATABASE fluvaccines;

\connect fluvaccines;

CREATE TABLE features(
  respondent_id   INT,
  h1n1_concern    INT,
  h1n1_knowledge  INT,
  behavioral_antiviral_meds   INT,
  behavioral_avoidance    INT,
  behavioral_face_mask    INT,
  behavioral_wash_hands   INT,
  behavioral_large_gatherings INT,
  behavioral_outside_home INT,
  behavioral_touch_face   INT,
  doctor_recc_h1n1    INT,
  doctor_recc_seasonal    INT,
  chronic_med_condition   INT,
  child_under_6_months    INT,
  health_worker   INT,
  health_insurance    INT,
  opinion_h1n1_vacc_effective INT,
  opinion_h1n1_risk   INT,
  opinion_h1n1_sick_from_vacc INT,
  opinion_seas_vacc_effective INT,
  opinion_seas_risk   INT,
  opinion_seas_sick_from_vacc INT,
  age_group   TEXT,
  education   TEXT,
  ace    TEXT,
  sex TEXT,
  income_poverty  TEXT,
  marital_status  TEXT,
  rent_or_own TEXT,
  employment_status   TEXT,
  hhs_geo_region  TEXT,
  census_msa  TEXT,
  household_adults    INT,
  household_children  INT,
  employment_industry TEXT,
  employment_occupation TEXT
);

CREATE TABLE targets(
  respondent_id INT,
  h1n1_vaccine  INT,
  seasonal_vaccine INT
);

\copy features FROM 'training_set_features.csv' DELIMITER ',' CSV HEADER;
\copy targets FROM 'training_set_labels.csv' DELIMITER ',' CSV HEADER;
