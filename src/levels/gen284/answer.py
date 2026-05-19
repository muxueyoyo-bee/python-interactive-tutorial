try:
    result = int('not a number')
    except (ValueError, TypeError) as e:
        print(f'Caught (ValueError, TypeError): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except TypeError as e:
        print(f'Caught TypeError: {e}')
finally:
    print('Cleanup complete')