from sims4communitylib.mod_support.common_mod_info import CommonModInfo


class ModInfo(CommonModInfo):
    """Mod info for the 1st World Problems Mod."""

    # To create a Mod Identity for this mod, simply do ModInfo.get_identity(). Please refrain from using the ModInfo of The Sims 4 Community Library in your own mod and instead use yours!
    _FILE_PATH: str = str(__file__)

    @property
    def _name(self) -> str:
        # This is the name that'll be used whenever a Messages.txt or Exceptions.txt file is created <_name>_Messages.txt and <_name>_Exceptions.txt.
        return "1stWorldProblems"

    @property
    def _author(self) -> str:
        # This is your name.
        return "Auxon"

    @property
    def _base_namespace(self) -> str:
        # This is the name of the root package
        return "1stWorldProblems"

    @property
    def _file_path(self) -> str:
        # This is simply a file path that you do not need to change.
        return ModInfo._FILE_PATH
