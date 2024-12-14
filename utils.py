import definitions


def get_item_form_query(config, query_params):
        config.network = query_params.get("type") if query_params.get("type") else definitions.NETWORK_TYPE["TCP"]
        config.header_type = query_params.get("headerType")
        config.host = query_params.get("host")
        config.path = query_params.get("path")

        config.seed = query_params.get("seed")
        config.quic_security = query_params.get("quicSecurity")
        config.quic_key = query_params.get("key")
        config.mode = query_params.get("mode")
        config.service_name = query_params.get("serviceName")
        config.authority = query_params.get("authority")
        config.xhttp_mode = query_params.get("mode")
        config.xhttp_extra = query_params.get("extra")

        config.security = query_params.get("security") if query_params.get("security") in ["tls", "reality"] else None

        if query_params.get("allowInsecure") is not None:
            config.insecure = query_params.get("allowInsecure") == "1"
        else:
            config.insecure = False

        config.sni = query_params.get("sni")
        config.finger_print = query_params.get("fp")
        config.alpn = query_params.get("alpn")
        config.public_key = query_params.get("pbk")
        config.short_id = query_params.get("sid")
        config.spiderX = query_params.get("spx")
        config.flow = query_params.get("flow")
