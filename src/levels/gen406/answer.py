try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
    except ParseError as e:
        print(f'Caught ParseError: {e}')
finally:
    print('Cleanup complete')