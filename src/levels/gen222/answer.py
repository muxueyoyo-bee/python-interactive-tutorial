try:
    result = int('not a number')
    except EnvironmentError as e:
        print(f'Caught EnvironmentError: {e}')
    except RpcGenError as e:
        print(f'Caught RpcGenError: {e}')
finally:
    print('Cleanup complete')