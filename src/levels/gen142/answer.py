try:
    result = int('not a number')
    except (Exception, asyncio.CancelledError) as e:
        print(f'Caught (Exception, asyncio.CancelledError): {e}')
finally:
    print('Cleanup complete')