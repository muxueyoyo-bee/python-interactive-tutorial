try:
    result = int('not a number')
    except (ImportError, OSError) as e:
        print(f'Caught (ImportError, OSError): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except OSError as e:
        print(f'Caught OSError: {e}')
finally:
    print('Cleanup complete')