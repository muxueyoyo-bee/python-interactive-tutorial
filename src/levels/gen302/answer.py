try:
    result = int('not a number')
    except (ProtocolError, OSError) as e:
        print(f'Caught (ProtocolError, OSError): {e}')
    except (_SSLError, _HTTPError) as e:
        print(f'Caught (_SSLError, _HTTPError): {e}')
    except ClosedPoolError as e:
        print(f'Caught ClosedPoolError: {e}')
finally:
    print('Cleanup complete')