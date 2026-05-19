try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except Finished as e:
        print(f'Caught Finished: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
finally:
    print('Cleanup complete')