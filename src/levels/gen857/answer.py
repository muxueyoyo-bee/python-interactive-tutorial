try:
    result = int('not a number')
    except (Exception, KeyboardInterrupt) as e:
        print(f'Caught (Exception, KeyboardInterrupt): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
finally:
    print('Cleanup complete')