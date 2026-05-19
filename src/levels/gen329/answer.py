try:
    result = int('not a number')
    except BaseException as e:
        print(f'Caught BaseException: {e}')
    except NoMatchFound as e:
        print(f'Caught NoMatchFound: {e}')
finally:
    print('Cleanup complete')