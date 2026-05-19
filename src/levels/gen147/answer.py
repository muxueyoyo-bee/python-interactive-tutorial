try:
    result = int('not a number')
    except (TypeError, ValueError) as e:
        print(f'Caught (TypeError, ValueError): {e}')
    except (asyncio.CancelledError, asyncio.TimeoutError) as e:
        print(f'Caught (asyncio.CancelledError, asyncio.TimeoutError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
finally:
    print('Cleanup complete')