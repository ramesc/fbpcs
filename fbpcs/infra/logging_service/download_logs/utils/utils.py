# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

import io
import os
import shutil

from dataclasses import dataclass
from enum import Enum
from typing import List


class Utils:
    def create_file(self, file_location: str, content: List[str]) -> None:
        """
        Create file in the file location with content.
        Args:
            file_location (str): Full path of the file location Eg: /tmp/xyz.txt
            content (list): Content to be written in file
        Returns:
            None
        """
        content = content or []

        try:
            # write to a file, if it already exists
            with open(file_location, "w") as file_object:
                self.write_to_file(file_object, content)
        except IOError as error:
            # T122918736 - for better execption messages
            raise Exception(f"Failed to create file {file_location}") from error

    @classmethod
    def write_to_file(
        cls,
        file_object: io.TextIOWrapper,
        contents: List[str],
        append_newline: bool = True,
    ) -> None:
        """
        Write content to the file.
        Args:
            file_object (IO): Object of file to read/write
            contents (list): Content to be written in file
        Returns:
            None
        """
        for content in contents:
            if append_newline:
                content = content + "\n"
            file_object.write(content)

    @staticmethod
    def create_folder(folder_location: str) -> None:
        """
        Creates folder in the given path
        Args:
            folder_location (str): Path were folder will be created. Path includes new folder name.
                                   Eg: If creating folder `test` in location `/tmp`, folder_location should be `/tmp/test`
        Returns:
            None
        """

        if not os.path.exists(folder_location):
            os.makedirs(folder_location)

    @staticmethod
    def compress_downloaded_logs(folder_location: str) -> None:
        """
        Compresses folder passed to the function in arguments
        Args:
            folder_location (str): Complete folder path Eg /tmp/folder1
        """
        if os.path.isdir(folder_location):
            shutil.make_archive(folder_location, "zip", folder_location)
        else:
            # T122918736 - for better exception messages
            raise Exception(
                f"Couldn't find folder {folder_location}."
                f"Please check if folder exists.\nAborting folder compression."
            )

    @staticmethod
    def copy_file(source: str, destination: str) -> None:
        """
        Copys folder from source to destination path
        """
        try:
            shutil.copy2(source, destination)
        except shutil.SameFileError as err:
            raise shutil.SameFileError(
                f"{source} and {destination} represents same file)"
            ) from err
        except PermissionError as err:
            raise PermissionError("Permission denied") from err

    @staticmethod
    def string_formatter(preset_string: str, *args: str) -> str:
        return preset_string.format(*args)


class StringFormatter(str, Enum):
    LOG_GROUP = "/{}/{}"
    LOG_STREAM = "{}/{}/{}"
    LOCAL_FOLDER_LOCATION = "/tmp/{}"
    LOCAL_ZIP_FOLDER_LOCATION = "{}.zip"
    FILE_LOCATION = "{}/{}"
    ZIPPED_FOLDER_NAME = "{}.zip"


@dataclass
class ContainerDetails:
    service_name: str
    container_name: str
    container_id: str
