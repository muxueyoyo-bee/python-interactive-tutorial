try:
    result = int('not a number')
    except (asyncio.CancelledError, asyncio.TimeoutError) as e:
        print(f'Caught (asyncio.CancelledError, asyncio.TimeoutError): {e}')
    except EofStream as e:
        print(f'Caught EofStream: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')