from dotenv import load_dotenv
load_dotenv()

import boto3
import time
import sys
import os

DB_IDENTIFIER = 'classicmodels-db'
AWS_REGION = 'us-east-1' 
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

def provision_rds():
    rds_client = boto3.client('rds', region_name=AWS_REGION)

    try:
        response = rds_client.create_db_instance(
            DBInstanceIdentifier=DB_IDENTIFIER,
            AllocatedStorage=20, # 20 GB é o mínimo para free-tier
            DBInstanceClass='db.t3.micro', # Instância elegível ao nível gratuito
            Engine='mysql',
            EngineVersion='8.0',
            MasterUsername=DB_USER,
            MasterUserPassword=DB_PASSWORD,
            PubliclyAccessible=True, # Necessário para acessar do computador local
            SkipFinalSnapshot=True
        )

        waiter = rds_client.get_waiter('db_instance_available')
        waiter.wait(DBInstanceIdentifier=DB_IDENTIFIER)

        instances = rds_client.describe_db_instances(DBInstanceIdentifier=DB_IDENTIFIER)
        endpoint = instances['DBInstances'][0]['Endpoint']['Address']
        
        print(f"Endpoint: {endpoint}")
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    provision_rds()