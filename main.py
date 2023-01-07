
from fastapi import FastAPI
from pydantic import BaseModel

from app.model.model import model_predict


app = FastAPI()


class data_in(BaseModel):
    REGION_POPULATION_RELATIVE:                         float
    DAYS_EMPLOYED:                                      float
    DAYS_REGISTRATION:                                  float
    DAYS_ID_PUBLISH:                                    float
    REGION_RATING_CLIENT:                               float
    AGE:                                                float
    housing_1:                                          float
    housing_2:                                          float
    sc_1:                                               float
    c_1:                                                float
    avg_ext:                                            float
    credit_annuity_ratio:                               float
    repaid_score:                                       float
    CNT_PAYMENT:                                        float
    NFLAG_INSURED_ON_APPROVAL:                          float
    PA_RATE_DOWN_PAYMENTmax:                            float
    PA_DAYS_DECISIONmax:                                float
    PA_DAYS_FIRST_DRAWINGmax:                           float
    PA_DAYS_FIRST_DUEmax:                               float
    PA_DAYS_LAST_DUE_1ST_VERSIONmax:                    float
    PA_DAYS_LAST_DUEmax:                                float
    PA_NAME_CONTRACT_TYPE_Cashloansmean:                float
    PA_NAME_CONTRACT_TYPE_Revolvingloansmean:           float
    PA_NAME_CONTRACT_STATUS_Approvedmean:               float
    PA_NAME_CONTRACT_STATUS_Canceledmean:               float
    PA_NAME_CONTRACT_STATUS_Refusedmean:                float
    PA_CODE_REJECT_REASON_XAPmean:                      float
    PA_NAME_TYPE_SUITE_Unaccompaniedmean:               float
    PA_NAME_CLIENT_TYPE_Newmean:                        float
    PA_NAME_CLIENT_TYPE_Repeatermean:                   float
    PA_NAME_SELLER_INDUSTRY_Consumerelectronicsmean:    float
    PA_NAME_YIELD_GROUP_highmean:                       float
    BB_CREDIT_TYPE_Creditcardmean_x:                    float
    BB_STATUS_0mean_x:                                  float
    BB_STATUS_Cmean_x:                                  float
    BB_STATUS_Xmean_x:                                  float
    BB_DAYS_CREDITmax_x:                                float
    BB_DAYS_CREDITmean_x:                               float
    BB_DAYS_CREDIT_ENDDATEmax_x:                        float
    BB_DAYS_ENDDATE_FACTmax_x:                          float
    CC_MONTHS_BALANCEmax:                               float
    IP_PAST_DUEmean:                                    float
    CODE_GENDER_M:                                      float
    NAME_EDUCATION_TYPE_Secondarysecondaryspecial:      float
    NAME_CLIENT_TYPE_Repeater:                          float
    
    class Config:
        schema_extra = {
            "example": {'REGION_POPULATION_RELATIVE': {0: 0.276357489964082},
                        'DAYS_EMPLOYED': {0: 0.9011780470102172},
                        'DAYS_REGISTRATION': {0: 0.8919422827496758},
                        'DAYS_ID_PUBLISH': {0: 0.2866737902610288},
                        'REGION_RATING_CLIENT': {0: 1.0},
                        'AGE': {0: 0.35997745208568205},
                        'housing_1': {0: 0.0},
                        'housing_2': {0: 0.41031414278590767},
                        'sc_1': {0: 0.40214353394131286},
                        'c_1': {0: 0.0},
                        'avg_ext': {0: 0.6990922906735763},
                        'credit_annuity_ratio': {0: 0.4588012163562275},
                        'repaid_score': {0: 0.075},
                        'CNT_PAYMENT': {0: 0.21428571428571427},
                        'NFLAG_INSURED_ON_APPROVAL': {0: 0.0},
                        'PA_RATE_DOWN_PAYMENTmax': {0: 0.0},
                        'PA_DAYS_DECISIONmax': {0: 0.6651831564532693},
                        'PA_DAYS_FIRST_DRAWINGmax': {0: 0.6540462216080447},
                        'PA_DAYS_FIRST_DUEmax': {0: 0.6724376731301939},
                        'PA_DAYS_LAST_DUE_1ST_VERSIONmax': {0: 0.45519367893621115},
                        'PA_DAYS_LAST_DUEmax': {0: 0.7866297194319363},
                        'PA_NAME_CONTRACT_TYPE_Cashloansmean': {0: 0.0},
                        'PA_NAME_CONTRACT_TYPE_Revolvingloansmean': {0: 0.0},
                        'PA_NAME_CONTRACT_STATUS_Approvedmean': {0: 1.0},
                        'PA_NAME_CONTRACT_STATUS_Canceledmean': {0: 0.0},
                        'PA_NAME_CONTRACT_STATUS_Refusedmean': {0: 0.0},
                        'PA_CODE_REJECT_REASON_XAPmean': {0: 1.0},
                        'PA_NAME_TYPE_SUITE_Unaccompaniedmean': {0: 0.0},
                        'PA_NAME_CLIENT_TYPE_Newmean': {0: 1.0},
                        'PA_NAME_CLIENT_TYPE_Repeatermean': {0: 0.0},
                        'PA_NAME_SELLER_INDUSTRY_Consumerelectronicsmean': {0: 1.0},
                        'PA_NAME_YIELD_GROUP_highmean': {0: 0.0},
                        'BB_CREDIT_TYPE_Creditcardmean_x': {0: 0.2},
                        'BB_STATUS_0mean_x': {0: 0.0},
                        'BB_STATUS_Cmean_x': {0: 0.0},
                        'BB_STATUS_Xmean_x': {0: 0.0},
                        'BB_DAYS_CREDITmax_x': {0: 0.8227241615331964},
                        'BB_DAYS_CREDITmean_x': {0: 0.6641683820010373},
                        'BB_DAYS_CREDIT_ENDDATEmax_x': {0: 0.9973718791064389},
                        'BB_DAYS_ENDDATE_FACTmax_x': {0: 0.9377186843946815},
                        'CC_MONTHS_BALANCEmax': {0: 0.882308173861809},
                        'IP_PAST_DUEmean': {0: 0.0},
                        'CODE_GENDER_M': {0: 1.0},
                        'NAME_EDUCATION_TYPE_Secondarysecondaryspecial': {0: 1.0},
                        'NAME_CLIENT_TYPE_Repeater': {0: 0.0}
            }
        }

class PredictionOut(BaseModel):
    outcome: str

@app.get("/")
def home():
    return {"health_check": "OK"}

@app.post('/predict')
def predict(data: data_in):
 outcome = model_predict(data.dict())

 return {"prediction": outcome}
