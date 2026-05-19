try:
    result = int('not a number')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except DatabaseError as e:
        print(f'Caught DatabaseError: {e}')
    except Error as e:
        print(f'Caught Error: {e}')
finally:
    print('Cleanup complete')