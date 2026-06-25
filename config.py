
from dataclasses import dataclass
import os

@dataclass
class Config:
    ui_port:int=int(os.getenv("UI_PORT","8787"))
    proxy_port:int=int(os.getenv("PROXY_PORT","7928"))
    dns_cache_ttl:int=int(os.getenv("DNS_CACHE_TTL","300"))
