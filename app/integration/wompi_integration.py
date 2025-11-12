from typing import Any, Dict, Optional, Union, TYPE_CHECKING

from app.integration.shared.base_integration import BaseIntegration

if TYPE_CHECKING:
    from app.config.env_config import Development, Production

class WompiIntegration(BaseIntegration):

    def __init__(self, config: Union[Development, Production]) -> None:
        super().__init__(config.DONATIONS_URL)

    async def create_payment_link(
        self,
        identificador_enlace: str,
        monto: float,
        nombre_producto: str,
        url_redirect: Optional[str] = None
    ) -> Dict[str, Any]:

        url = f"{self._base_url}/EnlacePago"
        payload: Dict[str, Any] = {
            "identificadorEnlaceComercio": identificador_enlace,
            "monto": monto,
            "nombreProducto": nombre_producto
        }
        if url_redirect:
            payload["configuracion"] = {
                "urlRedirect": url_redirect
            }

        async with self._client as client:
            resp = await client.post(url, json=payload)
            resp.raise_for_status()
            body = resp.json()
            return body