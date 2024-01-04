from dotenv import load_dotenv

import os
from loguru import logger

from ec.llm.service.inference_service import InferenceService

# function = lambda x: x ** 2
#
# print(list(map(function, range(10))))

load_dotenv('./secrets/.env-dev')

print(os.getenv('OPENAI_API_KEY', 'kepler'))

service = InferenceService()
logger.info(service.invoke('2020'))
