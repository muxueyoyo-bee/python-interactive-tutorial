try:
    result = int('not a number')
    except (IOError, ValueError) as e:
        print(f'Caught (IOError, ValueError): {e}')
    except IOError as e:
        print(f'Caught IOError: {e}')
    except OSError as e:
        print(f'Caught OSError: {e}')
finally:
    print('Cleanup complete')