try:
    result = int('not a number')
    except InvalidInput as e:
        print(f'Caught InvalidInput: {e}')
    except NotImplementedError as e:
        print(f'Caught NotImplementedError: {e}')
    except subprocess.CalledProcessError as e:
        print(f'Caught subprocess.CalledProcessError: {e}')
finally:
    print('Cleanup complete')