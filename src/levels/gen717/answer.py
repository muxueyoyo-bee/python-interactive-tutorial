try:
    result = int('not a number')
    except CertificateError as e:
        print(f'Caught CertificateError: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
finally:
    print('Cleanup complete')