try:
    result = int('not a number')
    except subprocess.CalledProcessError as e:
        print(f'Caught subprocess.CalledProcessError: {e}')
finally:
    print('Cleanup complete')