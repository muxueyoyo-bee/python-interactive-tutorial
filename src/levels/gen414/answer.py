try:
    result = int('not a number')
    except (IndexError, TypeError) as e:
        print(f'Caught (IndexError, TypeError): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
finally:
    print('Cleanup complete')