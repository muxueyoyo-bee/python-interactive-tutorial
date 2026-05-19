try:
    result = int('not a number')
    except (ValueError, AttributeError) as e:
        print(f'Caught (ValueError, AttributeError): {e}')
    except (subprocess.CalledProcessError, OSError) as e:
        print(f'Caught (subprocess.CalledProcessError, OSError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
finally:
    print('Cleanup complete')