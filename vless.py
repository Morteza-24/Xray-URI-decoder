import utils
import definitions
from config import Config
from v2ray_config import V2rayConfig
from urllib.parse import urlparse, parse_qs, unquote


def vless_parse(uri):
    config = Config(definitions.PROTOCOL_SCHEMES["VLESS"])
    uri = urlparse(uri.replace(" ", "%20").replace("|", "%7C"))
    query_params = parse_qs(uri.query)
    for param in query_params:
        query_params[param] = unquote(query_params[param])

    config.remarks = unquote(uri.fragment)
    config.server = uri.hostname
    # TODO: check server validity
    # if not (utils.is_ip_address(config.server) or utils.is_valid_url(config.server)):
    #     return None
    config.server_port = uri.port
    config.password = uri.username
    config.method = query_params.get("encryption")
    utils.get_item_form_query(config, query_params)

    return config


def vless_outbound(config):
    outbound = V2rayConfig.gen_outbound("vless")
    outbound["settings"]["vnext"][0]["address"] = str(config.server)
    outbound["settings"]["vnext"][0]["port"] = int(config.server_port) if config.server_port else 443
    outbound["settings"]["vnext"][0]["users"].append({
        "id": str(config.password),
        "encryption": config.method,
        "flow": config.flow,
        "level": 8
    })
    # TODO: finish vless outbound
