try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except httpx.StreamConsumed as e:
        print(f'Caught httpx.StreamConsumed: {e}')
finally:
    print('Cleanup complete')