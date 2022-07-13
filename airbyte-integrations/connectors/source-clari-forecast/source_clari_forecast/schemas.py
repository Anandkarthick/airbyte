def source_schema():
    schema = {
                "default_entries": {
                                "$schema": "http://json-schema.org/draft-07/schema#",
                                "type": "object",
                                "properties": {
                                "forecastValue": {
                                    "type": ["null", "number"]
                                },
                                "currency": {
                                    "type": ["null", "object"],
                                    "properties": {
                                    "code": {
                                        "type": "string"
                                    },
                                    "symbol": {
                                        "type": "string"
                                    }
                                    }
                                },
                                "isUpdated":{
                                    "type": "boolean"
                                },
                                "timeFrameId": {
                                    "type": "string"
                                },
                                "timePeriodId": {
                                    "type": "string"
                                },
                                "fieldId": {
                                    "type": "string"
                                },
                                "userId": {
                                    "type": "string"
                                },
                                "updatedBy": {
                                    "type": "string"
                                },
                                "updatedOn":{
                                    "type": ["null", "number"]
                                }
                                }
                            },
                "default_users" : {
                                    "$schema": "http://json-schema.org/draft-07/schema#",
                                    "type": "object",
                                    "properties": {
                                    "userId": {
                                        "type": ["null", "string"]
                                        },
                                    "name": {
                                        "type": ["null", "string"]
                                        },
                                    "email": {
                                        "type": ["null", "string"]
                                        },
                                    "scopeId": {
                                        "type": ["null", "string"]
                                        },
                                    "crmId": {
                                        "type": ["null", "string"]
                                        },
                                    "hierarchyId": {
                                        "type": ["null", "string"]
                                        },
                                    "hierarchyName": {
                                        "type": ["null", "string"]
                                        },
                                    "parentHierarchyId": {
                                        "type": ["null", "string"]
                                    },
                                    "parentHierarchyName": {
                                        "type": ["null", "string"]
                                    }
                                }   
                            },
                "default_fields": {
                                    "$schema": "http://json-schema.org/draft-07/schema#",
                                    "type": "object",
                                    "properties": {
                                    "fieldId": {
                                        "type": "string"
                                        },
                                    "fieldName": {
                                        "type": "string"
                                        },
                                    "fieldType": {
                                        "type": "string"
                                        }
                                }   
                                },
                "default_timeperiods": {
                                    "$schema": "http://json-schema.org/draft-07/schema#",
                                    "type": "object",
                                    "properties": {
                                    "timePeriodId": {
                                        "type": "string"
                                        },
                                    "type": {
                                        "type": "string"
                                        },
                                    "label": {
                                        "type": "string"
                                        },
                                    "year": {
                                        "type": "string"
                                        },
                                    "startDate": {
                                        "type": "string"
                                        },
                                    "endDate": {
                                        "type": "string"
                                        },
                                    "crmId": {
                                        "type": "string"
                                    }
                                }   
                                },
                "default_timeframes": {
                                    "$schema": "http://json-schema.org/draft-07/schema#",
                                    "type": "object",
                                    "properties": {
                                        "timeFrameId": {
                                            "type": "string"
                                        },
                                        "startDate": {
                                            "type": "string"
                                        },
                                        "endDate": {
                                            "type": "string"
                                        }
                                    }   
                                    },
                "quota_entries": {
                                    "$schema": "http://json-schema.org/draft-07/schema#",
                                    "type": "object",
                                    "properties": {
                                    "quotaValue": {
                                        "type": ["null", "number"]
                                    },
                                    "currency": {
                                        "type": ["null", "object"],
                                        "properties": {
                                        "code": {
                                            "type": "string"
                                        },
                                        "symbol": {
                                            "type": "string"
                                        }
                                        }
                                    },
                                    "timeFrameId": {
                                        "type": "string"
                                    },
                                    "timePeriodId": {
                                        "type": "string"
                                    },
                                    "fieldId": {
                                        "type": "string"
                                    },
                                    "userId": {
                                        "type": "string"
                                    }
                                    }
                                },
                "quota_users" : {
                                    "$schema": "http://json-schema.org/draft-07/schema#",
                                    "type": "object",
                                    "properties": {
                                    "userId": {
                                        "type": ["null", "string"]
                                        },
                                    "name": {
                                        "type": ["null", "string"]
                                        },
                                    "email": {
                                        "type": ["null", "string"]
                                        },
                                    "scopeId": {
                                        "type": ["null", "string"]
                                        },
                                    "crmId": {
                                        "type": ["null", "string"]
                                        },
                                    "hierarchyId": {
                                        "type": ["null", "string"]
                                        },
                                    "hierarchyName": {
                                        "type": ["null", "string"]
                                        },
                                    "parentHierarchyId": {
                                        "type": ["null", "string"]
                                    },
                                    "parentHierarchyName": {
                                        "type": ["null", "string"]
                                    }
                                }   
                            },
                "quota_fields": {
                                    "$schema": "http://json-schema.org/draft-07/schema#",
                                    "type": "object",
                                    "properties": {
                                    "fieldId": {
                                        "type": "string"
                                        },
                                    "fieldName": {
                                        "type": "string"
                                        },
                                    "fieldType": {
                                        "type": "string"
                                        }
                                }   
                                },
                "quota_timeperiods": {
                                    "$schema": "http://json-schema.org/draft-07/schema#",
                                    "type": "object",
                                    "properties": {
                                    "timePeriodId": {
                                        "type": "string"
                                        },
                                    "type": {
                                        "type": "string"
                                        },
                                    "label": {
                                        "type": "string"
                                        },
                                    "year": {
                                        "type": "string"
                                        },
                                    "startDate": {
                                        "type": "string"
                                        },
                                    "endDate": {
                                        "type": "string"
                                        },
                                    "crmId": {
                                        "type": "string"
                                    }
                                }   
                                },
                "quota_timeframes": {
                                    "$schema": "http://json-schema.org/draft-07/schema#",
                                    "type": "object",
                                    "properties": {
                                        "timeFrameId": {
                                            "type": "string"
                                        },
                                        "startDate": {
                                            "type": "string"
                                        },
                                        "endDate": {
                                            "type": "string"
                                        }
                                    }   
                                }
                }
    return schema