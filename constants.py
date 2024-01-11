# OpenAI key
APIKEY = "<OpenAI Key>"

# Salesforce credentials
USERNAME = '<your_username>'
PASSWORD = '<your_password>'
SECURITY_TOKEN = '<security_token>' #you will find this in user settings
DOMAIN = '.my.salesforce.com'
DOMAIN_FULL = "https://<your_domain>.my.salesforce.com"
CONSUMER_KEY = "<consumer_key>" #create connected app in salesforce and then use consumer key here
CONSUMER_SECRET = "<consumer_secret>" #create connected app in salesforce and then use consumer key here

# Salesforce Queries
QUERY_PERMISSION_SET_ASSIGNMENT = "SELECT id,Assignee.Name,PermissionSet.Name, Assignee.Profile.Name,Format(SystemModstamp) from PermissionSetAssignment"
QUERY_PERMISSION_SETS = "Select Name,Type,ProfileId,PermissionsAccessCMC,PermissionsAccessContentBuilder,PermissionsAccessToServiceProcess,PermissionsAccountSwitcherUser,PermissionsActivateContract,PermissionsActivateOrder,PermissionsActivitiesAccess,PermissionsAddAnalyticsRemoteConnections,PermissionsAddDirectMessageMembers,PermissionsAddWaveNotificationRecipients,PermissionsAICreateInsightObjects,PermissionsAIViewInsightObjects,PermissionsAllowEmailIC,PermissionsAllowLightningLogin,PermissionsAllowObjectDetection,PermissionsAllowObjectDetectionTraining,PermissionsAllowUniversalSearch,PermissionsAllowViewEditConvertedLeads,PermissionsAllowViewKnowledge,PermissionsApexRestServices,PermissionsApiEnabled,PermissionsApiUserOnly,PermissionsAssignPermissionSets,PermissionsAssignTopics,PermissionsAuthorApex,PermissionsAutomaticActivityCapture,PermissionsB2BMarketingAnalyticsUser,PermissionsBotManageBots,PermissionsBotManageBotsTrainingData,PermissionsBulkApiHardDelete,PermissionsBulkMacrosAllowed,PermissionsBypassMFAForUiLogins,PermissionsCampaignInfluence2,PermissionsCanAccessCE,PermissionsCanApproveFeedPost,PermissionsCanEditDataPrepRecipe,PermissionsCanEditPrompts,PermissionsCanInsertFeedSystemFields,PermissionsCanManageMaps,PermissionsCanUseNewDashboardBuilder,PermissionsCanVerifyComment,PermissionsChangeDashboardColors,PermissionsChatterComposeUiCodesnippet,PermissionsChatterEditOwnPost,PermissionsChatterEditOwnRecordPost,PermissionsChatterFileLink,PermissionsChatterInternalUser,PermissionsChatterInviteExternalUsers,PermissionsChatterOwnGroups,PermissionsClientSecretRotation,PermissionsCloseConversations,PermissionsConfigCustomRecs,PermissionsConnectOrgToEnvironmentHub,PermissionsConsentApiUpdate,PermissionsContentAdministrator,PermissionsContentHubUser,PermissionsContentWorkspaces,PermissionsConvertLeads,PermissionsCreateCustomizeDashboards,PermissionsCreateCustomizeFilters,PermissionsCreateCustomizeReports,PermissionsCreateDashboardFolders,PermissionsCreateLtngTempFolder,PermissionsCreateLtngTempInPub,PermissionsCreatePackaging,PermissionsCreateReportFolders,PermissionsCreateReportInLightning,PermissionsCreateTopics,PermissionsCreateWorkBadgeDefinition,PermissionsCreateWorkspaces,PermissionsCustomizeApplication,PermissionsCustomMobileAppsAccess,PermissionsCustomSidebarOnAllPages,PermissionsDataExport,PermissionsDelegatedTwoFactor,PermissionsDeleteActivatedContract,PermissionsDeleteTopics,PermissionsDistributeFromPersWksp,PermissionsEditActivatedOrders,PermissionsEditBillingInfo,PermissionsEditBrandTemplates,PermissionsEditCaseComments,PermissionsEditEvent,PermissionsEditHtmlTemplates,PermissionsEditKnowledge,PermissionsEditMyDashboards,PermissionsEditMyReports,PermissionsEditOppLineItemUnitPrice,PermissionsEditPublicDocuments,PermissionsEditPublicFilters,PermissionsEditPublicTemplates,PermissionsEditReadonlyFields,PermissionsEditTask,PermissionsEditTopics,PermissionsEmailAdministration,PermissionsEmailMass,PermissionsEmailSingle,PermissionsEmailTemplateManagement,PermissionsEnableBCTransactionPolling,PermissionsEnableCommunityAppLauncher,PermissionsEnableIPFSUpload,PermissionsEnableNotifications,PermissionSetGroupId,PermissionsExportReport,PermissionsFeedPinning,PermissionsFlowUFLRequired,PermissionsForceTwoFactor,PermissionsFSCArcGraphCommunityUser,PermissionsFSCComprehensiveUserAccess,PermissionsGiveRecognitionBadge,PermissionsGovernNetworks,PermissionsHasUnlimitedNBAExecutions,PermissionsHeadlessCMSAccess,PermissionsHideReadByList,PermissionsIdentityConnect,PermissionsIdentityEnabled,PermissionsImportCustomObjects,PermissionsImportLeads,PermissionsImportPersonal,PermissionsInsightsAppAdmin,PermissionsInsightsAppDashboardEditor,PermissionsInsightsAppEltEditor,PermissionsInsightsAppUploadUser,PermissionsInsightsAppUser,PermissionsInsightsCreateApplication,PermissionsInstallPackaging,PermissionsIotUser,PermissionsIsotopeAccess,PermissionsIsotopeCToCUser,PermissionsIsotopeLEX,PermissionsLearningManager,PermissionsLifecycleManagementAPIUser,PermissionsLightningConsoleAllowedForUser,PermissionsLightningExperienceUser,PermissionsListEmailSend,PermissionsLMEndMessagingSessionUserPerm,PermissionsLMOutboundMessagingUserPerm,PermissionsLtngPromoReserved01UserPerm,PermissionsManageAnalyticSnapshots,PermissionsManageAuthProviders,PermissionsManageBusinessHourHolidays,PermissionsManageC360AConnections,PermissionsManageCallCenters,PermissionsManageCases,PermissionsManageCategories,PermissionsManageCertificates,PermissionsManageChatterMessages,PermissionsManageCMS,PermissionsManageContentPermissions,PermissionsManageContentProperties,PermissionsManageContentTypes,PermissionsManageCustomPermissions,PermissionsManageCustomReportTypes,PermissionsManageDashbdsInPubFolders,PermissionsManageDataCategories,PermissionsManageDataIntegrations,PermissionsManageDynamicDashboards,PermissionsManageEmailClientConfig,PermissionsManageEncryptionKeys,PermissionsManageEntitlements,PermissionsManageExchangeConfig,PermissionsManageExternalConnections,PermissionsManageHealthCheck,PermissionsManageHubConnections,PermissionsManageInteraction,PermissionsManageInternalUsers,PermissionsManageIpAddresses,PermissionsManageKnowledge,PermissionsManageKnowledgeImportExport,PermissionsManageLeads,PermissionsManageLearningReporting,PermissionsManageLoginAccessPolicies,PermissionsManageMobile,PermissionsManageNetworks,PermissionsManageOrchInstsAndWorkItems,PermissionsManagePasswordPolicies,PermissionsManageProfilesPermissionsets,PermissionsManagePropositions,PermissionsManagePvtRptsAndDashbds,PermissionsManageRecommendationStrategies,PermissionsManageReleaseUpdates,PermissionsManageRemoteAccess,PermissionsManageReportsInPubFolders,PermissionsManageRoles,PermissionsManageSearchPromotionRules,PermissionsManageSecurityCommandCenter,PermissionsManageSessionPermissionSets,PermissionsManageSharing,PermissionsManageSolutions,PermissionsManageSubscriptions,PermissionsManageSurveys,PermissionsManageSynonyms,PermissionsManageTemplatedApp,PermissionsManageTranslation,PermissionsManageTwoFactor,PermissionsManageUnlistedGroups,PermissionsManageUsers,PermissionsMassInlineEdit,PermissionsMergeTopics,PermissionsModerateChatter,PermissionsModerateNetworkUsers,PermissionsModifyAllData,PermissionsModifyDataClassification,PermissionsModifyMetadata,PermissionsNativeWebviewScrolling,PermissionsNewReportBuilder,PermissionsOmnichannelInventorySync,PermissionsPackaging2,PermissionsPackaging2Delete,PermissionsPasswordNeverExpires,PermissionsPaymentsAPIUser,PermissionsPreventClassicExperience,PermissionsPrivacyDataAccess,PermissionsPublishPackaging,PermissionsQueryAllFiles,PermissionsQuipMetricsAccess,PermissionsQuipUserEngagementMetrics,PermissionsRemoveDirectMessageMembers,PermissionsResetPasswords,PermissionsRunFlow,PermissionsRunReports,PermissionsSalesConsole,PermissionsSalesforceIQInbox,PermissionsSalesforceIQInternal,PermissionsSandboxTestingInCommunityApp,PermissionsScheduleReports,PermissionsSelectFilesFromSalesforce,PermissionsSendAnnouncementEmails,PermissionsSendCustomNotifications,PermissionsSendSitRequests,PermissionsShareInternalArticles,PermissionsShowCompanyNameAsUserBadge,PermissionsSkipIdentityConfirmation,PermissionsSolutionImport,PermissionsStdAutomaticActivityCapture,PermissionsSubmitMacrosAllowed,PermissionsSubscribeDashboardRolesGrps,PermissionsSubscribeDashboardToOtherUsers,PermissionsSubscribeReportRolesGrps,PermissionsSubscribeReportsRunAsUser,PermissionsSubscribeReportToOtherUsers,PermissionsSubscribeToLightningDashboards,PermissionsSubscribeToLightningReports,PermissionsTraceXdsQueries,PermissionsTransactionalEmailSend,PermissionsTransactionSecurityExempt,PermissionsTransferAnyCase,PermissionsTransferAnyEntity,PermissionsTransferAnyLead,PermissionsTwoFactorApi,PermissionsUseAssistantDialog,PermissionsUseMySearch,PermissionsUseOmnichannelInventoryAPIs,PermissionsUseQuerySuggestions,PermissionsUseSubscriptionEmails,PermissionsUseTeamReassignWizards,PermissionsUseTemplatedApp,PermissionsUseWebLink,PermissionsViewAllActivities,PermissionsViewAllCustomSettings,PermissionsViewAllData,PermissionsViewAllForeignKeyNames,PermissionsViewAllProfiles,PermissionsViewAllUsers,PermissionsViewAnomalyEvents,PermissionsViewContent,PermissionsViewDataAssessment,PermissionsViewDataCategories,PermissionsViewDataLeakageEvents,PermissionsViewDeveloperName,PermissionsViewEncryptedData,PermissionsViewEventLogFiles,PermissionsViewHealthCheck,PermissionsViewHelpLink,PermissionsViewMLModels,PermissionsViewMyTeamsDashboards,PermissionsViewOnlyEmbeddedAppUser,PermissionsViewPlatformEvents,PermissionsViewPrivateStaticResources,PermissionsViewPublicDashboards,PermissionsViewPublicReports,PermissionsViewRestrictionAndScopingRules,PermissionsViewRoles,PermissionsViewSecurityCommandCenter,PermissionsViewSetup,PermissionsViewUserPII,PermissionsWaveCommunityUser,PermissionsWaveManagePrivateAssetsUser,PermissionsWaveTabularDownload,PermissionsWorkCalibrationUser,PermissionsWorkDotComUserPerm from PermissionSet WHERE Type != 'Profile'"
QUERY_OBJECT_PERMISSIONS = "Select Parent.Profile.Name,PermissionsCreate,PermissionsDelete,PermissionsEdit,PermissionsModifyAllRecords,PermissionsRead,PermissionsViewAllRecords,SobjectType From ObjectPermissions"
QUERY_USERS = "SELECT Id,isActive,CreatedDate FROM User"
QUERY_OBJECTS = "SELECT Id,QualifiedApiName, Label, ExternalSharingModel, InternalSharingModel, DurableId, DeploymentStatus, NamespacePrefix, LastModifiedDate, LastModifiedById FROM EntityDefinition ORDER BY QualifiedApiName"
QUERY_TOTAL_PERMISSION_SETS = "SELECT count(Id) FROM PermissionSet"
QUERY_TOTAL_PROFILES = "SELECT count(Id) FROM Profile"
QUERY_TOTAL_PACKAGES = "SELECT count(Id) FROM PackageLicense"
QUERY_ACCOUNTS = "SELECT Id, BillingCountry,AnnualRevenue FROM Account"