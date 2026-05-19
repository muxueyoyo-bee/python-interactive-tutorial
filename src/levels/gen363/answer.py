try:
    result = int('not a number')
    except BaseException as e:
        print(f'Caught BaseException: {e}')
    except ClientDisconnected as e:
        print(f'Caught ClientDisconnected: {e}')
    except ConnectionClosed as e:
        print(f'Caught ConnectionClosed: {e}')
finally:
    print('Cleanup complete')