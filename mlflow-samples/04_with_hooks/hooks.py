import boto3
import sagemaker
from sagemaker.session import Session


from sagemaker.feature_store.feature_group import FeatureGroup

boto_session = boto3.Session(region_name='ap-south-1')
sagemaker_session = sagemaker.Session()
default_bucket = sagemaker_session.default_bucket()
    
def get_fs_runtime():
    prefix = 'sagemaker-featurestore'
    sagemaker_client = boto_session.client(service_name='sagemaker', region_name='ap-south-1')
    featurestore_runtime = boto_session.client(service_name='sagemaker-featurestore-runtime', region_name='ap-south-1')
    return featurestore_runtime

def input_fn(X):
    featurestore_runtime = get_fs_runtime()
    data = featurestore_runtime.get_record(FeatureGroupName='<name>', RecordIdentifierValueAsString='<id>')
    ## do something with data ##
    return X
    

def output_fn(Y):
    return Y