from typing import Any, Dict, Optional, Union, TYPE_CHECKING

from app.integration.shared.base_integration import BaseIntegration

if TYPE_CHECKING:
    from app.config.env_config import Development, Production

class PayUIntegration(BaseIntegration):

    def __init__(self, config: Union[Development, Production]) -> None:
        super().__init__(config.DONATIONS_URL)

    async def create_donation(self):...





