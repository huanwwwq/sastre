"""
 Sastre - Automation Tools for Cisco SD-WAN Powered by Viptela

 cisco_sdwan.tasks.implementation
 This module contains the implementation of user-facing tasks
"""
from ._backup import TaskBackup, BackupArgs
from ._restore import TaskRestore, RestoreArgs
from ._delete import TaskDelete, DeleteArgs
from ._migrate import TaskMigrate, MigrateArgs
from ._attach_detach import TaskAttach, TaskDetach, AttachVsmartArgs, AttachEdgeArgs, DetachVsmartArgs, DetachEdgeArgs

__all__ = [
    'TaskBackup',
    'TaskRestore',
    'TaskDelete',
    'TaskMigrate',
    'TaskAttach',
    'TaskDetach',
    'BackupArgs',
    'RestoreArgs',
    'DeleteArgs',
    'MigrateArgs',
    'AttachVsmartArgs',
    'AttachEdgeArgs',
    'DetachVsmartArgs',
    'DetachEdgeArgs'
]
