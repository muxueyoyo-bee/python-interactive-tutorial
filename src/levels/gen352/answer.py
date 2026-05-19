try:
    result = int('not a number')
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f'Caught (subprocess.CalledProcessError, FileNotFoundError): {e}')
    except subprocess.CalledProcessError as e:
        print(f'Caught subprocess.CalledProcessError: {e}')
finally:
    print('Cleanup complete')