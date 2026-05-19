try:
    result = int('not a number')
    except (EOFError, KeyboardInterrupt) as e:
        print(f'Caught (EOFError, KeyboardInterrupt): {e}')
    except Abort as e:
        print(f'Caught Abort: {e}')
    except BadParameter as e:
        print(f'Caught BadParameter: {e}')
finally:
    print('Cleanup complete')