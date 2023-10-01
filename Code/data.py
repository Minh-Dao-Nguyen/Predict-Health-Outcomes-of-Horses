#Import 
import pandas as pd
import numpy as np

#equation for cleaning
def yesNoEncoding(x):
    if x == 'yes':
        return 1.0
    else:
        return 0.0

def adultEncoding(x):
    if x == 'adult':
        return 1.0
    else:
        return 0.0 

def clean_data(df): 
    #Change age, adule = 1, young = 0
    df['age'] = df['age'].apply(adultEncoding)
    #print(df['age'].head())

    #Change yes, no data to binary
    df['surgery'] = df['surgery'].apply(yesNoEncoding)
    df['surgical_lesion'] = df['surgical_lesion'].apply(yesNoEncoding)
    df['cp_data'] = df['cp_data'].apply(yesNoEncoding)

    #drop hopspital number
    df = df.drop(['hospital_number'], axis=1)

    ##### ONE HOT ENCODING #####

    #temp_of_extremities
    df = pd.get_dummies(df, columns=['temp_of_extremities'], prefix=['temp_of_extremities'])
    df = pd.drop(['temp_of_extremities_cold'], axis=1)
    #peripheral_pulse
    df = pd.get_dummies(df, columns=['peripheral_pulse'], prefix=['peripheral_pulse'])
    df = pd.drop(['peripheral_pulse'], axis=1)
    #mucous_membrane
    df = pd.get_dummies(df, columns=['mucous_membrane'], prefix=['mucous_membrane'])
    df = pd.drop(['mucous_membrane'], axis=1)
    #capillary_refill_time
    df = pd.get_dummies(df, columns=['capillary_refill_time'], prefix=['capillary_refill_time'])
    df = pd.drop(['capillary_refill_time'], axis=1)
    #pain
    df = pd.get_dummies(df, columns=['pain'], prefix=['pain'])
    df = pd.drop(['pain'], axis=1)
    #peristalsis
    df = pd.get_dummies(df, columns=['peristalsis'], prefix=['peristalsis'])
    df = pd.drop(['peristalsis'], axis=1)
    #abdominal_distention
    df = pd.get_dummies(df, columns=['abdominal_distention'], prefix=['abdominal_distention'])
    df = pd.drop(['abdominal_distention'], axis=1)
    #nasogastric_tube
    df = pd.get_dummies(df, columns=['nasogastric_tube'], prefix=['nasogastric_tube'])
    df = pd.drop(['nasogastric_tube'], axis=1)
    #nasogastric_reflux
    df = pd.get_dummies(df, columns=['nasogastric_reflux'], prefix=['nasogastric_reflux'])
    df = pd.drop(['nasogastric_reflux'], axis=1)
    #rectal_exam_feces
    df = pd.get_dummies(df, columns=['rectal_exam_feces'], prefix=['rectal_exam_feces'])
    df = pd.drop(['rectal_exam_feces'], axis=1)
    #abdomen
    df = pd.get_dummies(df, columns=['abdomen'], prefix=['abdomen'])
    df = pd.drop(['abdomen'], axis=1)
    #abdomo_appearance
    df= pd.get_dummies(df, columns=['abdomo_appearance'], prefix=['abdomo_appearance'])
    df = pd.drop(['abdomo_appearance'], axis=1)
    
    
    #change all the columns to float 
    for cols in df.columns:
        if df[cols].dtype != 'float64':
            df[cols] = df[cols].astype('float64')
    

    return df