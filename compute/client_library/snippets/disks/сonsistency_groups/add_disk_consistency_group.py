#  Copyright 2024 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# flake8: noqa


# This file is automatically generated. Please do not modify it directly.
# Find the relevant recipe file in the samples/recipes or samples/ingredients
# directory and apply your changes there.


# [START compute_consistency_group_add_disk]
from google.cloud import compute_v1


def add_disk_consistency_group(
    project_id: str,
    disk_name: str,
    disk_location: str,
    consistency_group_name: str,
    consistency_group_region: str,
) -> None:
    """Adds a disk to a specified consistency group.
    Args:
        project_id (str): The ID of the Google Cloud project.
        disk_name (str): The name of the disk to be added.
        disk_location (str): The region or zone of the disk
        consistency_group_name (str): The name of the consistency group.
        consistency_group_region (str): The region of the consistency group.
    Returns:
        None
    """
    consistency_group_link = (
        f"regions/{consistency_group_region}/resourcePolicies/{consistency_group_name}"
    )

    # Checking if the disk is zonal or regional
    # If the final character of the disk_location is a digit, it is a regional disk
    if disk_location[-1].isdigit():
        policy = compute_v1.RegionDisksAddResourcePoliciesRequest(
            resource_policies=[consistency_group_link]
        )
        disk_client = compute_v1.RegionDisksClient()
        disk_client.add_resource_policies(
            project=project_id,
            region=disk_location,
            disk=disk_name,
            region_disks_add_resource_policies_request_resource=policy,
        )
    # For zonal disks we use DisksClient
    else:
        print("Using DisksClient")
        policy = compute_v1.DisksAddResourcePoliciesRequest(
            resource_policies=[consistency_group_link]
        )
        disk_client = compute_v1.DisksClient()
        disk_client.add_resource_policies(
            project=project_id,
            zone=disk_location,
            disk=disk_name,
            disks_add_resource_policies_request_resource=policy,
        )

    print(f"Disk {disk_name} added to consistency group {consistency_group_name}")


# [END compute_consistency_group_add_disk]
