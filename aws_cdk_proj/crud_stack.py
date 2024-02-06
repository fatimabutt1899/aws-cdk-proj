from aws_cdk import Stack
from aws_cdk.aws_lambda import Function, Code, Runtime, CfnPermission
from constructs import Construct
from aws_cdk_proj.crud import crud_root
from aws_cdk_proj.base_function import BaseFunction


class CrudStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

      
        # create
        self.create = BaseFunction(
            scope=self,
            id='CreateFunction',
            function_name='CreateFunction',
            code=Code.from_asset(f'{crud_root}/create'),
        )
        
        # delete
        self.delete = BaseFunction(
            scope=self,
            id='DeleteFunction',
            function_name='DeleteFunction',
            code=Code.from_asset(f'{crud_root}/delete'),
        )


        # read
        self.read = BaseFunction(
            scope=self,
            id='ReadFunction',
            function_name='ReadFunction',
            code=Code.from_asset(f'{crud_root}/read'),
        )

        # update
        self.update = BaseFunction(
            scope=self,
            id='UpdateFunction',
            function_name='UpdateFunction',
            code=Code.from_asset(f'{crud_root}/update'),
        )

