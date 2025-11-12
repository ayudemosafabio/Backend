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
class Check_user_integration:

    def check_user(self, value: str, method: HTTPMethod = HTTPMethod.GET, endpoint: str = ""):...

