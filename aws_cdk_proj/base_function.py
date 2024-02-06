from aws_cdk.aws_lambda import Function, Code, Runtime, CfnPermission
from aws_cdk import Stack



class BaseFunction(Function):
    def __init__(
            self,
            scope: Stack,
            id: str,
            function_name: str,
            code: Code,
            *args,
            **kwargs
    ) -> None:
        super().__init__(
            scope=scope,
            id=id,
            code=code,
            handler='index.handler',
            runtime=Runtime.PYTHON_3_9,
            function_name=function_name,
            *args,
            **kwargs
        )

        
        CfnPermission(
            scope=scope,
            id=f'{function_name}InvokePermission',
            action='lambda:InvokeFunction',
            function_name=self.function_name,
            principal='apigateway.amazonaws.com',
        )
