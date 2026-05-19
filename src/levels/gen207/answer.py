try:
    result = int('not a number')
    except CodeNotFound as e:
        print(f'Caught CodeNotFound: {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
finally:
    print('Cleanup complete')