from importlib.metadata import version, PackageNotFoundError

class VersionUtil:
    @staticmethod
    def get_version():
        """ Returns the current version of the library. """
        try:
            return version('lib-version')
        except PackageNotFoundError:
            return "unknown"

    @staticmethod
    def print_version():
        """ Prints the current library version. """
        version = VersionUtil.get_version()
        print(f"Current library version: {version}")

# Example usage:
if __name__ == "__main__":
    VersionUtil.print_version()