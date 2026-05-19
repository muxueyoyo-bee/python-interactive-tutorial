try:
    result = int('not a number')
    except (InvalidWheelFilename, UnsupportedWheel) as e:
        print(f'Caught (InvalidWheelFilename, UnsupportedWheel): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except InvalidVersion as e:
        print(f'Caught InvalidVersion: {e}')
finally:
    print('Cleanup complete')