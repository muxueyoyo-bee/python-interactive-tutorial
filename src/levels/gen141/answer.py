try:
    result = int('not a number')
    except (GracefulExit, KeyboardInterrupt) as e:
        print(f'Caught (GracefulExit, KeyboardInterrupt): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
finally:
    print('Cleanup complete')