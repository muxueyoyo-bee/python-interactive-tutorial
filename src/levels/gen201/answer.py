try:
    result = int('not a number')
    except (ImportError, RuntimeError) as e:
        print(f'Caught (ImportError, RuntimeError): {e}')
    except GitError as e:
        print(f'Caught GitError: {e}')
    except GithubException as e:
        print(f'Caught GithubException: {e}')
finally:
    print('Cleanup complete')