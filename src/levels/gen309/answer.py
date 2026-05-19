try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except message.DecodeError as e:
        print(f'Caught message.DecodeError: {e}')
finally:
    print('Cleanup complete')