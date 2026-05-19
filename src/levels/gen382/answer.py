try:
    result = int('not a number')
    except httpx.ConnectError as e:
        print(f'Caught httpx.ConnectError: {e}')
finally:
    print('Cleanup complete')