try:
    result = int('not a number')
    except ClientDisconnect as e:
        print(f'Caught ClientDisconnect: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except anyio.BrokenResourceError as e:
        print(f'Caught anyio.BrokenResourceError: {e}')
finally:
    print('Cleanup complete')