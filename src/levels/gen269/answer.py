try:
    result = int('not a number')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
    except ValidationError as e:
        print(f'Caught ValidationError: {e}')
finally:
    print('Cleanup complete')