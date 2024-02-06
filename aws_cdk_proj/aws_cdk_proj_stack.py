from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    
)
from aws_cdk.aws_lambda import Function, Code, Runtime
from constructs import Construct

from aws_cdk_proj.crud_stack import CrudStack 

# from aws_cdk.aws_apigatewayv2 import * as API




class AwsCdkProjStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #means that it belongs to AwsCdkProjStack parent stack
        CrudStack( 
            scope=self, 
            # id='CrudStack',
            construct_id='CrudStack',
            stack_name='CrudStack',
            
        )

