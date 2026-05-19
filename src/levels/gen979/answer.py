try:
    result = int('not a number')
    except (CookieLoadError, DownloadError) as e:
        print(f'Caught (CookieLoadError, DownloadError): {e}')
    except (TypeError, ValueError) as e:
        print(f'Caught (TypeError, ValueError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
finally:
    print('Cleanup complete')