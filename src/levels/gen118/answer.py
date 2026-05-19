try:
    result = int('not a number')
    except BaseException as e:
        print(f'Caught BaseException: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except HttpProcessingError as e:
        print(f'Caught HttpProcessingError: {e}')
finally:
    print('Cleanup complete')