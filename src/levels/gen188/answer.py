try:
    result = int('not a number')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
    except IndexError as e:
        print(f'Caught IndexError: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
finally:
    print('Cleanup complete')