old_tickers = ["CAN", "AMD", "TSLA", "DVN", "WORK", "AMZN", "DO", "FFIV", "SNAP", "MANU", "CMCSA", "CXO", "AAPL","MELI", "FMC", "INTC", "IDXX", "EIX", "ALGN", "FSLR", "RTN", "SPOT", "COP", "LMT", "TWTR", "BUD", "AIR","DISCA", "GE", "AAP", "MMM", "EQR", "GILD", "FCX", "CVX", "UL", "DOV", "DVA", "EFX", "SU", "WBA", "DHR","ET", "EXPD", "MSFT", "EZJ", "ANSS", "CAT", "LYG", "SLB", "PYPL", "BMY", "OR", "FLS", "ADBE", "BAC", "NKE","ETFC", "EONGY", "RACE", "FB", "COST", "DHI", "EBAY", "BP", "JPM", "ACN", "AA", "XOM", "KO", "AGN", "RBS","EMR", "NVDA", "HAS", "MA", "GOOGL", "SYK", "ESS", "FITB", "EXR", "ADSK", "DAL", "EQT", "TMUS", "PFE", "CRM","BIDU", "MU", "ECL", "HSBC", "MS", "GS", "FIS", "TFX", "AMGN", "HON", "CVS", "CTAS", "ETR", "NEE", "VZ","DRE", "ABBV", "MCD", "BYND", "PM", "IBM", "CTXS", "FISV", "NFLX", "QCOM", "RMD", "ATVI", "SBUX", "VOD","CSCO", "FRT", "FE", "ED", "CL", "ZM", "PG", "DIS", "DRI", "BA", "PST", "KHC", "DTE", "WMT", "CRON", "EMN","ABT", "LYFT", "DLR", "BBY", "DFS", "TEF", "CTL", "MDT", "MO", "DBX", "BBVA", "GM", "CGC", "PINS", "TLRY", "GWPH", "ACB"]
new_tickers = ["AAPL","ABBNsEQ","AMZN","ELF","TSLA","VUSAl","FB","GOOGL","MSFT","NIO","NVDA","BABA","HCMC","MCD","NFLX","PLTR","RRl","T","AMD","BPl","COIN","DIS","SBUX","PEP","PYPL","INTC","WBD","ADP","AGNC","BYND1","PSEC","TLRY1","TROW","CCIV","EZJl","INRGl","BATSl","IAGl","LLOYl","NGl","SHELl","BARCl","CINEl","RBl","PLUG","AMLl","SEMBl","SSHYl","STHSl","TSCOl","VGOVl","ABNB","ALPP","GSKl","RIVN","ARBl","VODl","VTIQ","SNDL","AZNl","BNGO","GEHC","PTON","RIOl","VFEMl","VHYLl","VUKEl","ZM","ACB","ADBE","ECARl","ETSY","FCEL","IITU","NAKD","ULVRl","BAl","HLNl","HSBAl","LGENl","PNNl","ROKU","SGLNl","VWRLl","CCLl","CRSP","CSCO","DEAC","ENPH","HOOD","IPOE","MRNA","QCOM","SDC","AAL","ADSK","AIRp","AVl","BLNK","CIIC","CRWD","CSIQ","CSPX","EQQQl","FMCI","FPp","GOOG","HITIF","MCp","MELI","NETE","NNDM","OCDOl","PMOl","RIOT","SEDG","SMTl","TUIl","VUAAl","VUSDl","WKHS","ATVI","AVGO","BBBY","BLDP","BTl","CGC","COST","CRSR","CTRM","DGEl","DOCU","FSLR","INTUl","GEVO","IDEX","IMBl","IUKPl","JDWl","MARA","MU","OD7Fd","PSNl","RMGl","STNE","TTWO","UKDVl","UKWl","2NVDl","2OIEl","2OIGl","2OIGm","2OILl","2PALl","2STEl","2STRl","2STRm","2STSl","2SZMl","2SZMm","2TRVm","2TSEl","2TSLl","2UBEl","2UBRl","2UKLl","2UKSl","2VISl","3AAPl","3ABEl","3ABNl","3ADEl","2MCLl","2MSFl","2MUEl","2MUl","2MXp","2NFLl","3AIEl","3AIRl","3AKEl","3AKWl","3AMDl","3AMEl","3AMZl","3APEl","3AREl","3ARGl","3ARKl","3ARWl","3ASMl","3BABl","3BACl","3BAEl","3BAl","3BBEl","3BCEl","3BIDl","3BIEl","3BLRl","3BPEl","3BPl","3BRLl","3BTLm","3BULm","3CFLl","3CHEl","3CHIl","3CNEl","3CONl","3CPNl","3CREl","3CRMl","3DAXl","3DELl","3DESl","3DIEl","3DISl","3DXEl","3EULl","3EUSl","3FBEl","3FBl","3FNEl","3FNGl","3FNPl","3FTEl","3FTGl","3FTPl","3GDEl","3GDXl","3GFMl","3GILl","3GISl","3GLDl","3GLEl","3GMEl","3GMPl","3GOEl","3GOLl","3GOOl","3GOSl","3HCLl","3HCSl","3HSBl","3HSEl","3IBBl","3IBEl","3ICEl","3ICLl","3IFEl","3IFXl","3INl","3JDEl","3JDl","3JEEl","3JETl","3JPEl","3JPNl","3KORl","3KWBl","3KWEl","3LAAl","3LAEl","3LALl","3LAMl","3LAMp","3LAPl","3LARp","3LAXp","3LAZl","3LBA1l","3LBC1l","3LBNp","3LBPl","3LCOm","3LDAp","3LDEl","3LDOl","3LEUl","3LFBl","3LFEl","3LFPl","3LGEl","3LGLl","3LGPl","3LGSl","3LIEl","3LINl","3LIPl","3LIl","3LLLl","3LLVp","3LMEl","3LMIl","3LMIm","3LMOl","3LMOp","3LMPl","3LMSl","3LNEl","3LNFl","3LNGl","3LNIl","3LNPl","3LNVl","3LOIl","3LORp","3LPAl","3LPAp","3LPEl","3LPOl","3LPOm","3LPPl","3LPPm","3LRDl","3LRIl","3LSAp","3LSEp","3LSIl","3LSNp","3LSQl","3LSQm","3LSTp","3LTEl","3LTOp","3LTPl","3LTSl","3LUBl","3LUEl","3LUPl","3LUS1l","3LVEl","3LVOl","3LVPl","3LVWp","3LWPl","3LZNl","3LZPl","3MBEl","3MBGl","3MREl","3MRNl","3MSEl","3MSFl","3NFEl","3NFLl","3NGLl","3NGSl","3NIEl","3NIOl","3NVDl","3NVEl","3OILl","3OISl","3PLEl","3PLTl","3PLUl","3PREl","3PYEl","3PYPl","3QQEl","3QQQl","3RDEl","3RDSl","3ROEl","3ROKl","3S1El","3S1Pl","3S2El","3S2Pl","3S3El","3S3Pl","3SAAl","3SAAm","3SAEl","3SALl","3SAMl","3SAMp","3SAPl","3SARp","3SAXp","3SAZl","3SBAl","3SBBl","3SBCl","3SBEl","3SBNp","3SBPl","3SDAp","3SDEl","3SDOl","3SEEl","3SFBl","3SFEl","3SFGl","3SFPl","3SFTl","3SGEl","3SGFl","3SGGl","3SGLl","3SGOl","3SGPl","3SHEl","3SHPl","3SIEl","3SILl","3SIPl","3SISl","3SKEl","3SLVp","3SMEl","3SMHl","3SLEl","3SLLl","3SLVl","3SMDl","3SMFl","3SMIl","3SMIm","3SMOl","3SMOp","3SMPl","3SMSl","3SNEl","3SMTl","3SMZl","3SNFl","3SNIl","3SNPl","3SNVl","3SOIl","3SORp","3SPAp","3SPEl","3SPAl","3SPOl","3SPOm","3SPPl","3SPPm","3SPYl","3SQEl","3SQl","3SRDl","3SRIl","3SRRl1","3SSAp","3SSEp","3SSIl","3SSLl","3SSNp","3SSQl","3SSQm","3SSTp","3STEl","3STLl","3STOp","3STPl","3STSl","3SUBl","3SUEl","3SUPl","3SVEl","3SVO1l","3SVPl","3SVWp","3SWPl","3SXLl","3SYEl","3SZNl","3SZPl","3TAEl","3TAIl","3TSEl","3TSLl","3TSMl","3TYLl","3TYLm","3TYSm","3UBEl","3UBRl","3UKLl","3UKSl","3ULSl","3USLl","3USSl","3VDEl","3VODl","3VTEl","3VTl","3VWEl","3VWl","3XEEl","3XFEl","3XLEl","3XLFl","3XPEl","3XPVl","3ZMEl","3ZMl","5BUSm","5CH6d","5ESGl","5HEDl","5QQEl","5QQQl","5SPEl","5SPYl","5TYSm","888l","AAAPl","AACG","AACI","AACQ","AACp","AADVl","AAFl","AAIFl","AALl","AAME","AAOI","AAON","AAP1l","AAP2l","AAP3l","AAPEl","AAPLl","AAPSl","AASGl","AASIp","AASl","AATGl","AAWW","AAXN","ABCB","ABCL","ABCM","ABDl","ABEO","ABFl","ABGI","ABIO","ABN1l","ABN3l","ABNBl","ABNSl","ABOS","ABSI","ABST","ABUS","ABVC","ACAB","ACAC","ACAD","ACAH","ACAp","ACBA","ACCD","ACER","ACET","ACEV","ACGL","ACHC","ACHL","ACHV","ACIU","ACIW","ACLS","ACLX","ACMR","ACNB","ACND","ACON","ACOR","ACPEl","ACQR","ACRS","ACRX","ACST","ACTC","ACTD","ACTG","ACT","ACUIF","ACVA","ACWDl","ACWIl","ACXP","ACp","ADAG","ADAL","ADAP","ADER","ADES","ADGI","ADIGl","ADIL","ADI","ADMA","ADMP","ADMl","ADOC","ADOM","ADPT","ADPp","ADRO","ADT1l","ADTN","ADTX","ADUS","ADVICp","ADVM","ADXN","AEAC","AEAE","AEEEl","AEETl","AEGGl","AEHA","AEHR","AEIS","AELISp","AEMCl","AEMD","AEMUl","AEPl","AERC","AERIl","AERSl","AESE","AEWUl","AEXl","AEYE","AEY","AEZS","AFAC","AFAR","AFBI","AFCG","AFIB","AFIN","AFMD","AFMEp","AFRM","AFYA","AFp","AGBA","AGBPl","AGC","AGEDl","AGEDm","AGEN","AGESl","AGFS","AGFY","AGGBl","AGGGl","AGGR","AGIO","AGLE","AGMH","AGRI","AGROl","AGRUl","AGRX","AGRl","AGYS","AHAC","AHCO","AHI","AHPA","AHPI","AHRN","AHTl","AIAIl","AIAIm","AIBGl","AIB","AIEl","AIGAl","AIGCl","AIGEl","AIGGl","AIGIl","AIGLl","AIGOl","AIGPl","AIGSl","AIHS","AIH","AIKI","AIMC","AINV","AIP","AIR3l","AIREl","AIRG","AIRS","AIRSl","AIRT","AJAXl","AJBl","AJGl","AJITl","AJOTl","AKAM","AKAN","AKBA","AKER","AKEp","AKRO","AKTS","AKTX","AKYA","AL3Sl","ALACTp","ALAFYp","ALAGOp","ALAGl","ALAIRp","ALAIl","ALAMAp","ALAUDp","ALBIZp","ALBOAp","ALBOOp","ALBO","ALBPKp","ALBPSp","ALCAPp","ALCARp","ALCO","ALCRBp","ALCWEp","ALDLTp","ALDMSp","ALDNEp","ALDX","ALDp","ALEC","ALENOp","ALESEp","ALEUPp","ALFAl","ALFREp","ALFl","ALGAUp","ALGBEp","ALGM","ALGN","ALGS","ALGT","ALGWl","ALHAFp","ALHC","ALHEOp","ALHFp","ALHGOp","ALHGRp","ALHPIp","ALHRSp","ALHYPp","ALICAp","ALIKOp","ALIM","ALINNp","ALKALp","ALKEMp","ALKEYp","ALKKOp","ALKS","ALKT","ALKl","ALLGOp","ALLK","ALLO","ALLR","ALLT","ALMDPp","ALMICp","ALMLBp","ALMl","ALNFLp","ALNMRp","ALNY","ALODCp","ALOKWp","ALOR","ALOT","ALOp","ALPA","ALPHEp","ALPN","ALPX","ALRIBp","ALRM","ALRN","ALRPDp","ALRS","ALSA","ALSPTp","ALTNl","ALTOOp","ALTR","ALTTUp","ALTU","ALT","ALUMl","ALVAPp","ALVETp","ALVMGp","ALVR","ALWFp","ALXO","ALYUl","ALZN","AM3Sl","AMAL","AMALl","AMALm","AMAO","AMAPl","AMAT","AMBA","AMCII","AMCI","AMCX","AMD2l","AMD3l","AMDSl","AMED","AMEH","AMGN","AMGOl","AMHC","AMKR","AMLX","AMNB","AMOT","AMPG","AMPH","AMPL","AMRH","AMRK","AMRN","AMRS","AMSC","AMSF","AMST","AMSWA","AMTB","AMTI","AMTX","AMUNp","AMV","AMWD","AMYT","AMZ1l","AMZ2l","AMZ3l","AMZEl","AMZNl","AMZSl","AMp","ANAB","ANCN","ANDA","ANDE","ANEB","ANGI","ANGN","ANGO","ANIIl","ANIK","ANIP","ANIX","ANNX","ANPC","ANTE","ANTINp","ANTOl","ANTX","ANY","ANZU","AOGO","AOSL","AOUT","AOl","APAC","APAXl","APCX","APDN","APEI","APEN","APFl","API","APLD","APLS","APLSl","APLT","APMIU","APM","APOG","APOP","APPF","APPN","APPS","APP","APRE","APTDl","APTM","APTO","APTX","APVO","APWC","APXI","APXT","APYX","AQB","AQMS","AQSGl","AQST","AQU","AQWAl","AQWAm","AQWGl","ARAMIp","ARAV","ARAY","ARAl","ARBG","ARBK","ARCB","ARCC","ARCE","ARCK","ARCT","ARDS","ARDX","AREB","AREC","ARG1l","ARG3l","ARGEl","ARGSl","ARGX","ARGp","ARHS","ARIXl","ARIZ","ARK1l","ARK3l","ARKAl","ARKBl","ARKCl","ARKR","ARKSl","AROW","ARPO","ARQT","ARRW","ARRY","ARRl","ARTE","ARTL","ARTNA","ARTW","ARVN","ARW1l","ARW3l","ARWR","ARWSl","ARYA","ARYB","ARYD","ARYE","ASAIl","ASCA","ASCB","ASCIl","ASCLl","ASDVl","ASEIl","ASHMl","ASITl","ASLIl","ASLN","ASLl","ASM3l","ASMB","ASMEl","ASML","ASND","ASNS","ASOLp","ASO","ASPA","ASPC","ASPS","ASPU","ASPYl","ASRT","ASRV","ASTC","ASTE","ASTI","ASUR","ASYS","AT11l","AT1l","ATAI","ATAK","ATAT","ATCX","ATEC","ATEK","ATEX","ATEp","ATGl","ATHA","ATHE","ATHX","ATIF","ATLC","ATLO","ATMAl","ATNI","ATNX","ATOM","ATOS","ATOp","ATRA","ATRC","ATRI","ATRO","ATRl","ATSG","ATSTl","ATSl","ATTO","ATTl","ATVC","ATXG","ATXI","ATYl","AUBN","AUB","AUCOl","AUDC","AUEGl","AUGMl","AUGRp","AUGX","AUID","AUPH","AURA","AURC","AUTL","AVAC","AVAH","AVAPl","AVAV","AVBl","AVCO","AVCT","AVDL","AVDX","AVEO","AVGR","AVGRl","AVHI","AVID","AVIR","AVNW","AVONl","AVO","AVRO","AVTE","AVT","AVVl","AVXL","AWATp","AWEl","AWH","AWRE","AXDX","AXGN","AXGT","AXLA","AXNX","AXSM","AXSl","AXTI","AYLA","AYMl","AYRO","AYTU","AY","AZN","AZPN1","AZRX","AZYO","AZ","BA3Sl","BA3l","BAB2l","BAB3l","BABSl","BABl","BAESl","BAFN","BAFl","BAGl","BAINp","BAKKl","BBLG","BBM3l","BBSI","BBTRl","BBUSl","BBYl","BBp","BCAB","BCAC","BCAN","BCBP","BCDA","BCEL","BCGl","BCHNl","BCHNm","BCHSl","BCIl","BCLI","BCML","BCOGl","BCOMl","BCOR","BCOV","BCOW","BCPC","BCRX","BCS3l","BCSA","BCSSl","BCTG","BCTX","BCYC","BCYP","BDEVl","BDGE","BDSX","BDTX","BEAM","BEATT","BECN","BEEl","BELFA","BELFB","BENEl","BERIl","BERKl","BERMl","BEZl","BFC","BFIN","BFRI","BFST","BGCGl","BGCP","BGEOl","BGEUl","BGFDl","BGFV","BGLFl","BGNE","BGSCl","BGSl","BGUKl","BGXX","BHAC","BHAT","BHF","BHI","BHMGl","BHSE","BIAF","BID1l","BID3l","BIDU","BIDUl","BIFFl","BIGC","BIGl","BIIB","BILI","BIMI","BIMp","BIOC","BIOGl","BIOL","BIOS","BIOT","BIOTl","BIOX","BIRD","BIRG1l","BITF","BIUSl","BIVI","BJDX","BJRI","BKCC","BKCGl","BKCHl","BKCNl","BKGl","BKSC","BKYI","BLBD","BLBX","BLCM","BLEU","BLFS","BLFY","BLIN","BLI","BLKB","BLMN","BLNDl","BLNG","BLOKl","BLPH","BLPl","BLRX","BLTE","BLUE","BLU","BLVp","BLZE","BL","BMAQ","BMBL","BMDl","BMEA","BMEl","BMPGl","BMRA","BMRC","BMRG","BMRN","BMSl","BMVl","BMYl","BNCl","BNFT","BNIX","BNKRl","BNKSl","BNNR","BNOX","BNPp","BNRG","BNR","BNSO","BNTC","BNZLl","BNp","BOAS","BOCHHl","BOCN","BOKF","BOLT","BOLp","BON","BONp","BOOKl","BOOM","BOOTl","BOSC","BOTGl","BOTJ","BOTZl","BOTZm","BOWLl","BOXL","BOYl","BP","BP3Ll","BPAC","BPCRl","BPETl","BPMC","BPOP","BPRN","BPSl","BPTH","BPTS","BPTl","BRAC","BRAG","BRBYl","BRESl","BREZ","BRFH","BRFIl","BRGEl","BRICl","BRID","BRIGl","BRIV","BRK1l","BRK2l","BRKH","BRKL","BRKR","BRKS","BRLAl","BRLI","BRLT","BRNAl","BRNTl","BROG","BRPA","BRPM","BRP","BRQS","BRSCl","BRSH","BRT3l","BRTG1l","BRTUl","BRTX","BRWMl","BRY","BRZE","BSBK","BSCl","BSDl","BSET","BSFC","BSGA","BSGM","BSIFl","BSPE","BSQR","BSRR","BSRTl","BSVN","BSVl","BSY","BTAI","BTBD","BTBT","BTCS","BTCp","BTECl","BTEMl","BTNB","BTWN","BUGGl","BUGm","BULLl","BUMPl","BUOYl","BUSE","BUSXF","BUTl","BUYBl","BVCl","BVICl","BVIp","BVS","BVSl","BVTl","BVXV","BWAC","BWAQ","BWAY","BWB","BWC","BWEN","BWFG","BWMN","BWMX","BWNGl","BWSAl","BWV","BWYl","BXRX","BYFC","BYGl","BYITl","BYNO","BYRN","BYSI","BYTS","BZUN","BZ","C50Ul","CAAS","CABA","CACC","CAC","CADL","CAHC","CAKE","CALA","CALB","CALM","CALT","CALl","CAMP","CAMT","CAN","CAPA","CAPCl","CAPDl","CAPR","CAPUl","CAPp","CARB1l","CARBm","CARDl","CARE","CARG","CARPl","CARRl","CARV","CAR","CARl","CASA","CASH","CASHl","CASI","CASS","CASY","CATB","CATC","CATLl","CATS","CATY","CAUl","CAp","CBAN","CBAT","CBAY","CBDGp","CBDPl","CBDXl","CBFV","CBGl","CBIO","CBLI","CBNDl","CBNK","CBOTp","CBRG","CBRL","CBSH","CBS","CBTX","CBU7l","CBXl","CCAI","CCAP","CCBG","CCB","CCCC","CCCL","CCE","CCHl","CCJIl","CCNC","CCNE","CCOI","CCPGl","CCRN","CCRl","CCSI","CCTS","CDAK","CDAQ","CDFFl","CDIp","CDLX","CDLl","CDMO","CDNA","CDNS","CDTX","CDW","CDXC","CDXS","CDZI","CD","CEA1l","CEBGl","CECE","CEG","CELC","CELH","CELZ","CEMGl","CEMI","CENH","CENQ","CENTA","CENT","CENX","CERC","CERS","CERT","CESGl","CETX","CEU2l","CEUDm","CEVA","CEYl","CF1p","CFAC","CFBK","CFB","CFFA","CFFE","CFFI","CFFN","CFFS","CFII","CFIV","CFLT","CFMS","CFRX","CFSB","CFVI","CFV","CFYNl","CGBD","CGEM","CGEN","CGEOl","CGIX","CGIl","CGLl","CGNX","CGOl","CGRO","CGSl","CGTX","CGTl","CGWl","CG","CHCI","CHCO","CHDN","CHEA","CHEF","CHEK","CHFS","CHFW","CHFl","CHGBl","CHG","CHGl","CHI3l","CHINl","CHIPl","CHKK","CHKP","CHMG","CHNR","CHNSl","CHRGl","CHRS","CHRW","CHTR","CHUY","CHWA","CHX","CIBRl","CIDM","CIH","CIIG","CINC","CINF","CING","CISO","CIT2l","CITE","CITEl","CITSl","CIVB","CIZN","CIZl","CJJD","CKNl","CKPT","CLAQ","CLAR","CLAY","CLBK","CLBS","CLDNl","CLDX","CLEU","CLFD","CLGN","CLIGl","CLII","CLIR","CLIl","CLLS","CLMA","CLMP","CLNE","CLO6l","CLOE","CLOUm","CLOl","CLPS","CLPT","CLRB","CLRC","CLRO","CLSD","CLSK","CLSN","CLST","CLWT","CLXT","CLXl","CMBGl","CMBM","CMBUl","CMCA","CMCIl","CMCO","CMPS","CMPX","CMRSl","CMRX","CMTL","CNAl","CNCE","CNCTl","CNDT","CNDXl","CNET","CNEWl","CNEY","CNEl","CNFR","CNGL","CNNB","CNOB","CNSL","CNSP","CNTA","CNTB","CNTG","CNTQ","CNTX","CNTY","CNX1","CNXA","CNXC","CNXN","CNYAl","CO2Pl","CO2Ul","CO2l","COAl","COBRl","COCBl","COCO","COCOl","COCP","CODA","CODX","COFAp","COFFl","COFS","COFUl","COHU","COI1l","COIBl","COKE","COLB","COLL","COLM","COMFl","COMM","COMMl","COMS","COMXl","CON3l","CONN","CONX","COOL","COOP","COPAl","COPGl","COPLl","COPXl","CORDl","CORNl","CORPl","CORT","CORUl","COSM","COSTl","COSW2p","COTNl","COUKl","COUP","COVA","COVp","COWN","COYA","CP3El","CPAAA","CPAA","CPAQ","CPAR","CPGl","CPHC","CPIX","CPIl","CPJ1l","CPLP","CPN3l","CPNSl","CPOP","CPRT","CPRX","CPSH","CPSI","CPSS","CPST","CPTA","CPXJl","CRAI","CRBP","CRBU","CRCT","CRDAl","CRDO","CREC","CREG","CREIl","CRESY","CRESl","CREX","CRGE","CRGTl","CRHl","CRIS","CRKN","CRM2l","CRM3l","CRMD","CRMEl","CRMSl","CRMT","CRN1l","CRNC","CRNT","CRNX","CRON","CROPm","CROX","CRPSl","CRPUl","CRSA","CRSTl","CRTMl","CRTO","CRTPF","CRTX","CRU1l","CRUDl","CRUS","CRVL","CRVS","CRWS","CRZN","CS1l","CSBR","CSGP","CSGS","CSH2l","CSHl","CSII","CSLM","CSNl","CSP1","CSPI","CSSE","CSTE","CSTL","CSTR","CSWC","CSWI","CSX5l","CSX","CSp","CTECl","CTEGl","CTEKl","CTEKm","CTG","CTHR","CTIB","CTIC","CTKB","CTMX","CTOl","CTRN","CTSH","CTSO","CTXR","CTYl","CUEN","CUE","CUKXl","CULL","CUTR","CVAC","CVBF","CVCO","CVCY","CVGI","CVGW","CVLBD","CVLG","CVLT","CVLY","CVRX","CVV","CWBC","CWBR","CWCO","CWKl","CWST","CXADl","CXASl","CXDO","CYAD","CYAN","CYBAl","CYBGl","CYBPl","CYBR","CYBRl","CYBRm","CYCC","CYCN","CYGBl","CYN","CYNl","CYRN","CYRX","CYSEl","CYTH","CYTK","CYT","CZFS","CZNC","CZWI","DADA","DAGBl","DAIO","DAKT","DALS","DALl","DAPPl","DARE","DARKl","DATS","DAWN","DAX3l","DAXSl","DBDR","DBGI","DBTX","DBVT","DBX","DCBO","DCCl","DCPH","DCRB","DCRC","DCRD","DCRN","DCTH","DCT","DCl","DDI","DDMX","DDOG","DDV1l","DECA","DECp","DEEp","DEL2l","DEMl","DENN","DERM","DES2l","DEVCl","DEVl","DFDUl","DFEAl","DFEPl","DFEl","DFFN","DFHT","DFPH","DFSl","DGENl","DGEPl","DGHI","DGI9l","DGICA"]
not_avaliable = ["AGESL","BCHNM","ARYA","BYGL","ASPC","3TAIL","CLXL","2TSEL","BSRTL","SMTL","3LAML","AVHI","CGIL","3BIEL","BRESL","AIREL","BP3LL","UKDVL","3LDAP","DCCL","3MSEL","3FNPL","ARPO","3LINL","ALVMGP","CMBUL","3LPAP","AHTL","ASPA","2STRL","3STOP","3NGSL","AATGL","CPAAA","2MCLL","BVSL","ALAIL","3JDL","COSW2P","CARRL","CRN1L","BIMP","CYGBL","BRLAL","3AKEL","BPTL","3LSIL","3LIPL","CEU2L","3SWPL","3LNEL","3BCEL","LLOYL","3SAPL","BAINP","BYND1","AFP","3ABEL","BVIP","BRPA","BTECL","ALPHEP","3FTPL","COPXL","ALTOOP","COMXL","DECP","CYBGL","CIT2L","3SRIL","EQQQL","2OIGL","ASCLL","AAPSL","SHELL","2STRM","CIBRL","3USLL","DGEPL","CHIPL","3UKSL","CNYAL","DFSL","ATSTL","5SPEL","3OISL","AMDSL","CLMP","3BPEL","ADRO","CHFW","ALHGRP","CPST","ALDLTP","AGC","CCPGL","3SARP","ALODCP","CGSL","BWNGL","CRM3L","ASMEL","BUTL","3SBPL","EZJL","COBRL","BCOML","3CPNL","3LLLL","AUGX","ALBOOP","3ICEL","BAKKL","ALRIBP","CARPL","ARW1L","AT11L","3LFPL","3GDEL","3SAZL","AJGL","5SPYL","3PLTL","CF1P","BYITL","BNPP","CRU1L","CATLL","3KORL","VTIQ","BHI","ARKBL","ASAIL","CTYL","CMRSL","ARGSL","VWRLL","CTEKM","CGOL","ALDNEP","CS1L","BOAS","BAB2L","BCHSL","BIOGL","BLNDL","BVICL","3ZMEL","AUGML","BRSCL","CREIL","BKCGL","3SPEL","3LGSL","AMALL","CCCL","BOYL","IPOE","NAKD","CXADL","3LBC1L","BUGM","BCHNL","AEMUL","BNP","ALSA","3NGLL","ATMAL","3LAMP","CARB1L","ASLIL","3LPOM","DGENL","CNCTL","5CH6D","C50UL","DEAC","CSPX","CCIV","ACND","AZNL","3SXLL","3LUBL","AGEDL","OD7FD","BRT3L","ACEV","ALMDPP","ALPX","CBNDL","BKCHL","3KWBL","IMBL","AESE","3SMPL","3LFEL","3DXEL","ALVAPP","3LWPL","3LGPL","BGEUL","3SISL","BSGA","AVBL","ALML","CEA1L","3LEUL","IITU","AACQ","BWSAL","3BACL","APOP","BAB3L","AVL","CFFA","CRPSL","ANCN","AALL","2MXP","BID3L","AIR3L","AMAPL","ABBNSEQ","ALGAUP","DFPH","CCLL","VUSAL","3SVWP","BTCP","AGBPL","3XPEL","BRICL","BOCHHL","3HSEL","3SIPL","CCHL","ANTINP","COCOL","CPXJL","DBDR","3VTL","CRTML","3SALL","ALOKWP","AERSL","CLAQ","3SQEL","3SAMP","BRIGL","BCTG","BMEL","5HEDL","5TYSM","3LMPL","VFEML","AADVL","ALHGOP","BBM3L","AIAIL","ARIXL","CARL","CBS","3GOOL","LGENL","5BUSM","BRTG1L","3MREL","CON3L","CASHL","3SUEL","3SGLL","3S3PL","AGROL","BIGL","ADML","DAXSL","CITSL","BOCN","3LMOL","3SMOL","3LMIM","3LPEL","3JPNL","COAL","3SPAP","3KWEL","2TSLL","ALKALP","AAPLL","BOTGL","CNDXL","ASDVL","ARAMIP","3SSTP","3LUPL","AFMEP","3SSIL","3ROKL","CHNSL","3ARKL","CNEWL","ADPP","BCIL","3SGPL","3SFTL","BAGL","3SMDL","2UKLL","DFEAL","CYBRL","3SVEL","ABNSL","ALAGOP","BIRG1L","ACTC","CECE","ALHAFP","BPETL","3AIEL","DALL","UKWL","CRSTL","AVONL","3SLLL","VUAAL","3LTOP","AZRX","AHAC","CINEL","AGGBL","3SZPL","COIBL","3SNPL","CMCIL","3TSLL","COI1L","CROPM","BGSCL","CDFFL","CALT","AAFL","CCJIL","CO2PL","ATOP","AIGGL","AMZ3L","BWYL","COMML","APXI","BRNAL","CRDAL","ALUML","CAPP","JDWL","AMALM","3LPAL","3IBEL","IAGL","2OIGM","APTDL","3GMPL","ALIKOP","3SFPL","3LARP","3LVOL","CGEOL","3VWEL","BTEML","3LSQL","CNTQ","AIGOL","3SZNL","3LZPL","BPCRL","3AMZL","AMGOL","ALCRBP","CBXL","3BTLM","BSPE","HSBAL","3ADEL","MCP","BOOTL","BCOGL","ALVETP","3APEL","CBDGP","DEML","3SUBL","BTNB","3FNEL","ALAMAP","3AAPL","3SMTL","BCGL","IUKPL","CLOL","ALSPTP","ACAP","AOGO","ALAGL","3SFEL","3SSQL","3SNIL","CORUL","3SMEL","CRPUL","ALGWL","ASITL","ALNMRP","3PLUL","AJITL","CFAC","3ABNL","COOL","3SPOM","BID1L","3SPAL","3LORP","CTECL","CFV","3STPL","3SAAL","BEZL","INTUL","CORNL","ALFAL","3FTGL","CAPA","3HSBL","AMLL","CLIL","ABFL","3GISL","3QQQL","ALDP","ATRL","CSX5L","AXSL","3LALL","3NFEL","AIEL","ALBPSP","CYNL","ALACTP","ALYUL","3UBEL","ARAL","ALLGOP","ALHRSP","3EUSL","AVGRL","3ROEL","ALGBEP","CSP1","CXASL","3ARWL","ADIGL","3SFGL","CUKXL","BOTZM","3SLEL","3PYPL","BBUSL","BRGEL","3LNGL","COVP","3NVEL","3BBEL","3BLRL","APFL","3ZML","BRKS","CRM2L","BIDUL","3JETL","AASL","CPN3L","ARRL","3SMHL","AHPA","3STSL","ALTTUP","BRK2L","CRUDL","3LSQM","AEHA","CSH2L","3GOSL","CHFL","3XLFL","3LDEL","2MSFL","BRFIL","DAGBL","CFVI","CERC","BRK1L","CHGBL","ADGI","3SHPL","VHYLL","BGEOL","AL3SL","AAP3L","ATTL","CLIGL","3VWL","3LMSL","3PLEL","3BRLL","3LDOL","ASHML","CATB","3LSEP","CTEGL","BA3SL","CNEL","CPIL","CTOL","3TYLM","3LVPL","AMHC","3GILL","BDGE","3SPPM","ARTE","AAPEL","COTNL","3BAL","BGLFL","ALBIZP","BUOYL","3XLEL","5ESGL","AKER","3SAEL","CLBS","ALAUDP","3BPL","3IFEL","AQWAM","DFDUL","3SMZL","3LIL","CKNL","BRBYL","3AREL","ALDMSP","ASCA","CPTA","ABN1L","3STEL","CARDL","BSVL","3RDEL","3SBEL","3XEEL","HLNL","BENEL","DFEL","CLSN","COPLL","ALCAPP","BULLL","CSHL","3SLVL","3ULSL","ASPYL","3LMEL","AJBL","BMPGL","GSKL","INRGL","BEEL","CORPL","BRPM","3SSEP","CESGL","DAX3L","3SQL","ALMLBP","ARWSL","CHINL","3SNVL","AIRP","STHSL","ALENOP","COFFL","3CNEL","3S3EL","3OILL","3GFML","ATYL","3SGOL","3SAAM","2OIEL","AFAC","AQWAL","DAPPL","3LBPL","AZPN1","2MUEL","CYSEL","ALAIRP","3FTEL","3SOIL","ARGP","3SDAP","AMUNP","COUKL","BIFFL","2NVDL","3SSNP","2UBRL","AEGGL","2SZMM","ALBPKP","BNKSL","ATEP","ANDA","CLDNL","3CFLL","BSIFL","3LMIL","CIIC","COCBL","3SGEL","VGOVL","COPAL","3TYLL","ADER","BRWML","CO2L","CHWA","BTBD","ARBL","3GDXL","ARK3L","AMCII","CMBGL","BRNTL","COVA","BKCNL","3LPPL","ALHYPP","BBYL","AINV","ALNFLP","3SMOP","3MBGL","3VODL","FMCI","3S1PL","AMZNL","AEXL","AQSGL","3LCOM","ALAFYP","3JEEL","CHG","3BAEL","BOWLL","3LSAP","ADOM","BEATT","AMZSL","VUKEL","3SSQM","BSCL","AOL","AAP2L","3RDSL","BABSL","BUYBL","BMVL","TUIL","RBL","PMOL","3SBNP","ARK1L","ARG1L","3AIRL","ARBG","3LSTP","3LGLL","DEVCL","3SORP","3VDEL","3ASML","3LNIL","AEEEL","CAP","AEWUL","TSCOL","ANTOL","ASOLP","CEYL","BIOS","DFHT","3FNGL","3TAEL","CLOE","ARIZ","ARYB","BMSL","3SGGL","ALINNP","3LAAL","CRTX","3LIEL","APLSL","DDMX","RRL","BERKL","ALHPIP","ARGEL","OCDOL","BCSSL","ATVC","3SLVP","3DIEL","3CRML","AGEDM","CSLM","3AMDL","ACWDL","3SDOL","3LUS1L","3GMEL","3GLEL","3QQEL","3XPVL","CATS","CNX1","2STEL","CFSB","2NFLL","CO2UL","3SBCL","AUCOL","2UKSL","3SVPL","CPNSL","CHKK","ALTNL","AT1L","3LTSL","3SPYL","BRKH","ABNBL","BONP","DCRB","TLRY1","AGRUL","3IBBL","ACWIL","ADT1L","AMD3L","DCRC","BLEU","888L","ALHFP","AIGPL","CTEKL","3SRDL","CEUDM","3SMFL","3CHEL","CAUL","BDEVL","3SAML","AIGEL","3SILL","AEMCL","CLII","AWATP","3BABL","3MSFL","AIAIM","BSDL","3DAXL","RIOL","BTL","AUGRP","3SGFL","ATGL","AM3SL","BHSE","BBTRL","CFBK","AASIP","3SPOL","ALRPDP","3LGEL","CFII","3INL","ALWFP","3SSAP","COPGL","AASGL","CHGL","COSTL","ACPEL","AAP1L","3LAZL","COMFL","DFEPL","AQWGL","CSNL","APAXL","AIGLL","3DISL","3GOLL","2UBEL","3BIDL","AUEGL","CBTX","CBLI","BUMPL","COFUL","AAIFL","3DESL","BMYL","DGEL","BARCL","AURC","3LUEL","CHRGL","AMZEL","CGWL","DES2L","ACTD","CENH","CITEL","AGGGL","3LOIL","CRTPF","3SYEL","ECARL","BCYP","BLOKL","3LAPL","3TSEL","CRSA","COFAP","ALKEMP","3S2EL","3SBAL","3MRNL","3IFXL","ALCARP","3LTEL","3JPEL","ALOP","ALKEYP","3GLDL","CBU7L","CRGTL","BAFL","3LRIL","3LLVP","ATSL","3LAXP","BLPL","BIOTL","3BULM","APMIU","AERIL","3HCSL","2VISL","ALKKOP","3SEEL","3SSLL","DEVL","AACP","3LTPL","BGSL","3LSNP","CNAL","3USSL","AMZ1L","3SIEL","3AMEL","CWKL","CAPUL","BKGL","ASEIL","FPP","CEBGL","2TRVM","3LBNP","3LAEL","2OILL","DARKL","BVTL","CGLL","BIUSL","BUSXF","CRESL","3SAXP","BWAQ","3JDEL","3MBEL","AIRSL","3AKWL","CAPDL","ARW3L","AVCO","CRMEL","3SNEL","CIZL","2SZML","3EULL","DCL","ASM3L","3FBL","AFIN","ABN3L","ADVICP","BMDL","DDV1L","3LVWP","3SHEL","3SVO1L","3HCLL","CBOTP","CLMA","BMRG","ANIIL","ARKCL","RMGL","SGLNL","BNZLL","ABDL","ALICAP","FB","HITIF","AJAXL","AVVL","CPGL","3NIEL","AXGT","3S2PL","3CHIL","3TSML","3FBEL","CEMGL","3LZNL","DCRN","3VTEL","ARG3L","AIKI","CARBM","DEL2L","AWEL","AEETL","5QQEL","VODL","3SMIM","3GOEL","BLVP","AIBGL","AUBN","3SMSL","BPL","BGUKL","AIGSL","ALESEP","3LNPL","2PALL","3CREL","AYML","CBDPL","BNKRL","AIGCL","SSHYL","ALFL","PNNL","CYBPL","3LPPM","3LFBL","3UBRL","3NFLL","ALCWEP","BOOKL","3LRDL","BVCL","3ARGL","3LBA1L","CFYNL","BCS3L","3CONL","CLO6L","ARKSL","CSP","3LNFL","3UKLL","BGCGL","CPJ1L","SEMBL","BRTUL","BCAC","ALHEOP","AKEP","CDLL","CYBRM","BPSL","3S1EL","3PREL","ALBOAP","CRHL","AAAPL","ARKAL","3SDEL","ASCIL","3LMOP","3SRRL1","ALMICP","AIGAL","3STLL","3XFEL","ASLL","CRMSL","3PYEL","BATSL","CAHC","CGIX","CORDL","3LPOL","AMZ2L","3SNFL","CHI3L","AMRH","3LVEL","AMD2L","CYBAL","AEPL","3LNVL","3SKEL","VUSDL","3NVDL","BNCL","BUGGL","2STSL","CBDXL","CDIP","NETE","BGFDL","BOLP","BHMGL","APXT","3SBBL","3DELL","5QQQL","CAPCL","CGTL","AVAPL","2MUL","DGI9L","AELISP","ACUIF","BOTZL","3SMIL","BERIL","CCE","BAESL","3ICLL","ALEUPP","3TYSM","CP3EL","3SPPL","BA3L","3SUPL","ULVRL","AIGIL","CVLBD","3NIOL","AGRL","BERML","ALFREP","CCRL","AJOTL","3SFBL","CHFS","CGRO","CLOUM","ALKL","AAXN"]
new_tickers = [ticker.upper() for ticker in new_tickers]
not_avaliable = [ticker.upper() for ticker in not_avaliable]
tickers = list(set(new_tickers) - set(not_avaliable))
intervals = ["1m", "2m", "1h", "1d"]
