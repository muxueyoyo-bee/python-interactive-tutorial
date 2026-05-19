try:
    result = int('not a number')
    except OSError as e:
        print(f'Caught OSError: {e}')
    except asyncio.TimeoutError as e:
        print(f'Caught asyncio.TimeoutError: {e}')
finally:
    print('Cleanup complete')