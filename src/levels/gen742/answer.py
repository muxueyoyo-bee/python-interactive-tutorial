try:
    result = int('not a number')
    except (BadZipFile, UnsupportedWheelError) as e:
        print(f'Caught (BadZipFile, UnsupportedWheelError): {e}')
    except BaseException as e:
        print(f'Caught BaseException: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')