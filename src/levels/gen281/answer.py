try:
    result = int('not a number')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except CycleError as e:
        print(f'Caught CycleError: {e}')
    except IndexError as e:
        print(f'Caught IndexError: {e}')
finally:
    print('Cleanup complete')