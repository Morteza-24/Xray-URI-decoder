class V2rayConfig:
	def __init__(self, log, policy, inbounds, outbounds, dns, routing, remarks=None, stats=None, api=None, transport=None, reverse=None, fakedns=None, browserForwarder=None, observatory=None, burstObservatory=None):
		self.log = log
		# ...

	@classmethod
	def init_log(cls, access, error, log_level, dns_log=None):
		return {"access": access, "error": error, "loglevel": log_level, "dnsLog": dns_log}

	@classmethod
	def init_inbound(cls, tag, port, protocol, sniffing, listen=None, settings=None, streamSettings=None, allocate=None):
		return {"tag": tag, "port": port, "protocol": protocol, "sniffing": sniffing, "listen": listen, "settings": settings, "streamSettings": streamSettings, "allocate": allocate,
				"settings": {"auth": None, "udp": None, "userLevel": None, "address": None, "port": None, "network": None},
				"sniffing": {"enabled": None, "destOverride": [], "metadataOnly": None, "routeOnly": None}}

	@classmethod
	def init_outbound(cls, protocol, tag="proxy", mux=None, settings=None, streamSettings=None, proxySettings=None, sendThrough=None):
		if mux is None:
			mux = cls.get_mux(False)
		return {"protocol": protocol, "tag": tag, "mux": mux, "settings": settings, "streamSettings": streamSettings, "proxySettings": proxySettings, "sendThrough": sendThrough}

	@classmethod
	def gen_outbound(cls, config_type):
		match config_type:
			case "vless" | "vmess":
				return cls.init_outbound(protocol=config_type, settings=cls.init_out_settings(vnex=[cls.init_vnex(user=[cls.init_users()])]), streamSettings=cls.init_stream_settings())
			case "trojan" | "shadowsocks" | "hysteria2" | "socks":
				return cls.init_outbound(protocol=config_type, settings=cls.init_out_settings(servers=[cls.init_servers()]), streamSettings=cls.init_stream_settings())
			case "wireguard":
				return cls.init_outbound(protocol=config_type, settings=cls.init_settings(secret_key="", peers=[cls.init_wireguard()]))

	@classmethod
	def init_out_settings(cls, vnext=None, fragment=None, noises=None, servers=None, response=None, network=None, address=None, port=None, domain_strategy=None, redirect=None, user_level=None, inbound_tag=None, secret_key=None, peers=None, reserved=None, mtu=None, obfs_password=None):
		return {"vnext": vnext, "fragment": fragment, "noises": noises, "servers": servers, "response": response, "network": network, "address": address, "port": port, "domainStrategy": domain_strategy, "redirect": redirect, "userLevel": user_level, "inboundTag": inbound_tag, "secretKey": secret_key, "peers": peers, "reserved": reserved, "mtu": mtu, "obfsPassword": obfs_password}

	@classmethod
	def init_vnext(cls, address="", port=443, users=None):
		return {"address": address, "port": port, "users": users}

	@classmethod
	def init_users(cls, id="", level=8, alter_id=None, security=None, encryption=None, flow=None):
		return {"id": id, "level": level, "alterId": alter_id, "security": security, "encryption": encryption, "flow": flow}

	@classmethod
	def init_fragment(cls, packets=None, length=None, interval=None):
		return {"packets": packets, "length": length, "interval": interval}

	# TODO: finish V2rayConfig implementation
