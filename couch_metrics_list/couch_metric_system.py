couch_system_filtered={"_system.uptime",
    "_system.memory.other",
    "_system.memory.atom",
    "_system.memory.atom_used",
    "_system.memory.processes",
    "_system.memory.processes_used",
    "_system.memory.binary",
    "_system.memory.code",
    "_system.memory.ets",
    "_system.io_input",
    "_system.io_output"
    }

couch_system_completed={"_system.uptime",
    "_system.memory.other",
    "_system.memory.atom",
    "_system.memory.atom_used",
    "_system.memory.processes",
    "_system.memory.processes_used",
    "_system.memory.binary",
    "_system.memory.code",
    "_system.memory.ets",
    "_system.run_queue",
    "_system.run_queue_dirty_cpu",
    "_system.ets_table_count",
    "_system.context_switches",
    "_system.reductions",
    "_system.garbage_collection_count",
    "_system.words_reclaimed",
    "_system.io_input",
    "_system.io_output",
    "_system.os_proc_count",
    "_system.stale_proc_count",
    "_system.process_count",
    "_system.process_limit",
    "_system.message_queues.couch_file.count",
    "_system.message_queues.couch_file.min",
    "_system.message_queues.couch_file.max",
    "_system.message_queues.couch_file.50",
    "_system.message_queues.couch_file.90",
    "_system.message_queues.couch_file.99",
    "_system.message_queues.couch_db_updater.count",
    "_system.message_queues.couch_db_updater.min",
    "_system.message_queues.couch_db_updater.max",
    "_system.message_queues.couch_db_updater.50",
    "_system.message_queues.couch_db_updater.90",
    "_system.message_queues.couch_db_updater.99",
    "_system.message_queues.couch_server",
    "_system.message_queues.rex",
    "_system.message_queues.net_sup",
    "_system.message_queues.couch_uuids",
    "_system.message_queues.kernel_sup",
    "_system.message_queues.ioq_sup",
    "_system.message_queues.global_name_server",
    "_system.message_queues.ioq",
    "_system.message_queues.file_server_2",
    "_system.message_queues.couch_task_status",
    "_system.message_queues.dreyfus_sup",
    "_system.message_queues.ftp_sup",
    "_system.message_queues.ibrowse_sup",
    "_system.message_queues.couch_sup",
    "_system.message_queues.chttpd_sup",
    "_system.message_queues.dreyfus_index_manager",
    "_system.message_queues.ibrowse",
    "_system.message_queues.couch_proc_manager",
    "_system.message_queues.couch_epi_functions_gen_couch_index",
    "_system.message_queues.couch_epi_functions_gen_chttpd_auth",
    "_system.message_queues.release_handler",
    "_system.message_queues.couch_epi_functions_gen_couch_db",
    "_system.message_queues.couch_epi_data_gen_flags_config",
    "_system.message_queues.couch_epi_functions_gen_global_changes",
    "_system.message_queues.couch_epi_functions_gen_chttpd_handlers",
    "_system.message_queues.couch_epi_functions_gen_feature_flags",
    "_system.message_queues.couch_event_sup2",
    "_system.message_queues.couch_epi_functions_gen_chttpd",
    "_system.message_queues.couch_httpd_vhost",
    "_system.message_queues.alarm_handler",
    "_system.message_queues.couch_event_server",
    "_system.message_queues.rexi_buffer_mon",
    "_system.message_queues.chttpd_auth_cache",
    "_system.message_queues.rexi_buffer_sup",
    "_system.message_queues.ddoc_cache_sup",
    "_system.message_queues.runtime_tools_sup",
    "_system.message_queues.ddoc_cache_opener",
    "_system.message_queues.chttpd",
    "_system.message_queues.ddoc_cache_lru",
    "_system.message_queues.inet_gethost_native_sup",
    "_system.message_queues.couch_stats_sup",
    "_system.message_queues.couch_stats_process_tracker",
    "_system.message_queues.couch_stats_aggregator",
    "_system.message_queues.tftp_sup",
    "_system.message_queues.couch_plugin",
    "_system.message_queues.custodian_sup",
    "_system.message_queues.custodian_server",
    "_system.message_queues.folsom_sup",
    "_system.message_queues.couch_drv",
    "_system.message_queues.custodian_db_checker",
    "_system.message_queues.folsom_sample_slide_sup",
    "_system.message_queues.couch_peruser_sup",
    "_system.message_queues.smoosh_sup",
    "_system.message_queues.standard_error",
    "_system.message_queues.smoosh_server",
    "_system.message_queues.couch_peruser",
    "_system.message_queues.couch_server_1",
    "_system.message_queues.standard_error_sup",
    "_system.message_queues.couch_replicator_sup",
    "_system.message_queues.setup_sup",
    "_system.message_queues.tls_connection_sup",
    "_system.message_queues.folsom_metrics_histogram_ets",
    "_system.message_queues.couch_replicator_scheduler_sup",
    "_system.message_queues.couch_replicator_scheduler",
    "_system.message_queues.couch_replicator_rate_limiter",
    "_system.message_queues.mango_sup",
    "_system.message_queues.ssl_sup",
    "_system.message_queues.mem3_sync_nodes",
    "_system.message_queues.folsom_meter_timer_server",
    "_system.message_queues.mem3_sync",
    "_system.message_queues.couch_replication",
    "_system.message_queues.mem3_sup",
    "_system.message_queues.chttpd_auth_cache_lru",
    "_system.message_queues.couch_prometheus_sup",
    "_system.message_queues.mem3_events",
    "_system.message_queues.mem3_shards",
    "_system.message_queues.inet_gethost_native",
    "_system.message_queues.inets_sup",
    "_system.message_queues.couch_prometheus_server",
    "_system.message_queues.couch_epi_data_gen_dreyfus_black_list",
    "_system.message_queues.mem3_seeds",
    "_system.message_queues.inet_db",
    "_system.message_queues.ssl_pem_cache",
    "_system.message_queues.ssl_manager",
    "_system.message_queues.ssl_listen_tracker_sup",
    "_system.message_queues.couch_secondary_services",
    "_system.message_queues.mem3_reshard_sup",
    "_system.message_queues.couch_primary_services",
    "_system.message_queues.mem3_reshard_job_sup",
    "_system.message_queues.httpd_sup",
    "_system.message_queues.couch_replicator_doc_processor",
    "_system.message_queues.couch_log_sup",
    "_system.message_queues.couch_log_server",
    "_system.message_queues.sasl_safe_sup",
    "_system.message_queues.couch_replicator_connection",
    "_system.message_queues.mem3_reshard_dbdoc",
    "_system.message_queues.couch_replicator_clustering",
    "_system.message_queues.config_event",
    "_system.message_queues.global_group",
    "_system.message_queues.couch_server_8",
    "_system.message_queues.mem3_reshard",
    "_system.message_queues.ssl_connection_sup",
    "_system.message_queues.erts_code_purger",
    "_system.message_queues.couch_server_7",
    "_system.message_queues.error_logger",
    "_system.message_queues.couch_server_6",
    "_system.message_queues.sasl_sup",
    "_system.message_queues.couch_server_5",
    "_system.message_queues.mem3_nodes",
    "_system.message_queues.init",
    "_system.message_queues.couch_server_4",
    "_system.message_queues.erl_signal_server",
    "_system.message_queues.net_kernel",
    "_system.message_queues.couch_server_3",
    "_system.message_queues.couch_epi_sup",
    "_system.message_queues.config",
    "_system.message_queues.couch_server_2",
    "_system.message_queues.user",
    "_system.message_queues.erl_epmd",
    "_system.message_queues.ken_sup",
    "_system.message_queues.ssl_admin_sup",
    "_system.message_queues.ken_server",
    "_system.message_queues.mochiweb_clock",
    "_system.message_queues.timer_server",
    "_system.message_queues.dtls_udp_sup",
    "_system.message_queues.rexi_sup",
    "_system.message_queues.jwtf_sup",
    "_system.message_queues.rexi_server_sup",
    "_system.message_queues.jwtf_keystore",
    "_system.message_queues.rexi_server_mon",
    "_system.message_queues.rexi_server",
    "_system.message_queues.code_server",
    "_system.message_queues.httpc_sup",
    "_system.message_queues.erl_prim_loader",
    "_system.message_queues.dtls_connection_sup",
    "_system.message_queues.kernel_safe_sup",
    "_system.message_queues.application_controller",
    "_system.message_queues.httpc_profile_sup",
    "_system.message_queues.config_sup",
    "_system.message_queues.global_changes_sup",
    "_system.message_queues.httpc_manager",
    "_system.message_queues.couch_index_sup",
    "_system.message_queues.global_changes_server",
    "_system.message_queues.auth",
    "_system.message_queues.httpc_handler_sup",
    "_system.message_queues.couch_index_server",
    "_system.internal_replication_jobs"
    }