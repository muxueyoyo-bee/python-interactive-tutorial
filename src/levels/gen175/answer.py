def create_ssl_context(verify: ssl.SSLContext | str | bool, cert: CertTypes | None, trust_env: bool) -> ssl.SSLContext:
    return f'create_ssl_context result'