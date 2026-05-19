try:
    result = int('not a number')
    except Error as e:
        print(f'Caught Error: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
finally:
    print('Cleanup complete')