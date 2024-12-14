import definitions
import vless
import base64
import json


def xray_decoder(uri):
    decoded_uri = _try_base64_decode(uri)
    if not decoded_uri:
        decoded_uri = _try_base64_decode(uri.rstrip('='))
    uri = decoded_uri if decoded_uri else uri
    return _config_to_json(_parse_config(uri))


def _try_base64_decode(text):
    try:
        return base64.b64decode(text)
    except:
        return None


def _parse_config(uri):
    if uri.startswith(definitions.PROTOCOL_SCHEMES["VLESS"]):
        config = vless.parse(uri)
    # TODO: support more protocols
    # elif uri.startswith(definitions.PROTOCOL_SCHEMES["TROJAN"]):
    #     config = trojan_parse(uri)
    # elif uri.startswith(definitions.PROTOCOL_SCHEMES["VMESS"]):
    #     config = vmess_parse(uri)
    # elif uri.startswith(definitions.PROTOCOL_SCHEMES["SHADOWSOCKS"]):
    #     config = shadowsocks_parse(uri)
    # elif uri.startswith(definitions.PROTOCOL_SCHEMES["HYSTERIA2"]) or uri.startswith(definitions.PROTOCOL_SCHEMES["HY2"]):
    #     config = hysteria2_parse(uri)
    # elif uri.startswith(definitions.PROTOCOL_SCHEMES["WIREGUARD"]):
    #     config = wireguard_parse(uri)
    # elif uri.startswith(definitions.PROTOCOL_SCHEMES["SOCKS"]):
    #     config = socks_parse(uri)
    else:
        return None


def _config_to_json(config):
    with open("v2ray_config.json", "rt") as f:
        v2ray_config = json.load(f)
    v2ray_config["remarks"] = config.remarks
    if config["config_type"] == definitions.PROTOCOL_SCHEMES["HYSTERIA2"]:
        return None
    match config.config_type:
        case definitions.PROTOCOL_SCHEMES.get("VLESS"):
            outbound = vless.outbound(config)
        # TODO: support more protocols
        # case definitions.PROTOCOL_SCHEMES.get("TROJAN"):
        #     trojan_outbound(config)
        # case definitions.PROTOCOL_SCHEMES.get("VMESS"):
        #     vmess_outbound(config)
        # case definitions.PROTOCOL_SCHEMES.get("SHADOWSOCKS"):
        #     shadowsocks_outbound(config)
        # case definitions.PROTOCOL_SCHEMES.get("HYSTERIA2"):
        #     hysteria2_outbound(config)
        # case definitions.PROTOCOL_SCHEMES.get("WIREGUARD"):
        #     wireguard_outbound(config)
        # case definitions.PROTOCOL_SCHEMES.get("SOCKS"):
        #     socks_outbound(config)
    # TODO: finish json creation
