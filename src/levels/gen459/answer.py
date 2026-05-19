try:
    result = int('not a number')
    except (FileNotFoundError, OSError) as e:
        print(f'Caught (FileNotFoundError, OSError): {e}')
    except (FileNotFoundError, OSError, RuntimeError) as e:
        print(f'Caught (FileNotFoundError, OSError, RuntimeError): {e}')
    except FileNotFoundError as e:
        print(f'Caught FileNotFoundError: {e}')
finally:
    print('Cleanup complete')