try:
    result = int('not a number')
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        print(f'Caught (FileNotFoundError, subprocess.TimeoutExpired): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')