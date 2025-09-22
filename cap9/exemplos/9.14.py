from zoneinfo import ZoneInfo
from datetime import datetime


bruxelas = ZoneInfo('Europe/Brussels')
novaIorque = ZoneInfo('America/New-York')
tokio = ZoneInfo('Japan')
manaus = ZoneInfo('America/Manaus')
brasilia = ZoneInfo('Brazil/East')
rioBranco = ZoneInfo('America/Rio_Branco')
agora = datetime.now()
print('Agora em:')
print('Bruxelas ', agora.astimezone(bruxelas))
print('Nova Iorque ', agora.astimezone(novaIorque))
print('Tokio ', agora.astimezone(tokio))