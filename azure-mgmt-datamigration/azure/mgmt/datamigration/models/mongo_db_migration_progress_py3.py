# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .mongo_db_progress_py3 import MongoDbProgress


class MongoDbMigrationProgress(MongoDbProgress):
    """Describes the progress of the overall migration.

    All required parameters must be populated in order to send to Azure.

    :param bytes_copied: Required. The number of document bytes copied during
     the Copying stage
    :type bytes_copied: long
    :param documents_copied: Required. The number of documents copied during
     the Copying stage
    :type documents_copied: long
    :param elapsed_time: Required. The elapsed time in the format
     [ddd.]hh:mm:ss[.fffffff] (i.e. TimeSpan format)
    :type elapsed_time: str
    :param errors: Required. The errors and warnings that have occurred for
     the current object. The keys are the error codes.
    :type errors: dict[str, ~azure.mgmt.datamigration.models.MongoDbError]
    :param events_pending: Required. The number of oplog events awaiting
     replay
    :type events_pending: long
    :param events_replayed: Required. The number of oplog events replayed so
     far
    :type events_replayed: long
    :param last_event_time: The timestamp of the last oplog event received, or
     null if no oplog event has been received yet
    :type last_event_time: datetime
    :param last_replay_time: The timestamp of the last oplog event replayed,
     or null if no oplog event has been replayed yet
    :type last_replay_time: datetime
    :param name: The name of the progress object. For a collection, this is
     the unqualified collection name. For a database, this is the database
     name. For the overall migration, this is null.
    :type name: str
    :param qualified_name: The qualified name of the progress object. For a
     collection, this is the database-qualified name. For a database, this is
     the database name. For the overall migration, this is null.
    :type qualified_name: str
    :param result_type: Required. The type of progress object. Possible values
     include: 'Migration', 'Database', 'Collection'
    :type result_type: str or ~azure.mgmt.datamigration.models.enum
    :param state: Required. Possible values include: 'NotStarted',
     'ValidatingInput', 'Initializing', 'Restarting', 'Copying',
     'InitialReplay', 'Replaying', 'Finalizing', 'Complete', 'Canceled',
     'Failed'
    :type state: str or ~azure.mgmt.datamigration.models.MongoDbMigrationState
    :param total_bytes: Required. The total number of document bytes on the
     source at the beginning of the Copying stage, or -1 if the total size was
     unknown
    :type total_bytes: long
    :param total_documents: Required. The total number of documents on the
     source at the beginning of the Copying stage, or -1 if the total count was
     unknown
    :type total_documents: long
    :param databases: The progress of the databases in the migration. The keys
     are the names of the databases
    :type databases: dict[str,
     ~azure.mgmt.datamigration.models.MongoDbDatabaseProgress]
    """

    _validation = {
        'bytes_copied': {'required': True},
        'documents_copied': {'required': True},
        'elapsed_time': {'required': True},
        'errors': {'required': True},
        'events_pending': {'required': True},
        'events_replayed': {'required': True},
        'result_type': {'required': True},
        'state': {'required': True},
        'total_bytes': {'required': True},
        'total_documents': {'required': True},
    }

    _attribute_map = {
        'bytes_copied': {'key': 'bytesCopied', 'type': 'long'},
        'documents_copied': {'key': 'documentsCopied', 'type': 'long'},
        'elapsed_time': {'key': 'elapsedTime', 'type': 'str'},
        'errors': {'key': 'errors', 'type': '{MongoDbError}'},
        'events_pending': {'key': 'eventsPending', 'type': 'long'},
        'events_replayed': {'key': 'eventsReplayed', 'type': 'long'},
        'last_event_time': {'key': 'lastEventTime', 'type': 'iso-8601'},
        'last_replay_time': {'key': 'lastReplayTime', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'qualified_name': {'key': 'qualifiedName', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'total_bytes': {'key': 'totalBytes', 'type': 'long'},
        'total_documents': {'key': 'totalDocuments', 'type': 'long'},
        'databases': {'key': 'databases', 'type': '{MongoDbDatabaseProgress}'},
    }

    def __init__(self, *, bytes_copied: int, documents_copied: int, elapsed_time: str, errors, events_pending: int, events_replayed: int, result_type, state, total_bytes: int, total_documents: int, last_event_time=None, last_replay_time=None, name: str=None, qualified_name: str=None, databases=None, **kwargs) -> None:
        super(MongoDbMigrationProgress, self).__init__(bytes_copied=bytes_copied, documents_copied=documents_copied, elapsed_time=elapsed_time, errors=errors, events_pending=events_pending, events_replayed=events_replayed, last_event_time=last_event_time, last_replay_time=last_replay_time, name=name, qualified_name=qualified_name, result_type=result_type, state=state, total_bytes=total_bytes, total_documents=total_documents, **kwargs)
        self.databases = databases
