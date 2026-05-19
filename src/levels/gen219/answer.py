try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except getopt.GetoptError as e:
        print(f'Caught getopt.GetoptError: {e}')
finally:
    print('Cleanup complete')