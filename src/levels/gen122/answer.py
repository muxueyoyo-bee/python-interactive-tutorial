try:
    result = int('not a number')
    except (ClientConnectorError, asyncio.TimeoutError) as e:
        print(f'Caught (ClientConnectorError, asyncio.TimeoutError): {e}')
    except BaseException as e:
        print(f'Caught BaseException: {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
finally:
    print('Cleanup complete')