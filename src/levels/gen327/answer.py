try:
    result = int('not a number')
    except Error as e:
        print(f'Caught Error: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except FileNotFoundError as e:
        print(f'Caught FileNotFoundError: {e}')
finally:
    print('Cleanup complete')