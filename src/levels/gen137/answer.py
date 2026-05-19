try:
    result = int('not a number')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
    except aiodns.error.DNSError as e:
        print(f'Caught aiodns.error.DNSError: {e}')
finally:
    print('Cleanup complete')