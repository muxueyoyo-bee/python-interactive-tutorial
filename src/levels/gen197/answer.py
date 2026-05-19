try:
    result = int('not a number')
    except (subprocess.CalledProcessError, FileNotFoundError, Exception) as e:
        print(f'Caught (subprocess.CalledProcessError, FileNotFoundError, Exception): {e}')
    except ET.ParseError as e:
        print(f'Caught ET.ParseError: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')