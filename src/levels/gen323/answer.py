try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except subprocess.CalledProcessError as e:
        print(f'Caught subprocess.CalledProcessError: {e}')
finally:
    print('Cleanup complete')