try:
    result = int('not a number')
    except (OSError, subprocess.CalledProcessError) as e:
        print(f'Caught (OSError, subprocess.CalledProcessError): {e}')
    except FileNotFoundError as e:
        print(f'Caught FileNotFoundError: {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
finally:
    print('Cleanup complete')