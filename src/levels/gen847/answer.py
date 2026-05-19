try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except IndexError as e:
        print(f'Caught IndexError: {e}')
finally:
    print('Cleanup complete')