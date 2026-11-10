from pathlib import Path


SOURCE_DIR = Path(__file__).parent / "sample_files"


def list_files(directory: Path) -> list[Path]:
    """Return regular files directly inside the given directory."""
    # TODO: Return the files in this directory without including subdirectories.
    return []


def group_files_by_extension(files: list[Path]) -> dict[str, list[Path]]:
    """Group files by lowercase extension, using 'sem-extensao' when needed."""
    # TODO: Build and return a dictionary of file groups.
    return {}


def organize_files(directory: Path) -> None:
    """Move each file into a subdirectory named after its extension."""
    # TODO: Create the destination directories and move each file into its group.
    pass


def main() -> None:
    SOURCE_DIR.mkdir(exist_ok=True)
    files = list_files(SOURCE_DIR)
    print(f"Arquivos encontrados: {len(files)}")

    groups = group_files_by_extension(files)
    for extension, grouped_files in groups.items():
        print(f"{extension}: {len(grouped_files)} arquivo(s)")

    organize_files(SOURCE_DIR)
    print("Organização concluída.")


if __name__ == "__main__":
    main()