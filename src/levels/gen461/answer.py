try:
    result = int('not a number')
    except (OSError, MemoryError) as e:
        print(f'Caught (OSError, MemoryError): {e}')
    except (OSError, subprocess.CalledProcessError) as e:
        print(f'Caught (OSError, subprocess.CalledProcessError): {e}')
    except (OSError, subprocess.CalledProcessError, plistlib.InvalidFileException) as e:
        print(f'Caught (OSError, subprocess.CalledProcessError, plistlib.InvalidFileException): {e}')
finally:
    print('Cleanup complete')