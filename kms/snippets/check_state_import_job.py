# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and


# [START kms_check_state_import_job]
from google.cloud import kms


def check_state_import_job(
    project_id: str, location_id: str, key_ring_id: str, import_job_id: str
) -> None:
    """
    Check the state of an import job in Cloud KMS.

    Args:
        project_id (string): Google Cloud project ID (e.g. 'my-project').
        location_id (string): Cloud KMS location (e.g. 'us-east1').
        key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
        import_job_id (string): ID of the import job (e.g. 'my-import-job').
    """

    # Create the client.
    client = kms.KeyManagementServiceClient()

    # Retrieve the fully-qualified import_job string.
    import_job_name = client.import_job_path(
        project_id, location_id, key_ring_id, import_job_id
    )

    # Retrieve the state from an existing import job.
    import_job = client.get_import_job(name=import_job_name)

    print(f"Current state of import job {import_job.name}: {import_job.state}")


# [END kms_check_state_import_job]