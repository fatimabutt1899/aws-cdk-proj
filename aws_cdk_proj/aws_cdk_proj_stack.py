from aws_cdk import Stack
from constructs import Construct
from aws_cdk_proj.crud_stack import CrudStack 
from aws_cdk_proj.api_stack import APIStack



class AwsCdkProjStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #means that it belongs to AwsCdkProjStack parent stack
        crud_stack = CrudStack( 
            scope=self, 
            construct_id='CrudStack',
            stack_name='CrudStack',
        )
        
        

        APIStack(
            scope=self,
            construct_id="ApiStack",

            create_backend=crud_stack.create,
            read_backend=crud_stack.read,
            delete_backend=crud_stack.delete,
            update_backend=crud_stack.update,
        )

    


