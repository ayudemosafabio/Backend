from http import HTTPMethod
from nexilum import connect_to

@connect_to(
    base_url="API_BASE",
    headers={
        "Authorization": f"Bearer {"API_TOKEN"}",
        "Content-Type": "application/json"
    },
    timeout=30,
    verify_ssl=True
)
class AIWorkspaceIntegration:

    def list_files(self, method=HTTPMethod.GET, endpoint="api/v1/files/"): ...
    """List all files from knowledge
    
    """

    def upload_file(self, value: str, method=HTTPMethod.POST, endpoint="api/v1/files/", **data): ...
    """Upload a file 
    
    """

    def delete_file(self, value: str, method=HTTPMethod.DELETE, endpoint="api/v1/files/"): ...
    """Delete a file from knowledge
       Args: 
            value (str): Value is file id value
    """

    def list_knowledge(self, method=HTTPMethod.GET, endpoint="api/v1/knowledge/"): ...
    """Delete a file from knowledge
       Args: 
            value (str): Value is file id value
    """
    
    def create_knowledge(self, method=HTTPMethod.POST, endpoint="api/v1/knowledge/", **data): ...
    """Delete a file from knowledge
       Args: 
            value (str): Value is file id value
    """
    
    def add_file_to_knowledge(self, endpoint: str, method=HTTPMethod.POST, **data): ...
    """Delete a file from knowledge
       Args: 
            value (str): Value is file id value
    """
    
    def add_file_to_knowledge_endpoint(self, knowledge_id: str):
        """Delete a file from knowledge
        Args: 
                value (str): Value is file id value
        """
        return f"api/v1/knowledge/{knowledge_id}/file/add"
    
