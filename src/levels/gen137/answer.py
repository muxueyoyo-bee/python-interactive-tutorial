try:
    result = int('not a number')
    except ExceptionGroup as e:
        print(f'Caught ExceptionGroup: {e}')
finally:
    print('Cleanup complete')