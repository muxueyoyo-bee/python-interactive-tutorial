try:
    result = int('not a number')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
finally:
    print('Cleanup complete')