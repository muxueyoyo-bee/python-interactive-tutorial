try:
    result = int('not a number')
    except (ClientOSError, ServerDisconnectedError) as e:
        print(f'Caught (ClientOSError, ServerDisconnectedError): {e}')
    except (ConnectionTimeoutError, ClientConnectorError, ClientConnectorCertificateError, ClientConnectorSSLError) as e:
        print(f'Caught (ConnectionTimeoutError, ClientConnectorError, ClientConnectorCertificateError, ClientConnectorSSLError): {e}')
    except BaseException as e:
        print(f'Caught BaseException: {e}')
finally:
    print('Cleanup complete')