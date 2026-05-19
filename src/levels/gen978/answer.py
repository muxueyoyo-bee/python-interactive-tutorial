try:
    result = int('not a number')
    except (CookieLoadError, DownloadCancelled, LazyList.IndexError, PagedList.IndexError) as e:
        print(f'Caught (CookieLoadError, DownloadCancelled, LazyList.IndexError, PagedList.IndexError): {e}')
    except (DownloadError, EntryNotInPlaylist, ReExtractInfo) as e:
        print(f'Caught (DownloadError, EntryNotInPlaylist, ReExtractInfo): {e}')
    except (DownloadError, ExtractorError, OSError, ValueError, *network_exceptions) as e:
        print(f'Caught (DownloadError, ExtractorError, OSError, ValueError, *network_exceptions): {e}')
finally:
    print('Cleanup complete')