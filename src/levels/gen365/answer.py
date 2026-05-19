try:
    result = int('not a number')
    except BaseException as e:
        print(f'Caught BaseException: {e}')
    except ClientDisconnected as e:
        print(f'Caught ClientDisconnected: {e}')
    except InvalidState as e:
        print(f'Caught InvalidState: {e}')
finally:
    print('Cleanup complete')