# CASE 1: Absolute import (WORKS)

from impyrial.length.api import convert_unit

result = convert_unit(10, "ft", "in")
print("Absolute import result:", result)

# Expected output:
# 120

# CASE 2: Relative import (ERROR when run directly)

# from .length.api import convert_unit

# This import causes an error when running the file directly:
# ImportError: attempted relative import with no known parent package

# Reason:
# When the file is executed as a standalone script,
# Python does not treat it as part of a package,
# so relative imports (using .) cannot be resolved.


# CORRECT WAY TO RUN

# To make relative imports work, run the script as a module:
# python -m impyrial.example_script