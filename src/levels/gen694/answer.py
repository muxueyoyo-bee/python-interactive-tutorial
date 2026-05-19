try:
    result = int('not a number')
    except IndexError as e:
        print(f'Caught IndexError: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
    except OSError as e:
        print(f'Caught OSError: {e}')
finally:
    print('Cleanup complete')