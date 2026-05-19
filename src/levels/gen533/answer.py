try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except InvalidWheelFilename as e:
        print(f'Caught InvalidWheelFilename: {e}')
finally:
    print('Cleanup complete')