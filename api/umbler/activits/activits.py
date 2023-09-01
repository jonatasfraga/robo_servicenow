from api.umbler.constantes import ORGANIZATION_ID
from api.umbler.utils import get

ACTIVITES = f'/v1/activity-logs?organizationId={ORGANIZATION_ID}'

r = get(ACTIVITES)
resposta = r.json()

print(r.json())
