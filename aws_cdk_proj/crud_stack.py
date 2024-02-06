from aws_cdk import (
    Duration,
    Stack,

    
)
from aws_cdk.aws_lambda import Function, Code, Runtime
from constructs import Construct
from aws_cdk_proj.crud import crud_root



class CrudStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

      
        # create
        Function(
            scope=self,
            id='CreateFunction',
            function_name='CreateFunction',
            code=Code.from_asset(f'{crud_root}/create'),
            runtime=Runtime.PYTHON_3_9,
            handler='index.handler'
        )
        
        # delete
        Function(
            scope=self,
            id='DeleteFunction',
            function_name='DeleteFunction',
            code=Code.from_asset(f'{crud_root}/delete'),
            runtime=Runtime.PYTHON_3_9,
            handler='index.handler'
        )

        # read
        Function(
            scope=self,
            id='ReadFunction',
            function_name='ReadFunction',
            code=Code.from_asset(f'{crud_root}/read'),
            runtime=Runtime.PYTHON_3_9,
            handler='index.handler'
        )

        # update
        Function(
            scope=self,
            id='UpdateFunction',
            function_name='UpdateFunction',
            code=Code.from_asset(f'{crud_root}/update'),
            runtime=Runtime.PYTHON_3_9,
            handler='index.handler'
        )

