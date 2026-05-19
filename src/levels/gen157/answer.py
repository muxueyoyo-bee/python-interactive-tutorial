try:
    result = int('not a number')
    except (ValueError, *CIRCULAR_SYMLINK_ERROR) as e:
        print(f'Caught (ValueError, *CIRCULAR_SYMLINK_ERROR): {e}')
    except (ValueError, FileNotFoundError) as e:
        print(f'Caught (ValueError, FileNotFoundError): {e}')
    except FileNotFoundError as e:
        print(f'Caught FileNotFoundError: {e}')
finally:
    print('Cleanup complete')