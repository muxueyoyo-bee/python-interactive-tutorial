try:
    result = int('not a number')
    except IndexError as e:
        print(f'Caught IndexError: {e}')
    except UnicodeDecodeError as e:
        print(f'Caught UnicodeDecodeError: {e}')
    except UnicodeEncodeError as e:
        print(f'Caught UnicodeEncodeError: {e}')
finally:
    print('Cleanup complete')