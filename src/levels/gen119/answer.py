try:
    result = int('not a number')
    except (asyncio.CancelledError, asyncio.TimeoutError) as e:
        print(f'Caught (asyncio.CancelledError, asyncio.TimeoutError): {e}')
    except ClientError as e:
        print(f'Caught ClientError: {e}')
    except EofStream as e:
        print(f'Caught EofStream: {e}')
finally:
    print('Cleanup complete')